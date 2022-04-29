# -*- coding:utf-8 -*-
import argparse
import numpy as np
import cv2
from box_utils import non_max_suppression, scale_coords, decode_netout
import onnxruntime as ort
from numpy import random
anchors = [[10,13, 16,30, 33,23], [30,61, 62,45, 59,119], [116,90, 156,198, 373,326]]

def letterbox(img, new_shape, color, mode):
    shape = img.shape[:2]

    if isinstance(new_shape, int):
        ratio = float(new_shape) / max(shape)
    else:
        ratio = max(new_shape) / max(shape)
    ratiow, ratioh = ratio, ratio
    new_unpad = (int(round(shape[1] * ratio)), int(round(shape[0] * ratio)))


    if mode is 'auto':
        dw = np.mod(new_shape - new_unpad[0], 32) / 2
        dh = np.mod(new_shape - new_unpad[1], 32) / 2
    elif mode is 'square':
        dw = (new_shape - new_unpad[0]) / 2
        dh = (new_shape - new_unpad[1]) / 2
    elif mode is 'rect':
        dw = (new_shape[1] - new_unpad[0]) / 2
        dh = (new_shape[0] - new_unpad[1]) / 2
    elif mode is 'scaleFill':
        dw, dh = 0.0, 0.0
        new_unpad = (new_shape, new_shape)
        ratiow, ratioh = new_shape / shape[1], new_shape / shape[0]

    if shape[::-1] != new_unpad:
        img = cv2.resize(img, new_unpad, interpolation=cv2.INTER_AREA)  # INTER_AREA is better, INTER_LINEAR is faster
    top, bottom = int(round(dh - 0.1)), int(round(dh + 0.1))
    left, right = int(round(dw - 0.1)), int(round(dw + 0.1))
    img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)  # add border
    return img, ratiow, ratioh, dw, dh

def find_object_in_image(img, od_input_name, od_output_name, od_ort_session):
    img, _, _, _, _ = letterbox(img, new_shape=320, color=(114, 114, 114), mode='square')
    img = img[:, :, ::-1].transpose(2, 0, 1)
    img = np.ascontiguousarray(img, dtype=np.float32)  # uint8 to fp32
    img /= 255.0  # 0 - 255 to 0.0 - 1.0
    dst = od_ort_session.run(od_output_name, {od_input_name: np.expand_dims(img, 0)})
    return dst

parser = argparse.ArgumentParser(description='object detect')
parser.add_argument('--image_path', default='./data/bus.jpg', help='input image path')
parser.add_argument('--image_out_path', default='./data/bus_out.jpg', help='output image path')
parser.add_argument('--onnx_path', default='../../models/onnx/yolov5s_320_sigmoid.onnx', help='onnx model path')
parser.add_argument('--confidence_threshold', default=0.5, type=float, help='confidence_threshold')
parser.add_argument('--nms_threshold', default=0.45, type=float, help='nms_threshold')
args = parser.parse_args()

if __name__ == '__main__':
    colors = [[random.randint(0, 255) for _ in range(3)] for _ in range(80)]
    od_onnx_path = args.onnx_path
    # net and model
    od_ort_session = ort.InferenceSession(od_onnx_path)
    od_input_name = od_ort_session.get_inputs()[0].name
    od_output_name = [o.name for o in od_ort_session.get_outputs()]

    img_raw = cv2.imread(args.image_path)
    orig_image = img_raw.copy()
    dst = find_object_in_image(img_raw, od_input_name, od_output_name, od_ort_session)
    class_score = []
    loc = []
    for _i in range(3):
        decode_data = dst[_i][0]
        decode_netout(np.reshape(decode_data, [3, -1, dst[_i].shape[2], dst[_i].shape[3]]), 320, anchors[_i], loc, class_score)
    dets = non_max_suppression(np.array(class_score), np.array(loc), args.confidence_threshold, args.nms_threshold, 'OR')
    dets = scale_coords((320, 320), dets, img_raw.shape)
    for _i, b in enumerate(dets):
        b = list(map(int, b))
        color = colors[int(b[5])]
        cv2.rectangle(orig_image, (b[0], b[1]), (b[2], b[3]), color, 2)
    cv2.imwrite(args.image_out_path, orig_image)

