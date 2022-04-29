import numpy as np

def xywh2xyxy(x):
    y = np.zeros_like(x)
    y[:, 0] = x[:, 0] - x[:, 2] / 2
    y[:, 1] = x[:, 1] - x[:, 3] / 2
    y[:, 2] = x[:, 0] + x[:, 2] / 2
    y[:, 3] = x[:, 1] + x[:, 3] / 2
    return y

def bbox_iou(box1, box2, x1y1x2y2=True, GIoU=False):
    box2 = np.transpose(box2,[1,0])

    if x1y1x2y2:
        b1_x1, b1_y1, b1_x2, b1_y2 = box1[0], box1[1], box1[2], box1[3]
        b2_x1, b2_y1, b2_x2, b2_y2 = box2[0,:], box2[1,:], box2[2,:], box2[3,:]
    else:
        b1_x1, b1_x2 = box1[0] - box1[2] / 2, box1[0] + box1[2] / 2
        b1_y1, b1_y2 = box1[1] - box1[3] / 2, box1[1] + box1[3] / 2
        b2_x1, b2_x2 = box2[0,:] - box2[2,:] / 2, box2[0,:] + box2[2,:] / 2
        b2_y1, b2_y2 = box2[1,:] - box2[3,:] / 2, box2[1,:] + box2[3,:] / 2

    inter_area = np.clip(np.minimum(b1_x2, b2_x2) - np.maximum(b1_x1, b2_x1), 0, 100000)* \
                 np.clip(np.minimum(b1_y2, b2_y2) - np.maximum(b1_y1, b2_y1), 0, 100000)

    union_area = ((b1_x2 - b1_x1) * (b1_y2 - b1_y1) + 1e-16) + \
                 (b2_x2 - b2_x1) * (b2_y2 - b2_y1) - inter_area

    iou = inter_area / union_area  # iou
    if GIoU:
        c_x1, c_x2 = np.minimum(b1_x1, b2_x1), np.maximum(b1_x2, b2_x2)
        c_y1, c_y2 = np.minimum(b1_y1, b2_y1), np.maximum(b1_y2, b2_y2)
        c_area = (c_x2 - c_x1) * (c_y2 - c_y1)  # convex area
        return iou - (c_area - union_area) / c_area  # GIoU

    return iou

def non_max_suppression(class_score, loc, conf_thres=0.5, nms_thres=0.5, nms_style = 'MERGE' ):
    output = [None]
    class_conf = class_score.max(axis=1)
    valid_index = (class_conf > conf_thres) & np.isfinite(loc).all(axis=1) & np.isfinite(class_score).all(axis=1)
    if np.sum(valid_index) == 0:
        return output
    class_conf = class_conf[valid_index]
    valid_score = class_score[valid_index]
    class_pred = np.argmax(valid_score, axis=1)
    valid_loc = loc[valid_index]
    valid_loc = xywh2xyxy(valid_loc)
    pred = np.concatenate([valid_loc, np.expand_dims(class_conf, 1), np.expand_dims(class_pred, 1)], axis=1)
    pred = pred[(-pred[:, 4]).argsort()]
    det_max = []
    for c in np.unique(pred[:, -1]):
        dc = pred[pred[:, -1] == c]
        n = len(dc)
        if n == 1:
            det_max.append(dc)
            continue
        elif n > 100:
            dc = dc[:100]

        if nms_style == 'OR':
            while dc.shape[0]:
                det_max.append(dc[:1])
                if len(dc) == 1:
                    break
                iou = bbox_iou(dc[0], dc[1:])
                dc = dc[1:][iou < nms_thres]

        elif nms_style == 'AND':
            while len(dc) > 1:
                iou = bbox_iou(dc[0], dc[1:])
                if iou.max() > 0.5:
                    det_max.append(dc[:1])
                dc = dc[1:][iou < nms_thres]

        elif nms_style == 'MERGE':
            while len(dc):
                if len(dc) == 1:
                    det_max.append(dc)
                    break
                i = bbox_iou(dc[0], dc) > nms_thres
                weights = dc[i, 4:5]
                dc[0, :4] = (weights * dc[i, :4]).sum(0) / weights.sum()
                det_max.append(dc[:1])
                dc = dc[i == 0]

        elif nms_style == 'SOFT':
            sigma = 0.5
            while len(dc):
                if len(dc) == 1:
                    det_max.append(dc)
                    break
                det_max.append(dc[:1])
                iou = bbox_iou(dc[0], dc[1:])
                dc = dc[1:]
                dc[:, 4] *= np.exp(-iou ** 2 / sigma)
                dc = dc[dc[:, 4] > nms_thres]

    if len(det_max):
        det_max = np.concatenate(det_max)
        output = det_max[(-det_max[:, 4]).argsort()]

    return output

def clip_coords(boxes, img_shape):
    boxes[:, [0, 2]] = np.clip(boxes[:, [0, 2]], 0, img_shape[1])
    boxes[:, [1, 3]] = np.clip(boxes[:, [1, 3]], 0, img_shape[0])
    return boxes

def scale_coords(img1_shape, coords, img0_shape):
    coords[:, [0, 2]] *= img1_shape[1]
    coords[:, [1, 3]] *= img1_shape[0]
    gain = max(img1_shape) / max(img0_shape)
    coords[:, [0, 2]] -= (img1_shape[1] - img0_shape[1] * gain) / 2
    coords[:, [1, 3]] -= (img1_shape[0] - img0_shape[0] * gain) / 2
    coords[:, :4] /= gain
    clip_coords(coords, img0_shape)
    return coords

def _sigmoid(x):
    return 1. / (1. + np.exp(-x))


def decode_netout(netout, net_len, anchors, loc, class_score):
    netout = np.transpose(netout, [0, 2, 3, 1])
    nb_box, grid_h, grid_w,  = netout.shape[:3]
    netout[..., 4] = (netout[..., 4])
    netout[..., 5:] = netout[..., 4][..., np.newaxis] * (netout[..., 5:])
    for b in range(nb_box):
        for row in range(grid_h):
            for col in range(grid_w):
                classes = netout[b, row, col, 5:]
                if np.sum(classes) > 0.0:
                    x, y, w, h = netout[b, row, col, :4]
                    x = ((x) * 2 - 0.5 + col) / grid_w
                    y = ((y) * 2 - 0.5 + row) / grid_h
                    w = anchors[2 * b + 0] * (((w) * 2) ** 2) / net_len
                    h = anchors[2 * b + 1] * (((h) * 2) ** 2) / net_len
                    loc.append([x, y, w, h])
                    class_score.append(classes)