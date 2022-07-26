![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 멀티미디어 개발 가이드</font>**

<font face="黑体"  size=3>문서 버전: V1.0.0</font>

<font face="黑体"  size=3>게시 날짜: 2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**면책 조항**</font>
귀하가 구매한 제품, 서비스 또는 기능은 베이징 Jiananges 정보 기술 유한 회사(이하 "회사")의 상업 계약 및 약관의 적용을 받으며, 이 문서에 설명된 제품, 서비스 또는 기능의 전부 또는 일부는 구매 또는 사용의 범위를 벗어납니다. 계약에 달리 합의하지 않는 한, 회사는 본 문서의 진술, 정보, 내용의 정확성, 신뢰성, 완전성, 마케팅, 특정 목적 및 비침략성에 대해 명시적 또는 묵시적으로 어떠한 진술이나 보증도 하지 않습니다. 달리 합의하지 않는 한, 이 문서는 사용 지침의 참조로만 사용됩니다.
이 문서의 내용은 제품 버전 업그레이드 또는 기타 이유로 인해 예고 없이 수시로 업데이트되거나 수정될 수 있습니다.

**<font face="黑体"  size=3>상표 고지</font>**

베이징 <img src="../zh/images/canaan-logo.png" style="zoom:33%;" />Jianan Jets 정보 기술 유한 공사의 상표는 Jianan, Jianan 및 Jianan의 다른 상표입니다. 이 문서에 언급될 수 있는 기타 모든 상표 또는 등록 상표는 해당 소유자가 소유합니다.

**<font face="黑体"  size=3>저작권 ©2022 베이징 Jiananjets 정보 기술 유한 회사</font>**
이 문서는 K510 플랫폼 개발 및 설계에만 적용되며, 어떠한 단위나 개인도 회사의 서면 허가 없이 이 문서의 일부 또는 전부를 어떤 형태로든 배포할 수 없습니다.

**<font face="黑体"  size=3>베이징 Jiananjets 정보 기술 유한 회사</font>**
웹 사이트: canaan-creative.com
비즈니스 문의: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# 서문
## 문서의 목적
이 문서는 K510 Multimedia 앱 인스턴스에 대한 설명서입니다.
## 대상 독자
이 문서는 다음을 위한 것입니다.
- 소프트웨어 개발자
- 기술 지원 담당자

## 레코드를 수정합니다

| 버전 번호입니다    | 수정자 | 개정일입니다| 개정 지침  |  
|  ------  |-------| -------| ------ |
| v1.0.0 버전    |시스템 소프트웨어 그룹입니다 | 2022-03-09 | SDK V1.5 릴리스 |
|     |     |      |   |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>카탈로그</font>**

[목차]

# 인코더 API 1개

## 1.1 헤더 파일에 대한 설명입니다

k510_buildroot/패키지/encode_app/enc_interface.h

## 1.2 API 함수 설명입니다

### 1.2.1 VideoEncoder_Create

[설명]

비디오 인코더를 만듭니다

【문법】

```c
EncoderHandle* VIdeoEncoder_Create(EncSettings *pCfg)
```

[매개변수]

pCfg: 인코딩 구성 매개 변수를 입력합니다

|            매개 변수 이름입니다             | 매개 변수 설명입니다                                                     |                           값 범위입니다                           | 코딩 모듈에 적합합니다 |
| :---------------------------: | :----------------------------------------------------------- | :----------------------------------------------------------: | ------------ |
|            채널            | 최대 8개의 인코딩 채널을 지원하는 채널 번호입니다                                   |                            [0，7]                            | jpeg、avc    |
|             너비             | 인코딩된 이미지의 너비입니다                                                 | avc[128,2048]: , 8 <br/> jpeg의 배수: 최대 8192, 16의 배수 | jpeg、avc    |
|            높이             | 인코딩된 이미지 높이입니다                                                 | avc[64,2048]: , 8 <br/> jpeg의 배수: 최대 8192, 2의 배수 | jpeg、avc    |
|           프레임 속도           | 프레임 속도는 몇 가지 값을 고정하도록 구성할 수 있습니다                                    |                       (25,30,50,60,75)                       | jpeg、avc    |
|            rcMode             | 비트 전송률 제어 모드 0:CONST_QP 1:CBR 2:VBR<br />jpeg는 CONST_QP 고정됩니다|                       RateCtrlMode를 참조하십시오                       | jpeg, avc    |
|            비트 전송률            | CBR 모드의 대상 비트 전송률 또는 VBR 모드에서 가장 낮은 비트 전송률입니다                    |                        [10,20000000]                         | 획          |
|          최대 비트 레이트           | VBR 모드에서 가장 높은 비트 전송률입니다                                          |                        [10,20000000]                         | 획          |
|            슬라이스QP            | 초기 QP 값, -1은 auto를 나타냅니다                                        | avc : -1, jpeg :[0,51]<br/>[1,100]                | jpeg, avc    |
|             최소 QP             | 최소 qp 값입니다                                                     |                         [0,슬라이스qp]                          | 획          |
|             최대 QP             | 최대 qp 값입니다                                                     |                         [슬라이스qp,54]                         | 획          |
|            윤곽            | SPS의 profile_idc 매개 변수: 0: base 1:main 2:high 3:jpeg       |                            [0,3]                             | jpeg, avc    |
|             수준             | PS의 level_idc 매개 변수입니다                                       |                           [10,42]                            | 획          |
|          종횡비          | 축척을 표시합니다                                                     |                     AVC_AspectRatio 참조하십시오                      | jpeg, avc    |
|            FreqIDR            | 두 IDR 프레임 사이의 간격입니다                                              |                           [1,1000]                           | 획          |
|            고프렌             | Group Of Picture, 즉 두 I-프레임 사이의 간격입니다                      |                           [1,1000]                           | 획          |
|          bEnableGDR           | 인트라 프레임 새로 고침을 사용할지 여부입니다                                             |                         [참, 거짓]                         | 획          |
|            gdrMode            | gdr 새로 고침 모드: 0, 수직 새로 고침 1, 가로 새로 고침                        |                       GDRCtrlMode를 참조하십시오                        | 획          |
|          bEnableLTR           | 장기 참조 프레임을 사용할지 여부입니다                                           |                         [참, 거짓]                         | 획          |
|          로이Ctrl 모드          | roi 제어 모드 : 0 : roi 1을 사용하지 마십시오 : 상대 qp 2 : 절대 qp                 |                       ROICtrlMode를 참조하십시오                        | 획          |
|       EncSliceSplitCfg        | 슬라이스 분할 배포                                               |                                                              | 획          |
|         bSplitEnable          | 슬리스 분할이 가능한지 여부입니다                                           |                         [참, 거짓]                         | 획          |
|         u32분할 모드          | 슬리스 분할 모드: 0: 비트 수로 분할합니다. <br />1: 매크로 블록 행으로 분할합니다|                            [0,1]                             | 획          |
|         u32슬라이스 크기          | u32SplitMode=0은 각 slice에 대한 byte <br />u32SplitMode=1을 나타내며 각 slice가 차지하는 매크로 블록 행 수를 나타냅니다<br /> | u32 분할 모드 = [100,65535]<br />0,u32 분할 모드 = 1,[1, (이미지 높이 +15) / 16] | 획          |
|          엔트로피모드          | 엔트로피 코드, 0: CABAC 1:CAVLC                                |                      EncEntropyMode를 참조하십시오                      | 획          |
|          encDblkCfg           | 청크 필터링 구성입니다                                                 |                                                              | 획          |
| disable_deblocking_filter_idc | 기본값 0은 H.264 협의를 참조하십시오                          |                            [0，2]                            | 획          |
|  slice_alpha_c0_offset_div2   | 기본값 0은 H.264 협의를 참조하십시오                          |                           [-6，6]                            | 획          |
|    slice_beta_offset_div2     | 기본값 0은 H.264 협의를 참조하십시오                          |                          [-6,   6]                           | 획          |

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

[반환 값]

```c
typedef void* EncoderHandle
```

### 1.2.2 VideoEncoder_SetRoiCfg

[설명]

최대 8개의 직사각형 영역을 지원하는 roi 설정은 시스템 내에서 0~7개의 인덱스 번호로 ROI 영역을 관리하고 uIndex는 사용자가 ROI의 인덱스 번호를 설정하도록 나타냅니다. ROI 영역은 서로 중첩될 수 있으며 오버레이가 발생할 때 인덱스 번호 0~7에 따라 ROI 영역 간의 우선 순위가 증가합니다.

인코더를 만든 후 소멸될 때까지 사용할 수 있습니다. 인코딩 프로세스 중에 roi 영역을 동적으로 조정할 수 있습니다.

【문법】

```c
EncStatus VideoEncoder_SetRoiCfg(EncoderHandle *hEnc,const EncROICfg*pEncRoiCfg);
```

[매개변수]

hEnc: 만들 때 반환되는 핸들입니다

pEncRoiCfg:roi 영역 구성 정보

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

매개 변수 설명입니다

```text
uIndex     - 指定该roi区域索引号，范围0-7最多支持8个区域
bEnable    - 指定该区域是否使能，只有使能的区域才有效
uQpValue   - qp值，可以是相对qp或绝对qp，qp模式由EncSettings中roiCtrlMode属性决定。绝对qp范围                  [0,51]，相对qp范围[-31,31]
stRect     - roi矩形区域，s32X矩形左上角x值，s32Y矩形左上角y值，u32Width矩形宽度，u32Height矩形高度
```

[반환 값]

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.3 VideoEncoder_SetLongTerm

[설명]

인코딩된 다음 프레임을 장기 참조 프레임으로 설정합니다. 인코더를 만든 후 소멸될 때까지 사용할 수 있습니다. EncSettings의 bEnableLTR 속성은 기능이 활성화되는지 여부를 결정합니다.

【문법】

```c
EncStatus VideoEncoder_SetLongTerm(EncoderHandle *hEnc);
```

[매개변수]

hEnc: 만들 때 반환되는 핸들입니다

[반환 값]

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.4 VideoEncoder_UseLongTerm

[설명]

인코딩된 다음 프레임은 장기 참조 프레임을 사용하도록 설정됩니다. 인코더를 만든 후 소멸될 때까지 사용할 수 있습니다. EncSettings의 bEnableLTR 속성은 기능이 활성화되는지 여부를 결정합니다.

【문법】

```c
EncStatus VideoEncoder_UseLongTerm(EncoderHandle *hEnc);
```

[매개변수]

hEnc: 만들 때 반환되는 핸들입니다

[반환 값]

```c
typedef enum
{
    Enc_SUCCESS = 0,
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.5 VideoEncoder_InsertUserData

[설명]

사용자 데이터를 삽입합니다.

인코더를 만든 후 소멸하기 전에 사용할 수 있으며 인코딩 프로세스 중에 사용자 데이터의 내용을 실시간으로 수정할 수 있습니다. 사용자 데이터는 IDR 프레임의 SEI 데이터 영역에 삽입됩니다.

【문법】

```c
EncStatus      VideoEncoder_InsertUserData(EncoderHandle *hEnc,char*pUserData,unsigned int nlen);
```

[매개변수]

hEnc: 만들 때 반환되는 핸들입니다

pUserData: 사용자 데이터 포인터입니다

nlen: 사용자 데이터 길이(0, 1024]

[반환 값]

```c
typedef enum
{
    Enc_SUCCESS = 0,
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.6 VideoEncoder_Destory

[설명]

비디오 인코더를 제거합니다

【문법】

```c
EncStatus VideoEncoder_Destroy(EncoderHandle *hEnc)
```

[매개변수]

hEnc: 만들 때 반환되는 핸들입니다

[반환 값]

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.7 VideoEncoder_EncodeOneFrame

[설명]

비디오 프레임을 인코딩합니다

【문법】

```c
EncStatus VideoEncoder_EncodeOneFrame(EncoderHandle *hEnc, EncInputFrame *input)
```

[매개변수]

hEnc: 만들 때 반환되는 핸들입니다

input: YUV 비디오 데이터를 입력합니다

```c
typedef struct
{
    unsigned short width;
    unsigned short height;
    unsigned short stride;
    unsigned char *data;
}EncInputFrame;
```

[반환 값]

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.2.8 VideoEncoder_GetStream

[설명]

비디오 인코딩 스트림의 버퍼를 가져옵니다. 참고: 버퍼 공간은 인코더에 의해 내부적으로 할당됩니다.

【문법】

```c
EncStatus VideoEncoder_GetStream(EncoderHandle *hEnc, EncOutputStream *output)
```

[매개변수]

hEnc: 만들 때 반환되는 핸들입니다

output: 인코딩된 스트림 데이터를 출력한 buffer, bufSize가 0보다 큰 경우에만 출력이 있습니다

```c
typedef struct
{
    unsigned char *bufAddr;
    unsigned int bufSize; 
}EncOutputStream;
```

[반환 값]

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.2.9 VideoEncoder_GetStream_ByExtBuf

[설명]

비디오 인코딩 스트림의 버퍼를 가져옵니다. 참고: 이 버퍼 공간은 소비자가 이 함수를 호출하기 전에 할당해야 합니다.

【문법】

```c
EncStatus VideoEncoder_GetStream(EncoderHandle *hEnc, EncOutputStream *output)
```

[매개변수]

hEnc: 만들 때 반환되는 핸들입니다

output: 인코딩된 스트림 데이터를 출력한 buffer, bufSize가 0보다 큰 경우에만 출력이 있습니다

```c
typedef struct
{
    unsigned char *bufAddr;
    unsigned int bufSize; 
}EncOutputStream;
```

[반환 값]

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.3.0 VideoEncoder_ReleaseStream

[설명]

비디오 인코딩 스트림을 해제하는 버퍼입니다

【문법】

```c
EncStatus VideoEncoder_ReleaseStream(EncoderHandle *hEnc, EncOutputStream *output)
```

[매개변수]

- hEnc: 만들 때 반환되는 핸들입니다
- output: 반환된 버퍼를 VideoEncoder_GetStream

[반환 값]

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

# 2 하드웨어 구조 다이어그램 및 소프트웨어 아키텍처

# 2.1 하드웨어 구조도

K510의 하드웨어 블록 다이어그램은 다음과 같습니다.
![hardware_block_diagram](../zh/images/multimedia_guides/hardware_block_diagram.png)

비디오 센서로부터 수신된 데이터는 MIPI DPHY, CSI, VI, ISP 처리하여 유브 소스 데이터를 얻어 DDR에 저장합니다. h264 encoder 모듈은 DDR에서 데이터를 읽고 코딩하며 결과는 DDR에 저장됩니다.

# 2.2 소프트웨어 아키텍처

멀티미디어 개발 플랫폼의 소프트웨어 아키텍처는 다음과 같습니다.

![multimedia_block_diagram.png](../zh/images/multimedia_guides/multimedia_block_diagram.png)

그 중,

- `libvenc`: h264 encoder core를 호출하는 encoder 라이브러리입니다
- `libmediactl`: isp 라이브러리, sensor를 제어합니다
- `libaudio3a`: 오디오에 대한 3a 연산을 위한 audio3a 라이브러리
- `alsa-lib`: 오디오 인터페이스를 제어하는 오디오 라이브러리입니다

# 3 Demo 앱

## 3.1 응용 프로그램 인코딩

프로그램은 디렉토리에 배치됩니다`/app/encode_app`:

- `encode_app`:Encode application 프로그램입니다
- 테스트용 유브 파일 크기는 크고 SDK팩에 넣지 않았다

실행합니다`encode_app`

| 매개 변수 이름입니다 | 매개 변수 설명입니다 | 기본값입니다 | 값 범위입니다 | 코딩 모듈에 적합합니다 |
|:-|:-|:-|:-|:-|
| 도움말 | 도움말 정보입니다| | ||
| 쪼개다 | 채널 수입니다 | 영 | [1,4] | jpeg、avc |
| 채널 | 채널 번호(0부터 시작) | 영 | [0,3] | jpeg、avc |
| 나는 |nv12 **형식** 만 지원하는 yuv 파일을 입력합니다| 영 | v4l2 <br> xxx.yuv | jpeg、avc |
| 개발 | v4l2 장치 이름 | 영 | **센서0:** /dev/video3 /dev/video4 <br> <br>sensor1:<br> **/dev/video7 /  dev/** video8 <br> <br> | 획 |
| 또는 | 출력| 영 | rtsp <br> xxx.264 <br> xxx.MJPEG <br> xxx.JPEG | jpeg、avc |
| 안으로 | 출력 이미지 너비입니다 | 1920 | avc[128,2048]: , 8 <br> jpeg의 배수: 최대 8192, 16의 배수 | jpeg、avc |
| h | 출력 이미지 높이입니다 | 1080 | avc[64,2048]: , 8 <br> jpeg의 배수: 최대 8192, 2의 배수 | jpeg、avc |
| fps | 카메라 캡처 프레임 속도는 현재 30pfs만 지원합니다 | 30 | 30 | 획 |
| r | 인코딩된 출력 프레임 속도입니다 | 30 | fps 또는 fps로 나눌 수 있는 숫자입니다 | 획 |
| 인프레임 | 유브 프레임 수를 입력합니다 | 0 | [0,50] | jpeg、avc |
| 아웃프레임 | yuv 프레임 수를 출력하고 매개 변수-inframes보다 크면 인코딩이 반복됩니다 | 0 | [0,32767] | jpeg、avc |
| 공화당 | Group Of Picture, 즉 두 I-프레임 사이의 간격입니다 | 25 | [1,1000] | 획 |
| rcmode | 비트 전송률 제어 모드 0:CONST_QP 1:CBR 2:VBR을 나타냅니다 | 증권 시세 표시기 | [0,2] | 획 |
| 비트 전송률 | CBR 모드의 대상 비트 전송률 또는 VBR 모드에서 가장 낮은 비트 전송률(Kb 단위)입니다 | 4000 | [1,20000] | 획 |
| 최대 비트 전송률 | VBR 모드에서 가장 높은 비트 전송률(Kb)입니다 | 4000 | [1,20000] | 획 |
| 윤곽 | SPS의 profile_idc 매개 변수: 0: base 1:main 2:high 3:jpeg | AVC_HIGH | [0,3] | jpeg、avc |
| 수준 | SPS의 level_idc 매개 변수입니다 | 42 | [10,42] | 획 |
| 슬라이스qp | 초기 QP 값, -1은 auto를 나타냅니다 | 25 | avc : -1, jpeg :[0,51]<br/>[1,100] | jpeg、avc |
| 민크프 | 최소 QP 값입니다 | 0 | [0,슬라이스qp] | 획 |
| 최대 qp | 최대 QP 값입니다 | 54 | [슬라이스qp,54] | 획 |
| 인에이블LTR | 장기 참조 프레임을 가능하게 하는 매개변수는 새로 고침 주기를 지정합니다. 0: 새로 고침 주기를 사용할 수 없습니다. 양수: 주기적으로 참조 프레임을 설정하고 다음 프레임은 장기 참조 프레임을 사용하도록 설정됩니다 | 0 | [0,65535] | 획 |
| 왕 | 여러 roi 영역을 지정하는 roi 프로필입니다 | 영 | xxx.conf | 획 |
| ᄀ | AE를 가능하게 합니다 | 0 | 0-인에이화 AE<br>1-인에이지 AE | |
| conf | vl42 구성 파일은 명령줄 입력 매개 변수에 따라 v4l2 구성 매개 변수를 수정하여 구성 파일을 지정합니다 | 영 | xxx.conf | 획 |

### 3.1.1 yuv 파일을 입력하고 파일을 출력합니다

```shell
./encode_app -split 1 -ch 0 -i your_file.yuv -o out.264 -w 1920 -h 1080 -inframes 10 -outframes 30
./encode_app -split 1 -ch 0 -i your_file.yuv -o out.mjpeg -w 1920 -h 1080 -inframes 10 -outframes 30
```

### 3.1.2 입력 v4l2, 출력 rtsp 푸시 스트림

#### 3.1.2.1 단일 채널

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

ffplay 끌어서 흘리기 명령의 예:

```shell
 ffplay -rtsp_transport tcp rtsp://192.168.137.11:8554/testStream
```

- `rtsp://192.168.137.11:8554/testStream`rtsp 스트림 URL 주소 , -rtsp_transport tcp는 tcp를 사용하여 오디오 및 비디오 데이터를 전송하는 것을 의미하며(기본적으로 udp를 사용), -fflags nobuffer 옵션을 추가하여 플레이어 캐시로 인한 지연 증가를 방지합니다.

#### 3.1.2.2 단일 카메라 듀얼 채널

```shell
./encode_app -split 2 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -ch 1 -i v4l2 -dev /dev/video4 -o rtsp -w 1280 -h 720 -conf video_sample.conf
```

ffplay 끌어 흐름 명령이 위와 동일합니다.

#### 3.1.2.3 듀얼 카메라

```shell
./encode_app -split 2 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -ch 1 -i v4l2 -dev /dev/video7 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

ffplay 끌어 흐름 명령이 위와 동일합니다.

#### 3.1.2.4 roi 테스트

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -sliceqp -1 -bitrate 2048 -roi roi_1920x1080.conf -conf video_sample.conf
```

roi 파일 형식입니다

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

매개 변수 설명:

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

ffplay 끌어 흐름 명령이 위와 동일합니다.

### 3.1.3 프레임 속도 변환

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -r 60 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

ffplay 끌어 흐름 명령이 위와 동일합니다.

### 3.1.4 다양한 입력 프레임 속도

현재 VGA@75fps 및 720p60이 지원됩니다

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 640 -h 480 -fps 75 -r 75 -conf video_sample_vga480p75.conf
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1280 -h 720 -fps 60 -r 60 -conf video_sample_720p60.conf
```

ffplay 끌어 흐름 명령이 위와 동일합니다.

### 3.1.5 rtsp는 오디오 및 비디오 스트림을 푸시합니다

```c
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -alsa 1 -ac 2 -ar 44100 -af 2 -ad hw:0 -conf video_sample.conf
```

ffplay 끌어 흐름 명령이 위와 동일합니다.

### 3.1.6 주의 사항

- 운영 환경: 코어 보드 sensor: IMX219_SENSOR

- rtsp 스트림 주소 형식: rtsp://ip 주소: ip 주소 및 포트 번호가 가변적이고 나머지가 고정된 포트 번호/testStream입니다.

  rtsp://192.168.137.11:8554/testStream ip 주소는 192.168.137.11이고 포트 번호는 8554입니다.

  ip 주소: 보드의 IP 주소이며 보드에 ifconfig를 입력하여 얻을 수 있습니다.

  포트 번호: 8554 + <通道号>*2, 채널 번호는 일반적으로 0(-ch 0, -ch 1...)부터 시작합니다.

- rtsp 스트림 재생 방법: 해당 rtsp 스트림은 vlc 또는 ffplay를 통해 재생할 수 있으며, 스트림은 udp 또는 tcp 프로토콜을 통해 전송될 수 있습니다.

  1) rtp over udp播放:ffplay -rtsp_transport udp rtsp://192.168.137.11:8554/testStream

  2) rtp over tcp 播放: ffplay -rtsp_transport tcp rtsp://192.168.137.11:8554/testStream

  udp 패킷 손실로 인한 화면 손실을 방지하기 위해 rtp over tcp를 사용하여 재생하는 것이 좋습니다.

## 3.2 ffmpeg

ffmpeg는 /usr/local/bin 디렉토리에 배치됩니다.

- `ffmpeg`: ffmpeg 응용 프로그램.

실행합니다`ffmpeg`

(1) encoder libk510_h264 매개 변수입니다
| 매개 변수 이름입니다 | 매개 변수 설명입니다 | 기본값입니다 | 값 범위입니다 |
|:-|:-|:-|:-|
| g | GOP 크기 | 25 | 1~1000명 |
| b | 비트 전송률 | 4000000 | 0~20000000 |
| r | isp는 현재 30fps만 지원하므로 디코더를 30으로 설정해야 합니다 | 30 | 30 |
| idr_freq | IDR 주파수입니다 | -1(IDR 없음) | -1~256 |
| 증권 시세 표시기 | cqp로 인코딩할 때 qp 값을 구성합니다 | -1 (자동) | -1~100 |
| 최대 속도 | bitrate의 최대값입니다 | 0 | 20000000 |
| 윤곽 | 지원되는 profile입니다 | 2(높음) | 0 - 기준선 <br> 1 - 주 <br> 2 - 높음 |
| 수준 | 코드 레벨 | 42 | 10~42명 |
| 할 텐데 | 화면 종횡비입니다 | 0 (자동) | 0 - 자동  1 - 4:3 <br> 2 - 16:9 <br> 3 - 없음 <br> |
| 채널 | 채널 번호 | 0 | 0-7 |
| 프레임토인코딩 | 인코딩된 프레임 수입니다 | -1(모든 프레임) | -1~16383 |

(2) encoder libk510_jpeg 매개 변수입니다
| 매개 변수 이름입니다 | 매개 변수 설명입니다 | 기본값입니다 | 값 범위입니다 |
|:-|:-|:-|:-|
| 증권 시세 표시기 | cqp로 인코딩할 때 qp 값을 구성합니다 | 25 | -1~100 |
| r | 프레임 속도 | 30 | 25~60세 |
| 채널 | 채널 인코딩 | 0 | 0~7명 |
| 최대 속도 | 최대 비트 전송률. (0=무시) | 4000000 | 0~20000000 |
| 할 텐데 | 종횡비 | 0 (자동) | 0 - 자동  1 - 4:3 <br> 2 - 16:9 <br> 3 - 없음 <br> |

(3) device libk510_video 매개 변수입니다
| 매개 변수 이름입니다 | 매개 변수 설명입니다 | 기본값입니다 | 값 범위입니다 |
|:-|:-|:-|:-|
| 어 | 프레임 크기 | 영 | **인코더의 경우 libk510_h264:: 최대 2048x2048 폭** 8 <br> 높이  8 분의 배수: 128 분. 높이: <br>인코더 libk510_jpeg의 경우<br> 64 <br> <br>:<br> 최대 8192x8192 **폭 16** 높이 배수 2 <br> <br> <br> |
| 특급 | 노출 매개 변수 | 0 | 0~128명 |
| agc | 아날로그 게인 | 0 | 0~232명 |

(4) audio3a 매개 변수
| 매개 변수 이름입니다 | 매개 변수 설명입니다 | 기본값입니다 | 값 범위입니다 |
|:-|:-|:-|:-|
| sample_rate | 오디오 샘플 속도입니다 | 16000 | 1~65535 |
| agc | 오디오 게인 모드입니다 | 3(AgcModeFixedDigital) | 0 - AgcModeUnchanged  1 - AgcModeAdaptiveAnalog 2 - AgcModeAdaptiveDigital <br> 3 - AgcModeFixedDigital <br> <br> |
| ns | 노이즈 레벨 | 3 (매우 높음) | 0 - 낮 <br> 음  1 - 보통  2 - 높음 <br> 3 - 매우 높음 <br> |
| dsp_task | auido3a 실행 위치입니다 | 1(dsp) | 0 - CPU <br>1 - dsp |

구성 가능한 매개 변수는 도움말 명령을 통해 볼 수 있습니다

```shell
ffmpeg -h encoder=libk510_h264 #查看k510编码器的参数
ffmpeg -h demuxer=v4l2 #查看demuxer的配置参数
ffmpeg -h filter=audio3a #查看audio3a的配置参数
```

ffmpeg의 논리 상자는 다음과 같습니다.

![ffmpeg_block_diagram](../zh/images/multimedia_guides/ffmpeg_block_diagram.png)

audio3a는 수신된 오디오를 3a 연산하고 출력하는 데 사용되며 논리 블록 다이어그램은 다음과 같습니다.

![ffmpeg_canaan_audio3a](../zh/images/multimedia_guides/ffmpeg_canaan_audio3a.png)

### 3.2.1 프로그램 실행 지침

#### 3.2.1.1 rtp 푸시 스트림

##### 3.2.1.1.1. rtp는 비디오 스트림을 푸시합니다

ffmpeg 실행 명령의 예:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.102.231.29:1234
```

이 중 10.102.231.29는 실제 변경에 따라 수신 측 주소입니다.
프로그램 실행 중에 "q"를 눌러 실행을 중지합니다.

ffplay 수신 명령:

```shell
ffplay.exe -protocol_whitelist "file,udp,rtp" -i test.sdp -fflags nobuffer -analyzeduration 1000000 -flags low_delay
```

여기서 test.sdp는 다음 예제에 따라 구성됩니다.

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

.sdp 매개 변수 설명:

- c=: 미디어 링크 정보; IN: 네트워크 유형; IP4: 주소 유형; IP 주소 뒤에는 (수신자가 있는 IP 주소가 발신자의 IP가 아님)
- m=미디어 수준 세션의 시작, 비디오: 미디어 유형; 1234: 포트 번호; RTP/AVP: 전송 프로토콜; 96:rtp 헤더의 payload 형식입니다
실제 상황에 따라 수신 측 IP 주소 및 포트 번호를 수정하고 rtp의 포트 번호는 짝수이어야 합니다.

##### 3.2.1.1.2. rtp는 오디오 스트림을 푸시합니다

ffmpeg 실행 명령의 예:

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f rtp rtp://10.100.232.11:1234
```

이 중 10.100.232.11은 실제 수정에 따라 수신 측 주소입니다.

- ac: 오디오 채널 수를 설정합니다
- ar: 오디오 샘플 속도를 설정합니다

ffplay 수신 명령은 비디오 스트림 수신과 동일하며 sdp 파일은 다음 예제를 참조합니다.

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

##### 3.2.1.1.3 rtp는 오디오 및 비디오 스트림을 푸시합니다

ffmpeg 실행 명령의 예:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234 -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

ffplay 수신 명령은 오디오 스트림을 수신하는 것과 동일하며 sdp 파일은 다음 예제를 참조합니다.

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

#### 3.2.1.2 rtsp 푸시 스트림

rtsp는 스트림을 푸시하기 전에 rtsp 서버를 배포하여 서버에 데이터 흐름을 푸시해야 합니다.

##### 3.2.1.2.1 rtsp 푸시 비디오 스트림

ffmpeg 실행 명령의 예:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -acodec copy -f rtsp rtsp://10.100.232.11:5544/live/test110
```

- `idr_freq`IDR 프레임 간격의 경우 GOP의 정수 배수여야 합니다. 스트림으로 끌어오려면 rtsp 푸시 스트림이 IDR 프레임을 생성해야 합니다.
- `rtsp://10.100.232.11:5544/live/test110`rtsp 서버의 밀기 및 당기기 흐름 URL 주소입니다

ffplay 끌어서 흘리기 명령의 예:

```shell
ffplay.exe -protocol_whitelist "file,udp,rtp,tcp" -i rtsp://10.100.232.11:5544/live/test110
```

##### 3.2.1.2.2 rtsp 푸시 오디오 스트림

ffmpeg 실행 명령의 예:

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f rtsp rtsp://10.100.232.11:5544/live/test110
```

ffplay 끌어오기 명령은 rtsp 끌어오기 비디오 스트림의 명령과 동일합니다.

##### 3.2.1.2.3 rtsp 푸시 톤 비디오 스트림

ffmpeg 실행 명령의 예:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -f alsa -ac 2 -ar 32000 -i hw:0 -idr_freq 25 -vcodec libk510_h264 -acodec aac -f rtsp rtsp://10.100.232.11:5544/live/test110
```

ffplay 끌어오기 명령은 rtsp 끌어오기 비디오 스트림의 명령과 동일합니다.

#### 3.2.1.3 rtmp 푸시 스트림

rtmp를 푸시하기 전에 rtmp 서버를 배포하여 서버에 데이터 흐름을 푸시해야 합니다. rtmp 프로토콜을 지원하는 서버에는 fms, nginx, srs 등이 포함됩니다.

##### 3.2.1.3.1 rtmp 푸시 비디오 스트림

ffmpeg 실행 명령의 예:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`rtmp 서버로 흐름을 푸시하는 URL 주소입니다  

ffplay 끌어서 흘리기 명령의 예:

```shell
ffplay -fflags nobuffer rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`rtmp 서버에서 스트림의 URL 주소를 당기기 위해 (푸시 스트림은 끌어오기 스트림의 주소와 동일) -fflags nobuffer 옵션은 플레이어 캐시로 인한 지연 증가를 방지합니다.

##### 3.2.1.3.2 rtmp 푸시 오디오 스트림

ffmpeg 실행 명령의 예:

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`rtmp 서버로 흐름을 푸시하는 URL 주소입니다

ffplay 끌어오기 명령은 rtmp 끌어오기 비디오 스트림의 명령과 동일합니다.

##### 3.2.1.3.3 rtmp 푸시 톤 비디오 스트림

ffmpeg 실행 명령의 예:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -f alsa -ac 2 -ar 32000 -i hw:0 -idr_freq 25 -vcodec libk510_h264 -acodec aac -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`rtmp 서버로 흐름을 푸시하는 URL 주소입니다

ffplay 끌어오기 명령은 rtmp 끌어오기 비디오 스트림의 명령과 동일합니다.

#### 3.2.1.4 오디오3a

##### 3.2.1.4.1 audio를 별도로 실행합니다

(1) cpu에서 audio3a를 실행합니다
ffmpeg 실행 명령의 예:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000:dsp_task=0 -f rtp rtp://10.100.232.11:1234
```

(2) dsp에서 audio3a를 실행합니다
두 개의 텔넷 창을 실행하고 두 창에서 dsp task scheduler 및 fffmpeg를 실행합니다(dsp task scheduler 먼저 실행).
dsp task scheduler는 명령 인스턴스를 실행합니다.

```shell
cd /app/dsp_app_new/
./dsp_app /app/dsp_scheduler/scheduler.bin
```

ffmpeg는 명령 인스턴스를 실행합니다.

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000 -f rtp rtp://10.100.232.11:1234
```

##### 3.2.1.4.2 audio3a와 video를 동시에 실행합니다

(1) cpu에서 audio3a를 실행합니다
두 개의 텔넷 창을 실행하고 두 창에서 audio3a 및 video를 실행합니다.
비디오 명령의 예:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234
```

audio3a 명령의 예:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000:dsp_task=0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

cpu에서 audio3a와 video를 동시에 실행하면 오버플로우가 나타나 dsp에서 audio3a를 실행하는 것이 좋습니다
(2) dsp에서 audio3a를 실행합니다
3개의 텔넷 창을 실행하고 aodio3a 호출, video 및 dsp scheduler를 각각 실행합니다.dsp task scheduler를 먼저 실행합니다.
dsp task scheduler는 audio3a를 별도로 실행하는 것과 동일한 명령을 실행합니다.

audio3a 명령 인스턴스:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000 -f rtp rtp://10.100.232.11:1236
```

비디오 명령의 예:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234
```

- 10.100.232.11은 rtp 수신 측의 IP 주소입니다.
- 수신 측 ffplay의 SDP 파일 내용은 위의 ffmpeg 명령을 실행한 후 인쇄된 로그에서 얻을 수 있습니다.

#### 3.2.1.5 v4l2

구성 가능한 매개 변수는 도움말 명령을 통해 볼 수 있습니다

```shell
ffmpeg -h demuxer=v4l2 #查看v4l2的配置参数
```

| 매개 변수 이름입니다 | 매개 변수 설명입니다 | 기본값입니다 | 값 범위입니다 |
| :-- | :-- | :-- | :-- |
| s | 이미지 해상도(예: 1920x1080) | 영 | |
| r | 프레임 레이트, 현재 30fps만 지원합니다 | 30 | 30 |
| ISP | k510 isp 하드웨어를 엽니다 | 0 | 0-1 |
| buf_type | v4l2 buffer`类型` <br>1: V4L2_MEMORY_MMAP : -vcodec copy<br>2: V4L2_MEMORY_USERPTR: -vcodec libk510_h264 적합합니다| 1 | 1~2명 |
| conf | v4l2 설정 파일 | 영 | |

ffmpeg 실행 명령의 예: 여기서 10.100.232.11은 실제 수정에 따라 수신 측 주소입니다.

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234 -f alsa -ac 2 -ar 16000 -i hw:0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -i /dev/video3 -vcodec copy -y out.yuv
```

설명:

1. 런타임은 실행 디렉터리에서 파일을 찾고`video_sampe.conf``imx219_0.conf``imx219_1.conf` 구성해야 합니다`/encode_app/`.
2. 카메라가 실시간으로 들어오는 비디오는 yuv 파일로 작성되며, yuv 파일이 크기 때문에 로컬 ddr 또는 nfs가 속도를 따라갈 수 없으므로 프레임이 손실될 수 있습니다.

#### 3.2.1.6 JPEG 인코딩

파일 출력:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_jpeg -y test.mjpeg
```

설명: 런타임은 실행 디렉터리에서 파일을 찾고`video_sampe.conf``imx219_0.conf``imx219_1.conf` 구성해야 합니다`/encode_app/`.

출력 파일 test.mjpeg는 PC 측에서 ffplay로 재생할 수 있습니다

```shell
ffplay -i test.mjpeg
```

푸시 흐름:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_jpeg -an -f rtp rtp://10.100.232.11:1234
```

ffplay를 사용하여 흐름을 당깁십시오

#### 3.2.1.7 멀티플렉서 코드

최대 8개의 동시 인코딩을 지원하며, 각 프레임 크기에 프레임 속도를 곱하여 1080p60의 데이터 양을 초과하지 말고 -vcodec 옵션 h264 또는 jpeg를 사용할 수 있습니다.

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -filter_complex 'split=2[out1][out2]' -map '[out1]' -vcodec libk510_h264 -ch 0 -an -f rtp rtp://10.20.1.101:1234 -map '[out2]' -vcodec libk510_h264 -ch 1 -an -f rtp rtp://10.20.1.101:2236
```

```shell
ffmpeg -f v4l2 -s 480x360 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -filter_complex 'split=8[out1][out2][out3][out4][out5][out6][out7][out8]' -map '[out1]' -vcodec libk510_h264 -b:v 300000 -ch 0 -an -f rtp rtp://10.20.1.101:1234 -map '[out2]' -vcodec libk510_h264 -b:v 300000 -ch 1 -an -f rtp rtp://10.20.1.101:2322 -map '[out3]' -vcodec libk510_h264 -b:v 300000 -ch 2 -an -f rtp rtp://10.20.1.101:3086 -map '[out4]' -vcodec libk510_h264 -b:v 300000 -ch 3 -an -f rtp rtp://10.20.1.101:4234 -map '[out5]' -vcodec libk510_h264 -b:v 300000 -ch 4 -an -f rtp rtp://10.20.1.101:5216 -map '[out6]' -vcodec libk510_h264 -b:v 300000 -ch 5 -an -f rtp rtp://10.20.1.101:6788 -map '[out7]' -vcodec libk510_h264 -b:v 300000 -ch 6 -an -f rtp rtp://10.20.1.101:7230 -map '[out8]' -vcodec libk510_h264 -b:v 300000 -ch 7 -an -f rtp rtp://10.20.1.101:8976
```

ffplay로 스트리밍할 때 SDP 파일의 포트 번호를 변경하여 다른 경로의 비디오를 전환하거나 여러 ffplay 스트림을 시작하여 비디오를 모든 방법을 끌어당길 수 있습니다.

### 3.2.2 프로그램 마이그레이션 지침

`ffmpeg``ffmpeg`오픈 소스 코드 4.4의 버전에서 포팅,`xxx.patch` 패치 팩에 대 한 추가

- `ff_libk510_h264_encoder`: h264 하드웨어 인코딩을 제어하고 참조합니다`libvenc.so`
- `ff_libk510_jpeg_encoder`: jpeg 하드웨어 인코딩을 제어하고 참조합니다`libvenc.so`
- v4l2: v4l2.c에서 k510 하드웨어 관련 코드가 추가되어 v4l2 buffer 형식 V4L2_MEMORY_USERPTR 구현되고 참조됩니다`libmediactl.so`.

#### 3.2.2.1 patch는 명령을 생성합니다

（1）

```shell
quilt new -p ab xxx.patch #在patches目录下生成xxx.patch文件
quilt add <filename> #添加修改前的文件
### 修改代码 ###
quilt refresh #修改内容被添加到xxx.patch
```

（2）
xxx.patch를 package/ffmpeg_canaan 디렉토리에 복사하고 현재 경로에 따라 patch 파일의 파일 경로를 수정합니다.

```shell
mv ../../patches/xxx.patch ../../package/ffmpeg_canaan
rm ../../patches/series
sed -i "s/\/dl\/ffmpeg_canaan\/ffmpeg-4.4//g" ../../package/ffmpeg_canaan/xxx.patch
```

#### 3.2.2.2 ffmpeg 구성

파일에서 `package/ffmpeg_canaan/ffmpeg.mk`configure 옵션을 사용하여 CPU 코어를 수정하고 도구 체인을 컴파일하여 및 을 사용할 수 있습니다`ff_k510_video_demuxer``ff_libk510_jpeg_encoder``ff_libk510_h264_encoder`.

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

**번역 면책 조항**  
고객의 편의를 위해 Canan은 AI 번역 프로그램을 사용하여 오류를 포함할 수 있는 여러 언어로 텍스트를 번역합니다. 당사는 제공된 번역의 정확성, 신뢰성 또는 적시성을 보장하지 않습니다. Canan은 번역된 정보의 정확성이나 신뢰성에 의존하여 발생하는 손실이나 손해에 대해 책임을 지지 않습니다. 언어 번역 간에 콘텐츠 차이가 있는 경우 중국어 간체 버전이 우선합니다.

번역 오류 또는 부정확한 문제를 신고하려면 이메일로 문의하시기 바랍니다.
