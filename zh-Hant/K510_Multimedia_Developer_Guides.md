![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 多媒體開發指南</font>**

<font face="黑体"  size=3>文件版本：V1.0.0</font>

<font face="黑体"  size=3>發佈日期：2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**免責聲明**</font>
您購買的產品、服務或特性等應受北京嘉楠捷思資訊技術有限公司（“本公司”，下同）商業合同和條款的約束，本文檔中描述的全部或部分產品、服務或特性可能不在您的購買或使用範圍之內。 除非合同另有約定，本公司不對本文檔的任何陳述、資訊、內容的準確性、可靠性、完整性、行銷型、特定目的性和非侵略性提供任何明示或默示的聲明或保證。 除非另有約定，本文檔僅作為使用指導的參考。
由於產品版本升級或其他原因，本文檔內容將可能在未經任何通知的情況下，不定期進行更新或修改。 

**<font face="黑体"  size=3>商標聲明</font>**

“<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />”、“Canaan”圖示、嘉楠和嘉楠其他商標均為北京嘉楠捷思資訊技術有限公司的商標。 本文檔可能提及的其他所有商標或註冊商標，由各自的所有人擁有。 

**<font face="黑体"  size=3>版權所有©2022北京嘉楠捷思資訊技術有限公司</font>**
本文檔僅適用K510平台開發設計，非經本公司書面許可，任何單位和個人不得以任何形式對本文檔的部分或全部內容傳播。 

**<font face="黑体"  size=3>北京嘉楠捷思資訊技術有限公司</font>**
網址：canaan-creative.com
商務垂詢：salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# 前言
## 文件目的
本文檔為K510 Multimedia 應用實例的說明文檔。
## 目標讀者
本文檔面向的人員：
- 軟體開發人員
- 技術支持人員

## 修訂記錄

| 版本號    | 修改者 | 修訂日期| 修訂說明  |  
|  ------  |-------| -------| ------ |
| 1.0.0 版    |系統軟體組 | 2022-03-09 | SDK V1.5發佈 |
|     |     |      |   |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>目 錄</font>**

[目錄]

# 1 編碼器介面

## 1.1 頭文件說明

k510_buildroot/包裝/encode_app/enc_interface.h

## 1.2 API 函數說明

### 1.2.1 VideoEncoder_Create

【描述】

創建視頻編碼器

【語法】

```c
EncoderHandle* VIdeoEncoder_Create(EncSettings *pCfg)
```

【參數】

pCfg：輸入編碼配置參數

|            參數名             | 參數解釋                                                     |                           取值範圍                           | 適用編碼模組 |
| :---------------------------: | :----------------------------------------------------------- | :----------------------------------------------------------: | ------------ |
|            管道            | 通道號，最多支援8個編碼通道                                   |                            [0，7]                            | jpeg、avc    |
|             寬度             | 編碼圖像寬度                                                 | avc： [128,2048]， 8 jpeg 的倍數 <br/> ： 最多 8192， 16 的倍數 | jpeg、avc    |
|            高度             | 編碼圖像高度                                                 | avc： [64,2048]， 8 jpeg 的倍數 <br/> ： 最多 8192， 2 的倍數 | jpeg、avc    |
|           幀速率           | 幀率，只能配置為固定幾個值                                    |                       (25,30,50,60,75)                       | jpeg、avc    |
|            rcMode             | 碼率控制模式 0：CONST_QP 1：CBR 2：VBR<br />jpeg固定為CONST_QP  |                       參見RateCtrlMode                       | jpeg，avc    |
|            比特率            | CBR 模式下的目標碼率或VBR模式下的最低碼率                    |                        [10,20000000]                         | 中風          |
|          最大比特率           | VBR模式下的最高碼率                                          |                        [10,20000000]                         | 中風          |
|            SliceQP            | 初始 QP 值，-1表示auto                                        |                avc：-1，jpeg[0,51]<br/>：[1,100]                | jpeg，avc    |
|             最小QP             | 最小qp值                                                     |                         [0，切片]                          | 中風          |
|             最大QP             | 最大qp值                                                     |                         [切片qp，54]                         | 中風          |
|            輪廓            | SPS 中的 profile_idc 參數：0： base 1：main 2：high 3：jpeg       |                            [0,3]                             | jpeg，avc    |
|             水準             | PS 中的 level_idc 參數                                       |                           [10,42]                            | 中風          |
|          AspectRatio          | 顯示比例                                                     |                     參見AVC_AspectRatio                      | jpeg，avc    |
|            頻率            | 兩個idr幀的間隔                                              |                           [1,1000]                           | 中風          |
|            gopLen             | Group Of Picture，即兩個 I 幀之間的間隔                      |                           [1,1000]                           | 中風          |
|          b啟用全球戰略           | 是否啟用幀內刷新                                             |                         [真，假]                         | 中風          |
|            gdrMode            | gdr 刷新模式：0，垂直刷新 1，水準刷新                        |                       參見GDRCtrlMode                        | 中風          |
|          bEnableLTR           | 是否啟用長期參考幀                                           |                         [真，假]                         | 中風          |
|          RoiCtrlMode          | roi控制模式：0：不使用roi 1：相對qp 2：絕對qp                 |                       參見ROICtrlMode                        | 中風          |
|       EncSliceSplitCfg        | slice 分割配置                                               |                                                              | 中風          |
|         bSplitEnable          | Slice 分割是否使能                                           |                         [真，假]                         | 中風          |
|         u32拆分模式          | Slice 分割模式：0：按 bit 數分割。 <br />1：按宏塊行分割        |                            [0,1]                             | 中風          |
|         u32切片大小          | u32SplitMode=0，表示每個 slice 的 byte 數<br />u32SplitMode=1，表示每個 slice 佔的宏塊行數<br /> | u32SplitMode=0，[100,65535]<br />u32SplitMode=1，[1，（圖像高+15）/16] | 中風          |
|          熵模式          | 熵編碼，0：CABAC 1：CAVLC                                |                      參見EncEntropyMode                      | 中風          |
|          encDblkCfg           | 區塊濾波配置                                                 |                                                              | 中風          |
| disable_deblocking_filter_idc | 默認值0，具體含義請參見 H.264 協 議                          |                            [0，2]                            | 中風          |
|  slice_alpha_c0_offset_div2   | 默認值0，具體含義請參見 H.264 協 議                          |                           [-6，6]                            | 中風          |
|    slice_beta_offset_div2     | 默認值0，具體含義請參見 H.264 協 議                          |                          [-6,   6]                           | 中風          |

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

【返回值】

```c
typedef void* EncoderHandle
```

### 1.2.2 VideoEncoder_SetRoiCfg

【描述】

roi設置，最多支援8個矩形區域，系統內部按照0~7的索引號對ROI區域進行管理，uIndex 表示的使用者設置ROI的索引號。 ROI 區域之間可以互相疊加，且當發生疊加時，ROI 區域之間的優先順序按照索引號0~7 依次提高。

在編碼器創建後到銷毀前均可使用。 編碼過程中可以動態調整roi區域。

【語法】

```c
EncStatus VideoEncoder_SetRoiCfg(EncoderHandle *hEnc,const EncROICfg*pEncRoiCfg);
```

【參數】

hEnc： 建立時返回的句柄

pEncRoiCfg：roi 區域配置資訊

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

參數說明

```text
uIndex     - 指定该roi区域索引号，范围0-7最多支持8个区域
bEnable    - 指定该区域是否使能，只有使能的区域才有效
uQpValue   - qp值，可以是相对qp或绝对qp，qp模式由EncSettings中roiCtrlMode属性决定。绝对qp范围                  [0,51]，相对qp范围[-31,31]
stRect     - roi矩形区域，s32X矩形左上角x值，s32Y矩形左上角y值，u32Width矩形宽度，u32Height矩形高度
```

【返回值】

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.3 VideoEncoder_SetLongTerm

【描述】

設置編碼的下一幀為長期參考幀。 在編碼器創建後到銷毀前均可使用。 EncSettings中bEnableLTR屬性決定該功能是否使能。

【語法】

```c
EncStatus VideoEncoder_SetLongTerm(EncoderHandle *hEnc);
```

【參數】

hEnc： 建立時返回的句柄

【返回值】

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.4 VideoEncoder_UseLongTerm

【描述】

設置編碼的下一幀使用長期參考幀。 在編碼器創建後到銷毀前均可使用。 EncSettings中bEnableLTR屬性決定該功能是否使能。

【語法】

```c
EncStatus VideoEncoder_UseLongTerm(EncoderHandle *hEnc);
```

【參數】

hEnc： 建立時返回的句柄

【返回值】

```c
typedef enum
{
    Enc_SUCCESS = 0,
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.5 VideoEncoder_InsertUserData

【描述】

插入用戶數據。

在編碼器創建後到銷毀前均可使用，編碼過程中可以即時修改用戶數據內容。 用戶數據將被插入到IDR幀的SEI數據區域。

【語法】

```c
EncStatus      VideoEncoder_InsertUserData(EncoderHandle *hEnc,char*pUserData,unsigned int nlen);
```

【參數】

hEnc： 建立時返回的句柄

pUserData：用戶數據指標

nlen：用戶數據長度（0， 1024]

【返回值】

```c
typedef enum
{
    Enc_SUCCESS = 0,
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.6 VideoEncoder_Destory

【描述】

銷毀視頻編碼器

【語法】

```c
EncStatus VideoEncoder_Destroy(EncoderHandle *hEnc)
```

【參數】

hEnc： 建立時返回的句柄

【返回值】

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.7 VideoEncoder_EncodeOneFrame

【描述】

編碼一個視頻幀

【語法】

```c
EncStatus VideoEncoder_EncodeOneFrame(EncoderHandle *hEnc, EncInputFrame *input)
```

【參數】

hEnc： 建立時返回的句柄

input：輸入YUV視頻數據

```c
typedef struct
{
    unsigned short width;
    unsigned short height;
    unsigned short stride;
    unsigned char *data;
}EncInputFrame;
```

【返回值】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.2.8 VideoEncoder_GetStream

【描述】

獲取視頻編碼流的buffer，注：該buffer空間由編碼器內部分配。

【語法】

```c
EncStatus VideoEncoder_GetStream(EncoderHandle *hEnc, EncOutputStream *output)
```

【參數】

hEnc： 建立時返回的句柄

output：輸出編碼后的流數據buffer，bufSize大於0才有輸出

```c
typedef struct
{
    unsigned char *bufAddr;
    unsigned int bufSize; 
}EncOutputStream;
```

【返回值】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.2.9 VideoEncoder_GetStream_ByExtBuf

【描述】

獲取視頻編碼流的buffer，注：該buffer空間需由消費者調用此函數前分配。

【語法】

```c
EncStatus VideoEncoder_GetStream(EncoderHandle *hEnc, EncOutputStream *output)
```

【參數】

hEnc： 建立時返回的句柄

output：輸出編碼后的流數據buffer，bufSize大於0才有輸出

```c
typedef struct
{
    unsigned char *bufAddr;
    unsigned int bufSize; 
}EncOutputStream;
```

【返回值】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.3.0 VideoEncoder_ReleaseStream

【描述】

釋放視頻編碼流的buffer

【語法】

```c
EncStatus VideoEncoder_ReleaseStream(EncoderHandle *hEnc, EncOutputStream *output)
```

【參數】

- hEnc： 建立時返回的句柄
- output：VideoEncoder_GetStream返回的buffer

【返回值】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

# 2 硬體結構圖及軟體架構

# 2.1 硬體結構圖

K510的硬體框圖如下：
![hardware_block_diagram](../zh/images/multimedia_guides/hardware_block_diagram.png)

從video sensor接收到的數據，經MIPI DPHY、CSI、VI、ISP處理得到yuv源數據，並存儲到DDR中。 h264 encoder模組從DDR讀取數據，進行編碼運算，運算結果存儲到DDR中。

# 2.2 軟體架構

多媒體開發平臺的軟體架構如下：

![multimedia_block_diagram.png](../zh/images/multimedia_guides/multimedia_block_diagram.png)

其中，

- `libvenc`： encoder庫，用於調用h264 encoder core
- `libmediactl`： isp庫，用於控制sensor
- `libaudio3a`： audio3a庫，用於對音訊進行3a運算
- `alsa-lib`： 音訊庫，用於控制音訊介面

# 3 Demo應用

## 3.1 編碼應用程式

程式放在`/app/encode_app`目錄下：

- `encode_app`：Encode application程式
- 用於測試的yuv檔尺寸較大，沒有放入SDK包

運行`encode_app`

| 參數名 | 參數解釋 | 預設值 | 取值範圍 | 適用編碼模組 |
|:-|:-|:-|:-|:-|
| 説明 | 幫助資訊| | ||
| 分裂 | 通道個數 | 零 | [1,4] | jpeg、avc |
| 中文 | 通道號（從0開始） | 零 | [0,3] | jpeg、avc |
| 我 | 輸入yuv檔，只支援**nv12**格式 | 零 | v4l2 <br> xxx.yuv | jpeg、avc |
| 開發 | v4l2 設備名稱 | 零 | **sensor0：** /dev/video3 /dev/video4 <br> <br>sensor1：<br> ** /dev/video7 / ** dev/ <br> video8 <br> | 中風 |
| 或 | 輸出| 零 | rtsp <br> xxx.264 <br> xxx.MJPEG <br> xxx.JPEG | jpeg、avc |
| 在 | 輸出圖像寬度 | 1920 | avc： [128,2048]， 8 jpeg 的倍數 <br> ： 最多 8192， 16 的倍數 | jpeg、avc |
| h | 輸出圖像高度 | 1080 | avc： [64,2048]， 8 jpeg 的倍數 <br> ： 最多 8192， 2 的倍數 | jpeg、avc |
| 幀率 | 攝像頭採集幀率，目前只支援30pfs | 30 | 30 | 中風 |
| r | 編碼輸出幀率 | 30 | 能整除fps或者被fps整除的數 | 中風 |
| 內聯幀 | 輸入yuv幀數 | 0 | [0,32767] | jpeg、avc |
| 外幀 | 輸出yuv幀數，如果比參數-inframes大，將會重複編碼 | 0 | [0,32767] | jpeg、avc |
| 共和黨 | Group Of Picture，即兩個 I 幀之間的間隔 | 25 | [1,1000] | 中風 |
| rcmode | 表示碼率控制模式 0：CONST_QP 1：CBR 2：VBR | 斷續器 | [0,2] | 中風 |
| 比特率 | CBR 模式下的目標碼率或VBR模式下的最低碼率，單位Kb | 4000 | [1,20000] | 中風 |
| 最大比特 | VBR模式下的最高碼率，單位Kb | 4000 | [1,20000] | 中風 |
| 輪廓 | SPS 中的 profile_idc 參數：0： base 1：main 2：high 3：jpeg | AVC_HIGH | [0,3] | jpeg、avc |
| 水準 | SPS 中的 level_idc 參數 | 42 | [10,42] | 中風 |
| sliceqp | 初始 QP 值，-1表示auto | 25 | avc：-1，jpeg[0,51]<br/>：[1,100] | jpeg、avc |
| 最小 | 最小QP 值 | 0 | [0，切片] | 中風 |
| 最大qp | 最大QP值 | 54 | [切片qp，54] | 中風 |
| enableLTR | 使能長期參考幀，參數指定刷新週期。 0：不啟用刷新週期。 正數：週期性設置參考幀並且下一幀設置為使用長期參考幀 | 0 | [0,65535] | 中風 |
| 王 | roi配置檔，指定多個roi區域 | 零 | xxx.conf | 中風 |
| ae | 使能AE | 0 | 0-不使能AE<br>1-使能AE |
| 會議 | vl42配置檔，會指定的配置檔的基礎上，根據命令行輸入參數修改v4l2配置參數 | 零 | xxx.conf | 中風 |

### 3.1.1 輸入yuv文件，輸出檔

```shell
./encode_app -split 1 -ch 0 -i your_file.yuv -o out.264 -w 1920 -h 1080 -inframes 10 -outframes 30
./encode_app -split 1 -ch 0 -i your_file.yuv -o out.mjpeg -w 1920 -h 1080 -inframes 10 -outframes 30
```

### 3.1.2 輸入v4l2，輸出rtsp推流

#### 3.1.2.1 單通道

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

ffplay拉流命令示例：

```shell
 ffplay -rtsp_transport tcp rtsp://192.168.137.11:8554/testStream
```

- `rtsp://192.168.137.11:8554/testStream`為rtsp流url位址 ，-rtsp_transport tcp表示使用tcp傳輸音視頻數據（預設使用udp），可增加-fflags nobuffer選項來避免因播放機緩存而增加的延遲。

#### 3.1.2.2 單攝像頭雙通道

```shell
./encode_app -split 2 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -ch 1 -i v4l2 -dev /dev/video4 -o rtsp -w 1280 -h 720 -conf video_sample.conf
```

ffplay拉流命令同上。

#### 3.1.2.3 雙攝像頭

```shell
./encode_app -split 2 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -ch 1 -i v4l2 -dev /dev/video7 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

ffplay拉流命令同上。

#### 3.1.2.4 roi測試

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -sliceqp -1 -bitrate 2048 -roi roi_1920x1080.conf -conf video_sample.conf
```

roi檔格式

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

參數說明：

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

ffplay拉流命令同上。

### 3.1.3 幀率變換

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -r 60 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

ffplay拉流命令同上。

### 3.1.4 多種輸入幀率

目前支援VGA@75fps和720p60

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 640 -h 480 -fps 75 -r 75 -conf video_sample_vga480p75.conf
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1280 -h 720 -fps 60 -r 60 -conf video_sample_720p60.conf
```

ffplay拉流命令同上。

### 3.1.5 rtsp推送音視頻流

```c
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -alsa 1 -ac 2 -ar 44100 -af 2 -ad hw:0 -conf video_sample.conf
```

ffplay拉流命令同上。

### 3.1.6 注意事項

- 運行環境：核心板sensor：IMX219_SENSOR

- rtsp流位址格式：rtsp://ip 位址：埠號/testStream，其中ip位址和埠號可變，其餘部分固定.

  如：rtsp://192.168.137.11:8554/testStream，其中ip位址為192.168.137.11，埠號為8554.

  ip地址：開發板的ip位址，在板子上輸入ifconfig即可獲取。

  埠號：8554 + <通道号>*2，通道號一般從0開始（-ch 0，-ch 1...）。 

- 播放rtsp流方式：可通過vlc或ffplay來播放對應的rtsp流，數據流可以通過udp或tcp協定傳輸。

  1）rtp over udp播放：ffplay -rtsp_transport udp rtsp://192.168.137.11:8554/testStream

  2）rtp over tcp 播放： ffplay -rtsp_transport tcp rtsp://192.168.137.11:8554/testStream

  建議使用rtp over tcp方式播放，避免因udp丟包導致畫面花屏。

## 3.2 ffmpeg

ffmpeg放在/usr/local/bin目錄下。

- `ffmpeg`： ffmpeg 應用程式。

運行`ffmpeg`

（1） encoder libk510_h264參數
| 參數名 | 參數解釋 | 預設值 | 取值範圍 |
|:-|:-|:-|:-|
| g | 戈普大小 | 25 | 1~1000 |
| b | 比特率 | 4000000 | 0~20000000 |
| r | 幀率，由於isp目前只支援30fps，故解碼器應設置為30 | 30 | 30 |
| idr_freq | IDR頻率 | -1（沒有IDR） | -1~256 |
| 斷續器 | 用cqp編碼時，配置qp值 | -1（自動） | -1~100 |
| 最大速率 | bitrate的最大值 | 0 | 20000000 |
| 輪廓 | 支援的profile | 2（高） | 0 - 基線 <br> 1 - 主 <br> 2 - 高 |
| 水準 | 編碼level | 42 | 10~42 |
| 願意 | 屏幕寬高比 | 0（自動） | 0 - 自動 <br> 1 - 4：3 <br> 2 - 16：9 <br> 3 - 無 |
| 中文 | 通道數 | 0 | 0-7 |
| 幀到代碼 | 編碼幀數 | -1（所有幀） | -1~16383 |

（2） encoder libk510_jpeg參數
| 參數名 | 參數解釋 | 預設值 | 取值範圍 |
|:-|:-|:-|:-|
| 斷續器 | 用cqp編碼時，配置qp值 | 25 | -1~100 |
| r | 幀速率 | 30 | 25~60 |
| 中文 | 編碼通道 | 0 | 0~7 |
| 最大速率 | 最大比特率。（0=忽略） | 4000000 | 0~20000000 |
| 願意 | 縱橫比 | 0（自動） | 0 - 自動 <br> 1 - 4：3 <br> 2 - 16：9 <br> 3 - 無 |

（3） device libk510_video參數
| 參數名 | 參數解釋 | 預設值 | 取值範圍 |
|:-|:-|:-|:-|
| 瓦時 | 框架尺寸 | 零 | **對於編碼器 libk510_h264：**：<br>  最多 2048x2048 <br> 寬度倍數 8 <br> 高度倍數 8 <br> 分鐘 寬度： 128 <br> 最小高度： 64 <br> **對於編碼器 libk510_jpeg：** <br> 最大 8192x8192 <br> 寬度倍數 16 <br> 高度倍數 2 |
| exp | 曝光參數 | 0 | 0~128 |
| 斷續器 | 類比增益 | 0 | 0~232 |

（4） audio3a參數
| 參數名 | 參數解釋 | 預設值 | 取值範圍 |
|:-|:-|:-|:-|
| sample_rate | 音訊採樣率 | 16000 | 1~65535 |
| 斷續器 | 音訊增益模式 | 3（AgcModeFixedDigital） | 0 - AgcModeUnchanged <br> 1 - AgcModeAdaptiveAnalog <br> 2 - AgcModeAdaptiveDigital <br> 3 - AgcModeFixedIgital |
| ns | 雜訊level | 3（非常高） | 0 - 低 <br> 1 - 中等 <br> 2 - 高 <br> 3 - 非常高 |
| dsp_task | auido3a運行位置 | 1（分）分 | 0 - 中央處理器 <br>1 - DSP |

可以通過help命令查看可配置參數

```shell
ffmpeg -h encoder=libk510_h264 #查看k510编码器的参数
ffmpeg -h demuxer=v4l2 #查看demuxer的配置参数
ffmpeg -h filter=audio3a #查看audio3a的配置参数
```

ffmpeg的邏輯框如下：

![ffmpeg_block_diagram](../zh/images/multimedia_guides/ffmpeg_block_diagram.png)

audio3a用於將接收到的音訊進行3a運算並輸出，其邏輯框圖如下：

![ffmpeg_canaan_audio3a](../zh/images/multimedia_guides/ffmpeg_canaan_audio3a.png)

### 3.2.1 程序運行說明

#### 3.2.1.1 rtp推流

##### 3.2.1.1.1. rtp推送視頻流

ffmpeg執行命令示例：

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.102.231.29:1234
```

其中10.102.231.29為接收端位址，根據實際更改。
程序運行中按「q」停止運行。

ffplay 接收命令：

```shell
ffplay.exe -protocol_whitelist "file,udp,rtp" -i test.sdp -fflags nobuffer -analyzeduration 1000000 -flags low_delay
```

其中test.sdp按照如下範例配置。

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

.sdp參數說明：

- c=：媒體鏈接資訊; IN：網路類型; IP4：位址類型; 後面是IP位址（注意是接收端所在的IP位址，不是發送方的IP）
- m=是媒體級會話的開始處，video：媒體類型; 1234：埠號; RTP/AVP：傳輸協定; 96：rtp頭中的payload格式
按照實際情況修改接收端IP位址和埠號，注意rtp的埠號需為偶數。

##### 3.2.1.1.2. rtp推送音訊流

ffmpeg執行命令示例：

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f rtp rtp://10.100.232.11:1234
```

其中10.100.232.11為接收端位址，根據實際修改。

- ac：設置音訊通道數
- ar：設置音訊採樣率

ffplay接收命令與接收視頻流相同，sdp文件參考下面的示例。

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

##### 3.2.1.1.3 rtp推送音視頻流

ffmpeg執行命令示例：

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234 -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

ffplay接收命令與接收音訊流相同，sdp文件參考下面的示例。

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

#### 3.2.1.2 rtsp推流

rtsp推流前需要部署rtsp伺服器，將數據流推送到伺服器上。

##### 3.2.1.2.1 rtsp推視頻流

ffmpeg執行命令示例：

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -acodec copy -f rtsp rtsp://10.100.232.11:5544/live/test110
```

- `idr_freq`為IDR幀間隔，需要為GOP的整數倍。 rtsp推流必須生成IDR幀才能拉到流。
- `rtsp://10.100.232.11:5544/live/test110`為rtsp伺服器的推拉流url位址

ffplay拉流命令示例：

```shell
ffplay.exe -protocol_whitelist "file,udp,rtp,tcp" -i rtsp://10.100.232.11:5544/live/test110
```

##### 3.2.1.2.2 rtsp推音訊流

ffmpeg執行命令示例：

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f rtsp rtsp://10.100.232.11:5544/live/test110
```

ffplay拉流命令與rtsp拉視頻流的命令相同。

##### 3.2.1.2.3 rtsp推音視頻流

ffmpeg執行命令示例：

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -f alsa -ac 2 -ar 32000 -i hw:0 -idr_freq 25 -vcodec libk510_h264 -acodec aac -f rtsp rtsp://10.100.232.11:5544/live/test110
```

ffplay拉流命令與rtsp拉視頻流的命令相同。

#### 3.2.1.3 rtmp推流

rtmp推流前需要部署rtmp伺服器，將數據流推送到伺服器上。 支援rtmp協議的伺服器包括fms，nginx，srs等。

##### 3.2.1.3.1 rtmp推視頻流

ffmpeg執行命令示例：

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`為向rtmp伺服器推流的url位址  

ffplay拉流命令示例：

```shell
ffplay -fflags nobuffer rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`為從rtmp伺服器拉流的url位址 （推流和拉流的位址一樣），-fflags nobuffer選項來避免因播放機緩存而增加的延遲。

##### 3.2.1.3.2 rtmp推音訊流

ffmpeg執行命令示例：

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`為向rtmp伺服器推流的url位址

ffplay拉流命令與rtmp拉視頻流的命令相同。

##### 3.2.1.3.3 rtmp推音視頻流

ffmpeg執行命令示例：

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -f alsa -ac 2 -ar 32000 -i hw:0 -idr_freq 25 -vcodec libk510_h264 -acodec aac -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`為向rtmp伺服器推流的url位址

ffplay拉流命令與rtmp拉視頻流的命令相同。

#### 3.2.1.4 音訊3a

##### 3.2.1.4.1 單獨運行audio

（1） 在cpu上運行audio3a
ffmpeg執行命令示例：

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000:dsp_task=0 -f rtp rtp://10.100.232.11:1234
```

（2） 在dsp上運行audio3a
運行兩個telnet視窗，在兩個視窗中分別運行dsp task scheduler和ffmpeg（先運行dsp task scheduler）
dsp task scheduler運行命令實例：

```shell
cd /app/dsp_app_new/
./dsp_app /app/dsp_scheduler/scheduler.bin
```

ffmpeg運行命令實例：

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000 -f rtp rtp://10.100.232.11:1234
```

##### 3.2.1.4.2 同時運行audio3a和video

（1） 在cpu上運行audio3a
運行兩個telnet視窗，在兩個視窗中分別運行audio3a和video。
video命令示例：

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234
```

audio3a命令示例：

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000:dsp_task=0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

在cpu上同時運行audio3a和video會出現overflow，建議在dsp上運行audio3a
（2） 在dsp上運行audio3a
運行三個telnet視窗，在三個視窗上分別運行audio3a調用、video和dsp scheduler（先運行dsp task scheduler）
dsp task scheduler運行命令與單獨運行audio3a相同。

audio3a命令實例：

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000 -f rtp rtp://10.100.232.11:1236
```

video命令示例：

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234
```

- 10.100.232.11為rtp接收端的ip位址。
- 接收端ffplay的SDP文件內容，可以在運行上述ffmpeg命令后，從列印出來的log得到。

#### 3.2.1.5 v4l2

可以通過help命令查看可配置參數

```shell
ffmpeg -h demuxer=v4l2 #查看v4l2的配置参数
```

| 參數名 | 參數解釋 | 預設值 | 取值範圍 |
| :-- | :-- | :-- | :-- |
| s | 圖像解析度，例如1920x1080 | 零 | |
| r | 幀率，目前只支援30fps | 30 | 30 |
| 胰島 | 打開k510 isp硬體 | 0 | 0-1 |
| buf_type | v4l2 buffer`类型` <br>1： V4L2_MEMORY_MMAP ：適合於-vcodec copy<br>2： V4L2_MEMORY_USERPTR：適合於-vcodec libk510_h264 | 1 | 1~4 |
| 會議 | v4l2 配置檔 | 零 | |

ffmpeg運行命令示例：其中10.100.232.11為接收端位址，根據實際修改。

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234 -f alsa -ac 2 -ar 16000 -i hw:0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -i /dev/video3 -vcodec copy -y out.yuv
```

說明：

1. 運行時需要在運行目錄中查找`video_sampe.conf`、`imx219_0.conf`和`imx219_1.conf`檔進行配置，這三個檔在`/encode_app/`目錄下。 
2. 攝像頭實時進來的視頻寫成yuv文件，由於yuv檔很大，本地ddr或者nfs的寫速度跟不上，可能導致丟幀。

#### 3.2.1.6 JPEG編碼

檔案輸出：

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_jpeg -y test.mjpeg
```

說明：運行時需要在運行目錄中查找`video_sampe.conf`、`imx219_0.conf`和`imx219_1.conf`檔進行配置，這三個檔在`/encode_app/`目錄下。 

輸出的檔test.mjpeg可在PC端用ffplay播放

```shell
ffplay -i test.mjpeg
```

推流：

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_jpeg -an -f rtp rtp://10.100.232.11:1234
```

可用ffplay拉流

#### 3.2.1.7 多路編碼

最多支援8路同時編碼，可用每路的幀大小乘以幀率再相加，不要超過1080p60的數據量，-vcodec可選h264或者jpeg.

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -filter_complex 'split=2[out1][out2]' -map '[out1]' -vcodec libk510_h264 -ch 0 -an -f rtp rtp://10.20.1.101:1234 -map '[out2]' -vcodec libk510_h264 -ch 1 -an -f rtp rtp://10.20.1.101:2236
```

```shell
ffmpeg -f v4l2 -s 480x360 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -filter_complex 'split=8[out1][out2][out3][out4][out5][out6][out7][out8]' -map '[out1]' -vcodec libk510_h264 -b:v 300000 -ch 0 -an -f rtp rtp://10.20.1.101:1234 -map '[out2]' -vcodec libk510_h264 -b:v 300000 -ch 1 -an -f rtp rtp://10.20.1.101:2322 -map '[out3]' -vcodec libk510_h264 -b:v 300000 -ch 2 -an -f rtp rtp://10.20.1.101:3086 -map '[out4]' -vcodec libk510_h264 -b:v 300000 -ch 3 -an -f rtp rtp://10.20.1.101:4234 -map '[out5]' -vcodec libk510_h264 -b:v 300000 -ch 4 -an -f rtp rtp://10.20.1.101:5216 -map '[out6]' -vcodec libk510_h264 -b:v 300000 -ch 5 -an -f rtp rtp://10.20.1.101:6788 -map '[out7]' -vcodec libk510_h264 -b:v 300000 -ch 6 -an -f rtp rtp://10.20.1.101:7230 -map '[out8]' -vcodec libk510_h264 -b:v 300000 -ch 7 -an -f rtp rtp://10.20.1.101:8976
```

用ffplay拉流時，注意只能拉一路視頻，通過改變SDP檔里的埠號切換其他路的視頻，或者啟動多個ffplay拉流。

### 3.2.2 程式移植說明

`ffmpeg`在`ffmpeg`開原始程式碼4.4的版本上進行移植，`xxx.patch`為補丁包，增加了

- `ff_libk510_h264_encoder`：控制h264硬體編碼，引用了`libvenc.so`
- `ff_libk510_jpeg_encoder`：控制jpeg硬體編碼，引用了`libvenc.so`
- v4l2：在v4l2.c裡，加入了k510硬體相關代碼，實現了v4l2 buffer類型V4L2_MEMORY_USERPTR，引用了`libmediactl.so`。 

#### 3.2.2.1 patch生成命令

（1）

```shell
quilt new -p ab xxx.patch #在patches目录下生成xxx.patch文件
quilt add <filename> #添加修改前的文件
### 修改代码 ###
quilt refresh #修改内容被添加到xxx.patch
```

（2）
將xxx.patch複製到package/ffmpeg_canaan目錄中，並按照當前路徑修改patch檔中的文件路徑。

```shell
mv ../../patches/xxx.patch ../../package/ffmpeg_canaan
rm ../../patches/series
sed -i "s/\/dl\/ffmpeg_canaan\/ffmpeg-4.4//g" ../../package/ffmpeg_canaan/xxx.patch
```

#### 3.2.2.2 ffmpeg配置

在`package/ffmpeg_canaan/ffmpeg.mk`檔中，可以通過configure選項修改CPU核、編譯工具鏈，使能`ff_k510_video_demuxer` `ff_libk510_jpeg_encoder`和`ff_libk510_h264_encoder`。 

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

**翻譯免責聲明**  
為方便客戶，Canaan 使用 AI 翻譯程式將文字翻譯為多種語言，它可能包含錯誤。 我們不保證提供的譯文的準確性、可靠性或時效性。 對於因依賴已翻譯信息的準確性或可靠性而造成的任何損失或損害，Canaan 概不負責。 如果不同語言翻譯之間存在內容差異，以簡體中文版本為準。 

如果您要報告翻譯錯誤或不準確的問題，歡迎通過郵件與我們聯繫。