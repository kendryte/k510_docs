![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 AI 애플리케이션 가이드</font>**

<font face="黑体"  size=3>문서 버전: V1.0.0</font>

<font face="黑体"  size=3>게시 날짜: 2022-03-07</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**면책 조항**</font>
귀하가 구매한 제품, 서비스 또는 기능은 베이징 Jiananges 정보 기술 유한 회사(이하 "회사")의 상업 계약 및 약관의 적용을 받으며, 이 문서에 설명된 제품, 서비스 또는 기능의 전부 또는 일부는 구매 또는 사용의 범위를 벗어납니다. 계약에 달리 합의하지 않는 한, 회사는 본 문서의 진술, 정보, 내용의 정확성, 신뢰성, 완전성, 마케팅, 특정 목적 및 비침략성에 대해 명시적 또는 묵시적으로 어떠한 진술이나 보증도 하지 않습니다. 달리 합의하지 않는 한, 이 문서는 사용 지침으로만 추론됩니다.
이 문서의 내용은 제품 버전 업그레이드 또는 기타 이유로 인해 예고 없이 수시로 업데이트되거나 수정될 수 있습니다.

**<font face="黑体"  size=3>상표 고지</font>**

베이징 <img src="../zh/images/canaan-logo.png" style="zoom:33%;" />Jianan Jets 정보 기술 유한 공사의 상표는 Jianan, Jianan 및 Jianan의 다른 상표입니다. 이 문서에 언급될 수 있는 기타 모든 상표 또는 등록 상표는 해당 소유자가 소유합니다.

**<font face="黑体"  size=3>저작권 ©2022 베이징 Jiananjets 정보 기술 유한 회사</font>**
이 문서는 K510 플랫폼 개발 및 설계에만 적용되며, 어떠한 단위나 개인도 회사의 서면 허가 없이 이 문서의 일부 또는 전부를 어떤 형태로든 배포할 수 없습니다.

**<font face="黑体"  size=3>베이징 Jiananjets 정보 기술 유한 회사</font>**
웹 사이트: canaan-creative.com
비즈니스 문의: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# 서문
**<font face="黑体"  size=5>문서의 목적</font>**
이 문서는 엔지니어가 k510 AI 앱의 작성 및 적용을 이해할 수 있도록 설계된 K510 AI 애플리케이션을 위한 컴패니언 문서입니다.

**<font face="黑体"  size=5>독자 개체입니다</font>**

이 문서(이 가이드)가 주로 적용되는 사람:

- 소프트웨어 개발자
- 기술 지원 담당자

**<font face="黑体"  size=5>레코드를 수정합니다</font>**
 <font face="宋体"  size=2>개정 레코드에는 각 문서 업데이트에 대한 설명이 누적됩니다. 문서의 최신 버전에는 이전 버전의 모든 업데이트가 포함되어 있습니다. </font>

| 버전 번호입니다   | 수정자     | 개정일입니다 | 개정 지침 |
| :-----  |-------    |  ------ | ------  |
| V1.0.0  | AI 제품 부서  | 2022-03-07 |      |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>카탈로그</font>**

[목차]

<div style="page-break-after:always"></div>

# 1 소개

이 문서에서는 K510 AI 앱의 작성 및 적용에 대해 설명합니다. K510 AI 칩을 기반으로 하는 AI 애플리케이션 개발에는 여러 단계가 있습니다.

모델 준비: 학습된 모델을 PC에서 유효성을 검사하여(정적 이미지 추론을 사용하여) 모델이 올바른지 확인합니다

모델 생성: 학습된 모델을 nncase compiler를 사용하여 컴파일하여 kmodel을 생성합니다

모델 검증: 결과 kmodel은 nncase simulator를 사용하여 정밀도 검증을 수행합니다

AI 응용 프로그램 작성: 비디오/사진 읽기, 입력 전처리, 모델 추론, 모델 후처리를 완료합니다

AI 응용 프로그램 컴파일: 교차 컴파일 도구 체인을 사용하여 K510 AI 응용 프로그램의 컴파일을 완료합니다

배포 및 튜닝: 컴파일된 AI 애플리케이션을 K510 하드웨어 제품에 연결하고 실제 시나리오에서 기능을 조정합니다

K510 AI 칩에서 AI 애플리케이션 개발을 위한 전체 아키텍처는 다음과 같습니다.

![](../zh/images/ai_demo/image-ai-demo.png)

이 문서에서는 320x320 해상도의 YOLOV5s onnx 모델을 예로 들어 K510 AI 응용 프로그램의 전체 프로세스를 작성하고 적용하는 것을 보여 줍니다.

# 2 모델 준비

추론을 위한 YOLOV5s의 onnx 모델은 /docs/utils/AI_Application/aidemo_sdk/models/onnx 하위 디렉토리에 있습니다(파일이 없는 경우 [models를 다운로드하십시오](https://github.com/kendryte/k510_docs/releases/download/v1.5/models.tar.gz))  및 압축 해제), 정적 이미지는 /docs/utils/AI_Application/aidemo_sdk/examples/python_inference_on_PC/data 하위 디렉토리에 있고 스크립트는 /docs/utils/AI_Application/aidemo_sdk/examples/python_inference_on_PC 하위 디렉토리에 있습니다.

스크립트 명령 프롬프트에 따라 yolov5_image.py 스크립트를 실행하여 정적 그림의 추론 결과를 얻습니다. 출력 이미지의 감지 프레임이 올바른지 확인하여 모델의 정확성을 감지합니다.

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

# 3 모델 생성

모델 생성은 nncase compiler에 따라 달라지며 nncase compiler에 대한 특정 사용 규칙은[K510_nncase_Developer_Guides.md를 참조할 수 있습니다](./K510_nncase_Developer_Guides.md). YOLOV5s를 생성하는 kmodel 스크립트는 /docs/utils/AI_Application/aidemo_sdk/scripts 하위 디렉토리에 있습니다.

스크립트 명령 프롬프트에 따라 gen_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py 실행하여 해당 kmodel을 생성합니다.

```shell
usage: gen_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py [-h] [--target TARGET] [--dump_dir DUMP_DIR] [--onnx ONNX] [--kmodel KMODEL]

optional arguments:
  -h, --help           show this help message and exit
  --target TARGET      target to run
  --dump_dir DUMP_DIR  temp folder to dump
  --onnx ONNX          onnx model path
  --kmodel KMODEL      kendryte model path
```

CPU에서 전처리를 최소화하기 위해 스크립트의 컴파일 옵션은 다음과 같이 구성됩니다.

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

# 4 모델 유효성 검사

모델 유효성 검사는 nncase simulator에 따라 달라지며 nncase simulator에 대한 특정 사용 규칙은[K510_nncase_Developer_Guides.md를 참조할 수 있습니다](./K510_nncase_Developer_Guides.md). YOLOV5s의 kmodel 스크립트가 /docs/utils/AI_Application/aidemo_sdk/스크립트 하위 디렉토리에 있는지 확인합니다.

스크립트 명령 프롬프트에 따라 simu_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py 실행하여 해당 kmodel이 올바르게 생성되었는지 확인합니다.

```shell
usage: sim_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py [-h] [--onnx ONNX] [--kmodel KMODEL]

optional arguments:
  -h, --help       show this help message and exit
  --onnx ONNX      original model file
  --kmodel KMODEL  kmodel file
```

cosine similarity가 1에 가깝거나 같으면 생성된 kmodel이 올바른지 확인합니다.

```text
output 0 cosine similarity : 0.9999450445175171
output 1 cosine similarity : 0.9999403953552246
output 2 cosine similarity : 0.9999019503593445
```

# 5 AI 응용 프로그램을 작성합니다

모델 유효성 검사는 nncase runtime에 의존하며 nncase runtime에 대한 특정 사용 규칙은[K510_nncase_Developer_Guides.md를 참조할 수 있습니다](./K510_nncase_Developer_Guides.md). AI 애플리케이션 참조 `k510_buildroot/package/ai/code/object_detect`. 먼저 대상 검색 인스턴스를 만들고 kmodel 입력 및 출력에 공간을 할당해야 합니다.

```c++
objectDetect od(obj_thresh, nms_thresh, net_len, {valid_width, valid_height});
od.load_model(kmodel_path);  // load kmodel
od.prepare_memory();  // memory allocation
```

zero memory copy를 구현하려면 ISP 출력 주소를 kmodel 입력 주소와 연결합니다

```c++
// define cv::Mat for ai input
// padding offset is (valid_width - valid_height) / 2 * valid_width
cv::Mat rgb24_img_for_ai(net_len, net_len, CV_8UC3, od.virtual_addr_input[0] + (valid_width - valid_height) / 2 * valid_width);
```

ISP 출력의 너비와 높이를 구성합니다

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

ISP의 실제 출력 높이가 video_height_r ISP의 다른 채널 간의 높이 오프셋을 video_height 해당 비디오 프로필을 구성합니다

```json
"/dev/video5":{
    "video5_used":1,
    "video5_width":320,
    "video5_height":320,
    "video5_height_r":240,
    "video5_out_format":0
}
```

입력 및 출력 주소를 kmodel의 input_tensor 및 output_tensor 연결합니다

```c++
od.set_input(0);
od.set_output();
```

kmodel을 실행하고 출력을 얻고 후처리합니다

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

마지막으로 감지 상자가 OSD에 그려져 출력이 표시됩니다

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

# 6 AI 응용 프로그램을 컴파일합니다

교차 컴파일 도구 체인을 사용하면 AI 응용 프로그램 컴파일에 대한 특정 사용 규칙을 참조할 수 K510_SDK_Build_and_Burn_Guide[](./K510_SDK_Build_and_Burn_Guide.md).

**번역 면책 조항**  
고객의 편의를 위해 Canan은 AI 번역 프로그램을 사용하여 오류를 포함할 수 있는 여러 언어로 텍스트를 번역합니다. 당사는 제공된 번역의 정확성, 신뢰성 또는 적시성을 보장하지 않습니다. Canan은 번역된 정보의 정확성이나 신뢰성에 의존하여 발생하는 손실이나 손해에 대해 책임을 지지 않습니다. 언어 번역 간에 콘텐츠 차이가 있는 경우 중국어 간체 버전이 우선합니다.

번역 오류 또는 부정확한 문제를 신고하려면 이메일로 문의하시기 바랍니다.
