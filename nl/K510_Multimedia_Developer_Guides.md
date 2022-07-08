![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 Multimedia Ontwikkelaarshandleiding</font>**

<font face="黑体"  size=3>Document versie: V1.0.0</font>

<font face="黑体"  size=3>Publicatiedatum: 2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Disclaimer**</font>
De producten, diensten of functies die u koopt, zijn onderworpen aan de commerciële contracten en voorwaarden van Beijing Canaan Jiesi Information Technology Co., Ltd. ("het Bedrijf", hierna hetzelfde), en alle of een deel van de producten, diensten of functies die in dit document worden beschreven, vallen mogelijk niet binnen het bereik van uw aankoop of gebruik. Tenzij anders overeengekomen in het contract, wijst het bedrijf alle verklaringen of garanties af, expliciet of impliciet, met betrekking tot de nauwkeurigheid, betrouwbaarheid, volledigheid, marketing, specifiek doel en niet-agressie van verklaringen, informatie of inhoud van dit document. Tenzij anders overeengekomen, wordt dit document uitsluitend verstrekt als leidraad voor gebruik.
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
## Doel van het document
Dit document is een toelichtend document voor het voorbeeld van de K510 Multimedia-toepassing.
## Doelgroep
Voor wie dit document bedoeld is:
- Softwareontwikkelaars
- Technisch ondersteunend personeel

## Revisiegeschiedenis

| Het versienummer    | Gewijzigd door | Datum van herziening| Opmerkingen bij herziening  |  
|  ------  |-------| -------| ------ |
| v1.0.0    |Systeemsoftwaregroepen | 2022-03-09 | SDK V1.5 vrijgegeven |
|     |     |      |   |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Inhoud</font>**

[INHOUDSOPGAVE]

# 1 Encoder API

## 1.1 Beschrijving van headerbestand

k510_buildroot/pakket/encode_app/enc_interface.h

## 1.2 API-functiebeschrijvingen

### 1.2.1 VideoEncoder_Create

【Beschrijving】

Een video-encoder maken

【Grammatica】

```c
EncoderHandle* VIdeoEncoder_Create(EncSettings *pCfg)
```

【Parameters】

pCfg: Voer de coderingsconfiguratieparameters in

|            De parameternaam             | Parameterinterpretatie                                                     |                           Het waardebereik                           | Toepasselijke coderingsmodules |
| :---------------------------: | :----------------------------------------------------------- | :----------------------------------------------------------: | ------------ |
|            kanaal            | Kanaalnummer, ondersteunt tot 8 gecodeerde kanalen                                   |                            [0，7]                            | jpeg、avc    |
|             Breedte             | Codeert de afbeeldingsbreedte                                                 | avc: [128,2048], veelvoud van 8 <br/> jpeg: tot 8192, veelvoud van 16 | jpeg、avc    |
|            hoogte             | De hoogte van de afbeelding coderen                                                 | avc: [64,2048], veelvoud van 8 <br/> jpeg: tot 8192, veelvoud van 2 | jpeg、avc    |
|           Framerate           | Framesnelheid, die alleen kan worden geconfigureerd voor een vast aantal waarden                                    |                       (25,30,50,60,75)                       | jpeg、avc    |
|            rcMode             | Bitrate control mode 0:CONST_QP 1:CBR 2:VBR<br />jpeg is vastgezet op CONST_QP  |                       Zie RateCtrlMode                       | JPEG, AVC    |
|            Bitrate            | Doelbitsnelheid in CBR-modus of laagste bitsnelheid in VBR-modus                    |                        [10,20000000]                         | aaien          |
|          Maxbitrate           | De hoogste bitsnelheid in VBR-modus                                          |                        [10,20000000]                         | aaien          |
|            SliceQP            | De initiële QP-waarde, -1 voor automatisch                                        |                AVC: -1, jpeg[0,51]<br/>:[1,100]                | JPEG, AVC    |
|             MinQP             | De minimale qp-waarde                                                     |                         [0,sliceqp]                          | aaien          |
|             MaxQP             | De maximale qp-waarde                                                     |                         [SliceQP,54]                         | aaien          |
|            profiel            | profile_idc parameters in SPS: 0: basis 1:main 2:hoog 3:jpeg       |                            [0,3]                             | JPEG, AVC    |
|             niveau             | level_idc parameters in PS                                       |                           [10,42]                            | aaien          |
|          Aspectratio          | Weegschaal weergeven                                                     |                     Bekijk AVC_AspectRatio                      | JPEG, AVC    |
|            FreqIDR            | Het interval tussen twee idr-frames                                              |                           [1,1000]                           | aaien          |
|            gopLen             | Group Of Picture, het interval tussen twee I-frames                      |                           [1,1000]                           | aaien          |
|          bEnableGDR           | In-frame vernieuwen inschakelen                                             |                         [waar, onwaar]                         | aaien          |
|            GDRMode            | gdr-vernieuwingsmodus: 0, verticaal vernieuwen 1, horizontaal vernieuwen                        |                       Zie GDRCtrlMode                        | aaien          |
|          bEnableLTR           | Of referentiekaders op lange termijn zijn ingeschakeld                                           |                         [waar, onwaar]                         | aaien          |
|          roiCtrlMode          | ROI-controlemodus: 0: Gebruik geen roi 1: relatieve qp 2: absolute qp                 |                       Zie ROICtrlMode                        | aaien          |
|       EncSliceSplitCfg        | implementatie van slice split                                               |                                                              | aaien          |
|         bSplitEnable          | Of segmentsplitsing is ingeschakeld                                           |                         [waar, onwaar]                         | aaien          |
|         u32SplitMode          | Segmentatiemodus: 0: Splitsen door bits. <br />1: Splitsen door macroblokrijen        |                            [0,1]                             | aaien          |
|         u32SliceSize          | u32SplitMode=0, dat het aantal bytes per segment <br />u32SplitMode=1 aangeeft, staat voor het aantal<br /> macroblokrijen per segment| u32SplitMode=[100,65535]<br />0,u32SplitMode=1,[1, (beeldhoogte +15)/16] | aaien          |
|          entropieMode          | Entropiecodering, 0: CABAC 1: CAVLC                                |                      Zie EncEntropyMode                      | aaien          |
|          nlcDblkCfg           | Configuratie van blokfiltering                                                 |                                                              | aaien          |
| disable_deblocking_filter_idc | De standaardwaarde is 0, wat H.264-overeenkomst betekent                          |                            [0，2]                            | aaien          |
|  slice_alpha_c0_offset_div2   | De standaardwaarde is 0, wat H.264-overeenkomst betekent                          |                           [-6，6]                            | aaien          |
|    slice_beta_offset_div2     | De standaardwaarde is 0, wat H.264-overeenkomst betekent                          |                          [-6,   6]                           | aaien          |

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

【Retourwaarde】

```c
typedef void* EncoderHandle
```

### 1.2.2 VideoEncoder_SetRoiCfg

【Beschrijving】

roi instelling, ondersteuning tot 8 rechthoekige gebieden, het systeem volgens het indexnummer van 0 ~ 7 om het ROI-gebied te beheren, uIndex geeft aan dat de gebruiker het indexnummer van ROI instelt. ROI-regio's kunnen op elkaar worden gelegd en wanneer een overlay optreedt, neemt de prioriteit tussen ROI-regio's achtereenvolgens toe van indexnummer 0 tot 7.

Het kan worden gebruikt nadat de encoder is gemaakt en voordat deze wordt vernietigd. Het roi-gebied kan dynamisch worden aangepast tijdens het coderingsproces.

【Grammatica】

```c
EncStatus VideoEncoder_SetRoiCfg(EncoderHandle *hEnc,const EncROICfg*pEncRoiCfg);
```

【Parameters】

hEnc: de greep die wordt geretourneerd tijdens het maken

pEncRoiCfg: configuratie-informatie roizone

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

Parameter beschrijving

```text
uIndex     - 指定该roi区域索引号，范围0-7最多支持8个区域
bEnable    - 指定该区域是否使能，只有使能的区域才有效
uQpValue   - qp值，可以是相对qp或绝对qp，qp模式由EncSettings中roiCtrlMode属性决定。绝对qp范围                  [0,51]，相对qp范围[-31,31]
stRect     - roi矩形区域，s32X矩形左上角x值，s32Y矩形左上角y值，u32Width矩形宽度，u32Height矩形高度
```

【Retourwaarde】

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.3 VideoEncoder_SetLongTerm

【Beschrijving】

Hiermee stelt u het volgende frame van de codering in op een referentiekader voor de lange termijn. Het kan worden gebruikt nadat de encoder is gemaakt en voordat deze wordt vernietigd. Het kenmerk bEnableLTR in EncSettings bepaalt of de functie is ingeschakeld.

【Grammatica】

```c
EncStatus VideoEncoder_SetLongTerm(EncoderHandle *hEnc);
```

【Parameters】

hEnc: de greep die wordt geretourneerd tijdens het maken

【Retourwaarde】

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.4 VideoEncoder_UseLongTerm

【Beschrijving】

Hiermee stelt u de codering in op het volgende frame met behulp van een referentiekader voor de lange termijn. Het kan worden gebruikt nadat de encoder is gemaakt en voordat deze wordt vernietigd. Het kenmerk bEnableLTR in EncSettings bepaalt of de functie is ingeschakeld.

【Grammatica】

```c
EncStatus VideoEncoder_UseLongTerm(EncoderHandle *hEnc);
```

【Parameters】

hEnc: de greep die wordt geretourneerd tijdens het maken

【Retourwaarde】

```c
typedef enum
{
    Enc_SUCCESS = 0,
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.5 VideoEncoder_InsertUserData

【Beschrijving】

Voeg gebruikersgegevens in.

Het kan worden gebruikt nadat de encoder is gemaakt en voordat deze wordt vernietigd, en de inhoud van de gebruikersgegevens kan in realtime worden gewijzigd tijdens het coderingsproces. De gebruikersgegevens worden ingevoegd in het SEI-gegevensgebied van het IDR-frame.

【Grammatica】

```c
EncStatus      VideoEncoder_InsertUserData(EncoderHandle *hEnc,char*pUserData,unsigned int nlen);
```

【Parameters】

hEnc: de greep die wordt geretourneerd tijdens het maken

pUserData: een verwijzing naar gebruikersgegevens

nlen: Lengte van gebruikersgegevens (0, 1024)

【Retourwaarde】

```c
typedef enum
{
    Enc_SUCCESS = 0,
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.6 VideoEncoder_Destory

【Beschrijving】

Vernietig de video-encoder

【Grammatica】

```c
EncStatus VideoEncoder_Destroy(EncoderHandle *hEnc)
```

【Parameters】

hEnc: de greep die wordt geretourneerd tijdens het maken

【Retourwaarde】

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.7 VideoEncoder_EncodeOneFrame

【Beschrijving】

Een videoframe coderen

【Grammatica】

```c
EncStatus VideoEncoder_EncodeOneFrame(EncoderHandle *hEnc, EncInputFrame *input)
```

【Parameters】

hEnc: de greep die wordt geretourneerd tijdens het maken

invoer: Voer de YUV-videogegevens in

```c
typedef struct
{
    unsigned short width;
    unsigned short height;
    unsigned short stride;
    unsigned char *data;
}EncInputFrame;
```

【Retourwaarde】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.2.8 VideoEncoder_GetStream

【Beschrijving】

Hiermee wordt de buffer van de videocoderingsstream opgehaald, Opmerking: Deze bufferruimte wordt intern toegewezen door het coderingsprogramma.

【Grammatica】

```c
EncStatus VideoEncoder_GetStream(EncoderHandle *hEnc, EncOutputStream *output)
```

【Parameters】

hEnc: de greep die wordt geretourneerd tijdens het maken

output: Voer de gecodeerde streamgegevensbuffer uit, bufSize is groter dan 0 om de uitvoer te hebben

```c
typedef struct
{
    unsigned char *bufAddr;
    unsigned int bufSize; 
}EncOutputStream;
```

【Retourwaarde】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.2.9 VideoEncoder_GetStream_ByExtBuf

【Beschrijving】

Haalt de buffer van de videocoderingsstream op, Opmerking: De bufferruimte moet door de consument worden toegewezen voordat deze functie wordt aangeroepen.

【Grammatica】

```c
EncStatus VideoEncoder_GetStream(EncoderHandle *hEnc, EncOutputStream *output)
```

【Parameters】

hEnc: de greep die wordt geretourneerd tijdens het maken

output: Voer de gecodeerde streamgegevensbuffer uit, bufSize is groter dan 0 om de uitvoer te hebben

```c
typedef struct
{
    unsigned char *bufAddr;
    unsigned int bufSize; 
}EncOutputStream;
```

【Retourwaarde】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.3.0 VideoEncoder_ReleaseStream

【Beschrijving】

De buffer van de videocoderingsstream vrijgeven

【Grammatica】

```c
EncStatus VideoEncoder_ReleaseStream(EncoderHandle *hEnc, EncOutputStream *output)
```

【Parameters】

- hEnc: de greep die wordt geretourneerd tijdens het maken
- uitvoer:VideoEncoder_GetStream de geretourneerde buffer

【Retourwaarde】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

# 2 Hardware structuur diagram en software architectuur

# 2.1 Hardwarestructuurdiagram

Het hardwareblokdiagram van de K510 is als volgt:
![hardware_block_diagram](../zh/images/multimedia_guides/hardware_block_diagram.png)

De gegevens die van de videosensor worden ontvangen, worden verwerkt door MIPI DPHY, CSI, VI, isP om de yuv-brongegevens te verkrijgen en opgeslagen in de DDR. De h264-encodermodule leest gegevens van de DDR, voert coderingsbewerkingen uit en slaat de resultaten van de bewerkingen op in de DDR.

# 2.2 Software architectuur

De softwarearchitectuur van het multimedia-ontwikkelingsplatform is als volgt:

![multimedia_block_diagram.png](../zh/images/multimedia_guides/multimedia_block_diagram.png)

daarin

- `libvenc`: Encoder bibliotheek voor het aanroepen van h264 encoder kern
- `libmediactl`: Isp bibliotheek voor het aansturen van sensoren
- `libaudio3a`: Audio3a bibliotheek voor 3a bewerkingen op audio
- `alsa-lib`: Audiobibliotheek voor het bedienen van de audio-interface

# 3 Demo-app

## 3.1 Toepassing coderen

Het programma wordt `/app/encode_app`in de directory geplaatst:

- `encode_app`: Encode applicatieprogramma
- Het yuv-bestand dat wordt gebruikt voor het testen is groot en past niet in het SDK-pakket

rennen`encode_app`

| De parameternaam | Parameterinterpretatie | De standaardwaarde | Het waardebereik | Toepasselijke coderingsmodules |
|:-|:-|:-|:-|:-|
| Help | Help-informatie| | ||
| splijten | Het aantal kanalen | NUL | [1,4] | jpeg、avc |
| Ch | Kanaalnummer (op basis van 0) | NUL | [0,3] | jpeg、avc |
| Ik | Voer het YUV-bestand in, alleen **ondersteuning voor nv12-indeling**  | NUL | v4l2 <br> xxx.yuv | jpeg、avc |
| Dev | v4l2 apparaatnaam | NUL | **sensor0:** /dev/video3 /dev/video4 <br> <br>sensor1:<br> ** /dev/video7 / ** dev/ <br> video8 <br> | aaien |
| of | uitvoer| NUL | rtsp <br> xxx.264 <br> xxx.MJPEG <br> xxx.JPEG | jpeg、avc |
| in | Breedte van het uitvoerbeeld | 1920 | avc: [128,2048], veelvoud van 8 <br> jpeg: tot 8192, veelvoud van 16 | jpeg、avc |
| h | Hoogte van het uitvoerbeeld | 1080 | avc: [64,2048], veelvoud van 8 <br> jpeg: tot 8192, veelvoud van 2 | jpeg、avc |
| Fps | De camera legt framesnelheden vast, die momenteel slechts 30pfs ondersteunen | 30 | 30 | aaien |
| r | Gecodeerde framesnelheid van uitvoer | 30 | Het getal dat deelbaar of deelbaar kan zijn door fps | aaien |
| inframes | Voer het aantal yuv-frames in | 0 | [0,32767] | jpeg、avc |
| outframes | De uitvoer van de yuv-frames, indien groter dan de parameter -inframes, wordt herhaald gecodeerd | 0 | [0,32767] | jpeg、avc |
| Gop | Group Of Picture, het interval tussen twee I-frames | 25 | [1,1000] | aaien |
| Rcmode | Vertegenwoordigt bitrate controlemodus 0:CONST_QP 1:CBR 2:VBR | CBR | [0,2] | aaien |
| bitrate | Doelbitsnelheid in CBR-modus of laagste bitsnelheid in VBR-modus, in kB | 4000 | [1,20000] | aaien |
| maxbitrate | De hoogste bitsnelheid in VBR-modus, in Kb | 4000 | [1,20000] | aaien |
| profiel | profile_idc parameters in SPS: 0: basis 1:main 2:hoog 3:jpeg | AVC_HIGH | [0,3] | jpeg、avc |
| niveau | level_idc parameters in SPS | 42 | [10,42] | aaien |
| Sliceqp | De initiële QP-waarde, -1 voor automatisch | 25 | AVC: -1, jpeg[0,51]<br/>:[1,100] | jpeg、avc |
| Minqp | De minimale QP-waarde | 0 | [0,sliceqp] | aaien |
| MaxQP | De maximale QP-waarde | 54 | [SliceQP,54] | aaien |
| enableLTR inschakelen | Hiermee schakelt u referentiekaders voor de lange termijn in en geven parameters de vernieuwingsperiode op. 0: De vernieuwingscyclus is niet ingeschakeld. Positief: Hiermee wordt periodiek het referentiekader ingesteld en het volgende frame wordt ingesteld om het lange referentiekader te gebruiken | 0 | [0,65535] | aaien |
| koning | Roi-configuratiebestand, dat meerdere roi-regio's opgeeft | NUL | xxx.conf | aaien |
| Ae | AE inschakelen | 0 | 0 - Schakelt AE 1 niet in<br>- AE inschakelen |
| Conf | Het vl42-configuratiebestand wijzigt de v4l2-configuratieparameters op basis van het opgegeven configuratiebestand en de invoerparameters van de opdrachtregel | NUL | xxx.conf | aaien |

### 3.1.1 Voer het yuv-bestand in en voer het bestand uit

```shell
./encode_app -split 1 -ch 0 -i your_file.yuv -o out.264 -w 1920 -h 1080 -inframes 10 -outframes 30
./encode_app -split 1 -ch 0 -i your_file.yuv -o out.mjpeg -w 1920 -h 1080 -inframes 10 -outframes 30
```

### 3.1.2 Ingang v4l2, uitgang rtsp push stream

#### 3.1.2.1. Eenkanaals

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

Voorbeeld van een ffplay pull commando:

```shell
 ffplay -rtsp_transport tcp rtsp://192.168.137.11:8554/testStream
```

- `rtsp://192.168.137.11:8554/testStream`Voor het rtsp stream url-adres betekent -rtsp_transport tcp om tcp te gebruiken om audio- en videogegevens te verzenden (udp wordt standaard gebruikt) en de -fflags nobuffer-optie kan worden toegevoegd om verhoogde latentie als gevolg van spelercaching te voorkomen.

#### 3.1.2.2. Enkele camera dual channel

```shell
./encode_app -split 2 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -ch 1 -i v4l2 -dev /dev/video4 -o rtsp -w 1280 -h 720 -conf video_sample.conf
```

Het ffplay pull stream commando is hetzelfde als hierboven.

#### 3.1.2.3. Dubbele camera's

```shell
./encode_app -split 2 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -ch 1 -i v4l2 -dev /dev/video7 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

Het ffplay pull stream commando is hetzelfde als hierboven.

#### 3.1.2.4. ROI-test

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -sliceqp -1 -bitrate 2048 -roi roi_1920x1080.conf -conf video_sample.conf
```

roi bestandsformaat

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

Parameter beschrijving:

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

Het ffplay pull stream commando is hetzelfde als hierboven.

### 3.1.3 Framesnelheid transformatie

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -r 60 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

Het ffplay pull stream commando is hetzelfde als hierboven.

### 3.1.4 Meerdere invoerframesnelheden

VGA@75fps en 720p60 worden momenteel ondersteund

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 640 -h 480 -fps 75 -r 75 -conf video_sample_vga480p75.conf
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1280 -h 720 -fps 60 -r 60 -conf video_sample_720p60.conf
```

Het ffplay pull stream commando is hetzelfde als hierboven.

### 3.1.5 rtsp push audio- en videostreams

```c
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -alsa 1 -ac 2 -ar 44100 -af 2 -ad hw:0 -conf video_sample.conf
```

Het ffplay pull stream commando is hetzelfde als hierboven.

### 3.1.6 Voorzorgsmaatregelen

- Werkomgeving: Core board sensor: IMX219_SENSOR

- rtsp stream address format: rtsp://ip adres: port number/testStream, waarbij ip address en port number variabel zijn en de rest vastligt.

  Zoals: rtsp://192.168.137.11:8554/testStream, waarbij het IP-adres 192.168.137.11 is, is het poortnummer 8554.

  IP-adres: Het IP-adres van de ontwikkelraad, voer ifconfig in op het bord om te verkrijgen.

  Poortnummer: 8554 + <通道号>*2, kanaalnummers beginnen over het algemeen vanaf 0 (-ch 0, -ch 1...). 

- Speel RTSP-streammodus: de bijbehorende RTSP-stream kan worden afgespeeld via vlc of ffplay en de gegevensstroom kan worden verzonden via het udp- of TCP-protocol.

  1) rtp over udp播放: ffplay -rtsp_transport udp rtsp://192.168.137.11:8554/testStream

  2) rtp over tcp 播放: ffplay -rtsp_transport tcp rtsp://192.168.137.11:8554/testStream

  Het wordt aanbevolen om rtp over tcp te gebruiken om te spelen om het scherm veroorzaakt door udp-pakketverlies te voorkomen.

## 3,2 ffmpeg

ffmpeg wordt in de map /usr/local/bin geplaatst.

- `ffmpeg`: ffmpeg app.

rennen`ffmpeg`

(1) Encoder libk510_h264 parameter
| De parameternaam | Parameterinterpretatie | De standaardwaarde | Het waardebereik |
|:-|:-|:-|:-|
| g | gop grootte | 25 | 1 ~ 1000 |
| b | bitrate | 4000000 | 0 ~ 20000000 |
| r | Framesnelheid, omdat isps momenteel slechts 30 fps ondersteunen, dus de decoder moet worden ingesteld op 30 | 30 | 30 |
| idr_freq | IDR-frequentie | -1 (geen IDR) | -1 ~ 256 |
| Qp | Wanneer u codeert met cqp, configureert u de qp-waarde | -1 (automatisch) | -1 ~ 100 |
| maxrate | De maximale waarde van de bitrate | 0 | 20000000 |
| profiel | Ondersteunde profielen | 2 (hoog) | 0 - basislijn <br> 1 - hoofd <br> 2 - hoog |
| niveau | Codeerniveau | 42 | 10 ~ 42 |
| Zou | Beeldverhouding van het scherm | 0 (automatisch) | 0 - auto <br> 1 - 4:3 <br> 2 - 16:9 <br> 3 - geen |
| Ch | kanaalnummer | 0 | 0-7 |
| framesToEncode | Het aantal gecodeerde frames | -1 (alle frames) | -1 ~ 16383 |

(2) Encoder libk510_jpeg parameters
| De parameternaam | Parameterinterpretatie | De standaardwaarde | Het waardebereik |
|:-|:-|:-|:-|
| Qp | Wanneer u codeert met cqp, configureert u de qp-waarde | 25 | -1 ~ 100 |
| r | framerate | 30 | 25 ~ 60 |
| Ch | kanaal coderen | 0 | 0 ~ 7 |
| maxrate | Maximale bitrate. (0=negeren) | 4000000 | 0 ~ 20000000 |
| Zou | aspectverhouding | 0 (automatisch) | 0 - auto <br> 1 - 4:3 <br> 2 - 16:9 <br> 3 - geen |

(3) Het apparaat libk510_video parameter
| De parameternaam | Parameterinterpretatie | De standaardwaarde | Het waardebereik |
|:-|:-|:-|:-|
| Wh | framemaat | NUL | **voor encoder libk510_h264:**:<br>  tot 2048x2048 <br> breedte veelvoud van 8 <br> hoogte veelvoud van 8 <br> min. breedte: 128 <br> min. hoogte: 64 <br> **voor encoder libk510_jpeg:** <br> tot 8192x8192 <br> breedte veelvoud van 16 <br> hoogte veelvoud van 2 |
| Exp | belichtingsparameter | 0 | 0 ~ 128 |
| Agc | analoge versterking | 0 | 0 ~ 232 |

(4) audio3a parameter
| De parameternaam | Parameterinterpretatie | De standaardwaarde | Het waardebereik |
|:-|:-|:-|:-|
| sample_rate | Audio sample rate | 16000 | 1 ~ 65535 |
| Agc | Audioversterkingsmodus | 3 (AgcModeFixedDigital) | 0 - AgcModeUnchanged <br> 1 - AgcModeAdaptiveAnalog <br> 2 - AgcModeAdaptiveDigital <br> 3 - AgcModeFixedDigital |
| Ns | Geluidsniveau | 3 (Zeerhoog) | 0 - Laag <br> 1 - Matig <br> 2 - Hoog <br> 3 - Zeerhoog |
| dsp_task | Auido3a looppositie | 1 (dsp) | 0 - cpu <br>1 - dsp |

Configureerbare parameters kunnen worden bekeken via de help-opdracht

```shell
ffmpeg -h encoder=libk510_h264 #查看k510编码器的参数
ffmpeg -h demuxer=v4l2 #查看demuxer的配置参数
ffmpeg -h filter=audio3a #查看audio3a的配置参数
```

Het logische kader voor ffmpeg is als volgt:

![ffmpeg_block_diagram](../zh/images/multimedia_guides/ffmpeg_block_diagram.png)

audio3a wordt gebruikt om 3a-bewerkingen uit te voeren op de ontvangen audio en deze uit te voeren, en het logische blokdiagram is als volgt:

![ffmpeg_canaan_audio3a](../zh/images/multimedia_guides/ffmpeg_canaan_audio3a.png)

### 3.2.1 Bedieningsinstructies voor het programma

#### 3.2.1.1 rtp stream push

##### 3.2.1.1.1. rtp push video stream

Voorbeeld van een ffmpeg run commando:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.102.231.29:1234
```

Waar 10.102.231.29 het ontvangstadres is, wordt dit gewijzigd op basis van de werkelijke situatie.
Druk op "q" terwijl het programma wordt uitgevoerd om te stoppen met werken.

ffplay krijgt het commando:

```shell
ffplay.exe -protocol_whitelist "file,udp,rtp" -i test.sdp -fflags nobuffer -analyzeduration 1000000 -flags low_delay
```

Test.sdp is als volgt geconfigureerd.

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

Beschrijving van de parameter .sdp:

- c=: Informatie over medialinks; IN: Netwerktype; IP4: Adrestype; Gevolgd door het IP-adres (merk op dat dit het IP-adres is waar de ontvanger zich bevindt, niet het IP-adres van de afzender)
- m= is het begin van een sessie op medianiveau, video:mediatype; 1234: Poortnummer; RTP/AVP: Vervoersprotocol; 96: Payload-indeling in de rtp-header
Wijzig het ip-adres en poortnummer van de ontvanger op basis van de werkelijke situatie en merk op dat het poortnummer van rtp gelijkmatig moet zijn.

##### 3.2.1.1.2. rtp push audiostream

Voorbeeld van een ffmpeg run commando:

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f rtp rtp://10.100.232.11:1234
```

Wanneer 10.100.232.11 het ontvangstadres is, wordt dit aangepast aan de werkelijke situatie.

- ac: hiermee stelt u het aantal audiokanalen in
- ar: stelt de audio sample rate in

De opdracht ffplay receive is hetzelfde als het ontvangen van een videostream en het sdp-bestand verwijst naar het volgende voorbeeld.

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

##### 3.2.1.1.3 rtp push audio- en videostreams

Voorbeeld van een ffmpeg run commando:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234 -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

De opdracht ffplay receive is hetzelfde als het ontvangen van een audiostream en het sdp-bestand verwijst naar het volgende voorbeeld.

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

#### 3.2.1.2. rtsp push stream

Voordat rtsp de stream pusht, moet u de rtsp-server implementeren om de gegevensstroom naar de server te pushen.

##### 3.2.1.2.1 rtsp push video streams

Voorbeeld van een ffmpeg run commando:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -acodec copy -f rtsp rtsp://10.100.232.11:5544/live/test110
```

- `idr_freq`Voor het IDR-frame-interval is een geheel getal veelvoud van de GOP vereist. RTSP-streams moeten IDR-frames genereren om naar streams te kunnen trekken.
- `rtsp://10.100.232.11:5544/live/test110`Is het PUSH-PULL STREAM URL-adres van de RTSP-server

Voorbeeld van een ffplay pull commando:

```shell
ffplay.exe -protocol_whitelist "file,udp,rtp,tcp" -i rtsp://10.100.232.11:5544/live/test110
```

##### 3.2.1.2.2.2 rtsp push audiostream

Voorbeeld van een ffmpeg run commando:

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f rtsp rtsp://10.100.232.11:5544/live/test110
```

Het ffplay pull stream commando is hetzelfde als het rtsp pull video stream commando.

##### 3.2.1.2.3 rtsp push audio video stream

Voorbeeld van een ffmpeg run commando:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -f alsa -ac 2 -ar 32000 -i hw:0 -idr_freq 25 -vcodec libk510_h264 -acodec aac -f rtsp rtsp://10.100.232.11:5544/live/test110
```

Het ffplay pull stream commando is hetzelfde als het rtsp pull video stream commando.

#### 3.2.1.3 rtmp push stream

Voordat rtmp streaming, moet u de rtmp-server implementeren om de gegevensstroom naar de server te pushen. Servers die het RTMP-protocol ondersteunen zijn onder andere fms, nginx, srs, etc.

##### 3.2.1.3.1 rtmp pusht videostreams

Voorbeeld van een ffmpeg run commando:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`Het URL-adres voor het pushen van de stream naar de rtmp-server  

Voorbeeld van een ffplay pull commando:

```shell
ffplay -fflags nobuffer rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`Om het url-adres van de stream van de rtmp-server te halen (pushstreams zijn hetzelfde als het adres van de pull-stream), is de -fflags nobuffer-optie om verhoogde latentie als gevolg van spelercaching te voorkomen.

##### 3.2.1.3.2 rtmp push audiostream

Voorbeeld van een ffmpeg run commando:

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`Het URL-adres voor het pushen van de stream naar de rtmp-server

Het ffplay pull stream commando is hetzelfde als het rtmp pull video stream commando.

##### 3.2.1.3.3.3 rtmp push audio- en videostreams

Voorbeeld van een ffmpeg run commando:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -f alsa -ac 2 -ar 32000 -i hw:0 -idr_freq 25 -vcodec libk510_h264 -acodec aac -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`Het URL-adres voor het pushen van de stream naar de rtmp-server

Het ffplay pull stream commando is hetzelfde als het rtmp pull video stream commando.

#### 3.2.1.4 audio3a

##### 3.2.1.4.1 Audio afzonderlijk uitvoeren

(1) Voer audio3a uit op de CPU
Voorbeeld van een ffmpeg run commando:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000:dsp_task=0 -f rtp rtp://10.100.232.11:1234
```

(2) Voer audio3a uit op dsp
Voer twee Telnet-vensters uit, voer dsp-taakplanner en ffmpeg uit in beide vensters (voer eerst dsp-taakplanner uit)
dsp task scheduler voert de opdrachtinstantie uit:

```shell
cd /app/dsp_app_new/
./dsp_app /app/dsp_scheduler/scheduler.bin
```

ffmpeg run commando voorbeeld:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000 -f rtp rtp://10.100.232.11:1234
```

##### 3.2.1.4.2 Audio3a en video tegelijkertijd uitvoeren

(1) Voer audio3a uit op de CPU
Voer twee Telnet-vensters uit, voer audio3a en video uit in beide vensters.
Voorbeeld van de videoopdracht:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234
```

Voorbeeld van de opdracht audio3a:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000:dsp_task=0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

Het tegelijkertijd uitvoeren van audio3a en video op de cpu zal overloop veroorzaken, het wordt aanbevolen om audio3a op dsp uit te voeren
(2) Voer audio3a uit op dsp
Voer drie Telnet-vensters uit, voer audio3a-oproepen, video en dsp-planner uit op elk van de drie vensters
De opdracht dsp task scheduler run is hetzelfde als het uitvoeren van audio3a alleen.

Voorbeeld van de opdracht audio3a:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000 -f rtp rtp://10.100.232.11:1236
```

Voorbeeld van de videoopdracht:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234
```

- 10.100.232.11 is het IP-adres van de rtp-ontvanger.
- De inhoud van het SDP-bestand van de ontvangende terminal ffplay kan worden verkregen uit het afgedrukte logboek na het uitvoeren van de bovenstaande ffmpeg-opdracht.

#### 3.2.1.5 v4l2

Configureerbare parameters kunnen worden bekeken via de help-opdracht

```shell
ffmpeg -h demuxer=v4l2 #查看v4l2的配置参数
```

| De parameternaam | Parameterinterpretatie | De standaardwaarde | Het waardebereik |
| :-- | :-- | :-- | :-- |
| s | Beeldresolutie, zoals 1920x1080 | NUL | |
| r | Framesnelheid, momenteel alleen ondersteuning voor 30 fps | 30 | 30 |
| internetprovider | Schakel de K510 ISP-hardware in | 0 | 0-1 |
| buf_type | v4l2 buffer`类型` <br>1: V4L2_MEMORY_MMAP: for -vcodec copy<br>2: V4L2_MEMORY_USERPTR: for -vcodec libk510_h264 | 1 | 1 ~ 4 |
| Conf | v4l2 configuratie bestand | NUL | |

Voorbeeld van de ffmpeg running command: waarbij 10.100.232.11 het ontvangende adres is, aangepast aan de werkelijke situatie.

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234 -f alsa -ac 2 -ar 16000 -i hw:0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -i /dev/video3 -vcodec copy -y out.yuv
```

Illustreren:

1. De runtime moet worden gevonden in de map run`video_sampe.conf` `imx219_0.conf`en de `imx219_1.conf`bestanden zijn geconfigureerd en de drie bestanden bevinden zich onder`/encode_app/` de map. 
2. De video die in realtime door de camera wordt geleverd, is geschreven als een YUV-bestand en omdat het YUV-bestand erg groot is, kan de lokale DDR- of NFS-schrijfsnelheid het niet bijhouden, wat kan leiden tot framedrop.

#### 3.2.1.6 JPEG-codering

Bestandsuitvoer:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_jpeg -y test.mjpeg
```

Beschrijving: de runtime moet zich in de map run bevinden`video_sampe.conf` `imx219_0.conf`en `imx219_1.conf`de bestanden zijn geconfigureerd en de drie bestanden bevinden zich onder`/encode_app/` de map. 

Het uitvoerbestand test.mjpeg kan aan de pc-kant worden afgespeeld met ffplay

```shell
ffplay -i test.mjpeg
```

Push Stream:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_jpeg -an -f rtp rtp://10.100.232.11:1234
```

Ffplay pull streams zijn beschikbaar

#### 3.2.1.7. Multiplexing codering

Ondersteuning van maximaal 8 gelijktijdige codering, u kunt de framegrootte van elk kanaal gebruiken vermenigvuldigd met de framesnelheid en vervolgens toevoegen, niet groter zijn dan de hoeveelheid gegevens van 1080p60, -vcodec kan h264 of jpeg kiezen.

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -filter_complex 'split=2[out1][out2]' -map '[out1]' -vcodec libk510_h264 -ch 0 -an -f rtp rtp://10.20.1.101:1234 -map '[out2]' -vcodec libk510_h264 -ch 1 -an -f rtp rtp://10.20.1.101:2236
```

```shell
ffmpeg -f v4l2 -s 480x360 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -filter_complex 'split=8[out1][out2][out3][out4][out5][out6][out7][out8]' -map '[out1]' -vcodec libk510_h264 -b:v 300000 -ch 0 -an -f rtp rtp://10.20.1.101:1234 -map '[out2]' -vcodec libk510_h264 -b:v 300000 -ch 1 -an -f rtp rtp://10.20.1.101:2322 -map '[out3]' -vcodec libk510_h264 -b:v 300000 -ch 2 -an -f rtp rtp://10.20.1.101:3086 -map '[out4]' -vcodec libk510_h264 -b:v 300000 -ch 3 -an -f rtp rtp://10.20.1.101:4234 -map '[out5]' -vcodec libk510_h264 -b:v 300000 -ch 4 -an -f rtp rtp://10.20.1.101:5216 -map '[out6]' -vcodec libk510_h264 -b:v 300000 -ch 5 -an -f rtp rtp://10.20.1.101:6788 -map '[out7]' -vcodec libk510_h264 -b:v 300000 -ch 6 -an -f rtp rtp://10.20.1.101:7230 -map '[out8]' -vcodec libk510_h264 -b:v 300000 -ch 7 -an -f rtp rtp://10.20.1.101:8976
```

Wanneer u ffplay gebruikt om streams te trekken, moet u ervoor zorgen dat u slechts één video trekt, de video van andere wegen schakelt door het poortnummer in het SDP-bestand te wijzigen of meerdere ffplay-streams start.

### 3.2.2 Instructies voor het overzetten van programma's

`ffmpeg``ffmpeg`Geporteerd op de open source versie 4.4,`xxx.patch` toegevoegd voor het servicepack

- `ff_libk510_h264_encoder`: Controle h264 hardware codering, waarnaar wordt verwezen`libvenc.so`
- `ff_libk510_jpeg_encoder`: Regelt de jpeg hardware codering, waarnaar wordt verwezen`libvenc.so`
- v4l2: In v4l2.c is k510 hardwaregerelateerde code toegevoegd en het v4l2-buffertype V4L2_MEMORY_USERPTR en waarnaar wordt verwezen`libmediactl.so`. 

#### 3.2.2.1. opdracht voor het genereren van patches

（1）

```shell
quilt new -p ab xxx.patch #在patches目录下生成xxx.patch文件
quilt add <filename> #添加修改前的文件
### 修改代码 ###
quilt refresh #修改内容被添加到xxx.patch
```

（2）
Kopieer xxx.patch naar de map package/ffmpeg_canaan en wijzig het bestandspad in het patchbestand volgens het huidige pad.

```shell
mv ../../patches/xxx.patch ../../package/ffmpeg_canaan
rm ../../patches/series
sed -i "s/\/dl\/ffmpeg_canaan\/ffmpeg-4.4//g" ../../package/ffmpeg_canaan/xxx.patch
```

#### 3.2.2.2 ffmpeg configuratie

In het `package/ffmpeg_canaan/ffmpeg.mk`bestand kan de CPU-kern worden gewijzigd, de compilatietoolchain en kan de inschakeling worden gemaakt via de configuratieoptie`ff_k510_video_demuxer`.`ff_libk510_jpeg_encoder` `ff_libk510_h264_encoder` 

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

**Vertaling Disclaimer**  
Voor het gemak van klanten gebruikt Canaan een AI-vertaler om tekst in meerdere talen te vertalen, wat fouten kan bevatten. Wij garanderen niet de nauwkeurigheid, betrouwbaarheid of tijdigheid van de geleverde vertalingen. Canaan is niet aansprakelijk voor enig verlies of schade veroorzaakt door het vertrouwen op de nauwkeurigheid of betrouwbaarheid van de vertaalde informatie. Als er een inhoudelijk verschil is tussen de vertalingen in verschillende talen, prevaleert de vereenvoudigd Chinese versie. 

Als u een vertaalfout of onnauwkeurigheid wilt melden, neem dan gerust contact met ons op via e-mail.