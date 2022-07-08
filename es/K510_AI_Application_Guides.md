![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">Guía de aplicación de K510 AI</font>**

<font face="黑体"  size=3>Versión del documento: V1.0.0</font>

<font face="黑体"  size=3>Publicado: 2022-03-07</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Renuncia**</font>
Los productos, servicios o características que compre estarán sujetos a los contratos comerciales y términos de Beijing Canaan Jiesi Information Technology Co., Ltd. ("la Compañía", la misma en adelante), y todos o parte de los productos, servicios o características descritos en este documento pueden no estar dentro del alcance de su compra o uso. Salvo que se acuerde lo contrario en el contrato, la Compañía renuncia a todas las representaciones o garantías, expresas o implícitas, en cuanto a la precisión, confiabilidad, integridad, marketing, propósito específico y no agresión de cualquier representación, información o contenido de este documento. A menos que se acuerde lo contrario, este documento se proporciona únicamente como una guía para el razonamiento.
Debido a actualizaciones de la versión del producto u otras razones, el contenido de este documento puede actualizarse o modificarse de vez en cuando sin previo aviso.

**<font face="黑体"  size=3>Avisos de marcas comerciales</font>**

""<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, el icono de "Canaan", Canaan y otras marcas comerciales de Canaan y otras marcas comerciales de Canaan son marcas comerciales de Beijing Canaan Jiesi Information Technology Co., Ltd. Todas las demás marcas comerciales o marcas registradas que puedan mencionarse en este documento son propiedad de sus respectivos propietarios.

**<font face="黑体"  size=3>Derechos de autor ©2022 Beijing Canaan Jiesi Information Technology Co., Ltd</font>**
Este documento solo es aplicable al desarrollo y diseño de la plataforma K510, sin el permiso por escrito de la empresa, ninguna unidad o individuo puede difundir parte o la totalidad del contenido de este documento en ninguna forma.

**<font face="黑体"  size=3>Beijing Canaan Jiesi Información Technology Co., Ltd</font>**
URL: canaan-creative.com
Consultas comerciales: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# prefacio
**<font face="黑体"  size=5>Propósito del documento</font>**
Este documento es un documento complementario para la aplicación K510 AI y está diseñado para ayudar a los ingenieros a comprender la escritura y la aplicación de las aplicaciones k510 AI.

**<font face="黑体"  size=5>Objetos reader</font>**

Las principales personas a las que se aplica este documento (esta guía):

- Desarrolladores de software
- Personal de soporte técnico

**<font face="黑体"  size=5>Historial
 </font>**de revisiones <font face="宋体"  size=2>El historial de revisiones acumula una descripción de cada actualización del documento. La versión más reciente del documento contiene actualizaciones para todas las versiones anteriores. </font>

| El número de versión   | Modificado por     | Fecha de revisión | Notas de revisión |
| :-----  |-------    |  ------ | ------  |
| V1.0.0  | División de Productos de IA  | 2022-03-07 |      |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenido</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Introducción

Este documento describe la escritura y aplicación de aplicaciones de IA K510. Basado en el chip de IA K510, el desarrollo de aplicaciones de IA tiene las siguientes etapas:

Preparación del modelo: el modelo entrenado se valida en el lado de la PC (se puede utilizar la inferencia de imagen estática) para garantizar la exactitud del modelo

Generación de modelos: el modelo entrenado se compila utilizando el compilador nncase para generar un kmodel

Validación del modelo: El kmodel generado se valida con precisión utilizando el simulador nncase

Escribir aplicaciones de IA: lectura completa de video / imagen, preprocesamiento de entrada, inferencia de modelos, postprocesamiento de modelos

Compilar aplicaciones de IA: utilice la cadena de herramientas de compilación cruzada para compilar aplicaciones de IA K510

Implementación y co-puesta en marcha: La aplicación de IA compilada se implementa en el producto de hardware K510, y la co-depuración funcional se lleva a cabo en el escenario real.

La arquitectura general del desarrollo de aplicaciones de IA en el chip de IA K510 se muestra en la siguiente figura:

![](../zh/images/ai_demo/image-ai-demo.png)

Este documento tomará como ejemplo el modelo onnx de resolución 320x320 YOLOV5s para introducir todo el proceso de escritura y aplicación de aplicaciones de IA K510.

# 2 Preparación del modelo

El modelo onnx para YOLOV5s para inferencia se encuentra en el subdirectorio /docs/utils/AI_Application/aidemo_sdk/models/onnx (descargue modelos si no hay archivos disponibles[](https://github.com/kendryte/k510_docs/releases/download/v1.5/models.tar.gz)).  y descomprimir), la imagen estática se encuentra en el subdirectorio /docs/utils/AI_Application/aidemo_sdk/examples/python_inference_on_PC/data, y el script se encuentra en el subdirectorio /docs/utils/AI_Application/aidemo_sdk/examples/python_inference_on_PC.

Siga el símbolo del sistema de secuencia de comandos para ejecutar la secuencia de comandos de yolov5_image.py para obtener el resultado de inferencia de la imagen estática. Detecte la corrección del modelo verificando que el cuadro de detección de la imagen de salida sea correcto o no.

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

# 3 Generación de modelos

La generación del modelo depende del compilador nncase, y las reglas específicas para usar el compilador nncase se pueden encontrar[K510_nncase_Developer_Guides.md](./K510_nncase_Developer_Guides.md). El script que genera el kmodel para YOLOV5s se encuentra en el subdirectorio /docs/utils/AI_Application/aidemo_sdk/scripts.

En el símbolo del sistema del script, ejecute el gen_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py para generar el kmodel correspondiente.

```shell
usage: gen_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py [-h] [--target TARGET] [--dump_dir DUMP_DIR] [--onnx ONNX] [--kmodel KMODEL]

optional arguments:
  -h, --help           show this help message and exit
  --target TARGET      target to run
  --dump_dir DUMP_DIR  temp folder to dump
  --onnx ONNX          onnx model path
  --kmodel KMODEL      kendryte model path
```

Cabe señalar que para minimizar el preprocesamiento en la CPU, las opciones de compilación en el script se configuran de la siguiente manera:

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

# 4 Validación del modelo

La validación del modelo depende de nncase simulator, y las reglas específicas para usar nncase simulator se pueden encontrar[en K510_nncase_Developer_Guides.md](./K510_nncase_Developer_Guides.md). Compruebe que el script kmodel de yolov5s se encuentra en el subdirectorio /docs/utils/AI_Application/aidemo_sdk/scripts.

En el símbolo del sistema de script, ejecute simu_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py para comprobar que el kmodel correspondiente se genera correctamente.

```shell
usage: sim_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py [-h] [--onnx ONNX] [--kmodel KMODEL]

optional arguments:
  -h, --help       show this help message and exit
  --onnx ONNX      original model file
  --kmodel KMODEL  kmodel file
```

Si la similitud del coseno es cercana a 1 o igual a 1, se garantiza la exactitud del kmodelo generado.

```text
output 0 cosine similarity : 0.9999450445175171
output 1 cosine similarity : 0.9999403953552246
output 2 cosine similarity : 0.9999019503593445
```

# 5 Escribir aplicaciones de IA

La validación del modelo depende del tiempo de ejecución de nncase, y las reglas específicas para usar el tiempo de ejecución de nncase se pueden encontrar[K510_nncase_Developer_Guides.md](./K510_nncase_Developer_Guides.md). Referencia de aplicación de IA`k510_buildroot/package/ai/code/object_detect`. En primer lugar, debe crear una instancia de detección de objetos y asignar espacio para la entrada y salida del modelo kmodel.

```c++
objectDetect od(obj_thresh, nms_thresh, net_len, {valid_width, valid_height});
od.load_model(kmodel_path);  // load kmodel
od.prepare_memory();  // memory allocation
```

Para implementar la copia de memoria cero, asocie la dirección de salida del ISP con la dirección de entrada kmodel

```c++
// define cv::Mat for ai input
// padding offset is (valid_width - valid_height) / 2 * valid_width
cv::Mat rgb24_img_for_ai(net_len, net_len, CV_8UC3, od.virtual_addr_input[0] + (valid_width - valid_height) / 2 * valid_width);
```

Configura el ancho y el alto de la salida del ISP

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

Configure el archivo de configuración de vídeo adecuado, video_height_r la altura de salida real del ISP y el desplazamiento de altura video_height entre los diferentes canales del ISP

```json
"/dev/video5":{
    "video5_used":1,
    "video5_width":320,
    "video5_height":320,
    "video5_height_r":240,
    "video5_out_format":0
}
```

Asociar las direcciones de entrada y salida con la input_tensor y output_tensor del kmodel

```c++
od.set_input(0);
od.set_output();
```

Ejecute el kmodel, obtenga el resultado de salida y realice el posprocesamiento

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

Finalmente, dibuje el cuadro de detección en el OSD para mostrar la salida

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

# 6 Compilar aplicaciones de IA

Utilizando la cadena de herramientas de compilación cruzada, las reglas específicas para la compilación de aplicaciones de IA se pueden consultar[K510_SDK_Build_and_Burn_Guide](./K510_SDK_Build_and_Burn_Guide.md).

**Descargo de responsabilidad de**traducción  
Para la comodidad de los clientes, Canaan utiliza un traductor de IA para traducir texto a varios idiomas, que pueden contener errores. No garantizamos la exactitud, fiabilidad o puntualidad de las traducciones proporcionadas. Canaan no será responsable de ninguna pérdida o daño causado por la confianza en la exactitud o fiabilidad de la información traducida. Si existe una diferencia de contenido entre las traducciones en diferentes idiomas, prevalecerá la versión en chino simplificado.

Si desea informar de un error o inexactitud de traducción, no dude en ponerse en contacto con nosotros por correo.
