![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 AI — przewodnik po aplikacjach</font>**

<font face="黑体"  size=3>Wersja dokumentu: V1.0.0</font>

<font face="黑体"  size=3>Opublikowano: 2022-03-07</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Zrzeczenie się**</font>
Zakupione produkty, usługi lub funkcje podlegają umowom handlowym i warunkom Beijing Canaan Jiesi Information Technology Co., Ltd. ("Spółka", ta sama poniżej), a wszystkie lub część produktów, usług lub funkcji opisanych w niniejszym dokumencie może nie być objęta zakresem zakupu lub użytkowania. O ile nie uzgodniono inaczej w umowie, Firma zrzeka się wszelkich oświadczeń lub gwarancji, wyraźnych lub dorozumianych, co do dokładności, niezawodności, kompletności, marketingu, konkretnego celu i nieagresji jakichkolwiek oświadczeń, informacji lub treści tego dokumentu. O ile nie uzgodniono inaczej, niniejszy dokument jest dostarczany wyłącznie jako wskazówka do rozumowania.
Ze względu na aktualizacje wersji produktu lub z innych powodów zawartość tego dokumentu może być od czasu do czasu aktualizowana lub modyfikowana bez powiadomienia. 

**<font face="黑体"  size=3>Informacje o znakach towarowych</font>**

""<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, ikona "Canaan", Canaan i inne znaki towarowe Canaan oraz inne znaki towarowe Canaan są znakami towarowymi Beijing Canaan Jiesi Information Technology Co., Ltd. Wszystkie inne znaki towarowe lub zarejestrowane znaki towarowe, które mogą być wymienione w niniejszym dokumencie, są własnością ich odpowiednich właścicieli. 

**<font face="黑体"  size=3>Prawa autorskie ©2022 Beijing Canaan Jiesi Information Technology Co., Ltd</font>**
Niniejszy dokument ma zastosowanie wyłącznie do rozwoju i projektowania platformy K510, bez pisemnej zgody firmy, żadna jednostka ani osoba fizyczna nie może rozpowszechniać części lub całości treści tego dokumentu w jakiejkolwiek formie. 

**<font face="黑体"  size=3>Pekin Canaan Jiesi Information Technology Co Ltd</font>**
Adres internetowy: canaan-creative.com
Zapytania biznesowe: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# przedmowa
**<font face="黑体"  size=5>Przeznaczenie </font>**dokumentu
Ten dokument jest dokumentem towarzyszącym aplikacji K510 AI i ma na celu pomóc inżynierom zrozumieć pisanie i zastosowanie aplikacji K510 AI. 

**<font face="黑体"  size=5>Obiekty programu Reader</font>**

Główne osoby, których dotyczy ten dokument (ten przewodnik):

- Programiści
- Personel wsparcia technicznego

**<font face="黑体"  size=5>Historia</font>**
 zmian <font face="宋体"  size=2>Historia zmian gromadzi opis każdej aktualizacji dokumentu. Najnowsza wersja dokumentu zawiera aktualizacje dla wszystkich poprzednich wersji. </font>

| Numer wersji   | Zmodyfikowane przez     | Data aktualizacji | Uwagi do poprawek |
| :-----  |-------    |  ------ | ------  |
| Wersja 1.0.0  | Dział Produktów AI  | 2022-03-07 |      |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Treść</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Wstęp

W niniejszym dokumencie opisano pisanie i stosowanie aplikacji K510 AI. W oparciu o układ AI K510, tworzenie aplikacji AI ma następujące etapy:

Przygotowanie modelu: Wyszkolony model jest walidowany po stronie komputera (można użyć statycznego wnioskowania obrazu) w celu zapewnienia poprawności modelu

Generowanie modelu: Wyszkolony model jest kompilowany przy użyciu kompilatora nncase w celu wygenerowania kmodel

Walidacja modelu: Wygenerowany kmodel jest dokładnie weryfikowany przy użyciu symulatora nncase

Pisanie aplikacji AI: pełny odczyt wideo / obrazu, wstępne przetwarzanie danych wejściowych, wnioskowanie modelu, przetwarzanie końcowe modelu

Kompiluj aplikacje AI: Użyj łańcucha narzędzi kompilacji krzyżowej, aby skompilować aplikacje AI K510

Wdrażanie i współzasyłanie: Skompilowana aplikacja AI jest wdrażana w produkcie sprzętowym K510, a funkcjonalne współdebugowanie odbywa się w rzeczywistym scenariuszu

Ogólną architekturę tworzenia aplikacji AI na chipie K510 AI pokazano na poniższym rysunku:

![](../zh/images/ai_demo/image-ai-demo.png)

W tym dokumencie weźmiemy model onnx o rozdzielczości 320x320 YOLOV5s jako przykład, aby wprowadzić cały proces pisania i stosowania aplikacji K510 AI.

# 2 Przygotowanie modelu

Model onnx dla YOLOV5s do wnioskowania znajduje się w podkatalogu /docs/utils/AI_Application/aidemo_sdk/models/onnx (pobierz modele, jeśli nie są dostępne[ żadne pliki](https://github.com/kendryte/k510_docs/releases/download/v1.5/models.tar.gz)).  i rozpakuj), statyczny obraz znajduje się w podkatalogu /docs/utils/AI_Application/aidemo_sdk/examples/python_inference_on_PC/data, a skrypt znajduje się w podkatalogu /docs/utils/AI_Application/aidemo_sdk/examples/python_inference_on_PC. 

Postępuj zgodnie z wierszem polecenia skryptu, aby uruchomić skrypt yolov5_image.py w celu uzyskania wyniku wnioskowania obrazu statycznego. Wykryj poprawność modelu, sprawdzając, czy pole wykrywania obrazu wyjściowego jest poprawne, czy nie.

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

# 3 Generacja modelu

Generowanie modelu zależy od kompilatora nncase, a szczegółowe reguły korzystania z kompilatora nncase można znaleźć[ K510_nncase_Developer_Guides.md](./K510_nncase_Developer_Guides.md). Skrypt generujący kmodel dla YOLOV5s znajduje się w podkatalogu /docs/utils/AI_Application/aidemo_sdk/scripts. 

W wierszu polecenia skryptu uruchom gen_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py, aby wygenerować odpowiedni kmodel.

```shell
usage: gen_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py [-h] [--target TARGET] [--dump_dir DUMP_DIR] [--onnx ONNX] [--kmodel KMODEL]

optional arguments:
  -h, --help           show this help message and exit
  --target TARGET      target to run
  --dump_dir DUMP_DIR  temp folder to dump
  --onnx ONNX          onnx model path
  --kmodel KMODEL      kendryte model path
```

Należy zauważyć, że w celu zminimalizowania wstępnego przetwarzania na procesorze, opcje kompilacji w skrypcie są skonfigurowane w następujący sposób:

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

# 4 Walidacja modelu

Walidacja modelu zależy od symulatora nncase, a szczegółowe zasady korzystania z symulatora nncase można znaleźć[ w K510_nncase_Developer_Guides.md](./K510_nncase_Developer_Guides.md). Sprawdź, czy skrypt kmodel yolov5s znajduje się w podkatalogu /docs/utils/AI_Application/aidemo_sdk/scripts. 

W wierszu polecenia skryptu uruchom simu_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py, aby sprawdzić, czy odpowiedni kmodel jest generowany poprawnie.

```shell
usage: sim_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py [-h] [--onnx ONNX] [--kmodel KMODEL]

optional arguments:
  -h, --help       show this help message and exit
  --onnx ONNX      original model file
  --kmodel KMODEL  kmodel file
```

Jeśli podobieństwo cosinusa jest bliskie 1 lub równe 1, zapewniona jest poprawność wygenerowanego kmodelu.

```text
output 0 cosine similarity : 0.9999450445175171
output 1 cosine similarity : 0.9999403953552246
output 2 cosine similarity : 0.9999019503593445
```

# 5 Pisanie aplikacji AI

Sprawdzanie poprawności modelu zależy od środowiska uruchomieniowego nncase, a szczegółowe reguły korzystania ze środowiska wykonawczego nncase można znaleźć[ K510_nncase_Developer_Guides.md](./K510_nncase_Developer_Guides.md). Dokumentacja aplikacji AI`k510_buildroot/package/ai/code/object_detect`. Najpierw należy utworzyć instancję wykrywania obiektów i przydzielić miejsce na wejście i wyjście kmodel. 

```c++
objectDetect od(obj_thresh, nms_thresh, net_len, {valid_width, valid_height});
od.load_model(kmodel_path);  // load kmodel
od.prepare_memory();  // memory allocation
```

Aby zaimplementować zerową kopię pamięci, skojarz adres wyjściowy usługodawcy internetowego z adresem wejściowym kmodel

```c++
// define cv::Mat for ai input
// padding offset is (valid_width - valid_height) / 2 * valid_width
cv::Mat rgb24_img_for_ai(net_len, net_len, CV_8UC3, od.virtual_addr_input[0] + (valid_width - valid_height) / 2 * valid_width);
```

Konfiguruje szerokość i wysokość danych wyjściowych usługodawcy internetowego

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

Skonfiguruj odpowiedni plik konfiguracyjny wideo, video_height_r rzeczywistą wysokość wyjściową usługodawcy internetowego i video_height przesunięcie wysokości między różnymi kanałami usługodawcy internetowego

```json
"/dev/video5":{
    "video5_used":1,
    "video5_width":320,
    "video5_height":320,
    "video5_height_r":240,
    "video5_out_format":0
}
```

Skojarz adresy wejściowy i wyjściowy z input_tensor i output_tensor kmodel

```c++
od.set_input(0);
od.set_output();
```

Uruchom kmodel, uzyskaj wynik wyjściowy i wykonaj przetwarzanie końcowe

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

Na koniec narysuj pole wykrywania na dysku OSD, aby wyświetlić wyjście

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

# 6 Kompiluj aplikacje AI

Korzystając z łańcucha narzędzi kompilacji krzyżowej, można odwołać się do szczegółowych reguł kompilacji aplikacji AI[ K510_SDK_Build_and_Burn_Guide](./K510_SDK_Build_and_Burn_Guide.md). 

**Zrzeczenie się odpowiedzialności za **tłumaczenie  
Dla wygody klientów Canaan używa tłumacza AI do tłumaczenia tekstu na wiele języków, które mogą zawierać błędy. Nie gwarantujemy dokładności, rzetelności ani terminowości dostarczonych tłumaczeń. Canaan nie ponosi odpowiedzialności za jakiekolwiek straty lub szkody spowodowane poleganiem na dokładności lub wiarygodności przetłumaczonych informacji. W przypadku różnic w treści tłumaczeń w różnych językach, pierwszeństwo ma chińska wersja uproszczona. 

Jeśli chcesz zgłosić błąd lub niedokładność tłumaczenia, skontaktuj się z nami pocztą.