![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 人工智慧應用指南</font>**

<font face="黑体"  size=3>文件版本：V1.0.0</font>

<font face="黑体"  size=3>發佈日期：2022-03-07</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**免責聲明**</font>
您購買的產品、服務或特性等應受北京嘉楠捷思資訊技術有限公司（“本公司”，下同）商業合同和條款的約束，本文檔中描述的全部或部分產品、服務或特性可能不在您的購買或使用範圍之內。 除非合同另有約定，本公司不對本文檔的任何陳述、資訊、內容的準確性、可靠性、完整性、行銷型、特定目的性和非侵略性提供任何明示或默示的聲明或保證。 除非另有約定，本文檔僅作為使用指導的推理。
由於產品版本升級或其他原因，本文檔內容將可能在未經任何通知的情況下，不定期進行更新或修改。

**<font face="黑体"  size=3>商標聲明</font>**

“<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />”、“Canaan”圖示、嘉楠和嘉楠其他商標均為北京嘉楠捷思資訊技術有限公司的商標。 本文檔可能提及的其他所有商標或註冊商標，由各自的所有人擁有。

**<font face="黑体"  size=3>版權所有©2022北京嘉楠捷思資訊技術有限公司</font>**
本文檔僅適用K510平台開發設計，非經本公司書面許可，任何單位和個人不得以任何形式對本文檔的部分或全部內容傳播。

**<font face="黑体"  size=3>北京嘉楠捷思資訊技術有限公司</font>**
網址：canaan-creative.com
商務垂詢：salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# 前言
**<font face="黑体"  size=5>文件目的</font>**
本文檔為K510 AI 應用的配套文檔，旨在幫助工程師瞭解 k510 AI 應用的編寫與應用。

**<font face="黑体"  size=5>讀者物件</font>**

本文檔（本指南）主要適用的人員：

- 軟體開發人員
- 技術支持人員

**<font face="黑体"  size=5>修訂記錄</font>**
 <font face="宋体"  size=2>修訂記錄累積了每次文檔更新的說明。 最新版本的文件包含以前所有版本的更新內容。 </font>

| 版本號   | 修改者     | 修訂日期 | 修訂說明 |
| :-----  |-------    |  ------ | ------  |
| 1.0.0 版  | AI 產品部  | 2022-03-07 |      |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>目 錄</font>**

[目錄]

<div style="page-break-after:always"></div>

# 1 簡介

本文檔介紹K510 AI應用的編寫與應用。 基於K510 AI晶元進行AI應用開發共有如下幾個階段：

模型準備：將訓練好的模型在PC端進行驗證（可使用靜態圖片推理），以確保模型的正確性

模型生成：將訓練好的模型使用nncase compiler進行編譯，生成kmodel

模型驗證：將生成的kmodel使用nncase simulator進行精度驗證

編寫AI 應用程式：完成視頻/圖片的讀取、輸入的預處理、模型推理、模型後處理

編譯AI 應用程式：使用交叉編譯工具鏈，完成K510 AI應用程式的編譯

部署和聯調：將編譯好的AI 應用署到K510硬體產品上，並在實際場景中進行功能的聯調

在K510 AI晶片上進行AI應用開發的整體架構如下圖所示：

![](../zh/images/ai_demo/image-ai-demo.png)

本文檔將以320x320解析度的YOLOV5s的onnx模型為示例，介紹K510 AI應用整個流程的編寫與應用。

# 2 模型準備

用於推理的YOLOV5s的onnx模型位於/docs/utils/AI_Application/aidemo_sdk/models/onnx子目錄（如果沒有檔請下載 [models](https://github.com/kendryte/k510_docs/releases/download/v1.5/models.tar.gz)  並解壓），靜態圖片位於/docs/utils/AI_Application/aidemo_sdk/examples/python_inference_on_PC/data子目錄，腳本位於/docs/utils/AI_Application/aidemo_sdk/examples/python_inference_on_PC子目錄。

按照腳本命令提示，運行yolov5_image.py腳本，得到靜態圖片的推理結果。 通過驗證輸出圖片的檢測框正確與否來檢測模型的正確性。

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

# 3 模型生成

模型生成依賴於nncase compiler，關於nncase compiler的具體使用規則可參考[K510_nncase_Developer_Guides.md](./K510_nncase_Developer_Guides.md)。 生成YOLOV5s的kmodel的腳本位於/docs/utils/AI_Application/aidemo_sdk/scripts子目錄。

按照腳本命令提示，運行gen_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py，可生成相應的kmodel。

```shell
usage: gen_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py [-h] [--target TARGET] [--dump_dir DUMP_DIR] [--onnx ONNX] [--kmodel KMODEL]

optional arguments:
  -h, --help           show this help message and exit
  --target TARGET      target to run
  --dump_dir DUMP_DIR  temp folder to dump
  --onnx ONNX          onnx model path
  --kmodel KMODEL      kendryte model path
```

需要注意的是，為了盡可能減少在CPU上做預處理，腳本中的編譯選項配置如下：

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

# 4 模型驗證

模型驗證依賴於nncase simulator，關於nncase simulator的具體使用規則可參考[K510_nncase_Developer_Guides.md](./K510_nncase_Developer_Guides.md)。 驗證YOLOV5s的kmodel腳本位於/docs/utils/AI_Application/aidemo_sdk/scripts子目錄。

按照腳本命令提示，運行simu_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py，可驗證相應的kmodel是否生成正確。

```shell
usage: sim_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py [-h] [--onnx ONNX] [--kmodel KMODEL]

optional arguments:
  -h, --help       show this help message and exit
  --onnx ONNX      original model file
  --kmodel KMODEL  kmodel file
```

如有cosine similarity接近與1或者等於1，則可確保生成的kmodel的正確性。

```text
output 0 cosine similarity : 0.9999450445175171
output 1 cosine similarity : 0.9999403953552246
output 2 cosine similarity : 0.9999019503593445
```

# 5 編寫AI 應用程式

模型驗證依賴於nncase runtime，關於nncase runtime的具體使用規則可參考[K510_nncase_Developer_Guides.md](./K510_nncase_Developer_Guides.md)。 AI 應用程式參考 `k510_buildroot/package/ai/code/object_detect`。 首先需要創建目標檢測實例，併為kmodel輸入輸出分配空間。

```c++
objectDetect od(obj_thresh, nms_thresh, net_len, {valid_width, valid_height});
od.load_model(kmodel_path);  // load kmodel
od.prepare_memory();  // memory allocation
```

為實現zero memory copy，將ISP輸出位址與kmodel輸入地址關聯

```c++
// define cv::Mat for ai input
// padding offset is (valid_width - valid_height) / 2 * valid_width
cv::Mat rgb24_img_for_ai(net_len, net_len, CV_8UC3, od.virtual_addr_input[0] + (valid_width - valid_height) / 2 * valid_width);
```

配置ISP輸出的寬高

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

配置相應的video配置檔，video_height_r為ISP真實輸出高度，video_height為ISP不同通道間的高度偏移

```json
"/dev/video5":{
    "video5_used":1,
    "video5_width":320,
    "video5_height":320,
    "video5_height_r":240,
    "video5_out_format":0
}
```

將輸入輸出位址與kmodel的input_tensor和output_tensor關聯

```c++
od.set_input(0);
od.set_output();
```

運行kmodel，得到輸出結果，並進行後處理

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

最終，將檢測框畫到OSD上，顯示輸出

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

# 6 編譯AI應用程式

使用交叉編譯工具鏈，關於AI應用程式的編譯的具體使用規則可參考[K510_SDK_Build_and_Burn_Guide](./K510_SDK_Build_and_Burn_Guide.md)。

**翻譯免責聲明**  
為方便客戶，Canaan 使用 AI 翻譯程式將文字翻譯為多種語言，它可能包含錯誤。 我們不保證提供的譯文的準確性、可靠性或時效性。 對於因依賴已翻譯信息的準確性或可靠性而造成的任何損失或損害，Canaan 概不負責。 如果不同語言翻譯之間存在內容差異，以簡體中文版本為準。

如果您要報告翻譯錯誤或不準確的問題，歡迎通過郵件與我們聯繫。
