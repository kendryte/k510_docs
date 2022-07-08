![](../zh/images/canaan-cover.png)
&nbsp;
&nbsp;
**<font face="黑体" size="6" style="float:right">K510 CRB V1.2 Hardware Guides</font>**

<font face="黑体" size=100>&nbsp;
&nbsp;
&nbsp;</font>

<font face="黑体"  size=3>Document version: V1.0.0</font>

<font face="黑体"  size=3>Published: 2022-03-15</font>

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
This document is a companion document to the K510 sdk and is intended to help engineers understand the compilation and burning of the K510 sdk. 

**<font face="黑体"  size=5>Reader Objects</font>**

The main people to whom this document (this guide) applies:

- Software developers
- Technical support personnel

**<font face="黑体"  size=5>Revision history</font>**
 <font face="宋体"  size=2>The revision history accumulates a description of each document update. The latest version of the document contains updates for all previous versions. </font>

| The version number | Modified by    | Date of revision   | Revision Notes           |
| :----- | --------- | ---------- | ------------------ |
| V1.0.0 | AI Products Division | 2022-03-15 | |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contents</font>**

[toc]

<div style="page-break-after:always"></div>

# 1 Overview

&emsp; &emsp; K510 CRB is a hardware development platform for Canaan Kendryte K510 AI chip that integrates reference design, chip debugging and testing, and user product development verification, which is used to demonstrate the powerful computing power and functions of the K510 chip. At the same time, it provides customers with hardware reference designs based on K510 chips, so that customers do not need to modify or simply modify the module circuit of the reference design, and can complete the product hardware development work with K510 chips as the core.

&emsp; &emsp; K510 CRB supports the hardware development, application software design, debugging and operation of the K510 chip, because considering different usage environments, the chip is fully functional verification, so the various interfaces are complete and the design is relatively complete. The K510 CRB can be connected to a PC via a USB cable, used as a basic development system, or to a more complete development system and demo environment, connecting the following devices and components:

- power supply

- TF Card storage device

- MIPI DSI LCD display

- MIPI CSI camera module

- DVP camera module

- Ethernet network cable

- HDMI display

- Headphones or speakers

- Expand spare parts

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-K510_Core.png">
</div>

  <center>Figure 1-1 K510 CRB rendering</center>

    **禁止事项**

  1. It is forbidden to plug and unplug the core module and peripheral modules live!
  2. It is forbidden to operate this product directly without the measures of discharge static electricity or without static protection.
  3. It is forbidden to use organic solvents or corrosive liquids to clean this product.
  4. It is forbidden to perform operations such as tapping and twisting that may cause physical damage.

    **Precautions**

  1. Please note that after the electrostatic discharge of the human body, before operating this product, it is recommended to wear an electrostatic bracelet.
  2. Before operation, confirm the supply voltage and adapter voltage of the backplane within the allowable range described in this document.
  3. Be sure to read this document and the considerations in the engineering file before designing.
  4. Note that the use of products in high temperature, high humidity, high corrosion environment requires special treatment such as heat dissipation, drainage, and sealing.
  5. Please do not repair and disassemble yourself, otherwise you will not be able to enjoy free after-sales service.

<div style="page-break-after:always"></div>

## 1.1 System Block Diagram

&emsp; &emsp; The system block diagram is used to describe the design principles of the K510 CRB and the relationship between the components, so that the use of the K510 CRB and developers can have an intuitive understanding of the architecture and principles of the entire system.

&emsp; &emsp; For more information on K510 features, please refer to K510 Full Datasheet.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_1_2.png">
</div>

<center>Figure 1-2 K510 CRB composition</center>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_1_3.png">
</div>

<center>Figure 1-3 K510 CRB System Block Diagram </center>

<div style="page-break-after:always"></div>

&emsp; &emsp; The K510 CRB development kit consists mainly of the following components:

| parts | quantity |
| :-: | :-: |
| K510 CRB motherboard | 1 |
| USB type C线缆 | 2 |
| Micro USB OTG cable | 1 |
| MIPI DSI display with a resolution of 1920x1080 | 1 |
| MIPI CSI camera sub-board, on-board Sony IMX219 image sensor two | 1 |
| Acrylic protective housing | 1 |

<div style="page-break-after:always"></div>

## 1.2 Function Overview

&emsp; &emsp; The K510 SDK is based on buildroot as the basic framework, with K510 linux kernel (linux version 4.17.0), u-boot (u-boot version 2020.01), riscv-pk-k510

&emsp; &emsp; The main features of K510 CRB V1.2 (if there are no special declarations, the versions of CRB described later in this document are V1.2) are as follows:

- PMIC: Power management
- 32 bit LPDDR3EE, total capacity 512MByte
- 8bit eMMC, total capacity 4GByte
- QSPI NAND, total capacity 128MByte
- TF Card: Supports external expansion of TF card storage.
- USB OTG: System upgrade, support Host/Device switching
- SDIO WIFI: Supports Wireless Internet function and Bluetooth connection
- Audio: Support voice input and output
- PDM MIC: VAD wake-up function
- Uart & JTAG Debug: Development boards used by Debug
- Video Input: Dual MIPI CSI 2lane camera input
- Video Output: MIPI DSI 4lane, 1080P display
- RGMII: Gigabit Ethernet connection
- HDMI: High-definition multimedia interface
- Extended interfaces: power supply, GPIO, I2C, SPI
- Keys, indicators

<div style="page-break-after:always"></div>

# 2 Introduction to hardware resources

## 2.1 Overall renderings

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_1.png" width=80%>
</div>

<center> Figure 2-1 Motherboard front </center>

<div style="page-break-after:always"></div>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_2.png" width=80%>
</div>

<center> Figure 2-1 On the back of the motherboard </center>

<div style="page-break-after:always"></div>

## 2.2 Schematic diagram of structure and interface

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_3.png" width=120%>
</div>

<center> Figure 2-3 Position of each device on the front of the motherboard </center>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2-4.png" width=120%>
</div>

<center> Figure 2-4 Back of the motherboard </center>

<div style="page-break-after:always"></div>

## 2.3 Power Block Diagram

&emsp; &emsp; The K510 CRB uses DC-5V as the input power of the entire board, providing DC-5V for the K510 CORE core module, and 1.8V and 3.3V for the other peripherals of the backplane through two DC-DCs.

## 2.4 I2C Device Address

<center>Table 2-1 I2C Device Address Table</center>

| name | Pins (SCL, SDA) | address | remark |
| :-: | :-: | :-: | :-: |
| touch screen | IO_103、IO_102 | 0x14 or 0x5D | |
| HDMI | IO_117、IO_116 | 0x3B | |
| Audio Codec | IO_117、IO_116 | 0x1A | |
| MIPI CSI Camera0 | IO_120、IO_121 | 0x10 | |
| MIPI CSI Camera1 | IO_47、IO_48   | 0x10 | |

## 2.5 Schematics

&emsp; &emsp; The reference schematic for the K510 CRB development board should be[ downloaded at release](https://github.com/kendryte/k510_docs/releases). 

<div style="page-break-after:always"></div>

# 3 Introduction to each section of the development board

## 3.1 Core Modules

&emsp; &emsp; Before using K510 CRB for learning and development, it is recommended to refer to the detailed architecture of the chip in the K510 manual, so that you can have a deeper understanding of the power supply, storage, computing resources and peripherals of the K510, which is conducive to the familiarity and development of the chip solution. The K510 core board is shown in Figure 3-1.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_1.png">
</div>

<center>Figure 3-1 K510 Core Core Module</center>

<div style="page-break-after:always"></div>

## 3.2 Input power supply

&emsp; &emsp; K510 CRB uses external 5V power supply, on-board two USB type C interfaces, can be used to power the development board, of which the UART interface is used to connect to the computer, the COMPUTER's USB interface can only provide 500mA current, in the case of insufficient power supply, please use the adapter at the same time to supply power at DC: 5V. The interface is shown in the following figure.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_2.png" width=60%>
</div>

<center> Figure 3-2 Power input connector </center>

**Note: Limit the use of 5V power supply, when using the fast charge adapter, try not to connect other devices such as mobile phones at the same time, so as not to cause the fast charge adapter to incorrectly output a power supply higher than 5V, resulting in damage to the power supply part of the development board. **
&emsp; &emsp; Use the K2 toggle switch for power-up and power-down operation, as shown in the following figure. 

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-3.jpg" width=50%>
</div>

<center>Figure 3-3 Power switch description</center>

<div style="page-break-after:always"></div>

## 3.3 Storage Devices

&emsp; &emsp; The K510 CRB includes a variety of storage devices on board, including DDR, eMMC, NAND Flash, and TF Card.

### 3.3.1 eMMC

&emsp; &emsp; A 4G Bytes eMMC memory on board on the K510 CRB, located on the core module, can be used to store data such as startup code and user files.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-eMMC.png" width=70%>
</div>

<center>Figure 3-4 eMMC memory</center>

### 3.3.2 NandFlash

&emsp; &emsp; The K510 CRB includes 128M Bytes of NAND Flash memory, which can be used to store data such as startup code and user files.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_5.jpg " width=75%>
</div>

<center>Figure 3-5 NAND Flash memory</center>

### 3.3.2 TF Card

&emsp; &emsp; The K510 CRB has a TF card holder on board that can be connected externally to a TF card to store data such as startup code and user files.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_6.png">
</div>

<center>Figure 3-6 TF Card Holder</center>

<div style="page-break-after:always"></div>

## 3.4 Keystrokes

&emsp; &emsp; The K510 CRB contains two user touch buttons that allow users to customize the tap buttons to trigger as system inputs or other software-related functions.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_7.jpg" width=50%>
</div>

<center>Figure 3-7 Keys</center>

## 3.5 LEDs

&emsp; &emsp; The K510 CRB has a light-emitting diode on board that is connected directly to the GPIO pin of the K510 chip.

&emsp; &emsp; The K510 CRB is onboard a colored LED WS2812 that is connected directly to the GPIO pin of the K510 chip.

&emsp; &emsp; The two LEDs are custom programmed to light or extinguish and can be used as system outputs or software-related status indications.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_8.jpg" width=60%>
</div>

<center>Figure 3-8 LED</center>

<div style="page-break-after:always"></div>

## 3.6 Boot Mode and Reset

&emsp; &emsp; The K510 CRB has a variety of storage devices on board, and the boot mode is selected by configuring the levels of the boot pins, BOOT0 and BOOT1, with 0 and 1 representing low and high levels.

&emsp; &emsp; On the PCB, the startup mode is selected by the DIP switch shown in the following figure, and the core module has been designed to pull up BOOT0 and BOOT1, and the side of the on-dialing light marking ON represents the corresponding bit pull down effective, and the other side of ON corresponds to OFF represents the pull-up effective.

&emsp; &emsp; The K510 determines the chip boot mode by the status of the boot0 and BOOT1 hardware pins, and the boot mode selection is shown in the following table.

<center>Table 2-1 Boot modes</center>

| BOOT1   | BOOT0   | Startup mode      |
| ------- | ------- | ------------ |
| 0(ON)   | 0(ON)   | Serial port boot      |
| 0(ON)   | 1(OFF)  | The SD card boots      |
| 1(OFF)  | 0(ON)   | NANDFLASH boots |
| 1(OFF)  | 1(OFF)  | EMMC boots      |

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_9.jpg" width=60%>
</div>

<center>Figure 3-9 Reset switch and start mode DIP switch</center>

&emsp; &emsp; The K510 CRB on-board reset button is K2 in Figure 3-9, which can be pressed to perform a hardware reset operation of the system.

<div style="page-break-after:always"></div>

## 3.7 Audio input and output

&emsp; &emsp; The K510 CRB uses Nuvoton's audio codec chip, NAU88C22, to implement input and output functions for speech. Includes an onboard microphone, standard 3.5mm headphone jack and 2P speaker connector.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-10.jpg" width=60%>
</div>

<center>Figure 3-10 Audio</center>

## 3.8 USB OTG socket

&emsp; &emsp; The K510 CRB onboard USB OTG socket can be used to implement USB host/device functionality.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_11.jpg">
</div>

<center>Figure 3-11 USB-OTG seat</center>

<div style="page-break-after:always"></div>

## 3.9 UART interface

&emsp; &emsp; K510 CRB In order to facilitate user development and debugging, the K510 CRB has a USB-> UART interface on board, which can be operated by USART serial port communication and debugging of the K510 through the PC-USB cable. Initial use may require loading the driver, as detailed in Section 4.2. The on-board UART interface is shown in the figure below.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_12.jpg" width=50%>
</div>

<center>Figure 3-12 USB-UART interface</center>

## 3.10 WIFI/BT module

&emsp; &emsp; The K510 CRB includes a WIFI/BT 2-in-1 module AP6212 to extend the development board for network connectivity and Bluetooth communication functions, as shown in the on-board interface below.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-13.jpg" width=40%>
</div>

<center>Figure 3-13 WIFI/BT module</center>

<div style="page-break-after:always"></div>

## 3.11 Ethernet

&emsp; &emsp; The K510 CRB has an on-board Gigabit Ethernet holder, and the K510 is implemented via an external PHY chip with an RGMII interface. The on-board interface is shown in the following figure.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_14.jpg" width=60%>
</div>

<center>Figure 3-14 Ethernet interface</center>

## 3.12 hdmi output

&emsp; &emsp; The K510 CRB onboard HDMI-A female mount can be connected to the external display via a standard HDMI cable, using the K510's mipi dsi interface output conversion. The on-board interface is shown in the following figure.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_15.jpg" width=60%>
</div>

<center>Figure 3-15 HDMI interface</center>

 **Note**: Because both the HDMI and 1080P TFT displays use mipi dsi drivers, they can only choose one of the two displays, can not be used at the same time, switch through the control pin GPIO to select one of the outputs. 

<div style="page-break-after:always"></div>

## 3.13 Video In

&emsp; &emsp; The K510 CRB draws mipi CSI, DVP, power supply, and partial GPIO through a 0.8mm pitch board-to-board connector to achieve camera input in different scenarios and different demand situations. The on-board interface is shown in the following figure. The interface definitions are shown in the following table.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-16.jpg">
</div>

<center>Figure 3-16 Video IN interface</center>

<center>Table 3-2 Video IN interface definitions</center>

| numbering | definition             | numbering | definition                       |
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

**Note**: Pay attention to the level range of the connected pins when connecting externally to prevent the wrong voltage input from permanently damaging the K510 chip. 

<div style="page-break-after:always"></div>

## 3.14 Video Out

&emsp; &emsp; The K510 CRB has a 0.5mm pitch 30P flap under the FPC connector for connecting to an external LCD display, as shown in the figure below. The interface definitions are shown in the following table.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-17.jpg">
</div>

<center>Figure 3-17 Video Out interface</center>

<center>Table 3-3 Video Out interface definitions</center>

| numbering | definition              | numbering | definition             |
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

## 3.15 Extending the Interface

&emsp; &emsp; In order to facilitate the implementation of custom expansion functions for users, a 30P 2.54mm expansion pin is reserved on the K510 CRB, which leads to a power supply and part of the GPIO, which the user can operate through the software iomux to map hardware resources such as I2C, UART, SPI to the corresponding GPIO to achieve external connection and expansion of the corresponding functions. The on-board interface is shown in the following figure. The detailed definitions are shown in the following table.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw-3-18.jpg">
</div>

<center>Figure 3-18 40P pin extension interface</center>

<center>Table 3-4 Extended interface definitions</center>

| numbering | definition         | numbering | definition         |
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

**Note**: Pay attention to the level range of the connected pins when connecting externally to prevent the wrong voltage input from permanently damaging the K510 chip. 

<div style="page-break-after:always"></div>

# 4 Development board use

## 4.1 Installing the Driver

&emsp; &emsp; The K510 CRB has ch340E onboard to implement the USB-UART communication function, so the corresponding driver needs to be installed before use.

&emsp; &emsp; Use the driver in the package or download and install it at the following address.

&emsp;&emsp;<http://www.wch.cn/product/CH340.html>

## 4.2 Firmware burn

&emsp; &emsp; Please refer to[ the K510_SDK_Build_and_Burn_Guide ](./K510_SDK_Build_and_Burn_Guide.md)documentation. 

## 4.3 Switch on and off

&emsp; &emsp; 1) Install the power cable and USB debugging cable.

&emsp; &emsp; 2) DIP switch selected to start from TF card.

&emsp; &emsp; 3) Power on the switch by toggling the switch as shown in Section 3.2.

## 4.4 Serial port debugging

&emsp; &emsp; After the driver is installed, power-on the K510 CRB, at which point the port appears in the PC's Device Manager - Port.

&emsp; &emsp; Using the serial port debugging tool, open the port number of the device, baud rate 115200.

&emsp; &emsp; As shown in the following figure, the device is "COM6", which is shown in the PC Device Manager.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_4_1.jpg">
</div>

<center>Figure 4-1 Device Manager after driver installation is complete</center>

**Translation Disclaimer**  
For the convenience of customers, Canaan uses an AI translator to translate text into multiple languages, which may contain errors. We do not guarantee the accuracy, reliability or timeliness of the translations provided. Canaan shall not be liable for any loss or damage caused by reliance on the accuracy or reliability of the translated information. If there is a content difference between the translations in different languages, the Chinese Simplified version shall prevail. 

If you would like to report a translation error or inaccuracy, please feel free to contact us by mail.
