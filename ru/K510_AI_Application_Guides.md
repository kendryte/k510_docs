![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">Руководство по применению K510 AI</font>**

<font face="黑体"  size=3>Версия документа: V1.0.0</font>

<font face="黑体"  size=3>Опубликовано: 2022-03-07</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Отказ**</font>
Продукты, услуги или функции, которые вы покупаете, регулируются коммерческими контрактами и условиями Beijing Canaan Jiesi Information Technology Co., Ltd. («Компания», то же самое далее), и все или часть продуктов, услуг или функций, описанных в этом документе, могут не входить в сферу вашей покупки или использования. Если иное не оговорено в договоре, Компания отказывается от всех заявлений или гарантий, явных или подразумеваемых, в отношении точности, надежности, полноты, маркетинга, конкретной цели и ненападения любых заявлений, информации или содержания этого документа. Если не согласовано иное, настоящий документ предоставляется исключительно в качестве руководства для рассуждений.
В связи с обновлением версии продукта или по другим причинам содержимое этого документа может время от времени обновляться или изменяться без какого-либо уведомления.

**<font face="黑体"  size=3>Уведомления о товарных знаках</font>**

""<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, значок "Canaan", Canaan и другие товарные знаки Canaan и другие товарные знаки Canaan являются товарными знаками Beijing Canaan Jiesi Information Technology Co., Ltd. Все другие товарные знаки или зарегистрированные товарные знаки, которые могут быть упомянуты в этом документе, принадлежат их соответствующим владельцам.

**<font face="黑体"  size=3>Copyright ©2022 Пекин Ханаан Цзеси Информационные технологии Co., Ltd</font>**
Настоящий документ применим только к разработке и проектированию платформы K510, без письменного разрешения компании, ни одно подразделение или частное лицо не может распространять часть или все содержание этого документа в любой форме.

**<font face="黑体"  size=3>Пекин Ханаан Цзеси Информационные Технологии Co., Ltd</font>**
URL: canaan-creative.com
Бизнес-запросы: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# предисловие
**<font face="黑体"  size=5>Назначение </font>**документа
Этот документ является сопутствующим документом для приложения K510 AI и предназначен для того, чтобы помочь инженерам понять написание и применение приложений K510 AI.

**<font face="黑体"  size=5>Объекты чтения</font>**

Основные люди, к которым относится этот документ (это руководство):

- Разработчики программного обеспечения
- Персонал технической поддержки

**<font face="黑体"  size=5>История изменений</font>**
 <font face="宋体"  size=2>Журнал изменений накапливает описание каждого обновления документа. Последняя версия документа содержит обновления для всех предыдущих версий. </font>

| Номер версии   | Изменено     | Дата пересмотра | Примечания к пересмотру |
| :-----  |-------    |  ------ | ------  |
| Версия 1.0.0  | Отдел продуктов ИИ  | 2022-03-07 |      |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Содержание</font>**

[ОГЛАВЛЕНИЯ]

<div style="page-break-after:always"></div>

# 1 Введение

В этом документе описывается написание и применение приложений K510 AI. На базе чипа K510 AI разработка приложений ИИ имеет следующие этапы:

Подготовка модели: обученная модель проверяется на стороне ПК (можно использовать статический вывод изображения) для обеспечения правильности модели

Генерация модели: обученная модель компилируется с помощью компилятора nncase для создания kmodel

Проверка модели: сгенерированный kmodel проверяется с точностью с помощью симулятора nncase

Написание приложений ИИ: полное чтение видео/изображений, предварительная обработка ввода, вывод модели, постобработка модели

Компиляция приложений ИИ: использование цепочки инструментов кросс-компиляции для компиляции приложений ИИ K510

Развертывание и совместное ввод в эксплуатацию: скомпилированное приложение ИИ развертывается в аппаратном продукте K510, а функциональная совместная отладка выполняется в реальном сценарии.

Общая архитектура разработки приложений ИИ на чипе K510 AI показана на следующем рисунке:

![](../zh/images/ai_demo/image-ai-demo.png)

В этом документе в качестве примера будет взята модель onnx с разрешением 320x320 YOLOV5s, чтобы представить весь процесс написания и применения приложений K510 AI.

# 2 Подготовка модели

Модель onnx для YOLOV5s для вывода находится в подкаталоге /docs/utils/AI_Application/aidemo_sdk/models/onnx (загружайте модели, если файлы[недоступны](https://github.com/kendryte/k510_docs/releases/download/v1.5/models.tar.gz)).  и unzip), статическое изображение находится в подкаталоге /docs/utils/AI_Application/aidemo_sdk/examples/python_inference_on_PC/data, а скрипт — в подкаталоге /docs/utils/AI_Application/aidemo_sdk/examples/python_inference_on_PC.

Следуйте указаниям командной строки сценария, чтобы запустить сценарий yolov5_image.py для получения результата вывода статического рисунка. Определите правильность модели, проверив правильность или неправильность поля обнаружения выходного изображения.

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

# 3 Генерация моделей

Создание модели зависит от компилятора nncase, а конкретные правила использования компилятора nncase можно найти[K510_nncase_Developer_Guides.md](./K510_nncase_Developer_Guides.md). Скрипт, генерирующий kmodel для YOLOV5s, находится в подкаталоге /docs/utils/AI_Application/aidemo_sdk/scripts.

В командной строке сценария запустите gen_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py для создания соответствующего kmodel.

```shell
usage: gen_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py [-h] [--target TARGET] [--dump_dir DUMP_DIR] [--onnx ONNX] [--kmodel KMODEL]

optional arguments:
  -h, --help           show this help message and exit
  --target TARGET      target to run
  --dump_dir DUMP_DIR  temp folder to dump
  --onnx ONNX          onnx model path
  --kmodel KMODEL      kendryte model path
```

Следует отметить, что для минимизации препроцессирования на процессоре параметры компиляции в скрипте настроены следующим образом:

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

# 4 Проверка модели

Проверка модели зависит от симулятора nncase, а конкретные правила использования симулятора nncase можно найти[в K510_nncase_Developer_Guides.md](./K510_nncase_Developer_Guides.md). Убедитесь, что скрипт kmodel yolov5s находится в подкаталоге /docs/utils/AI_Application/aidemo_sdk/scripts.

В командной строке сценария выполните simu_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py, чтобы убедиться, что соответствующий kmodel сгенерирован правильно.

```shell
usage: sim_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py [-h] [--onnx ONNX] [--kmodel KMODEL]

optional arguments:
  -h, --help       show this help message and exit
  --onnx ONNX      original model file
  --kmodel KMODEL  kmodel file
```

Если косинусное сходство близко к 1 или равно 1, обеспечивается правильность генерируемого кмоделя.

```text
output 0 cosine similarity : 0.9999450445175171
output 1 cosine similarity : 0.9999403953552246
output 2 cosine similarity : 0.9999019503593445
```

# 5 Написание приложений ИИ

Проверка модели зависит от среды выполнения nncase, а конкретные правила использования среды выполнения nncase можно найти[K510_nncase_Developer_Guides.md](./K510_nncase_Developer_Guides.md). Справочник по приложениям ИИ`k510_buildroot/package/ai/code/object_detect`. Во-первых, необходимо создать экземпляр обнаружения объектов и выделить место для ввода и вывода kmodel.

```c++
objectDetect od(obj_thresh, nms_thresh, net_len, {valid_width, valid_height});
od.load_model(kmodel_path);  // load kmodel
od.prepare_memory();  // memory allocation
```

Чтобы реализовать нулевую копию памяти, свяжите выходной адрес поставщика услуг Интернета с входным адресом kmodel

```c++
// define cv::Mat for ai input
// padding offset is (valid_width - valid_height) / 2 * valid_width
cv::Mat rgb24_img_for_ai(net_len, net_len, CV_8UC3, od.virtual_addr_input[0] + (valid_width - valid_height) / 2 * valid_width);
```

Настройка ширины и высоты выходных данных поставщика услуг Интернета

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

Настройте соответствующий файл конфигурации видео, video_height_r истинную выходную высоту поставщика услуг Интернета, а video_height смещение высоты между различными каналами поставщика услуг Интернета.

```json
"/dev/video5":{
    "video5_used":1,
    "video5_width":320,
    "video5_height":320,
    "video5_height_r":240,
    "video5_out_format":0
}
```

Связывание входных и выходных адресов с input_tensor и output_tensor kmodel

```c++
od.set_input(0);
od.set_output();
```

Запустите kmodel, получите выходной результат и выполните постобработку

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

Наконец, нарисуйте поле обнаружения на экранном меню, чтобы отобразить выходные данные

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

# 6 Компиляция приложений ИИ

Используя цепочку инструментов кросс-компиляции, конкретные правила компиляции приложений ИИ можно сослаться[K510_SDK_Build_and_Burn_Guide](./K510_SDK_Build_and_Burn_Guide.md).

**Отказ от ответственности за**перевод  
Для удобства клиентов Canaan использует переводчик AI для перевода текста на несколько языков, которые могут содержать ошибки. Мы не гарантируем точность, надежность или своевременность предоставленных переводов. Компания Canaan не несет ответственности за любые убытки или ущерб, вызванные доверием к точности или надежности переведенной информации. При наличии разницы в содержании переводов на разные языки преимущественную силу имеет упрощенная версия на китайском языке.

Если вы хотите сообщить об ошибке или неточности перевода, пожалуйста, не стесняйтесь обращаться к нам по почте.
