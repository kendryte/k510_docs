![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 Руководство разработчика мультимедиа</font>**

<font face="黑体"  size=3>Версия документа: V1.0.0</font>

<font face="黑体"  size=3>Опубликовано: 2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Отказ**</font>
Продукты, услуги или функции, которые вы покупаете, регулируются коммерческими контрактами и условиями Beijing Canaan Jiesi Information Technology Co., Ltd. («Компания», то же самое далее), и все или часть продуктов, услуг или функций, описанных в этом документе, могут не входить в сферу вашей покупки или использования. Если иное не оговорено в договоре, Компания отказывается от всех заявлений или гарантий, явных или подразумеваемых, в отношении точности, надежности, полноты, маркетинга, конкретной цели и ненападения любых заявлений, информации или содержания этого документа. Если не согласовано иное, настоящий документ предоставляется только в качестве руководства для использования.
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
## Назначение документа
Этот документ является пояснительным документом к примеру приложения K510 Multimedia.
## Целевая аудитория
Для кого предназначен этот документ:
- Разработчики программного обеспечения
- Персонал технической поддержки

## История изменений

| Номер версии    | Изменено | Дата пересмотра| Примечания к пересмотру  |  
|  ------  |-------| -------| ------ |
| v1.0.0    |Группы системного программного обеспечения | 2022-03-09 | Выпущен пакет SDK версии 1.5 |
|     |     |      |   |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Содержание</font>**

[ОГЛАВЛЕНИЯ]

# 1 API кодировщика

## 1.1 Описание файла заголовка

k510_buildroot/пакет/encode_app/enc_interface.ч

## 1.2 Описания функций API

### 1.2.1 VideoEncoder_Create

【Описание】

Создание видеокодера

【Грамматика】

```c
EncoderHandle* VIdeoEncoder_Create(EncSettings *pCfg)
```

【Параметры】

pCfg: Ввод параметров конфигурации кодировки

|            Имя параметра             | Интерпретация параметров                                                     |                           Диапазон значений                           | Применимые модули кодирования |
| :---------------------------: | :----------------------------------------------------------- | :----------------------------------------------------------: | ------------ |
|            канал            | Номер канала, поддерживает до 8 закодированных каналов                                   |                            [0，7]                            | jpeg、avc    |
|             Ширина             | Кодирует ширину изображения                                                 | avc: [128,2048], кратно 8 <br/> jpeg: до 8192, кратно 16 | jpeg、avc    |
|            высота             | Кодирование высоты изображения                                                 | avc: [64,2048], кратно 8 <br/> jpeg: до 8192, кратно 2 | jpeg、avc    |
|           Частота кадров           | Частота кадров, которая может быть настроена только на несколько фиксированных значений                                    |                       (25,30,50,60,75)                       | jpeg、avc    |
|            rcMode             | Режим управления битрейтом 0:CONST_QP 1:CBR 2:VBR<br />jpeg исправлен для CONST_QP  |                       Смотреть RateCtrlMode                       | jpeg,avc    |
|            БитРейт            | Целевой битрейт в режиме CBR или самый низкий битрейт в режиме VBR                    |                        [10,20000000]                         | удар          |
|          МаксБитРат           | Самый высокий битрейт в режиме VBR                                          |                        [10,20000000]                         | удар          |
|            SliceQP            | Начальное значение QP, -1 для авто                                        |                avc:-1,jpeg[0,51]<br/>:[1,100]                | jpeg,avc    |
|             МинQP             | Минимальное значение qp                                                     |                         [0,sliceqp]                          | удар          |
|             МаксQP             | Максимальное значение qp                                                     |                         [sliceqp,54]                         | удар          |
|            профиль            | параметры profile_idc в SPS: 0: base 1:main 2:high 3:jpeg       |                            [0,3]                             | jpeg,avc    |
|             уровень             | параметры level_idc в PS                                       |                           [10,42]                            | удар          |
|          АспектРатио          | Шкала дисплея                                                     |                     Посмотреть AVC_AspectRatio                      | jpeg,avc    |
|            ФрекИДР            | Интервал между двумя кадрами iDR                                              |                           [1,1000]                           | удар          |
|            gopЛен             | Группа рисунка, интервал между двумя I кадрами                      |                           [1,1000]                           | удар          |
|          bОбновляемыйДР           | Следует ли включать обновление в кадре                                             |                         [true,false]                         | удар          |
|            gdrMode            | Режим обновления gdr: 0, вертикальное обновление 1, горизонтальное обновление                        |                       См. GDRCtrlMode                        | удар          |
|          bУстранимыйLTR           | Включены ли долгосрочные системы отсчета                                           |                         [true,false]                         | удар          |
|          roiCtrlMode          | Режим управления ROI: 0: Не используйте ROI 1: относительный qp 2: абсолютный qp                 |                       Просмотреть ROICtrlMode                        | удар          |
|       ЭнкСлицеСплитКфг        | развертывание с разделением фрагментов                                               |                                                              | удар          |
|         bSplitEnable          | Включено ли разделение фрагментов                                           |                         [true,false]                         | удар          |
|         u32СплитМод          | Режим сегментации срезов: 0: Разделение по битам. <br />1: Разделение по строкам макроблока        |                            [0,1]                             | удар          |
|         u32СразрезРазмер          | u32SplitMode=0, указывающий количество байтов на фрагмент<br /> u32SplitMode=1, представляет количество<br /> строк макроблока на фрагмент| u32SplitMode=[100,65535]<br />0,u32SplitMode=1,[1, (высота изображения +15)/16] | удар          |
|          энтропияРежим          | Энтропийное кодирование, 0: CABAC 1: CAVLC                                |                      См. ЭнкЭнтропияМодель                      | удар          |
|          encDblkCfg           | Конфигурация фильтрации блоков                                                 |                                                              | удар          |
| disable_deblocking_filter_idc | Значение по умолчанию — 0, что означает соглашение H.264                          |                            [0，2]                            | удар          |
|  slice_alpha_c0_offset_div2   | Значение по умолчанию — 0, что означает соглашение H.264                          |                           [-6，6]                            | удар          |
|    slice_beta_offset_div2     | Значение по умолчанию — 0, что означает соглашение H.264                          |                          [-6,   6]                           | удар          |

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

【Возвращаемое значение】

```c
typedef void* EncoderHandle
```

### 1.2.2 VideoEncoder_SetRoiCfg

【Описание】

настройка roi, поддержка до 8 прямоугольных областей, система согласно номеру индекса 0 ~ 7 для управления областью ROI, uIndex указывает, что пользователь устанавливает индекс номера ROI. Регионы ROI могут быть наложены друг на друга, и при наложении приоритет между регионами ROI последовательно увеличивается с индекса No 0 до 7.

Его можно использовать после создания кодировщика и до его уничтожения. Область roi может динамически настраиваться в процессе кодирования.

【Грамматика】

```c
EncStatus VideoEncoder_SetRoiCfg(EncoderHandle *hEnc,const EncROICfg*pEncRoiCfg);
```

【Параметры】

hEnc: дескриптор, возвращаемый во время создания

pEncRoiCfg: сведения о конфигурации зоны Roi

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

Описание параметра

```text
uIndex     - 指定该roi区域索引号，范围0-7最多支持8个区域
bEnable    - 指定该区域是否使能，只有使能的区域才有效
uQpValue   - qp值，可以是相对qp或绝对qp，qp模式由EncSettings中roiCtrlMode属性决定。绝对qp范围                  [0,51]，相对qp范围[-31,31]
stRect     - roi矩形区域，s32X矩形左上角x值，s32Y矩形左上角y值，u32Width矩形宽度，u32Height矩形高度
```

【Возвращаемое значение】

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.3 VideoEncoder_SetLongTerm

【Описание】

Задает следующий кадр кодировки в долгосрочную систему отсчета. Его можно использовать после создания кодировщика и до его уничтожения. Атрибут bEnableLTR в EncSettings определяет, включена ли эта функция.

【Грамматика】

```c
EncStatus VideoEncoder_SetLongTerm(EncoderHandle *hEnc);
```

【Параметры】

hEnc: дескриптор, возвращаемый во время создания

【Возвращаемое значение】

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.4 VideoEncoder_UseLongTerm

【Описание】

Задает кодировку для следующего кадра, используя долгосрочную систему отсчета. Его можно использовать после создания кодировщика и до его уничтожения. Атрибут bEnableLTR в EncSettings определяет, включена ли эта функция.

【Грамматика】

```c
EncStatus VideoEncoder_UseLongTerm(EncoderHandle *hEnc);
```

【Параметры】

hEnc: дескриптор, возвращаемый во время создания

【Возвращаемое значение】

```c
typedef enum
{
    Enc_SUCCESS = 0,
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.5 VideoEncoder_InsertUserData

【Описание】

Вставка пользовательских данных.

Его можно использовать после создания кодировщика и до его уничтожения, а содержимое пользовательских данных может быть изменено в режиме реального времени в процессе кодирования. Пользовательские данные будут вставлены в область данных SEI кадра IDR.

【Грамматика】

```c
EncStatus      VideoEncoder_InsertUserData(EncoderHandle *hEnc,char*pUserData,unsigned int nlen);
```

【Параметры】

hEnc: дескриптор, возвращаемый во время создания

pUserData: указатель на пользовательские данные

nlen: Длина пользовательских данных (0, 1024)

【Возвращаемое значение】

```c
typedef enum
{
    Enc_SUCCESS = 0,
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.6 VideoEncoder_Destory

【Описание】

Уничтожение видеокодера

【Грамматика】

```c
EncStatus VideoEncoder_Destroy(EncoderHandle *hEnc)
```

【Параметры】

hEnc: дескриптор, возвращаемый во время создания

【Возвращаемое значение】

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.7 VideoEncoder_EncodeOneFrame

【Описание】

Кодирование видеокадры

【Грамматика】

```c
EncStatus VideoEncoder_EncodeOneFrame(EncoderHandle *hEnc, EncInputFrame *input)
```

【Параметры】

hEnc: дескриптор, возвращаемый во время создания

ввод: Ввод видеоданных YUV

```c
typedef struct
{
    unsigned short width;
    unsigned short height;
    unsigned short stride;
    unsigned char *data;
}EncInputFrame;
```

【Возвращаемое значение】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.2.8 VideoEncoder_GetStream

【Описание】

Получает буфер потока кодирования видео Примечание: Это буферное пространство выделяется внутренне кодировщиком.

【Грамматика】

```c
EncStatus VideoEncoder_GetStream(EncoderHandle *hEnc, EncOutputStream *output)
```

【Параметры】

hEnc: дескриптор, возвращаемый во время создания

output: Вывод закодированного буфера потоковых данных, bufSize больше 0, чтобы иметь вывод

```c
typedef struct
{
    unsigned char *bufAddr;
    unsigned int bufSize; 
}EncOutputStream;
```

【Возвращаемое значение】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.2.9 VideoEncoder_GetStream_ByExtBuf

【Описание】

Получает буфер потока кодирования видео Примечание: перед вызовом этой функции потребитель должен выделить буферное пространство.

【Грамматика】

```c
EncStatus VideoEncoder_GetStream(EncoderHandle *hEnc, EncOutputStream *output)
```

【Параметры】

hEnc: дескриптор, возвращаемый во время создания

output: Вывод закодированного буфера потоковых данных, bufSize больше 0, чтобы иметь вывод

```c
typedef struct
{
    unsigned char *bufAddr;
    unsigned int bufSize; 
}EncOutputStream;
```

【Возвращаемое значение】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.3.0 VideoEncoder_ReleaseStream

【Описание】

Освобождение буфера потока кодирования видео

【Грамматика】

```c
EncStatus VideoEncoder_ReleaseStream(EncoderHandle *hEnc, EncOutputStream *output)
```

【Параметры】

- hEnc: дескриптор, возвращаемый во время создания
- output:VideoEncoder_GetStream возвращенный буфер

【Возвращаемое значение】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

# 2 Схема структуры аппаратного обеспечения и архитектура программного обеспечения

# 2.1 Схема структуры оборудования

Аппаратная блок-схема K510 выглядит следующим образом:
![hardware_block_diagram](../zh/images/multimedia_guides/hardware_block_diagram.png)

Данные, полученные от видеодатчика, обрабатываются MIPI DPHY, CSI, VI, isP для получения исходных данных yuv и хранятся в DDR. Модуль кодировщика h264 считывает данные из DDR, выполняет операции кодирования и сохраняет результаты операций в DDR.

# 2.2 Архитектура программного обеспечения

Программная архитектура платформы разработки мультимедиа выглядит следующим образом:

![multimedia_block_diagram.png](../zh/images/multimedia_guides/multimedia_block_diagram.png)

в нем

- `libvenc`: Библиотека кодировщика для вызова ядра кодировщика h264
- `libmediactl`: Библиотека ISP для управления датчиками
- `libaudio3a`: Библиотека Audio3a для операций 3a над аудио
- `alsa-lib`: Аудио библиотека для управления аудиоинтерфейсом

# 3 Демонстрационное приложение

## 3.1 Кодирование приложения

Программа размещается`/app/encode_app` в каталоге:

- `encode_app`: Кодирование прикладной программы
- Файл yuv, используемый для тестирования, имеет большой размер и не помещается в пакет SDK

бежать`encode_app`

| Имя параметра | Интерпретация параметров | Значение по умолчанию | Диапазон значений | Применимые модули кодирования |
|:-|:-|:-|:-|:-|
| Справка | Справочная информация| | ||
| раскалывать | Количество каналов | НЕДЕЙСТВИТЕЛЬНЫЙ | [1,4] | jpeg、avc |
| ч | Номер канала (на основе 0) | НЕДЕЙСТВИТЕЛЬНЫЙ | [0,3] | jpeg、avc |
| я | Введите файл YUV, поддерживает только** формат ** nv12| НЕДЕЙСТВИТЕЛЬНЫЙ | v4l2 <br> xxx.yuv | jpeg、avc |
| разработчик | Имя устройства v4l2 | НЕДЕЙСТВИТЕЛЬНЫЙ | **sensor0:** /dev/video3 /dev/video4 <br> <br>sensor1:<br> ** /dev/video7 / ** dev/ <br> video8 <br> | удар |
| или | выпуск| НЕДЕЙСТВИТЕЛЬНЫЙ | rtsp <br> xxx.264 <br> xxx.MJPEG <br> xxx.JPEG | jpeg、avc |
| в | Ширина выходного изображения | 1920 | avc: [128,2048], кратно 8 <br> jpeg: до 8192, кратно 16 | jpeg、avc |
| h | Высота выходного изображения | 1080 | avc: [64,2048], кратно 8 <br> jpeg: до 8192, кратно 2 | jpeg、avc |
| кадров в секунду | Камера захватывает частоту кадров, которая в настоящее время поддерживает только 30pfs | 30 | 30 | удар |
| r | Закодированная частота выходных кадров | 30 | Число, которое может быть делимым или делимым на fps | удар |
| inframes | Введите количество кадров yuv | 0 | [0,32767] | jpeg、avc |
| аутфреймы | На выходе кадров yuv, если они больше параметра -inframes, будет повторена кодировка | 0 | [0,32767] | jpeg、avc |
| gop | Группа рисунка, интервал между двумя I кадрами | 25 | [1,1000] | удар |
| rcmode | Представляет режим управления битрейтом 0:CONST_QP 1:CBR 2:VBR | ЦБ РФ | [0,2] | удар |
| битрейт | Целевой битрейт в режиме CBR или самый низкий битрейт в режиме VBR, в КБ | 4000 | [1,20000] | удар |
| максбитрат | Самый высокий битрейт в режиме VBR, в Кб | 4000 | [1,20000] | удар |
| профиль | параметры profile_idc в SPS: 0: base 1:main 2:high 3:jpeg | AVC_HIGH | [0,3] | jpeg、avc |
| уровень | параметры level_idc в SPS | 42 | [10,42] | удар |
| sliceqp | Начальное значение QP, -1 для авто | 25 | avc:-1,jpeg[0,51]<br/>:[1,100] | jpeg、avc |
| minqp | Минимальное значение QP | 0 | [0,sliceqp] | удар |
| maxqp | Максимальное значение QP | 54 | [sliceqp,54] | удар |
| включитьLTR | Включает долгосрочные системы отсчета, а параметры определяют период обновления. 0: Цикл обновления не включен. Положительный: периодически устанавливает систему отсчета, а следующая система устанавливается для использования длинной системы отсчета | 0 | [0,65535] | удар |
| король | Файл конфигурации Roi, в котором указывается несколько областей ROI | НЕДЕЙСТВИТЕЛЬНЫЙ | х.конф | удар |
| аэ | Включить AE | 0 | 0 - Не включает AE<br>1 - Включить AE |
| Конф | Файл конфигурации vl42 изменяет параметры конфигурации v4l2 на основе указанного файла конфигурации и входных параметров командной строки | НЕДЕЙСТВИТЕЛЬНЫЙ | х.конф | удар |

### 3.1.1 Введите файл yuv и выведите файл

```shell
./encode_app -split 1 -ch 0 -i your_file.yuv -o out.264 -w 1920 -h 1080 -inframes 10 -outframes 30
./encode_app -split 1 -ch 0 -i your_file.yuv -o out.mjpeg -w 1920 -h 1080 -inframes 10 -outframes 30
```

### 3.1.2 Вход v4l2, выходной поток rtsp push

#### 3.1.2.1 Одноканальный

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

Пример команды извлечения ffplay:

```shell
 ffplay -rtsp_transport tcp rtsp://192.168.137.11:8554/testStream
```

- `rtsp://192.168.137.11:8554/testStream`Для URL-адреса потока RTSP -rtsp_transport tcp означает использование tcp для передачи аудио- и видеоданных (udp используется по умолчанию), а параметр -fflags nobuffer можно добавить, чтобы избежать увеличения задержки из-за кэширования проигрывателя.

#### 3.1.2.2 Однокамерная двухканальная камера

```shell
./encode_app -split 2 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -ch 1 -i v4l2 -dev /dev/video4 -o rtsp -w 1280 -h 720 -conf video_sample.conf
```

Команда ffplay pull stream такая же, как и выше.

#### 3.1.2.3 Двойные камеры

```shell
./encode_app -split 2 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -ch 1 -i v4l2 -dev /dev/video7 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

Команда ffplay pull stream такая же, как и выше.

#### 3.1.2.4 Тест на окупаемость инвестиций

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -sliceqp -1 -bitrate 2048 -roi roi_1920x1080.conf -conf video_sample.conf
```

формат файла roi

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

Описание параметра:

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

Команда ffplay pull stream такая же, как и выше.

### 3.1.3 Преобразование частоты кадров

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -r 60 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

Команда ffplay pull stream такая же, как и выше.

### 3.1.4 Несколько входных кадров

VGA@75fps и 720p60 в настоящее время поддерживаются

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 640 -h 480 -fps 75 -r 75 -conf video_sample_vga480p75.conf
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1280 -h 720 -fps 60 -r 60 -conf video_sample_720p60.conf
```

Команда ffplay pull stream такая же, как и выше.

### 3.1.5 rtsp push аудио и видео потоки

```c
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -alsa 1 -ac 2 -ar 44100 -af 2 -ad hw:0 -conf video_sample.conf
```

Команда ffplay pull stream такая же, как и выше.

### 3.1.6 Меры предосторожности

- Рабочая среда: Датчик основной платы: IMX219_SENSOR

- Формат адреса потока rtsp: rtsp://ip адрес: номер порта/testStream, где IP-адрес и номер порта являются переменными, а остальные фиксированными.

  Например: rtsp://192.168.137.11:8554/testStream, где IP-адрес 192.168.137.11, номер порта 8554.

  IP-адрес: IP-адрес платы разработки, введите ifconfig на плате для получения.

  Номер порта: 8554 + <通道号>*2, номера каналов обычно начинаются от 0 (-ch 0, -ch 1...). 

- Режим воспроизведения потока RTSP: соответствующий поток RTSP может воспроизводиться через vlc или ffplay, а поток данных может передаваться по протоколу udp или TCP.

  1)rtp over udp播放:ffplay -rtsp_transport udp rtsp://192.168.137.11:8554/testStream

  2)rtp over tcp 播放: ffplay -rtsp_transport tcp rtsp://192.168.137.11:8554/testStream

  Рекомендуется использовать rtp через tcp для воспроизведения, чтобы избежать экрана, вызванного потерей пакетов udp.

## 3.2 ffmpeg

ffmpeg помещается в каталог /usr/local/bin.

- `ffmpeg`: приложение ffmpeg.

бежать`ffmpeg`

(1) Параметр libk510_h264 кодировщика
| Имя параметра | Интерпретация параметров | Значение по умолчанию | Диапазон значений |
|:-|:-|:-|:-|
| g | размер gop | 25 | 1 ~ 1000 |
| b | битрейт | 4000000 | 0 ~ 20000000 |
| r | Частота кадров, так как isps в настоящее время поддерживают только 30 кадров в секунду, поэтому декодер должен быть установлен на 30 | 30 | 30 |
| idr_freq | Частота IDR | -1 (без IDR) | -1 ~ 256 |
| qp | При кодировании с помощью cqp настройте значение qp | -1(авто) | -1 ~ 100 |
| максрейт | Максимальное значение битрейта | 0 | 20000000 |
| профиль | Поддерживаемые профили | 2 (высокий) | 0 - базовый уровень <br> 1 - основной <br> 2 - высокий |
| уровень | Уровень кодирования | 42 | 10 ~ 42 |
| модальный глагол | Соотношение сторон экрана | 0 (авто) | 0 - авто <br> 1 - 4:3 <br> 2 - 16:9 <br> 3 - нет |
| ч | номер канала | 0 | 0-7 |
| framesToEncode | Количество закодированных кадров | -1 (все кадры) | -1 ~ 16383 |

(2) Параметры libk510_jpeg кодировщика
| Имя параметра | Интерпретация параметров | Значение по умолчанию | Диапазон значений |
|:-|:-|:-|:-|
| qp | При кодировании с помощью cqp настройте значение qp | 25 | -1 ~ 100 |
| r | частота кадров | 30 | 25 ~ 60 |
| ч | кодировать канал | 0 | 0 ~ 7 |
| максрейт | Максимальный битрейт. (0=игнорировать) | 4000000 | 0 ~ 20000000 |
| модальный глагол | относительное удлинение | 0 (авто) | 0 - авто <br> 1 - 4:3 <br> 2 - 16:9 <br> 3 - нет |

(3) Параметр libk510_video устройства
| Имя параметра | Интерпретация параметров | Значение по умолчанию | Диапазон значений |
|:-|:-|:-|:-|
| вт | размер рамы | НЕДЕЙСТВИТЕЛЬНЫЙ | **для энкодера libk510_h264:**:<br>  до 2048x2048 <br> ширина кратная 8 <br> высота кратная 8 <br> мин. ширина: 128 <br> мин. высота: 64 <br> **для энкодера libk510_jpeg:** <br> до 8192x8192 <br> ширина кратная 16 <br> высота кратная 2 |
| exp | параметр экспозиции | 0 | 0 ~128 |
| АГК | аналоговое усиление | 0 | 0 ~ 232 |

(4) параметр audio3a
| Имя параметра | Интерпретация параметров | Значение по умолчанию | Диапазон значений |
|:-|:-|:-|:-|
| sample_rate | Частота дискретизации звука | 16000 | 1 ~ 65535 |
| АГК | Режим усиления звука | 3 (AgcModeFixedDigital) | 0 - AgcModeUnchanged <br> 1 - AgcModeAdaptiveАналог <br> 2 - AgcModeAdaptiveDigital <br> 3 - AgcModeFixedDigital |
| нс | Уровень шума | 3 (очень высокий) | 0 - Низкий <br> 1 - Умеренный <br> 2 - Высокий <br> 3 - Очень Высокий |
| dsp_task | Позиция auido3a для бега | 1(dsp) | 0 - процессор <br>1 - dsp |

Настраиваемые параметры можно просмотреть с помощью команды help

```shell
ffmpeg -h encoder=libk510_h264 #查看k510编码器的参数
ffmpeg -h demuxer=v4l2 #查看demuxer的配置参数
ffmpeg -h filter=audio3a #查看audio3a的配置参数
```

Логическая рамка для ffmpeg выглядит следующим образом:

![ffmpeg_block_diagram](../zh/images/multimedia_guides/ffmpeg_block_diagram.png)

audio3a используется для выполнения операций 3a над полученным аудио и его вывода, а его логическая блок-схема выглядит следующим образом:

![ffmpeg_canaan_audio3a](../zh/images/multimedia_guides/ffmpeg_canaan_audio3a.png)

### 3.2.1 Инструкции по эксплуатации программы

#### 3.2.1.1 Потоковая передача RTP

##### 3.2.1.1.1. поток push-видео rtp

Пример команды запуска ffmpeg:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.102.231.29:1234
```

Если 10.102.231.29 является адресом получения, он изменяется в соответствии с фактической ситуацией.
Нажмите "q" во время работы программы, чтобы остановить работу.

ffplay получает команду:

```shell
ffplay.exe -protocol_whitelist "file,udp,rtp" -i test.sdp -fflags nobuffer -analyzeduration 1000000 -flags low_delay
```

Test.sdp настраивается следующим образом.

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

Описание параметра .sdp:

- c=: Информация о ссылках на СМИ; IN: Тип сети; IP4: Тип адреса; Затем следует IP-адрес (обратите внимание, что это IP-адрес, на котором находится получатель, а не IP-адрес отправителя)
- m= - начало сеанса уровня мультимедиа, video:media type; 1234: Номер порта; RTP/AVP: Транспортный протокол; 96: Формат полезных данных в заголовке rtp
Измените IP-адрес и номер порта приемника в соответствии с фактической ситуацией и обратите внимание, что номер порта rtp должен быть четным.

##### 3.2.1.1.2. поток push-аудио rtp

Пример команды запуска ffmpeg:

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f rtp rtp://10.100.232.11:1234
```

Если 10.100.232.11 является адресом получения, он изменяется в соответствии с фактической ситуацией.

- ac: задает количество аудиоканалов
- ar: Задает частоту дискретизации звука

Команда ffplay receive аналогична получению видеопотока, а sdp-файл ссылается на следующий пример.

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

##### 3.2.1.1.3 push-аудио- и видеопотоки rtp

Пример команды запуска ffmpeg:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234 -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

Команда ffplay receive аналогична получению аудиопотока, а sdp-файл ссылается на следующий пример.

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

#### 3.2.1.2 Push-поток RTSP

Перед отправкой потока rtsp необходимо развернуть rtsp-сервер для отправки потока данных на сервер.

##### 3.2.1.2.1 push-видеопотоки rtsp

Пример команды запуска ffmpeg:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -acodec copy -f rtsp rtsp://10.100.232.11:5544/live/test110
```

- `idr_freq`Для интервала кадров IDR требуется целое число, кратное GOP. Потоки RTSP должны генерировать кадры IDR для извлечения в потоки.
- `rtsp://10.100.232.11:5544/live/test110`URL-адрес потока push-pull сервера RTSP.

Пример команды извлечения ffplay:

```shell
ffplay.exe -protocol_whitelist "file,udp,rtp,tcp" -i rtsp://10.100.232.11:5544/live/test110
```

##### 3.2.1.2.2 rtsp push аудиопоток

Пример команды запуска ffmpeg:

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f rtsp rtsp://10.100.232.11:5544/live/test110
```

Команда ffplay pull stream аналогична команде rtsp pull video stream.

##### 3.2.1.2.3 rtsp push аудио видео поток

Пример команды запуска ffmpeg:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -f alsa -ac 2 -ar 32000 -i hw:0 -idr_freq 25 -vcodec libk510_h264 -acodec aac -f rtsp rtsp://10.100.232.11:5544/live/test110
```

Команда ffplay pull stream аналогична команде rtsp pull video stream.

#### 3.2.1.3 push-поток rtmp

Перед потоковой передачей rtmp необходимо развернуть rtmp-сервер для отправки потока данных на сервер. Серверы, поддерживающие протокол RTMP, включают fms, nginx, srs и т.д.

##### 3.2.1.3.1 rtmp толкает видеопотоки

Пример команды запуска ffmpeg:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`URL-адрес для отправки потока на rtmp-сервер  

Пример команды извлечения ffplay:

```shell
ffplay -fflags nobuffer rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`Чтобы извлечь URL-адрес потока с сервера rtmp (push-потоки совпадают с адресом вытягивающего потока), параметр -fflags nobuffer позволяет избежать увеличения задержки из-за кэширования проигрывателя.

##### 3.2.1.3.2 rtmp push аудиопоток

Пример команды запуска ffmpeg:

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`URL-адрес для отправки потока на rtmp-сервер

Команда ffplay pull stream аналогична команде rtmp pull video stream.

##### 3.2.1.3.3 push аудио- и видеопотоки rtmp

Пример команды запуска ffmpeg:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -f alsa -ac 2 -ar 32000 -i hw:0 -idr_freq 25 -vcodec libk510_h264 -acodec aac -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`URL-адрес для отправки потока на rtmp-сервер

Команда ffplay pull stream аналогична команде rtmp pull video stream.

#### 3.2.1.4 аудио3а

##### 3.2.1.4.1 Запуск аудио отдельно

(1) Запустите audio3a на процессоре
Пример команды запуска ffmpeg:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000:dsp_task=0 -f rtp rtp://10.100.232.11:1234
```

(2) Запуск audio3a на dsp
Запустите два окна telnet, запустите планировщик заданий DSP и ffmpeg в обоих окнах (сначала запустите планировщик заданий DSP)
Планировщик заданий dsp запускает экземпляр команды:

```shell
cd /app/dsp_app_new/
./dsp_app /app/dsp_scheduler/scheduler.bin
```

Пример команды ffmpeg run:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000 -f rtp rtp://10.100.232.11:1234
```

##### 3.2.1.4.2 Одновременный запуск аудио3a и видео

(1) Запустите audio3a на процессоре
Запустите два окна telnet, запустите audio3a и видео в обоих окнах.
Пример команды video:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234
```

Пример команды audio3a:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000:dsp_task=0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

Запуск audio3a и видео на процессоре одновременно приведет к переполнению, рекомендуется запускать audio3a на dsp
(2) Запуск audio3a на dsp
Запустите три окна telnet, запустите вызовы Audio3a, видео и планировщик DSP в каждом из трех окон
Команда запуска планировщика заданий dsp аналогична команде запуска только audio3a.

Пример команды audio3a:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000 -f rtp rtp://10.100.232.11:1236
```

Пример команды video:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234
```

- 10.100.232.11 — IP-адрес rtp-приемника.
- Содержимое SDP-файла приемного терминала ffplay можно получить из распечатанного журнала после выполнения приведенной выше команды ffmpeg.

#### 3.2.1.5 v4l2

Настраиваемые параметры можно просмотреть с помощью команды help

```shell
ffmpeg -h demuxer=v4l2 #查看v4l2的配置参数
```

| Имя параметра | Интерпретация параметров | Значение по умолчанию | Диапазон значений |
| :-- | :-- | :-- | :-- |
| s | Разрешение изображения, например 1920x1080 | НЕДЕЙСТВИТЕЛЬНЫЙ | |
| r | Частота кадров, в настоящее время поддержка только 30 кадров в секунду | 30 | 30 |
| интернет-провайдер | Включение оборудования k510 ISP | 0 | 0-1 |
| buf_type | Буфер v4l2`类型` <br>1: V4L2_MEMORY_MMAP: для -vcodec копия<br>2: V4L2_MEMORY_USERPTR: для -vcodec libk510_h264 | 1 | 1 ~ 4 |
| Конф | Конфигурационный файл v4l2 | НЕДЕЙСТВИТЕЛЬНЫЙ | |

Пример выполнения команды ffmpeg: где 10.100.232.11 — адрес получения, измененный в соответствии с фактической ситуацией.

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234 -f alsa -ac 2 -ar 16000 -i hw:0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -i /dev/video3 -vcodec copy -y out.yuv
```

Иллюстрировать:

1. Среда выполнения должна быть найдена в каталоге выполнения`video_sampe.conf`, `imx219_0.conf`и `imx219_1.conf`файлы настроены, а три файла находятся в`/encode_app/` каталоге. 
2. Видео, которое приходит в режиме реального времени камерой, записывается в виде файла YUV, и поскольку файл YUV очень большой, локальная скорость записи DDR или NFS не может идти в ногу, что может привести к падению кадра.

#### 3.2.1.6 Кодировка JPEG

Вывод файла:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_jpeg -y test.mjpeg
```

Описание: Среда выполнения должна быть расположена в каталоге выполнения`video_sampe.conf`, `imx219_0.conf`и `imx219_1.conf`файлы настроены, а три файла находятся в`/encode_app/` каталоге. 

Выходной файл test.mjpeg можно воспроизводить на стороне ПК с помощью ffplay

```shell
ffplay -i test.mjpeg
```

Push Stream:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_jpeg -an -f rtp rtp://10.100.232.11:1234
```

Доступны вытягивающие потоки Ffplay

#### 3.2.1.7 Мультиплексирование кодирования

Поддержка до 8 одновременных кодировок, вы можете использовать размер кадра каждого канала, умноженный на частоту кадров, а затем добавленный, не превышающий объем данных 1080p60, -vcodec может выбрать h264 или jpeg.

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -filter_complex 'split=2[out1][out2]' -map '[out1]' -vcodec libk510_h264 -ch 0 -an -f rtp rtp://10.20.1.101:1234 -map '[out2]' -vcodec libk510_h264 -ch 1 -an -f rtp rtp://10.20.1.101:2236
```

```shell
ffmpeg -f v4l2 -s 480x360 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -filter_complex 'split=8[out1][out2][out3][out4][out5][out6][out7][out8]' -map '[out1]' -vcodec libk510_h264 -b:v 300000 -ch 0 -an -f rtp rtp://10.20.1.101:1234 -map '[out2]' -vcodec libk510_h264 -b:v 300000 -ch 1 -an -f rtp rtp://10.20.1.101:2322 -map '[out3]' -vcodec libk510_h264 -b:v 300000 -ch 2 -an -f rtp rtp://10.20.1.101:3086 -map '[out4]' -vcodec libk510_h264 -b:v 300000 -ch 3 -an -f rtp rtp://10.20.1.101:4234 -map '[out5]' -vcodec libk510_h264 -b:v 300000 -ch 4 -an -f rtp rtp://10.20.1.101:5216 -map '[out6]' -vcodec libk510_h264 -b:v 300000 -ch 5 -an -f rtp rtp://10.20.1.101:6788 -map '[out7]' -vcodec libk510_h264 -b:v 300000 -ch 6 -an -f rtp rtp://10.20.1.101:7230 -map '[out8]' -vcodec libk510_h264 -b:v 300000 -ch 7 -an -f rtp rtp://10.20.1.101:8976
```

При использовании ffplay для извлечения потоков будьте осторожны, чтобы извлечь только одно видео, переключить видео других дорог, изменив номер порта в SDP-файле, или запустить несколько потоков ffplay.

### 3.2.2 Инструкции по переносу программ

`ffmpeg``ffmpeg`Портирован на версию с открытым исходным кодом 4.4,`xxx.patch` добавлен для пакета обновления

- `ff_libk510_h264_encoder`: Управление аппаратной кодировкой h264, ссылка`libvenc.so`
- `ff_libk510_jpeg_encoder`: Управляет аппаратной кодировкой jpeg, на которую ссылаются`libvenc.so`
- v4l2: В v4l2.c был добавлен аппаратный код k510, а тип буфера v4l2 V4L2_MEMORY_USERPTR и ссылки`libmediactl.so`. 

#### 3.2.2.1 Команда создания патчей

（1）

```shell
quilt new -p ab xxx.patch #在patches目录下生成xxx.patch文件
quilt add <filename> #添加修改前的文件
### 修改代码 ###
quilt refresh #修改内容被添加到xxx.patch
```

（2）
Скопируйте xxx.patch в каталог package/ffmpeg_canaan и измените путь к файлу в файле исправления в соответствии с текущим путем.

```shell
mv ../../patches/xxx.patch ../../package/ffmpeg_canaan
rm ../../patches/series
sed -i "s/\/dl\/ffmpeg_canaan\/ffmpeg-4.4//g" ../../package/ffmpeg_canaan/xxx.patch
```

#### 3.2.2.2 Конфигурация ffmpeg

В `package/ffmpeg_canaan/ffmpeg.mk`файле можно изменить ядро ЦП, цепочку инструментов компиляции и включить с помощью параметра`ff_k510_video_demuxer` configee.`ff_libk510_jpeg_encoder` `ff_libk510_h264_encoder` 

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

**Отказ от ответственности за **перевод  
Для удобства клиентов Canaan использует переводчик AI для перевода текста на несколько языков, которые могут содержать ошибки. Мы не гарантируем точность, надежность или своевременность предоставленных переводов. Компания Canaan не несет ответственности за любые убытки или ущерб, вызванные доверием к точности или надежности переведенной информации. При наличии разницы в содержании переводов на разные языки преимущественную силу имеет упрощенная версия на китайском языке. 

Если вы хотите сообщить об ошибке или неточности перевода, пожалуйста, не стесняйтесь обращаться к нам по почте.