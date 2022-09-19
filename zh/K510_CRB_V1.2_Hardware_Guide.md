![](../zh/images/canaan-cover.png)
&nbsp;
&nbsp;
**<font face="黑体" size="6" style="float:right">K510 CRB V1.2 Hardware Guides</font>**

<font face="黑体" size=100>
&nbsp;
&nbsp;
&nbsp;
</font>

<font face="黑体"  size=3>文档版本：V1.0.0</font>

<font face="黑体"  size=3>发布日期：2022-03-15</font>

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
本文档为K510 sdk的配套文档，旨在帮助工程师了解 k510 sdk的编译和烧录。

**<font face="黑体"  size=5>读者对象</font>**

本文档（本指南）主要适用的人员：

- 软件开发人员
- 技术支持人员

**<font face="黑体"  size=5>修订记录</font>**
<font face="宋体"  size=2>修订记录累积了每次文档更新的说明。最新版本的文档包含以前所有版本的更新内容。</font>

| 版本号 | 修改者    | 修订日期   | 修订说明           |
| :----- | --------- | ---------- | ------------------ |
| V1.0.0 | AI 产品部 | 2022-03-15 | |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>目 录</font>**

[toc]

<div style="page-break-after:always"></div>

# 1 概述

&emsp;&emsp;K510 CRB是针对Canaan Kendryte K510 AI芯片开发的集参考设计、芯片调试和测试、用户产品开发验证一体的硬件开发平台，用于展示K510芯片强大的算力和功能等。同时为客户提供基于K510芯片的硬件参考设计，使客户不需修改或只需要简单的修改参考设计的模块电路，就可以完成以K510芯片为核心的产品硬件开发工作。

&emsp;&emsp;K510 CRB支持K510芯片的硬件开发、应用软件设计、调试和运行等，因为考虑到不同的使用环境，对芯片进行全功能验证，所以各种接口齐全，设计相对完整。K510 CRB可以通过USB线缆与PC进行连接，作为一个基本开发系统使用，或实现更完全的开发系统和演示环境，连接如下设备和部件：

- 电源

- TF Card存储设备

- MIPI DSI LCD显示屏

- MIPI CSI摄像头模组

- DVP摄像头模组

- 以太网网线

- HDMI显示屏

- 耳机或喇叭

- 拓展备件

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-K510_Core.png">
</div>

  <center>图 1-1 K510 CRB 渲染图</center>

    **禁止事项**

  1. 禁止带电插拔核心模组及外围模块！
  2. 禁止在没有经释放静电或无静电防护的措施下直接操作本产品。
  3. 禁止使用有机溶剂或者腐蚀性液体清洗本产品。
  4. 禁止进行敲打、扭曲等可能造成物理损伤的操作。

    **注意事项**

  1. 请注意对人体进行静电释放后，再操作本产品，建议佩戴静电手环。
  2. 操作前请确认底板的供电电压和适配器电压在本文档所描述的允许范围内。
  3. 设计前请务必阅读本文档及工程文件中的注意事项。
  4. 注意产品在高温、高湿、高腐蚀环境下使用需要进行散热、排水、密封等特殊处理。
  5. 请勿自行维修、拆解，否则将无法享受免费的售后服务。

<div style="page-break-after:always"></div>

## 1.1 系统框图

&emsp;&emsp;系统框图用于描述K510 CRB的设计原理和各部件之间的关系，以让K510 CRB的使用和开发人员，能够对整个系统的架构和原理有一个直观的认识。

&emsp;&emsp;关于K510功能详情，请参考《K510 Full Datasheet》。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_1_2.png">
</div>

<center>图 1-2 K510 CRB组成</center>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_1_3.png">
</div>

<center>图 1-3 K510 CRB 系统框图 </center>

<div style="page-break-after:always"></div>

&emsp;&emsp;K510 CRB开发套件主要包括以下部件：

| 部件 | 数量 |
| :-: | :-: |
| K510 CRB主板 | 1 |
| USB type C线缆 | 2 |
| Micro USB OTG线缆 | 1 |
| MIPI DSI显示屏,分辨率1920x1080 | 1 |
| MIPI CSI摄像头子板，板载Sony IMX219 image sensor 两颗 | 1 |
| 亚克力保护外壳 | 1 |

<div style="page-break-after:always"></div>

## 1.2 功能概述

&emsp;&emsp;K510 SDK是以buildroot为基本框架，以K510 linux kernel（linux版本4.17.0），u-boot（u-boot版本2020.01），riscv-pk-k510

&emsp;&emsp;K510 CRB V1.2（如果没有特殊声明，本文档后续描述的CRB的版本都是V1.2）的主要功能如下：

- PMIC：电源管理
- 32 bit LPDDR3EE,总容量512MByte
- 8bit eMMC，总容量4GByte
- QSPI NAND,总容量 128MByte
- TF Card：支持外部扩展TF卡存储。
- USB OTG：系统升级使用，支持Host/Device切换
- SDIO WIFI：支持无线上网功能和蓝牙连接
- Audio：支持语音输入输出
- PDM MIC：VAD唤醒功能
- Uart &JTAG Debug: 开发板Debug使用
- Video Input: 双路MIPI CSI 2lane摄像头输入
- Video Output: MIPI DSI 4lane,1080P显示屏
- RGMII：千兆以太网连接
- HDMI: 高清晰度多媒体接口
- 拓展接口：电源、GPIO、I2C、SPI
- 按键、指示灯

<div style="page-break-after:always"></div>

# 2 硬件资源介绍

## 2.1 整体效果图

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_1.png" width=80%>
</div>

<center> 图2-1 主板正面图 </center>

<div style="page-break-after:always"></div>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_2.png" width=80%>
</div>

<center> 图2-1 主板背面图 </center>

<div style="page-break-after:always"></div>

## 2.2 结构与接口示意图

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_3.png" width=120%>
</div>

<center> 图2-3 主板正面各器件位置 </center>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2-4.png" width=120%>
</div>

<center> 图 2-4 主板背面 </center>

<div style="page-break-after:always"></div>

## 2.3 电源框图

&emsp;&emsp;K510 CRB使用DC-5V作为整板的输入电源，为K510 CORE 核心模组提供DC-5V，同时通过两个DC-DC为底板的其他外设提供1.8V和3.3V两路电源。

## 2.4 I2C设备地址

<center>表2-1 I2C设备地址表</center>

| 名称 | 管脚(SCL、SDA) | 地址 | 备注 |
| :-: | :-: | :-: | :-: |
| 触摸屏 | IO_103、IO_102 | 0x14或0x5D | |
| HDMI | IO_117、IO_116 | 0x3B | |
| Audio Codec | IO_117、IO_116 | 0x1A | |
| MIPI CSI Camera0 | IO_120、IO_121 | 0x10 | |
| MIPI CSI Camera1 | IO_47、IO_48   | 0x10 | |

## 2.5 原理图

&emsp;&emsp;K510 CRB开发板对应的参考原理图请在[release](https://github.com/kendryte/k510_docs/releases)处下载。

<div style="page-break-after:always"></div>

# 3 K510 Core V1.2核心模组

&emsp;&emsp;在使用K510 CRB进行学习和开发之前，建议先参考K510手册中芯片的详细架构，这样可以对K510的供电、存储、计算资源和外设等有更深入的了解，有利于芯片方案的熟悉和开发。

K510 核心板如图4-1。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_1.png">
</div>

<center>图4-1 K510 Core核心模组</center>
关于K510 核心模组更详细的资料请参阅《K510 Core 核心模组数据手册.pdf》
<div style="page-break-after:always"></div>
# 4 K510 CRB V1.2 客户参考板介绍

## 4.1 输入电源

&emsp;&emsp;K510 CRB使用外部5V供电，板载了两个USB type C接口，都可以为开发板进行供电，其中UART接口用于连接电脑，电脑的USB接口只能提供500mA电流，在遇到供电不足时，请同时使用适配器在DC:5V处供电。接口如下图所示。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_2.png" width=60%>
</div>

<center> 图4-2 电源输入接口 </center>

**注：限定使用5V电源，在使用快充适配器时，尽量不要同时连接手机等其它设备，以免造成快充适配器错误输出高于5V的电源，导致开发板电源部分损坏。**
&emsp;&emsp;使用K2 拨动开关进行上电和掉电的操作，如下图所示。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-3.jpg" width=50%>
</div>

<center>图4-3 电源开关说明</center>

<div style="page-break-after:always"></div>

## 4.2 存储设备

&emsp;&emsp;K510 CRB 板载了多种存储设备，包括DDR、eMMC、NAND Flash和TF Card。

### 4.2.1 eMMC

&emsp;&emsp;K510 CRB板载的一颗4G Bytes的eMMC存储器，位于核心模组上，可以用于存储启动代码和用户文件等数据。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-eMMC.png" width=70%>
</div>

<center>图4-4 eMMC存储器</center>

### 4.2.2 NandFlash

&emsp;&emsp;K510 CRB 板载了128M Bytes的NAND Flash存储器，可以用于存储启动代码和用户文件等数据。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_5.jpg " width=75%>
</div>

<center>图4-5 NAND Flash存储器</center>

### 4.2.3 TF卡

&emsp;&emsp;K510 CRB 板载了TF卡座，可以外接TF卡，用于存储启动代码和用户文件等数据。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_6.png">
</div>

<center>图4-6 TF卡座</center>

<div style="page-break-after:always"></div>

## 4.3 按键

&emsp;&emsp;K510 CRB板载了两颗用户轻触按键，用户可以对轻触按键进行自定义编程，作为系统输入触发或软件相关的其他功能等。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_7.jpg" width=50%>
</div>

<center>图4-7 按键</center>

## 4.4 指示灯

&emsp;&emsp;K510 CRB板载了一颗发光二极管，直接连接到了K510芯片的GPIO管脚上。

&emsp;&emsp;K510 CRB板载了一颗彩色发光二极管WS2812，直接连接到了K510芯片的GPIO管脚上。

&emsp;&emsp;对两颗指示灯进行自定义编程点亮或熄灭，可以作为系统输出或软件相关的状态指示等功能。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_8.jpg" width=60%>
</div>

<center>图4-8 指示灯</center>

<div style="page-break-after:always"></div>

## 4.5 启动模式和复位

&emsp;&emsp;K510 CRB板载了多种存储设备，通过配置启动时 BOOT0 和 BOOT1 两个管脚的电平来选择启动模式，0和1代表低电平和高电平。

&emsp;&emsp;PCB上通过下图所示的拨码开关选择启动模式，核心模组设计时已对 BOOT0 和 BOOT1 做了上拉设计，拨码开光上标记ON的一侧代表相应位拉低有效，ON对应的另一侧OFF代表上拉有效。

&emsp;&emsp;K510 通过 BOOT0 和 BOOT1 两个硬件管脚的状态决定芯片启动模式，启动模式选择如下表所示。

<center>表4-1 启动模式</center>

| BOOT1   | BOOT0   | 启动方式      |
| ------- | ------- | ------------ |
| 0(ON)   | 0(ON)   | 串口启动      |
| 0(ON)   | 1(OFF)  | SD卡启动      |
| 1(OFF)  | 0(ON)   | NANDFLASH启动 |
| 1(OFF)  | 1(OFF)  | EMMC启动      |

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_9.jpg" width=60%>
</div>

<center>图4-9 复位开关和启动模式拨码开关</center>

&emsp;&emsp;K510 CRB板载复位按键为图3-9 中的K2，按下可实现系统的硬件复位操作。

<div style="page-break-after:always"></div>

## 4.6 Audio 输入输出

&emsp;&emsp;K510 CRB使用了nuvoton公司的音频编解码器芯片NAU88C22，实现语音的输入和输出功能。包括一颗板载麦克风、标准3.5mm耳机插座和2P扬声器接口。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-10.jpg" width=60%>
</div>

<center>图4-10 Audio</center>

## 4.7 USB OTG插座

&emsp;&emsp;K510 CRB 板载USB OTG插座，可以用来实现USB host/device功能。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_11.jpg">
</div>

<center>图4-11 USB-OTG座</center>

<div style="page-break-after:always"></div>

## 4.8 UART接口

&emsp;&emsp;K510 CRB为了方便用户开发和调试，板载了USB->UART接口，可以通过PC-USB线缆对K510进行UART串口通信和调试等操作。初次使用可能会需要加载驱动，详见4.2节。板载UART接口如下图所示。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_12.jpg" width=50%>
</div>

<center>图4-12 USB-UART接口</center>

## 4.9 WIFI/BT模组

&emsp;&emsp;K510 CRB 板载了一颗WIFI/BT二合一模组AP6212，用于拓展开发板进行网络的连接和蓝牙的通信功能，板载接口如下图所示。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-13.jpg" width=40%>
</div>

<center>图4-13 WIFI/BT模组</center>

<div style="page-break-after:always"></div>

## 4.10 以太网

&emsp;&emsp;K510 CRB 板载千兆以太网座，K510通过RGMII接口外接PHY芯片实现。板载接口如下图所示。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_14.jpg" width=60%>
</div>

<center>图4-14 以太网接口</center>

## 4.11 HDMI输出

&emsp;&emsp;K510 CRB板载HDMI-A母座，可以通过标准HDMI线缆连接外置显示屏，使用K510的mipi dsi接口输出转换实现。板载接口如下图所示。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_15.jpg" width=60%>
</div>

<center>图4-15 HDMI接口</center>

 **注意**：因为HDMI和1080P TFT显示屏都是使用mipi dsi驱动，所以只能二选一显示，无法同时使用，切换通过控制管脚GPIO来选择其中之一输出。

<div style="page-break-after:always"></div>

## 4.12 Video In

&emsp;&emsp;K510 CRB通过0.8mm 间距板对板连接器，将MIPI CSI、DVP、电源和部分GPIO等进行了引出，用于实现不同场景和不同需求情况下的摄像头输入。板载接口如下图所示。接口定义如下表所示。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-16.jpg">
</div>

<center>图4-16 Video IN接口</center>

<center>表4-2 Video IN接口定义</center>

| 编号 | 定义             | 编号 | 定义                       |
| ---- | ---------------- | ---- | --------------- |
| 1    | VDD_5V           | 60   | GPIO_1V8_59_DVP_D12      |
| 2    | VDD_5V           | 59   | GPIO_1V8_58_DVP_D11      |
| 3    | VDD_5V           | 58   | GPIO_1V8_50_DVP_D3       |
| 4    | VDD_5V           | 57   | GPIO_1V8_51_DVP_D4       |
| 5    | GND              | 56   | GPIO_1V8_60_DVP_D13      |
| 6    | GND              | 55   | GPIO_1V8_55_DVP_D8       |
| 7    | MIPI_CSI_D0_P    | 54   | GPIO_1V8_61_DVP_D14      |
| 8    | MIPI_CSI_D0_N    | 53   | GPIO_1V8_52_DVP_D5       |
| 9    | GND              | 52   | GPIO_1V8_47_DVP_D0       |
| 10   | MIPI_CSI_CLK0_P  | 51   | GPIO_1V8_56_DVP_D9       |
| 11   | MIPI_CSI_CLK0_N  | 50   | GPIO_1V8_53_DVP_D6       |
| 12   | GND              | 49   | GPIO_1V8_57_DVP_D10      |
| 13   | MIPI_CSI_D1_P    | 48   | GPIO_1V8_48_DVP_D1       |
| 14   | MIPI_CSI_D1_N    | 47   | GPIO_1V8_54_DVP_D7       |
| 15   | GND              | 46   | GPIO_1V8_64_DVP_HREF     |
| 16   | MIPI_CSI_D2_N    | 45   | GPIO_1V8_49_DVP_D2       |
| 17   | MIPI_CSI_D2_P    | 44   | GPIO_1V8_65_DVP_DEN      |
| 18   | GND              | 43   | GPIO_1V8_66_DVP_PCLK     |
| 19   | MIPI_CSI_CLK1_N  | 42   | GPIO_1V8_62_DVP_D15      |
| 20   | MIPI_CSI_CLK1_P  | 41   | GPIO_1V8_63_DVP_VSYNC    |
| 21   | GND              | 40   | GPIO_1V8_82 |
| 22   | MIPI_CSI_D3_N    | 39   | GPIO_1V8_67  |
| 23   | MIPI_CSI_D3_P    | 38   | GPIO_1V8_68  |
| 24   | GND              | 37   | GPIO_1V8_72  |
| 25   | MIPI_CSI_I2C_SCL | 36   | GPIO_1V8_73  |
| 26   | MIPI_CSI_I2C_SCA | 35   | GPIO_1V8_74  |
| 27   | GND              | 34   | GND          |
| 28   | GND              | 33   | GND          |
| 29   | 1V8              | 32   | 3V3          |
| 30   | 1V8              | 31   | 3V3          |

**注意**：外部连接时注意所连接管脚的电平范围，防止错误的电压输入永久性损坏K510芯片。

<div style="page-break-after:always"></div>

## 4.13 Video Out

&emsp;&emsp;K510 CRB板载了0.5mm间距30P的翻盖下接FPC连接器，用于连接外部的LCD显示屏，板载接口如下图所示。接口定义如下表所示。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-17.jpg">
</div>

<center>图4-17 Video Out接口</center>

<center>表4-3 Video Out接口定义</center>

| 编号 | 定义              | 编号 | 定义             |
| ---- | ----------------- | ---- | ---------------- |
| 1    | GND               | 16   | MIPI_DSI_D1_N    |
| 2    | GND               | 17   | MIPI_DSI_D1_P    |
| 3    | VDD_5V            | 18   | GND              |
| 4    | VDD_5V            | 19   | MIPI_DSI_CLK_N   |
| 5    | VDD_3V3           | 20   | MIPI_DSI_CLK_P   |
| 6    | VDD_3V3           | 21   | GND              |
| 7    | GND               | 22   | MIPI_DSI_D0_N    |
| 8    | TOUCH_1V8_I2C_SCL | 23   | MIPI_DSI_D0_P    |
| 9    | TOUCH_1V8_I2C_SDA | 24   | GND              |
| 10   | TOUCH_1V8_INT     | 25   | MIPI_DSI_D3_N    |
| 11   | TOUCH_1V8_RST     | 26   | MIPI_DSI_D3_P    |
| 12   | GND               | 27   | GND              |
| 13   | MIPI_DSI_D2_N     | 28   | MIPI_DSI_LCD_RST |
| 14   | MIPI_DSI_D2_P     | 29   | MIPI_DSI_LCD_EN  |
| 15   | GND               | 30   | GND              |

<div style="page-break-after:always"></div>

## 4.14 拓展接口

&emsp;&emsp;为了方便用户进行自定义拓展功能的实现，在K510 CRB上预留了30P的2.54mm拓展排针，引出了包括电源和部分GPIO，用户可通过软件iomux操作，将I2C、UART、SPI等硬件资源映射到相应的GPIO上，以实现相应功能的外部连接和拓展。板载接口如下图所示。详细定义如下表所示。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw-3-18.jpg">
</div>

<center>图4-18 40P排针拓展接口</center>

<center>表4-4 拓展接口定义</center>

| 编号 | 定义         | 编号 | 定义         |
| ---- | ------------ | ---- | ------------ |
| 1    | VDD_1V8      | 2    | GND          |
| 3    | VDD_1V8      | 4    | GND          |
| 5    | VDD_3V3      | 6    | GND          |
| 7    | VDD_3V3      | 8    | GND          |
| 9    | VDD_5V       | 10   | GND          |
| 11   | VDD_5V       | 12   | GPIO_1V8_95  |
| 13   | GPIO_3V3_114 | 14   | GPIO_3V3_115 |
| 15   | GPIO_1V8_92  | 16   | GPIO_1V8_96  |
| 17   | GPIO_1V8_105 | 18   | GPIO_1V8_107 |
| 19   | GPIO_1V8_104 | 20   | GPIO_1V8_106 |
| 21   | GPIO_1V8_118 | 22   | GPIO_1V8_119 |
| 23   | GPIO_1V8_93  | 24   | GPIO_1V8_94  |
| 25   | GPIO_3V3_125 | 26   | GPIO_3V3_124 |
| 27   | GPIO_3V3_127 | 28   | GPIO_3V3_126 |
| 29   | GND          | 30   | GND          |

**注意**：外部连接时注意所连接管脚的电平范围，防止错误的电压输入永久性损坏K510芯片。

<div style="page-break-after:always"></div>

# 5 IMX219 双通道RGB摄像头模组介绍

    IMX219双通道RGB摄像头模组，使用第4.12节中的Video IN接口连接K510 CRB V1.2开发板, 每个摄像头通过2 lane MIPI CSI 输入图像到K510芯片。详细数据手册请参阅《IMX219双通道RGB摄像头模组数据手册》。

# 6 1080P LCD 电容触摸显示屏模组介绍

    暂无

# 7 开发板使用

## 7.1 安装驱动

&emsp;&emsp;K510 CRB板载了CH340E来实现USB-UART通信功能，所以在使用前，需要先安装对应的驱动。

&emsp;&emsp;使用资料包中的驱动程序或者在如下地址进行下载安装即可。

&emsp;&emsp;<http://www.wch.cn/product/CH340.html>

## 7.2 固件烧录

&emsp;&emsp;请参考[K510_SDK_Build_and_Burn_Guide](./K510_SDK_Build_and_Burn_Guide.md)文档。

## 7.3 开关机

&emsp;&emsp;1）安装电源线和USB调试线。

&emsp;&emsp;2）拨码开关选择从TF卡启动。

&emsp;&emsp;3）按照4.1节所示的方法拨动开关进行上电。

## 7.4 串口调试

&emsp;&emsp;驱动安装完成后，对K510 CRB进行上电操作，这时候，在PC的设备管理器-端口中会出现端口。

&emsp;&emsp;使用串口调试工具，打开设备所的端口号，波特率115200。

&emsp;&emsp;如下图所示，设备为“COM6”，具体以PC设备管理器中显示的情况为准。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_4_1.jpg">
</div>

<center>图7-1 驱动安装完成后的设备管理器</center>

**翻译免责声明**  
为方便客户，Canaan 使用 AI 翻译程序将文本翻译为多种语言，它可能包含错误。我们不保证提供的译文的准确性、可靠性或时效性。对于因依赖已翻译信息的准确性或可靠性而造成的任何损失或损害，Canaan 概不负责。如果不同语言翻译之间存在内容差异，以简体中文版本为准。

如果您要报告翻译错误或不准确的问题，欢迎通过邮件与我们联系。
