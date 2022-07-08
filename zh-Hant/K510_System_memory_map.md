![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 系統記憶體映射</font>**

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
**<font face="黑体"  size=5>文件目的</font>**
本文檔為K510 SDK 應用實例的說明文檔。 

**<font face="黑体"  size=5>讀者物件</font>**

本文檔（本指南）主要適用的人員：

- 軟體開發人員
- 技術支持人員

**<font face="黑体"  size=5>修訂記錄</font>**
 <font face="宋体"  size=2>修訂記錄累積了每次文檔更新的說明。 最新版本的文件包含以前所有版本的更新內容。 </font>

| 版本號   | 修改者     | 修訂日期 | 修訂說明 |
|  :-----  |-------   |  ------  |  ------  |
| 1.0.0 版 | 系統軟體組 | 2022-03-09 |   |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>目 錄</font>**

[目錄]

<div style="page-break-after:always"></div>

# 1 K510 系統記憶體規劃

K510的記憶體規劃如下圖所示：

![](../zh/images/system_memory_map/k510-system-memory-map.png)

K510 crb參考板上有512MB DDR，總共規劃了四個區域：

- 0~240M規劃給Linux kernel
- 240M~496MB規劃給share memory，採用預留CMA記憶體池的方式，這樣在Share memory沒有使用的情況下，Linux kernel記憶體管理子系統也可以從CMA池中分配記憶體
- 496M~510M規劃給DSP使用
- 510M~512M規劃給logo使用

# 2 設備樹描述

K510的記憶體規劃採用reserved-meory的方式，通過設備樹的reserved-memory節點進行描述。 相關設備樹節點資訊如下：

```text
ddr_memory: memory@0 {
    status              = "okay";
    device_type         = "memory";
    reg                 = <0x0 0x00000000 0x0 0x20000000>;
};

sharem_cma:sharem_cma@8000000 {
    compatible          = "k510-share-memory-cma";
    reg                 = <0x0 0xf000000 0x0 0x10000000>;  /*240M~496M*/
};

reserved-memory {
    #address-cells = <2>;
    #size-cells = <2>;
    ranges;

    cma_buffer: buffer@f000000 {
        compatible = "shared-dma-pool";
        reusable;
        linux,cma-default;
        reg = <0x0 0xf000000 0x0 0x10000000>;
    };

    dsp_buffer: buffer@1f000000 {
        no-map;
        reg = <0x0 0x1f000000 0x0 0xe00000>;
    };

    logo_buffer: buffer@1fe00000 {
        no-map;
        reg = <0x0 0x1fe00000 0x0 0x200000>;
    };
};
```

# 3 Buildroot相關配置

系統記憶體規劃全部在linux kernel的dts中描述，但是dsp firmware的載入位址需要在buildroot中配置：

設定/k510_crb_lp3_v0_1_defconfig：

設定/k510_crb_lp3_v1_2_defconfig：

BR2_TARGET_EVB_FIRMWARE_LOAD_ADD=0x1f000000

**翻譯免責聲明**  
為方便客戶，Canaan 使用 AI 翻譯程式將文字翻譯為多種語言，它可能包含錯誤。 我們不保證提供的譯文的準確性、可靠性或時效性。 對於因依賴已翻譯信息的準確性或可靠性而造成的任何損失或損害，Canaan 概不負責。 如果不同語言翻譯之間存在內容差異，以簡體中文版本為準。 

如果您要報告翻譯錯誤或不準確的問題，歡迎通過郵件與我們聯繫。