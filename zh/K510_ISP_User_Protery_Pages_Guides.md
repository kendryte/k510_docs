

![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 ISP User Property Pages Guides</font>**

<font face="黑体"  size=3>文档版本：V1.0.0</font>

<font face="黑体"  size=3>发布日期：2022-09-30</font>

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
本文档为ISP User Property Pages说明文档。

**<font face="黑体"  size=5>读者对象</font>**

本文件的主要受众是有经验的软件工程师、图像算法工程师、系统设计师和系统集成商，他们希望实现私有应用程序和驱动程序。

**<font face="黑体"  size=5>修订记录</font>**
<font face="宋体"  size=2>修订记录累积了每次文档更新的说明。最新版本的文档包含以前所有版本的更新内容。</font>

| 版本号   | 修改者     | 修订日期 | 修订说明 |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | 系统软件组 | 2022-09-30 | SDK V1.9发布 |

<div style="page-break-after:always"></div>
<div style="page-break-after:always"></div>



# API

类型说明

```c
enum  isp_pipeline_e //pipeline的索引号，通常以数字或成员名称表示不同的pipeline
{
   ISP_F2K_PIPELINE; //对应int类型0
   ISP_R2K_PIPELINE; //对应int类型1
   ISP_TOF_PIPELINE; //对应int类型2
}；
```

```c
typedef struct _ADAPTIVE_USER_ATTR_ISP_CTL_T //属性页ISP控制功能汇总结构体，修改成员值可以实现控制
{
int nLscEnable; //控制LSC模块使能，0：关闭，1：开启
int nLdcEnable; //控制LDC模块使能，0：关闭，1：开启。当前LDC不能打开ISP异常
int nAeEnable; //控制自动/手动曝光，0：手动模式，1：自动模式。自动切换至手动状态默认使用上一帧曝光参数作为当前的手动值
int nAeEnhMode; //控制背光补偿/强光抑制，0：关闭，1：背光补偿，2：强光抑制。与WDR功能冲突，仅有一种模式可以开启，当其他模式开启时，当前模式启动无效
int nWdrEnable; // 0: normal, 1: linner-wdr enable。控制Linner WDR功能，与背光补偿和强光抑制功能冲突，仅有一种模式可以开启，当其他模式开启时，当前模式启动无效
int nAwbEnable; //控制自动/手动白平衡，0：手动模式，1：自动模式。若模式为手动时可以选配不同光源的CCM及手动设置白平衡Rgain、Ggain、Bgain
int nFlip; //控制镜像模式，0：正常，1：水平镜像，2：垂直镜像，3：水平垂直镜像
int nAntiflickerScl; //控制工频闪烁抑制功能，0：关闭，1，2：50Hz自动/强制，3，4：60Hz自动/强制。强制模式时高亮场景将限制最小曝光时间只能达到1/100s(50Hz)或1/120s(60Hz)
int nDefogEn; //控制去雾功能，0：关闭，1：开启
int reserved[10]; 
}ADAPTIVE_USER_ATTR_ISP_CTL_T;//通常初始化时用该别名
```

```c
typedef struct _ADAPTIVE_USER_ATTR_LIMIT_T //属性页限制参数范围汇总结构体
{
int nGainRange[2]; // gain range [0]: min, [1]: max
int nEtRange[2]; // ET range [0]: min, [1]: max
int nCtScl; // 选择不同光源下的CCM矩阵设置。0：A，1：U30，2：U35，3：TL84，4：D50，5：D65。AWB处于手动模式时，当前功能有效
}ADAPTIVE_USER_ATTR_LIMIT_T; //通常初始化时用该别名
```

```c
typedef struct _ADAPTIVE_USER_ATTR_WEIGHT_T //属性页调整功能强度汇总结构体
{
int nSaturationCoeff; //控制饱和度等级，范围0-100，默认50
int nBrightnessCoeff; //控制亮度等级，范围0-100，默认50
int nContrastCoeff; //控制对比度等级，范围0-100，默认50
int nSharpnessCoeff; //控制锐度强度，范围0-100，默认50
int n2dnrLevelCoeff; //控制2D降噪强度，范围0-10，默认5
/* ae param */
int nAeBacklightCoeff; //控制背光补偿模式强度，自动曝光且开启背光补偿模式下，范围1-10，不与强光抑制同时生效
int nAeStronglightCoeff; //控制强光抑制模式强度，自动曝光且开启强光抑制模式下，范围1-10，不与背光补偿同时生效
int nWdrCoeff; //Linner WDR功能有效开启时，控制WDR强度，范围0-9，注意设置超过9图像将异常
}ADAPTIVE_USER_ATTR_WEIGHT_T; //通常初始化时用该别名
```

```c
typedef struct _ADAPTIVE_USER_MENU_3A_T //属性页开启手动模式时可以控制的参数
{
int nCurGain; // current gain: 1~16x, default 2x, over range will use min or max value
int float nCurExpTime; // current exposure time(us)
int nCurWbRGain; //手动白平衡下，控制红通道增益，范围0-1023，默认202
int nCurWbGGain; //手动白平衡下，控制绿通道增益，范围0-1023，默认256不动
int nCurWbBGain; //手动白平衡下，控制蓝通道增益，范围0-1023，默认356
}ADAPTIVE_USER_MENU_3A_T; //通常初始化时用该别名
```

```c
typedef struct _ADAP_USER_ATTR_PAGE_T //属性页控制汇总结构体
{
int nWritten; //写入状态，下发时默认置为2，其他值将无法下发
int nAdaptiveUserAttrEnable; //属性页使能，0：关闭属性页功能，1：开启属性页功能
int nAdaptiveUserAeMode; // only use to ae auto/handle switch 0: sw, 1: hw
int nAeSync; // only use for ae sync in dual camera & sw ae
ADAPTIVE_USER_ATTR_ISP_CTL_T tUserAttrIspCtl; //ISP控制功能，上述结构体
ADAPTIVE_USER_ATTR_LIMIT_T tUserAttrLimit; //限制参数范围，上述结构体
ADAPTIVE_USER_ATTR_WEIGHT_T tUserAttrWeight; //调整功能强度，上述结构体
ADAPTIVE_USER_MENU_3A_T tUserMenu3A; //手动模式下控制参数，上述结构体
}ADAPTIVE_ATTRIBUTE_PAGE_T; // Root Permission for whole adaptive function
```

函数

```c
int attr_page_params_setting(enum isp_pipeline_e pipeline, ADAPTIVE_ATTRIBUTE_PAGE_T * attr_page); //属性页功能设置，传入参数pipeline 0：f2k, 1：r2k，3：tof（不支持），attr_page为上述汇总结构体指针，即可控制
int attr_page_get_written_stat(enum isp_pipeline_e pipeline); //获取可写状态，返回3，可进行配置
```



# API_DEMO

mediactl_init初始化以及ISP初始化结束后可进行属性页控制功能调用

```
1. 初始化默认参数结构体adap_attr_page_r2k
2. 设置written = 2
3. 调用attr_page_get_written_stat确认返回值是否为3，是则继续
4. 调用attr_page_params_setting，将adap_attr_page_r2k地址传入，等待生效
5. 修改其他参数，重复步骤2-4
```

注意：避免多个关联模块参数的修改，可能会导致控制异常。如：AE同步，AE手动/自动，曝光和增益范围等。



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

// 此demo数据同步暂时不完善
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



**翻译免责声明**  
为方便客户，Canaan 使用 AI 翻译程序将文本翻译为多种语言，它可能包含错误。我们不保证提供的译文的准确性、可靠性或时效性。对于因依赖已翻译信息的准确性或可靠性而造成的任何损失或损害，Canaan 概不负责。如果不同语言翻译之间存在内容差异，以简体中文版本为准。

如果您要报告翻译错误或不准确的问题，欢迎通过邮件与我们联系。
