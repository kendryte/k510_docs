![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 Multimedia Entwicklerhandbuch</font>**

<font face="黑体"  size=3>Dokumentversion: V1.0.0</font>

<font face="黑体"  size=3>Veröffentlicht: 2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Verzichtserklärung**</font>
Die Produkte, Dienstleistungen oder Funktionen, die Sie erwerben, unterliegen den kommerziellen Verträgen und Bedingungen von Beijing Canaan Jiesi Information Technology Co., Ltd. ("das Unternehmen", dasselbe im Folgenden), und alle oder ein Teil der in diesem Dokument beschriebenen Produkte, Dienstleistungen oder Funktionen fallen möglicherweise nicht in den Rahmen Ihres Kaufs oder Ihrer Nutzung. Sofern im Vertrag nicht anders vereinbart, lehnt das Unternehmen alle ausdrücklichen oder stillschweigenden Zusicherungen oder Gewährleistungen hinsichtlich der Genauigkeit, Zuverlässigkeit, Vollständigkeit, des Marketings, des spezifischen Zwecks und der Nichtverletzung von Zusicherungen, Informationen oder Inhalten dieses Dokuments ab. Sofern nicht anders vereinbart, wird dieses Dokument nur als Leitfaden für die Verwendung zur Verfügung gestellt.
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
## Zweck des Dokuments
Dieses Dokument ist ein erläuterndes Dokument für das Anwendungsbeispiel K510 Multimedia.
## Zielgruppe
Für wen dieses Dokument bestimmt ist:
- Softwareentwickler
- Mitarbeiter des technischen Supports

## Revisionshistorie

| Die Versionsnummer    | Geändert von | Datum der Überarbeitung| Revisionshinweise  |  
|  ------  |-------| -------| ------ |
| v1.0.0    |Systemsoftwaregruppen | 2022-03-09 | SDK V1.5 veröffentlicht |
|     |     |      |   |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Inhalt</font>**

[TOC]

# 1 Encoder-API

## 1.1 Beschreibung der Header-Datei

k510_buildroot/Paket/encode_app/enc_interface.h

## 1.2 API-Funktionsbeschreibungen

### 1.2.1 VideoEncoder_Create

【Beschreibung】

Erstellen eines Video-Encoders

【Grammatik】

```c
EncoderHandle* VIdeoEncoder_Create(EncSettings *pCfg)
```

【Parameters】

pCfg: Geben Sie die Codierungskonfigurationsparameter ein

|            Der Parametername             | Parameter-Interpretation                                                     |                           Der Wertebereich                           | Anwendbare Codierungsmodule |
| :---------------------------: | :----------------------------------------------------------- | :----------------------------------------------------------: | ------------ |
|            Kanal            | Kanalnummer, unterstützt bis zu 8 codierte Kanäle                                   |                            [0，7]                            | jpeg、avc    |
|             Breite             | Codiert die Bildbreite                                                 | AVC: , Vielfaches von 8 [128,2048] JPEG: bis zu 8192, Vielfaches von 16 <br/> | jpeg、avc    |
|            Höhe             | Codieren der Höhe des Bilds                                                 | AVC: , Vielfaches von 8 [64,2048] JPEG: bis zu 8192, Vielfaches von 2 <br/> | jpeg、avc    |
|           Framerate           | Bildrate, die nur auf wenige feste Werte konfiguriert werden kann                                    |                       (25,30,50,60,75)                       | jpeg、avc    |
|            rcMode             | Bitratensteuerungsmodus 0:CONST_QP 1:CBR 2:VBR<br />jpeg ist auf CONST_QP festgelegt  |                       Siehe RateCtrlMode                       | jpeg, avc    |
|            Bitrate            | Zielbitrate im CBR-Modus oder niedrigste Bitrate im VBR-Modus                    |                        [10,20000000]                         | Takt          |
|          MaxBitRate           | Die höchste Bitrate im VBR-Modus                                          |                        [10,20000000]                         | Takt          |
|            SliceQP            | Der anfängliche QP-Wert, -1 für auto                                        | avc:-1,jpeg:[0,51]<br/>[1,100]                | jpeg, avc    |
|             MinQP             | Der minimale qp-Wert                                                     |                         [0,sliceqp]                          | Takt          |
|             MaxQP             | Der maximale qp-Wert                                                     |                         [sliceqp,54]                         | Takt          |
|            Profil            | profile_idc Parameter in SPS: 0: Basis 1:main 2:high 3:jpeg       |                            [0,3]                             | jpeg, avc    |
|             Niveau             | level_idc Parameter in PS                                       |                           [10,42]                            | Takt          |
|          AspectRatio          | Display-Skala                                                     |                     Siehe AVC_AspectRatio                      | jpeg, avc    |
|            FreqIDR            | Das Intervall zwischen zwei idr-Frames                                              |                           [1,1000]                           | Takt          |
|            gopLen             | Group Of Picture, das Intervall zwischen zwei I-Frames                      |                           [1,1000]                           | Takt          |
|          bEnableGDR           | Gibt an, ob die In-Frame-Aktualisierung aktiviert werden soll                                             |                         [true,false]                         | Takt          |
|            gdrMode            | DDR-Aktualisierungsmodus: 0, vertikale Aktualisierung 1, horizontale Aktualisierung                        |                       Siehe GDRCtrlMode                        | Takt          |
|          bEnableLTR           | Ob langfristige Referenzrahmen aktiviert sind                                           |                         [true,false]                         | Takt          |
|          roiCtrlMode          | ROI-Steuerungsmodus: 0: Verwenden Sie nicht ROI 1: Relativer qp 2: absoluter qp                 |                       Siehe ROICtrlMode                        | Takt          |
|       EncSliceSplitCfg        | Bereitstellung von Slice-Splits                                               |                                                              | Takt          |
|         bSplitEnable          | Ob die Slice-Aufteilung aktiviert ist                                           |                         [true,false]                         | Takt          |
|         u32SplitMode          | Slice-Segmentierungsmodus: 0: Aufgeteilt nach Bits. <br />1: Aufteilen nach Makroblockzeilen        |                            [0,1]                             | Takt          |
|         u32SliceSize          | u32SplitMode=0, das die Anzahl der Bytes pro Slice <br />angibt u32SplitMode=1, stellt die Anzahl<br /> der Makroblockzeilen pro Slice dar| u32SplitMode=0,u32SplitMode=[100,65535]<br />1,[1, (Bildhöhe +15)/16] | Takt          |
|          EntropieModus          | Entropiekodierung, 0: CABAC 1: CAVLC                                |                      Siehe EncEntropyMode                      | Takt          |
|          encDblkCfg           | Konfiguration der Blockfilterung                                                 |                                                              | Takt          |
| disable_deblocking_filter_idc | Der Standardwert ist 0, was H.264-Vereinbarung bedeutet.                          |                            [0，2]                            | Takt          |
|  slice_alpha_c0_offset_div2   | Der Standardwert ist 0, was H.264-Vereinbarung bedeutet.                          |                           [-6，6]                            | Takt          |
|    slice_beta_offset_div2     | Der Standardwert ist 0, was H.264-Vereinbarung bedeutet.                          |                          [-6,   6]                           | Takt          |

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

【Rückgabewert】

```c
typedef void* EncoderHandle
```

### 1.2.2 VideoEncoder_SetRoiCfg

【Beschreibung】

ROI-Einstellung, unterstützt bis zu 8 rechteckige Bereiche, das System entsprechend der Indexnummer von 0 ~ 7 zur Verwaltung des ROI-Bereichs, uIndex zeigt an, dass der Benutzer die Indexnummer des ROI festlegt. ROI-Regionen können übereinander gelegt werden, und wenn ein Overlay auftritt, erhöht sich die Priorität zwischen ROI-Regionen sequenziell von Indexnummer 0 auf 7.

Es kann verwendet werden, nachdem der Encoder erstellt wurde und bevor er zerstört wird. Der Roi-Bereich kann während des Kodierungsprozesses dynamisch angepasst werden.

【Grammatik】

```c
EncStatus VideoEncoder_SetRoiCfg(EncoderHandle *hEnc,const EncROICfg*pEncRoiCfg);
```

【Parameters】

hEnc: Das zum Zeitpunkt der Erstellung zurückgegebene Handle

pEncRoiCfg: Konfigurationsinformationen zur Roi-Zone

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

Beschreibung der Parameter

```text
uIndex     - 指定该roi区域索引号，范围0-7最多支持8个区域
bEnable    - 指定该区域是否使能，只有使能的区域才有效
uQpValue   - qp值，可以是相对qp或绝对qp，qp模式由EncSettings中roiCtrlMode属性决定。绝对qp范围                  [0,51]，相对qp范围[-31,31]
stRect     - roi矩形区域，s32X矩形左上角x值，s32Y矩形左上角y值，u32Width矩形宽度，u32Height矩形高度
```

【Rückgabewert】

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.3 VideoEncoder_SetLongTerm

【Beschreibung】

Legt den nächsten Frame der Codierung auf einen langfristigen Referenzrahmen fest. Es kann verwendet werden, nachdem der Encoder erstellt wurde und bevor er zerstört wird. Das bEnableLTR-Attribut in EncSettings bestimmt, ob die Funktion aktiviert ist.

【Grammatik】

```c
EncStatus VideoEncoder_SetLongTerm(EncoderHandle *hEnc);
```

【Parameters】

hEnc: Das zum Zeitpunkt der Erstellung zurückgegebene Handle

【Rückgabewert】

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.4 VideoEncoder_UseLongTerm

【Beschreibung】

Legt die Codierung mithilfe eines langfristigen Bezugsrahmens auf das nächste Frame fest. Es kann verwendet werden, nachdem der Encoder erstellt wurde und bevor er zerstört wird. Das bEnableLTR-Attribut in EncSettings bestimmt, ob die Funktion aktiviert ist.

【Grammatik】

```c
EncStatus VideoEncoder_UseLongTerm(EncoderHandle *hEnc);
```

【Parameters】

hEnc: Das zum Zeitpunkt der Erstellung zurückgegebene Handle

【Rückgabewert】

```c
typedef enum
{
    Enc_SUCCESS = 0,
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.5 VideoEncoder_InsertUserData

【Beschreibung】

Fügen Sie Benutzerdaten ein.

Es kann verwendet werden, nachdem der Encoder erstellt wurde und bevor er zerstört wird, und der Benutzerdateninhalt kann während des Codierungsprozesses in Echtzeit geändert werden. Die Benutzerdaten werden in den SEI-Datenbereich des IDR-Frames eingefügt.

【Grammatik】

```c
EncStatus      VideoEncoder_InsertUserData(EncoderHandle *hEnc,char*pUserData,unsigned int nlen);
```

【Parameters】

hEnc: Das zum Zeitpunkt der Erstellung zurückgegebene Handle

pUserData: Ein Zeiger auf Benutzerdaten

nlen: Länge der Benutzerdaten (0, 1024)

【Rückgabewert】

```c
typedef enum
{
    Enc_SUCCESS = 0,
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.6 VideoEncoder_Destory

【Beschreibung】

Zerstören des Video-Encoders

【Grammatik】

```c
EncStatus VideoEncoder_Destroy(EncoderHandle *hEnc)
```

【Parameters】

hEnc: Das zum Zeitpunkt der Erstellung zurückgegebene Handle

【Rückgabewert】

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.7 VideoEncoder_EncodeOneFrame

【Beschreibung】

Codieren eines Videoframes

【Grammatik】

```c
EncStatus VideoEncoder_EncodeOneFrame(EncoderHandle *hEnc, EncInputFrame *input)
```

【Parameters】

hEnc: Das zum Zeitpunkt der Erstellung zurückgegebene Handle

Eingang: Geben Sie die YUV-Videodaten ein

```c
typedef struct
{
    unsigned short width;
    unsigned short height;
    unsigned short stride;
    unsigned char *data;
}EncInputFrame;
```

【Rückgabewert】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.2.8 VideoEncoder_GetStream

【Beschreibung】

Ruft den Puffer des Videocodierungsstreams ab, Hinweis: Dieser Pufferspeicher wird intern vom Encoder zugewiesen.

【Grammatik】

```c
EncStatus VideoEncoder_GetStream(EncoderHandle *hEnc, EncOutputStream *output)
```

【Parameters】

hEnc: Das zum Zeitpunkt der Erstellung zurückgegebene Handle

Ausgabe: Ausgabe des codierten Datenstrompuffers, bufSize ist größer als 0, um die Ausgabe zu erhalten

```c
typedef struct
{
    unsigned char *bufAddr;
    unsigned int bufSize; 
}EncOutputStream;
```

【Rückgabewert】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.2.9 VideoEncoder_GetStream_ByExtBuf

【Beschreibung】

Ruft den Puffer des Videocodierungsstreams ab, Hinweis: Der Pufferspeicher muss vom Consumer zugewiesen werden, bevor diese Funktion aufgerufen wird.

【Grammatik】

```c
EncStatus VideoEncoder_GetStream(EncoderHandle *hEnc, EncOutputStream *output)
```

【Parameters】

hEnc: Das zum Zeitpunkt der Erstellung zurückgegebene Handle

Ausgabe: Ausgabe des codierten Datenstrompuffers, bufSize ist größer als 0, um die Ausgabe zu erhalten

```c
typedef struct
{
    unsigned char *bufAddr;
    unsigned int bufSize; 
}EncOutputStream;
```

【Rückgabewert】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.3.0 VideoEncoder_ReleaseStream

【Beschreibung】

Freigeben des Puffers des Videocodierungsdatenstroms

【Grammatik】

```c
EncStatus VideoEncoder_ReleaseStream(EncoderHandle *hEnc, EncOutputStream *output)
```

【Parameters】

- hEnc: Das zum Zeitpunkt der Erstellung zurückgegebene Handle
- Ausgabe:VideoEncoder_GetStream zurückgegebenen Puffers

【Rückgabewert】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

# 2 Hardware-Strukturdiagramm und Software-Architektur

# 2.1 Hardware-Strukturdiagramm

Das Hardware-Blockdiagramm des K510 lautet wie folgt:
![hardware_block_diagram](../zh/images/multimedia_guides/hardware_block_diagram.png)

Die vom Videosensor empfangenen Daten werden von MIPI DPHY, CSI, VI, isP verarbeitet, um die Yuv-Quelldaten zu erhalten und in der DDR gespeichert. Das h264-Encodermodul liest Daten aus dem DDR, führt Codierungsvorgänge durch und speichert die Ergebnisse der Operationen in der DDR.

# 2.2 Software-Architektur

Die Softwarearchitektur der Multimedia-Entwicklungsplattform lautet wie folgt:

![multimedia_block_diagram.png](../zh/images/multimedia_guides/multimedia_block_diagram.png)

darin

- `libvenc`: Encoder-Bibliothek zum Aufrufen des h264-Encoder-Kerns
- `libmediactl`: ISP-Bibliothek zur Steuerung von Sensoren
- `libaudio3a`: Audio3a-Bibliothek für 3a-Operationen auf Audio
- `alsa-lib`: Audiobibliothek zur Steuerung des Audio-Interfaces

# 3 Demo-App

## 3.1 Anwendung codieren

Das Programm befindet sich`/app/encode_app` im Verzeichnis:

- `encode_app`: Anwendungsprogramm codieren
- Die zum Testen verwendete Yuv-Datei ist groß und passt nicht in das SDK-Paket

laufen`encode_app`

| Der Parametername | Parameter-Interpretation | Der Standardwert | Der Wertebereich | Anwendbare Codierungsmodule |
|:-|:-|:-|:-|:-|
| Hilfe | Hilfe-Informationen| | ||
| trennen | Die Anzahl der Kanäle | NULL | [1,4] | jpeg、avc |
| Ch | Kanalnummer (0-basiert) | NULL | [0,3] | jpeg、avc |
| Ich | Geben Sie die YUV-Datei ein, unterstützen Sie nur**das nv12-Format**  | NULL | V4L2 <br> xxx.yuv | jpeg、avc |
| Dev | v4l2-Gerätename | NULL |**sensor0:** /dev/video3 /dev/video4 <br> <br>sensor1:<br> **/dev/video7 /  dev/** video8 <br> <br> | Takt |
| oder | Ausgabe| NULL | rtsp <br> xxx.264 <br> xxx.MJPEG xxx <br> .JPEG | jpeg、avc |
| in | Breite des Ausgabebilds | 1920 | AVC: , Vielfaches von 8 [128,2048] JPEG: bis zu 8192, Vielfaches von 16 <br> | jpeg、avc |
| h | Höhe des Ausgabebildes | 1080 | AVC: , Vielfaches von 8 [64,2048] JPEG: bis zu 8192, Vielfaches von 2 <br> | jpeg、avc |
| Ego-Shooter | Die Kamera erfasst Bildraten, die derzeit nur 30pfs unterstützen | 30 | 30 | Takt |
| r | Codierte Ausgabe-Bildrate | 30 | Die Zahl, die durch fps teilbar oder teilbar sein kann | Takt |
| Inframes | Geben Sie die Anzahl der Yuv-Frames ein | 0 | [0,32767] | jpeg、avc |
| Außenrahmen | Die Ausgabe der Yuv-Frames, wenn sie größer als der Parameter -inframes ist, wird wiederholt codiert | 0 | [0,32767] | jpeg、avc |
| Gop | Group Of Picture, das Intervall zwischen zwei I-Frames | 25 | [1,1000] | Takt |
| rcmode | Stellt den Bitratensteuerungsmodus 0:CONST_QP 1:CBR 2:VBR dar. | CBR | [0,2] | Takt |
| Bitrate | Zielbitrate im CBR-Modus oder niedrigste Bitrate im VBR-Modus, in KB | 4000 | [1,20000] | Takt |
| maxbitrate | Die höchste Bitrate im VBR-Modus, in Kb | 4000 | [1,20000] | Takt |
| Profil | profile_idc Parameter in SPS: 0: Basis 1:main 2:high 3:jpeg | AVC_HIGH | [0,3] | jpeg、avc |
| Niveau | level_idc Parameter in SPS | 42 | [10,42] | Takt |
| sliceqp | Der anfängliche QP-Wert, -1 für auto | 25 | avc:-1,jpeg:[0,51]<br/>[1,100] | jpeg、avc |
| minqp | Der minimale QP-Wert | 0 | [0,sliceqp] | Takt |
| maxqp | Der maximale QP-Wert | 54 | [sliceqp,54] | Takt |
| enableLTR | Aktiviert langfristige Bezugsrahmen, und Parameter geben den Aktualisierungszeitraum an. 0: Der Aktualisierungszyklus ist nicht aktiviert. Positiv: Legt regelmäßig das Bezugssystem fest und das nächste Frame wird so eingestellt, dass das lange Bezugssystem verwendet wird. | 0 | [0,65535] | Takt |
| König | Roi-Konfigurationsdatei, die mehrere Roi-Regionen angibt | NULL | xxx.conf | Takt |
| ae | AE aktivieren | 0 | 0 - Aktiviert AE 1 nicht<br> - AE aktivieren |
| conf | Die vl42-Konfigurationsdatei ändert die v4l2-Konfigurationsparameter basierend auf der angegebenen Konfigurationsdatei und den Befehlszeileneingabeparametern | NULL | xxx.conf | Takt |

### 3.1.1 Geben Sie die Yuv-Datei ein und geben Sie die Datei aus

```shell
./encode_app -split 1 -ch 0 -i your_file.yuv -o out.264 -w 1920 -h 1080 -inframes 10 -outframes 30
./encode_app -split 1 -ch 0 -i your_file.yuv -o out.mjpeg -w 1920 -h 1080 -inframes 10 -outframes 30
```

### 3.1.2 Eingang v4l2, Ausgang rtsp Push Stream

#### 3.1.2.1. Einkanal

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

Beispiel für einen ffplay-Pull-Befehl:

```shell
 ffplay -rtsp_transport tcp rtsp://192.168.137.11:8554/testStream
```

- `rtsp://192.168.137.11:8554/testStream`Für die rtsp-Stream-URL-Adresse bedeutet -rtsp_transport tcp, tcp zum Übertragen von Audio- und Videodaten zu verwenden (udp wird standardmäßig verwendet), und die nobuffer-Option -fflags kann hinzugefügt werden, um eine erhöhte Latenz aufgrund von Player-Caching zu vermeiden.

#### 3.1.2.2 Einzelkamera Dual Channel

```shell
./encode_app -split 2 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -ch 1 -i v4l2 -dev /dev/video4 -o rtsp -w 1280 -h 720 -conf video_sample.conf
```

Der ffplay-Pull-Stream-Befehl ist derselbe wie oben.

#### 3.1.2.3. Dual-Kameras

```shell
./encode_app -split 2 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -ch 1 -i v4l2 -dev /dev/video7 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

Der ffplay-Pull-Stream-Befehl ist derselbe wie oben.

#### 3.1.2.4 ROI-Test

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -sliceqp -1 -bitrate 2048 -roi roi_1920x1080.conf -conf video_sample.conf
```

ROI-Dateiformat

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

Parameterbeschreibung:

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

Der ffplay-Pull-Stream-Befehl ist derselbe wie oben.

### 3.1.3 Transformation der Bildrate

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -r 60 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

Der ffplay-Pull-Stream-Befehl ist derselbe wie oben.

### 3.1.4 Mehrere Eingangsframeraten

VGA@75fps und 720p60 werden derzeit unterstützt

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 640 -h 480 -fps 75 -r 75 -conf video_sample_vga480p75.conf
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1280 -h 720 -fps 60 -r 60 -conf video_sample_720p60.conf
```

Der ffplay-Pull-Stream-Befehl ist derselbe wie oben.

### 3.1.5 RTSP-Push-Audio- und Videostreams

```c
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -alsa 1 -ac 2 -ar 44100 -af 2 -ad hw:0 -conf video_sample.conf
```

Der ffplay-Pull-Stream-Befehl ist derselbe wie oben.

### 3.1.6 Vorsichtsmaßnahmen

- Betriebsumgebung: Core-Board-Sensor: IMX219_SENSOR

- RTSP-Stream-Adressformat: rtsp://ip Adresse: Portnummer/testStream, wobei IP-Adresse und Portnummer variabel und der Rest fest sind.

  Wie zum Beispiel: rtsp://192.168.137.11:8554/testStream, wo die IP-Adresse 192.168.137.11 ist, ist die Portnummer 8554.

  IP-Adresse: Geben Sie ifconfig auf dem Board ein, um die IP-Adresse des Entwicklungsboards zu erhalten.

  Portnummer: 8554 + <通道号>*2, Kanalnummern beginnen im Allgemeinen bei 0 (-ch 0, -ch 1...).

- RTSP-Stream-Modus abspielen: Der entsprechende RTSP-Stream kann über VLC oder FFPLAY abgespielt werden, und der Datenstrom kann über das UDP- oder TCP-Protokoll übertragen werden.

  1)rtp over udp播放:ffplay -rtsp_transport udp rtsp://192.168.137.11:8554/testStream

  2)RTP over TCP 播放: ffplay -rtsp_transport TCP rtsp://192.168.137.11:8554/testStream

  Es wird empfohlen, RTP über TCP für die Wiedergabe zu verwenden, um den durch den Verlust von UDP-Paketen verursachten Bildschirm zu vermeiden.

## 3,2 ffmpeg

ffmpeg befindet sich im Verzeichnis /usr/local/bin.

- `ffmpeg`: FFMPEG-App.

laufen`ffmpeg`

(1) Encoder libk510_h264 Parameter
| Der Parametername | Parameter-Interpretation | Der Standardwert | Der Wertebereich |
|:-|:-|:-|:-|
| g | gop Größe | 25 | 1 ~ 1000 |
| b | Bitrate | 4000000 | 0 ~ 20000000 |
| r | Bildrate, da ISPs derzeit nur 30fps unterstützen, sollte der Decoder auf 30 eingestellt werden | 30 | 30 |
| idr_freq | IDR-Frequenz | -1 (keine eingehende Überprüfung) | -1 ~ 256 |
| Qp | Konfigurieren Sie beim Codieren mit cqp den qp-Wert | -1(auto) | -1 ~ 100 |
| maxrate | Der maximale Wert der Bitrate | 0 | 20000000 |
| Profil | Unterstützte Profile | 2(hoch) | 0 - Baseline <br> 1 - Main <br> 2 - Hoch |
| Niveau | Kodierungsebene | 42 | 10 ~ 42 |
| würde | Bildschirm-Seitenverhältnis | 0（auto） | 0 - auto <br> 1 - 4:3 <br> 2 - 16:9 <br> 3 - keine |
| Ch | Kanalnummer | 0 | 0-7 |
| framesToEncode | Die Anzahl der codierten Frames | -1 (alle Frames) | -1 ~ 16383 |

(2) Encoder libk510_jpeg Parameter
| Der Parametername | Parameter-Interpretation | Der Standardwert | Der Wertebereich |
|:-|:-|:-|:-|
| Qp | Konfigurieren Sie beim Codieren mit cqp den qp-Wert | 25 | -1 ~ 100 |
| r | Framerate | 30 | 25 ~ 60 |
| Ch | Kanal kodieren | 0 | 0 ~ 7 |
| maxrate | Maximale Bitrate. (0=ignorieren) | 4000000 | 0 ~ 20000000 |
| würde | Seitenverhältnis | 0(auto) | 0 - auto <br> 1 - 4:3 <br> 2 - 16:9 <br> 3 - keine |

(3) Das Gerät libk510_video Parameter
| Der Parametername | Parameter-Interpretation | Der Standardwert | Der Wertebereich |
|:-|:-|:-|:-|
| Wh | Rahmengröße | NULL | **Für Drehgeber libk510_h264:: bis  2048x2048** Breite Vielfaches von 8 Höhe Vielfaches von 8 min. Breite:  128 min. <br> Höhe:  64 <br> <br>für Drehgeber libk510_jpeg:<br> <br> bis zu 8192x8192 <br>**** Breite Vielfaches von 16 <br> Höhe Vielfaches <br> von 2 <br> |
| Exp | Belichtungsparameter | 0 | 0 ~ 128 |
| Agc | Analogverstärkung | 0 | 0 ~ 232 |

(4) audio3a Parameter
| Der Parametername | Parameter-Interpretation | Der Standardwert | Der Wertebereich |
|:-|:-|:-|:-|
| sample_rate | Audio-Abtastrate | 16000 | 1 ~ 65535 |
| Agc | Audio-Verstärkungsmodus | 3(AgcModeFixedDigital) |0 - AgcModeUnchanged 1 - AgcModeAdaptiveAnalog 2 - AgcModeAdaptiveDigital 3  - <br> <br> AgcModeFixedDigital <br> |
| Ns | Lärmpegel | 3 (Sehr hoch) | 0 - Niedrig <br> 1 - Moderat <br> 2  - Hoch <br> 3 - Sehr Hoch |
| dsp_task | Auido3a Laufposition | 1 (dsp) | 0 - CPU <br>1 - DSP |

Konfigurierbare Parameter können über den Hilfebefehl eingesehen werden

```shell
ffmpeg -h encoder=libk510_h264 #查看k510编码器的参数
ffmpeg -h demuxer=v4l2 #查看demuxer的配置参数
ffmpeg -h filter=audio3a #查看audio3a的配置参数
```

Das logische Feld für ffmpeg lautet wie folgt:

![ffmpeg_block_diagram](../zh/images/multimedia_guides/ffmpeg_block_diagram.png)

audio3a wird verwendet, um 3a-Operationen auf dem empfangenen Audio auszuführen und auszugeben, und sein logisches Blockdiagramm lautet wie folgt:

![ffmpeg_canaan_audio3a](../zh/images/multimedia_guides/ffmpeg_canaan_audio3a.png)

### 3.2.1 Bedienungsanleitung des Programms

#### 3.2.1.1 RTP-Stream-Push

##### 3.2.1.1.1. RTP-Push-Videostream

Beispiel für einen ffmpeg-Ausführungsbefehl:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.102.231.29:1234
```

Wenn 10.102.231.29 die Empfangsadresse ist, wird sie entsprechend der tatsächlichen Situation geändert.
Drücken Sie "q", während das Programm ausgeführt wird, um die Ausführung zu beenden.

ffplay empfängt den Befehl:

```shell
ffplay.exe -protocol_whitelist "file,udp,rtp" -i test.sdp -fflags nobuffer -analyzeduration 1000000 -flags low_delay
```

Test.sdp ist wie folgt konfiguriert.

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

Beschreibung des SDP-Parameters:

- c=: Medienverknüpfungsinformationen; IN: Netzwerktyp; IP4: Adresstyp; Gefolgt von der IP-Adresse (beachten Sie, dass es sich um die IP-Adresse handelt, unter der sich der Empfänger befindet, nicht um die IP-Adresse des Absenders)
- m= ist der Beginn einer Sitzung auf Medienebene, video:media type; 1234: Portnummer; RTP/AVP: Transportprotokoll; 96: Payload-Format im RTP-Header
Ändern Sie die IP-Adresse und die Portnummer des Empfängers entsprechend der tatsächlichen Situation und beachten Sie, dass die Portnummer von rtp gerade sein muss.

##### 3.2.1.1.2. RTP-Push-Audiostream

Beispiel für einen ffmpeg-Ausführungsbefehl:

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f rtp rtp://10.100.232.11:1234
```

Wenn 10.100.232.11 die Empfangsadresse ist, wird sie entsprechend der tatsächlichen Situation geändert.

- ac: Legt die Anzahl der Audiokanäle fest
- ar: Legt die Audio-Abtastrate fest

Der ffplay receive-Befehl ist derselbe wie das Empfangen eines Videostreams, und die sdp-Datei bezieht sich auf das folgende Beispiel.

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

##### 3.2.1.1.3. RTP-Push-Audio- und Videostreams

Beispiel für einen ffmpeg-Ausführungsbefehl:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234 -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

Der Befehl ffplay receive ist derselbe wie das Empfangen eines Audiostreams, und die sdp-Datei bezieht sich auf das folgende Beispiel.

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

#### 3.2.1.2. RTSP-Pushstream

Bevor rtsp den Stream pusht, müssen Sie den rtsp-Server bereitstellen, um den Datenstream per Push auf den Server zu übertragen.

##### 3.2.1.2.1 RTSP-Push-Videostreams

Beispiel für einen ffmpeg-Ausführungsbefehl:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -acodec copy -f rtsp rtsp://10.100.232.11:5544/live/test110
```

- `idr_freq`Für das IDR-Frameintervall ist ein ganzzahliges Vielfaches des GOP erforderlich. RTSP-Streams müssen IDR-Frames generieren, um sie in Streams zu ziehen.
- `rtsp://10.100.232.11:5544/live/test110`Ist die Push-Pull-Stream-URL-Adresse des RTSP-Servers.

Beispiel für einen ffplay-Pull-Befehl:

```shell
ffplay.exe -protocol_whitelist "file,udp,rtp,tcp" -i rtsp://10.100.232.11:5544/live/test110
```

##### 3.2.1.2.2. RTSP-Push-Audiostream

Beispiel für einen ffmpeg-Ausführungsbefehl:

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f rtsp rtsp://10.100.232.11:5544/live/test110
```

Der Befehl ffplay pull stream ist derselbe wie der Befehl rtsp pull video stream.

##### 3.2.1.2.3. RTSP-Push-Audio-Videostream

Beispiel für einen ffmpeg-Ausführungsbefehl:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -f alsa -ac 2 -ar 32000 -i hw:0 -idr_freq 25 -vcodec libk510_h264 -acodec aac -f rtsp rtsp://10.100.232.11:5544/live/test110
```

Der Befehl ffplay pull stream ist derselbe wie der Befehl rtsp pull video stream.

#### 3.2.1.3 RTMP-Push-Stream

Vor dem rtmp-Streaming müssen Sie den rtmp-Server bereitstellen, um den Datenstrom per Push auf den Server zu übertragen. Zu den Servern, die das RTMP-Protokoll unterstützen, gehören fms, nginx, srs usw.

##### 3.2.1.3.1 RTMP pusht Videostreams

Beispiel für einen ffmpeg-Ausführungsbefehl:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`Die URL-Adresse zum Übertragen des Streams an den rtmp-Server  

Beispiel für einen ffplay-Pull-Befehl:

```shell
ffplay -fflags nobuffer rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`Um die URL-Adresse des Streams vom rtmp-Server abzurufen (Push-Streams sind mit der Adresse des Pull-Streams identisch), ist die nobuffer-Option -fflags nobuffer verfügbar, um eine erhöhte Latenz aufgrund des Player-Caching zu vermeiden.

##### 3.2.1.3.2. RTMP-Push-Audiostream

Beispiel für einen ffmpeg-Ausführungsbefehl:

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`Die URL-Adresse zum Übertragen des Streams an den rtmp-Server

Der Befehl ffplay pull stream ist derselbe wie der Befehl rtmp pull video stream.

##### 3.2.1.3.3 RTMP-Push-Audio- und Videostreams

Beispiel für einen ffmpeg-Ausführungsbefehl:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -f alsa -ac 2 -ar 32000 -i hw:0 -idr_freq 25 -vcodec libk510_h264 -acodec aac -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`Die URL-Adresse zum Übertragen des Streams an den rtmp-Server

Der Befehl ffplay pull stream ist derselbe wie der Befehl rtmp pull video stream.

#### 3.2.1.4 Audio3a

##### 3.2.1.4.1 Audio separat ausführen

(1) Führen Sie audio3a auf der CPU aus
Beispiel für einen ffmpeg-Ausführungsbefehl:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000:dsp_task=0 -f rtp rtp://10.100.232.11:1234
```

(2) Führen Sie audio3a auf dsp aus
Führen Sie zwei Telnet-Fenster aus, führen Sie dsp task scheduler und ffmpeg in beiden Fenstern aus (führen Sie zuerst dsp task scheduler aus)
Der DSP-Taskplaner führt die Befehlsinstanz aus:

```shell
cd /app/dsp_app_new/
./dsp_app /app/dsp_scheduler/scheduler.bin
```

ffmpeg run Befehl Beispiel:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000 -f rtp rtp://10.100.232.11:1234
```

##### 3.2.1.4.2 Audio3a und Video gleichzeitig ausführen

(1) Führen Sie audio3a auf der CPU aus
Führen Sie zwei Telnet-Fenster, Audio3a und Video in beiden Fenstern aus.
Beispiel für den Befehl video:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234
```

Beispiel für den Befehl audio3a:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000:dsp_task=0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

Das gleichzeitige Ausführen von audio3a und Video auf der CPU führt zu einem Überlauf, es wird empfohlen, audio3a auf dsp auszuführen
(2) Führen Sie audio3a auf dsp aus
Führen Sie drei Telnet-Fenster, Audio3a-Anrufe, Video und DSP-Scheduler auf jedem der drei Fenster aus
Der Befehl dsp task scheduler run ist derselbe wie das Ausführen von audio3a allein.

Beispiel für den Befehl audio3a:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000 -f rtp rtp://10.100.232.11:1236
```

Beispiel für den Befehl video:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234
```

- 10.100.232.11 ist die IP-Adresse des RTP-Empfängers.
- Der Inhalt der SDP-Datei des empfangenden Terminals ffplay kann dem gedruckten Protokoll entnommen werden, nachdem Sie den obigen ffmpeg-Befehl ausgeführt haben.

#### 3.2.1.5 v4l2

Konfigurierbare Parameter können über den Hilfebefehl eingesehen werden

```shell
ffmpeg -h demuxer=v4l2 #查看v4l2的配置参数
```

| Der Parametername | Parameter-Interpretation | Der Standardwert | Der Wertebereich |
| :-- | :-- | :-- | :-- |
| s | Bildauflösung, z. B. 1920 x 1080 | NULL | |
| r | Bildrate, unterstützt derzeit nur 30fps | 30 | 30 |
| ISP | Schalten Sie die k510 ISP-Hardware ein. | 0 | 0-1 |
| buf_type | v4l2 buffer`类型` <br> 1: V4L2_MEMORY_MMAP: for -vcodec copy 2: V4L2_MEMORY_USERPTR: for -vcodec<br>libk510_h264 | 1 | 1~2 |
| conf | v4l2-Konfigurationsdatei | NULL | |

Beispiel für den ausführenden Befehl ffmpeg: wobei 10.100.232.11 die empfangende Adresse ist, die je nach tatsächlicher Situation geändert wird.

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234 -f alsa -ac 2 -ar 16000 -i hw:0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -i /dev/video3 -vcodec copy -y out.yuv
```

Illustrieren:

1. Die Laufzeit muss im Ausführungsverzeichnis gefunden werden`video_sampe.conf`, `imx219_0.conf`und die Dateien `imx219_1.conf`sind konfiguriert, und die drei Dateien befinden sich unter`/encode_app/` dem Verzeichnis.
2. Das Video, das in Echtzeit von der Kamera geliefert wird, wird als YUV-Datei geschrieben, und da die YUV-Datei sehr groß ist, kann die lokale DDR- oder NFS-Schreibgeschwindigkeit nicht mithalten, was zu einem Frame-Drop führen kann.

#### 3.2.1.6 JPEG-Codierung

Dateiausgabe:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_jpeg -y test.mjpeg
```

Beschreibung: Die Laufzeit muss sich im Ausführungsverzeichnis`video_sampe.conf` befinden, und die Dateien `imx219_0.conf`sind konfiguriert, und die drei Dateien befinden sich unter`imx219_1.conf`  `/encode_app/`dem Verzeichnis.

Die Ausgabedatei test.mjpeg kann auf der PC-Seite mit ffplay abgespielt werden

```shell
ffplay -i test.mjpeg
```

Push-Stream:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_jpeg -an -f rtp rtp://10.100.232.11:1234
```

Ffplay Pull Streams sind verfügbar

#### 3.2.1.7 Multiplexing-Codierung

Unterstützung bis zu 8 gleichzeitige Kodierung, Sie können die Bildgröße jedes Kanals multipliziert mit der Bildrate multipliziert und dann hinzufügen, überschreiten Sie nicht die Datenmenge von 1080p60, -vcodec kann h264 oder jpeg wählen.

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -filter_complex 'split=2[out1][out2]' -map '[out1]' -vcodec libk510_h264 -ch 0 -an -f rtp rtp://10.20.1.101:1234 -map '[out2]' -vcodec libk510_h264 -ch 1 -an -f rtp rtp://10.20.1.101:2236
```

```shell
ffmpeg -f v4l2 -s 480x360 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -filter_complex 'split=8[out1][out2][out3][out4][out5][out6][out7][out8]' -map '[out1]' -vcodec libk510_h264 -b:v 300000 -ch 0 -an -f rtp rtp://10.20.1.101:1234 -map '[out2]' -vcodec libk510_h264 -b:v 300000 -ch 1 -an -f rtp rtp://10.20.1.101:2322 -map '[out3]' -vcodec libk510_h264 -b:v 300000 -ch 2 -an -f rtp rtp://10.20.1.101:3086 -map '[out4]' -vcodec libk510_h264 -b:v 300000 -ch 3 -an -f rtp rtp://10.20.1.101:4234 -map '[out5]' -vcodec libk510_h264 -b:v 300000 -ch 4 -an -f rtp rtp://10.20.1.101:5216 -map '[out6]' -vcodec libk510_h264 -b:v 300000 -ch 5 -an -f rtp rtp://10.20.1.101:6788 -map '[out7]' -vcodec libk510_h264 -b:v 300000 -ch 6 -an -f rtp rtp://10.20.1.101:7230 -map '[out8]' -vcodec libk510_h264 -b:v 300000 -ch 7 -an -f rtp rtp://10.20.1.101:8976
```

Wenn Sie ffplay zum Abrufen von Streams verwenden, achten Sie darauf, nur ein Video zu ziehen, das Video anderer Straßen zu wechseln, indem Sie die Portnummer in der SDP-Datei ändern, oder starten Sie mehrere ffplay-Streams.

### 3.2.2 Anweisungen zur Programmportierung

`ffmpeg``ffmpeg`Portiert auf die Open-Source-Version 4.4,`xxx.patch` hinzugefügt für das Service Pack

- `ff_libk510_h264_encoder`: Steuerung der h264-Hardwarecodierung, referenziert`libvenc.so`
- `ff_libk510_jpeg_encoder`: Steuert die JPEG-Hardwarecodierung, referenziert`libvenc.so`
- v4l2: In v4l2.c wurde k510-Hardware-bezogener Code hinzugefügt, und der v4l2-Puffertyp V4L2_MEMORY_USERPTR und referenziert.`libmediactl.so`

#### 3.2.2.1 Befehl zur Patch-Generierung

（1）

```shell
quilt new -p ab xxx.patch #在patches目录下生成xxx.patch文件
quilt add <filename> #添加修改前的文件
### 修改代码 ###
quilt refresh #修改内容被添加到xxx.patch
```

（2）
Kopieren Sie xxx.patch in das Verzeichnis package/ffmpeg_canaan und ändern Sie den Dateipfad in der Patch-Datei entsprechend dem aktuellen Pfad.

```shell
mv ../../patches/xxx.patch ../../package/ffmpeg_canaan
rm ../../patches/series
sed -i "s/\/dl\/ffmpeg_canaan\/ffmpeg-4.4//g" ../../package/ffmpeg_canaan/xxx.patch
```

#### 3.2.2.2. ffmpeg-Konfiguration

In der `package/ffmpeg_canaan/ffmpeg.mk`Datei kann der CPU-Kern geändert werden, die Kompilierungs-Toolchain und die Aktivierung kann über die configee-Option`ff_k510_video_demuxer` erfolgen.`ff_libk510_jpeg_encoder` `ff_libk510_h264_encoder`

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

**Haftungsausschluss**für Übersetzungen  
Für die Bequemlichkeit der Kunden verwendet Canaan einen KI-Übersetzer, um Text in mehrere Sprachen zu übersetzen, die Fehler enthalten können. Wir übernehmen keine Gewähr für die Genauigkeit, Zuverlässigkeit oder Aktualität der bereitgestellten Übersetzungen. Canaan haftet nicht für Verluste oder Schäden, die durch das Vertrauen auf die Richtigkeit oder Zuverlässigkeit der übersetzten Informationen verursacht werden. Wenn es einen inhaltlichen Unterschied zwischen den Übersetzungen in verschiedenen Sprachen gibt, ist die vereinfachte chinesische Version maßgebend.

Wenn Sie einen Übersetzungsfehler oder eine Ungenauigkeit melden möchten, können Sie uns gerne per E-Mail kontaktieren.
