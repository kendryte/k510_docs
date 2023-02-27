

![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 ISP User Property Pages Guides</font>**

<font face="黑体"  size=3>Document version:V1.0.0</font>

<font face="黑体"  size=3>Published:2022-09-30</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Disclaimer**</font>
The products, services or features you purchase shall be subject to the commercial contracts and terms of Beijing Canaan Jiesi Information Technology Co., Ltd. ("the Company", the same hereinafter), and all or part of the products, services or features described in this document may not be within the scope of your purchase or use. Except as otherwise agreed in the contract, the Company disclaims all representations or warranties, express or implied, as to the accuracy, reliability, completeness, marketing, specific purpose and non-aggression of any representations, information, or content of this document. Unless otherwise agreed, this document is provided as a guide for use only. Due to product version upgrades or other reasons, the contents of this document may be updated or modified from time to time without any notice.

**<font face="黑体"  size=3>Trademark Notices</font>**

“<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />”,"Canaan" icon, Canaan and other trademarks of Canaan and other trademarks of Canaan are trademarks of Beijing Canaan Jiesi Information Technology Co., Ltd. All other trademarks or registered trademarks that may be mentioned in this document are owned by their respective owners.

**<font face="黑体"  size=3>Copyright ©2022 Beijing Canaan Jiesi Information Technology Co., Ltd</font>**
This document is only applicable to the development and design of the K510 platform, without the written permission of the company, no unit or individual may disseminate part or all of the content of this document in any form.

**<font face="黑体"  size=3>Beijing Canaan Jiesi Information Technology Co., Ltd</font>**
URL: canaan-creative.com
Business inquiry: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# Preface
**<font face="黑体"  size=5>Document purpose</font>**
This document is an ISP User Property Pages documentation.

**<font face="黑体"  size=5>Reader objects</font>**

The primary audience for this document is experienced software engineers, image algorithm engineers, system designers, and system integrators who want to implement proprietary applications and drivers.

**<font face="黑体"  size=5>Revision history</font>**
The revision history accumulates a description of each document update. The latest version of the document contains updates for all previous versions.

| The version number | The version number | Date of revision | Revision Notes |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | System software groups | 2022-09-30 | SDK V1.9 released |

<div style="page-break-after:always"></div>
<div style="page-break-after:always"></div>



# API

Type description

```c
enum  isp_pipeline_e //The index number of the pipeline, which usually represents different pipelines by numbers or member names
{
   ISP_F2K_PIPELINE; //Corresponding int type 0
   ISP_R2K_PIPELINE; //Corresponding int type 1
   ISP_TOF_PIPELINE; //Corresponding int type 2
}；
```

```c
typedef struct _ADAPTIVE_USER_ATTR_ISP_CTL_T //the ISP control function of the property page summarizes the structure, and can be controlled by modifying the member values
{
int nLscEnable; //Control LSC module to enable,0: off，1: on
int nLdcEnable; //Control LDC module to enable,0: off，1: on.current LDC cannot open
int nAeEnable; //Control automatic/manual exposure, 0: manual mode, 1: automatic mode, and automatically switch to manual mode. By default, the exposure parameters of the previous frame are used as the current manual values.
int nAeEnhMode; //Control backlight compensation/strong light suppression, 0: off, 1: backlight compensation, 2: strong light suppression, which conflicts with WDR function. Only one mode can be turned on. When other modes are turned on, the current mode is invalid.
int nWdrEnable; // 0: normal,1: linner-wdr enable.Control the Linner WDR function conflicts with the functions of backlight compensation and strong light suppression, and only one mode can be turned on. When other modes are turned on, the current mode is invalid.
int nAwbEnable; //Control automatic/manual white balance, 0: manual mode, 1: automatic mode.If the mode is set to manual, CCM with different light sources and manual setting of Rgain, Ggain, and Bgain for white balance can be optionally selected.
int nFlip; //Control the mirror&flip mode: 0: normal, 1: mirror, 2: flip, 3: mirror and flip.
int nAntiflickerScl; //Control the power frequency flicker suppression function, 0: off, 1, 2: 50hz automatic/forced, 3, 4: 60hz automatic/forced. And highlight the scene in forced mode, which will limit the minimum exposure to 1/100s(at 50Hz) or 1/120s(at 60Hz).
int nDefogEn; //Control defogging function, 0: off, 1: on.
int reserved[10]; 
}ADAPTIVE_USER_ATTR_ISP_CTL_T;//This alias is usually used for initialization.
```

```c
typedef struct _ADAPTIVE_USER_ATTR_LIMIT_T //Property Page Limit Parameter Range Summary Structure
{
int nGainRange[2]; // Limit the range of gain, [0]-[1]: [min]-[max]
int nEtRange[2]; // Limit the exposure time range, [0]-[1]: [min]-[max]
int nCtScl; // Select CCM matrix settings for different light sources. 0: A, 1: U30, 2: U35, 3: TL84, 4: D50, 5: D65. This function is available when AWB is in manual mode.
}ADAPTIVE_USER_ATTR_LIMIT_T; //This alias is usually used for initialization.
```

```c
typedef struct _ADAPTIVE_USER_ATTR_WEIGHT_T //Property page adjustment function strength summary structure
{
int nSaturationCoeff; //Control the saturation level, ranging from 0 to 100, and the default is 50.
int nBrightnessCoeff; //Control the brightness level, ranging from 0 to 100, and the default is 50.
int nContrastCoeff; //Control the contrast level, ranging from 0 to 100, and the default is 50.
int nSharpnessCoeff; //Control the sharpness intensity, ranging from 0 to 100, and the default is 50.
int n2dnrLevelCoeff; //Control the intensity of 2D noise reduction, with a range of 0-10 and a default of 5.
/* ae param */
int nAeBacklightCoeff; //Control the intensity of backlight compensation mode, automatically expose and turn on backlight compensation mode, the range is 1-10, which does not take effect at the same time as strong light suppression.
int nAeStronglightCoeff; //Control the intensity of strong light suppression mode, automatically expose and turn on the strong light suppression mode, the range is 1-10, which does not take effect at the same time as backlight compensation.
int nWdrCoeff; //When the Linner WDR function is effectively turned on, control the WDR intensity, with the range of 0-9. Note that the image will be abnormal if it is set to more than 9.
}ADAPTIVE_USER_ATTR_WEIGHT_T; //This alias is usually used for initialization.
```

```c
typedef struct _ADAPTIVE_USER_MENU_3A_T //Parameters that can be controlled when the property page is turned on in manual mode.
{
int nCurGain; // current gain: 1~16x, default 2x, over range will use min or max value
int float nCurExpTime; // current exposure time(us)
int nCurWbRGain; //Under manual white balance, the red channel gain is controlled, ranging from 0 to 1023, and the default value is 202.
int nCurWbGGain; //Under manual white balance, control the green channel gain, ranging from 0-1023, and the default value is 256.
int nCurWbBGain; //Under manual white balance, control the blue channel gain, ranging from 0 to 1023, and the default value is 356.
}ADAPTIVE_USER_MENU_3A_T; //This alias is usually used for initialization.
```

```c
typedef struct _ADAP_USER_ATTR_PAGE_T //Property page controls summary structure.
{
int nWritten; //Write status, set to 2 by default when distributing, and other values will not be distributed.
int nAdaptiveUserAttrEnable; //Enable control of the property page. 0: Turn off property page function, 1: Turn on property page function.
int nAdaptiveUserAeMode; // only use to ae auto/handle switch 0: sw, 1: hw
int nAeSync; // only use for ae sync in dual camera & sw ae
ADAPTIVE_USER_ATTR_ISP_CTL_T tUserAttrIspCtl; //ISP control function, the above structure
ADAPTIVE_USER_ATTR_LIMIT_T tUserAttrLimit; //Limit the parameter range, the above structure
ADAPTIVE_USER_ATTR_WEIGHT_T tUserAttrWeight; //Adjust the functional strength, the above structure
ADAPTIVE_USER_MENU_3A_T tUserMenu3A; //Control parameter in manual mode, the above structure
}ADAPTIVE_ATTRIBUTE_PAGE_T; // Root Permission for whole adaptive function
```

Function

```c
int attr_page_params_setting(enum isp_pipeline_e pipeline, ADAPTIVE_ATTRIBUTE_PAGE_T * attr_page); //Property page function setting can be controlled by passing in parameters pipeline 0: f2k, 1: r2k, 3: tof (not supported) and attr_page as the above summary structure pointer.
int attr_page_get_written_stat(enum isp_pipeline_e pipeline); //Get the writable status, configuration can be performed when 3 is returned.
```



# API_DEMO

After the initialization of mediactl_init and ISP, the property page control function can be called.

```
1. initialize the default parameter structure adap_attr_page_r2k.
2. Set written = 2
3. Call attr_page_get_written_stat to confirm whether the return value is 3, and if so, continue.
4. Call attr_page_params_setting, and pass in the adap_attr_page_r2k address, waiting for it to take effect.
5. Modify other parameters and repeat steps 2 -4.
```

Note: Avoid modifying the parameters of multiple associated modules, which may lead to abnormal control.Such as: AE synchronization, AE manual/automatic, exposure and gain range, etc.

```c
static ADAPTIVE_ATTRIBUTE_PAGE_T adap_attr_page_f2k =
{
	.nAdaptiveUserAttrEnable = 1, // 0: disable, 1: enable
	.nAdaptiveUserAeMode = 0, // 0: sw, 1: hw
	.nWritten = 2,
	.nAeSync = 0,
	.tUserAttrIspCtl = {
		.nAeEnable = 1,
		.nAeEnhMode = 0,
		.nAwbEnable = 1,
		.nLdcEnable = 0, // 0: disable, 1: enable
		.nLscEnable = 1, // 0: disable, 1: enable
		.nFlip = 0,      // 0: normal, 1: hflip, 2: vflip, 3: hvflip
		.nAntiflickerScl = 1, // only sw ae use, 0: normal, 1: 50Hz auto, 2: 50Hz force, 3: 60Hz auto, 4: 60Hz force
		.nDefogEn = 0, // 0: disable, 1 & 2: reserved, 3: enable
		.nWdrEnable = 0,
	},
	.tUserAttrLimit = {
		.nCtScl = 0, // 0: A, 1: U30, 2: U35, 3: TL84, 4: D50, 5: D65
		.nEtRange = {1, 30000}, // [0]: min, [1]: max
		.nGainRange = {2, 16}, // [0]: min do not modify, [1]: max
	},
	.tUserAttrWeight = {
		.n2dnrLevelCoeff = 5, // level 0:10, default 5
		.nBrightnessCoeff = 50, // level: 0 - 100, default 50
		.nContrastCoeff = 50, // level: 0 - 100, default 50
		.nSaturationCoeff = 50, // level: 0 - 100, default 50
		.nSharpnessCoeff = 50, // level: 0 - 100, default 50
		.nAeBacklightCoeff = 0,
		.nAeStronglightCoeff = 0,
	},
	.tUserMenu3A = {
		.nCurExpTime = 30000,
		.nCurGain = 2,
		.nCurWbRGain = 202,
		.nCurWbGGain = 256,
		.nCurWbBGain = 356,
	}
};

static ADAPTIVE_ATTRIBUTE_PAGE_T adap_attr_page_r2k =
{
	.nAdaptiveUserAttrEnable = 1, // 0: disable, 1: enable
	.nAdaptiveUserAeMode = 0, // 0: sw, 1: hw
	.nWritten = 2,
	.nAeSync = 0,
	.tUserAttrIspCtl = {
		.nAeEnable = 1,
		.nAeEnhMode = 0,
		.nAwbEnable = 1,
		.nLdcEnable = 0, // 0: disable, 1: enable
		.nLscEnable = 1, // 0: disable, 1: enable
		.nFlip = 0,      // 0: normal, 1: hflip, 2: vflip, 3: hvflip
		.nAntiflickerScl = 1, // only sw ae use, 0: normal, 1: 50Hz auto, 2: 50Hz force, 3: 60Hz auto, 4: 60Hz force
		.nDefogEn = 0, // 0: disable, 1 & 2: reserved, 3: enable
		.nWdrEnable = 0,
	},
	.tUserAttrLimit = {
		.nCtScl = 0, // 0: A, 1: U30, 2: U35, 3: TL84, 4: D50, 5: D65
		.nEtRange = {1, 30000}, // [0]: min, [1]: max
		.nGainRange = {2, 16}, // [0]: min do not modify, [1]: max
	},
	.tUserAttrWeight = {
		.n2dnrLevelCoeff = 5, // level 0:10, default 5
		.nBrightnessCoeff = 50, // level: 0 - 100, default 50
		.nContrastCoeff = 50, // level: 0 - 100, default 50
		.nSaturationCoeff = 50, // level: 0 - 100, default 50
		.nSharpnessCoeff = 50, // level: 0 - 100, default 50
		.nAeBacklightCoeff = 0,
		.nAeStronglightCoeff = 0,
	},
	.tUserMenu3A = {
		.nCurExpTime = 30000,
		.nCurGain = 2,
		.nCurWbRGain = 202,
		.nCurWbGGain = 256,
		.nCurWbBGain = 365,
	}
};

pthread_t attr_page_daemon;

// The data synchronization of this demo is temporarily incomplete.
int modify_attr_param()
{
	while(1)
	{
		if(adap_attr_page_f2k.nAdaptiveUserAttrEnable == 0)
		{
			adap_attr_page_f2k.nAdaptiveUserAttrEnable = 1;
		}
		else
		{
			adap_attr_page_f2k.nAdaptiveUserAttrEnable = 0;
		}
		sleep(1);
	}
}

int attr_page_set(int pipeline)
{
	while(1)
	{
		while(attr_page_get_written_stat(pipeline) != 3)
		{
			usleep(20);
		}
		attr_page_params_setting(pipeline, &adap_attr_page_f2k);
	}
}

int main()
{
	pthread_create(&attr_page_daemon, NULL, modify_attr_param, NULL);
	f2k_pipeline = 0;
	attr_page_set(f2k_pipeline);
}

```



**Translation Disclaimer**
For the convenience of customers, Canaan uses an AI translator to translate text into multiple languages, which may contain errors. We do not guarantee the accuracy, reliability or timeliness of the translations provided. Canaan shall not be liable for any loss or damage caused by reliance on the accuracy or reliability of the translated information. If there is a content difference between the translations in different languages, the Chinese Simplified version shall prevail.

If you would like to report a translation error or inaccuracy, please feel free to contact us by mail.
