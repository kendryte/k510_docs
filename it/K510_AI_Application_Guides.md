![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">Guida all'applicazione AI K510</font>**

<font face="黑体"  size=3>Versione del documento: V1.0.0</font>

<font face="黑体"  size=3>Data di pubblicazione: 2022-03-07</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Disconoscimento**</font>
I prodotti, i servizi o le funzionalità acquistati saranno soggetti ai contratti e ai termini commerciali di Beijing Canaan Jiesi Information Technology Co., Ltd. ("la Società", la stessa di seguito), e tutti o parte dei prodotti, servizi o funzionalità descritti in questo documento potrebbero non rientrare nell'ambito dell'acquisto o dell'utilizzo. Salvo quanto diversamente concordato nel contratto, la Società declina ogni dichiarazione o garanzia, espressa o implicita, in merito all'accuratezza, affidabilità, completezza, marketing, scopo specifico e non aggressione di qualsiasi dichiarazione, informazione o contenuto di questo documento. Salvo diverso accordo, questo documento è fornito esclusivamente come guida al ragionamento.
A causa di aggiornamenti della versione del prodotto o altri motivi, il contenuto di questo documento può essere aggiornato o modificato di volta in volta senza alcun preavviso. 

**<font face="黑体"  size=3>Avvisi sui marchi</font>**

""<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, l'icona "Canaan", Canaan e altri marchi di Canaan e altri marchi di Canaan sono marchi di Beijing Canaan Jiesi Information Technology Co., Ltd. Tutti gli altri marchi o marchi registrati che possono essere menzionati in questo documento sono di proprietà dei rispettivi proprietari. 

**<font face="黑体"  size=3>Copyright ©2022 Pechino Canaan Jiesi Information Technology Co., Ltd</font>**
Questo documento è applicabile solo allo sviluppo e alla progettazione della piattaforma K510, senza il permesso scritto della società, nessuna unità o individuo può diffondere parte o tutto il contenuto di questo documento in qualsiasi forma. 

**<font face="黑体"  size=3>Pechino Canaan Jiesi Information Technology Co., Ltd</font>**
URL: canaan-creative.com
Richieste commerciali: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# prefazione
**<font face="黑体"  size=5>Scopo </font>**del documento
Questo documento è un documento complementare per l'applicazione AI K510 ed è progettato per aiutare gli ingegneri a comprendere la scrittura e l'applicazione delle applicazioni AI k510. 

**<font face="黑体"  size=5>Oggetti lettore</font>**

Le principali persone a cui si applica questo documento (questa guida):

- Sviluppatori di software
- Personale di supporto tecnico

**<font face="黑体"  size=5>Cronologia delle revisioni</font>**
 <font face="宋体"  size=2>La cronologia delle revisioni accumula una descrizione di ogni aggiornamento del documento. La versione più recente del documento contiene gli aggiornamenti per tutte le versioni precedenti. </font>

| Il numero di versione   | Modificato da     | Data della revisione | Note di revisione |
| :-----  |-------    |  ------ | ------  |
| V1.0.0 ·  | Divisione Prodotti AI  | 2022-03-07 |      |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenuto</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Introduzione

Questo documento descrive la scrittura e l'applicazione delle applicazioni AI K510. Basato sul chip AI K510, lo sviluppo di applicazioni AI ha le seguenti fasi:

Preparazione del modello: il modello sottoposto a training viene convalidato sul lato PC (è possibile utilizzare l'inferenza dell'immagine statica) per garantire la correttezza del modello

Generazione del modello: il modello sottoposto a training viene compilato utilizzando il compilatore nncase per generare un kmodel

Convalida del modello: il kmodel generato viene convalidato con precisione utilizzando il simulatore nncase

Scrittura di applicazioni AI: lettura completa di video / immagini, pre-elaborazione dell'input, inferenza del modello, post-elaborazione del modello

Compilare applicazioni AI: utilizzare la toolchain di compilazione incrociata per compilare applicazioni AI K510

Distribuzione e co-messa in servizio: l'applicazione AI compilata viene distribuita nel prodotto hardware K510 e il co-debug funzionale viene eseguito nello scenario effettivo

L'architettura complessiva dello sviluppo di applicazioni AI sul chip AI K510 è illustrata nella figura seguente:

![](../zh/images/ai_demo/image-ai-demo.png)

Questo documento prenderà il modello onnx di YOLOV5 con risoluzione 320x320 come esempio per introdurre l'intero processo di scrittura e applicazione delle applicazioni AI K510.

# 2 Preparazione del modello

Il modello onnx per YOLOV5s per l'inferenza si trova nella sottodirectory /docs/utils/AI_Application/aidemo_sdk/models/onnx (scaricare i modelli se non sono disponibili[ file](https://github.com/kendryte/k510_docs/releases/download/v1.5/models.tar.gz)).  e decomprimere), l'immagine statica si trova nella sottodirectory /docs/utils/AI_Application/aidemo_sdk/examples/python_inference_on_PC/data e lo script si trova nella sottodirectory /docs/utils/AI_Application/aidemo_sdk/examples/python_inference_on_PC. 

Seguire il prompt dei comandi dello script per eseguire lo script yolov5_image.py per ottenere il risultato dell'inferenza dell'immagine statica. Rilevare la correttezza del modello verificando che la casella di rilevamento dell'immagine di output sia corretta o meno.

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

# 3 Generazione di modelli

La generazione del modello dipende dal compilatore nncase e le regole specifiche per l'utilizzo del compilatore nncase sono disponibili[ K510_nncase_Developer_Guides.md](./K510_nncase_Developer_Guides.md). Lo script che genera il kmodel per YOLOV5s si trova nella sottodirectory /docs/utils/AI_Application/aidemo_sdk/scripts. 

Al prompt dei comandi dello script, eseguire il gen_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py per generare il kmodel corrispondente.

```shell
usage: gen_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py [-h] [--target TARGET] [--dump_dir DUMP_DIR] [--onnx ONNX] [--kmodel KMODEL]

optional arguments:
  -h, --help           show this help message and exit
  --target TARGET      target to run
  --dump_dir DUMP_DIR  temp folder to dump
  --onnx ONNX          onnx model path
  --kmodel KMODEL      kendryte model path
```

Va notato che al fine di ridurre al minimo la pre-elaborazione sulla CPU, le opzioni di compilazione nello script sono configurate come segue:

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

# 4 Validazione del modello

La convalida del modello dipende dal simulatore nncase e le regole specifiche per l'utilizzo del simulatore nncase sono disponibili[ in K510_nncase_Developer_Guides.md](./K510_nncase_Developer_Guides.md). Verificare che lo script kmodel di yolov5s si trovi nella sottodirectory /docs/utils/AI_Application/aidemo_sdk/scripts. 

Al prompt dei comandi dello script eseguire simu_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py per verificare che il kmodel corrispondente sia generato correttamente.

```shell
usage: sim_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py [-h] [--onnx ONNX] [--kmodel KMODEL]

optional arguments:
  -h, --help       show this help message and exit
  --onnx ONNX      original model file
  --kmodel KMODEL  kmodel file
```

Se la somiglianza del coseno è vicina a 1 o uguale a 1, viene garantita la correttezza del kmodel generato.

```text
output 0 cosine similarity : 0.9999450445175171
output 1 cosine similarity : 0.9999403953552246
output 2 cosine similarity : 0.9999019503593445
```

# 5 Scrivi applicazioni AI

La convalida del modello dipende dal runtime nncase e le regole specifiche per l'utilizzo del runtime nncase sono disponibili[ K510_nncase_Developer_Guides.md](./K510_nncase_Developer_Guides.md). Riferimento all'applicazione AI`k510_buildroot/package/ai/code/object_detect`. Innanzitutto, è necessario creare un'istanza di rilevamento degli oggetti e allocare lo spazio per l'input e l'output kmodel. 

```c++
objectDetect od(obj_thresh, nms_thresh, net_len, {valid_width, valid_height});
od.load_model(kmodel_path);  // load kmodel
od.prepare_memory();  // memory allocation
```

Per implementare zero copia di memoria, associare l'indirizzo di output dell'ISP all'indirizzo di input kmodel

```c++
// define cv::Mat for ai input
// padding offset is (valid_width - valid_height) / 2 * valid_width
cv::Mat rgb24_img_for_ai(net_len, net_len, CV_8UC3, od.virtual_addr_input[0] + (valid_width - valid_height) / 2 * valid_width);
```

Configura la larghezza e l'altezza dell'output dell'ISP

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

Configurare il file di configurazione video appropriato, video_height_r l'altezza di output reale dell'ISP e il video_height l'offset dell'altezza tra i diversi canali dell'ISP

```json
"/dev/video5":{
    "video5_used":1,
    "video5_width":320,
    "video5_height":320,
    "video5_height_r":240,
    "video5_out_format":0
}
```

Associare gli indirizzi di input e output alla input_tensor e output_tensor del kmodel

```c++
od.set_input(0);
od.set_output();
```

Esegui il kmodel, ottieni il risultato di output ed esegui la post-elaborazione

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

Infine, disegna la casella di rilevamento sull'OSD per visualizzare l'output

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

# 6 Compilare applicazioni AI

Utilizzando la toolchain di compilazione incrociata, è possibile fare riferimento alle regole specifiche per la compilazione di applicazioni AI[ K510_SDK_Build_and_Burn_Guide](./K510_SDK_Build_and_Burn_Guide.md). 

**Traduzione Disclaimer**  
Per la comodità dei clienti, Canaan utilizza un traduttore AI per tradurre il testo in più lingue, che possono contenere errori. Non garantiamo l'accuratezza, l'affidabilità o la tempestività delle traduzioni fornite. Canaan non sarà responsabile per eventuali perdite o danni causati dall'affidamento sull'accuratezza o sull'affidabilità delle informazioni tradotte. Se c'è una differenza di contenuto tra le traduzioni in lingue diverse, prevarrà la versione cinese semplificata. 

Se desideri segnalare un errore di traduzione o un'inesattezza, non esitare a contattarci via mail.