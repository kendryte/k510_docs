![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 U-boot 開發人員指南</font>**

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
本文檔為K510 demo板sdk配套文檔，主要介紹uboot相關內容，比如uboot下k510 demo板配置檔、設備樹、驅動位置等資訊。 

**<font face="黑体"  size=5>讀者物件</font>**

本文檔（本指南）主要適用的人員：

- 軟體開發人員
- 技術支持人員

**<font face="黑体"  size=5>修訂記錄</font>**
 <font face="宋体"  size=2>修訂記錄累積了每次文檔更新的說明。 最新版本的文件包含以前所有版本的更新內容。 </font>

| 版本號   | 修改者     | 修訂日期 | 修訂說明 |
|  :-----  |-------   |  ------  |  ------  |
| 1.0.0 版 | 系統軟體組 | 2022-03-09 |          |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>目 錄</font>**

[目錄]

<div style="page-break-after:always"></div>

# 1 U-Boot 簡介

u-boot是sdk的一部分，sdk目前使用的u-boot版本是2020.01。 Uboot是德國DENX小組的開發用於多種嵌入式CPU的bootloader程式， UBoot不僅僅支援嵌入式Linux系統的引導，當前，它還支援NetBSD， VxWorks， QNX， RTEMS， ARTOS， LynxOS嵌入式操作系統。 UBoot除了支援PowerPC系列的處理器外，還能支援MIPS、 x86、ARM、NIOS、RISICV等，主要功能有初始化記憶體，引導linux系統，更多u-boot介紹請參考<https://www.denx.de/wiki/U-Boot>

# 2 開發環境簡介

- 操作系統

| 編號 | 軟體資源 | 說明        |
| ---- | -------- | ----------- |
| 1    | 烏班圖   | 18.04/20.04 |

- 軟體環境

軟體環境要求如下表所示：

| 編號 | 軟體資源 | 說明 |
| ---- | -------- | ---- |
| 1    | K510 開發工具組 |      |

# 3 獲取方式

下載並編譯sdk，sdk編譯的時候會下載uboot代碼，並編譯uboot代碼。 sdk的下載編譯方法請參考[K510_SDK_Build_and_Burn_Guide.md](./K510_SDK_Build_and_Burn_Guide.md)

# 4 重要目錄和文件說明

本章以編譯k510_evb_lp3_v1_1_defconfig為例。 對應的sdk編譯方法是make CONF=k510_evb_lp3_v1_1_defconfig，其編譯完后目錄如下：

![圖片-20210930135634105](../zh/images/uboot_guides/build_out.png)

k510_evb_lp3_v1_1_defconfig/build/uboot-custom ---uboot的代碼和編譯目錄;

board/canaan/k510/uboot-sdcard.env---uboot默認環境變數配置檔

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/configs/k510_evb_lp3_v1_1_defconfig --uboot配置檔;

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/arch/riscv/dts/k510_evb_lp3_v1_1.dts----設備樹檔;

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/include/configs/k510_evb_lp3_v1_1.h---頭檔;

k510_evb_lp3_v1_1_defconfig/images/u-boot_burn.bin ---uboot燒寫固件

buildroot-2020.02.11/boot/uboot ----buildroot裡面關於uboot的編譯腳本，一般不需修改;

configs/k510_evb_lp3_v1_1_defconfig---sdk的配置檔，BR2_TARGET_UBOOT_BOARD_DEFCONFIG指定uboot的配置檔;

# 5 uboot啟動流程

_start（arch/riscv/cpu/start.S，第 43 行）

board_init_f（通用/board_f.c，第1013行）

board_init_r（普通/board_r.c，第845行）

run_main_loop（通用/board_r.c，第637行）

# 6 uboot下驅動說明

## 6.1 ddr驅動

板/迦南/k510_evb_lp3/ddr_init.c

## 6.2 eth驅動

drivers/net/macb.c

裝置樹：

```text
ethernet@93030000 {
    compatible = "cdns,macb";
    reg = <0x0 0x93030000 0x0 0x10000>;
    phy-mode = "rmii";
    interrupts = <0x36 0x4>;
    interrupt-parent = <0x4>;
    clocks = <0x5 0x5>;
    clock-names = "hclk", "pclk";
};
```

## 6.3 串口驅動

驅動程式/串行/ns16550.c

裝置樹：

```text
serial@96000000 {
    compatible = "andestech,uart16550", "ns16550a";
    reg = <0x0 0x96000000 0x0 0x1000>;
    interrupts = <0x19 0x4>;
    clock-frequency = <0x17d7840>;
    reg-shift = <0x2>;
    reg-io-width = <0x4>;
    no-loopback-test = <0x1>;
    interrupt-parent = <0x4>;
};
```

## 6.4 碘

drivers/pinctrl/pinctrl-single.c

裝置樹：

```text
iomux@97040000 {
    compatible = "pinctrl-single";
    reg = <0x0 0x97040000 0x0 0x10000>;
    #address-cells = <0x1>;
    #size-cells = <0x0>;
    #pinctrl-cells = <0x1>;
    pinctrl-single,register-width = <0x20>;
    pinctrl-single,function-mask = <0xffffffff>;
    pinctrl-names = "default";
    pinctrl-0 = <0x6 0x7 0x8 0x9 0xa>;

    iomux_uart0_pins {
        pinctrl-single,pins = <0x1c0 0x540ca8 0x1c4 0x5a0c69>;
        phandle = <0x6>;
    };

    iomux_emac_pins {
        pinctrl-single,pins = <0x8c 0x4e 0x90 0xce 0x88 0x8e 0x98 0x4e 0x80 0x8e 0xb8 0x4e 0xb4 0x4e 0xa8 0x8e 0xa4 0x8e 0x74 0x8e>;
        phandle = <0x7>;
    };

    iomux_spi0_pins {
        pinctrl-single,pins = <0x158 0x4e 0x15c 0x4e 0x160 0xce 0x164 0xce 0x168 0xce 0x16c 0xce 0x170 0xce 0x174 0xce 0x178 0xce 0x17c 0xce 0x180 0x8e>;
        phandle = <0x8>;
    };

    iomux_mmc0_pins {
        pinctrl-single,pins = <0x1c 0x4e 0x20 0xce 0x24 0xce 0x28 0xce 0x2c 0xce 0x30 0xce 0x34 0xce 0x38 0xce 0x3c 0xce 0x40 0xce>;
        phandle = <0x9>;
    };

    iomux_mmc2_pins {
        pinctrl-single,pins = <0x5c 0x4e 0x60 0xce 0x64 0xce 0x68 0xce 0x6c 0xce 0x70 0xce>;
        phandle = <0xa>;
    };
};
```

## 6.5 mmc和sd卡驅動

drivers/mmc/sdhci-cadence.c

設備樹

```text
mmc0@93000000 {
    compatible = "socionext,uniphier-sd4hc", "cdns,sd4hc";
    reg = <0x0 0x93000000 0x0 0x400>;
    interrupts = <0x30 0x4>;
    interrupt-parent = <0x4>;
    clocks = <0xb 0x4>;
    max-frequency = <0xbebc200>;
    cap-mmc-highspeed;
    bus-width = <0x8>;
};

mmc2@93020000 {
    compatible = "socionext,uniphier-sd4hc", "cdns,sd4hc";
    reg = <0x0 0x93020000 0x0 0x400>;
    interrupts = <0x32 0x4>;
    interrupt-parent = <0x4>;
    clocks = <0xb 0x4>;
    max-frequency = <0xbebc200>;
    cap-sd-highspeed;
    bus-width = <0x1>;
};
```

# 7 Uboot預設環境變數

uboot的預設環境變數在SDK的board/canaan/k510目錄下，用文本文件預定義：

uboot-emmc.env

uboot-nfs.env

uboot-sdcard.env

SDK的post腳本會在編譯的時候調用mkenvimage將文本的環境變數定義編譯為uboot可以載入的二進位鏡像，放在啟動分區中。

舉例如下：

uboot-sdcard.env

```text
bootm_size=0x2000000
bootdelay=3

stderr=serial@96000000
stdin=serial@96000000
stdout=serial@96000000
arch=riscv
baudrate=115200

ipaddr=10.100.226.221
netmask=255.255.255.0
gatewayip=10.100.226.254
serverip=10.100.226.63
bootargs=root=/dev/mmcblk1p2 rw console=ttyS0,115200n8 debug loglevel=7

bootcmd=fatload mmc 1:1 0x600000 bootm-bbl.img;fatload mmc 1:1 0x2000000 k510.dtb;bootm 0x600000 - 0x2000000
bootcmd_nfs=tftp 0x600000 bootm-bbl.img;tftp 0x2000000 k510_nfsroot.dtb;bootm 0x600000 - 0x2000000
```

注：內核啟動參數bootargs由uboot的默認環境變數設置，dts中的bootargs將會被覆蓋。 詳見 常見問題-bootargs 哪裡獲取並傳給內核的？

# 8 Uboot程式更新

## 8.1 燒寫sdk鏡像方法

sdk鏡像裡面已經包含uboot程式，直接燒寫sdk鏡像，比如：k510_evb_lp3_v1_1_defconfig/images/sysimage-sdcard.img檔

## 8.2 linux下更新sd卡裡面的uboot程式

把u-boot_burn.bin檔放到tftp目錄，配置設備網口ip地址，進入/root/sd/p1目錄; 執行tftp -gr u-boot_burn.bin xxx.xxx.xxx.xx 命令;

## 8.3 linux更新emmc裡面的uboot程式

把u-boot_burn.bin檔放到tftp目錄，配置設備網口ip位址;通過tftp -gr u-boot_burn.bin xxx.xxx.xxx.xx下載檔到設備;

執行dd if=u-boot_burn.bin of=/dev/mmcblk0p1 命令把檔寫到mmc卡。

# 9 常見問題

## 9.1 DDR 頻率如何配置？

答：目前evb只能跑800，CRB可以設置800或1600。 CRB板子ddr頻率設置方法見uboot的board\Canaan\k510_crb_lp3\ddr_param.h檔，800M對應#define DDR_800 1，1600M對應#define DDR_1600 1。

## 9.2 bootargs 哪裡獲取並傳給內核的？

答：從uboot環境變數bootargs 獲取，uboot引導內核時會根據bootargs 環境變數值，修改記憶體設備樹裡面的bootargs參數。 相關代碼如下：

```c
int fdt_chosen(void *fdt)
{
    int   nodeoffset;
    int   err;
    char  *str; /* used to set string properties */

    err = fdt_check_header(fdt);
    if (err < 0) {
        printf("fdt_chosen: %s\n", fdt_strerror(err));
        return err;
    }

    /* find or create "/chosen" node. */
    nodeoffset = fdt_find_or_add_subnode(fdt, 0, "chosen");
    if (nodeoffset < 0)
        return nodeoffset;

    str = env_get("bootargs");
    if (str) {
        err = fdt_setprop(fdt, nodeoffset, "bootargs", str,
                    strlen(str) + 1);
        if (err < 0) {
            printf("WARNING: could not set bootargs %s.\n",
                    fdt_strerror(err));
            return err;
        }
    }

    return fdt_fixup_stdout(fdt, nodeoffset);
}
```

## 9.3 啟動參數和編譯的設備樹檔不一致？

答：uboot根據啟動方式動態獲取環境變數，引導內核時根據bootargs環境變數，更新記憶體裡面的設備樹。 修改完後的啟動參數見/sys/firmware/devicetree/base/chosen節點。

## 9.4 uboot環境變數保存在那裡？

答：

| 啟動方式 | uboot讀取和保存位置 | 編譯時對應檔 |
| :-: | :-: | :-: |
| emmc啟動 | emmc第二個分區的uboot-emmc.env檔 | board\canaan\k510\uboot-emmc.env |
| sd卡啟動 | sd卡第一個分區的uboot-sd.env檔 | board\canaan\k510\uboot-sd.env |

## 9.5 qos如何設置？

答：qos相關寄存器是QOS_CTRL0 QOS_CTRL1 QOS_CTRL2 QOS_CTRL3 QOS_CTRL4 。 例子：
設置qos后，nncase demo性能有所提高

```c
*(uint32_t *)0x970E00FC = (0x2 << 8) | (0x2 << 12) | (0x2 << 16) | (0x2 << 20) | (0x2 << 24);
*(uint32_t *)0x970E0100 = (0x3 << 4) | 0x3;
*(uint32_t *)0x970E00F4 = (0x5 << 16) | (0x5 << 20);
```

**翻譯免責聲明**  
為方便客戶，Canaan 使用 AI 翻譯程式將文字翻譯為多種語言，它可能包含錯誤。 我們不保證提供的譯文的準確性、可靠性或時效性。 對於因依賴已翻譯信息的準確性或可靠性而造成的任何損失或損害，Canaan 概不負責。 如果不同語言翻譯之間存在內容差異，以簡體中文版本為準。 

如果您要報告翻譯錯誤或不準確的問題，歡迎通過郵件與我們聯繫。