![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 Guía para desarrolladores multimedia</font>**

<font face="黑体"  size=3>Versión del documento: V1.0.0</font>

<font face="黑体"  size=3>Publicado: 2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Renuncia**</font>
Los productos, servicios o características que compre estarán sujetos a los contratos comerciales y términos de Beijing Canaan Jiesi Information Technology Co., Ltd. ("la Compañía", la misma en adelante), y todos o parte de los productos, servicios o características descritos en este documento pueden no estar dentro del alcance de su compra o uso. Salvo que se acuerde lo contrario en el contrato, la Compañía renuncia a todas las representaciones o garantías, expresas o implícitas, en cuanto a la precisión, confiabilidad, integridad, marketing, propósito específico y no agresión de cualquier representación, información o contenido de este documento. A menos que se acuerde lo contrario, este documento se proporciona como una guía para su uso solamente.
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
## Propósito del documento
Este documento es un documento explicativo para el ejemplo de aplicación multimedia K510.
## Público objetivo
A quién va dirigido este documento:
- Desarrolladores de software
- Personal de soporte técnico

## Historial de revisiones

| El número de versión    | Modificado por | Fecha de revisión| Notas de revisión  |  
|  ------  |-------| -------| ------ |
| v1.0.0    |Grupos de software del sistema | 2022-03-09 | Lanzamiento del SDK V1.5 |
|     |     |      |   |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenido</font>**

[TOC]

# 1 API de codificador

## 1.1 Descripción del archivo de encabezado

k510_buildroot/package/encode_app/enc_interface.h

## 1.2 Descripciones de las funciones de la API

### 1.2.1 VideoEncoder_Create

【Descripción】

Crear un codificador de vídeo

【Gramática】

```c
EncoderHandle* VIdeoEncoder_Create(EncSettings *pCfg)
```

【Parámetros】

pCfg: Introduzca los parámetros de configuración de codificación

|            El nombre del parámetro             | Interpretación de parámetros                                                     |                           El rango de valores                           | Módulos de codificación aplicables |
| :---------------------------: | :----------------------------------------------------------- | :----------------------------------------------------------: | ------------ |
|            canal            | Número de canal, admite hasta 8 canales codificados                                   |                            [0，7]                            | jpeg、avc    |
|             Ancho             | Codifica el ancho de la imagen                                                 | avc: [128,2048], múltiplo de 8 <br/> jpeg: hasta 8192, múltiplo de 16 | jpeg、avc    |
|            altura             | Codificar la altura de la imagen                                                 | avc: [64,2048], múltiplo de 8 <br/> jpeg: hasta 8192, múltiplo de 2 | jpeg、avc    |
|           FrameRate           | Velocidad de fotogramas, que solo se puede configurar a unos pocos valores fijos                                    |                       (25,30,50,60,75)                       | jpeg、avc    |
|            rcMode             | El modo de control de velocidad de bits 0:CONST_QP 1:CBR 2:VBR<br />jpeg se fija a CONST_QP  |                       Ver RateCtrlMode                       | jpeg, avc    |
|            BitRate            | Tasa de bits de destino en modo CBR o tasa de bits más baja en modo VBR                    |                        [10,20000000]                         | Golpe          |
|          MaxBitRate           | La tasa de bits más alta en modo VBR                                          |                        [10,20000000]                         | Golpe          |
|            SliceQP            | El valor QP inicial, -1 para auto                                        |                avc:-1,jpeg[0,51]<br/>:[1,100]                | jpeg, avc    |
|             MinQP             | El valor mínimo de qp                                                     |                         [0,sliceqp]                          | Golpe          |
|             MaxQP             | El valor máximo de qp                                                     |                         [sliceqp,54]                         | Golpe          |
|            perfil            | profile_idc parámetros en SPS: 0: base 1:main 2:high 3:jpeg       |                            [0,3]                             | jpeg, avc    |
|             nivel             | level_idc parámetros en PS                                       |                           [10,42]                            | Golpe          |
|          AspectRatio          | Escala de visualización                                                     |                     Ver AVC_AspectRatio                      | jpeg, avc    |
|            FreqIDR            | El intervalo entre dos fotogramas idr                                              |                           [1,1000]                           | Golpe          |
|            gopLen             | Grupo de imagen, el intervalo entre dos marcos I                      |                           [1,1000]                           | Golpe          |
|          bEnableGDR           | Si se habilita la actualización en el marco                                             |                         [verdadero, falso]                         | Golpe          |
|            gdrMode            | Modo de actualización gdr: 0, actualización vertical 1, actualización horizontal                        |                       Ver GDRCtrlMode                        | Golpe          |
|          bEnableLTR           | Si los marcos de referencia a largo plazo están habilitados                                           |                         [verdadero, falso]                         | Golpe          |
|          roiCtrlMode          | Modo de control de ROI: 0: No usar roi 1: qp relativo 2: qp absoluto                 |                       Ver ROICtrlMode                        | Golpe          |
|       EncSliceSplitCfg        | Implementación dividida de sectores                                               |                                                              | Golpe          |
|         bSplitEnable          | Si la división de sectores está habilitada                                           |                         [verdadero, falso]                         | Golpe          |
|         u32SplitMode          | Modo de segmentación de cortes: 0: Dividido por bits. <br />1: Dividir por filas de macrobloques        |                            [0,1]                             | Golpe          |
|         u32SliceSize          | u32SplitMode=0, que indica el número de bytes por sector<br /> u32SplitMode=1, representa el número<br /> de filas de macrobloques por sector| u32SplitMode=[100,65535]<br />0,u32SplitMode=1,[1, (altura de la imagen +15)/16] | Golpe          |
|          entropíaModo          | Codificación de entropía, 0: CABAC 1: CAVLC                                |                      Ver EncEntropyMode                      | Golpe          |
|          encDblkCfg           | Configuración de filtrado de bloques                                                 |                                                              | Golpe          |
| disable_deblocking_filter_idc | El valor predeterminado es 0, lo que significa Acuerdo H.264                          |                            [0，2]                            | Golpe          |
|  slice_alpha_c0_offset_div2   | El valor predeterminado es 0, lo que significa Acuerdo H.264                          |                           [-6，6]                            | Golpe          |
|    slice_beta_offset_div2     | El valor predeterminado es 0, lo que significa Acuerdo H.264                          |                          [-6,   6]                           | Golpe          |

```c
typedef struct
{
    int                       channel;  //encode channel number
    unsigned short            width;
    unsigned short            height;
    unsigned char             FrameRate;
    RateCtrlMode              rcMode;
    unsigned int              BitRate;
    unsigned int              MaxBitRate;
    int                       SliceQP;  //auto: -1, or from 0 to 51
    int                       MinQP;//from 0 to SliceQP
    int                       MaxQP;//from SliceQP to 51
    AVC_Profile               profile;
    unsigned int              level;  //1 .. 51, 51 is 5.1
    AVC_AspectRatio           AspectRatio;
    int                       FreqIDR; //default value  : -1,IDR:number of frames between two IDR pictures;GDR:refresh period
    unsigned int              gopLen;  
    bool                      bEnableGDR;//gdr
    GDRCtrlMode               gdrMode;
    bool                      bEnableLTR;//Long Term reference

    ROICtrlMode               roiCtrlMode;
    EncSliceSplitCfg          sliceSplitCfg;
    EncEntropyMode            entropyMode;//Profile is set to AVC_MAIN or AVC_HIGH is valid
    EncDblkCfg                encDblkCfg;
}EncSettings;
typedef enum
{
    CONST_QP,
    CBR,
    VBR
} RateCtrlMode;
typedef enum
{
    AVC_C_BASELINE,
    AVC_MAIN,
    AVC_HIGH,
    JPEG
} AVC_Profile;
typedef enum
{
    ASPECT_RATIO_AUTO,
    ASPECT_RATIO_4_3,
    ASPECT_RATIO_16_9,
    ASPECT_RATIO_NONE
} AVC_AspectRatio;
typedef struct
{
    unsigned int          s32X;
    unsigned int          s32Y;
    unsigned int          u32Width;
    unsigned int          u32Height;
} RECT_S;
typedef struct
{
    unsigned int          uIndex;//index[0-7]
    bool                  bEnable;
    int                   uQpValue;
    RECT_S                stRect;
} EncROICfg;
typedef enum
{
    ROI_QP_TABLE_NONE,
    ROI_QP_TABLE_RELATIVE,//[-32,31],6 LSBs effective
    ROI_QP_TABLE_ABSOLUTE,//[0,51],6 LSBs effective
} ROICtrlMode;
typedef enum
{
    GDR_VERTICAL = 0,
    GDR_HORIZONTAL,
    GDR_CTRLMAX,
} GDRCtrlMode;
typedef struct
{
    bool bSplitEnable;
    unsigned int u32SplitMode; // 0:splite by byte; 1:splite by slice count
    unsigned int u32SliceSize;
}EncSliceSplitCfg;

typedef enum
{
    ENTROPY_MODE_CABAC = 0,
    ENTROPY_MODE_CAVLC,
}EncEntropyMode;

typedef struct
{
    unsigned int  disable_deblocking_filter_idc;//[0,2]
    int  slice_alpha_c0_offset_div2;//[-6,6]
    int  slice_beta_offset_div2;//[-6,6]
}EncDblkCfg;
```

【Valor de retorno】

```c
typedef void* EncoderHandle
```

### 1.2.2 VideoEncoder_SetRoiCfg

【Descripción】

configuración de roi, admite hasta 8 áreas rectangulares, el sistema de acuerdo con el número de índice de 0 ~ 7 para administrar el área de ROI, uIndex indica que el usuario establece el número de índice de ROI. Las regiones de ROI se pueden superponer entre sí, y cuando se produce una superposición, la prioridad entre las regiones de ROI aumenta secuencialmente del número de índice 0 al 7.

Se puede usar después de que se crea el codificador y antes de que se destruya. La región roi se puede ajustar dinámicamente durante el proceso de codificación.

【Gramática】

```c
EncStatus VideoEncoder_SetRoiCfg(EncoderHandle *hEnc,const EncROICfg*pEncRoiCfg);
```

【Parámetros】

hEnc: El identificador devuelto en el momento de la creación

pEncRoiCfg: Información de configuración de la zona roi

```c
typedef struct
{
    unsigned int          s32X;
    unsigned int          s32Y;
    unsigned int          u32Width;
    unsigned int          u32Height;
}RECT_S;

typedef struct 
{
    unsigned int          uIndex;//index[0-7]
    bool                  bEnable;
    int                   uQpValue;
    RECT_S                stRect;
}EncROICfg;
```

Descripción del parámetro

```text
uIndex     - 指定该roi区域索引号，范围0-7最多支持8个区域
bEnable    - 指定该区域是否使能，只有使能的区域才有效
uQpValue   - qp值，可以是相对qp或绝对qp，qp模式由EncSettings中roiCtrlMode属性决定。绝对qp范围                  [0,51]，相对qp范围[-31,31]
stRect     - roi矩形区域，s32X矩形左上角x值，s32Y矩形左上角y值，u32Width矩形宽度，u32Height矩形高度
```

【Valor de retorno】

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.3 VideoEncoder_SetLongTerm

【Descripción】

Establece el siguiente fotograma de la codificación en un marco de referencia a largo plazo. Se puede usar después de que se crea el codificador y antes de que se destruya. El atributo bEnableLTR de EncSettings determina si la característica está habilitada.

【Gramática】

```c
EncStatus VideoEncoder_SetLongTerm(EncoderHandle *hEnc);
```

【Parámetros】

hEnc: El identificador devuelto en el momento de la creación

【Valor de retorno】

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.4 VideoEncoder_UseLongTerm

【Descripción】

Establece la codificación en el siguiente fotograma mediante un marco de referencia a largo plazo. Se puede usar después de que se crea el codificador y antes de que se destruya. El atributo bEnableLTR de EncSettings determina si la característica está habilitada.

【Gramática】

```c
EncStatus VideoEncoder_UseLongTerm(EncoderHandle *hEnc);
```

【Parámetros】

hEnc: El identificador devuelto en el momento de la creación

【Valor de retorno】

```c
typedef enum
{
    Enc_SUCCESS = 0,
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.5 VideoEncoder_InsertUserData

【Descripción】

Insertar datos de usuario.

Se puede utilizar después de crear el codificador y antes de que se destruya, y el contenido de los datos del usuario se puede modificar en tiempo real durante el proceso de codificación. Los datos del usuario se insertarán en el área de datos SEI del marco IDR.

【Gramática】

```c
EncStatus      VideoEncoder_InsertUserData(EncoderHandle *hEnc,char*pUserData,unsigned int nlen);
```

【Parámetros】

hEnc: El identificador devuelto en el momento de la creación

pUserData: un puntero a los datos del usuario

nlen: Longitud de los datos del usuario (0, 1024)

【Valor de retorno】

```c
typedef enum
{
    Enc_SUCCESS = 0,
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.6 VideoEncoder_Destory

【Descripción】

Destruir el codificador de vídeo

【Gramática】

```c
EncStatus VideoEncoder_Destroy(EncoderHandle *hEnc)
```

【Parámetros】

hEnc: El identificador devuelto en el momento de la creación

【Valor de retorno】

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.7 VideoEncoder_EncodeOneFrame

【Descripción】

Codificar un fotograma de vídeo

【Gramática】

```c
EncStatus VideoEncoder_EncodeOneFrame(EncoderHandle *hEnc, EncInputFrame *input)
```

【Parámetros】

hEnc: El identificador devuelto en el momento de la creación

entrada: Ingrese los datos de video YUV

```c
typedef struct
{
    unsigned short width;
    unsigned short height;
    unsigned short stride;
    unsigned char *data;
}EncInputFrame;
```

【Valor de retorno】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.2.8 VideoEncoder_GetStream

【Descripción】

Obtiene el búfer de la secuencia de codificación de vídeo, Nota: Este espacio de búfer es asignado internamente por el codificador.

【Gramática】

```c
EncStatus VideoEncoder_GetStream(EncoderHandle *hEnc, EncOutputStream *output)
```

【Parámetros】

hEnc: El identificador devuelto en el momento de la creación

salida: Salida del búfer de datos de flujo codificado, bufSize es mayor que 0 para tener la salida

```c
typedef struct
{
    unsigned char *bufAddr;
    unsigned int bufSize; 
}EncOutputStream;
```

【Valor de retorno】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.2.9 VideoEncoder_GetStream_ByExtBuf

【Descripción】

Obtiene el búfer de la secuencia de codificación de vídeo, Nota: El consumidor debe asignar el espacio de búfer antes de llamar a esta función.

【Gramática】

```c
EncStatus VideoEncoder_GetStream(EncoderHandle *hEnc, EncOutputStream *output)
```

【Parámetros】

hEnc: El identificador devuelto en el momento de la creación

salida: Salida del búfer de datos de flujo codificado, bufSize es mayor que 0 para tener la salida

```c
typedef struct
{
    unsigned char *bufAddr;
    unsigned int bufSize; 
}EncOutputStream;
```

【Valor de retorno】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.3.0 VideoEncoder_ReleaseStream

【Descripción】

Liberar el búfer de la secuencia de codificación de vídeo

【Gramática】

```c
EncStatus VideoEncoder_ReleaseStream(EncoderHandle *hEnc, EncOutputStream *output)
```

【Parámetros】

- hEnc: El identificador devuelto en el momento de la creación
- salida:VideoEncoder_GetStream devuelto el búfer

【Valor de retorno】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

# 2 Diagrama de estructura de hardware y arquitectura de software

# 2.1 Diagrama de estructura de hardware

El diagrama de bloques de hardware del K510 es el siguiente:
![hardware_block_diagram](../zh/images/multimedia_guides/hardware_block_diagram.png)

Los datos recibidos del sensor de vídeo son procesados por MIPI DPHY, CSI, VI, isP para obtener los datos de la fuente yuv y almacenados en el DDR. El módulo codificador h264 lee datos del DDR, realiza operaciones de codificación y almacena los resultados de las operaciones en el DDR.

# 2.2 Arquitectura de software

La arquitectura de software de la plataforma de desarrollo multimedia es la siguiente:

![multimedia_block_diagram.png](../zh/images/multimedia_guides/multimedia_block_diagram.png)

en ello

- `libvenc`: Biblioteca de codificador para llamar al núcleo del codificador h264
- `libmediactl`: Biblioteca isp para controlar sensores
- `libaudio3a`: Biblioteca Audio3a para operaciones 3a en audio
- `alsa-lib`: Biblioteca de audio para controlar la interfaz de audio

# 3 Aplicación de demostración

## 3.1 Aplicación de codificación

El programa se coloca`/app/encode_app` en el directorio:

- `encode_app`: Programa de aplicación Encode
- El archivo yuv utilizado para las pruebas es de gran tamaño y no cabe en el paquete SDK

correr`encode_app`

| El nombre del parámetro | Interpretación de parámetros | El valor predeterminado | El rango de valores | Módulos de codificación aplicables |
|:-|:-|:-|:-|:-|
| Ayuda | Información de ayuda| | ||
| partir | El número de canales | NULO | [1,4] | jpeg、avc |
| Ch | Número de canal (basado en 0) | NULO | [0,3] | jpeg、avc |
| Yo | Ingrese el archivo YUV, solo**admite el formato** nv12| NULO | v4l2 <br> xxx.yuv | jpeg、avc |
| Dev | Nombre del dispositivo v4l2 | NULO | **sensor0:** /dev/video3 /dev/video4 <br> <br>sensor1:<br> **/dev/video7 /** dev/ <br> video8 <br> | Golpe |
| o | salida| NULO | rtsp <br> xxx.264 <br> xxx.MJPEG <br> xxx.JPEG | jpeg、avc |
| en | Ancho de imagen de salida | 1920 | avc: [128,2048], múltiplo de 8 <br> jpeg: hasta 8192, múltiplo de 16 | jpeg、avc |
| h | Altura de la imagen de salida | 1080 | avc: [64,2048], múltiplo de 8 <br> jpeg: hasta 8192, múltiplo de 2 | jpeg、avc |
| Fps | La cámara captura velocidades de fotogramas, que actualmente solo admiten 30pfs | 30 | 30 | Golpe |
| r | Velocidad de fotogramas de salida codificada | 30 | El número que puede ser divisible o divisible por fps | Golpe |
| inframes | Introduzca el número de fotogramas yuv | 0 | [0,32767] | jpeg、avc |
| fotogramas salientes | La salida de los fotogramas yuv, si es mayor que el parámetro -inframes, se repetirá la codificación | 0 | [0,32767] | jpeg、avc |
| Gop | Grupo de imagen, el intervalo entre dos marcos I | 25 | [1,1000] | Golpe |
| rcmode | Representa el modo de control de velocidad de bits 0:CONST_QP 1:CBR 2:VBR | CBR | [0,2] | Golpe |
| tasa de bits | Tasa de bits de destino en modo CBR o tasa de bits más baja en modo VBR, en KB | 4000 | [1,20000] | Golpe |
| maxbitrate | La tasa de bits más alta en modo VBR, en Kb | 4000 | [1,20000] | Golpe |
| perfil | profile_idc parámetros en SPS: 0: base 1:main 2:high 3:jpeg | AVC_HIGH | [0,3] | jpeg、avc |
| nivel | level_idc parámetros en SPS | 42 | [10,42] | Golpe |
| sliceqp | El valor QP inicial, -1 para auto | 25 | avc:-1,jpeg[0,51]<br/>:[1,100] | jpeg、avc |
| minqp | El valor mínimo de QP | 0 | [0,sliceqp] | Golpe |
| maxqp | El valor máximo de QP | 54 | [sliceqp,54] | Golpe |
| enableLTR | Habilita marcos de referencia a largo plazo y los parámetros especifican el período de actualización. 0: El ciclo de actualización no está habilitado. Positivo: establece periódicamente el marco de referencia y el siguiente marco se establece para usar el marco de referencia largo | 0 | [0,65535] | Golpe |
| rey | Archivo de configuración de Roi, que especifica varias regiones de roi | NULO | xxx.conf | Golpe |
| Æ | Habilitar AE | 0 | 0 - No habilita AE<br>1 - Habilitar AE |
| Conf | El archivo de configuración vl42 modifica los parámetros de configuración de v4l2 en función del archivo de configuración especificado y los parámetros de entrada de la línea de comandos | NULO | xxx.conf | Golpe |

### 3.1.1 Ingrese el archivo yuv y genere el archivo

```shell
./encode_app -split 1 -ch 0 -i your_file.yuv -o out.264 -w 1920 -h 1080 -inframes 10 -outframes 30
./encode_app -split 1 -ch 0 -i your_file.yuv -o out.mjpeg -w 1920 -h 1080 -inframes 10 -outframes 30
```

### 3.1.2 Entrada v4l2, salida rtsp push stream

#### 3.1.2.1 Canal único

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

Ejemplo de un comando ffplay pull:

```shell
 ffplay -rtsp_transport tcp rtsp://192.168.137.11:8554/testStream
```

- `rtsp://192.168.137.11:8554/testStream`Para la dirección URL de la transmisión rtsp, -rtsp_transport tcp significa usar tcp para transmitir datos de audio y video (udp se usa de forma predeterminada), y se puede agregar la opción -fflags nobuffer para evitar una mayor latencia debido al almacenamiento en caché del reproductor.

#### 3.1.2.2 Cámara única de doble canal

```shell
./encode_app -split 2 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -ch 1 -i v4l2 -dev /dev/video4 -o rtsp -w 1280 -h 720 -conf video_sample.conf
```

El comando ffplay pull stream es el mismo que el anterior.

#### 3.1.2.3 Cámaras duales

```shell
./encode_app -split 2 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -ch 1 -i v4l2 -dev /dev/video7 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

El comando ffplay pull stream es el mismo que el anterior.

#### 3.1.2.4 Prueba de ROI

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -sliceqp -1 -bitrate 2048 -roi roi_1920x1080.conf -conf video_sample.conf
```

formato de archivo roi

```json
{
  "roiCtrMode": 1,
  "roiRegion": [
    {
      "qpValue": -15,
      "qpRegion": {
        "left": 0,
        "top": 0,
        "width": 500,
        "heigth": 500
      }
    }
  ]
}
```

Descripción del parámetro:

```text
roiCtrMode - 1:相对qp  2:绝对qp
roiRegion  - roi区域，为多个区域数组，最多支持8个区域。
qpValue    - 指定该区域使用的qp值，相对qp范围:[-31,31]     绝对qp范围:[0,51]
qpRegion   - roi矩形区域
left       - 矩形区域的左上角X坐标
top        - 矩形区域的左上角Y坐标
width      - 矩形区域的宽度
heigth     - 矩形区域的高度
```

El comando ffplay pull stream es el mismo que el anterior.

### 3.1.3 Transformación de la velocidad de fotogramas

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -r 60 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

El comando ffplay pull stream es el mismo que el anterior.

### 3.1.4 Velocidades de fotogramas de entrada múltiple

VGA@75fps y 720p60 son compatibles actualmente

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 640 -h 480 -fps 75 -r 75 -conf video_sample_vga480p75.conf
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1280 -h 720 -fps 60 -r 60 -conf video_sample_720p60.conf
```

El comando ffplay pull stream es el mismo que el anterior.

### 3.1.5 rtsp push secuencias de audio y vídeo

```c
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -alsa 1 -ac 2 -ar 44100 -af 2 -ad hw:0 -conf video_sample.conf
```

El comando ffplay pull stream es el mismo que el anterior.

### 3.1.6 Precauciones

- Entorno operativo: Sensor de la placa central: IMX219_SENSOR

- Formato de dirección de flujo rtsp: rtsp://ip dirección: número de puerto / testStream, donde la dirección IP y el número de puerto son variables y el resto son fijos.

  Como: rtsp://192.168.137.11:8554/testStream, donde la dirección IP es 192.168.137.11, el número de puerto es 8554.

  Dirección IP: La dirección IP de la placa de desarrollo, ingrese ifconfig en la placa para obtener.

  Número de puerto: 8554 + <通道号>*2, los números de canal generalmente comienzan desde 0 (-ch 0, -ch 1...).

- Modo de transmisión RTSP: la transmisión RTSP correspondiente se puede reproducir a través de vlc o ffplay, y la transmisión de datos se puede transmitir a través del protocolo udp o TCP.

  1) rtp over udp播放:ffplay -rtsp_transport udp rtsp://192.168.137.11:8554/testStream

  2) rtp sobre tcp 播放: ffplay -rtsp_transport tcp rtsp://192.168.137.11:8554/testStream

  Se recomienda usar rtp sobre tcp para jugar para evitar la pantalla causada por la pérdida de paquetes udp.

## 3.2 ffmpeg

ffmpeg se coloca en el directorio /usr/local/bin.

- `ffmpeg`: aplicación ffmpeg.

correr`ffmpeg`

(1) Parámetro de libk510_h264 del codificador
| El nombre del parámetro | Interpretación de parámetros | El valor predeterminado | El rango de valores |
|:-|:-|:-|:-|
| g | tamaño gop | 25 | 1 ~ 1000 |
| b | tasa de bits | 4000000 | 0 ~ 20000000 |
| r | Velocidad de fotogramas, ya que los isps actualmente solo admiten 30 fps, por lo que el decodificador debe establecerse en 30 | 30 | 30 |
| idr_freq | Frecuencia IDR | -1 (sin IDR) | -1 ~256 |
| Qp | Al codificar con cqp, configure el valor qp | -1 (automático) | -1 ~ 100 |
| maxrate | El valor máximo de la tasa de bits | 0 | 20000000 |
| perfil | Perfiles admitidos | 2 (alto) | 0 - línea de base <br> 1 - principal <br> 2 - alto |
| nivel | Nivel de codificación | 42 | 10 ~ 42 |
| Sería | Relación de aspecto de la pantalla | 0 (automático) | 0 - auto <br> 1 - 4:3 <br> 2 - 16:9 <br> 3 - ninguno |
| Ch | número de canal | 0 | 0-7 |
| framesToEncode | El número de tramas codificadas | -1 (todos los fotogramas) | -1 ~16383 |

(2) Parámetros de libk510_jpeg del codificador
| El nombre del parámetro | Interpretación de parámetros | El valor predeterminado | El rango de valores |
|:-|:-|:-|:-|
| Qp | Al codificar con cqp, configure el valor qp | 25 | -1 ~ 100 |
| r | velocidad de fotogramas | 30 | 25 ~ 60 |
| Ch | canal de codificación | 0 | 0 ~ 7 |
| maxrate | Tasa de bits máxima. (0=ignorar) | 4000000 | 0 ~ 20000000 |
| Sería | relación de aspecto | 0 (automático) | 0 - auto <br> 1 - 4:3 <br> 2 - 16:9 <br> 3 - ninguno |

(3) El parámetro de libk510_video del dispositivo
| El nombre del parámetro | Interpretación de parámetros | El valor predeterminado | El rango de valores |
|:-|:-|:-|:-|
| wh | tamaño del marco | NULO | **para el codificador libk510_h264:**:<br>  hasta 2048x2048 <br> múltiplo de ancho de 8 <br> múltiplo de altura de 8 <br> min. ancho: 128 <br> min. alto: 64 <br> **para libk510_jpeg de codificador:** <br> hasta 8192x8192 <br> múltiplo de ancho de 16 <br> múltiplo de altura de 2 |
| Exp | parámetro de exposición | 0 | 0 ~ 128 |
| Agc | ganancia analógica | 0 | 0 ~ 232 |

(4) parámetro audio3a
| El nombre del parámetro | Interpretación de parámetros | El valor predeterminado | El rango de valores |
|:-|:-|:-|:-|
| sample_rate | Frecuencia de muestreo de audio | 16000 | 1 ~65535 |
| Agc | Modo de ganancia de audio | 3(AgcModeFixedDigital) | 0 - AgcModeUnchanged <br> 1 - AgcModeAdaptiveAnalog <br> 2 - AgcModeAdaptiveDigital <br> 3 - AgcModeFixedDigital |
| Ns | Nivel sonoro | 3 (Muy alto) | 0 - Bajo <br> 1 - Moderado <br> 2 - Alto <br> 3 - Muy alto |
| dsp_task | Posición de carrera de Auido3a | 1 (dsp) | 0 - cpu <br>1 - dsp |

Los parámetros configurables se pueden ver a través del comando de ayuda

```shell
ffmpeg -h encoder=libk510_h264 #查看k510编码器的参数
ffmpeg -h demuxer=v4l2 #查看demuxer的配置参数
ffmpeg -h filter=audio3a #查看audio3a的配置参数
```

El cuadro lógico para ffmpeg es el siguiente:

![ffmpeg_block_diagram](../zh/images/multimedia_guides/ffmpeg_block_diagram.png)

audio3a se utiliza para realizar operaciones 3a en el audio recibido y emitirlo, y su diagrama de bloques lógico es el siguiente:

![ffmpeg_canaan_audio3a](../zh/images/multimedia_guides/ffmpeg_canaan_audio3a.png)

### 3.2.1 Instrucciones de funcionamiento del programa

#### 3.2.1.1 Rtp stream push

##### 3.2.1.1.1. rtp push video stream

Ejemplo de un comando ffmpeg run:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.102.231.29:1234
```

Cuando 10.102.231.29 es la dirección receptora, se cambia de acuerdo con la situación real.
Presione "q" mientras el programa se está ejecutando para dejar de ejecutarse.

ffplay recibe el comando:

```shell
ffplay.exe -protocol_whitelist "file,udp,rtp" -i test.sdp -fflags nobuffer -analyzeduration 1000000 -flags low_delay
```

Test.sdp se configura de la siguiente manera.

```text
SDP:
v=0
o=- 0 0 IN IP4 127.0.0.1
s=No Name
c=IN IP4 10.102.231.29
t=0 0
a=tool:libavformat 58.76.100
m=video 1234 RTP/AVP 96
a=rtpmap:96 H264/90000
a=fmtp:96 packetization-mode=1
```

Descripción del parámetro .sdp:

- c=: Información de enlace de medios; EN: Tipo de red; IP4: Tipo de dirección; Seguido de la dirección IP (tenga en cuenta que es la dirección IP donde se encuentra el receptor, no la IP del remitente)
- m= es el comienzo de una sesión a nivel de medios, video:media type; 1234: Número de puerto; RTP/AVP: Protocolo de transporte; 96: Formato de carga útil en el encabezado rtp
Modifique la dirección IP y el número de puerto del receptor de acuerdo con la situación real, y tenga en cuenta que el número de puerto de rtp debe ser par.

##### 3.2.1.1.2. rtp push audio stream

Ejemplo de un comando ffmpeg run:

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f rtp rtp://10.100.232.11:1234
```

Cuando 10.100.232.11 es la dirección receptora, se modifica de acuerdo con la situación real.

- ac: Establece el número de canales de audio
- ar: Establece la frecuencia de muestreo de audio

El comando ffplay receive es el mismo que recibir una secuencia de vídeo, y el archivo sdp hace referencia al siguiente ejemplo.

```text
SDP:
v=0
o=- 0 0 IN IP4 127.0.0.1
s=No Name
c=IN IP4 10.100.232.11
t=0 0
a=tool:libavformat 58.76.100
m=audio 1234 RTP/AVP 97
b=AS:128
a=rtpmap:97 MPEG4-GENERIC/32000/2
a=fmtp:97 profile-level-id=1;mode=AAC-hbr;sizelength=13;indexlength=3;indexdeltalength=3; config=129056E500
```

##### 3.2.1.1.3 rtp push audio y vídeo

Ejemplo de un comando ffmpeg run:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234 -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

El comando ffplay receive es el mismo que recibir una secuencia de audio, y el archivo sdp hace referencia al siguiente ejemplo.

```text
SDP:
v=0
o=- 0 0 IN IP4 127.0.0.1
s=No Name
t=0 0
a=tool:libavformat 58.76.100
m=video 1234 RTP/AVP 96
c=IN IP4 10.100.232.11
a=rtpmap:96 H264/90000
a=fmtp:96 packetization-mode=1
m=audio 1236 RTP/AVP 97
c=IN IP4 10.100.232.11
b=AS:128
a=rtpmap:97 MPEG4-GENERIC/32000/2
a=fmtp:97 profile-level-id=1;mode=AAC-hbr;sizelength=13;indexlength=3;indexdeltalength=3; config=129056E500
```

#### 3.2.1.2 rtsp flujo push

Antes de que rtsp inserte la secuencia, debe implementar el servidor rtsp para enviar la secuencia de datos al servidor.

##### 3.2.1.2.1 rtsp secuencias de vídeo push

Ejemplo de un comando ffmpeg run:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -acodec copy -f rtsp rtsp://10.100.232.11:5544/live/test110
```

- `idr_freq`Para el intervalo de trama IDR, se requiere un múltiplo entero del GOP. Las transmisiones RTSP deben generar tramas IDR para extraerlas a las transmisiones.
- `rtsp://10.100.232.11:5544/live/test110`Es la dirección URL de la secuencia push-pull del servidor RTSP

Ejemplo de un comando ffplay pull:

```shell
ffplay.exe -protocol_whitelist "file,udp,rtp,tcp" -i rtsp://10.100.232.11:5544/live/test110
```

##### 3.2.1.2.2 rtsp secuencia de audio push

Ejemplo de un comando ffmpeg run:

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f rtsp rtsp://10.100.232.11:5544/live/test110
```

El comando ffplay pull stream es el mismo que el comando rtsp pull video stream.

##### 3.2.1.2.3 rtsp push audio video stream

Ejemplo de un comando ffmpeg run:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -f alsa -ac 2 -ar 32000 -i hw:0 -idr_freq 25 -vcodec libk510_h264 -acodec aac -f rtsp rtsp://10.100.232.11:5544/live/test110
```

El comando ffplay pull stream es el mismo que el comando rtsp pull video stream.

#### 3.2.1.3 flujo push rtmp

Antes de la transmisión rtmp, debe implementar el servidor rtmp para enviar la secuencia de datos al servidor. Los servidores que admiten el protocolo RTMP incluyen fms, nginx, srs, etc.

##### 3.2.1.3.1 rtmp empuja las transmisiones de vídeo

Ejemplo de un comando ffmpeg run:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`La dirección URL para enviar la secuencia al servidor rtmp  

Ejemplo de un comando ffplay pull:

```shell
ffplay -fflags nobuffer rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`Para extraer la dirección URL de la secuencia del servidor rtmp (las secuencias push son las mismas que la dirección de la secuencia de extracción), la opción -fflags nobuffer para evitar un aumento de la latencia debido al almacenamiento en caché del reproductor.

##### 3.2.1.3.2 rtmp secuencia de audio push

Ejemplo de un comando ffmpeg run:

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`La dirección URL para enviar la secuencia al servidor rtmp

El comando ffplay pull stream es el mismo que el comando rtmp pull video stream.

##### 3.2.1.3.3 rtmp push secuencias de audio y vídeo

Ejemplo de un comando ffmpeg run:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -f alsa -ac 2 -ar 32000 -i hw:0 -idr_freq 25 -vcodec libk510_h264 -acodec aac -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`La dirección URL para enviar la secuencia al servidor rtmp

El comando ffplay pull stream es el mismo que el comando rtmp pull video stream.

#### 3.2.1.4 audio3a

##### 3.2.1.4.1 Ejecute audio por separado

(1) Ejecute audio3a en la CPU
Ejemplo de un comando ffmpeg run:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000:dsp_task=0 -f rtp rtp://10.100.232.11:1234
```

(2) Ejecute audio3a en dsp
Ejecute dos ventanas telnet, ejecute el programador de tareas dsp y ffmpeg en ambas ventanas (ejecute primero el programador de tareas dsp)
El programador de tareas dsp ejecuta la instancia de comando:

```shell
cd /app/dsp_app_new/
./dsp_app /app/dsp_scheduler/scheduler.bin
```

Ejemplo de comando ffmpeg run:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000 -f rtp rtp://10.100.232.11:1234
```

##### 3.2.1.4.2 Ejecute audio3a y vídeo al mismo tiempo

(1) Ejecute audio3a en la CPU
Ejecute dos ventanas telnet, ejecute audio3a y video en ambas ventanas.
Ejemplo del comando de vídeo:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234
```

Ejemplo del comando audio3a:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000:dsp_task=0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

Ejecutar audio3a y video en la cpu al mismo tiempo producirá desbordamiento, se recomienda ejecutar audio3a en dsp
(2) Ejecute audio3a en dsp
Ejecute tres ventanas telnet, ejecute llamadas audio3a, video y programador dsp en cada una de las tres ventanas
El comando dsp task scheduler run es el mismo que ejecutar audio3a solo.

Ejemplo del comando audio3a:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000 -f rtp rtp://10.100.232.11:1236
```

Ejemplo del comando de vídeo:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234
```

- 10.100.232.11 es la dirección IP del receptor rtp.
- El contenido del archivo SDP del terminal receptor ffplay se puede obtener del registro impreso después de ejecutar el comando ffmpeg anterior.

#### 3.2.1.5 v4l2

Los parámetros configurables se pueden ver a través del comando de ayuda

```shell
ffmpeg -h demuxer=v4l2 #查看v4l2的配置参数
```

| El nombre del parámetro | Interpretación de parámetros | El valor predeterminado | El rango de valores |
| :-- | :-- | :-- | :-- |
| s | Resolución de imagen, como 1920x1080 | NULO | |
| r | Velocidad de fotogramas, actualmente solo admite 30 fps | 30 | 30 |
| isp | Encienda el hardware del ISP k510 | 0 | 0-1 |
| buf_type | búfer`类型`  v4l2 <br>1: V4L2_MEMORY_MMAP: para -vcodec copia<br>2: V4L2_MEMORY_USERPTR: para -vcodec libk510_h264 | 1 | 1 ~ 4 |
| Conf | Archivo de configuración v4l2 | NULO | |

Ejemplo de comando ffmpeg running: donde 10.100.232.11 es la dirección receptora, modificada según la situación real.

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234 -f alsa -ac 2 -ar 16000 -i hw:0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -i /dev/video3 -vcodec copy -y out.yuv
```

Ilustrar:

1. El tiempo de ejecución debe encontrarse en el directorio de ejecución`video_sampe.conf`, `imx219_0.conf`y los `imx219_1.conf`archivos están configurados, y los tres archivos están bajo`/encode_app/` el directorio.
2. El video que viene en tiempo real por la cámara está escrito como un archivo YUV, y debido a que el archivo YUV es muy grande, la velocidad de escritura DDR o NFS local no puede mantenerse al día, lo que puede causar la caída de fotogramas.

#### 3.2.1.6 Codificación JPEG

Salida de archivo:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_jpeg -y test.mjpeg
```

Descripción: El tiempo de ejecución debe estar ubicado en el directorio de ejecución`video_sampe.conf`, `imx219_0.conf`y `imx219_1.conf`los archivos están configurados, y los tres archivos están bajo`/encode_app/` el directorio.

El archivo de salida test.mjpeg se puede reproducir en el lado de la PC con ffplay

```shell
ffplay -i test.mjpeg
```

Flujo push:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_jpeg -an -f rtp rtp://10.100.232.11:1234
```

Las transmisiones de extracción de Ffplay están disponibles

#### 3.2.1.7 Codificación de multiplexación

Admite hasta 8 codificaciones simultáneas, puede usar el tamaño de fotograma de cada canal multiplicado por la velocidad de fotogramas y luego agregado, no exceda la cantidad de datos de 1080p60, -vcodec puede elegir h264 o jpeg.

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -filter_complex 'split=2[out1][out2]' -map '[out1]' -vcodec libk510_h264 -ch 0 -an -f rtp rtp://10.20.1.101:1234 -map '[out2]' -vcodec libk510_h264 -ch 1 -an -f rtp rtp://10.20.1.101:2236
```

```shell
ffmpeg -f v4l2 -s 480x360 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -filter_complex 'split=8[out1][out2][out3][out4][out5][out6][out7][out8]' -map '[out1]' -vcodec libk510_h264 -b:v 300000 -ch 0 -an -f rtp rtp://10.20.1.101:1234 -map '[out2]' -vcodec libk510_h264 -b:v 300000 -ch 1 -an -f rtp rtp://10.20.1.101:2322 -map '[out3]' -vcodec libk510_h264 -b:v 300000 -ch 2 -an -f rtp rtp://10.20.1.101:3086 -map '[out4]' -vcodec libk510_h264 -b:v 300000 -ch 3 -an -f rtp rtp://10.20.1.101:4234 -map '[out5]' -vcodec libk510_h264 -b:v 300000 -ch 4 -an -f rtp rtp://10.20.1.101:5216 -map '[out6]' -vcodec libk510_h264 -b:v 300000 -ch 5 -an -f rtp rtp://10.20.1.101:6788 -map '[out7]' -vcodec libk510_h264 -b:v 300000 -ch 6 -an -f rtp rtp://10.20.1.101:7230 -map '[out8]' -vcodec libk510_h264 -b:v 300000 -ch 7 -an -f rtp rtp://10.20.1.101:8976
```

Cuando use ffplay para extraer transmisiones, tenga cuidado de extraer solo un video, cambiar el video de otras carreteras cambiando el número de puerto en el archivo SDP o iniciar varias transmisiones ffplay.

### 3.2.2 Instrucciones de portabilidad del programa

`ffmpeg``ffmpeg`Migrado a la versión de código abierto 4.4,`xxx.patch` agregada para el Service Pack

- `ff_libk510_h264_encoder`: Codificación de hardware h264 de control, referenciada`libvenc.so`
- `ff_libk510_jpeg_encoder`: Controla la codificación de hardware jpeg, a la que se hace referencia`libvenc.so`
- v4l2: En v4l2.c, se agregó código relacionado con el hardware k510 y se V4L2_MEMORY_USERPTR y referenciar el tipo de búfer v4l2`libmediactl.so`.

#### 3.2.2.1 Comando de generación de parches

（1）

```shell
quilt new -p ab xxx.patch #在patches目录下生成xxx.patch文件
quilt add <filename> #添加修改前的文件
### 修改代码 ###
quilt refresh #修改内容被添加到xxx.patch
```

（2）
Copie xxx.patch en el directorio package/ffmpeg_canaan y modifique la ruta del archivo en el archivo de revisión de acuerdo con la ruta actual.

```shell
mv ../../patches/xxx.patch ../../package/ffmpeg_canaan
rm ../../patches/series
sed -i "s/\/dl\/ffmpeg_canaan\/ffmpeg-4.4//g" ../../package/ffmpeg_canaan/xxx.patch
```

#### 3.2.2.2 Configuración de ffmpeg

En el `package/ffmpeg_canaan/ffmpeg.mk`archivo, el núcleo de la CPU se puede modificar, la cadena de herramientas de compilación y la habilitación se puede realizar a través de la opción`ff_k510_video_demuxer` configee.`ff_libk510_jpeg_encoder` `ff_libk510_h264_encoder`

```shell
./configure \
    --cross-prefix=riscv64-linux- \
    --enable-cross-compile \
    --target-os=linux \
    --cc=riscv64-linux-gcc \
    --arch=riscv64 \
    --extra-ldflags="-L./" \
    --extra-ldflags="-ldl" \
    --extra-ldflags="-Wl,-rpath ." \
    --enable-static \
    --enable-libk510_video \
    --enable-libk510_h264 \
    --enable-libk510_jpeg \
    --enable-alsa \
    --disable-autodetect \
    --disable-ffplay \
    --disable-ffprobe \
    --disable-doc \
    --enalbe-audio3a \
    --enable-indev=v4l2 \
```

**Descargo de responsabilidad de**traducción  
Para la comodidad de los clientes, Canaan utiliza un traductor de IA para traducir texto a varios idiomas, que pueden contener errores. No garantizamos la exactitud, fiabilidad o puntualidad de las traducciones proporcionadas. Canaan no será responsable de ninguna pérdida o daño causado por la confianza en la exactitud o fiabilidad de la información traducida. Si existe una diferencia de contenido entre las traducciones en diferentes idiomas, prevalecerá la versión en chino simplificado.

Si desea informar de un error o inexactitud de traducción, no dude en ponerse en contacto con nosotros por correo.
