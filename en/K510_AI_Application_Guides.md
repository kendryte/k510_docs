![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 AI Application Guide</font>**

<font face="黑体"  size=3>Document version: V1.0.0</font>

<font face="黑体"  size=3>Published: 2022-03-07</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Disclaimer**</font>
The products, services or features you purchase shall be subject to the commercial contracts and terms of Beijing Canaan Jiesi Information Technology Co., Ltd. ("the Company", the same hereinafter), and all or part of the products, services or features described in this document may not be within the scope of your purchase or use. Except as otherwise agreed in the contract, the Company disclaims all representations or warranties, express or implied, as to the accuracy, reliability, completeness, marketing, specific purpose and non-aggression of any representations, information, or content of this document. Unless otherwise agreed, this document is provided solely as a guide to reasoning.
Due to product version upgrades or other reasons, the contents of this document may be updated or modified from time to time without any notice. 

**<font face="黑体"  size=3>Trademark Notices</font>**

""<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, "Canaan" icon, Canaan and other trademarks of Canaan and other trademarks of Canaan are trademarks of Beijing Canaan Jiesi Information Technology Co., Ltd. All other trademarks or registered trademarks that may be mentioned in this document are owned by their respective owners. 

**<font face="黑体"  size=3>Copyright ©2022 Beijing Canaan Jiesi Information Technology Co., Ltd</font>**
This document is only applicable to the development and design of the K510 platform, without the written permission of the company, no unit or individual may disseminate part or all of the content of this document in any form. 

**<font face="黑体"  size=3>Beijing Canaan Jiesi Information Technology Co., Ltd</font>**
URL: canaan-creative.com
Business Enquiries: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# preface
**<font face="黑体"  size=5>Document purpose</font>**
This document is a companion document for the K510 AI application and is designed to help engineers understand the writing and application of k510 AI applications. 

**<font face="黑体"  size=5>Reader Objects</font>**

The main people to whom this document (this guide) applies:

- Software developers
- Technical support personnel

**<font face="黑体"  size=5>Revision history</font>**
 <font face="宋体"  size=2>The revision history accumulates a description of each document update. The latest version of the document contains updates for all previous versions. </font>

| The version number   | Modified by     | Date of revision | Revision Notes |
| :-----  |-------    |  ------ | ------  |
| V1.0.0  | AI Products Division  | 2022-03-07 |      |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contents</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Introduction

This document describes the writing and application of K510 AI applications. Based on the K510 AI chip, AI application development has the following stages:

Model preparation: The trained model is validated on the PC side (static picture inference can be used) to ensure the correctness of the model

Model generation: The trained model is compiled using the nncase compiler to generate a kmodel

Model Validation: The generated kmodel is validated with precision using the nncase simulator

Write AI applications: complete video/image reading, input preprocessing, model inference, model post-processing

Compile AI applications: Use the cross-compilation toolchain to compile K510 AI applications

Deployment and co-commissioning: The compiled AI application is deployed to the K510 hardware product, and the functional co-debugging is carried out in the actual scenario

The overall architecture of AI application development on the K510 AI chip is shown in the following figure:

![](../zh/images/ai_demo/image-ai-demo.png)

This document will take the onnx model of 320x320 resolution YOLOV5s as an example to introduce the entire process of writing and applying K510 AI applications.

# 2 Model preparation

The onnx model for YOLOV5s for inference is located in the /docs/utils/AI_Application/aidemo_sdk/models/onnx subdirectory (download models if no files are available[](https://github.com/kendryte/k510_docs/releases/download/v1.5/models.tar.gz).)  and unzip), the static image is located in the /docs/utils/AI_Application/aidemo_sdk/examples/python_inference_on_PC/data subdirectory, and the script is located in the /docs/utils/AI_Application/aidemo_sdk/examples/python_inference_on_PC subdirectory. 

Follow the script command prompt to run the yolov5_image.py script to obtain the inference result of the static picture. Detect the correctness of the model by verifying that the detection box of the output picture is correct or not.

```shell
usage: yolov5_image.py [-h] [--image_path IMAGE_PATH]
                       [--image_out_path IMAGE_OUT_PATH]
                       [--onnx_path ONNX_PATH]
                       [--confidence_threshold CONFIDENCE_THRESHOLD]
                       [--nms_threshold NMS_THRESHOLD]

object detect

optional arguments:
  -h, --help            show this help message and exit
  --image_path IMAGE_PATH
                        input image path
  --image_out_path IMAGE_OUT_PATH
                        output image path
  --onnx_path ONNX_PATH
                        onnx model path
  --confidence_threshold CONFIDENCE_THRESHOLD
                        confidence_threshold
  --nms_threshold NMS_THRESHOLD
                        nms_threshold
```

# 3 Model generation

Model generation depends on the nncase compiler, and the specific rules for using the nncase compiler can be found[ K510_nncase_Developer_Guides.md](./K510_nncase_Developer_Guides.md). The script that generates the kmodel for YOLOV5s is located in the /docs/utils/AI_Application/aidemo_sdk/scripts subdirectory. 

At the command prompt of the script, run the gen_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py to generate the corresponding kmodel.

```shell
usage: gen_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py [-h] [--target TARGET] [--dump_dir DUMP_DIR] [--onnx ONNX] [--kmodel KMODEL]

optional arguments:
  -h, --help           show this help message and exit
  --target TARGET      target to run
  --dump_dir DUMP_DIR  temp folder to dump
  --onnx ONNX          onnx model path
  --kmodel KMODEL      kendryte model path
```

It should be noted that in order to minimize preprocessing on the CPU, the compilation options in the script are configured as follows:

```python
compile_options.input_type = 'uint8'
compile_options.preprocess = True
compile_options.input_layout = 'NCHW'
compile_options.output_layout = 'NHWC'
compile_options.input_shape = [1, 3, 320, 320]
compile_options.mean = [0, 0, 0]
compile_options.std = [255, 255, 255]
compile_options.input_range = [0, 255]
```

# 4 Model validation

Model validation depends on nncase simulator, and the specific rules for using nncase simulator can be found[ in K510_nncase_Developer_Guides.md](./K510_nncase_Developer_Guides.md). Verify that yolov5s' kmodel script is located in the /docs/utils/AI_Application/aidemo_sdk/scripts subdirectory. 

At the script command prompt, run simu_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py to verify that the corresponding kmodel is generated correctly.

```shell
usage: sim_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py [-h] [--onnx ONNX] [--kmodel KMODEL]

optional arguments:
  -h, --help       show this help message and exit
  --onnx ONNX      original model file
  --kmodel KMODEL  kmodel file
```

If the cosine similarity is close to 1 or equal to 1, the correctness of the generated kmodel is ensured.

```text
output 0 cosine similarity : 0.9999450445175171
output 1 cosine similarity : 0.9999403953552246
output 2 cosine similarity : 0.9999019503593445
```

# 5 Write AI applications

Model validation depends on the nncase runtime, and the specific rules for using the nncase runtime can be found[ K510_nncase_Developer_Guides.md](./K510_nncase_Developer_Guides.md). AI Application Reference`k510_buildroot/package/ai/code/object_detect`. First, you need to create an object detection instance and allocate space for the kmodel input and output. 

```c++
objectDetect od(obj_thresh, nms_thresh, net_len, {valid_width, valid_height});
od.load_model(kmodel_path);  // load kmodel
od.prepare_memory();  // memory allocation
```

To implement zero memory copy, associate the ISP output address with the kmodel input address

```c++
// define cv::Mat for ai input
// padding offset is (valid_width - valid_height) / 2 * valid_width
cv::Mat rgb24_img_for_ai(net_len, net_len, CV_8UC3, od.virtual_addr_input[0] + (valid_width - valid_height) / 2 * valid_width);
```

Configures the width and height of the ISP output

```c++
 /****fixed operation for video operation****/
 mtx.lock();
 cv::VideoCapture capture;
 capture.open(5);
 // video setting
 capture.set(cv::CAP_PROP_CONVERT_RGB, 0);
 capture.set(cv::CAP_PROP_FRAME_WIDTH, net_len);
 capture.set(cv::CAP_PROP_FRAME_HEIGHT, net_len);
 // RRRRRR....GGGGGGG....BBBBBB, CHW
 capture.set(cv::CAP_PROP_FOURCC, V4L2_PIX_FMT_RGB24);
 mtx.unlock();
```

Configure the appropriate video configuration file, video_height_r the true output height of the ISP, and the video_height the height offset between the different channels of the ISP

```json
"/dev/video5":{
    "video5_used":1,
    "video5_width":320,
    "video5_height":320,
    "video5_height_r":240,
    "video5_out_format":0
}
```

Associate the input and output addresses with the input_tensor and output_tensor of the kmodel

```c++
od.set_input(0);
od.set_output();
```

Run the kmodel, get the output result, and perform post-processing

```c++
{
    ScopedTiming st("od run", enable_profile);
    od.run();
}

{
    ScopedTiming st("od get output", enable_profile);
    od.get_output();
}
std::vector<BoxInfo> result;
{
    ScopedTiming st("post process", enable_profile);
    od.post_process(result);
}
```

Finally, draw the detection box on the OSD to display the output

```c++
{
    ScopedTiming st("draw osd", enable_profile);
    obj_cnt = 0;
        for (auto r : result)
        {
        if (obj_cnt < 32)
        {
            struct vo_draw_frame frame;
            frame.crtc_id = drm_dev.crtc_id;
            frame.draw_en = 1;
            frame.frame_num = obj_cnt;
            frame.line_y_start = r.x2 * DRM_INPUT_WIDTH / valid_width;
            frame.line_x_start = r.x1 * DRM_INPUT_WIDTH / valid_width;
            frame.line_x_end = r.y1 * DRM_INPUT_HEIGHT / valid_height + DRM_OFFSET_HEIGHT;
            frame.line_y_end = r.y2 * DRM_INPUT_HEIGHT / valid_height + DRM_OFFSET_HEIGHT;
            draw_frame(&frame);

            cv::Point origin;
            origin.x = (int)(r.x1 * DRM_INPUT_WIDTH / valid_width);
            origin.y = (int)(r.y1 * DRM_INPUT_HEIGHT / valid_height + 10);
            std::string text = od.labels[r.label] + ":" + std::to_string(round(r.score * 100) / 100.0).substr(0,4);
            cv::putText(img_argb, text, origin, cv::FONT_HERSHEY_COMPLEX, 1.5, cv::Scalar(0, 0, 255, 255), 1, 8, 0);
        }
        obj_cnt += 1;
    }
}
```

# 6 Compile AI applications

Using the cross-compilation toolchain, the specific rules for the compilation of AI applications can be referred to[ K510_SDK_Build_and_Burn_Guide](./K510_SDK_Build_and_Burn_Guide.md). 

**Translation Disclaimer**  
For the convenience of customers, Canaan uses an AI translator to translate text into multiple languages, which may contain errors. We do not guarantee the accuracy, reliability or timeliness of the translations provided. Canaan shall not be liable for any loss or damage caused by reliance on the accuracy or reliability of the translated information. If there is a content difference between the translations in different languages, the Chinese Simplified version shall prevail. 

If you would like to report a translation error or inaccuracy, please feel free to contact us by mail.