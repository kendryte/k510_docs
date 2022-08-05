![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 Multimedia Developer Guide</font>**

<font face="黑体"  size=3>Document version: V1.0.0</font>

<font face="黑体"  size=3>Published: 2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Disclaimer**</font>
The products, services or features you purchase shall be subject to the commercial contracts and terms of Beijing Canaan Jiesi Information Technology Co., Ltd. ("the Company", the same hereinafter), and all or part of the products, services or features described in this document may not be within the scope of your purchase or use. Except as otherwise agreed in the contract, the Company disclaims all representations or warranties, express or implied, as to the accuracy, reliability, completeness, marketing, specific purpose and non-aggression of any representations, information, or content of this document. Unless otherwise agreed, this document is provided as a guide for use only.
Due to product version upgrades or other reasons, the contents of this document may be updated or modified from time to time without any notice.

**<font face="黑体"  size=3>Trademark Notices</font>**

""<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, "Canaan" icon, Canaan and other trademarks of Canaan and other trademarks of Canaan are trademarks of Beijing Canaan Jiesi Information Technology Co., Ltd. All other trademarks or registered trademarks that may be mentioned in this document are owned by their respective owners.

**<font face="黑体"  size=3>Copyright ©2022 Beijing Canaan Jiesi Information Technology Co., Ltd</font>**
This document is only applicable to the development and design of the K510 platform, without the written permission of the company, no unit or individual may disseminate part or all of the content of this document in any form.

**<font face="黑体"  size=3>Beijing Canaan Jiesi Information Technology Co., Ltd</font>**
URL: canaan-creative.com
Business Enquiries: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# preface
## Document purpose
This document is an explanatory document for the K510 Multimedia application example.
## Target audience
For whom this document is intended:
- Software developers
- Technical support personnel

## Revision history

| The version number    | Modified by | Date of revision| Revision Notes  |  
|  ------  |-------| -------| ------ |
| v1.0.0    |System software groups | 2022-03-09 | SDK V1.5 released |
|     |     |      |   |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contents</font>**

[TOC]

# 1 Encoder API

## 1.1 Header File Description

k510_buildroot/package/encode_app/enc_interface.h

## 1.2 API function descriptions

### 1.2.1 VideoEncoder_Create

【Description】

Create a video encoder

【Grammar】

```c
EncoderHandle* VIdeoEncoder_Create(EncSettings *pCfg)
```

【Parameters】

pCfg: Enter the encoding configuration parameters

|            The parameter name             | Parameter interpretation                                                     |                           The value range                           | Applicable encoding modules |
| :---------------------------: | :----------------------------------------------------------- | :----------------------------------------------------------: | ------------ |
|            channel            | Channel number, supports up to 8 coded channels                                   |                            [0，7]                            | jpeg、avc    |
|             width             | Encodes the image width                                                 | avc: [128,2048], multiple of 8 <br/> jpeg: up to 8192, multiple of 16 | jpeg、avc    |
|            height             | Encode the height of the image                                                 | avc: [64,2048], multiple of 8 <br/> jpeg: up to 8192, multiple of 2 | jpeg、avc    |
|           FrameRate           | Frame rate, which can only be configured to a fixed few values                                    |                       (25,30,50,60,75)                       | jpeg、avc    |
|            rcMode             | Bitrate control mode 0:CONST_QP 1:CBR 2:VBR<br />jpeg is fixed to CONST_QP  |                       See RateCtrlMode                       | jpeg,avc    |
|            BitRate            | Target bitrate in CBR mode or lowest bitrate in VBR mode                    |                        [10,20000000]                         | stroke          |
|          MaxBitRate           | The highest bitrate in VBR mode                                          |                        [10,20000000]                         | stroke          |
|            SliceQP            | The initial QP value, -1 for auto                                        |                avc:-1,jpeg[0,51]<br/>:[1,100]                | jpeg,avc    |
|             MinQP             | The minimum qp value                                                     |                         [0,sliceqp]                          | stroke          |
|             MaxQP             | The maximum qp value                                                     |                         [sliceqp,54]                         | stroke          |
|            profile            | profile_idc parameters in SPS: 0: base 1:main 2:high 3:jpeg       |                            [0,3]                             | jpeg,avc    |
|             level             | level_idc parameters in PS                                       |                           [10,42]                            | stroke          |
|          AspectRatio          | Display scale                                                     |                     See AVC_AspectRatio                      | jpeg,avc    |
|            FreqIDR            | The interval between two idr frames                                              |                           [1,1000]                           | stroke          |
|            gopLen             | Group Of Picture, the interval between two I frames                      |                           [1,1000]                           | stroke          |
|          bEnableGDR           | Whether to enable in-frame refresh                                             |                         [true,false]                         | stroke          |
|            gdrMode            | gdr refresh mode: 0, vertical refresh 1, horizontal refresh                        |                       See GDRCtrlMode                        | stroke          |
|          bEnableLTR           | Whether long-term reference frames are enabled                                           |                         [true,false]                         | stroke          |
|          roiCtrlMode          | ROI control mode: 0: Do not use roi 1: relative qp 2: absolute qp                 |                       See ROICtrlMode                        | stroke          |
|       EncSliceSplitCfg        | slice split deployment                                               |                                                              | stroke          |
|         bSplitEnable          | Whether Slice splitting is enabled                                           |                         [true,false]                         | stroke          |
|         u32SplitMode          | Slice segmentation mode: 0: Split by bits. <br />1: Split by macroblock rows        |                            [0,1]                             | stroke          |
|         u32SliceSize          | u32SplitMode=0, indicating the number of bytes per slice<br /> u32SplitMode=1, represents the number<br /> of macroblock rows per slice| u32SplitMode=0，[100,65535]<br />u32SplitMode=1，[1, (image height +15)/16] | stroke          |
|          entropyMode          | Entropy encoding, 0: CABAC 1: CAVLC                                |                      See EncEntropyMode                      | stroke          |
|          encDblkCfg           | Block filtering configuration                                                 |                                                              | stroke          |
| disable_deblocking_filter_idc | The default value is 0, which means H.264 Agreement                          |                            [0，2]                            | stroke          |
|  slice_alpha_c0_offset_div2   | The default value is 0, which means H.264 Agreement                          |                           [-6，6]                            | stroke          |
|    slice_beta_offset_div2     | The default value is 0, which means H.264 Agreement                          |                          [-6,   6]                           | stroke          |

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

【Return value】

```c
typedef void* EncoderHandle
```

### 1.2.2 VideoEncoder_SetRoiCfg

【Description】

roi setting, support up to 8 rectangular areas, the system according to the index number of 0 ~ 7 to manage the ROI area, uIndex indicates that the user sets the index number of ROI. ROI regions can be superimposed on each other, and when an overlay occurs, the priority between ROI regions increases sequentially from index number 0 to 7.

It can be used after the encoder is created and before it is destroyed. The roi region can be dynamically adjusted during the encoding process.

【Grammar】

```c
EncStatus VideoEncoder_SetRoiCfg(EncoderHandle *hEnc,const EncROICfg*pEncRoiCfg);
```

【Parameters】

hEnc: The handle returned at creation time

pEncRoiCfg: Roi zone configuration information

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

Parameter description

```text
uIndex     - 指定该roi区域索引号，范围0-7最多支持8个区域
bEnable    - 指定该区域是否使能，只有使能的区域才有效
uQpValue   - qp值，可以是相对qp或绝对qp，qp模式由EncSettings中roiCtrlMode属性决定。绝对qp范围                  [0,51]，相对qp范围[-31,31]
stRect     - roi矩形区域，s32X矩形左上角x值，s32Y矩形左上角y值，u32Width矩形宽度，u32Height矩形高度
```

【Return value】

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.3 VideoEncoder_SetLongTerm

【Description】

Sets the next frame of the encoding to a long-term reference frame. It can be used after the encoder is created and before it is destroyed. The bEnableLTR attribute in EncSettings determines whether the feature is enabled.

【Grammar】

```c
EncStatus VideoEncoder_SetLongTerm(EncoderHandle *hEnc);
```

【Parameters】

hEnc: The handle returned at creation time

【Return value】

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.4 VideoEncoder_UseLongTerm

【Description】

Sets the encoding to the next frame using a long-term reference frame. It can be used after the encoder is created and before it is destroyed. The bEnableLTR attribute in EncSettings determines whether the feature is enabled.

【Grammar】

```c
EncStatus VideoEncoder_UseLongTerm(EncoderHandle *hEnc);
```

【Parameters】

hEnc: The handle returned at creation time

【Return value】

```c
typedef enum
{
    Enc_SUCCESS = 0,
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.5 VideoEncoder_InsertUserData

【Description】

Insert user data.

It can be used after the encoder is created and before it is destroyed, and the user data content can be modified in real time during the encoding process. The user data will be inserted into the SEI data area of the IDR frame.

【Grammar】

```c
EncStatus      VideoEncoder_InsertUserData(EncoderHandle *hEnc,char*pUserData,unsigned int nlen);
```

【Parameters】

hEnc: The handle returned at creation time

pUserData: A pointer to user data

nlen: User data length (0, 1024)

【Return value】

```c
typedef enum
{
    Enc_SUCCESS = 0,
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.6 VideoEncoder_Destory

【Description】

Destroy the video encoder

【Grammar】

```c
EncStatus VideoEncoder_Destroy(EncoderHandle *hEnc)
```

【Parameters】

hEnc: The handle returned at creation time

【Return value】

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.7 VideoEncoder_EncodeOneFrame

【Description】

Encode a video frame

【Grammar】

```c
EncStatus VideoEncoder_EncodeOneFrame(EncoderHandle *hEnc, EncInputFrame *input)
```

【Parameters】

hEnc: The handle returned at creation time

input: Enter the YUV video data

```c
typedef struct
{
    unsigned short width;
    unsigned short height;
    unsigned short stride;
    unsigned char *data;
}EncInputFrame;
```

【Return value】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.2.8 VideoEncoder_GetStream

【Description】

Gets the buffer of the video encoding stream, Note: This buffer space is allocated internally by the encoder.

【Grammar】

```c
EncStatus VideoEncoder_GetStream(EncoderHandle *hEnc, EncOutputStream *output)
```

【Parameters】

hEnc: The handle returned at creation time

output: Output the encoded stream data buffer, bufSize is greater than 0 to have the output

```c
typedef struct
{
    unsigned char *bufAddr;
    unsigned int bufSize; 
}EncOutputStream;
```

【Return value】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.2.9 VideoEncoder_GetStream_ByExtBuf

【Description】

Gets the buffer of the video encoding stream, Note: The buffer space needs to be allocated by the consumer before calling this function.

【Grammar】

```c
EncStatus VideoEncoder_GetStream(EncoderHandle *hEnc, EncOutputStream *output)
```

【Parameters】

hEnc: The handle returned at creation time

output: Output the encoded stream data buffer, bufSize is greater than 0 to have the output

```c
typedef struct
{
    unsigned char *bufAddr;
    unsigned int bufSize; 
}EncOutputStream;
```

【Return value】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.3.0 VideoEncoder_ReleaseStream

【Description】

Release the buffer of the video encoding stream

【Grammar】

```c
EncStatus VideoEncoder_ReleaseStream(EncoderHandle *hEnc, EncOutputStream *output)
```

【Parameters】

- hEnc: The handle returned at creation time
- output:VideoEncoder_GetStream the buffer returned

【Return value】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

# 2 Hardware structure diagram and software architecture

# 2.1 Hardware Structure Diagram

The hardware block diagram of the K510 is as follows:
![hardware_block_diagram](../zh/images/multimedia_guides/hardware_block_diagram.png)

The data received from the video sensor is processed by MIPI DPHY, CSI, VI, isP to obtain the yuv source data and stored in the DDR. The h264 encoder module reads data from the DDR, performs encoding operations, and stores the results of the operations in the DDR.

# 2.2 Software Architecture

The software architecture of the multimedia development platform is as follows:

![multimedia_block_diagram.png](../zh/images/multimedia_guides/multimedia_block_diagram.png)

thereinto

- `libvenc`: Encoder library for calling h264 encoder core
- `libmediactl`: Isp library for controlling sensors
- `libaudio3a`: Audio3a library for 3a operations on audio
- `alsa-lib`: Audio library for controlling the audio interface

# 3 Demo app

## 3.1 Encode Application

The program is placed`/app/encode_app` in the directory:

- `encode_app`: Encode application program
- The yuv file used for testing is large in size and does not fit into the SDK package

run`encode_app`

| The parameter name | Parameter interpretation | The default value | The value range | Applicable encoding modules |
|:-|:-|:-|:-|:-|
| help | Help information| | ||
| split | The number of channels | NULL | [1,4] | jpeg、avc |
| ch | Channel number (0-based) | NULL | [0,3] | jpeg、avc |
| i | Enter the YUV file, only**support nv12** format | NULL | v4l2 <br> xxx.yuv | jpeg、avc |
| dev | v4l2 device name | NULL | **sensor0:** /dev/video3 /dev/video4 <br> <br>sensor1:<br> **/dev/video7 /** dev/ <br> video8 <br> | stroke |
| or | output| NULL | rtsp <br> xxx.264 <br> xxx.MJPEG <br> xxx.JPEG | jpeg、avc |
| in | Output image width | 1920 | avc: [128,2048], multiple of 8 <br> jpeg: up to 8192, multiple of 16 | jpeg、avc |
| h | Output image height | 1080 | avc: [64,2048], multiple of 8 <br> jpeg: up to 8192, multiple of 2 | jpeg、avc |
| fps | The camera captures frame rates, which currently only support 30pfs | 30 | 30 | stroke |
| r | Encoded output frame rate | 30 | The number that can divisible or be divisible by fps | stroke |
| inframes | Enter the number of yuv frames | 0 | [0,50] | jpeg、avc |
| outframes | The output of the yuv frames, if larger than the parameter -inframes, will be repeated encoding | 0 | [0,32767] | jpeg、avc |
| gop | Group Of Picture, the interval between two I frames | 25 | [1,1000] | stroke |
| rcmode | Represents bitrate control mode 0:CONST_QP 1:CBR 2:VBR | CBR | [0,2] | stroke |
| bitrate | Target bitrate in CBR mode or lowest bitrate in VBR mode, in KB | 4000 | [1,20000] | stroke |
| maxbitrate | The highest bitrate in VBR mode, in Kb | 4000 | [1,20000] | stroke |
| profile | profile_idc parameters in SPS: 0: base 1:main 2:high 3:jpeg | AVC_HIGH | [0,3] | jpeg、avc |
| level | level_idc parameters in SPS | 42 | [10,42] | stroke |
| sliceqp | The initial QP value, -1 for auto | 25 | avc:-1,jpeg[0,51]<br/>:[1,100] | jpeg、avc |
| minqp | The minimum QP value | 0 | [0,sliceqp] | stroke |
| maxqp | The maximum QP value | 54 | [sliceqp,54] | stroke |
| enableLTR | Enables long-term reference frames, and parameters specify the refresh period. 0: The refresh cycle is not enabled. Positive: Periodically sets the reference frame and the next frame is set to use the long reference frame | 0 | [0,65535] | stroke |
| king | Roi configuration file, which specifies multiple roi regions | NULL | xxx.conf | stroke |
| ae | Enable AE | 0 | 0 - Does not enable AE<br>1 - Enable AE | |
| Conf | The vl42 configuration file modifies the v4l2 configuration parameters based on the specified configuration file and the command line input parameters | NULL | xxx.conf | stroke |

### 3.1.1 Enter the yuv file and output the file

```shell
./encode_app -split 1 -ch 0 -i your_file.yuv -o out.264 -w 1920 -h 1080 -inframes 10 -outframes 30
./encode_app -split 1 -ch 0 -i your_file.yuv -o out.mjpeg -w 1920 -h 1080 -inframes 10 -outframes 30
```

### 3.1.2 Input v4l2, output rtsp push stream

#### 3.1.2.1 Single Channel

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

Example of a ffplay pull command:

```shell
 ffplay -rtsp_transport tcp rtsp://192.168.137.11:8554/testStream
```

- `rtsp://192.168.137.11:8554/testStream`For the rtsp stream url address, -rtsp_transport tcp means to use tcp to transmit audio and video data (udp is used by default), and the -fflags nobuffer option can be added to avoid increased latency due to player caching.

#### 3.1.2.2 Single camera dual channel

```shell
./encode_app -split 2 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -ch 1 -i v4l2 -dev /dev/video4 -o rtsp -w 1280 -h 720 -conf video_sample.conf
```

The ffplay pull stream command is the same as above.

#### 3.1.2.3 Dual Cameras

```shell
./encode_app -split 2 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -ch 1 -i v4l2 -dev /dev/video7 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

The ffplay pull stream command is the same as above.

#### 3.1.2.4 ROI test

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -sliceqp -1 -bitrate 2048 -roi roi_1920x1080.conf -conf video_sample.conf
```

roi file format

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

Parameter description:

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

The ffplay pull stream command is the same as above.

### 3.1.3 Frame rate transformation

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -r 60 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

The ffplay pull stream command is the same as above.

### 3.1.4 Multiple input frame rates

VGA@75fps and 720p60 are currently supported

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 640 -h 480 -fps 75 -r 75 -conf video_sample_vga480p75.conf
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1280 -h 720 -fps 60 -r 60 -conf video_sample_720p60.conf
```

The ffplay pull stream command is the same as above.

### 3.1.5 rtsp push audio and video streams

```c
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -alsa 1 -ac 2 -ar 44100 -af 2 -ad hw:0 -conf video_sample.conf
```

The ffplay pull stream command is the same as above.

### 3.1.6 Precautions

- Operating environment: Core board sensor: IMX219_SENSOR

- rtsp stream address format: rtsp://ip address: port number/testStream, where ip address and port number are variable and the rest are fixed.

  Such as: rtsp://192.168.137.11:8554/testStream, where the IP address is 192.168.137.11, the port number is 8554.

  IP address: The IP address of the development board, enter ifconfig on the board to obtain.

  Port number: 8554 + <通道号>*2, channel numbers generally start from 0 (-ch 0, -ch 1...).

- Play RTSP stream mode: the corresponding RTSP stream can be played through vlc or ffplay, and the data stream can be transmitted through the udp or TCP protocol.

  1)rtp over udp播放：ffplay -rtsp_transport  udp rtsp://192.168.137.11:8554/testStream

  2)rtp over tcp 播放:   ffplay -rtsp_transport   tcp  rtsp://192.168.137.11:8554/testStream

  It is recommended to use rtp over tcp to play to avoid the screen caused by udp packet loss.

## 3.2 ffmpeg

ffmpeg is placed in the /usr/local/bin directory.

- `ffmpeg`: ffmpeg app.

run`ffmpeg`

(1) Encoder libk510_h264 parameter
| The parameter name | Parameter interpretation | The default value | The value range |
|:-|:-|:-|:-|
| g | gop size | 25 | 1~1000 |
| b | bitrate | 4000000 | 0~20000000 |
| r | Frame rate, since isps currently only support 30fps, so the decoder should be set to 30 | 30 | 30 |
| idr_freq | IDR frequency | -1 (no IDR) | -1~256 |
| qp | When encoding with cqp, configure the qp value | -1(auto) | -1~100 |
| maxrate | The maximum value of the bitrate | 0 | 20000000 |
| profile | Supported profiles | 2(high) | 0 - baseline <br> 1 - main <br> 2 - high |
| level | Encode level | 42 | 10~42 |
| would | Screen aspect ratio | 0(auto) | 0 - auto <br> 1 - 4:3 <br> 2 - 16:9 <br> 3 - none |
| ch | channel number | 0 | 0-7 |
| framesToEncode | The number of encoded frames | -1 (all frames) | -1~16383 |

(2) Encoder libk510_jpeg parameters
| The parameter name | Parameter interpretation | The default value | The value range |
|:-|:-|:-|:-|
| qp | When encoding with cqp, configure the qp value | 25 | -1~100 |
| r | framerate | 30 | 25~60 |
| ch | encode channel | 0 | 0~7 |
| maxrate | Maximum bitrate. (0=ignore) | 4000000 | 0~20000000 |
| would | aspect ratio | 0(auto) | 0 - auto <br> 1 - 4:3 <br> 2 - 16:9 <br> 3 - none |

(3) The device libk510_video parameter
| The parameter name | Parameter interpretation | The default value | The value range |
|:-|:-|:-|:-|
| wh | frame size | NULL | **for encoder libk510_h264:**:<br>  up to 2048x2048 <br> width multiple of 8 <br> height multiple of 8 <br> min. width: 128 <br> min. height: 64 <br> **for encoder libk510_jpeg:** <br> up to 8192x8192 <br> width multiple of 16 <br> height multiple of 2 |
| exp | exposure parameter | 0 | 0~128 |
| agc | analog gain | 0 | 0~232 |

(4) audio3a parameter
| The parameter name | Parameter interpretation | The default value | The value range |
|:-|:-|:-|:-|
| sample_rate | Audio sample rate | 16000 | 1~65535 |
| agc | Audio gain mode | 3(AgcModeFixedDigital) | 0 - AgcModeUnchanged <br> 1 - AgcModeAdaptiveAnalog <br> 2 - AgcModeAdaptiveDigital <br> 3 - AgcModeFixedDigital |
| ns | Noise level | 3(VeryHigh) | 0 - Low <br> 1 - Moderate <br> 2 - High <br> 3 - VeryHigh |
| dsp_task | Auido3a running position | 1(dsp) | 0 - cpu <br>1 - dsp |

Configurable parameters can be viewed via the help command

```shell
ffmpeg -h encoder=libk510_h264 #查看k510编码器的参数
ffmpeg -h demuxer=v4l2 #查看demuxer的配置参数
ffmpeg -h filter=audio3a #查看audio3a的配置参数
```

The logical box for ffmpeg is as follows:

![ffmpeg_block_diagram](../zh/images/multimedia_guides/ffmpeg_block_diagram.png)

audio3a is used to perform 3a operations on the received audio and output it, and its logical block diagram is as follows:

![ffmpeg_canaan_audio3a](../zh/images/multimedia_guides/ffmpeg_canaan_audio3a.png)

### 3.2.1 Program Operation Instructions

#### 3.2.1.1 rtp stream push

##### 3.2.1.1.1. rtp push video stream

Example of a ffmpeg run command:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.102.231.29:1234
```

Where 10.102.231.29 is the receiving address, it is changed according to the actual situation.
Press "q" while the program is running to stop running.

ffplay receives the command:

```shell
ffplay.exe -protocol_whitelist "file,udp,rtp" -i test.sdp -fflags nobuffer -analyzeduration 1000000 -flags low_delay
```

Test.sdp is configured as follows.

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

Description of the .sdp parameter:

- c=: Media link information; IN: Network Type; IP4: Address type; Followed by the IP address (note that it is the IP address where the receiver is located, not the IP of the sender)
- m= is the beginning of a media-level session, video:media type; 1234: Port number; RTP/AVP: Transport Protocol; 96: Payload format in the rtp header
Modify the ip address and port number of the receiver according to the actual situation, and note that the port number of rtp must be even.

##### 3.2.1.1.2. rtp push audio stream

Example of a ffmpeg run command:

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f rtp rtp://10.100.232.11:1234
```

Where 10.100.232.11 is the receiving address, it is modified according to the actual situation.

- ac: Sets the number of audio channels
- ar: Sets the audio sample rate

The ffplay receive command is the same as receiving a video stream, and the sdp file refers to the following example.

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

##### 3.2.1.1.3 rtp push audio and video streams

Example of a ffmpeg run command:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234 -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

The ffplay receive command is the same as receiving an audio stream, and the sdp file refers to the following example.

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

Before rtsp pushes the stream, you need to deploy the rtsp server to push the data stream to the server.

##### 3.2.1.2.1 rtsp push video streams

Example of a ffmpeg run command:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -acodec copy -f rtsp rtsp://10.100.232.11:5544/live/test110
```

- `idr_freq`For the IDR frame interval, an integer multiple of the GOP is required. RTSP streams must generate IDR frames to pull to streams.
- `rtsp://10.100.232.11:5544/live/test110`Is the push-pull stream URL address of the RTSP server

Example of a ffplay pull command:

```shell
ffplay.exe -protocol_whitelist "file,udp,rtp,tcp" -i rtsp://10.100.232.11:5544/live/test110
```

##### 3.2.1.2.2 rtsp push audio stream

Example of a ffmpeg run command:

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f rtsp rtsp://10.100.232.11:5544/live/test110
```

The ffplay pull stream command is the same as the rtsp pull video stream command.

##### 3.2.1.2.3 rtsp push audio video stream

Example of a ffmpeg run command:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -f alsa -ac 2 -ar 32000 -i hw:0 -idr_freq 25 -vcodec libk510_h264 -acodec aac -f rtsp rtsp://10.100.232.11:5544/live/test110
```

The ffplay pull stream command is the same as the rtsp pull video stream command.

#### 3.2.1.3 rtmp push stream

Before rtmp streaming, you need to deploy the rtmp server to push the data stream to the server. Servers that support the RTMP protocol include fms, nginx, srs, etc.

##### 3.2.1.3.1 rtmp pushes video streams

Example of a ffmpeg run command:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`The URL address for pushing the stream to the rtmp server  

Example of a ffplay pull command:

```shell
ffplay -fflags nobuffer rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`To pull the url address of the stream from the rtmp server (push streams are the same as the address of the pull stream), the -fflags nobuffer option to avoid increased latency due to player caching.

##### 3.2.1.3.2 rtmp push audio stream

Example of a ffmpeg run command:

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`The URL address for pushing the stream to the rtmp server

The ffplay pull stream command is the same as the rtmp pull video stream command.

##### 3.2.1.3.3 rtmp push audio and video streams

Example of a ffmpeg run command:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -f alsa -ac 2 -ar 32000 -i hw:0 -idr_freq 25 -vcodec libk510_h264 -acodec aac -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`The URL address for pushing the stream to the rtmp server

The ffplay pull stream command is the same as the rtmp pull video stream command.

#### 3.2.1.4 audio3a

##### 3.2.1.4.1 Run audio separately

(1) Run audio3a on the CPU
Example of a ffmpeg run command:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000:dsp_task=0 -f rtp rtp://10.100.232.11:1234
```

(2) Run audio3a on dsp
Run two telnet windows, run dsp task scheduler and ffmpeg in both windows (run dsp task scheduler first)
dsp task scheduler runs the command instance:

```shell
cd /app/dsp_app_new/
./dsp_app /app/dsp_scheduler/scheduler.bin
```

ffmpeg run command example:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000 -f rtp rtp://10.100.232.11:1234
```

##### 3.2.1.4.2 Run audio3a and video at the same time

(1) Run audio3a on the CPU
Run two telnet windows, run audio3a and video in both windows.
Example of the video command:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234
```

Example of the audio3a command:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000:dsp_task=0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

Running audio3a and video on the cpu at the same time will produce overflow, it is recommended to run audio3a on dsp
(2) Run audio3a on dsp
Run three telnet windows, run audio3a calls, video, and dsp scheduler on each of the three windows
The dsp task scheduler run command is the same as running audio3a alone.

Example of the audio3a command:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000 -f rtp rtp://10.100.232.11:1236
```

Example of the video command:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234
```

- 10.100.232.11 is the IP address of the rtp receiver.
- The contents of the SDP file of the receiving terminal ffplay can be obtained from the printed log after running the above ffmpeg command.

#### 3.2.1.5 v4l2

Configurable parameters can be viewed via the help command

```shell
ffmpeg -h demuxer=v4l2 #查看v4l2的配置参数
```

| The parameter name | Parameter interpretation | The default value | The value range |
| :-- | :-- | :-- | :-- |
| s | Image resolution, such as 1920x1080 | NULL | |
| r | Frame rate, currently only support 30fps | 30 | 30 |
| isp | Turn on the k510 ISP hardware | 0 | 0-1 |
| buf_type | v4l2 buffer`类型` <br>1: V4L2_MEMORY_MMAP: for -vcodec copy<br>2: V4L2_MEMORY_USERPTR: for -vcodec libk510_h264 | 1 | 1~2 |
| Conf | v4l2 config file | NULL | |

Example of ffmpeg running command: where 10.100.232.11 is the receiving address, modified according to the actual situation.

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234 -f alsa -ac 2 -ar 16000 -i hw:0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -i /dev/video3 -vcodec copy -y out.yuv
```

Illustrate:

1. The runtime needs to be found in the run directory`video_sampe.conf`, `imx219_0.conf`and the `imx219_1.conf`files are configured, and the three files are under`/encode_app/` the directory.
2. The video that comes in real time by the camera is written as a YUV file, and because the YUV file is very large, the local DDR or NFS writing speed cannot keep up, which may cause frame drop.

#### 3.2.1.6 JPEG encoding

File Output:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_jpeg -y test.mjpeg
```

Description: The runtime needs to be located in the run directory`video_sampe.conf`, `imx219_0.conf`and `imx219_1.conf`the files are configured, and the three files are under`/encode_app/` the directory.

The output file test.mjpeg can be played on the PC side with ffplay

```shell
ffplay -i test.mjpeg
```

Push Stream:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_jpeg -an -f rtp rtp://10.100.232.11:1234
```

Ffplay pull streams are available

#### 3.2.1.7 Multiplexing encoding

Support up to 8 simultaneous encoding, you can use the frame size of each channel multiplied by the frame rate and then added, do not exceed the amount of data of 1080p60, -vcodec can choose h264 or jpeg.

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -filter_complex 'split=2[out1][out2]' -map '[out1]' -vcodec libk510_h264 -ch 0 -an -f rtp rtp://10.20.1.101:1234 -map '[out2]' -vcodec libk510_h264 -ch 1 -an -f rtp rtp://10.20.1.101:2236
```

```shell
ffmpeg -f v4l2 -s 480x360 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -filter_complex 'split=8[out1][out2][out3][out4][out5][out6][out7][out8]' -map '[out1]' -vcodec libk510_h264 -b:v 300000 -ch 0 -an -f rtp rtp://10.20.1.101:1234 -map '[out2]' -vcodec libk510_h264 -b:v 300000 -ch 1 -an -f rtp rtp://10.20.1.101:2322 -map '[out3]' -vcodec libk510_h264 -b:v 300000 -ch 2 -an -f rtp rtp://10.20.1.101:3086 -map '[out4]' -vcodec libk510_h264 -b:v 300000 -ch 3 -an -f rtp rtp://10.20.1.101:4234 -map '[out5]' -vcodec libk510_h264 -b:v 300000 -ch 4 -an -f rtp rtp://10.20.1.101:5216 -map '[out6]' -vcodec libk510_h264 -b:v 300000 -ch 5 -an -f rtp rtp://10.20.1.101:6788 -map '[out7]' -vcodec libk510_h264 -b:v 300000 -ch 6 -an -f rtp rtp://10.20.1.101:7230 -map '[out8]' -vcodec libk510_h264 -b:v 300000 -ch 7 -an -f rtp rtp://10.20.1.101:8976
```

When using ffplay to pull streams, be careful to pull only one video, switch the video of other roads by changing the port number in the SDP file, or start multiple ffplay streams.

### 3.2.2 Program Porting Instructions

`ffmpeg``ffmpeg`Ported on the open source version 4.4,`xxx.patch` added for the service pack

- `ff_libk510_h264_encoder`: Control h264 hardware encoding, referenced`libvenc.so`
- `ff_libk510_jpeg_encoder`: Controls the jpeg hardware encoding, referenced`libvenc.so`
- v4l2: In v4l2.c, k510 hardware-related code was added, and the v4l2 buffer type V4L2_MEMORY_USERPTR and referenced`libmediactl.so`.

#### 3.2.2.1 patch generation command

（1）

```shell
quilt new -p ab xxx.patch #在patches目录下生成xxx.patch文件
quilt add <filename> #添加修改前的文件
### 修改代码 ###
quilt refresh #修改内容被添加到xxx.patch
```

（2）
Copy xxx.patch to the package/ffmpeg_canaan directory and modify the file path in the patch file according to the current path.

```shell
mv ../../patches/xxx.patch ../../package/ffmpeg_canaan
rm ../../patches/series
sed -i "s/\/dl\/ffmpeg_canaan\/ffmpeg-4.4//g" ../../package/ffmpeg_canaan/xxx.patch
```

#### 3.2.2.2 ffmpeg configuration

In the `package/ffmpeg_canaan/ffmpeg.mk`file, the CPU core can be modified, the compilation toolchain, and the enable can be made through the configee option`ff_k510_video_demuxer`.`ff_libk510_jpeg_encoder` `ff_libk510_h264_encoder`

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

**Translation Disclaimer**  
For the convenience of customers, Canaan uses an AI translator to translate text into multiple languages, which may contain errors. We do not guarantee the accuracy, reliability or timeliness of the translations provided. Canaan shall not be liable for any loss or damage caused by reliance on the accuracy or reliability of the translated information. If there is a content difference between the translations in different languages, the Chinese Simplified version shall prevail.

If you would like to report a translation error or inaccuracy, please feel free to contact us by mail.
