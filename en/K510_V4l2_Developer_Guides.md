![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 V4L2 Developer's Guide</font>**

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
**<font face="黑体"  size=5>Document purpose</font>**
This document is an explanatory document for the K510 V4L2 application example.

**<font face="黑体"  size=5>Reader Objects</font>**

The main people to whom this document (this guide) applies:

- Software developers
- Technical support personnel

**<font face="黑体"  size=5>Revision history</font>**
 <font face="宋体"  size=2>The revision history accumulates a description of each document update. The latest version of the document contains updates for all previous versions. </font>

| The version number   | Modified by     | Date of revision | Revision Notes |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | System software groups | 2022-03-09 | SDK V1.5 released |
| v1.0.1 | Zhu Dalei | 2022-03-11 | SDK V1.5 released |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contents</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 V4L2 mediactl library

## 1.1 Header File Description

\#include “media_ctl.h”

## 1.2 API function descriptions

### ◆ mediactl_init

```c
struct video_info {
    unsigned int video_used;
    char *video_name[4];
    unsigned int enable[4];
    unsigned int video_width[4];
    unsigned int video_height[4];
    unsigned int video_out_format[4];
};

int mediactl_init(char *video_cfg_file,struct video_info *dev_info);
```

Initialize media.

#### parameter

```text
parameter:
[in]    video_cfg_file: The video configuration file, the content of this file only needs to care about the content explained below, the specific explanation is as follows.
sensor0_name: the name of the sensor driver only set in the V4L2 driver.
sensor0_cfg_file: the name of the isp parameter configuration file corresponding to the sensor, such as imx219_0.conf.
sensor0_total_width: the total pixels in the horizontal direction output by the sensor are used to generate the VSYNC signal, such as 3476
sensor0_total_height: the total number of lines output by sensor, used to generate HSYNC signal, such as 1166
sensor0_active_width: the effective pixels in the horizontal direction of the sensor output, such as 1920
sensor0_active_height: number of valid lines of sensor output, such as 1080
video2_used: 1 -- enable, 0 -- not use.
video2_width: video output width, such as 1920.
video2_height: video output height, such as 1080.
video2_out_format: 1--YUV420,NV21.
video3_used: 1 -- enable，0 -- not use.
video3_width: video output width, such as 1080.
video3_height: video output height, such as 720.
video3_out_format: 1--YUV420,NV21.
video4_used: 1 -- enable，0 -- not use.
video4_width: video output width, such as 640.
video4_height: video output height, such as 480.
video4_out_format: 1--YUV420,NV21.
video5_used: 1 -- enable，0 -- not use.
video5_width: video output width, such as 320.
video5_height: the height of video storage, such as 320.
video5_height_r: video output height, such as 240.
video5_out_format: 0--Separate RGB, 1--ARGB.
sensor1_name: the name of the sensor driver only set in the V4L2 driver.
sensor1_cfg_file: the name of the isp parameter configuration file corresponding to the sensor, such as imx219_0.conf.
sensor1_total_width: the total pixels in the horizontal direction output by the sensor are used to generate the VSYNC signal, such as 3476.
sensor1_total_height: the total number of lines output by sensor, used to generate HSYNC signal, such as 1166.
sensor1_active_width: the effective pixels in the horizontal direction output by the sensor, such as 1920.
sensor1_active_height: the number of valid lines output by sensor, such as 1080
video6_used: 1 -- enable，0 -- not use.
video6_width: video output width, such as 1920.
video6_height: video output height, such as 1080.
video6_out_format: 1--YUV420,NV21.
video7_used: 1 -- enable，0 -- not use.
video7_width: video output width, such as 1080.
video7_height: video output height, such as 720.
video7_out_format: 1--YUV420,NV21.
video8_used: 1 -- enable，0 -- not use.
video8_width: video output width, such as 640.
video8_height: video output height, such as 480.
video8_out_format: 1--YUV420,NV21.
video9_used: 1 -- enable，0 -- not use.
video9_width: video output width, such as 320.
video9_height: the width of video storage, such as 320.
video9_height_r: video output height, such as 240.
video9_out_format: 0--Separate RGB, 1--ARGB.
[out]   dev_info: mediactl_lib returns the video information obtained from the video configuration file, the specific explanation is as follows.
video_used: this refers to the ISP's pipeline, if it is used, it will return 1, otherwise 0. K510 supports two pipelines, ISP_F2K/ISP_R2K, and each pipeline supports up to 4 video outputs.
video_name[4]: the name of the returned video. The four videos of f2k are video2/video3/video4/video5; the four videos of r2k are video6/video7/video8/video9.
enable[4]: whether each video returned is enable, 1 -- enable, 0 -- not use.
video_width[4]: the width of each video returned.
video_height[4]: the height of each video returned.
video_out_format[4]: the output image format of each video returned, see the explanation of "Video Configuration File" for details.
The specific usage is as follows:
char *video_cfg_file = "video_cfg";
struct video_info dev_info[2]
mediactl_init(video_cfg_file,&dev_info)
```

#### The return value

```text
0 success,  -1 fail.
```

### ◆ mediactl_exit

Shut down the media device and free up the requested share memory memory.

#### parameter

```text
parameter:
N/A
```

### ◆ adaptive_enable

```c
enum adaptive_enable_select_e
{
    ADAPTIVE_SELECT_DISABLE,
    ADAPTIVE_SELECT_ENABLE,
};
int adaptive_enable(int scl);
```

Configuring the ISP Adaptive Function Switch

#### parameter

```text
parameter
ADAPTIVE_SELECT_DISABLE: disable adaptive calc function
ADAPTIVE_SELECT_ENABLE: disable adaptive calc function(default)
```

### ◆ ae_select_init

```c
enum ae_select_e
{
    AE_SELECT_SW_MODE,
    AE_SELECT_HW_MODE,
};
int ae_select_init(int scl);

```

configure sw/hw AE switch function

#### parameter

```text
parameter
AE_SELECT_SW_MODE: enable sw AE(default)
AE_SELECT_HW_MODE: enable hw AE
```

### ◆ anti_flicker_init

```c
enum anti_flicker_scl_e
{
    ANTI_FLICKER_ALL_DSIABLE,
    ANTI_FLICKER_F2K_ENABLE,
    ANTI_FLICKER_R2K_ENABLE,
    ANTI_FLICKER_ALL2K_ENABLE,
};
int anti_flicker_init(int scl);
```

configure antiflicker correction function

#### parameter

```text
parameter
ANTI_FLICKER_ALL_DSIABLE: disable antiflicker correction function
ANTI_FLICKER_F2K_ENABLE: enable F2K antiflicker50Hz correction function
ANTI_FLICKER_R2K_ENABLE: enable R2K antiflicker50Hz correction function
ANTI_FLICKER_ALL2K_ENABLE: enableF2K/R2K antiflicker50Hz  correction function(default)
```

### ◆ mediactl_rect

```c
/**
 * @brief Use ISP to draw rect.
 * @param pipeline
 * @param layer 0: main out, 1: DS0, 2: DS1.
 * @param area support 32 area, 0 to 31
 * @param x
 * @param y
 * @param width
 * @param height
 * @param line_width 0 to 63 pixels
 * @param color AYCbCr, Alpha as hight bits, Cr as low bits
 * @param border_mask up/right/bottom/left, up as low bit, left as hight bit
 * @return return 0 if success, -1 if failed.
*/
int mediactl_rect(enum isp_pipeline_e pipeline, unsigned layer, unsigned area, unsigned x, unsigned y, unsigned width, unsigned height, unsigned line_width, unsigned color, unsigned border_mask);
```

Draw rectangles.

### ◆ mediactl_disable_ae

```c
enum isp_pipeline_e {
    ISP_F2K_PIPELINE,
    ISP_R2K_PIPELINE,
    ISP_TOF_PIPELINE
};
int mediactl_set_ae(enum isp_pipeline_e pipeline);
```

Disable specific ISP AE.

#### parameter

```text
parameter:
ISP_F2K_PIPELINE: configure f2k pipeline AE
ISP_R2K_PIPELINE: configure r2k pipeline AE
ISP_TOF_PIPELINE:not use.
```

### ◆ mediactl_get_isp_modules

```c
enum isp_modules {
    ISP_TPG,
    ISP_BLC,
    ISP_LSC,
    ISP_AE,
    ISP_AWB,
    ISP_AWB_D65,
    ISP_AWB_CCM,
    ISP_WDR,
    ISP_RGB_GAMMA,
    ISP_YUV_GAMMA,
    ISP_ADA,
    ISP_ADA_SBZ,
    ISP_ADA_CCR,
    ISP_RGBIR,
    ISP_RAW_2DNR,
    ISP_YUV_Y_2DNR,
    ISP_YUV_UV_2DNR,
    ISP_3DNR,
    ISP_LTM,
    ISP_SHARP,
    ISP_CC,
    ISP_CTRST,
    ISP_LUMA,
    ISP_SATURATION,
    ISP_LDC,
    ISP_AF,
};

unsigned int mediactl_get_isp_modules(enum isp_pipeline_e pipeline,enum isp_modules module);
```

Gets the enable status of each module of the ISP.

#### parameter

```text
parameter:
isp_pipeline_e: more details see notes in mediactl_set_ae
isp_modules:
  ISP_TPG --  Test Pattern Control moudel
  ISP_BLC --  Black Level Correction moudel
  ISP_LSC --  Lens Shading Correction moudel
  ISP_AE --  AUTO Exposure Gain moudel
  ISP_AWB -- AUTO white balance moudel
  ISP_AWB_D65 -- AUTO white balance d65 moudel
  ISP_AWB_CCM -- AUTO white balance ccm moudel
  ISP_WDR --  wide dynamic range moudel
  ISP_RGB_GAMMA -- rgb gamma moudel
  ISP_YUV_GAMMA -- yuv gamma moudel
  ISP_ADA --  Adaptive dynamic range adjust moudel
  ISP_ADA_SBZ -- Image stabilization moudel
  ISP_ADA_CCR -- Color correction moudel
  ISP_RGBIR -- rgbir rectify moudel
  ISP_RAW_2DNR -- raw domain 2DNR moudel
  ISP_YUV_Y_2DNR -- yuv domain 2D YNR moudel
  ISP_YUV_UV_2DNR -- yuv domain 2D uvNR moudel
  ISP_3DNR --  yuv domain 3DNR moudel
  ISP_LTM --  local tone mapping moudel
  ISP_SHARP -- sharpness moudel
  ISP_CC --  color correction moudel
  ISP_CTRST -- contrast adjust moudel
  ISP_LUMA --  luma adjust moudel
  ISP_SATURATION -- saturation adjust  moudel
  ISP_LDC -- lens Distortion Correction moudel
  ISP_AF -- ATUO FOCUS moudel
```

#### The return value

```text
0 -- moudel disable  1 -- moudel enable
```

# 2 Demo app

## 2.1 v4l2_drm

The program is placed`/app/mediactl_lib` in the directory:

- `v4l2_drm.out`:v4l2 and drm linkage case, added -f to modify the name of the input configuration file, -e to open the isp ae function. You can use -h to view help.

Run v4l2_drm.out

- -e:0 turns off all aes, 1 turns on f-2k ae, 2 turns on r-2k ae, and 3 turns on all aes. By default, you can leave -e to turn off all aes.
- -x:0 switch to sw ae provided by lib3actl, 1 switch to hardware AE. By default, you can not specify -x, will use sw ae.
- -a:0 disable antiflicker correction, 1 enable f-2k 50Hz correction, 2 enable r-2k correction, 3 enable all antiflicker 50Hz correction. By default, you can not specify -a, will enable f2k/r2k 50Hz correction functions.
- -l:0 disable the ISP adaptive calculation function provided by libadaptive.so, 1 ISP adaptive calculation function provided by libadaptive.so. By default, you can not specify -l, will enable the ISP adaptive computing function provided by libadaptive.so.
- The demo requires the video configuration file and the corresponding sensor configuration file to be in the current directory.
- The demo can demonstrate single and double cameras by changing the configuration file.
- The demo demo single-camera full screen: ./v4l2_drm.out -e 1 -f video_drm_1080x1920.conf
- The demo demo dual camera: ./v4l2_drm.out -f video_drm_1920x1080.conf
- The demo must ensure that three profiles video_drm_1920x1080.conf, imx219_0.conf, and imx219_1.conf exist

**Translation Disclaimer**
For the convenience of customers, Canaan uses an AI translator to translate text into multiple languages, which may contain errors. We do not guarantee the accuracy, reliability or timeliness of the translations provided. Canaan shall not be liable for any loss or damage caused by reliance on the accuracy or reliability of the translated information. If there is a content difference between the translations in different languages, the Chinese Simplified version shall prevail.

If you would like to report a translation error or inaccuracy, please feel free to contact us by mail.
