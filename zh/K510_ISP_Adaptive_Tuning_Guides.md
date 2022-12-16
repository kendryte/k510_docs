![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 ISP Adaptive Tuning's Guide</font>**

<font face="黑体"  size=3>文档版本：V1.0.0</font>

<font face="黑体"  size=3>发布日期：2022-12-16</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**免责声明**</font>
您购买的产品、服务或特性等应受北京嘉楠捷思信息技术有限公司（“本公司”，下同）商业合同和条款的约束，本文档中描述的全部或部分产品、服务或特性可能不在您的购买或使用范围之内。除非合同另有约定，本公司不对本文档的任何陈述、信息、内容的准确性、可靠性、完整性、营销型、特定目的性和非侵略性提供任何明示或默示的声明或保证。除非另有约定，本文档仅作为使用指导的参考。
由于产品版本升级或其他原因，本文档内容将可能在未经任何通知的情况下，不定期进行更新或修改。

**<font face="黑体"  size=3>商标声明</font>**

“<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />”、“Canaan”图标、嘉楠和嘉楠其他商标均为北京嘉楠捷思信息技术有限公司的商标。本文档可能提及的其他所有商标或注册商标，由各自的所有人拥有。

**<font face="黑体"  size=3>版权所有©2022北京嘉楠捷思信息技术有限公司</font>**
本文档仅适用K510平台开发设计，非经本公司书面许可，任何单位和个人不得以任何形式对本文档的部分或全部内容传播。

**<font face="黑体"  size=3>北京嘉楠捷思信息技术有限公司</font>**
网址：canaan-creative.com
商务垂询：salesAI@canaan-creative.com

<div style="page-break-after:always"></div>

# 前言

**<font face="黑体"  size=5>文档目的</font>**

本文档为K510 ISP Adaptive Tuning参数说明文档。

**<font face="黑体"  size=5>读者对象</font>**

本文档（本指南）主要适用的人员：

- 图像调试人员

**<font face="黑体"  size=5>修订记录</font>**

<font face="宋体"  size=2>修订记录累积了每次文档更新的说明。最新版本的文档包含以前所有版本的更新内容。</font>

| 版本号   | 修改者     | 修订日期 | 修订说明 |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | 系统软件部 | 2022-12-16 | SDK V1.9发布 |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>

**<font face="黑体"  size=6>目 录</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 添加调试参数

## 1.1 调试参数说明

`#include "sensor_params/imx219/adaptive_imx219_f2k.h"`

### ◆ adap_imx219_f2k

```c
typedef struct {
    float nFps;
    ADAPTIVE_ISP_AE_PARAM_T tAeParam;
    ADAPTIVE_ISP_AE_GAIN_PARAM_T tAeGainParam;
    ADAPTIVE_ISP_BLC_PARAM_T tBlcParam;
    ADAPTIVE_ISP_LSC_PARAM_T tLscParam;
    ADAPTIVE_ISP_SHARPNESS_PARAM_T tSharpnessParam;
    ADAPTIVE_ISP_LTM_PARAM_T tLtm_param;
    ADAPTIVE_ISP_2D_DENOISE_PARAM_T tNr2dParam;
    ADAPTIVE_ISP_3D_DENOISE_PARAM_T tNr3dParam;
    ADAPTIVE_ISP_WDR_PARAM_T tWdrParam;
    ADAPTIVE_ISP_CCM_PARAM_T tCcmParam;
    ADAPTIVE_ISP_AWB_PARAM_T tAwbParam;
    ADAPTIVE_ISP_GAMMA_PARAM_T tGammaParam;
    ADAPTIVE_ISP_IR_CUT_PARAM_T tIrCutParam; // TBD
    ADAPTIVE_ISP_POST_SATURATION_PARAM_T tSaturationParam;
    ADAPTIVE_ISP_COLOR_GREY_SWITCH_PARAM_T tColorGreySwitchParam;
    ADAPTIVE_ISP_ADA_PARAM_T tAdaParam;
} ADAPTIVE_ISP_PIPELINE_PARAM_T;
```

#### 成员

```c
float nFps: 当前设备使用的帧率
ADAPTIVE_ISP_AE_PARAM_T tAeParam: AE曝光时间范围、目标值和调整分段
ADAPTIVE_ISP_AE_GAIN_PARAM_T tAeGainParam: AE增益调整范围和调整分段
ADAPTIVE_ISP_BLC_PARAM_T tBlcParam: 多组黑电平参数，对应AE增益分段
ADAPTIVE_ISP_LSC_PARAM_T tLscParam: 多组镜头渐晕矫正参数，对应AE增益分段
ADAPTIVE_ISP_SHARPNESS_PARAM_T tSharpnessParam: 多组锐度参数，对应AE增益分段
ADAPTIVE_ISP_LTM_PARAM_T tLtm_param: 多组局部色调映射参数，对应AE增益分段
ADAPTIVE_ISP_2D_DENOISE_PARAM_T tNr2dParam: 多组2d降噪参数，对应AE增益分段
ADAPTIVE_ISP_3D_DENOISE_PARAM_T tNr3dParam: 多组3dnr降噪参数，对应AE增益分段
ADAPTIVE_ISP_WDR_PARAM_T tWdrParam: 多组硬件WDR参数，对应AE增益分段，目前不可用
ADAPTIVE_ISP_CCM_PARAM_T tCcmParam: 多组CCM矩阵，对应不同的标定色温
ADAPTIVE_ISP_AWB_PARAM_T tAwbParam: 多组AWB范围限制参数，对应AE增益分段
ADAPTIVE_ISP_GAMMA_PARAM_T tGammaParam: 白天和夜晚共两组gamma曲线，对应不同的曝光量，
ADAPTIVE_ISP_IR_CUT_PARAM_T tIrCutParam: 控制IR CUT切换，对应曝光量切换日片和夜片
ADAPTIVE_ISP_POST_SATURATION_PARAM_T tSaturationParam: 多组饱和度参数，对应AE增益分段
ADAPTIVE_ISP_COLOR_GREY_SWITCH_PARAM_T tColorGreySwitchParam: 彩色模式和黑白模式，对应不同的曝光量，默认关闭
ADAPTIVE_ISP_ADA_PARAM_T tAdaParam: 多组ada参数，在曝光量达到AE增益和曝光时间上限后，根据target的下降进行分段控制
```

#### tAeParam

```c
typedef struct {
    int nAeYTarget;
    int nAeYTargetRange;
} _AE_CTL_PARAM_T;

typedef struct {
    int nExposureTime;      /* 0 - 40000 us */
    int nExposureGain;      /* 256 - 8192; 1x is 256 */
    _AE_CTL_PARAM_T tAeCtlParam;
} ISP_AE_PARAM_T;

typedef struct {
    unsigned short nAdaptiveEnable;    /* 0: disable 1: enable */
    int nAntiFlickerSelect; /* 0: Anti_Flicker_None; 1: Anti_Flicker_50Hz; 2: Anti_Flicker_60Hz */
    ISP_AE_PARAM_T tAeParam[ADAPTIVE_AE_ROUTE_STEPS];
} ADAPTIVE_ISP_AE_PARAM_T;

nAdaptiveEnable: 0 disable， 1 enable，控制此模块是否参与adaptive的控制
nAntiFlickerSelect: 此功能已经由sw ae接管，此处控制无效
nExposureTime: 微秒， 当前一组参数的曝光时间
nExposureGain: 倍数x256，256-4095（1*256-16*256） 当前一组参数的增益
nAeYTarget: 0-255， 当前一组参数对应需要控制的亮度目标值
nAeYTargetRange: 0-255， 当前一组参数对应需要控制的亮度目标误差
tAeParam[ADAPTIVE_AE_ROUTE_STEPS]: 五组曝光参数，当实际曝光参数达到其中某一组的nExposureTime和nExposureGain时，将使用该组的tAeCtlParam进行ISP控制
```

#### tAeGainParam

```c
/* Gain Range */

typedef struct {
    int nGain[ADAPTIVE_GAIN_ROUTE_STEPS];
} ADAPTIVE_ISP_AE_GAIN_PARAM_T;

nGain[ADAPTIVE_GAIN_ROUTE_STEPS]: 5组AE增益值，其他依赖AE增益模块的分段将根据此结构体选择，实际增益达到某一个gain值的时候，会控制其他模块使用该索引对应的控制参数。
```

#### tBlcParam

```c
/*
* BLC
* follow ae gain
*/

typedef struct {
    unsigned short nOffset;            /* default 220 */
} _BLC_CTL_PARAM_T;

typedef struct {
    unsigned short nAdaptiveEnable;    /* 0: disable 1: enable */
    _BLC_CTL_PARAM_T tBlcCtlParam[ADAPTIVE_GAIN_ROUTE_STEPS];
} ADAPTIVE_ISP_BLC_PARAM_T;

控制不同曝光增益下黑电平值
nAdaptiveEnable： 0 disable， 1 enable，控制此模块是否参与adaptive的控制
nOffset: 0-4095， 黑电平值，用于写寄存器
tBlcCtlParam[ADAPTIVE_GAIN_ROUTE_STEPS]: 共五组，通过AE增益提供的索引，取对应的控制参数控制ISP
```

#### tLscParam

```c
/*
* LSC
* follow ae gain
*/

typedef struct {
    unsigned short nLscRedRatio;
    unsigned short nLscGreenRatio;
    unsigned short nLscBlueRatio;
} _LSC_CTL_PARAM_T;

typedef struct {
    unsigned short nAdaptiveEnable;    /* 0: disable 1: enable */
    _LSC_CTL_PARAM_T tLscCtlParam[ADAPTIVE_GAIN_ROUTE_STEPS];
} ADAPTIVE_ISP_LSC_PARAM_T;

控制不同曝光增益下镜头渐晕的效果
nAdaptiveEnable： 0 disable， 1 enable，控制此模块是否参与adaptive的控制
nLscRedRatio、nLscGreenRatio、nLscBlueRatio: 0-511，一组控制参数，三通道的增益
tLscCtlParam[ADAPTIVE_GAIN_ROUTE_STEPS]: 共五组，通过AE增益提供的索引，取对应的控制参数控制ISP
```

#### tSharpnessParam

```c
/*
* SHARPNESS
* follow ae gain
*/

typedef struct {
    unsigned short nSharpnessCore;
    unsigned short nSharpnessThres[2]; /* [0]: threshold0 [1]: threshold1 */
    unsigned short nSharpnessGain;
} _SHARPNESS_CTL_PARAM_T;

typedef struct {
    unsigned short nAdaptiveEnable;    /* 0: disable 1: enable */
    _SHARPNESS_CTL_PARAM_T tSharpnessCtlParam[ADAPTIVE_GAIN_ROUTE_STEPS];
} ADAPTIVE_ISP_SHARPNESS_PARAM_T;

控制不同曝光增益下锐化强度
nSharpnessCore: 0-255
nSharpnessThres: 0-4095, [0]必须小于[1]
nSharpnessGain: 0-255
nAdaptiveEnable： 0 disable， 1 enable，控制此模块是否参与adaptive的控制
tSharpnessCtlParam[ADAPTIVE_GAIN_ROUTE_STEPS]: 共五组，通过AE增益提供的索引，取对应的控制参数控制ISP

```

#### tLtm_param

```c
/*
* LTM
* follow ae gain
*/

typedef struct {
    unsigned short nLtmGain;
    unsigned short nLtmThres;
} _LTM_CTL_PARAM_T;

typedef struct {
    unsigned short nAdaptiveEnable;    /* 0: disable 1: enable */
    _LTM_CTL_PARAM_T tLtmCtlParam[ADAPTIVE_GAIN_ROUTE_STEPS];
} ADAPTIVE_ISP_LTM_PARAM_T;

控制不同曝光增益下局部色调映射的值
nAdaptiveEnable： 0 disable， 1 enable，控制此模块是否参与adaptive的控制
nLtmGain: 0-255
nLtmThres: 0-255
tLtmCtlParam[ADAPTIVE_GAIN_ROUTE_STEPS]: 共五组，通过AE增益提供的索引，取对应的控制参数控制ISP
```

#### tNr2dParam

```c
/*
* 2D NR
* follow ae gain
*/

typedef struct {
    unsigned short nRawDomainIntensity;
    unsigned short n2dAdjacentPixIntensity;
    unsigned short n2dEdgeIntensity;
    unsigned short n2dLumaIntensit;
    unsigned short n2dChromaIntensity;
} _2D_DENOISE_CTL_PARAM_T;

typedef struct {
    unsigned short nAdaptiveEnable;    /* 0: disable 1: enable */
    _2D_DENOISE_CTL_PARAM_T t2dNoiseCtlParam[ADAPTIVE_GAIN_ROUTE_STEPS];
} ADAPTIVE_ISP_2D_DENOISE_PARAM_T;

控制不同曝光增益下2d降噪强度
nAdaptiveEnable： 0 disable， 1 enable，控制此模块是否参与adaptive的控制
nRawDomainIntensity: 0-255
n2dAdjacentPixIntensity: 0-511
n2dEdgeIntensity: 0-1023
n2dLumaIntensit: 0-255
n2dChromaIntensity: 0-255
t2dNoiseCtlParam[ADAPTIVE_GAIN_ROUTE_STEPS]: 共五组，通过AE增益提供的索引，取对应的控制参数控制ISP
```

#### tNr3dParam

```c
/*
* 3D NR
* follow ae gain
*/

typedef struct {
    unsigned short nPre3dLumaThres;   /* dp thy */
    unsigned short nPre3dLumaIntensity;     /* dp thyp */
    unsigned short nPre3dChromaIntensity;    /* dp thcp */
    unsigned short nMain3dMiddleFilterThres; /*  */
    unsigned short nMain3dPrevFrameMidFilter;
    unsigned short nMain3dCurFrameMidFilterThres;
    unsigned short nMain3dLowPassFilterVal;
    unsigned short nMain3dLumaThres;
    unsigned short nMain3dMinimumVal;
    unsigned short nMain3dLumaIntensity; /* dm thyp */
    unsigned short nMain3dChromaIntensity; /* dm thcp */
    unsigned short nPost3dEdgeThreshold; /* db theg */
    unsigned short nPost3dLumaIntensity; /* db thyp */
    unsigned short nPost3dChromaIntensity; /* db thcp */
} _3D_DENOISE_CTL_PARAM_T;

typedef struct {
    unsigned short nAdaptiveEnable;    /* 0: disable 1: enable */
    _3D_DENOISE_CTL_PARAM_T t3dNoiseCtlParam[ADAPTIVE_GAIN_ROUTE_STEPS];
} ADAPTIVE_ISP_3D_DENOISE_PARAM_T;

控制不同曝光增益下3d降噪强度
nPre3dLumaThres: 0-255
nPre3dLumaIntensity: 0-255
nPre3dChromaIntensity: 0-255
nMain3dMiddleFilterThres: 0-255
nMain3dPrevFrameMidFilter: 0-255
nMain3dCurFrameMidFilterThres: 0-255
nMain3dLowPassFilterVal: 0-255
nMain3dLumaThres: 0-255
nMain3dMinimumVal: 0-255
nMain3dLumaIntensity: 0-255
nMain3dChromaIntensity: 0-255
nPost3dEdgeThreshold: 0-255
nPost3dLumaIntensity: 0-255
nPost3dChromaIntensity: 0-255
nAdaptiveEnable： 0 disable， 1 enable，控制此模块是否参与adaptive的控制
t2dNoiseCtlParam[ADAPTIVE_GAIN_ROUTE_STEPS]: 共五组，通过AE增益提供的索引，取对应的控制参数控制ISP
```

#### tWdrParam

```c
/*
* WDR
* follow ae gain
*/

typedef struct {
    unsigned short nLghtTh[2]; /* Threshold of overexposure ratio [0] used for 3 frames mode; [1] used for 2 frames mode */
    unsigned short nFsTh; /* threshold of WDR fusion */
    unsigned short nFsK[2]; /* WDR image fusion handle value; [0] used for 3 frames mode; [1] used for 2 frames mode */
} _WDR_CTL_PARAM_T;

typedef struct {
    unsigned short nAdaptiveEnable;    /* 0: disable 1: enable */
    _WDR_CTL_PARAM_T tWdrCtlParam[ADAPTIVE_GAIN_ROUTE_STEPS];
} ADAPTIVE_ISP_WDR_PARAM_T;

该模块暂时无效
```

#### tCcmParam

```c
/*
* CCM
* follow awb gain
*/

typedef struct {
    int nCtCcm[3][3]; /* [0][0]: Rr [0][1]: Rg [0][2]: Rb; [1][0]: Gr [1][1]: Gg [1][2]: Gb; [2][0]: Br [2][0]: Bg [2][0]: Bb*/
} _CCM_CTL_PARAM_T;

typedef struct {
    unsigned short nRGain;
    unsigned short nBGain;
    _CCM_CTL_PARAM_T tCcmCtlParam;
} ISP_CCM_PARAM_T;

typedef struct {
    unsigned short nAdaptiveEnable;    /* 0: disable 1: enable */
    ISP_CCM_PARAM_T tCcmParam[ADAPTIVE_CCM_TEMPERATURE_NUM];
} ADAPTIVE_ISP_CCM_PARAM_T;

不同色温下切换CCM
nAdaptiveEnable： 0 disable， 1 enable，控制此模块是否参与adaptive的控制
nCtCcm: 0-511
nRGain、nBGain: 0-1023, 该组参数对应的wb rgain和bgain，
tCcmParam[ADAPTIVE_CCM_TEMPERATURE_NUM]: 当实际rgain和bgain的距离该组值最近时，对应的控制参数控制ISP，下发该组CCM矩阵
```

#### tAwbParam

```c
/*
* AWB
* follow ae
*/

typedef struct {
    unsigned short nRGain[2]; /* [0]: Min; [1]: Max */
    unsigned short nBGain[2]; /* [0]: Min; [1]: Max */
} _AWB_CTL_PARAM_T;

typedef struct {
    unsigned short nAdaptiveEnable;    /* 0: disable 1: enable */
    _AWB_CTL_PARAM_T tAwbCtlParam[ADAPTIVE_AE_ROUTE_STEPS];
} ADAPTIVE_ISP_AWB_PARAM_T;

限制不同环境光下的AWB范围，避免颜色不准确或者较大偏差
nAdaptiveEnable： 0 disable， 1 enable，控制此模块是否参与adaptive的控制
nRGain: 0-1023，控制参数，[0] rgain min， [1] rgain max
nBGain: 0-1023，控制参数，[0] bgain min， [1] bgain max
tAwbCtlParam[ADAPTIVE_AE_ROUTE_STEPS]: 五组参数，当实际曝光量达到某一区间时，使用AE曝光时间的索引对应的该组控制参数
```

#### tGammaParam

```c
/*
* GAMMA
* follow ae gain & exposure
*/

typedef struct {
    unsigned short nGammaCurve[ADAPTIVE_GAMMA_CURVE_INDEX_NUM];
} _GAMMA_CTL_PARAM_T;

typedef struct {
    int nEtGamma;
    int nGainGamma;
    _GAMMA_CTL_PARAM_T tGammaCtlParam;
} ISP_GAMMA_PARAM_T;

typedef struct {
    unsigned short nAdaptiveEnable;    /* 0: disable 1: enable */
    ISP_GAMMA_PARAM_T tGammaParam[ADAPTIVE_GAMMA_ROUTE_STEPS];
} ADAPTIVE_ISP_GAMMA_PARAM_T;

控制白天和夜晚的gamma曲线
nAdaptiveEnable: 0 disable， 1 enable，控制此模块是否参与adaptive的控制
nEtGamma、nGainGamma: 需要达到该组控制条件的曝光时间（行数）和曝光增益，内部使用两个值的乘积
tGammaParam[ADAPTIVE_GAMMA_ROUTE_STEPS]: 两组控制参数，当曝光量小于第一组的et和gain的乘积时，将启用第一组，大于第二组的et和gain的乘积时将启用第二组控制
nGammaCurve[ADAPTIVE_GAMMA_CURVE_INDEX_NUM]: 256点gamma曲线
```

#### tIrCutParam

```c
/*
* IR CUT
* follow ae gain & exposure
* callback from user
*/

typedef struct {
    unsigned short nHoldTime;
    unsigned short nIrCutMode;
} _IR_CUT_CTL_PARAM;

typedef struct {
    unsigned short nExposureTime;
    unsigned short nGain;
    _IR_CUT_CTL_PARAM tIrCutCtlParam;
    int nIrCutCtlMode; // ir cut auto/manual ctl mode 0 / 1
} ISP_IR_CUT_PARAM_T;

typedef struct {
    unsigned short nAutoSwitchEnable;    /* 0: disable 1: enable */
    ISP_IR_CUT_PARAM_T tIrCutParam[ADAPTIVE_IR_CUT_MODE_NUM];
} ADAPTIVE_ISP_IR_CUT_PARAM_T;

IR CUT切换模式控制
nAutoSwitchEnable: 0 disable， 1 enable，控制此模块是否参与adaptive的控制
nExposureTime、nGain: 达到切换条件的曝光时间和增益，内部使用两个值的乘积
nIrCutCtlMode: 控制IRCUT自动/手动切换，0 手动模式， 1 自动模式
nHoldTime: 曝光量达某一组值的持续时间（帧数），超过该时间才被判定需要切换
nIrCutMode: 0 夜片， 1 日片
```

#### tSaturationParam

```c
/*
* POST SATURATION
* follow ae gain
* need calc real saturation
*/

typedef struct {
    unsigned short nSaturationCoeff;
} _POST_SATURATION_CTL_PARAM_T;

typedef struct {
    unsigned short nAdaptiveEnable;    /* 0: disable 1: enable */
    _POST_SATURATION_CTL_PARAM_T tPostSaturationCtlParam[ADAPTIVE_GAIN_ROUTE_STEPS];
} ADAPTIVE_ISP_POST_SATURATION_PARAM_T;

饱和度升降控制
nAdaptiveEnable: 0 disable， 1 enable，控制此模块是否参与adaptive的控制
nSaturationCoeff: 0-100（0%-100%），饱和度倍数系数，将按照默认最大饱和度进行百分比进行设置，100则饱和度为最大值，50则饱和度为最大值的一半
tPostSaturationCtlParam[ADAPTIVE_GAIN_ROUTE_STEPS]: 共五组，通过AE增益提供的索引，取对应的控制参数控制ISP
```

#### tColorGreySwitchParam

```c
/*
* COLOR BLACK WHITE MODE
* follow ae gain
*/

typedef struct {
    unsigned short nSaturation;
} _COLOR_GREY_CTL_PARAM;

typedef struct {
    int nExposureTime;
    int nGain;
    _COLOR_GREY_CTL_PARAM tColorGreyCsmCtlParam;
} ISP_COLOR_GREY_SWITCH_PARAM_T;

typedef struct {
    unsigned short nAutoSwitchEnable;    /* 0: disable 1: saturation convert mode */
    ISP_COLOR_GREY_SWITCH_PARAM_T tColorGreySwitchParam[ADAPTIVE_COLOR_GREY_SWITCH_MODE_NUM];
} ADAPTIVE_ISP_COLOR_GREY_SWITCH_PARAM_T;

控制彩色黑白转换模式
nAutoSwitchEnable: 0 disable， 1 enable，控制此模块是否参与adaptive的控制，不需要切黑白模式时，默认置为0
nExposureTime、nGain: 该组的曝光时间和增益条件，内部使用两值的乘积
tColorGreySwitchParam[ADAPTIVE_COLOR_GREY_SWITCH_MODE_NUM]: 两组参数，[0]为黑白模式参数，[1]为彩色模式参数，彩色模式已经由饱和度控制模块代替。当曝光量大于第一组参数的曝光乘积时，将使用第一组的控制参数控制ISP
```

#### tAdaParam

```c
/*
* ADA
* follow ae TO_CPU_Y_AV(gain & et max ae lock)
*/

typedef struct {
    unsigned short nAdaHistMax;
    unsigned short nAdaTtlMax;
} _ADA_CTL_PARAM;

typedef struct {
    unsigned short nAeYEverage;
    _ADA_CTL_PARAM tAdaCtlParam;
} ISP_ADA_PARAM_T;

typedef struct {
    unsigned short nAdaptiveEnable;
    ISP_ADA_PARAM_T tAdaParam[ADAPTIVE_ADA_ROUTE_STEPS];
} ADAPTIVE_ISP_ADA_PARAM_T;

控制提升暗光环境下的亮度和对比度
nAdaptiveEnable: 0 disable， 1 enable，控制此模块是否参与adaptive的控制
nAeYEverage: 环境亮度条件值，当曝光量大等于tAeCtlParam最后一组曝光时间与gain的乘积后，该值生效
tAdaParam[ADAPTIVE_ADA_ROUTE_STEPS]: 五组参数，曝光达到最后一档，根据环境亮度条件，下发ada控制参数
```

#### 示例imx219 f2k参数

```c
static ADAPTIVE_ISP_PIPELINE_PARAM_T adap_imx219_f2k =

{
    /* fps */
    30,
    {
    /* AE Parameters */

    // static ADAPTIVE_ISP_AE_PARAM_T ae_param = {
        /* nAdaptiveEnable */
        1,
        /* nAntiFlickerSelect */
        0, //0: disable 1: 50Hz 2: 60Hz
        /* tAeParam */
        {
            /* 0 */
            {
                /* nExposureTime */
                280, // 6000lux
                /* nExposureGain */
                512,
                /* ae ctl */
                {
                    /* nAeYTarget */
                    100,
                    /* nAeYTargetRange */
                    14,
                },
            },
            /* 1 */
            {
                /* nExposureTime */
                2630, // 2500lux
                /* nExposureGain */
                512,
                /* ae ctl */
                {
                    /* nAeYTarget */
                    100,
                    /* nAeYTargetRange */
                    14,
                },
            },
            /* 2 */
            {
                /* nExposureTime */
                12108, // 400lux
                /* nExposureGain */
                512,
                /* ae ctl */
                {
                    /* nAeYTarget */
                    90,
                    /* AE_YTarget_Range */
                    13,
                },
            },
            /* 3 */
            {
                /* nExposureTime */
                33333, // 100lux
                /* nExposureGain */
                1024,
                {
                    /* nAeYTarget */
                    80,
                    /* AE_YTarget_Range */
                    11,
                },
            },
            /* 4 */
            {
                /* nExposureTime */
                33333,
                /* nExposureGain */
                4095,
                {
                    /* nAeYTarget */
                    72,
                    /* AE_YTarget_Range */
                    10,
                },
            },
        },
    // };
    },

    /* AE gain */

    {
        {256, 768, 1024, 2048, 4095},
    },

    {
    /* BLC Parameters */

    // static ADAPTIVE_ISP_BLC_PARAM_T blc_param = {
        /* nAdaptiveEnable */
        1,
        /* blc param */
        {
            /* 0 */
            {240},
            /* 1 */
            {240},
            /* 2 */
            {224},
            /* 3 */
            {224},
            /* 4 */
            {224},
        },
    // };
    },

    {
    /* LSC Parameters */

    // static ADAPTIVE_ISP_LSC_PARAM_T lsc_param = {
        /* nAdaptiveEnable */
        1,
        /* lsc param */
        {
            /* 0 */
            {
                /* nLscRedRatio */
                10,
                /* nLscGreenRatio */
                6,
                /* nLscBlueRatio */
                6,
            },
            /* 1 */
            {
                /* nLscRedRatio */
                10,
                /* nLscGreenRatio */
                6,
                /* nLscBlueRatio */
                6,
            },
            /* 2 */
            {
                /* nLscRedRatio */
                10,
                /* nLscGreenRatio */
                6,
                /* nLscBlueRatio */
                6,
            },
            /* 3 */
            {
                /* nLscRedRatio */
                10,
                /* nLscGreenRatio */
                6,
                /* nLscBlueRatio */
                6,
            },
            /* 4 */
            {
                /* nLscRedRatio */
                10,
                /* nLscGreenRatio */
                6,
                /* nLscBlueRatio */
                6,
            },
        },
    // };
    },

    {
    /* SHARPNESS Parameters */

    // static ADAPTIVE_ISP_SHARPNESS_PARAM_T sharpness_param = {
        /* nAdaptiveEnable */
        1,
        /* sharpness param */
        {
            /* 0 */
            {
                /* nSharpnessCore */
                4,
                /* nSharpnessThres[2]; [0]: thres1 [1]: thres2 */
                {3840, 4095},
                /* nSharpnessGain */
                64,
            },
            /* 1 */
            {
                /* nSharpnessCore */
                4,
                /* nSharpnessThres[2]; [0]: thres1 [1]: thres2 */
                {3840, 4095},
                /* nSharpnessGain */
                64,
            },
            /* 2 */
            {
                /* nSharpnessCore */
                8,
                /* nSharpnessThres[2]; [0]: thres1 [1]: thres2 */
                {3840, 4095},
                /* nSharpnessGain */
                56,
            },
            /* 3 */
            {
                /* nSharpnessCore */
                8,
                /* nSharpnessThres[2]; [0]: thres1 [1]: thres2 */
                {3840, 4095},
                /* nSharpnessGain */
                48,
            },
            /* 4 */
            {
                /* nSharpnessCore */
                8,
                /* nSharpnessThres[2]; [0]: thres1 [1]: thres2 */
                {3840, 4095},
                /* nSharpnessGain */
                40,
            },
        },
    // };
    },

    {
    /* LTM Parameters */

    // static ADAPTIVE_ISP_LTM_PARAM_T ltm_param = {
        /* nAdaptiveEnable */
        1,
        {
            /* 0 */
            {
                /* nLtmGain */
                128,
                /* nLtmThres */
                128,
            },
            /* 1 */
            {
                /* nLtmGain */
                128,
                /* nLtmThres */
                128,
            },
            /* 2 */
            {
                /* nLtmGain */
                128,
                /* nLtmThres */
                128,
            },
            /* 3 */
            {
                /* nLtmGain */
                100,
                /* nLtmThres */
                128,
            },
            /* 4 */
            {
                /* nLtmGain */
                80,
                /* nLtmThres */
                128,
            },
        },
    // };
    },

    {
    /* 2D NR Parameters */

    // static ADAPTIVE_ISP_2D_DENOISE_PARAM_T nr2d_param = {
        /* nAdaptiveEnable */
        1,
        /* 2dnr */
        {
            /* 0 */
            {
                /* nRawDomainIntensity */
                16,
                /* n2dAdjacentPixIntensity */
                128,
                /* n2dEdgeIntensity */
                32,
                /* n2dLumaIntensity */
                32,
                /* n2dChromaIntensity */
                1,
            },
            /* 1 */
            {
                /* nRawDomainIntensity */
                16,
                /* n2dAdjacentPixIntensity */
                128,
                /* n2dEdgeIntensity */
                32,
                /* n2dLumaIntensit */
                32,
                /* n2dChromaIntensity */
                1,
            },
            /* 2 */
            {
                /* nRawDomainIntensity */
                16,
                /* n2dAdjacentPixIntensity */
                128,
                /* n2dEdgeIntensity */
                40,
                /* n2dLumaIntensit */
                48,
                /* n2dChromaIntensity */
                160,
            },
            /* 3 */
            {
                /* nRawDomainIntensity */
                16,
                /* n2dAdjacentPixIntensity */
                511,
                /* n2dEdgeIntensity */
                48,
                /* n2dLumaIntensit */
                64,
                /* n2dChromaIntensity */
                255,
            },
            /* 4 */
            {
                /* nRawDomainIntensity */
                16,
                /* n2dAdjacentPixIntensity */
                511,
                /* n2dEdgeIntensity */
                48,
                /* n2dLumaIntensit */
                64,
                /* n2dChromaIntensity */
                255,
            },
        },
    // };
    },

    {
    /* 3D NR Parameters */

    // static ADAPTIVE_ISP_3D_DENOISE_PARAM_T nr3d_param = {
        /* nAdaptiveEnable */
        1,
        /* 3dnr */
        {
            /* 0 */
            {
                /* nPre3dLumaThres */
                64,
                /* nPre3dLumaIntensity */
                64,
                /* nPre3dChromaIntensity */
                64,
                /* nMain3dMiddleFilterThres */
                128,
                /* nMain3dPrevFrameMidFilter */
                8,
                /* nMain3dCurFrameMidFilterThres */
                128,
                /* nMain3dLowPassFilterVal */
                60,
                /* nMain3dLumaThres */
                64,
                /* nMain3dMinimumVal */
                1,
                /* nMain3dLumaIntensity */
                128,
                /* nMain3dChromaIntensity */
                16,
                /* nPost3dEdgeThreshold */
                64,
                /* nPost3dLumaIntensity */
                64,
                /* nPost3dChromaIntensity */
                32,
            },

            /* 1 */
            {
                /* nPre3dLumaThres */
                64,
                /* nPre3dLumaIntensity */
                64,
                /* nPre3dChromaIntensity */
                64,
                /* nMain3dMiddleFilterThres */
                128,
                /* nMain3dPrevFrameMidFilter */
                8,
                /* nMain3dCurFrameMidFilterThres */
                128,
                /* nMain3dLowPassFilterVal */
                60,
                /* nMain3dLumaThres */
                64,
                /* nMain3dMinimumVal */
                0,
                /* nMain3dLumaIntensity */
                128,
                /* nMain3dChromaIntensity */
                16,
                /* nPost3dEdgeThreshold */
                64,
                /* nPost3dLumaIntensity */
                64,
                /* nPost3dChromaIntensity */
                32,
            },

            /* 2 */
            {
                /* nPre3dLumaThres */
                64,
                /* nPre3dLumaIntensity */
                64,
                /* nPre3dChromaIntensity */
                64,
                /* nMain3dMiddleFilterThres */
                128,
                /* nMain3dPrevFrameMidFilter */
                8,
                /* nMain3dCurFrameMidFilterThres */
                128,
                /* nMain3dLowPassFilterVal */
                60,
                /* nMain3dLumaThres */
                64,
                /* nMain3dMinimumVal */
                0,
                /* nMain3dLumaIntensity */
                128,
                /* nMain3dChromaIntensity */
                16,
                /* nPost3dEdgeThreshold */
                64,
                /* nPost3dLumaIntensity */
                64,
                /* nPost3dChromaIntensity */
                32,
            },

            /* 3 */
            {
                /* nPre3dLumaThres */
                64,
                /* nPre3dLumaIntensity */
                64,
                /* nPre3dChromaIntensity */
                64,
                /* nMain3dMiddleFilterThres */
                128,
                /* nMain3dPrevFrameMidFilter */
                8,
                /* nMain3dCurFrameMidFilterThres */
                128,
                /* nMain3dLowPassFilterVal */
                60,
                /* nMain3dLumaThres */
                64,
                /* nMain3dMinimumVal */
                0,
                /* nMain3dLumaIntensity */
                128,
                /* nMain3dChromaIntensity */
                16,
                /* nPost3dEdgeThreshold */
                64,
                /* nPost3dLumaIntensity */
                64,
                /* nPost3dChromaIntensity */
                32,
            },

            /* 4 */
            {
                /* nPre3dLumaThres */
                64,
                /* nPre3dLumaIntensity */
                64,
                /* nPre3dChromaIntensity */
                64,
                /* nMain3dMiddleFilterThres */
                128,
                /* nMain3dPrevFrameMidFilter */
                8,
                /* nMain3dCurFrameMidFilterThres */
                128,
                /* nMain3dLowPassFilterVal */
                60,
                /* nMain3dLumaThres */
                64,
                /* nMain3dMinimumVal */
                0,
                /* nMain3dLumaIntensity */
                128,
                /* nMain3dChromaIntensity */
                16,
                /* nPost3dEdgeThreshold */
                64,
                /* nPost3dLumaIntensity */
                64,
                /* nPost3dChromaIntensity */
                32,
            },
        },
    // };
    },

    {
    /* WDR Parameters */

    // static ADAPTIVE_ISP_WDR_PARAM_T wdr_param = {
        /* nAdaptiveEnable */
        0,
        /* wdr param */
        {
            /* 0 */
            {
                /* nLghtTh[2] */
                {384, 32},
                /* nFsTh */
                192,
                /* nFsK */
                {0, 0},
            },
            /* 0 */
            {
                /* nLghtTh[2] */
                {384, 32},
                /* nFsTh */
                192,
                /* nFsK */
                {0, 0},
            },
            /* 2 */
            {
                /* nLghtTh[2] */
                {384, 32},
                /* nFsTh */
                192,
                /* nFsK */
                {0, 0},
            },
            /* 3 */
            {
                /* nLghtTh[2] */
                {384, 32},
                /* nFsTh */
                192,
                /* nFsK */
                {0, 0},
            },
            /* 4 */
            {
                /* nLghtTh[2] */
                {384, 32},
                /* nFsTh */
                192,
                /* nFsK */
                {0, 0},
            },
        },
    // };
    },

    {
    /* CCM Parameters */

    // static ADAPTIVE_ISP_CCM_PARAM_T ccm_param = {
        /* nAdaptiveEnable */
        1,
        /* tCcmParam */
        {
            /* A */
            {
                /* nRGain */
                162,
                /* nBGain */
                449,
                /* tCcmCtlParam */
                {
                    /* nCtCcm[3][3] */
                    {
                        {311, 49, 6},
                        {62, 343, 26},
                        {16, 142, 414},
                    },
                },
            },
            /* U30 */
            {
                /* nRGain */
                156,
                /* nBGain */
                458,
                /* tCcmCtlParam */
                {
                    /* nCtCcm[3][3] */
                    {
                        {299, 39, 5},
                        {56, 336, 24},
                        {13, 126, 395},
                    },
                },
            },
            /* U35 */
            {
                /* nRGain */
                176,
                /* nBGain */
                402,
                /* tCcmCtlParam */
                {
                    /* nCtCcm[3][3] */
                    {
                        {287, 28, 3},
                        {50, 328, 22},
                        {9, 111, 376},
                    },
                },
            },
            /* TL84 */
            {
                /* nRGain */
                194,
                /* nBGain */
                360,
                /* tCcmCtlParam */
                {
                    /* nCtCcm[3][3] */
                    {
                        {259, 2, 1},
                        {37, 310, 17},
                        {1, 75, 332},
                    },
                },
            },
            /* D50 */
            {
                /* nRGain */
                234,
                /* nBGain */
                299,
                /* tCcmCtlParam */
                {
                    /* nCtCcm[3][3] */
                    {
                        {277, 19, 3},
                        {45, 322, 20},
                        {6, 98, 360},
                    },
                },
            },
            /* D65 */
            {
                /* nRGain */
                257,
                /* nBGain */
                269,
                /* tCcmCtlParam */
                {
                    /* nCtCcm[3][3] */
                    {
                        {259, 2, 1},
                        {37, 310, 17},
                        {1, 75, 332},
                    },
                },
            },
        },
    // };
    },

    {
    /* AWB */

    // static ADAPTIVE_ISP_AWB_PARAM_T awb_param = {
        /* nAdaptiveEnable */
        1,
        /* awb param */
        {
            /* 0 */
            {
            /* nRGain[2]; [0]: Min [1]: Max */
            {194, 247},
            /* nBGain[2]; [0]: Min [1]: Max */
            {275, 360},
            },
            /* 1 */
            {
            /* nRGain[2]; [0]: Min [1]: Max */
            {194, 257},
            /* nBGain[2]; [0]: Min [1]: Max */
            {269, 360},
            },
            /* 2 */
            {
            /* nRGain[2]; [0]: Min [1]: Max */
            {162, 257},
            /* nBGain[2]; [0]: Min [1]: Max */
            {269, 449},
            },
            /* 3 */
            {
            /* nRGain[2]; [0]: Min [1]: Max */
            {194, 257},
            /* nBGain[2]; [0]: Min [1]: Max */
            {269, 360},
            },
            /* 4 */
            {
            /* nRGain[2]; [0]: Min [1]: Max */
            {194, 257},
            /* nBGain[2]; [0]: Min [1]: Max */
            {269, 360},
            },
        },
    // };
    },

    {

    /* GAMMA Parameters */

    // static ADAPTIVE_ISP_GAMMA_PARAM_T gamma_param = {
        /* nAdaptiveEnable */
        1, // if 1 affect ae stablization
        /* tGammaParam */
        {
            /* Day */
            {
                /* nEtGamma */
                33333,
                /* nGainGamma */
                512,
                /* tGammaCtlParam */
                {
                    /* nGammaCurve */
                    {
                        0x000, 0xC05, 0x80B, 0x411, 0xC16, 0x01C, 0x421, 0x426, 0x02B, 0x82F, 0xC33, 0xC37, 0x83B, 0x03F, 0x442, 0x445,
                        0x048, 0xC4A, 0x44D, 0xC4F, 0x052, 0x454, 0x856, 0x858, 0x85A, 0x85C, 0x85E, 0x860, 0x862, 0x864, 0x466, 0x068,
                        0xC69, 0x86B, 0x46D, 0x06F, 0xC70, 0x872, 0x074, 0x875, 0x077, 0x878, 0x07A, 0x87B, 0x07D, 0x87E, 0xC7F, 0x081,
                        0x482, 0x883, 0xC84, 0x086, 0x487, 0x888, 0xC89, 0x08B, 0x48C, 0x88D, 0x88E, 0x88F, 0x890, 0x891, 0x892, 0x893,
                        0x894, 0x895, 0x896, 0x897, 0x898, 0x899, 0x89A, 0x89B, 0x89C, 0x89D, 0x89E, 0x49F, 0x0A0, 0xCA0, 0x8A1, 0x4A2,
                        0x0A3, 0xCA3, 0x8A4, 0x4A5, 0x0A6, 0xCA6, 0x8A7, 0x4A8, 0x0A9, 0xCA9, 0x8AA, 0x4AB, 0x0AC, 0xCAC, 0x8AD, 0x4AE,
                        0x0AF, 0xCAF, 0x8B0, 0x4B1, 0x0B2, 0xCB2, 0x8B3, 0x4B4, 0x0B5, 0xCB5, 0x4B6, 0xCB6, 0x4B7, 0xCB7, 0x4B8, 0xCB8,
                        0x4B9, 0xCB9, 0x4BA, 0xCBA, 0x4BB, 0xCBB, 0x4BC, 0xCBC, 0x4BD, 0xCBD, 0x4BE, 0xCBE, 0x4BF, 0xCBF, 0x4C0, 0xCC0,
                        0x4C1, 0xCC1, 0x4C2, 0xCC2, 0x4C3, 0xCC3, 0x4C4, 0xCC4, 0x4C5, 0xCC5, 0x4C6, 0xCC6, 0x4C7, 0xCC7, 0x4C8, 0xCC8,
                        0x4C9, 0xCC9, 0x4CA, 0xCCA, 0x4CB, 0xCCB, 0x4CC, 0xCCC, 0x4CD, 0xCCD, 0x4CE, 0xCCE, 0x4CF, 0xCCF, 0x4D0, 0xCD0,
                        0x4D1, 0xCD1, 0x4D2, 0xCD2, 0x4D3, 0xCD3, 0x4D4, 0xCD4, 0x4D5, 0xCD5, 0x4D6, 0xCD6, 0x4D7, 0xCD7, 0x4D8, 0xCD8,
                        0x4D9, 0xCD9, 0x4DA, 0xCDA, 0x4DB, 0xCDB, 0x4DC, 0xCDC, 0x4DD, 0xCDD, 0x4DE, 0xCDE, 0x4DF, 0xCDF, 0x4E0, 0xCE0,
                        0x4E1, 0xCE1, 0x4E2, 0xCE2, 0x4E3, 0xCE3, 0x4E4, 0xCE4, 0x4E5, 0xCE5, 0x4E6, 0xCE6, 0x4E7, 0xCE7, 0x4E8, 0xCE8,
                        0x4E9, 0xCE9, 0x4EA, 0xCEA, 0x4EB, 0xCEB, 0x4EC, 0xCEC, 0x4ED, 0xCED, 0x4EE, 0xCEE, 0x4EF, 0xCEF, 0x4F0, 0xCF0,
                        0x4F1, 0xCF1, 0x4F2, 0xCF2, 0x4F3, 0xCF3, 0x4F4, 0xCF4, 0x4F5, 0xCF5, 0x4F6, 0xCF6, 0x4F7, 0xCF7, 0x4F8, 0xCF8,
                        0x4F9, 0xCF9, 0x4FA, 0xCFA, 0x4FB, 0xCFB, 0x4FC, 0xCFC, 0x4FD, 0xCFD, 0x4FE, 0xCFE, 0x0FF, 0x4FF, 0x8FF, 0xCFF,
                    },
                },
            },
            /* Night */
            {
                /* nEtGamma */
                33333,
                /* nGainGamma */
                3072,
                /* tGammaCtlParam */
                {
                    /* nGammaCurve */
                    {
                        0x001, 0x814, 0x41C, 0x022, 0xC26, 0xC2A, 0x82E, 0xC31, 0x035, 0xC37, 0x83A, 0x43D, 0xC3F, 0x042, 0x444, 0x846,
                        0x848, 0x84A, 0x84C, 0x84E, 0x450, 0x052, 0xC53, 0x855, 0x457, 0x059, 0x85A, 0x05C, 0x85D, 0x05F, 0x860, 0x062,
                        0x863, 0x065, 0x866, 0xC67, 0x069, 0x46A, 0x86B, 0xC6C, 0x06E, 0x46F, 0x870, 0xC71, 0x073, 0x474, 0x875, 0xC76,
                        0x078, 0x479, 0x47A, 0x47B, 0x47C, 0x47D, 0x47E, 0x47F, 0x480, 0x481, 0x482, 0x483, 0x484, 0x485, 0x486, 0x487,
                        0x488, 0x489, 0x48A, 0x48B, 0x48C, 0x48D, 0x48E, 0x48F, 0x490, 0x491, 0x492, 0x493, 0x494, 0x495, 0x496, 0x497,
                        0x098, 0xC98, 0x899, 0x49A, 0x09B, 0xC9B, 0x89C, 0x49D, 0x09E, 0xC9E, 0x89F, 0x4A0, 0x0A1, 0xCA1, 0x8A2, 0x4A3,
                        0x0A4, 0xCA4, 0x8A5, 0x4A6, 0x0A7, 0xCA7, 0x8A8, 0x4A9, 0x0AA, 0xCAA, 0x8AB, 0x4AC, 0x0AD, 0xCAD, 0x8AE, 0x4AF,
                        0x0B0, 0xCB0, 0x8B1, 0x4B2, 0x0B3, 0xCB3, 0x8B4, 0x4B5, 0x0B6, 0xCB6, 0x8B7, 0x4B8, 0x0B9, 0xCB9, 0x8BA, 0x4BB,
                        0x0BC, 0xCBC, 0x8BD, 0x4BE, 0x0BF, 0xCBF, 0x8C0, 0x4C1, 0x0C2, 0xCC2, 0x8C3, 0x4C4, 0x0C5, 0xCC5, 0x8C6, 0x4C7,
                        0x0C8, 0xCC8, 0x8C9, 0x4CA, 0x0CB, 0x8CB, 0x0CC, 0x8CC, 0x0CD, 0x8CD, 0x0CE, 0x8CE, 0x0CF, 0x8CF, 0x0D0, 0x8D0,
                        0x0D1, 0x8D1, 0x0D2, 0x8D2, 0x0D3, 0x8D3, 0x0D4, 0x8D4, 0x0D5, 0x8D5, 0x0D6, 0x8D6, 0x0D7, 0x8D7, 0x0D8, 0x8D8,
                        0x0D9, 0x8D9, 0x0DA, 0x8DA, 0x0DB, 0x8DB, 0x0DC, 0x8DC, 0x0DD, 0x8DD, 0x0DE, 0x8DE, 0x0DF, 0x8DF, 0x0E0, 0x8E0,
                        0x0E1, 0x8E1, 0x0E2, 0x8E2, 0x0E3, 0x8E3, 0x0E4, 0x8E4, 0x0E5, 0x8E5, 0x0E6, 0x8E6, 0x0E7, 0x8E7, 0x0E8, 0x8E8,
                        0x0E9, 0x8E9, 0x0EA, 0x8EA, 0x0EB, 0x8EB, 0x0EC, 0x8EC, 0x0ED, 0x8ED, 0x0EE, 0x8EE, 0x0EF, 0x8EF, 0x0F0, 0x8F0,
                        0x0F1, 0x8F1, 0x0F2, 0x8F2, 0x0F3, 0x8F3, 0x0F4, 0x8F4, 0x0F5, 0x8F5, 0x0F6, 0x8F6, 0x0F7, 0x8F7, 0x0F8, 0x8F8,
                        0x0F9, 0x8F9, 0x0FA, 0x8FA, 0x0FB, 0x8FB, 0x0FC, 0x8FC, 0x0FD, 0x8FD, 0x0FE, 0x8FE, 0x0FF, 0x4FF, 0x8FF, 0xCFF,
                    },
                },
            },
        },
    // };
    },

    {
    // static ADAPTIVE_ISP_IR_CUT_PARAM_T ir_cut_param = {
        /* nAutoSwitchEnable */
        1,
        /* tIrCutParam */
        {
            /* Day2Night */
            {
                /* nExposureTime */
                30000,
                /* nGain */
                2048,
                /* tIrCutCtlParam */
                {
                    /* nHoldTime */
                    120,
                    /* nIrCutMode */
                    1,
                },
            },
            /* Night2Day */
            {
                /* nExposureTime */
                20000,
                /* nGain */
                512,
                /* tIrCutCtlParam */
                {
                    /* nHoldTime */
                    120,
                    /* nIrCutMode */
                    0,
                },
            },
        },
    // };
    },

    {
    /* POST SATURATION Parameters */

    // static ADAPTIVE_ISP_POST_SATURATION_PARAM_T saturation_param = {
        /* nAdaptiveEnable */
        1,
        /* post saturation param */
        {
            /* 0 */
            {100},
            /* 1 */
            {100},
            /* 2 */
            {100},
            /* 3 */
            {100},
            /* 4 */
            {90},
        },
    // };
    },

    {
    /* Color Black White Mode Parameters */

    // static ADAPTIVE_ISP_COLOR_GREY_SWI2CH_PARAM_T color_grey_switch_param = {
        /* nAutoSwitchEnable  */
        0, // use csm mode
        /* tColorGreySwitchParam */
        {
            /* Color2BW */
            {
                /* nExposureTime */
                33333,
                /* nGain */
                4095,
                /* tColorGreyCsmCtlParam*/
                {0},
            },
            /* BW2Color */
            {
                /* nExposureTime */
                33333,
                /* nGain */
                1536,
                /* tColorGreyCsmCtlParam*/
                {255},
            },
        },
    // };
    },

    {
    /* ADA Parameters */

    // static ADAPTIVE_ISP_ADA_PARAM_T ada_param = {
        /* nAdaptiveEnable */
        1, // 1: enable, 0: disable
        /* tAdaParam */
        {
            /* 0 */
            {
                /* nAeYEverage */
                60,
                /* tAdaCtlParam */
                {
                    /* nAdaHistMax */
                    128,
                    /* nAdaTtlMax */
                    255,
                },
            },
            /* 1 */
            {
                /* nAeYEverage */
                50,
                /* tAdaCtlParam */
                {
                    /* nAdaHistMax */
                    128,
                    /* nAdaTtlMax */
                    200,
                },
            },
            /* 2 */
            {
                /* nAeYEverage */
                40,
                /* tAdaCtlParam */
                {
                    /* nAdaHistMax */
                    128,
                    /* nAdaTtlMax */
                    128,
                },
            },
            /* 3 */
            {
                /* nAeYEverage */
                30,
                /* tAdaCtlParam */
                {
                    /* nAdaHistMax */
                    128,
                    /* nAdaTtlMax */
                    100,
                },
            },
            /* 4 */
            {
                /* nAeYEverage */
                20,
                /* tAdaCtlParam */
                {
                    /* nAdaHistMax */
                    128,
                    /* nAdaTtlMax */
                    90,
                },
            },
        },
    // };
    },
};

参数以头文件形式保存在sensor_params/imx219/adaptive_imx219_f2k.h中
```

## 1.2 加载参数

### ◆ adaptive_sensor_name

```c
typedef struct {
    char * cSensor0Name;
    char * cSensor1Name;
    ADAPTIVE_ISP_PIPELINE_PARAM_T * tAdapIspParamF2k;
    ADAPTIVE_ISP_PIPELINE_PARAM_T * tAdapIspParamR2k;
} ADAPTIVE_SENSOR_NAME_T;
```

导入调试的参数文件，存放路径以IMX219为例，sensor_params/imx219/adaptive_imx219_f2k.h与sensor_params/imx219/adaptive_imx219_r2k.h，按要求赋值给adaptive_sensor_name结构体数组的成员中。

#### 成员

```c
cSensor0Name: sensor0的设备名称，对应pipeline0
cSensor1Name: sensor1的设备名称，对应pipeline1
tAdapIspParamF2k: pipeline0使用的adaptive参数
tAdapIspParamR2k: pipeline1使用的adaptive参数

具体使用方法如下:

#include "sensor_params/imx219/adaptive_imx219_f2k.h"`
#include "sensor_params/imx219/adaptive_imx219_r2k.h"`
ADAPTIVE_SENSOR_NAME_T adaptive_sensor_name[] =
{
    // imx219
    {
        .cSensor0Name = "m00_f_imx219_0 0-0010",
        .cSensor1Name = "m01_f_imx219_1 3-0010",
        .tAdapIspParamF2k = &adap_imx219_f2k,
        .tAdapIspParamR2k = &adap_imx219_r2k,
    },
    // imx385
    {
        .cSensor0Name = "m00_f_imx385_0 0-0010",
        .cSensor1Name = "m01_f_imx385_1 3-0010",
        .tAdapIspParamF2k = &adap_imx385_f2k,
        .tAdapIspParamR2k = &adap_imx385_r2k,
    },
};
按照定义添加新的数组成员，不同sensor顺序部分先后，没有对应sensor的调试参数时，adaptive将自动关闭功能。
```

**翻译免责声明**
为方便客户，Canaan 使用 AI 翻译程序将文本翻译为多种语言，它可能包含错误。我们不保证提供的译文的准确性、可靠性或时效性。对于因依赖已翻译信息的准确性或可靠性而造成的任何损失或损害，Canaan 概不负责。如果不同语言翻译之间存在内容差异，以简体中文版本为准。

如果您要报告翻译错误或不准确的问题，欢迎通过邮件与我们联系。
