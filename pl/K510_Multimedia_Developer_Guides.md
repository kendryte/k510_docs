![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 Multimedia Przewodnik programisty</font>**

<font face="黑体"  size=3>Wersja dokumentu: V1.0.0</font>

<font face="黑体"  size=3>Opublikowano: 2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Zrzeczenie się**</font>
Zakupione produkty, usługi lub funkcje podlegają umowom handlowym i warunkom Beijing Canaan Jiesi Information Technology Co., Ltd. ("Spółka", ta sama poniżej), a wszystkie lub część produktów, usług lub funkcji opisanych w niniejszym dokumencie może nie być objęta zakresem zakupu lub użytkowania. O ile nie uzgodniono inaczej w umowie, Firma zrzeka się wszelkich oświadczeń lub gwarancji, wyraźnych lub dorozumianych, co do dokładności, niezawodności, kompletności, marketingu, konkretnego celu i nieagresji jakichkolwiek oświadczeń, informacji lub treści tego dokumentu. O ile nie uzgodniono inaczej, niniejszy dokument jest dostarczany jako wskazówka wyłącznie do użytku.
Ze względu na aktualizacje wersji produktu lub z innych powodów zawartość tego dokumentu może być od czasu do czasu aktualizowana lub modyfikowana bez powiadomienia.

**<font face="黑体"  size=3>Informacje o znakach towarowych</font>**

""<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, ikona "Canaan", Canaan i inne znaki towarowe Canaan oraz inne znaki towarowe Canaan są znakami towarowymi Beijing Canaan Jiesi Information Technology Co., Ltd. Wszystkie inne znaki towarowe lub zarejestrowane znaki towarowe, które mogą być wymienione w niniejszym dokumencie, są własnością ich odpowiednich właścicieli.

**<font face="黑体"  size=3>Prawa autorskie ©2022 Beijing Canaan Jiesi Information Technology Co., Ltd</font>**
Niniejszy dokument ma zastosowanie wyłącznie do rozwoju i projektowania platformy K510, bez pisemnej zgody firmy, żadna jednostka ani osoba fizyczna nie może rozpowszechniać części lub całości treści tego dokumentu w jakiejkolwiek formie.

**<font face="黑体"  size=3>Pekin Canaan Jiesi Information Technology Co Ltd</font>**
Adres internetowy: canaan-creative.com
Zapytania biznesowe: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# przedmowa
## Przeznaczenie dokumentu
Niniejszy dokument jest dokumentem wyjaśniającym przykład aplikacji K510 Multimedia.
## Docelowej
Dla których niniejszy dokument jest przeznaczony:
- Programiści
- Personel wsparcia technicznego

## Historia zmian

| Numer wersji    | Zmodyfikowane przez | Data aktualizacji| Uwagi do poprawek  |  
|  ------  |-------| -------| ------ |
| wersja 1.0.0    |Grupy oprogramowania systemowego | 2022-03-09 | SDK V1.5 wydany |
|     |     |      |   |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Treść</font>**

[TOC]

# 1 Interfejs API kodera

## 1.1 Opis pliku nagłówka

k510_buildroot/pakiet/encode_app/enc_interface.h

## 1.2 Opisy funkcji API

### 1.2.1 VideoEncoder_Create

【Opis】

Tworzenie kodera wideo

【Gramatyka】

```c
EncoderHandle* VIdeoEncoder_Create(EncSettings *pCfg)
```

【Parametry】

pCfg: Wprowadź parametry konfiguracji kodowania

|            Nazwa parametru             | Interpretacja parametrów                                                     |                           Zakres wartości                           | Odpowiednie moduły kodowania |
| :---------------------------: | :----------------------------------------------------------- | :----------------------------------------------------------: | ------------ |
|            kanał            | Numer kanału, obsługuje do 8 kodowanych kanałów                                   |                            [0，7]                            | jpeg、avc    |
|             Szerokość             | Koduje szerokość obrazu                                                 | avc: [128,2048], wielokrotność 8 <br/> jpeg: do 8192, wielokrotność 16 | jpeg、avc    |
|            wysokość             | Kodowanie wysokości obrazu                                                 | avc: [64,2048], wielokrotność 8 <br/> jpeg: do 8192, wielokrotność 2 | jpeg、avc    |
|           Liczba klatek na sekundę           | Liczba klatek na sekundę, którą można skonfigurować tylko do ustalonych kilku wartości                                    |                       (25,30,50,60,75)                       | jpeg、avc    |
|            tryb rcMode             | Tryb sterowania przepływnością 0:CONST_QP 1:CBR 2:VBR<br />jpeg został ustalony na CONST_QP  |                       Zobacz RateCtrlMode                       | jpeg,avc    |
|            BitRate            | Docelowa przepływność w trybie CBR lub najniższa przepływność w trybie VBR                    |                        [10,20000000]                         | głaskać          |
|          MaxBitRate           | Najwyższa przepływność w trybie VBR                                          |                        [10,20000000]                         | głaskać          |
|            SliceQP            | Początkowa wartość QP, -1 dla auto                                        |                avc:-1,jpeg[0,51]<br/>:[1,100]                | jpeg,avc    |
|             MinQP             | Minimalna wartość qp                                                     |                         [0,sliceqp]                          | głaskać          |
|             MaxQP             | Maksymalna wartość qp                                                     |                         [sliceqp,54]                         | głaskać          |
|            profil            | profile_idc parametry w SPS: 0: base 1:main 2:high 3:jpeg       |                            [0,3]                             | jpeg,avc    |
|             poziom             | level_idc parametry w PS                                       |                           [10,42]                            | głaskać          |
|          AspectRatio          | Skala wyświetlacza                                                     |                     Zobacz AVC_AspectRatio                      | jpeg,avc    |
|            FreqIDR            | Interwał między dwiema ramkami idr                                              |                           [1,1000]                           | głaskać          |
|            gopLen             | Grupa obrazów, interwał między dwiema klatkami I                      |                           [1,1000]                           | głaskać          |
|          bEnableGDR           | Czy włączyć odświeżanie w ramce                                             |                         [prawda, fałsz]                         | głaskać          |
|            gdrMode            | Tryb odświeżania gdr: 0, odświeżanie pionowe 1, odświeżanie poziome                        |                       Zobacz GDRCtrlMode                        | głaskać          |
|          bEnableLTR           | Czy włączone są długoterminowe układy odniesienia                                           |                         [prawda, fałsz]                         | głaskać          |
|          roiCtrlMode          | Tryb kontroli ROI: 0: Nie używaj roi 1: względne qp 2: bezwzględne qp                 |                       Zobacz ROICtrlMode                        | głaskać          |
|       EncSliceSplitCfg        | wdrożenie dzielenia plasterków                                               |                                                              | głaskać          |
|         bSplitEnable          | Czy podział plasterków jest włączony                                           |                         [prawda, fałsz]                         | głaskać          |
|         u32SplitMode          | Tryb segmentacji plasterków: 0: Podzielony na bity. <br />1: Podział według wierszy makrobloków        |                            [0,1]                             | głaskać          |
|         u32SliceSize          | u32SplitMode=0, wskazując liczbę bajtów na plasterek<br /> u32SplitMode=1, reprezentuje liczbę<br /> wierszy makrobloku na plasterek| u32SplitMode=[100,65535]<br />0,u32SplitMode=1,[1, (wysokość obrazu +15)/16] | głaskać          |
|          entropiaMode          | Kodowanie entropii, 0: CABAC 1: CAVLC                                |                      Zobacz EncEntropyMode                      | głaskać          |
|          encDblkCfg           | Konfiguracja filtrowania bloków                                                 |                                                              | głaskać          |
| disable_deblocking_filter_idc | Wartość domyślna to 0, co oznacza H.264 Agreement                          |                            [0，2]                            | głaskać          |
|  slice_alpha_c0_offset_div2   | Wartość domyślna to 0, co oznacza H.264 Agreement                          |                           [-6，6]                            | głaskać          |
|    slice_beta_offset_div2     | Wartość domyślna to 0, co oznacza H.264 Agreement                          |                          [-6,   6]                           | głaskać          |

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

【Zwracana wartość】

```c
typedef void* EncoderHandle
```

### 1.2.2 VideoEncoder_SetRoiCfg

【Opis】

ustawienie roi, obsługa do 8 prostokątnych obszarów, system zgodnie z numerem indeksu 0 ~ 7 do zarządzania obszarem ROI, uIndex wskazuje, że użytkownik ustawia numer indeksu ROI. Regiony ROI mogą być nakładane na siebie, a gdy wystąpi nakładka, priorytet między regionami ROI wzrasta kolejno od numeru indeksu 0 do 7.

Może być używany po utworzeniu enkodera i przed jego zniszczeniem. Region roi można dynamicznie regulować podczas procesu kodowania.

【Gramatyka】

```c
EncStatus VideoEncoder_SetRoiCfg(EncoderHandle *hEnc,const EncROICfg*pEncRoiCfg);
```

【Parametry】

hEnc: Uchwyt zwrócony w czasie tworzenia

pEncRoiCfg: Informacje o konfiguracji strefy Roi

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

Opis parametru

```text
uIndex     - 指定该roi区域索引号，范围0-7最多支持8个区域
bEnable    - 指定该区域是否使能，只有使能的区域才有效
uQpValue   - qp值，可以是相对qp或绝对qp，qp模式由EncSettings中roiCtrlMode属性决定。绝对qp范围                  [0,51]，相对qp范围[-31,31]
stRect     - roi矩形区域，s32X矩形左上角x值，s32Y矩形左上角y值，u32Width矩形宽度，u32Height矩形高度
```

【Zwracana wartość】

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.3 VideoEncoder_SetLongTerm

【Opis】

Ustawia następną klatkę kodowania na długoterminową ramkę odniesienia. Może być używany po utworzeniu enkodera i przed jego zniszczeniem. Atrybut bEnableLTR w EncSettings określa, czy funkcja jest włączona.

【Gramatyka】

```c
EncStatus VideoEncoder_SetLongTerm(EncoderHandle *hEnc);
```

【Parametry】

hEnc: Uchwyt zwrócony w czasie tworzenia

【Zwracana wartość】

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.4 VideoEncoder_UseLongTerm

【Opis】

Ustawia kodowanie na następną klatkę przy użyciu długoterminowego układu odniesienia. Może być używany po utworzeniu enkodera i przed jego zniszczeniem. Atrybut bEnableLTR w EncSettings określa, czy funkcja jest włączona.

【Gramatyka】

```c
EncStatus VideoEncoder_UseLongTerm(EncoderHandle *hEnc);
```

【Parametry】

hEnc: Uchwyt zwrócony w czasie tworzenia

【Zwracana wartość】

```c
typedef enum
{
    Enc_SUCCESS = 0,
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.5 VideoEncoder_InsertUserData

【Opis】

Wstawianie danych użytkownika.

Może być używany po utworzeniu kodera i przed jego zniszczeniem, a zawartość danych użytkownika może być modyfikowana w czasie rzeczywistym podczas procesu kodowania. Dane użytkownika zostaną wstawione do obszaru danych SEI ramki IDR.

【Gramatyka】

```c
EncStatus      VideoEncoder_InsertUserData(EncoderHandle *hEnc,char*pUserData,unsigned int nlen);
```

【Parametry】

hEnc: Uchwyt zwrócony w czasie tworzenia

pUserData: Wskaźnik do danych użytkownika

nlen: Długość danych użytkownika (0, 1024)

【Zwracana wartość】

```c
typedef enum
{
    Enc_SUCCESS = 0,
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.6 VideoEncoder_Destory

【Opis】

Zniszcz wideoenkoder

【Gramatyka】

```c
EncStatus VideoEncoder_Destroy(EncoderHandle *hEnc)
```

【Parametry】

hEnc: Uchwyt zwrócony w czasie tworzenia

【Zwracana wartość】

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.7 VideoEncoder_EncodeOneFrame

【Opis】

Kodowanie klatki wideo

【Gramatyka】

```c
EncStatus VideoEncoder_EncodeOneFrame(EncoderHandle *hEnc, EncInputFrame *input)
```

【Parametry】

hEnc: Uchwyt zwrócony w czasie tworzenia

wejście: Wprowadź dane wideo YUV

```c
typedef struct
{
    unsigned short width;
    unsigned short height;
    unsigned short stride;
    unsigned char *data;
}EncInputFrame;
```

【Zwracana wartość】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.2.8 VideoEncoder_GetStream

【Opis】

Pobiera bufor strumienia kodowania wideo, Uwaga: Ta przestrzeń buforowa jest przydzielana wewnętrznie przez koder.

【Gramatyka】

```c
EncStatus VideoEncoder_GetStream(EncoderHandle *hEnc, EncOutputStream *output)
```

【Parametry】

hEnc: Uchwyt zwrócony w czasie tworzenia

wyjście: Wyjście zakodowanego bufora danych strumienia, bufSize jest większy niż 0, aby uzyskać wyjście

```c
typedef struct
{
    unsigned char *bufAddr;
    unsigned int bufSize; 
}EncOutputStream;
```

【Zwracana wartość】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.2.9 VideoEncoder_GetStream_ByExtBuf

【Opis】

Pobiera bufor strumienia kodowania wideo, Uwaga: Przestrzeń buforowa musi zostać przydzielona przez konsumenta przed wywołaniem tej funkcji.

【Gramatyka】

```c
EncStatus VideoEncoder_GetStream(EncoderHandle *hEnc, EncOutputStream *output)
```

【Parametry】

hEnc: Uchwyt zwrócony w czasie tworzenia

wyjście: Wyjście zakodowanego bufora danych strumienia, bufSize jest większy niż 0, aby uzyskać wyjście

```c
typedef struct
{
    unsigned char *bufAddr;
    unsigned int bufSize; 
}EncOutputStream;
```

【Zwracana wartość】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.3.0 VideoEncoder_ReleaseStream

【Opis】

Zwalnianie bufora strumienia kodowania wideo

【Gramatyka】

```c
EncStatus VideoEncoder_ReleaseStream(EncoderHandle *hEnc, EncOutputStream *output)
```

【Parametry】

- hEnc: Uchwyt zwrócony w czasie tworzenia
- wyjście:VideoEncoder_GetStream zwrócony bufor

【Zwracana wartość】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

# 2 Diagram struktury sprzętowej i architektura oprogramowania

# 2.1 Diagram struktury sprzętu

Schemat blokowy sprzętowy K510 jest następujący:
![hardware_block_diagram](../zh/images/multimedia_guides/hardware_block_diagram.png)

Dane otrzymane z czujnika wideo są przetwarzane przez MIPI DPHY, CSI, VI, isP w celu uzyskania danych źródłowych yuv i przechowywane w DDR. Moduł kodera h264 odczytuje dane z DDR, wykonuje operacje kodowania i przechowuje wyniki operacji w DDR.

# 2.2 Architektura oprogramowania

Architektura oprogramowania multimedialnej platformy programistycznej jest następująca:

![multimedia_block_diagram.png](../zh/images/multimedia_guides/multimedia_block_diagram.png)

w tym miejscu

- `libvenc`: Biblioteka enkodera do wywoływania rdzenia enkodera h264
- `libmediactl`: Biblioteka ISP do sterowania czujnikami
- `libaudio3a`: Biblioteka Audio3a dla operacji 3a na audio
- `alsa-lib`: Biblioteka audio do sterowania interfejsem audio

# 3 Aplikacja demonstracyjna

## 3.1 Kodowanie aplikacji

Program umieszczony jest`/app/encode_app` w katalogu:

- `encode_app`: Kodowanie programu aplikacyjnego
- Plik yuv używany do testowania jest duży i nie pasuje do pakietu SDK

biegać`encode_app`

| Nazwa parametru | Interpretacja parametrów | Wartość domyślna | Zakres wartości | Odpowiednie moduły kodowania |
|:-|:-|:-|:-|:-|
| Pomoc | Informacje pomocy| | ||
| rozszczepiać | Liczba kanałów | ZERO | [1,4] | jpeg、avc |
| Ch | Numer kanału (oparty na 0) | ZERO | [0,3] | jpeg、avc |
| ja | Wprowadź plik YUV, obsługuje tylko**format** nv12| ZERO | v4l2 <br> xxx.yuv | jpeg、avc |
| Dev | Nazwa urządzenia v4l2 | ZERO | **sensor0:** /dev/video3 /dev/video4 <br> <br>sensor1:<br> **/dev/video7 /** dev/ <br> video8 <br> | głaskać |
| lub | wyjście| ZERO | rtsp <br> xxx.264 <br> xxx.MJPEG <br> xxx.JPEG | jpeg、avc |
| w | Szerokość obrazu wyjściowego | 1920 | avc: [128,2048], wielokrotność 8 <br> jpeg: do 8192, wielokrotność 16 | jpeg、avc |
| h | Wysokość obrazu wyjściowego | 1080 | avc: [64,2048], wielokrotność 8 <br> jpeg: do 8192, wielokrotność 2 | jpeg、avc |
| Fps | Aparat rejestruje liczbę klatek na sekundę, która obecnie obsługuje tylko 30pfs | 30 | 30 | głaskać |
| r | Zakodowana wyjściowa liczba klatek na sekundę | 30 | Liczba, która może być podzielna lub podzielna przez fps | głaskać |
| ramki wejściowe | Wprowadź liczbę klatek yuv | 0 | [0,50] | jpeg、avc |
| outframes | Wyjście ramek yuv, jeśli są większe niż parametr -inframes, będą powtarzane kodowanie | 0 | [0,32767] | jpeg、avc |
| Gop | Grupa obrazów, interwał między dwiema klatkami I | 25 | [1,1000] | głaskać |
| rcmode | Reprezentuje tryb sterowania przepływnością 0:CONST_QP 1:CBR 2:VBR | CBR | [0,2] | głaskać |
| przepływność | Docelowa szybkość transmisji bitów w trybie CBR lub najniższa szybkość transmisji bitów w trybie VBR, w KB | 4000 | [1,20000] | głaskać |
| maxbitrate | Najwyższa przepływność w trybie VBR, w Kb | 4000 | [1,20000] | głaskać |
| profil | profile_idc parametry w SPS: 0: base 1:main 2:high 3:jpeg | AVC_HIGH | [0,3] | jpeg、avc |
| poziom | level_idc parametry w SPS | 42 | [10,42] | głaskać |
| sliceqp | Początkowa wartość QP, -1 dla auto | 25 | avc:-1,jpeg[0,51]<br/>:[1,100] | jpeg、avc |
| minqp | Minimalna wartość QP | 0 | [0,sliceqp] | głaskać |
| maxqp | Maksymalna wartość QP | 54 | [sliceqp,54] | głaskać |
| enableLTR | Włącza długoterminowe ramki odniesienia, a parametry określają okres odświeżania. 0: Cykl odświeżania nie jest włączony. Pozytywny: Okresowo ustawia układ odniesienia, a następna ramka jest ustawiona tak, aby używała długiego układu odniesienia. | 0 | [0,65535] | głaskać |
| król | Plik konfiguracyjny Roi, który określa wiele regionów roi | ZERO | xxx.conf | głaskać |
| Ae | Włącz AE | 0 | 0 - Nie włącza AE<br>1 - Włącz AE | |
| Conf | Plik konfiguracyjny vl42 modyfikuje parametry konfiguracyjne v4l2 na podstawie określonego pliku konfiguracyjnego i parametrów wejściowych wiersza polecenia | ZERO | xxx.conf | głaskać |

### 3.1.1 Wprowadź plik yuv i wyjdź plik

```shell
./encode_app -split 1 -ch 0 -i your_file.yuv -o out.264 -w 1920 -h 1080 -inframes 10 -outframes 30
./encode_app -split 1 -ch 0 -i your_file.yuv -o out.mjpeg -w 1920 -h 1080 -inframes 10 -outframes 30
```

### 3.1.2 Wejście v4l2, wyjście rtsp push stream

#### 3.1.2.1 Jednokanałowy

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

Przykład polecenia ffplay pull:

```shell
 ffplay -rtsp_transport tcp rtsp://192.168.137.11:8554/testStream
```

- `rtsp://192.168.137.11:8554/testStream`W przypadku adresu URL strumienia rtsp -rtsp_transport tcp oznacza użycie tcp do przesyłania danych audio i wideo (udp jest używany domyślnie), a opcja nobuffer -fflags może zostać dodana, aby uniknąć zwiększonego opóźnienia spowodowanego buforowaniem odtwarzacza.

#### 3.1.2.2 Podwójna kamera z pojedynczym kanałem

```shell
./encode_app -split 2 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -ch 1 -i v4l2 -dev /dev/video4 -o rtsp -w 1280 -h 720 -conf video_sample.conf
```

Polecenie ffplay pull stream jest takie samo jak powyżej.

#### 3.1.2.3 Podwójne kamery

```shell
./encode_app -split 2 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -ch 1 -i v4l2 -dev /dev/video7 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

Polecenie ffplay pull stream jest takie samo jak powyżej.

#### 3.1.2.4 Badanie ROI

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -sliceqp -1 -bitrate 2048 -roi roi_1920x1080.conf -conf video_sample.conf
```

format pliku roi

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

Opis parametru:

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

Polecenie ffplay pull stream jest takie samo jak powyżej.

### 3.1.3 Transformacja liczby klatek na sekundę

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -r 60 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

Polecenie ffplay pull stream jest takie samo jak powyżej.

### 3.1.4 Wiele wejściowych liczb klatek na sekundę

VGA@75fps i 720p60 są obecnie obsługiwane

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 640 -h 480 -fps 75 -r 75 -conf video_sample_vga480p75.conf
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1280 -h 720 -fps 60 -r 60 -conf video_sample_720p60.conf
```

Polecenie ffplay pull stream jest takie samo jak powyżej.

### 3.1.5 rtsp push strumienie audio i wideo

```c
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -alsa 1 -ac 2 -ar 44100 -af 2 -ad hw:0 -conf video_sample.conf
```

Polecenie ffplay pull stream jest takie samo jak powyżej.

### 3.1.6 Środki ostrożności

- Środowisko pracy: Czujnik płytki rdzenia: IMX219_SENSOR

- Format adresu strumienia rtsp: adres rtsp://ip: numer portu / testStream, gdzie adres IP i numer portu są zmienne, a reszta jest stała.

  Takie jak: rtsp://192.168.137.11:8554/testStream, gdzie adres IP to 192.168.137.11, numer portu to 8554.

  Adres IP: Adres IP płytki programistycznej, wprowadź ifconfig na płycie, aby uzyskać.

  Numer portu: 8554 + <通道号>*2, numery kanałów zazwyczaj zaczynają się od 0 (-ch 0, -ch 1...).

- Odtwórz tryb strumienia RTSP: odpowiedni strumień RTSP może być odtwarzany przez vlc lub ffplay, a strumień danych może być przesyłany przez protokół udp lub TCP.

  1)rtp over udp播放:ffplay -rtsp_transport udp rtsp://192.168.137.11:8554/testStream

  2)rtp over tcp 播放: ffplay -rtsp_transport tcp rtsp://192.168.137.11:8554/testStream

  Zaleca się używanie rtp przez tcp do gry, aby uniknąć ekranu spowodowanego utratą pakietów udp.

## 3.2 ffmpeg

ffmpeg jest umieszczony w katalogu /usr/local/bin.

- `ffmpeg`: aplikacja ffmpeg.

biegać`ffmpeg`

(1) Parametr libk510_h264 enkodera
| Nazwa parametru | Interpretacja parametrów | Wartość domyślna | Zakres wartości |
|:-|:-|:-|:-|
| g | rozmiar gop | 25 | 1 ~ 1000 |
| b | przepływność | 4000000 | 0 ~ 20000000 |
| r | Liczba klatek na sekundę, ponieważ isp obsługuje obecnie tylko 30 klatek na sekundę, więc dekoder powinien być ustawiony na 30 | 30 | 30 |
| idr_freq | Częstotliwość IDR | -1 (bez IDR) | -1 ~ 256 |
| Qp | Podczas kodowania za pomocą cqp skonfiguruj wartość qp | -1 (automatyczny) | -1 ~ 100 |
| maxrate | Maksymalna wartość przepływności | 0 | 20000000 |
| profil | Obsługiwane profile | 2 (wysoki) | 0 - linia podstawowa <br> 1 - główna <br> 2 - wysoka |
| poziom | Poziom kodowania | 42 | 10 ~ 42 |
| chciałby | Proporcje ekranu | 0 (automatyczny) | 0 - auto <br> 1 - 4:3 <br> 2 - 16:9 <br> 3 - brak |
| Ch | numer kanału | 0 | 0-7 |
| framesToEncode | Liczba zakodowanych klatek | -1 (wszystkie klatki) | -1 ~ 16383 |

(2) Parametry libk510_jpeg enkodera
| Nazwa parametru | Interpretacja parametrów | Wartość domyślna | Zakres wartości |
|:-|:-|:-|:-|
| Qp | Podczas kodowania za pomocą cqp skonfiguruj wartość qp | 25 | -1 ~ 100 |
| r | liczba klatek na sekundę | 30 | 25 ~ 60 |
| Ch | kodowanie kanału | 0 | 0 ~ 7 |
| maxrate | Maksymalna przepływność. (0=ignoruj) | 4000000 | 0 ~ 20000000 |
| chciałby | Proporcji | 0 (automatyczny) | 0 - auto <br> 1 - 4:3 <br> 2 - 16:9 <br> 3 - brak |

(3) Parametr libk510_video urządzenia
| Nazwa parametru | Interpretacja parametrów | Wartość domyślna | Zakres wartości |
|:-|:-|:-|:-|
| Wh | rozmiar ramy | ZERO | **dla enkodera libk510_h264:**:<br>  do 2048x2048 <br> szerokość wielokrotność 8 <br> wysokości wielokrotność 8 <br> min. szerokość: 128 <br> min. wysokość: 64 <br> **dla enkodera libk510_jpeg:** <br> do 8192x8192 <br> szerokość wielokrotność 16 <br> wysokości wielokrotność 2 |
| Exp | parametr ekspozycji | 0 | 0 ~ 128 |
| Agc | wzmocnienie analogowe | 0 | 0 ~ 232 |

(4) parametr audio3a
| Nazwa parametru | Interpretacja parametrów | Wartość domyślna | Zakres wartości |
|:-|:-|:-|:-|
| sample_rate | Częstotliwość próbkowania dźwięku | 16000 | 1 ~ 65535 |
| Agc | Tryb wzmocnienia dźwięku | 3 (AgcModeFixedDigital) | 0 - AgcModeUnchanged <br> 1 - AgcModeAdaptiveAnalog <br> 2 - AgcModeAdaptiveDigital <br> 3 - AgcModeFixedDigital |
| Ns | Poziom hałasu | 3 (bardzo wysoki) | 0 - Niski <br> 1 - Umiarkowany <br> 2 - Wysoki <br> 3 - BardzoWysoki |
| dsp_task | Pozycja biegowa Auido3a | 1(dsp) | 0 - cpu <br>1 - dsp |

Konfigurowalne parametry można przeglądać za pomocą polecenia pomocy

```shell
ffmpeg -h encoder=libk510_h264 #查看k510编码器的参数
ffmpeg -h demuxer=v4l2 #查看demuxer的配置参数
ffmpeg -h filter=audio3a #查看audio3a的配置参数
```

Logiczne pole dla ffmpeg jest następujące:

![ffmpeg_block_diagram](../zh/images/multimedia_guides/ffmpeg_block_diagram.png)

audio3a służy do wykonywania operacji 3a na odebranym dźwięku i wyprowadzaniu go, a jego logiczny schemat blokowy jest następujący:

![ffmpeg_canaan_audio3a](../zh/images/multimedia_guides/ffmpeg_canaan_audio3a.png)

### 3.2.1 Instrukcja obsługi programu

#### 3.2.1.1 rtp stream push

##### 3.2.1.1.1. Strumień wideo rtp push

Przykład polecenia ffmpeg run:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.102.231.29:1234
```

W przypadku gdy adres odbioru jest 10.102.231.29, zmienia się go w zależności od aktualnej sytuacji.
Naciśnij "q", gdy program jest uruchomiony, aby przestać działać.

ffplay otrzymuje polecenie:

```shell
ffplay.exe -protocol_whitelist "file,udp,rtp" -i test.sdp -fflags nobuffer -analyzeduration 1000000 -flags low_delay
```

Plik Test.sdp jest skonfigurowany w następujący sposób.

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

Opis parametru .sdp:

- c=: Informacje o linku do nośnika; IN: Typ sieci; IP4: Typ adresu; Po którym następuje adres IP (zauważ, że jest to adres IP, na którym znajduje się odbiornik, a nie adres IP nadawcy)
- m= jest początkiem sesji na poziomie multimediów, wideo:typ nośnika; 1234: Numer portu; RTP/AVP: Protokół transportowy; 96: Format ładunku w nagłówku rtp
Zmodyfikuj adres IP i numer portu odbiornika zgodnie z rzeczywistą sytuacją i pamiętaj, że numer portu rtp musi być parzysty.

##### 3.2.1.1.2. Strumień audio rtp push

Przykład polecenia ffmpeg run:

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f rtp rtp://10.100.232.11:1234
```

W przypadku gdy adres odbiorcy jest 10.100.232.11, jest on modyfikowany zgodnie z aktualną sytuacją.

- ac: Ustawia liczbę kanałów audio
- ar: Ustawia częstotliwość próbkowania dźwięku.

Polecenie ffplay receive jest takie samo jak odbieranie strumienia wideo, a plik sdp odnosi się do poniższego przykładu.

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

##### 3.2.1.1.3 strumienie audio i wideo rtp push

Przykład polecenia ffmpeg run:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234 -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

Polecenie ffplay receive jest takie samo jak odbieranie strumienia audio, a plik sdp odnosi się do poniższego przykładu.

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

#### 3.2.1.2 rtsp push stream

Zanim rtsp wypchnie strumień, musisz wdrożyć serwer rtsp, aby wypchnąć strumień danych na serwer.

##### 3.2.1.2.1 strumienie wideo wypychane na 3.1.2.2.1.1 rtsp

Przykład polecenia ffmpeg run:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -acodec copy -f rtsp rtsp://10.100.232.11:5544/live/test110
```

- `idr_freq`Dla interwału ramki IDR wymagana jest całkowita wielokrotność GOP. Strumienie RTSP muszą generować ramki IDR, aby pobierać je do strumieni.
- `rtsp://10.100.232.11:5544/live/test110`Jest adresem URL strumienia push-pull serwera RTSP

Przykład polecenia ffplay pull:

```shell
ffplay.exe -protocol_whitelist "file,udp,rtp,tcp" -i rtsp://10.100.232.11:5544/live/test110
```

##### 3.2.1.2.2 rtsp push audio stream

Przykład polecenia ffmpeg run:

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f rtsp rtsp://10.100.232.11:5544/live/test110
```

Polecenie ffplay pull stream jest takie samo jak polecenie rtsp pull video stream.

##### 3.2.1.2.3 rtsp push audio video stream

Przykład polecenia ffmpeg run:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -f alsa -ac 2 -ar 32000 -i hw:0 -idr_freq 25 -vcodec libk510_h264 -acodec aac -f rtsp rtsp://10.100.232.11:5544/live/test110
```

Polecenie ffplay pull stream jest takie samo jak polecenie rtsp pull video stream.

#### 3.2.1.3 strumień push rtmp

Przed przesyłaniem strumieniowym rtmp należy wdrożyć serwer rtmp, aby wypchnąć strumień danych na serwer. Serwery obsługujące protokół RTMP to fms, nginx, srs itp.

##### 3.2.1.3.1 rtmp wypycha strumienie wideo

Przykład polecenia ffmpeg run:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`Adres URL do wypychania strumienia na serwer rtmp  

Przykład polecenia ffplay pull:

```shell
ffplay -fflags nobuffer rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`Aby pobrać adres URL strumienia z serwera rtmp (strumienie push są takie same jak adres strumienia ściągania), opcja -fflags nobuffer, aby uniknąć zwiększonego opóźnienia spowodowanego buforowaniem odtwarzacza.

##### 3.2.1.3.2 rtmp push audio stream

Przykład polecenia ffmpeg run:

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`Adres URL do wypychania strumienia na serwer rtmp

Polecenie ffplay pull stream jest takie samo jak polecenie rtmp pull video stream.

##### 3.2.1.3.3 rtmp wypycha strumienie audio i wideo

Przykład polecenia ffmpeg run:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -f alsa -ac 2 -ar 32000 -i hw:0 -idr_freq 25 -vcodec libk510_h264 -acodec aac -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`Adres URL do wypychania strumienia na serwer rtmp

Polecenie ffplay pull stream jest takie samo jak polecenie rtmp pull video stream.

#### 3.2.1.4 audio3a

##### 3.2.1.4.1 Uruchamianie dźwięku oddzielnie

(1) Uruchom audio3a na procesorze
Przykład polecenia ffmpeg run:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000:dsp_task=0 -f rtp rtp://10.100.232.11:1234
```

(2) Uruchom audio3a na dsp
Uruchom dwa okna telnet, uruchom harmonogram zadań dsp i ffmpeg w obu oknach (najpierw uruchom harmonogram zadań dsp)
Harmonogram zadań dsp uruchamia instancję polecenia:

```shell
cd /app/dsp_app_new/
./dsp_app /app/dsp_scheduler/scheduler.bin
```

Przykład polecenia ffmpeg run:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000 -f rtp rtp://10.100.232.11:1234
```

##### 3.2.1.4.2 Uruchamiaj audio3a i wideo w tym samym czasie

(1) Uruchom audio3a na procesorze
Uruchom dwa okna Telnet, uruchom audio3a i wideo w obu oknach.
Przykład polecenia wideo:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234
```

Przykład polecenia audio3a:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000:dsp_task=0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

Uruchamianie audio3a i wideo na procesorze w tym samym czasie spowoduje przepełnienie, zaleca się uruchomienie audio3a na dsp
(2) Uruchom audio3a na dsp
Uruchom trzy okna Telnet, uruchom harmonogram połączeń audio3a, wideo i dsp w każdym z trzech okien
Polecenie uruchamiania harmonogramu zadań dsp jest takie samo jak uruchamianie samego audio3a.

Przykład polecenia audio3a:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000 -f rtp rtp://10.100.232.11:1236
```

Przykład polecenia wideo:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234
```

- 10.100.232.11 to adres IP odbiornika rtp.
- Zawartość pliku SDP terminala odbiorczego ffplay można uzyskać z wydrukowanego dziennika po uruchomieniu powyższego polecenia ffmpeg.

#### 3.2.1.5 v4l2

Konfigurowalne parametry można przeglądać za pomocą polecenia pomocy

```shell
ffmpeg -h demuxer=v4l2 #查看v4l2的配置参数
```

| Nazwa parametru | Interpretacja parametrów | Wartość domyślna | Zakres wartości |
| :-- | :-- | :-- | :-- |
| s | Rozdzielczość obrazu, na przykład 1920x1080 | ZERO | |
| r | Liczba klatek na sekundę, obecnie obsługuje tylko 30 klatek na sekundę | 30 | 30 |
| isp | Włączanie sprzętu k510 ISP | 0 | 0-1 |
| buf_type | v4l2 buffer`类型` <br>1: V4L2_MEMORY_MMAP: for -vcodec copy<br>2: V4L2_MEMORY_USERPTR: for -vcodec libk510_h264 | 1 | 1~2 |
| Conf | Plik konfiguracyjny v4l2 | ZERO | |

Przykład polecenia ffmpeg: gdzie 10.100.232.11 jest adresem odbierającym, zmodyfikowanym zgodnie z rzeczywistą sytuacją.

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234 -f alsa -ac 2 -ar 16000 -i hw:0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -i /dev/video3 -vcodec copy -y out.yuv
```

Ilustrują:

1. Środowisko wykonawcze musi znajdować się w katalogu uruchamiania`video_sampe.conf`, `imx219_0.conf`a `imx219_1.conf`pliki są konfigurowane, a trzy pliki znajdują się w`/encode_app/` katalogu.
2. Wideo, które przychodzi w czasie rzeczywistym przez kamerę, jest zapisywane jako plik YUV, a ponieważ plik YUV jest bardzo duży, lokalna prędkość zapisu DDR lub NFS nie może nadążyć, co może spowodować spadek liczby klatek.

#### 3.2.1.6 Kodowanie JPEG

Wyjście pliku:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_jpeg -y test.mjpeg
```

Opis: Środowisko wykonawcze musi znajdować się w katalogu uruchamiania`video_sampe.conf`, `imx219_0.conf`a `imx219_1.conf`pliki są konfigurowane, a trzy pliki znajdują się w`/encode_app/` katalogu.

Plik wyjściowy test.mjpeg można odtwarzać po stronie PC za pomocą ffplay

```shell
ffplay -i test.mjpeg
```

Strumień push:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_jpeg -an -f rtp rtp://10.100.232.11:1234
```

Dostępne są strumienie ffplay pull

#### 3.2.1.7 Kodowanie multipleksowania

Obsługa do 8 jednoczesnego kodowania, możesz użyć rozmiaru klatki każdego kanału pomnożonego przez liczbę klatek na sekundę, a następnie dodanego, nie przekraczaj ilości danych 1080p60, -vcodec może wybrać h264 lub jpeg.

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -filter_complex 'split=2[out1][out2]' -map '[out1]' -vcodec libk510_h264 -ch 0 -an -f rtp rtp://10.20.1.101:1234 -map '[out2]' -vcodec libk510_h264 -ch 1 -an -f rtp rtp://10.20.1.101:2236
```

```shell
ffmpeg -f v4l2 -s 480x360 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -filter_complex 'split=8[out1][out2][out3][out4][out5][out6][out7][out8]' -map '[out1]' -vcodec libk510_h264 -b:v 300000 -ch 0 -an -f rtp rtp://10.20.1.101:1234 -map '[out2]' -vcodec libk510_h264 -b:v 300000 -ch 1 -an -f rtp rtp://10.20.1.101:2322 -map '[out3]' -vcodec libk510_h264 -b:v 300000 -ch 2 -an -f rtp rtp://10.20.1.101:3086 -map '[out4]' -vcodec libk510_h264 -b:v 300000 -ch 3 -an -f rtp rtp://10.20.1.101:4234 -map '[out5]' -vcodec libk510_h264 -b:v 300000 -ch 4 -an -f rtp rtp://10.20.1.101:5216 -map '[out6]' -vcodec libk510_h264 -b:v 300000 -ch 5 -an -f rtp rtp://10.20.1.101:6788 -map '[out7]' -vcodec libk510_h264 -b:v 300000 -ch 6 -an -f rtp rtp://10.20.1.101:7230 -map '[out8]' -vcodec libk510_h264 -b:v 300000 -ch 7 -an -f rtp rtp://10.20.1.101:8976
```

Podczas korzystania z ffplay do ściągania strumieni, uważaj, aby pobrać tylko jeden film, przełącz wideo z innych dróg, zmieniając numer portu w pliku SDP lub uruchom wiele strumieni ffplay.

### 3.2.2 Instrukcje przenoszenia programu

`ffmpeg``ffmpeg`Przeniesiony na wersję open source 4.4,`xxx.patch` dodany do dodatku Service Pack

- `ff_libk510_h264_encoder`: Sterowanie kodowaniem sprzętowym h264, odniesienie`libvenc.so`
- `ff_libk510_jpeg_encoder`: Steruje kodowaniem sprzętowym jpeg, do którego się odwołuje`libvenc.so`
- v4l2: W wersji v4l2.c dodano kod sprzętowy k510, a typ bufora v4l2 V4L2_MEMORY_USERPTR i odwoływał się do niego`libmediactl.so`.

#### 3.2.2.1 polecenie generowania poprawek

（1）

```shell
quilt new -p ab xxx.patch #在patches目录下生成xxx.patch文件
quilt add <filename> #添加修改前的文件
### 修改代码 ###
quilt refresh #修改内容被添加到xxx.patch
```

（2）
Skopiuj xxx.patch do katalogu package/ffmpeg_canaan i zmodyfikuj ścieżkę pliku w pliku poprawki zgodnie z bieżącą ścieżką.

```shell
mv ../../patches/xxx.patch ../../package/ffmpeg_canaan
rm ../../patches/series
sed -i "s/\/dl\/ffmpeg_canaan\/ffmpeg-4.4//g" ../../package/ffmpeg_canaan/xxx.patch
```

#### 3.2.2.2 Konfiguracja ffmpeg

W `package/ffmpeg_canaan/ffmpeg.mk`pliku można zmodyfikować rdzeń procesora, łańcuch narzędzi kompilacji i włączyć za pomocą opcji`ff_k510_video_demuxer` konfiguracji.`ff_libk510_jpeg_encoder` `ff_libk510_h264_encoder`

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

**Zrzeczenie się odpowiedzialności za**tłumaczenie  
Dla wygody klientów Canaan używa tłumacza AI do tłumaczenia tekstu na wiele języków, które mogą zawierać błędy. Nie gwarantujemy dokładności, rzetelności ani terminowości dostarczonych tłumaczeń. Canaan nie ponosi odpowiedzialności za jakiekolwiek straty lub szkody spowodowane poleganiem na dokładności lub wiarygodności przetłumaczonych informacji. W przypadku różnic w treści tłumaczeń w różnych językach, pierwszeństwo ma chińska wersja uproszczona.

Jeśli chcesz zgłosić błąd lub niedokładność tłumaczenia, skontaktuj się z nami pocztą.
