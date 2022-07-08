![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 AI Anwendungshandbuch</font>**

<font face="黑体"  size=3>Dokumentversion: V1.0.0</font>

<font face="黑体"  size=3>Veröffentlicht: 2022-03-07</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Verzichtserklärung**</font>
Die Produkte, Dienstleistungen oder Funktionen, die Sie erwerben, unterliegen den kommerziellen Verträgen und Bedingungen von Beijing Canaan Jiesi Information Technology Co., Ltd. ("das Unternehmen", dasselbe im Folgenden), und alle oder ein Teil der in diesem Dokument beschriebenen Produkte, Dienstleistungen oder Funktionen fallen möglicherweise nicht in den Rahmen Ihres Kaufs oder Ihrer Nutzung. Sofern im Vertrag nicht anders vereinbart, lehnt das Unternehmen alle ausdrücklichen oder stillschweigenden Zusicherungen oder Gewährleistungen hinsichtlich der Genauigkeit, Zuverlässigkeit, Vollständigkeit, des Marketings, des spezifischen Zwecks und der Nichtverletzung von Zusicherungen, Informationen oder Inhalten dieses Dokuments ab. Sofern nicht anders vereinbart, wird dieses Dokument ausschließlich als Leitfaden für die Argumentation zur Verfügung gestellt.
Aufgrund von Produktversions-Upgrades oder anderen Gründen kann der Inhalt dieses Dokuments von Zeit zu Zeit ohne vorherige Ankündigung aktualisiert oder geändert werden.

**<font face="黑体"  size=3>Markenhinweise</font>**

"", "Canaan"-Symbol, Canaan und andere Marken von Canaan und andere Marken von Canaan <img src="../zh/images/canaan-logo.png" style="zoom:33%;" />sind Marken von Beijing Canaan Jiesi Information Technology Co., Ltd. Alle anderen Marken oder eingetragenen Warenzeichen, die in diesem Dokument erwähnt werden können, sind Eigentum ihrer jeweiligen Inhaber.

**<font face="黑体"  size=3>Copyright ©2022 Peking Canaan Jiesi Information Technology Co., Ltd</font>**
Dieses Dokument gilt nur für die Entwicklung und das Design der K510-Plattform, ohne die schriftliche Genehmigung des Unternehmens darf keine Einheit oder Einzelperson einen Teil oder den gesamten Inhalt dieses Dokuments in irgendeiner Form verbreiten.

**<font face="黑体"  size=3>Peking Canaan Jiesi Informationstechnologie Co., Ltd</font>**
URL: canaan-creative.com
Geschäftliche Anfragen: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# Vorwort
**<font face="黑体"  size=5>Zweck des Dokuments</font>**
Dieses Dokument ist ein Begleitdokument für die K510 AI-Anwendung und soll Ingenieuren helfen, das Schreiben und die Anwendung von k510 AI-Anwendungen zu verstehen.

**<font face="黑体"  size=5>Reader-Objekte</font>**

Die wichtigsten Personen, für die sich dieses Dokument (dieser Leitfaden) richtet:

- Softwareentwickler
- Mitarbeiter des technischen Supports

**<font face="黑体"  size=5>Revisionshistorie</font>**
 <font face="宋体"  size=2>In der Revisionshistorie wird eine Beschreibung jeder Dokumentaktualisierung gesammelt. Die neueste Version des Dokuments enthält Updates für alle vorherigen Versionen. </font>

| Die Versionsnummer   | Geändert von     | Datum der Überarbeitung | Revisionshinweise |
| :-----  |-------    |  ------ | ------  |
| V1.0.0  | Geschäftsbereich KI-Produkte  | 2022-03-07 |      |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Inhalt</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Einleitung

Dieses Dokument beschreibt das Schreiben und die Anwendung von K510 AI-Anwendungen. Basierend auf dem KI-Chip K510 umfasst die Entwicklung von KI-Anwendungen die folgenden Phasen:

Modellvorbereitung: Das trainierte Modell wird PC-seitig validiert (statische Bildinferenz kann verwendet werden), um die Korrektheit des Modells sicherzustellen

Modellgenerierung: Das trainierte Modell wird mit dem nncase-Compiler kompiliert, um ein kmodel zu generieren

Modellvalidierung: Das generierte kmodel wird mit dem nncase-Simulator präzise validiert

Schreiben Sie KI-Anwendungen: vollständiges Video- / Bildlesen, Eingabevorverarbeitung, Modellinferenz, Modellnachbearbeitung

Kompilieren von KI-Anwendungen: Verwenden Sie die Cross-Compilation-Toolchain, um K510 AI-Anwendungen zu kompilieren

Bereitstellung und Co-Inbetriebnahme: Die kompilierte KI-Anwendung wird auf dem K510-Hardwareprodukt bereitgestellt, und das funktionale Co-Debugging wird im tatsächlichen Szenario durchgeführt.

Die Gesamtarchitektur der KI-Anwendungsentwicklung auf dem KI-Chip K510 ist in der folgenden Abbildung dargestellt:

![](../zh/images/ai_demo/image-ai-demo.png)

In diesem Dokument wird das onnx-Modell der YOLOV5s mit einer Auflösung von 320 x 320 als Beispiel verwendet, um den gesamten Prozess des Schreibens und Anwendens von K510 AI-Anwendungen vorzustellen.

# 2 Modellvorbereitung

Das onnx-Modell für YOLOV5s für Inferenz befindet sich im Unterverzeichnis /docs/utils/AI_Application/aidemo_sdk/models/onnx (laden Sie Modelle herunter, wenn keine Dateien verfügbar[sind](https://github.com/kendryte/k510_docs/releases/download/v1.5/models.tar.gz).)  und entpacken), befindet sich das statische Bild im Unterverzeichnis /docs/utils/AI_Application/aidemo_sdk/examples/python_inference_on_PC/data, und das Skript befindet sich im Unterverzeichnis /docs/utils/AI_Application/aidemo_sdk/examples/python_inference_on_PC.

Folgen Sie der Skripteingabeaufforderung, um das yolov5_image.py Skript auszuführen, um das Inferenzergebnis des statischen Bilds abzurufen. Erkennen Sie die Richtigkeit des Modells, indem Sie überprüfen, ob das Erkennungsfeld des Ausgabebilds korrekt ist oder nicht.

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

# 3 Modellgenerierung

Die Modellgenerierung hängt vom nncase-Compiler ab, und die spezifischen Regeln für die Verwendung des nncase-Compilers finden[Sie K510_nncase_Developer_Guides.md.](./K510_nncase_Developer_Guides.md) Das Skript, das das kmodel für YOLOV5s generiert, befindet sich im Unterverzeichnis /docs/utils/AI_Application/aidemo_sdk/scripts.

Führen Sie an der Eingabeaufforderung des Skripts die gen_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py aus, um das entsprechende kmodel zu generieren.

```shell
usage: gen_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py [-h] [--target TARGET] [--dump_dir DUMP_DIR] [--onnx ONNX] [--kmodel KMODEL]

optional arguments:
  -h, --help           show this help message and exit
  --target TARGET      target to run
  --dump_dir DUMP_DIR  temp folder to dump
  --onnx ONNX          onnx model path
  --kmodel KMODEL      kendryte model path
```

Es sollte beachtet werden, dass, um die Vorverarbeitung auf der CPU zu minimieren, die Kompilierungsoptionen im Skript wie folgt konfiguriert sind:

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

# 4 Modellvalidierung

Die Modellvalidierung hängt vom nncase-Simulator ab, und die spezifischen Regeln für die Verwendung des nncase-Simulators finden Sie[in K510_nncase_Developer_Guides.md.](./K510_nncase_Developer_Guides.md) Stellen Sie sicher, dass sich das kmodel-Skript von yolov5s im Unterverzeichnis /docs/utils/AI_Application/aidemo_sdk/scripts befindet.

Führen Sie an der Skripteingabeaufforderung simu_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py aus, um zu überprüfen, ob das entsprechende kmodel ordnungsgemäß generiert wurde.

```shell
usage: sim_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py [-h] [--onnx ONNX] [--kmodel KMODEL]

optional arguments:
  -h, --help       show this help message and exit
  --onnx ONNX      original model file
  --kmodel KMODEL  kmodel file
```

Wenn die Kosinusähnlichkeit nahe bei 1 oder gleich 1 liegt, ist die Richtigkeit des generierten kmodels gewährleistet.

```text
output 0 cosine similarity : 0.9999450445175171
output 1 cosine similarity : 0.9999403953552246
output 2 cosine similarity : 0.9999019503593445
```

# 5 KI-Anwendungen schreiben

Die Modellvalidierung hängt von der nncase-Laufzeit ab, und die spezifischen Regeln für die Verwendung der nncase-Laufzeit finden Sie[K510_nncase_Developer_Guides.md.](./K510_nncase_Developer_Guides.md) KI-Anwendungsreferenz`k510_buildroot/package/ai/code/object_detect`. Zuerst müssen Sie eine Objekterkennungsinstanz erstellen und Speicherplatz für die kmodel-Eingabe und -Ausgabe zuweisen.

```c++
objectDetect od(obj_thresh, nms_thresh, net_len, {valid_width, valid_height});
od.load_model(kmodel_path);  // load kmodel
od.prepare_memory();  // memory allocation
```

Um eine Zero-Memory-Kopie zu implementieren, ordnen Sie die ISP-Ausgabeadresse der kmodel-Eingabeadresse zu

```c++
// define cv::Mat for ai input
// padding offset is (valid_width - valid_height) / 2 * valid_width
cv::Mat rgb24_img_for_ai(net_len, net_len, CV_8UC3, od.virtual_addr_input[0] + (valid_width - valid_height) / 2 * valid_width);
```

Konfiguriert die Breite und Höhe der ISP-Ausgabe

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

Konfigurieren Sie die entsprechende Videokonfigurationsdatei, video_height_r Sie die tatsächliche Ausgabehöhe des ISP und den video_height den Höhenoffset zwischen den verschiedenen Kanälen des ISP.

```json
"/dev/video5":{
    "video5_used":1,
    "video5_width":320,
    "video5_height":320,
    "video5_height_r":240,
    "video5_out_format":0
}
```

Ordnen Sie die Eingangs- und Ausgabeadressen dem input_tensor und output_tensor des kmodel zu

```c++
od.set_input(0);
od.set_output();
```

Führen Sie das kmodel aus, rufen Sie das Ausgabeergebnis ab und führen Sie die Nachbearbeitung durch

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

Zeichnen Sie schließlich die Erkennungsbox auf dem OSD, um die Ausgabe anzuzeigen

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

# 6 Kompilieren von KI-Anwendungen

Über die Cross-Compilation-Toolchain können die spezifischen Regeln für die Kompilierung von KI-Anwendungen K510_SDK_Build_and_Burn_Guide herangezogen werden[](./K510_SDK_Build_and_Burn_Guide.md).

**Haftungsausschluss**für Übersetzungen  
Für die Bequemlichkeit der Kunden verwendet Canaan einen KI-Übersetzer, um Text in mehrere Sprachen zu übersetzen, die Fehler enthalten können. Wir übernehmen keine Gewähr für die Genauigkeit, Zuverlässigkeit oder Aktualität der bereitgestellten Übersetzungen. Canaan haftet nicht für Verluste oder Schäden, die durch das Vertrauen auf die Richtigkeit oder Zuverlässigkeit der übersetzten Informationen verursacht werden. Wenn es einen inhaltlichen Unterschied zwischen den Übersetzungen in verschiedenen Sprachen gibt, ist die vereinfachte chinesische Version maßgebend.

Wenn Sie einen Übersetzungsfehler oder eine Ungenauigkeit melden möchten, können Sie uns gerne per E-Mail kontaktieren.
