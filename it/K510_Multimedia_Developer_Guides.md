![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 Multimedia Guida per gli sviluppatori</font>**

<font face="黑体"  size=3>Versione del documento: V1.0.0</font>

<font face="黑体"  size=3>Data di pubblicazione: 2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Disconoscimento**</font>
I prodotti, i servizi o le funzionalità acquistati saranno soggetti ai contratti e ai termini commerciali di Beijing Canaan Jiesi Information Technology Co., Ltd. ("la Società", la stessa di seguito), e tutti o parte dei prodotti, servizi o funzionalità descritti in questo documento potrebbero non rientrare nell'ambito dell'acquisto o dell'utilizzo. Salvo quanto diversamente concordato nel contratto, la Società declina ogni dichiarazione o garanzia, espressa o implicita, in merito all'accuratezza, affidabilità, completezza, marketing, scopo specifico e non aggressione di qualsiasi dichiarazione, informazione o contenuto di questo documento. Salvo diverso accordo, questo documento è fornito solo come guida per l'uso.
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
## Scopo del documento
Questo documento è un documento esplicativo per l'esempio di applicazione K510 Multimedia.
## Target
A chi è destinato il presente documento:
- Sviluppatori di software
- Personale di supporto tecnico

## Cronologia delle revisioni

| Il numero di versione    | Modificato da | Data della revisione| Note di revisione  |  
|  ------  |-------| -------| ------ |
| v1.0.0    |Gruppi di software di sistema | 2022-03-09 | Rilasciato SDK V1.5 |
|     |     |      |   |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenuto</font>**

[TOC]

# 1 API encoder

## 1.1 Descrizione del file di intestazione

k510_buildroot/pacchetto/encode_app/enc_interface.h

## 1.2 Descrizioni delle funzioni API

### 1.2.1 VideoEncoder_Create

【Descrizione】

Creare un codificatore video

【Grammatica】

```c
EncoderHandle* VIdeoEncoder_Create(EncSettings *pCfg)
```

【Parametri】

pCfg: immettere i parametri di configurazione della codifica

|            Il nome del parametro             | Interpretazione dei parametri                                                     |                           L'intervallo di valori                           | Moduli di codifica applicabili |
| :---------------------------: | :----------------------------------------------------------- | :----------------------------------------------------------: | ------------ |
|            canale            | Numero di canale, supporta fino a 8 canali codificati                                   |                            [0，7]                            | jpeg、avc    |
|             Larghezza             | Codifica la larghezza dell'immagine                                                 | avc: [128,2048], multiplo di 8 <br/> jpeg: fino a 8192, multiplo di 16 | jpeg、avc    |
|            altezza             | Codificare l'altezza dell'immagine                                                 | avc: [64,2048], multiplo di 8 <br/> jpeg: fino a 8192, multiplo di 2 | jpeg、avc    |
|           FrameRate           | Frame rate, che può essere configurato solo su pochi valori fissi                                    |                       (25,30,50,60,75)                       | jpeg、avc    |
|            rcMode             | La modalità di controllo del bitrate 0:CONST_QP 1:CBR 2:VBR<br />jpeg è fissata per CONST_QP  |                       Vedi RateCtrlMode                       | jpeg, avc    |
|            BitRate            | Bitrate di destinazione in modalità CBR o bitrate più basso in modalità VBR                    |                        [10,20000000]                         | infarto          |
|          Metodo MaxBitRate           | Il bitrate più alto in modalità VBR                                          |                        [10,20000000]                         | infarto          |
|            SliceQP            | Valore QP iniziale, -1 per auto                                        |                avc:-1,jpeg[0,51]<br/>:[1,100]                | jpeg, avc    |
|             MinQP             | Il valore qp minimo                                                     |                         [0, sliceqp]                          | infarto          |
|             MaxQP             | Il valore qp massimo                                                     |                         [sliceqp,54]                         | infarto          |
|            profilo            | profile_idc parametri in SPS: 0: base 1:principale 2:alto 3:jpeg       |                            [0,3]                             | jpeg, avc    |
|             livello             | parametri level_idc in PS                                       |                           [10,42]                            | infarto          |
|          AspectRatio          | Scala di visualizzazione                                                     |                     Vedi AVC_AspectRatio                      | jpeg, avc    |
|            FreqIDR            | Intervallo tra due frame IDR                                              |                           [1,1000]                           | infarto          |
|            gopLen             | Gruppo di immagini, l'intervallo tra due fotogrammi I                      |                           [1,1000]                           | infarto          |
|          bEnableGDR           | Se abilitare l'aggiornamento nel frame                                             |                         [vero, falso]                         | infarto          |
|            gdrMode            | modalità di aggiornamento gdr: 0, aggiornamento verticale 1, aggiornamento orizzontale                        |                       Vedere GDRCtrlMode                        | infarto          |
|          bEltRable           | Se i sistemi di riferimento a lungo termine sono abilitati                                           |                         [vero, falso]                         | infarto          |
|          roiCtrlMode          | Modalità di controllo ROI: 0: Non utilizzare roi 1: qp relativo 2: qp assoluto                 |                       Vedere ROICtrlMode                        | infarto          |
|       EncSliceSplitCfg        | distribuzione suddivisa in sezioni                                               |                                                              | infarto          |
|         bSplitEnable          | Se la divisione delle sezioni è abilitata                                           |                         [vero, falso]                         | infarto          |
|         u32SplitMode          | Modalità di segmentazione delle sezioni: 0: Diviso per bit. <br />1: Dividi per righe di macroblocchi        |                            [0,1]                             | infarto          |
|         u32SliceSize          | u32SplitMode=0, che indica il numero di byte per slice<br /> u32SplitMode=1, rappresenta il numero<br /> di righe di macroblocchi per slice| u32SplitMode=[100,65535]<br />0,u32SplitMode=1,[1, (altezza immagine +15)/16] | infarto          |
|          entropiaMode          | Codifica entropia, 0: CABAC 1: CAVLC                                |                      Vedere EncEntropyMode                      | infarto          |
|          encDblkCfg           | Configurazione del filtro dei blocchi                                                 |                                                              | infarto          |
| disable_deblocking_filter_idc | Il valore predefinito è 0, ovvero H.264 Agreement                          |                            [0，2]                            | infarto          |
|  slice_alpha_c0_offset_div2   | Il valore predefinito è 0, ovvero H.264 Agreement                          |                           [-6，6]                            | infarto          |
|    slice_beta_offset_div2     | Il valore predefinito è 0, ovvero H.264 Agreement                          |                          [-6,   6]                           | infarto          |

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

【Valore restituito】

```c
typedef void* EncoderHandle
```

### 1.2.2 VideoEncoder_SetRoiCfg

【Descrizione】

impostazione roi, supporto fino a 8 aree rettangolari, il sistema in base al numero indice di 0 ~ 7 per gestire l'area ROI, uIndex indica che l'utente imposta il numero indice di ROI. Le regioni ROI possono essere sovrapposte l'una all'altra e, quando si verifica una sovrapposizione, la priorità tra le regioni ROI aumenta sequenzialmente dal numero di indice 0 a 7.

Può essere utilizzato dopo la creazione dell'encoder e prima che venga distrutto. La regione roi può essere regolata dinamicamente durante il processo di codifica.

【Grammatica】

```c
EncStatus VideoEncoder_SetRoiCfg(EncoderHandle *hEnc,const EncROICfg*pEncRoiCfg);
```

【Parametri】

hEnc: l'handle restituito al momento della creazione

pEncRoiCfg: informazioni sulla configurazione della zona Roi

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

Descrizione del parametro

```text
uIndex     - 指定该roi区域索引号，范围0-7最多支持8个区域
bEnable    - 指定该区域是否使能，只有使能的区域才有效
uQpValue   - qp值，可以是相对qp或绝对qp，qp模式由EncSettings中roiCtrlMode属性决定。绝对qp范围                  [0,51]，相对qp范围[-31,31]
stRect     - roi矩形区域，s32X矩形左上角x值，s32Y矩形左上角y值，u32Width矩形宽度，u32Height矩形高度
```

【Valore restituito】

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.3 VideoEncoder_SetLongTerm

【Descrizione】

Imposta il fotogramma successivo della codifica su un fotogramma di riferimento a lungo termine. Può essere utilizzato dopo la creazione dell'encoder e prima che venga distrutto. L'attributo bEnableLTR in EncSettings determina se la funzionalità è abilitata.

【Grammatica】

```c
EncStatus VideoEncoder_SetLongTerm(EncoderHandle *hEnc);
```

【Parametri】

hEnc: l'handle restituito al momento della creazione

【Valore restituito】

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.4 VideoEncoder_UseLongTerm

【Descrizione】

Imposta la codifica sul fotogramma successivo utilizzando un quadro di riferimento a lungo termine. Può essere utilizzato dopo la creazione dell'encoder e prima che venga distrutto. L'attributo bEnableLTR in EncSettings determina se la funzionalità è abilitata.

【Grammatica】

```c
EncStatus VideoEncoder_UseLongTerm(EncoderHandle *hEnc);
```

【Parametri】

hEnc: l'handle restituito al momento della creazione

【Valore restituito】

```c
typedef enum
{
    Enc_SUCCESS = 0,
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.5 VideoEncoder_InsertUserData

【Descrizione】

Inserire i dati utente.

Può essere utilizzato dopo la creazione del codificatore e prima che venga distrutto e il contenuto dei dati utente può essere modificato in tempo reale durante il processo di codifica. I dati dell'utente saranno inseriti nell'area dati SEI del frame IDR.

【Grammatica】

```c
EncStatus      VideoEncoder_InsertUserData(EncoderHandle *hEnc,char*pUserData,unsigned int nlen);
```

【Parametri】

hEnc: l'handle restituito al momento della creazione

pUserData: un puntatore ai dati utente

nlen: Lunghezza dati utente (0, 1024)

【Valore restituito】

```c
typedef enum
{
    Enc_SUCCESS = 0,
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.6 VideoEncoder_Destory

【Descrizione】

Distruggere il codificatore video

【Grammatica】

```c
EncStatus VideoEncoder_Destroy(EncoderHandle *hEnc)
```

【Parametri】

hEnc: l'handle restituito al momento della creazione

【Valore restituito】

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.7 VideoEncoder_EncodeOneFrame

【Descrizione】

Codificare un fotogramma video

【Grammatica】

```c
EncStatus VideoEncoder_EncodeOneFrame(EncoderHandle *hEnc, EncInputFrame *input)
```

【Parametri】

hEnc: l'handle restituito al momento della creazione

ingresso: inserisci i dati video YUV

```c
typedef struct
{
    unsigned short width;
    unsigned short height;
    unsigned short stride;
    unsigned char *data;
}EncInputFrame;
```

【Valore restituito】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.2.8 VideoEncoder_GetStream

【Descrizione】

Ottiene il buffer del flusso di codifica video, Nota: questo spazio buffer viene allocato internamente dal codificatore.

【Grammatica】

```c
EncStatus VideoEncoder_GetStream(EncoderHandle *hEnc, EncOutputStream *output)
```

【Parametri】

hEnc: l'handle restituito al momento della creazione

output: output del buffer di dati del flusso codificato, bufSize è maggiore di 0 per avere l'output

```c
typedef struct
{
    unsigned char *bufAddr;
    unsigned int bufSize; 
}EncOutputStream;
```

【Valore restituito】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.2.9 VideoEncoder_GetStream_ByExtBuf

【Descrizione】

Ottiene il buffer del flusso di codifica video, Nota: lo spazio del buffer deve essere allocato dal consumer prima di chiamare questa funzione.

【Grammatica】

```c
EncStatus VideoEncoder_GetStream(EncoderHandle *hEnc, EncOutputStream *output)
```

【Parametri】

hEnc: l'handle restituito al momento della creazione

output: output del buffer di dati del flusso codificato, bufSize è maggiore di 0 per avere l'output

```c
typedef struct
{
    unsigned char *bufAddr;
    unsigned int bufSize; 
}EncOutputStream;
```

【Valore restituito】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.3.0 VideoEncoder_ReleaseStream

【Descrizione】

Rilasciare il buffer del flusso di codifica video

【Grammatica】

```c
EncStatus VideoEncoder_ReleaseStream(EncoderHandle *hEnc, EncOutputStream *output)
```

【Parametri】

- hEnc: l'handle restituito al momento della creazione
- output:VideoEncoder_GetStream restituito il buffer

【Valore restituito】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

# 2 Diagramma della struttura hardware e architettura software

# 2.1 Diagramma della struttura hardware

Lo schema a blocchi hardware del K510 è il seguente:
![hardware_block_diagram](../zh/images/multimedia_guides/hardware_block_diagram.png)

I dati ricevuti dal sensore video vengono elaborati da MIPI DPHY, CSI, VI, isP per ottenere i dati sorgente yuv e memorizzati nella DDR. Il modulo encoder h264 legge i dati dalla DDR, esegue operazioni di codifica e memorizza i risultati delle operazioni nella DDR.

# 2.2 Architettura software

L'architettura software della piattaforma di sviluppo multimediale è la seguente:

![multimedia_block_diagram.png](../zh/images/multimedia_guides/multimedia_block_diagram.png)

lì

- `libvenc`: Libreria encoder per chiamare h264 encoder core
- `libmediactl`: Libreria Isp per il controllo dei sensori
- `libaudio3a`: Libreria Audio3a per operazioni 3a sull'audio
- `alsa-lib`: Libreria audio per il controllo dell'interfaccia audio

# 3 App demo

## 3.1 Codifica dell'applicazione

Il programma viene inserito`/app/encode_app` nella directory:

- `encode_app`: Codifica programma applicativo
- Il file yuv utilizzato per il test è di grandi dimensioni e non si adatta al pacchetto SDK

Correre`encode_app`

| Il nome del parametro | Interpretazione dei parametri | Il valore predefinito | L'intervallo di valori | Moduli di codifica applicabili |
|:-|:-|:-|:-|:-|
| Guida | Informazioni di aiuto| | ||
| diviso | Il numero di canali | NULLO | [1,4] | jpeg、avc |
| Ch | Numero di canale (basato su 0) | NULLO | [0,3] | jpeg、avc |
| io | Inserisci il file YUV, supporta solo il**formato** nv12| NULLO | v4l2 <br> xxx.yuv | jpeg、avc |
| Dev | Nome dispositivo v4l2 | NULLO | **sensor0:** /dev/video3 /dev/video4 <br> <br>sensor1:<br> **/dev/video7 /** dev/ <br> video8 <br> | infarto |
| o | prodotto| NULLO | rtsp <br> xxx.264 <br> xxx.MJPEG <br> xxx.JPEG | jpeg、avc |
| in | Larghezza immagine di output | 1920 | avc: [128,2048], multiplo di 8 <br> jpeg: fino a 8192, multiplo di 16 | jpeg、avc |
| h | Altezza dell'immagine di output | 1080 | avc: [64,2048], multiplo di 8 <br> jpeg: fino a 8192, multiplo di 2 | jpeg、avc |
| fps | La fotocamera cattura frame rate, che attualmente supportano solo 30pfs | 30 | 30 | infarto |
| r | Frame rate di output codificato | 30 | Il numero che può essere divisibile o divisibile per fps | infarto |
| inframe | Inserisci il numero di fotogrammi yuv | 0 | [0,50] | jpeg、avc |
| outframe | L'output dei frame yuv, se più grande del parametro -inframes, verrà ripetuto codificando | 0 | [0,32767] | jpeg、avc |
| Gop | Gruppo di immagini, l'intervallo tra due fotogrammi I | 25 | [1,1000] | infarto |
| rcmode | Rappresenta la modalità di controllo del bitrate 0:CONST_QP 1:CBR 2:VBR | CBR | [0,2] | infarto |
| bitrate | Bitrate di destinazione in modalità CBR o bitrate più basso in modalità VBR, in KB | 4000 | [1,20000] | infarto |
| maxbitrate | Il bitrate più alto in modalità VBR, in Kb | 4000 | [1,20000] | infarto |
| profilo | profile_idc parametri in SPS: 0: base 1:principale 2:alto 3:jpeg | AVC_HIGH | [0,3] | jpeg、avc |
| livello | parametri level_idc in SPS | 42 | [10,42] | infarto |
| sliceqp | Valore QP iniziale, -1 per auto | 25 | avc:-1,jpeg[0,51]<br/>:[1,100] | jpeg、avc |
| minqp | Il valore QP minimo | 0 | [0, sliceqp] | infarto |
| maxqp | Il valore QP massimo | 54 | [sliceqp,54] | infarto |
| enableLTR | Abilita i frame di riferimento a lungo termine e i parametri specificano il periodo di aggiornamento. 0: Il ciclo di aggiornamento non è abilitato. Positivo: imposta periodicamente il fotogramma di riferimento e il fotogramma successivo viene impostato per utilizzare il fotogramma di riferimento lungo | 0 | [0,65535] | infarto |
| re | File di configurazione Roi, che specifica più aree ROI | NULLO | xxx.conf | infarto |
| Æ | Abilita AE | 0 | 0 - Non abilita AE<br>1 - Abilita AE | |
| Conf | Il file di configurazione vl42 modifica i parametri di configurazione v4l2 in base al file di configurazione specificato e ai parametri di input della riga di comando | NULLO | xxx.conf | infarto |

### 3.1.1 Inserire il file yuv e generare il file

```shell
./encode_app -split 1 -ch 0 -i your_file.yuv -o out.264 -w 1920 -h 1080 -inframes 10 -outframes 30
./encode_app -split 1 -ch 0 -i your_file.yuv -o out.mjpeg -w 1920 -h 1080 -inframes 10 -outframes 30
```

### 3.1.2 Ingresso v4l2, uscita rtsp push stream

#### 3.1.2.1 Canale singolo

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

Esempio di comando ffplay pull:

```shell
 ffplay -rtsp_transport tcp rtsp://192.168.137.11:8554/testStream
```

- `rtsp://192.168.137.11:8554/testStream`Per l'indirizzo URL del flusso rtsp, -rtsp_transport tcp significa utilizzare tcp per trasmettere dati audio e video (udp viene utilizzato per impostazione predefinita) e l'opzione -fflags nobuffer può essere aggiunta per evitare una maggiore latenza dovuta alla memorizzazione nella cache del lettore.

#### 3.1.2.2 Fotocamera singola a doppio canale

```shell
./encode_app -split 2 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -ch 1 -i v4l2 -dev /dev/video4 -o rtsp -w 1280 -h 720 -conf video_sample.conf
```

Il comando ffplay pull stream è lo stesso di cui sopra.

#### 3.1.2.3 Doppia fotocamera

```shell
./encode_app -split 2 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -ch 1 -i v4l2 -dev /dev/video7 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

Il comando ffplay pull stream è lo stesso di cui sopra.

#### 3.1.2.4 Test del ROI

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -sliceqp -1 -bitrate 2048 -roi roi_1920x1080.conf -conf video_sample.conf
```

formato di file ROI

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

Descrizione del parametro:

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

Il comando ffplay pull stream è lo stesso di cui sopra.

### 3.1.3 Trasformazione della frequenza dei fotogrammi

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -r 60 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

Il comando ffplay pull stream è lo stesso di cui sopra.

### 3.1.4 Frame rate di input multipli

VGA@75fps e 720p60 sono attualmente supportati

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 640 -h 480 -fps 75 -r 75 -conf video_sample_vga480p75.conf
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1280 -h 720 -fps 60 -r 60 -conf video_sample_720p60.conf
```

Il comando ffplay pull stream è lo stesso di cui sopra.

### 3.1.5 rtsp push flussi audio e video

```c
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -alsa 1 -ac 2 -ar 44100 -af 2 -ad hw:0 -conf video_sample.conf
```

Il comando ffplay pull stream è lo stesso di cui sopra.

### 3.1.6 Precauzioni

- Ambiente operativo: Sensore scheda principale: IMX219_SENSOR

- formato indirizzo flusso rtsp: indirizzo rtsp://ip: numero di porta/testStream, dove l'indirizzo IP e il numero di porta sono variabili e il resto è fisso.

  Ad esempio: rtsp://192.168.137.11:8554/testStream, dove l'indirizzo IP è 192.168.137.11, il numero di porta è 8554.

  Indirizzo IP: l'indirizzo IP della scheda di sviluppo, immettere ifconfig sulla scheda per ottenere.

  Numero di porta: 8554 + <通道号>*2, i numeri di canale generalmente partono da 0 (-ch 0, -ch 1...).

- Riproduci la modalità di flusso RTSP: il flusso RTSP corrispondente può essere riprodotto tramite vlc o ffplay e il flusso di dati può essere trasmesso tramite il protocollo udp o TCP.

  1) rtp su udp播放:ffplay -rtsp_transport udp rtsp://192.168.137.11:8554/testStream

  2) rtp su tcp 播放: ffplay -rtsp_transport tcp rtsp://192.168.137.11:8554/testStream

  Si consiglia di utilizzare rtp su tcp per riprodurre per evitare lo schermo causato dalla perdita di pacchetti udp.

## 3,2 ffmpeg

ffmpeg viene inserito nella directory /usr/local/bin.

- `ffmpeg`: ffmpeg app.

Correre`ffmpeg`

(1) Parametro libk510_h264 encoder
| Il nome del parametro | Interpretazione dei parametri | Il valore predefinito | L'intervallo di valori |
|:-|:-|:-|:-|
| g | dimensione gop | 25 | 1 ~ 1000 |
| b | bitrate | 4000000 | 0 ~ 20000000 |
| r | Frame rate, poiché gli isps attualmente supportano solo 30 fps, quindi il decodificatore deve essere impostato su 30 | 30 | 30 |
| idr_freq | Frequenza IDR | -1 (senza IDR) | -1 ~ 256 |
| Qp | Durante la codifica con cqp, configurare il valore qp | -1 (automatico) | -1 ~ 100 |
| maxrate | Il valore massimo del bitrate | 0 | 20000000 |
| profilo | Profili supportati | 2 (alto) | 0 - linea di base <br> 1 - principale <br> 2 - alta |
| livello | Livello di codifica | 42 | 10 ~ 42 |
| voler | Proporzioni dello schermo | 0 (auto) | 0 - auto <br> 1 - 4:3 <br> 2 - 16:9 <br> 3 - nessuno |
| Ch | numero di canale | 0 | 0-7 |
| framesToEncode | Il numero di fotogrammi codificati | -1 (tutti i fotogrammi) | -1 ~ 16383 |

(2) Parametri di libk510_jpeg encoder
| Il nome del parametro | Interpretazione dei parametri | Il valore predefinito | L'intervallo di valori |
|:-|:-|:-|:-|
| Qp | Durante la codifica con cqp, configurare il valore qp | 25 | -1 ~ 100 |
| r | framerate | 30 | 25 ~ 60 |
| Ch | codifica canale | 0 | 0 ~ 7 |
| maxrate | Bitrate massimo. (0=ignora) | 4000000 | 0 ~ 20000000 |
| voler | Proporzioni | 0 (auto) | 0 - auto <br> 1 - 4:3 <br> 2 - 16:9 <br> 3 - nessuno |

(3) Il parametro libk510_video dispositivo
| Il nome del parametro | Interpretazione dei parametri | Il valore predefinito | L'intervallo di valori |
|:-|:-|:-|:-|
| Wh | dimensione del telaio | NULLO | **per encoder libk510_h264:**:<br>  fino a 2048x2048 <br> larghezza multipla di 8 <br> altezza multipla di 8 <br> min. larghezza: 128 <br> min. altezza: 64 <br> **per encoder libk510_jpeg:** <br> fino a 8192x8192 <br> larghezza multipla di 16 <br> altezza multipla di 2 |
| Exp | parametro di esposizione | 0 | 0 ~ 128 |
| Agc | guadagno analogico | 0 | 0 ~ 232 |

(4) parametro audio3a
| Il nome del parametro | Interpretazione dei parametri | Il valore predefinito | L'intervallo di valori |
|:-|:-|:-|:-|
| sample_rate | Frequenza di campionamento audio | 16000 | 1 ~ 65535 |
| Agc | Modalità di guadagno audio | 3(AgcModeFixedDigital) | 0 - AgcModeUnchanged <br> 1 - AgcModeAdaptiveAnalog <br> 2 - AgcModeAdaptiveDigital <br> 3 - AgcModeFixedDigital |
| Ns | Livello di rumorosità | 3 (Molto alto) | 0 - Basso <br> 1 - Moderato <br> 2 - Alto <br> 3 - Molto Alto |
| dsp_task | Posizione di corsa Auido3a | 1 (dsp) | 0 - cpu <br>1 - dsp |

I parametri configurabili possono essere visualizzati tramite il comando help

```shell
ffmpeg -h encoder=libk510_h264 #查看k510编码器的参数
ffmpeg -h demuxer=v4l2 #查看demuxer的配置参数
ffmpeg -h filter=audio3a #查看audio3a的配置参数
```

La casella logica per ffmpeg è la seguente:

![ffmpeg_block_diagram](../zh/images/multimedia_guides/ffmpeg_block_diagram.png)

audio3a viene utilizzato per eseguire operazioni 3a sull'audio ricevuto e lo emette e il suo diagramma a blocchi logico è il seguente:

![ffmpeg_canaan_audio3a](../zh/images/multimedia_guides/ffmpeg_canaan_audio3a.png)

### 3.2.1 Istruzioni per il funzionamento del programma

#### 3.2.1.1 Spinta del flusso rtp

##### 3.2.1.1.1. flusso video push rtp

Esempio di comando ffmpeg run:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.102.231.29:1234
```

Dove 10.102.231.29 è l'indirizzo ricevente, viene modificato in base alla situazione reale.
Premere "q" mentre il programma è in esecuzione per interrompere l'esecuzione.

ffplay riceve il comando:

```shell
ffplay.exe -protocol_whitelist "file,udp,rtp" -i test.sdp -fflags nobuffer -analyzeduration 1000000 -flags low_delay
```

Test.sdp è configurato come segue.

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

Descrizione del parametro .sdp:

- c=: Informazioni sui collegamenti multimediali; IN: Tipo di rete; IP4: tipo di indirizzo; Seguito dall'indirizzo IP (si noti che è l'indirizzo IP in cui si trova il destinatario, non l'IP del mittente)
- m= è l'inizio di una sessione a livello multimediale, tipo video:media; 1234: Numero di porta; RTP/AVP: Protocollo di trasporto; 96: Formato payload nell'intestazione rtp
Modificare l'indirizzo IP e il numero di porta del ricevitore in base alla situazione reale e notare che il numero di porta di rtp deve essere pari.

##### 3.2.1.1.2. flusso audio push rtp

Esempio di comando ffmpeg run:

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f rtp rtp://10.100.232.11:1234
```

Dove 10.100.232.11 è l'indirizzo ricevente, viene modificato in base alla situazione reale.

- ac: imposta il numero di canali audio
- ar: imposta la frequenza di campionamento audio

Il comando di ricezione ffplay è uguale alla ricezione di un flusso video e il file sdp fa riferimento all'esempio seguente.

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

##### 3.2.1.1.3 rtp push di flussi audio e video

Esempio di comando ffmpeg run:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234 -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

Il comando di ricezione ffplay è uguale alla ricezione di un flusso audio e il file sdp fa riferimento all'esempio seguente.

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

#### 3.2.1.2 flusso push rtsp

Prima che rtsp esegua il push del flusso, è necessario distribuire il server rtsp per eseguire il push del flusso di dati al server.

##### 3.2.1.2.1 rtsp push flussi video

Esempio di comando ffmpeg run:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -acodec copy -f rtsp rtsp://10.100.232.11:5544/live/test110
```

- `idr_freq`Per l'intervallo di frame IDR, è necessario un multiplo intero del GOP. I flussi RTSP devono generare frame IDR per il pull ai flussi.
- `rtsp://10.100.232.11:5544/live/test110`È l'indirizzo URL del flusso push-pull del server RTSP

Esempio di comando ffplay pull:

```shell
ffplay.exe -protocol_whitelist "file,udp,rtp,tcp" -i rtsp://10.100.232.11:5544/live/test110
```

##### 3.2.1.2.2 rtsp push flusso audio

Esempio di comando ffmpeg run:

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f rtsp rtsp://10.100.232.11:5544/live/test110
```

Il comando ffplay pull stream è lo stesso del comando rtsp pull video stream.

##### 3.2.1.2.3 rtsp push flusso audio video

Esempio di comando ffmpeg run:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -f alsa -ac 2 -ar 32000 -i hw:0 -idr_freq 25 -vcodec libk510_h264 -acodec aac -f rtsp rtsp://10.100.232.11:5544/live/test110
```

Il comando ffplay pull stream è lo stesso del comando rtsp pull video stream.

#### 3.2.1.3 flusso push rtmp

Prima dello streaming rtmp, è necessario distribuire il server rtmp per eseguire il push del flusso di dati sul server. I server che supportano il protocollo RTMP includono fms, nginx, srs, ecc.

##### 3.2.1.3.1 rtmp spinge i flussi video

Esempio di comando ffmpeg run:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`L'indirizzo URL per il push del flusso al server rtmp  

Esempio di comando ffplay pull:

```shell
ffplay -fflags nobuffer rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`Per estrarre l'indirizzo URL del flusso dal server rtmp (i flussi push sono uguali all'indirizzo del flusso pull), l'opzione nobuffer -fflags per evitare una maggiore latenza dovuta alla memorizzazione nella cache del lettore.

##### 3.2.1.3.2 flusso audio push rtmp

Esempio di comando ffmpeg run:

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`L'indirizzo URL per il push del flusso al server rtmp

Il comando ffplay pull stream è lo stesso del comando rtmp pull video stream.

##### 3.2.1.3.3 rtmp push flussi audio e video

Esempio di comando ffmpeg run:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -f alsa -ac 2 -ar 32000 -i hw:0 -idr_freq 25 -vcodec libk510_h264 -acodec aac -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`L'indirizzo URL per il push del flusso al server rtmp

Il comando ffplay pull stream è lo stesso del comando rtmp pull video stream.

#### 3.2.1.4 audio3a

##### 3.2.1.4.1 Eseguire l'audio separatamente

(1) Esegui audio3a sulla CPU
Esempio di comando ffmpeg run:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000:dsp_task=0 -f rtp rtp://10.100.232.11:1234
```

(2) Esegui audio3a su dsp
Eseguire due finestre telnet, eseguire l'utilità di pianificazione dSP e ffmpeg in entrambe le finestre (eseguire prima l'utilità di pianificazione DSP)
L'utilità di pianificazione dSP esegue l'istanza del comando:

```shell
cd /app/dsp_app_new/
./dsp_app /app/dsp_scheduler/scheduler.bin
```

Esempio di comando di esecuzione ffmpeg:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000 -f rtp rtp://10.100.232.11:1234
```

##### 3.2.1.4.2 Eseguire audio3a e video contemporaneamente

(1) Esegui audio3a sulla CPU
Esegui due finestre telnet, esegui audio3a e video in entrambe le finestre.
Esempio del comando video:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234
```

Esempio del comando audio3a:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000:dsp_task=0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

L'esecuzione di audio3a e video sulla cpu allo stesso tempo produrrà overflow, si consiglia di eseguire audio3a su dsp
(2) Esegui audio3a su dsp
Eseguire tre finestre telnet, eseguire chiamate audio3a, video e utilità di pianificazione dSP su ciascuna delle tre finestre
Il comando dsp task scheduler run è lo stesso dell'esecuzione di audio3a da solo.

Esempio del comando audio3a:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000 -f rtp rtp://10.100.232.11:1236
```

Esempio del comando video:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234
```

- 10.100.232.11 è l'indirizzo IP del ricevitore rtp.
- Il contenuto del file SDP del terminale ricevente ffplay può essere ottenuto dal registro stampato dopo aver eseguito il comando ffmpeg sopra.

#### 3.2.1.5 v4l2

I parametri configurabili possono essere visualizzati tramite il comando help

```shell
ffmpeg -h demuxer=v4l2 #查看v4l2的配置参数
```

| Il nome del parametro | Interpretazione dei parametri | Il valore predefinito | L'intervallo di valori |
| :-- | :-- | :-- | :-- |
| s | Risoluzione dell'immagine, ad esempio 1920x1080 | NULLO | |
| r | Frame rate, attualmente supporta solo 30fps | 30 | 30 |
| isp | Accendere l'hardware dell'ISP k510 | 0 | 0-1 |
| buf_type | v4l2 buffer`类型` <br>1: V4L2_MEMORY_MMAP: per -vcodec copia<br>2: V4L2_MEMORY_USERPTR: per -vcodec libk510_h264 | 1 | 1~2 |
| Conf | File di configurazione v4L2 | NULLO | |

Esempio di comando in esecuzione ffmpeg: dove 10.100.232.11 è l'indirizzo ricevente, modificato in base alla situazione reale.

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234 -f alsa -ac 2 -ar 16000 -i hw:0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -i /dev/video3 -vcodec copy -y out.yuv
```

Illustrare:

1. Il runtime deve essere trovato nella directory di esecuzione`video_sampe.conf`, `imx219_0.conf`i `imx219_1.conf`file sono configurati e i tre file si trovano nella`/encode_app/` directory.
2. Il video che arriva in tempo reale dalla fotocamera viene scritto come un file YUV e, poiché il file YUV è molto grande, la velocità di scrittura DDR o NFS locale non può tenere il passo, il che potrebbe causare la caduta dei fotogrammi.

#### 3.2.1.6 Codifica JPEG

Output del file:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_jpeg -y test.mjpeg
```

Descrizione: il runtime deve trovarsi nella directory di esecuzione`video_sampe.conf`,`imx219_0.conf`  `imx219_1.conf`i file vengono configurati e i tre file si trovano nella`/encode_app/` directory.

Il file di output test.mjpeg può essere riprodotto sul lato PC con ffplay

```shell
ffplay -i test.mjpeg
```

Flusso push:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_jpeg -an -f rtp rtp://10.100.232.11:1234
```

Sono disponibili flussi pull Ffplay

#### 3.2.1.7 Codifica multiplexing

Supporta fino a 8 codifiche simultanee, è possibile utilizzare la dimensione del fotogramma di ciascun canale moltiplicata per il frame rate e quindi aggiunta, non superare la quantità di dati di 1080p60, -vcodec può scegliere h264 o jpeg.

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -filter_complex 'split=2[out1][out2]' -map '[out1]' -vcodec libk510_h264 -ch 0 -an -f rtp rtp://10.20.1.101:1234 -map '[out2]' -vcodec libk510_h264 -ch 1 -an -f rtp rtp://10.20.1.101:2236
```

```shell
ffmpeg -f v4l2 -s 480x360 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -filter_complex 'split=8[out1][out2][out3][out4][out5][out6][out7][out8]' -map '[out1]' -vcodec libk510_h264 -b:v 300000 -ch 0 -an -f rtp rtp://10.20.1.101:1234 -map '[out2]' -vcodec libk510_h264 -b:v 300000 -ch 1 -an -f rtp rtp://10.20.1.101:2322 -map '[out3]' -vcodec libk510_h264 -b:v 300000 -ch 2 -an -f rtp rtp://10.20.1.101:3086 -map '[out4]' -vcodec libk510_h264 -b:v 300000 -ch 3 -an -f rtp rtp://10.20.1.101:4234 -map '[out5]' -vcodec libk510_h264 -b:v 300000 -ch 4 -an -f rtp rtp://10.20.1.101:5216 -map '[out6]' -vcodec libk510_h264 -b:v 300000 -ch 5 -an -f rtp rtp://10.20.1.101:6788 -map '[out7]' -vcodec libk510_h264 -b:v 300000 -ch 6 -an -f rtp rtp://10.20.1.101:7230 -map '[out8]' -vcodec libk510_h264 -b:v 300000 -ch 7 -an -f rtp rtp://10.20.1.101:8976
```

Quando si utilizza ffplay per estrarre flussi, fare attenzione a estrarre un solo video, cambiare il video di altre strade modificando il numero di porta nel file SDP o avviare più flussi ffplay.

### 3.2.2 Istruzioni per il porting del programma

`ffmpeg``ffmpeg`Convertito nella versione open source 4.4,`xxx.patch` aggiunto per il service pack

- `ff_libk510_h264_encoder`: Controllo della codifica hardware h264, a cui si fa riferimento`libvenc.so`
- `ff_libk510_jpeg_encoder`: controlla la codifica hardware jpeg, a cui si fa riferimento`libvenc.so`
- v4l2: in v4l2.c è stato aggiunto codice relativo all'hardware k510 e il tipo di buffer v4l2 V4L2_MEMORY_USERPTR e referenziato`libmediactl.so`.

#### 3.2.2.1 Comando di generazione patch

（1）

```shell
quilt new -p ab xxx.patch #在patches目录下生成xxx.patch文件
quilt add <filename> #添加修改前的文件
### 修改代码 ###
quilt refresh #修改内容被添加到xxx.patch
```

（2）
Copiare xxx.patch nella directory package/ffmpeg_canaan e modificare il percorso del file nel file della patch in base al percorso corrente.

```shell
mv ../../patches/xxx.patch ../../package/ffmpeg_canaan
rm ../../patches/series
sed -i "s/\/dl\/ffmpeg_canaan\/ffmpeg-4.4//g" ../../package/ffmpeg_canaan/xxx.patch
```

#### 3.2.2.2 Configurazione ffmpeg

Nel `package/ffmpeg_canaan/ffmpeg.mk`file, il core della CPU può essere modificato, la toolchain di compilazione e l'abilitazione può essere effettuata tramite l'opzione`ff_k510_video_demuxer` configee.`ff_libk510_jpeg_encoder` `ff_libk510_h264_encoder`

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

**Traduzione Disclaimer**  
Per la comodità dei clienti, Canaan utilizza un traduttore AI per tradurre il testo in più lingue, che possono contenere errori. Non garantiamo l'accuratezza, l'affidabilità o la tempestività delle traduzioni fornite. Canaan non sarà responsabile per eventuali perdite o danni causati dall'affidamento sull'accuratezza o sull'affidabilità delle informazioni tradotte. Se c'è una differenza di contenuto tra le traduzioni in lingue diverse, prevarrà la versione cinese semplificata.

Se desideri segnalare un errore di traduzione o un'inesattezza, non esitare a contattarci via mail.
