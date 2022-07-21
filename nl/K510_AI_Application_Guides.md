![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 AI-toepassingshandleiding</font>**

<font face="黑体"  size=3>Document versie: V1.0.0</font>

<font face="黑体"  size=3>Publicatiedatum: 2022-03-07</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Disclaimer**</font>
De producten, diensten of functies die u koopt, zijn onderworpen aan de commerciële contracten en voorwaarden van Beijing Canaan Jiesi Information Technology Co., Ltd. ("het Bedrijf", hierna hetzelfde), en alle of een deel van de producten, diensten of functies die in dit document worden beschreven, vallen mogelijk niet binnen het bereik van uw aankoop of gebruik. Tenzij anders overeengekomen in het contract, wijst het bedrijf alle verklaringen of garanties af, expliciet of impliciet, met betrekking tot de nauwkeurigheid, betrouwbaarheid, volledigheid, marketing, specifiek doel en niet-agressie van verklaringen, informatie of inhoud van dit document. Tenzij anders overeengekomen, wordt dit document uitsluitend verstrekt als leidraad voor de redenering.
Vanwege upgrades van de productversie of andere redenen kan de inhoud van dit document van tijd tot tijd zonder enige kennisgeving worden bijgewerkt of gewijzigd.

**<font face="黑体"  size=3>Handelsmerkkennisgevingen</font>**

""<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, "Canaan" icoon, Kanaän en andere handelsmerken van Kanaän en andere handelsmerken van Kanaän zijn handelsmerken van Beijing Canaan Jiesi Information Technology Co., Ltd. Alle andere handelsmerken of geregistreerde handelsmerken die in dit document kunnen worden genoemd, zijn eigendom van hun respectieve eigenaars.

**<font face="黑体"  size=3>Copyright ©2022 Beijing Canaan Jiesi Information Technology Co, Ltd</font>**
Dit document is alleen van toepassing op de ontwikkeling en het ontwerp van het K510-platform, zonder de schriftelijke toestemming van het bedrijf mag geen enkele eenheid of persoon een deel of de inhoud van dit document in welke vorm dan ook verspreiden.

**<font face="黑体"  size=3>Beijing Canaan Jiesi Information Technology Co, Ltd</font>**
URL: canaan-creative.com
Zakelijke vragen: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# inleiding
**<font face="黑体"  size=5>Doel van het document</font>**
Dit document is een begeleidend document voor de K510 AI-toepassing en is ontworpen om ingenieurs te helpen het schrijven en de toepassing van k510 AI-toepassingen te begrijpen.

**<font face="黑体"  size=5>Reader Objecten</font>**

De belangrijkste personen op wie dit document (deze gids) van toepassing is:

- Softwareontwikkelaars
- Technisch ondersteunend personeel

**<font face="黑体"  size=5>Revisiegeschiedenis</font>**
 <font face="宋体"  size=2>De revisiegeschiedenis bevat een beschrijving van elke documentupdate. De nieuwste versie van het document bevat updates voor alle voorgaande versies. </font>

| Het versienummer   | Gewijzigd door     | Datum van herziening | Opmerkingen bij herziening |
| :-----  |-------    |  ------ | ------  |
| V1.0.0  | Divisie AI-producten  | 2022-03-07 |      |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Inhoud</font>**

[INHOUDSOPGAVE]

<div style="page-break-after:always"></div>

# 1 Inleiding

Dit document beschrijft het schrijven en toepassen van K510 AI-toepassingen. Op basis van de K510 AI-chip heeft de ontwikkeling van AI-toepassingen de volgende fasen:

Modelvoorbereiding: Het getrainde model wordt gevalideerd aan de pc-kant (statische beeldinferentie kan worden gebruikt) om de juistheid van het model te garanderen

Modelgeneratie: Het getrainde model wordt gecompileerd met behulp van de nncase-compiler om een kmodel te genereren

Modelvalidatie: Het gegenereerde kmodel wordt met precisie gevalideerd met behulp van de nncase-simulator

Schrijf AI-toepassingen: volledige video-/beeldlezing, invoervoorbewerking, modelinferentie, modelnabewerking

AI-toepassingen compileren: gebruik de cross-compilatietoolchain om K510 AI-toepassingen te compileren

Implementatie en co-commissioning: de gecompileerde AI-toepassing wordt geïmplementeerd op het K510-hardwareproduct en de functionele co-debuggen wordt uitgevoerd in het werkelijke scenario

De algemene architectuur van ai-applicatieontwikkeling op de K510 AI-chip wordt weergegeven in de volgende afbeelding:

![](../zh/images/ai_demo/image-ai-demo.png)

Dit document neemt het onnx-model van 320x320 resolutie YOLOV5s als voorbeeld om het hele proces van het schrijven en toepassen van K510 AI-toepassingen te introduceren.

# 2 Modelvoorbereiding

Het onnx-model voor YOLOV5s voor inferentie bevindt zich in de submap /docs/utils/AI_Application/aidemo_sdk/models/onnx (download modellen als er geen bestanden beschikbaar[zijn](https://github.com/kendryte/k510_docs/releases/download/v1.5/models.tar.gz).)  en unzip), bevindt de statische afbeelding zich in de submap /docs/utils/AI_Application/aidemo_sdk/examples/python_inference_on_PC/data en bevindt het script zich in de submap /docs/utils/AI_Application/aidemo_sdk/examples/python_inference_on_PC.

Volg de scriptopdrachtprompt om het yolov5_image.py script uit te voeren om het gevolgtrekkingsresultaat van de statische afbeelding te verkrijgen. Detecteer de juistheid van het model door te controleren of het detectievak van de uitvoerafbeelding correct is of niet.

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

# 3 Model generatie

Het genereren van modellen is afhankelijk van de nncase-compiler en de specifieke regels voor het gebruik van de nncase-compiler zijn te vinden[K510_nncase_Developer_Guides.md](./K510_nncase_Developer_Guides.md). Het script dat het kmodel voor YOLOV5s genereert, bevindt zich in de submap /docs/utils/AI_Application/aidemo_sdk/scripts.

Voer bij de opdrachtprompt van het script de gen_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py uit om het bijbehorende kmodel te genereren.

```shell
usage: gen_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py [-h] [--target TARGET] [--dump_dir DUMP_DIR] [--onnx ONNX] [--kmodel KMODEL]

optional arguments:
  -h, --help           show this help message and exit
  --target TARGET      target to run
  --dump_dir DUMP_DIR  temp folder to dump
  --onnx ONNX          onnx model path
  --kmodel KMODEL      kendryte model path
```

Opgemerkt moet worden dat om voorbewerking op de CPU te minimaliseren, de compilatie-opties in het script als volgt zijn geconfigureerd:

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

# 4 Model validatie

Modelvalidatie is afhankelijk van nncase simulator, en de specifieke regels voor het gebruik van nncase simulator zijn te vinden[in K510_nncase_Developer_Guides.md](./K510_nncase_Developer_Guides.md). Controleer of het kmodel-script van yolov5s zich in de submap /docs/utils/AI_Application/aidemo_sdk/scripts bevindt.

Voer bij de scriptopdrachtprompt simu_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py uit om te controleren of het bijbehorende kmodel correct is gegenereerd.

```shell
usage: sim_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py [-h] [--onnx ONNX] [--kmodel KMODEL]

optional arguments:
  -h, --help       show this help message and exit
  --onnx ONNX      original model file
  --kmodel KMODEL  kmodel file
```

Als de cosinusovereenkomst dicht bij 1 of gelijk aan 1 ligt, is de juistheid van het gegenereerde kmodel verzekerd.

```text
output 0 cosine similarity : 0.9999450445175171
output 1 cosine similarity : 0.9999403953552246
output 2 cosine similarity : 0.9999019503593445
```

# 5 AI-toepassingen schrijven

Modelvalidatie is afhankelijk van de nncase-runtime en de specifieke regels voor het gebruik van de nncase-runtime zijn te vinden[K510_nncase_Developer_Guides.md](./K510_nncase_Developer_Guides.md). Referentie voor AI-toepassingen`k510_buildroot/package/ai/code/object_detect`. Eerst moet u een objectdetectie-instantie maken en ruimte toewijzen voor de invoer en uitvoer van het kmodel.

```c++
objectDetect od(obj_thresh, nms_thresh, net_len, {valid_width, valid_height});
od.load_model(kmodel_path);  // load kmodel
od.prepare_memory();  // memory allocation
```

Als u zero memory copy wilt implementeren, koppelt u het uitvoeradres van de internetprovider aan het kmodel-invoeradres

```c++
// define cv::Mat for ai input
// padding offset is (valid_width - valid_height) / 2 * valid_width
cv::Mat rgb24_img_for_ai(net_len, net_len, CV_8UC3, od.virtual_addr_input[0] + (valid_width - valid_height) / 2 * valid_width);
```

Configureert de breedte en hoogte van de ISP-uitvoer

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

Configureer het juiste videoconfiguratiebestand, video_height_r de werkelijke uitvoerhoogte van de internetprovider en de video_height de hoogteverschuiving tussen de verschillende kanalen van de internetprovider

```json
"/dev/video5":{
    "video5_used":1,
    "video5_width":320,
    "video5_height":320,
    "video5_height_r":240,
    "video5_out_format":0
}
```

Koppel de invoer- en uitvoeradressen aan de input_tensor en output_tensor van het kmodel

```c++
od.set_input(0);
od.set_output();
```

Voer het kmodel uit, krijg het uitvoerresultaat en voer de nabewerking uit

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

Teken ten slotte het detectievak op het OSD om de uitvoer weer te geven

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

# 6 AI-toepassingen compileren

Met behulp van de cross-compilatie toolchain kunnen de specifieke regels voor de compilatie van AI-toepassingen worden verwezen K510_SDK_Build_and_Burn_Guide[](./K510_SDK_Build_and_Burn_Guide.md).

**Vertaling Disclaimer**  
Voor het gemak van klanten gebruikt Canaan een AI-vertaler om tekst in meerdere talen te vertalen, wat fouten kan bevatten. Wij garanderen niet de nauwkeurigheid, betrouwbaarheid of tijdigheid van de geleverde vertalingen. Canaan is niet aansprakelijk voor enig verlies of schade veroorzaakt door het vertrouwen op de nauwkeurigheid of betrouwbaarheid van de vertaalde informatie. Als er een inhoudelijk verschil is tussen de vertalingen in verschillende talen, prevaleert de vereenvoudigd Chinese versie.

Als u een vertaalfout of onnauwkeurigheid wilt melden, neem dan gerust contact met ons op via e-mail.
