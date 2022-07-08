![](../zh/images/canaan-cover.png)
&nbsp;
&nbsp;
**<font face="黑体" size="6" style="float:right">K510 CRB V1.2 硬體指南</font>**

<font face="黑体" size=100>&nbsp;
&nbsp;
&nbsp;</font>

<font face="黑体"  size=3>文件版本：V1.0.0</font>

<font face="黑体"  size=3>發佈日期：2022-03-15</font>

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
**<font face="黑体"  size=5>文件目的</font>**
本文檔為K510 sdk的配套文檔，旨在幫助工程師瞭解 k510 sdk的編譯和燒錄。 

**<font face="黑体"  size=5>讀者物件</font>**

本文檔（本指南）主要適用的人員：

- 軟體開發人員
- 技術支持人員

**<font face="黑体"  size=5>修訂記錄</font>**
 <font face="宋体"  size=2>修訂記錄累積了每次文檔更新的說明。 最新版本的文件包含以前所有版本的更新內容。 </font>

| 版本號 | 修改者    | 修訂日期   | 修訂說明           |
| :----- | --------- | ---------- | ------------------ |
| 1.0.0 版 | AI 產品部 | 2022-03-15 | |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>目 錄</font>**

[目錄]

<div style="page-break-after:always"></div>

# 1 概述

&emsp; &emsp; K510 CRB是針對Canaan Kendryte K510 AI晶片開發的集參考設計、晶片調試和測試、使用者產品開發驗證一體的硬體開發平臺，用於展示K510晶元強大的算力和功能等。 同時為客戶提供基於K510晶元的硬體參考設計，使客戶不需修改或只需要簡單的修改參考設計的模組電路，就可以完成以K510晶元為核心的產品硬體開發工作。

&emsp; &emsp; K510 CRB支援K510晶元的硬體開發、應用軟體設計、調試和運行等，因為考慮到不同的使用環境，對晶元進行全功能驗證，所以各種介面齊全，設計相對完整。 K510 CRB 可以通過USB線纜與PC進行連接，作為一個基本開發系統使用，或實現更完全的開發系統和演示環境，連接如下設備和部件：

- 電源

- TF Card存放設備

- MIPI DSI LCD顯示幕

- MIPI CSI攝像頭模組

- DVP攝像頭模組

- 乙太網網線

- HDMI顯示幕

- 耳機或喇叭

- 拓展備件

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-K510_Core.png">
</div>

  <center>圖 1-1 K510 CRB 渲染圖</center>

    **禁止事项**

  1. 禁止帶電插拔核心模組及週邊模組！
  2. 禁止在沒有經釋放靜電或無靜電防護的措施下直接操作本產品。
  3. 禁止使用有機溶劑或者腐蝕性液體清洗本產品。
  4. 禁止進行敲打、扭曲等可能造成物理損傷的操作。

    **注意事項**

  1. 請注意對人體進行靜電釋放后，再操作本產品，建議佩戴靜電手環。
  2. 操作前請確認底板的供電電壓和適配器電壓在本文檔所描述的允許範圍內。
  3. 設計前請務必閱讀本文檔及工程檔中的注意事項。
  4. 注意產品在高溫、高濕、高腐蝕環境下使用需要進行散熱、排水、密封等特殊處理。
  5. 請勿自行維修、拆解，否則將無法享受免費的售後服務。

<div style="page-break-after:always"></div>

## 1.1 系統框圖

&emsp; &emsp; 系統框圖用於描述K510 CRB的設計原理和各部件之間的關係，以讓K510 CRB的使用和開發人員，能夠對整個系統的架構和原理有一個直觀的認識。

&emsp; &emsp; 關於K510功能詳情，請參考《K510 Full Datasheet》。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_1_2.png">
</div>

<center>圖 1-2 K510 CRB組成</center>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_1_3.png">
</div>

<center>圖 1-3 K510 CRB 系統框圖 </center>

<div style="page-break-after:always"></div>

&emsp; &emsp; K510 CRB 開發套件主要包括以下部件：

| 部件 | 數量 |
| :-: | :-: |
| K510 CRB主機板 | 1 |
| USB 型 C線纜 | 2 |
| Micro USB OTG線纜 | 1 |
| MIPI DSI顯示幕，解析度1920x1080 | 1 |
| MIPI CSI攝像頭子板，板載Sony IMX219 image sensor 兩顆 | 1 |
| 亞克力保護外殼 | 1 |

<div style="page-break-after:always"></div>

## 1.2 功能概述

&emsp; &emsp; K510 SDK是以buildroot為基本框架，以K510 linux kernel（linux版本4.17.0），u-boot（u-boot版本2020.01），riscv-pk-k510

&emsp; &emsp; K510 CRB V1.2（如果沒有特殊聲明，本文檔後續描述的CRB的版本都是V1.2）的主要功能如下：

- PMIC：電源管理
- 32 bit LPDDR3EE，總容量512MByte
- 8bit eMMC，總容量4GByte
- QSPI NAND，總容量 128MByte
- TF Card：支援外部擴展TF卡存儲。
- USB OTG：系統升級使用，支援Host/Device切換
- SDIO WIFI：支援無線上網功能和藍牙連接
- Audio：支援語音輸入輸出
- PDM MIC：VAD喚醒功能
- Uart &JTAG Debug： 開發板Debug使用
- Video Input： 雙路MIPI CSI 2lane攝像頭輸入
- Video Output： MIPI DSI 4lane，1080P顯示幕
- RGMII：千兆乙太網連接
- HDMI： 高清晰度多媒體介面
- 拓展介面：電源、GPIO、I2C、SPI
- 按鍵、指示燈

<div style="page-break-after:always"></div>

# 2 硬體資源介紹

## 2.1 整體效果圖

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_1.png" width=80%>
</div>

<center> 圖2-1 主機板正面圖 </center>

<div style="page-break-after:always"></div>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_2.png" width=80%>
</div>

<center> 圖2-1 主機板背面圖 </center>

<div style="page-break-after:always"></div>

## 2.2 結構與介面示意圖

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_3.png" width=120%>
</div>

<center> 圖2-3 主機板正面各器件位置 </center>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2-4.png" width=120%>
</div>

<center> 圖 2-4 主機板背面 </center>

<div style="page-break-after:always"></div>

## 2.3 電源框圖

&emsp; &emsp; K510 CRB使用DC-5V作為整板的輸入電源，為K510 CORE 核心模組提供DC-5V，同時通過兩個DC-DC為底板的其他外設提供1.8V和3.3V兩路電源。

## 2.4 I2C設備位址

<center>表2-1 I2C設備位址表</center>

| 名稱 | 管腳（SCL、SDA） | 位址 | 備註 |
| :-: | :-: | :-: | :-: |
| 觸摸屏 | IO_103、IO_102 | 0x14或0x5D | |
| 高清麥克風 | IO_117、IO_116 | 0x3B | |
| 音訊編解碼器 | IO_117、IO_116 | 0x1A | |
| MIPI CSI 相機0 | IO_120、IO_121 | 0x10 | |
| MIPI CSI 相機1 | IO_47、IO_48   | 0x10 | |

## 2.5 原理圖

&emsp; &emsp; K510 CRB開發板對應的參考原理圖請在[release](https://github.com/kendryte/k510_docs/releases)處下載。 

<div style="page-break-after:always"></div>

# 3 開發板各部分介紹

## 3.1 核心模組

&emsp; &emsp; 在使用K510 CRB進行學習和開發之前，建議先參考K510手冊中晶元的詳細架構，這樣可以對K510的供電、存儲、計算資源和外設等有更深入的瞭解，有利於晶元方案的熟悉和開發。 K510 核心板如圖3-1。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_1.png">
</div>

<center>圖3-1 K510 Core核心模組</center>

<div style="page-break-after:always"></div>

## 3.2 輸入電源

&emsp; &emsp; K510 CRB使用外部5V供電，板載了兩個USB type C介面，都可以為開發板進行供電，其中UART介面用於連接電腦，電腦的USB介面只能提供500mA電流，在遇到供電不足時，請同時使用適配器在DC：5V處供電。 介面如下圖所示。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_2.png" width=60%>
</div>

<center> 圖3-2 電源輸入介面 </center>

**注：限定使用5V電源，在使用快充適配器時，盡量不要同時連接手機等其它設備，以免造成快充適配器錯誤輸出高於5V的電源，導致開發板電源部分損壞。 **
&emsp; &emsp; 使用K2 撥動開關進行上電和掉電的操作，如下圖所示。 

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-3.jpg" width=50%>
</div>

<center>圖3-3 電源開關說明</center>

<div style="page-break-after:always"></div>

## 3.3 儲存設備

&emsp; &emsp; K510 CRB 板載了多種存儲設備，包括DDR、eMMC、NAND Flash和TF Card。

### 3.3.1 電子多元組

&emsp; &emsp; K510 CRB板載的一顆4G Bytes的eMMC記憶體，位於核心模組上，可以用於存儲啟動代碼和使用者檔等數據。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-eMMC.png" width=70%>
</div>

<center>圖3-4 eMMC記憶體</center>

### 3.3.2 南德閃光燈

&emsp; &emsp; K510 CRB 板載了128M Bytes的NAND Flash記憶體，可以用於存儲啟動代碼和使用者檔等數據。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_5.jpg " width=75%>
</div>

<center>圖3-5 NAND Flash記憶體</center>

### 3.3.2 TF卡

&emsp; &emsp; K510 CRB 板載了TF卡座，可以外接TF卡，用於存儲啟動代碼和使用者文件等數據。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_6.png">
</div>

<center>圖3-6 TF卡座</center>

<div style="page-break-after:always"></div>

## 3.4 按鍵

&emsp; &emsp; K510 CRB板載了兩顆使用者輕觸按鍵，用戶可以對輕觸按鍵進行自定義程式設計，作為系統輸入觸發或軟體相關的其他功能等。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_7.jpg" width=50%>
</div>

<center>圖3-7 按鍵</center>

## 3.5 指示燈

&emsp; &emsp; K510 CRB板載了一顆發光二極體，直接連接到了K510晶元的GPIO管腳上。

&emsp; &emsp; K510 CRB板載了一顆彩色發光二極管WS2812，直接連接到了K510晶元的GPIO管腳上。

&emsp; &emsp; 對兩顆指示燈進行自定義程式設計點亮或熄滅，可以作為系統輸出或軟體相關的狀態指示等功能。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_8.jpg" width=60%>
</div>

<center>圖3-8 指示燈</center>

<div style="page-break-after:always"></div>

## 3.6 啟動模式和複位

&emsp; &emsp; K510 CRB板載了多種存儲設備，通過配置啟動時 BOOT0 和 BOOT1 兩個管腳的電平來選擇啟動模式，0和1代表低電平和高電平。

&emsp; &emsp; PCB上通過下圖所示的撥碼開關選擇啟動模式，核心模組設計時已對 BOOT0 和 BOOT1 做了上拉設計，撥碼開光上標記ON的一側代表相應位拉低有效，ON對應的另一側OFF代表上拉有效。

&emsp; &emsp; K510 通過 BOOT0 和 BOOT1 兩個硬體管腳的狀態決定晶片啟動模式，啟動模式選擇如下表所示。

<center>表2-1 啟動模式</center>

| 啟動1   | BOOT0   | 啟動方式      |
| ------- | ------- | ------------ |
| 0（開）   | 0（開）   | 串口啟動      |
| 0（開）   | 1（關）  | SD卡啟動      |
| 1（關）  | 0（開）   | NANDFLASH啟動 |
| 1（關）  | 1（關）  | EMMC啟動      |

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_9.jpg" width=60%>
</div>

<center>圖3-9 複位開關和啟動模式撥碼開關</center>

&emsp; &emsp; K510 CRB板載複位按鍵為圖3-9 中的K2，按下可實現系統的硬體複位操作。

<div style="page-break-after:always"></div>

## 3.7 Audio 輸入輸出

&emsp; &emsp; K510 CRB使用了nuvoton公司的音訊編解碼器晶片NAU88C22，實現語音的輸入和輸出功能。 包括一顆板載麥克風、標準3.5mm耳機插座和2P揚聲器介面。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-10.jpg" width=60%>
</div>

<center>圖3-10 Audio</center>

## 3.8 USB OTG插座

&emsp; &emsp; K510 CRB 板載USB OTG插座，可以用來實現USB host/device功能。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_11.jpg">
</div>

<center>圖3-11 USB-OTG座</center>

<div style="page-break-after:always"></div>

## 3.9 UART介面

&emsp; &emsp; K510 CRB為了方便使用者開發和調試，板載了USB->UART介面，可以通過PC-USB線纜對K510進行UART串口通信和調試等操作。 初次使用可能會需要載入驅動，詳見4.2節。 板載UART介面如下圖所示。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_12.jpg" width=50%>
</div>

<center>圖3-12 USB-UART介面</center>

## 3.10 WIFI/BT模組

&emsp; &emsp; K510 CRB 板載了一顆WIFI/BT二合一模組AP6212，用於拓展開發板進行網路的連接和藍牙的通信功能，板載介面如下圖所示。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-13.jpg" width=40%>
</div>

<center>圖3-13 WIFI/BT模組</center>

<div style="page-break-after:always"></div>

## 3.11 乙太網

&emsp; &emsp; K510 CRB 板載千兆乙太網座，K510通過RGMII介面外接PHY晶元實現。 板載介面如下圖所示。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_14.jpg" width=60%>
</div>

<center>圖3-14 乙太網介面</center>

## 3.12 hdmi 輸出

&emsp; &emsp; K510 CRB板載HDMI-A母座，可以通過標準HDMI線纜連接外置顯示幕，使用K510的mipi dsi介面輸出轉換實現。 板載介面如下圖所示。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_15.jpg" width=60%>
</div>

<center>圖3-15 HDMI介面</center>

 **注意**：因為HDMI和1080P TFT顯示幕都是使用mipi dsi驅動，所以只能二選一顯示，無法同時使用，切換通過控制管腳GPIO來選擇其中之一輸出。 

<div style="page-break-after:always"></div>

## 3.13 視頻輸入

&emsp; &emsp; K510 CRB通過0.8mm 間距板對板連接器，將MIPI CSI、DVP、電源和部分GPIO等進行了引出，用於實現不同場景和不同需求情況下的攝像頭輸入。 板載介面如下圖所示。 介面定義如下表所示。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-16.jpg">
</div>

<center>圖3-16 Video IN介面</center>

<center>表3-2 Video IN介面定義</center>

| 編號 | 定義             | 編號 | 定義                       |
| ---- | ---------------- | ---- | --------------- |
| 1    | VDD_5V           | 60   | GPIO_1V8_59_DVP_D12      |
| 2    | VDD_5V           | 59   | GPIO_1V8_58_DVP_D11      |
| 3    | VDD_5V           | 58   | GPIO_1V8_50_DVP_D3       |
| 4    | VDD_5V           | 57   | GPIO_1V8_51_DVP_D4       |
| 5    | 斷續器              | 56   | GPIO_1V8_60_DVP_D13      |
| 6    | 斷續器              | 55   | GPIO_1V8_55_DVP_D8       |
| 7    | MIPI_CSI_D0_P    | 54   | GPIO_1V8_61_DVP_D14      |
| 8    | MIPI_CSI_D0_N    | 53   | GPIO_1V8_52_DVP_D5       |
| 9    | 斷續器              | 52   | GPIO_1V8_47_DVP_D0       |
| 10   | MIPI_CSI_CLK0_P  | 51   | GPIO_1V8_56_DVP_D9       |
| 11   | MIPI_CSI_CLK0_N  | 50   | GPIO_1V8_53_DVP_D6       |
| 12   | 斷續器              | 49   | GPIO_1V8_57_DVP_D10      |
| 13   | MIPI_CSI_D1_P    | 48   | GPIO_1V8_48_DVP_D1       |
| 14   | MIPI_CSI_D1_N    | 47   | GPIO_1V8_54_DVP_D7       |
| 15   | 斷續器              | 46   | GPIO_1V8_64_DVP_HREF     |
| 16   | MIPI_CSI_D2_N    | 45   | GPIO_1V8_49_DVP_D2       |
| 17   | MIPI_CSI_D2_P    | 44   | GPIO_1V8_65_DVP_DEN      |
| 18   | 斷續器              | 43   | GPIO_1V8_66_DVP_PCLK     |
| 19   | MIPI_CSI_CLK1_N  | 42   | GPIO_1V8_62_DVP_D15      |
| 20   | MIPI_CSI_CLK1_P  | 41   | GPIO_1V8_63_DVP_VSYNC    |
| 21   | 斷續器              | 40   | GPIO_1V8_82 |
| 22   | MIPI_CSI_D3_N    | 39   | GPIO_1V8_67  |
| 23   | MIPI_CSI_D3_P    | 38   | GPIO_1V8_68  |
| 24   | 斷續器              | 37   | GPIO_1V8_72  |
| 25   | MIPI_CSI_I2C_SCL | 36   | GPIO_1V8_73  |
| 26   | MIPI_CSI_I2C_SCA | 35   | GPIO_1V8_74  |
| 27   | 斷續器              | 34   | 斷續器          |
| 28   | 斷續器              | 33   | 斷續器          |
| 29   | 1V8              | 32   | 3V3          |
| 30   | 1V8              | 31   | 3V3          |

**注意**：外部連接時注意所連接管腳的電平範圍，防止錯誤的電壓輸入永久性損壞K510晶元。 

<div style="page-break-after:always"></div>

## 3.14 視頻輸出

&emsp; &emsp; K510 CRB板載了0.5mm間距30P的翻蓋下接FPC連接器，用於連接外部的LCD顯示幕，板載介面如下圖所示。 介面定義如下表所示。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-17.jpg">
</div>

<center>圖3-17 Video Out介面</center>

<center>表3-3 Video Out介面定義</center>

| 編號 | 定義              | 編號 | 定義             |
| ---- | ----------------- | ---- | ---------------- |
| 1    | 斷續器               | 16   | MIPI_DSI_D1_N    |
| 2    | 斷續器               | 17   | MIPI_DSI_D1_P    |
| 3    | VDD_5V            | 18   | 斷續器              |
| 4    | VDD_5V            | 19   | MIPI_DSI_CLK_N   |
| 5    | VDD_3V3           | 20   | MIPI_DSI_CLK_P   |
| 6    | VDD_3V3           | 21   | 斷續器              |
| 7    | 斷續器               | 22   | MIPI_DSI_D0_N    |
| 8    | TOUCH_1V8_I2C_SCL | 23   | MIPI_DSI_D0_P    |
| 9    | TOUCH_1V8_I2C_SDA | 24   | 斷續器              |
| 10   | TOUCH_1V8_INT     | 25   | MIPI_DSI_D3_N    |
| 11   | TOUCH_1V8_RST     | 26   | MIPI_DSI_D3_P    |
| 12   | 斷續器               | 27   | 斷續器              |
| 13   | MIPI_DSI_D2_N     | 28   | MIPI_DSI_LCD_RST |
| 14   | MIPI_DSI_D2_P     | 29   | MIPI_DSI_LCD_EN  |
| 15   | 斷續器               | 30   | 斷續器              |

<div style="page-break-after:always"></div>

## 3.15 拓展介面

&emsp; &emsp; 為了方便用戶進行自定義拓展功能的實現，在K510 CRB上預留了30P的2.54mm拓展排針，引出了包括電源和部分GPIO，用戶可通過軟體iomux操作，將I2C、UART、SPI等硬體資源映射到相應的GPIO上，以實現相應功能的外部連接和拓展。 板載介面如下圖所示。 詳細定義如下表所示。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw-3-18.jpg">
</div>

<center>圖3-18 40P排針拓展介面</center>

<center>表3-4 拓展介面定義</center>

| 編號 | 定義         | 編號 | 定義         |
| ---- | ------------ | ---- | ------------ |
| 1    | VDD_1V8      | 2    | 斷續器          |
| 3    | VDD_1V8      | 4    | 斷續器          |
| 5    | VDD_3V3      | 6    | 斷續器          |
| 7    | VDD_3V3      | 8    | 斷續器          |
| 9    | VDD_5V       | 10   | 斷續器          |
| 11   | VDD_5V       | 12   | GPIO_1V8_95  |
| 13   | GPIO_3V3_114 | 14   | GPIO_3V3_115 |
| 15   | GPIO_1V8_92  | 16   | GPIO_1V8_96  |
| 17   | GPIO_1V8_105 | 18   | GPIO_1V8_107 |
| 19   | GPIO_1V8_104 | 20   | GPIO_1V8_106 |
| 21   | GPIO_1V8_118 | 22   | GPIO_1V8_119 |
| 23   | GPIO_1V8_93  | 24   | GPIO_1V8_94  |
| 25   | GPIO_3V3_125 | 26   | GPIO_3V3_124 |
| 27   | GPIO_3V3_127 | 28   | GPIO_3V3_126 |
| 29   | 斷續器          | 30   | 斷續器          |

**注意**：外部連接時注意所連接管腳的電平範圍，防止錯誤的電壓輸入永久性損壞K510晶元。 

<div style="page-break-after:always"></div>

# 4 開發板使用

## 4.1 安裝驅動

&emsp; &emsp; K510 CRB板載了CH340E來實現USB-UART通信功能，所以在使用前，需要先安裝對應的驅動。

&emsp; &emsp; 使用資料包中的驅動程式或者在如下位址進行下載安裝即可。

&emsp;&emsp;<http://www.wch.cn/product/CH340.html>

## 4.2 固件燒錄

&emsp; &emsp; 請參考[K510_SDK_Build_and_Burn_Guide](./K510_SDK_Build_and_Burn_Guide.md)文檔。 

## 4.3 開關機

&emsp; &emsp; 1）安裝電源線和USB調試線。

&emsp; &emsp; 2）撥碼開關選擇從TF卡啟動。

&emsp; &emsp; 3）按照3.2節所示的方法撥動開關進行上電。

## 4.4 串口調試

&emsp; &emsp; 驅動安裝完成後，對K510 CRB進行上電操作，這時候，在PC的設備管理器-埠中會出現埠。

&emsp; &emsp; 使用串口調試工具，打開設備所的埠號，波特率115200。

&emsp; &emsp; 如下圖所示，設備為“COM6”，具體以PC設備管理器中顯示的情況為準。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_4_1.jpg">
</div>

<center>圖4-1 驅動安裝完成後的設備管理員</center>

**翻譯免責聲明**  
為方便客戶，Canaan 使用 AI 翻譯程式將文字翻譯為多種語言，它可能包含錯誤。 我們不保證提供的譯文的準確性、可靠性或時效性。 對於因依賴已翻譯信息的準確性或可靠性而造成的任何損失或損害，Canaan 概不負責。 如果不同語言翻譯之間存在內容差異，以簡體中文版本為準。 

如果您要報告翻譯錯誤或不準確的問題，歡迎通過郵件與我們聯繫。
