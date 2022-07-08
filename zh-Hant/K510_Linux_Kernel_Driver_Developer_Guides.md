![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 Linux 內核驅動程式開發人員指南</font>**

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
本文檔為K510 sdk的配套文檔，本文檔主要講linux相關驅動、配置、調試等

**<font face="黑体"  size=5>讀者物件</font>**

本文檔（本指南）主要適用的人員：

- 軟體開發人員
- 技術支持人員

**<font face="黑体"  size=5>修訂記錄</font>**
 <font face="宋体"  size=2>修訂記錄累積了每次文檔更新的說明。 最新版本的文件包含以前所有版本的更新內容。 </font>

| 版本號   | 修改者     | 修訂日期 | 修訂說明 |
|  :-----  |-------   |  ------  |  ------  |
| 1.0.0 版 | 系統軟體組 | 2022-03-09 | SDK V1.5發佈 |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>目 錄</font>**

[目錄]

<div style="page-break-after:always"></div>

# 1 Linux Kernel簡介

目前sdk使用的linux版本是4.17.0。 Linux，全稱GNU/Linux，是一種免費使用和自由傳播的類UNIX操作系統，其內核由林納斯·本納第克特·托瓦茲於1991年10月5日首次發佈，它主要受到Minix和Unix思想的啟發，是一個基於POSIX的多使用者、多任務、支援多線程和多CPU的操作系統。 它能運行主要的Unix工具軟體、應用程式和網路協定。 它支援32位和64位硬體。 Linux繼承了Unix以網路為核心的設計思想，是一個性能穩定的多用戶網路操作系統。 Linux有上百種不同的發行版，如基於社區開發的debian、archlinux，和基於商業開發的Red Hat Enterprise Linux、SUSE、Oracle Linux等。

瞭解更多Linux kernel的相關資料，請訪問：<https://docs.kernel.org/>

## 1.1 獲取方式

下載並編譯sdk，sdk編譯的時候會下載並編譯linux代碼。

sdk的下載編譯方法請參考[K510_SDK_Build_and_Burn_Guide](./K510_SDK_Build_and_Burn_Guide.md)。 

## 1.2開發環境需求

- 操作系統

| 編號 | 軟體資源 | 說明        |
| ---- | -------- | ----------- |
| 1    | 烏班圖   | 18.04/20.04 |

- 軟體環境要求如下表所示：

| 編號 | 軟體資源 | 說明 |
| ---- | -------- | ---- |
| 1    | K510 開發工具組 | 版本1.5 |

# 2 內核預設配置檔及dts

預設的內核設定檔路徑：

arch/riscv/configs/k510_defconfig

kernel支持兩個開發板 K510 CRB 和EVB，相應的dts檔如下：

arch/riscv/boot/dts/canaan/k510_crb_lp3_v0_1.dts

arch/riscv/boot/dts/canaan/k510_evb_lp3_v1_1.dts

在arch/riscv/boot/dts/canaan/k510_common目錄下存放的是soc級公共dts定義。

# 3調試

## 3.1 使用JTAG調試linux內核

1. 安裝Andesight v3.2.1
2. 進入andesight安裝目錄下ice目錄，運行ICEMAN

    ```shell
    #ICEman -Z v5 --smp
    ```

3. 使用gdb調試，這裡以 /dev/mem 內核代碼driver/char/mem.c為例

    ```shell
    riscv64-linux-gdb --eval-command="target remote 192.168.200.100:1111"
    (gdb) symbol-file vmlinux
    (gdb) hbreak mmap_mem
    ```

4. 應用程式打開/dev/mem，調用mmap後進入斷點

# 4 驅動說明

## 4.1 UART

設定選項：

```shell
CONFIG_SERIAL_8250_DW
```

驅動檔案：

```shell
/tty/serial/8250
```

裝置樹：

```text
serial@96000000 {
    status = "okay";
    #address-cells = <0x2>;
    #size-cells = <0x2>;
    compatible = "snps,dw-apb-uart";
    reg = <0x0 0x96000000 0x0 0x100>;
    interrupt-parent = <0x6>;
    interrupts = <0x1 0x4>;
    resets = <0x4 0x58 0x1 0x1f 0x0>;
    reset-names = "uart0_rst";
    power-domains = <0x5 0x6>;
    clock-frequency = <0x17d7840>;
    reg-shift = <0x2>;
    reg-io-width = <0x4>;
    no-loopback-test = <0x1>;
    pinctrl-names = "default";
    pinctrl-0 = <0x1f>;
};
```

API：裝置檔案節點：

```shell
/dev/ttyS0
/dev/ttyS1/2/3    #目前dts中disable
```

程式設計介面：標準串口驅動，參考Linux man page

```shell
man termios
```

## 4.2 乙太幣

設定選項：

```shell
CONFIG_NET_CADENCE
```

驅動檔案：

```shell
drivers/net/ethernet/cadence
```

裝置樹：

```text
emac@93030000 {
    status = "okay";
    compatible = "cdns,k510-gem";
    reg = <0x0 0x93030000 0x0 0x10000>;
    interrupt-parent = <0x6>;
    interrupts = <0x36 0x4 0x37 0x4 0x38 0x4>;
    clocks = <0x1b 0x1b 0x1b 0x1b 0x1b 0x1b>;
    clock-names = "hclk", "pclk", "ether_clk", "tx_clk", "rx_clk", "tsu_clk";
    clock-config = <0x97001104>;
    resets = <0x4 0xe4 0x1 0x1f 0x0>;
    reset-names = "emac_rst";
    power-domains = <0x5 0x5>;
    phy-mode = "rgmii";
    pinctrl-names = "default";
    pinctrl-0 = <0x1c>;
};
```

設備：`eth0`
Api說明：標準網口驅動，請參考tcp/ip socket程式設計; 

網口ip配置：

```shell
ifconfig eth0 xxx.xxx.xxx.xxx
```

## 4.3 環境管理委員會

設定選項：

```shell
CONFIG_MMC_SDHCI_CADENCE
```

驅動檔案：

```shell
drivers/mmc/host/sdhci-cadence.c
```

裝置樹：

```text
sdio@93000000 {
    status = "okay";
    compatible = "socionext,uniphier-sd4hc", "cdns,sd4hc";
    reg = <0x0 0x93000000 0x0 0x2000>;
    interrupt-parent = <0x6>;
    interrupts = <0x30 0x4>;
    clocks = <0x14>;
    max-frequency = <0x2faf080>;
    resets = <0x4 0xc8 0x1 0x1f 0x0>;
    reset-names = "sdio0_rst";
    power-domains = <0x5 0x5>;
    bus-width = <0x8>;
    pinctrl-names = "default";
    pinctrl-0 = <0x15>;
};
```

設備和分區：

```shell
[root@k510-test ~ ]$ ls -l /dev/ | grep mmcblk0
brw------- 179,  0 Jan 1 1970 mmcblk0      # emmc
brw------- 179,  8 Jan 1 1970 mmcblk0boot0
brw------- 179, 16 Jan 1 1970 mmcblk0boot1
brw------- 179,  1 Jan 1 1970 mmcblk0p1    # emmc第一个分区(boot)
brw------- 179,  2 Jan 1 1970 mmcblk0p2    # emmc第二个分区(kenrel,env,vfat)
brw------- 179,  3 Jan 1 1970 mmcblk0p3    # emmmc第三个分区(rootfs文件系统，ext2)
```

驅動API：標準驅動，當成普通文件讀寫就可以。

## 4.4 SD 卡

設定選項：

```shell
CONFIG_MMC_SDHCI_CADENCE
```

驅動檔案：

```shell
drivers/mmc/host/sdhci-cadence.c
```

裝置樹：

```text
sdio@93020000 {
    status = "okay";
    compatible = "socionext,uniphier-sd4hc", "cdns,sd4hc";
    reg = <0x0 0x93020000 0x0 0x2000>;
    interrupt-parent = <0x6>;
    interrupts = <0x32 0x4>;
    clocks = <0x19>;
    max-frequency = <0x2faf080>;
    resets = <0x4 0xd0 0x1 0x1f 0x0>;
    reset-names = "sdio2_rst";
    power-domains = <0x5 0x5>;
    bus-width = <0x4>;
    cap-sd-highspeed;
    cdns,phy-input-delay-legacy = <0xf>;
    cdns,phy-input-delay-sd-highspeed = <0xf>;
    pinctrl-names = "default";
    pinctrl-0 = <0x1a>;
};
```

裝置：

```shell
[root@k510-test ~ ]$ ls -l /dev/ | grep mmcblk1
brw------- 179, 24 mmcblk1      # sd卡设备
brw------- 179, 25 mmcblk1p1    # sd卡第一个分区(boot,kenrel,env,vfat)
brw------- 179, 26 mmcblk1p2    # sd卡第二个分区(rootfs文件系统，ext2)
brw------- 179, 27 mmcblk1p3    # sd卡第三个分区(用户分区)
```

驅動API：標準驅動，當成普通文件讀寫就可以。

## 4.5 WDT

設定選項：

```shell
CONFIG_DW_WATCHDOG
```

驅動檔案：

```shell
drivers/watchdog/dw_wdt.c
```

裝置樹：

```text
wdt@97010000 {
    status = "okay";
    compatible = "snps,dw-wdt";
    reg = <0x0 0x97010000 0x0 0x100>;
    clocks = <0x44>;
    resets = <0x4 0x40 0x2 0x0 0x3>;
    reset-names = "wdt0_rst";
};

wdt@97020000 {
    status = "okay";
    compatible = "snps,dw-wdt";
    reg = <0x0 0x97020000 0x0 0x100>;
    clocks = <0x45>;
    resets = <0x4 0x40 0x2 0x0 0x4>;
    reset-names = "wdt1_rst";
};

wdt@97030000 {
    status = "okay";
    compatible = "snps,dw-wdt";
    reg = <0x0 0x97030000 0x0 0x100>;
    clocks = <0x46>;
    resets = <0x4 0x40 0x2 0x0 0x5>;
    reset-names = "wdt2_rst";
};
```

API：裝置檔案節點：

```shell
/dev/watchdog
/dev/watchdog0/1/2
```

程式設計介面：linux檔IO（open， close ， ioctl），詳見Linux man page
內核源碼自帶文檔：`Documentation/watchdog/watchdog-api.txt`

## 4.6 脈寬調製

設定選項：

```shell
CONFIG_PWM_GPIO
CONFIG_PWM_CANAAN
```

驅動檔案：

```shell
drivers/pwm/pwm-canaan.c
drivers/pwm/pwm-gpio.c
```

裝置樹：

```text
pwm0@970f0000 {
    status = "okay";
    compatible = "canaan,k510-pwm";
    reg = <0x0 0x970f0000 0x0 0x40>;
    clocks = <0x55>;
    clock-names = "pwm";
    resets = <0x4 0x40 0x2 0x0 0xb>;
    reset-names = "pwm_rst";
    pinctrl-names = "default";
    pinctrl-0 = <0x56>;
};

pwm1@970f0000 {
    status = "okay";
    compatible = "canaan,k510-pwm";
    reg = <0x0 0x970f0040 0x0 0x40>;
    clocks = <0x55>;
    clock-names = "pwm";
    resets = <0x4 0x40 0x2 0x0 0xb>;
    reset-names = "pwm_rst";
    pinctrl-names = "default";
    pinctrl-0 = <0x57>;
};
```

API：pwm驅動在用戶態可以通過sysfs訪問， `/sys/class/pwm/`

程式設計介面：Linux檔IO（open，read， write），詳見Linux man page

內核源碼自帶文檔：`Documentation/pwm.txt`

## 4.7 I2C

設定選項：

```shell
CONFIG_I2C_DESIGNWARE_CORE
CONFIG_I2C0_TEST_DRIVER
```

驅動檔案：

```shell
drivers/misc/canaan/i2c/test-i2c0.c
drivers/i2c/busses/i2c-designware-platdrv.c
```

裝置樹：

```text
i2c@97060000 {
    status = "disable";
    compatible = "snps,designware-i2c";
    reg = <0x0 0x97060000 0x0 0x100>;
    interrupt-parent = <0x6>;
    interrupts = <0xc 0x4>;
    clocks = <0x48>;
    clock-frequency = <0x186a0>;
    resets = <0x4 0x40 0x2 0x0 0x0>;
    reset-names = "i2c0_rst";
};
```

API： I2C驅動屬於總線驅動，使用Linux kernel I2C子系統框架實現。 用戶態可以通過sysfs訪問，也可以使用i2c-tools等用戶態工具程式。

```shell
/sys/bus/i2c/devices/
```

程式設計介面：linux檔IO（open，read， write），詳見Linux man page
內核源碼自帶文檔：`Documentation/i2c/dev-interface`

## 4.8 USB OTG

設定選項：

```shell
USB_CANAAN_OTG20
```

驅動：

```shell
drivers/usb/canaan_otg20/core_drv_mod
```

裝置樹：

```text
usb@93060000 {
    status = "okay";
    compatible = "Cadence,usb-dev1.00";
    reg = <0x0 0x93060000 0x0 0x10000>;
    interrupt-parent = <0x6>;
    interrupts = <0x2d 0x4 0x2e 0x4>;
    resets = <0x4 0x18c 0x1 0x1f 0x0>;
    reset-names = "usb_rst";
    power-domains = <0x5 0xc>;
    otg_power_supply-gpios = <0x13 0x10 0x0>;
};
```

USB作為host，可以掛載U盤，作為device，可以當作U盤。

## 4.9 斷續器

設定選項：

```shell
CONFIG_COMMON_CLK_CAN_K510
```

驅動檔案：

```shell
drivers/reset/canaan/reset-k510.c
```

裝置樹：

```shell
arch/riscv/boot/dts/canaan/k510_common/clock_provider.dtsi
arch/riscv/boot/dts/canaan/k510_common/clock_consumer.dtsi
```

- `clock_provider.dtsi`中定義所有時鐘節點
- `clock_consumer.dtsi`中在各個驅動dts節點引用

## 4.10 電源

設定選項：

```shell
CONFIG_CANAAN_PM_DOMAIN
```

驅動檔案：

```shell
drivers/soc/canaan/k510_pm_domains.c
```

裝置樹：

```shell
arch/riscv/boot/dts/canaan/k510_common/power_provider.dtsi
arch/riscv/boot/dts/canaan/k510_common/power_consumer.dtsi
```

```text
sysctl_power@97003000 {
    status = "okay";
    compatible = "canaan, k510-sysctl-power";
    reg = <0x0 0x97003000 0x0 0x1000>;
    #power-domain-cells = <0x1>;
    phandle = <0x5>;
};
```

- `power_provider.dtsi` 定義了provider的dts節點
- `include/dt-bindings/soc/canaan,k510_pm_domains.h` 中定義了全部電源域
- `power_consumer.dtsi`中在驅動各自dts節點中引用

## 4.11 複位

設定選項：

```shell
CONFIG_COMMON_RESET_K510
```

驅動檔案：

```shell
drivers/reset/canaan/reset-k510.c
```

裝置樹：

```shell
arch/riscv/boot/dts/canaan/k510_common/reset_provider.dtsi
arch/riscv/boot/dts/canaan/k510_common/reset_consumer.dtsi
```

```text
sysctl_reset@97002000 {
    status = "okay";
    compatible = "canaan,k510-sysctl-reset";
    reg = <0x0 0x97002000 0x0 0x1000>;
    #reset-cells = <0x4>;
    phandle = <0x4>;
};
```

- `reset_provider.dtsi` 定義了provider的dts節點
- `include/ dt-bindings/reset/canaan-k510-reset.h` 中定義了全部reset信號
- `reset_consumer.dtsi`中在驅動各自dts節點中引用

## 4.12 PINCTL

設定選項：

```shell
CONFIG_PINCTRL_K510
```

驅動檔案：

```shell
drivers/pinctrl/canaan
```

相關設備樹：

```shell
arch/riscv/boot/dts/canaan/k510_common/iomux_provider.dtsi
arch/riscv/boot/dts/canaan/k510_common/iomux_consumer.dtsi
```

```text
iomux@97040000 {
    status = "okay";
    compatible = "pinctrl-k510";
    reg = <0x0 0x97040000 0x0 0x1000>;
    resets = <0x4 0x40 0x2 0x0 0x9>;
    reset-names = "iomux_rst";
    #pinctrl-cells = <0x1>;
    pinctrl-k510,register-width = <0x20>;
    pinctrl-k510,function-mask = <0xffffffff>;

    iomux_emac_pins {
        pinctrl-k510,pins = <0x23 0x23012d 0x24 0x24012e 0x22 0x22012c 0x26 0x260132 0x20 0x20012a 0x2e 0x2e013a 0x2d 0x2d0139 0x2a 0x2a0136 0x29 0x290135 0x1d 0x1d0126>;
    };

    iomux_mmc0_pins {
        pinctrl-k510,pins = <0x7 0x70107 0x8 0x80108 0x9 0x90109 0xa 0xa010a 0xb 0xb010b 0xc 0xc010c 0xd 0xd010d 0xe 0xe010e 0xf 0xf010f 0x10 0x100110>;
        phandle = <0x15>;
    };

    iomux_mmc2_pins {
        pinctrl-k510,pins = <0x17 0x170117 0x18 0x180118 0x19 0x190119 0x1a 0x1a011a 0x1b 0x1b011b 0x1c 0x1c011c>;
        phandle = <0x1a>;
    };

    iomux_uart0_pins {
        pinctrl-k510,pins = <0x70 0x54 0x71 0x5a>;
        phandle = <0x1f>;
    };

    iomux_uart1_pins {
        pinctrl-k510,pins = <0x72 0x64 0x73 0x6a>;
        phandle = <0x20>;
    };

    iomux_emac_rgmii_pins {
        pinctrl-k510,pins = <0x23 0x23012d 0x24 0x24012e 0x1d 0x1d0123 0x26 0x260131 0x2e 0x2e013a 0x2d 0x2d0139 0x2c 0x2c0138 0x2b 0x2b0137 0x1e 0x1e0128 0x25 0x25012f 0x2a 0x2a0136 0x29 0x290135 0x28 0x280134 0x27 0x270133>;
        phandle = <0x1c>;
    };

    iomux_i2s_pins {
        pinctrl-k510,pins = <0x64 0xab 0x65 0xad 0x63 0xa3 0x62 0x93>;
        phandle = <0x22>;
    };

    iomux_i2c1_pins {
        pinctrl-k510,pins = <0x78 0x44 0x79 0x45>;
        phandle = <0x4a>;
    };

    iomux_i2c2_pins {
        pinctrl-k510,pins = <0x67 0x46 0x66 0x47>;
        phandle = <0x4d>;
    };

    iomux_i2c3_pins {
        pinctrl-k510,pins = <0x74 0x49 0x75 0x48>;
        phandle = <0x4f>;
    };

    iomux_i2c4_pins {
        pinctrl-k510,pins = <0x30 0x4b 0x2f 0x4a>;
        phandle = <0x52>;
    };

    iomux_dvp_pins {
        pinctrl-k510,pins = <0x33 0x33013f 0x34 0x340140 0x35 0x350141 0x36 0x360142 0x37 0x370143 0x38 0x380144 0x39 0x390145 0x3a 0x3a0146 0x3b 0x3b0147 0x3c 0x3c0148 0x3d 0x3d0149 0x3e 0x3e014a 0x3f 0x3f014b 0x40 0x40014c 0x42 0x42014e>;
        phandle = <0x6c>;
    };

    iomux_gpio_pins {
        pinctrl-k510,pins = <0x20 0x20 0x22 0x1f 0x45 0xc 0x46 0xd 0x47 0xe 0x4b 0xf 0x4c 0x10 0x4d 0x11 0x4e 0x1d 0x4f 0x1e 0x50 0x14 0x51 0x15 0x53 0x16 0x54 0x17 0x55 0x18 0x61 0x19 0x7b 0x1a>;
        phandle = <0x47>;
    };

    iomux_pwm0_pins {
        pinctrl-k510,pins = <0x7e 0xb3>;
        phandle = <0x56>;
    };

    iomux_pwm1_pins {
        pinctrl-k510,pins = <0x7f 0xb7>;
        phandle = <0x57>;
    };

    iomux_spi0_pins {
        pinctrl-k510,pins = <0x56 0x560162 0x57 0x570163 0x58 0x580164 0x59 0x590165 0x5a 0x5a0166 0x5b 0x5b0167>;
        phandle = <0xc>;
    };

    iomux_spi1_pins {
        pinctrl-k510,pins = <0x68 0x8 0x69 0x9 0x6a 0x0 0x6b 0x1>;
        phandle = <0xf>;
    };

    iomux_spi2_pins {
        pinctrl-k510,pins = <0x7a 0x2a>;
        phandle = <0x12>;
    };

    iomux_mmc1_pins {
        pinctrl-k510,pins = <0x11 0x110111 0x12 0x120112 0x13 0x130113 0x14 0x140114 0x15 0x150115 0x16 0x160116>;
        phandle = <0x17>;
    };
};
```

`iomux_provider.dtsi` 定義了provider的dts節點
`include/include/dt-bindings/pinctrl/k510.h`中定義了全部IO function number
`iomux_consumer.dtsi`中在驅動各自dts節點中引用

## 4.13 H264

設定選項：

```shell
CONFIG_ ALLEGRO_CODEC_DRIVER
```

驅動檔案：

```shell
drivers/media/platform/canaan/al5r
```

相關設備樹：

```text
h264@92740000 {
    status = "okay";
    compatible = "al,al5r";
    reg = <0x0 0x92740000 0x0 0x10000>;
    interrupt-parent = <0x6>;
    interrupts = <0x3f 0x4>;
    clocks = <0x7f>;
    resets = <0x4 0x184 0x1 0x1f 0x0>;
    reset-names = "h264_rst";
    power-domains = <0x5 0xb>;
};
```

API： 裝置檔案節點： `/dev/h264-codec`

程式設計介面： linux檔IO（open， close ， ioctl），詳見Linux man page

支援的IOCTL命令：

```c
#define AL_CMD_IP_WRITE_REG    _IOWR('q', 10, struct al5_reg)
#define AL_CMD_IP_READ_REG     _IOWR('q', 11, struct al5_reg)
#define AL_CMD_IP_WAIT_IRQ     _IOWR('q', 12, int)
#define AL_CMD_IP_IRQ_CNT      _IOWR('q', 13, int)
#define AL_CMD_IP_CLR_IRQ      _IOWR('q', 14, int)
```

範例代碼：`package/h264_demo/src`

## 4.14 數字信號處理器

設定選項：

```shell
CONFIG_ K510_DSP_DRIVER
```

驅動檔案：

```shell
drivers/misc/canaan/k510-dsp
```

相關設備樹：

```text
dsp@99800000 {
    status = "okay";
    compatible = "k510-dsp";
    reg = <0x0 0x99800000 0x0 0x80000>;
    resets = <0x4 0x14 0x0 0x1e 0x0>;
    reset-names = "dsp_rst";
    power-domains = <0x5 0x1>;
    sysctl-phy-addr = <0x97000000>;
};
```

API： 裝置檔案節點： `/dev/k510-dsp`

程式設計介面： linux檔IO（open， close ， ioctl），詳見Linux man page

支援的ioctl命令：

```c
#define DSP_CMD_BOOT       _IOWR('q', 1, unsigned long)
```

範例代碼：

```shell
package/dsp_app/src/
package/dsp_app_evb_lp3_v1_1/src/
```

## 4.15 千兆噸

設定選項：

```shell
CONFIG_ K510_GNNE_DRIVER
```

驅動檔案：

```shell
drivers/misc/canaan/gnne
```

相關設備樹：

```text
gnne@94000000 {
    status = "okay";
    compatible = "k510-gnne";
    reg = <0x0 0x94180000 0x0 0x80000>;
    interrupt-parent = <0x6>;
    interrupts = <0x27 0x4>;
    resets = <0x4 0x2c 0x1 0x1f 0x0>;
    reset-names = "gnne_rst";
    power-domains = <0x5 0x3>;
};
```

API： 裝置文件節點：/dev/k510-gnne
程式設計介面： linux檔IO（open， close ， ioctl），詳見Linux man page
支援的ioctl命令：

```c
#define GNNE_ENABLE                   _IOWR('g', 1, unsigned long)
#define GNNE_RESET                    _IOWR('g', 2, unsigned long)
#define GNNE_DISABLE                  _IOWR('g', 3, unsigned long)
#define GNNE_SET_PC                   _IOWR('g', 4, unsigned long)
#define GNNE_SET_MEM_BASE             _IOWR('g', 5, unsigned long)
#define GNNE_GET_STATUS               _IOWR('g', 10, unsigned long)
#define GNNE_SET_PC_ENABLE            _IOWR('g', 11, unsigned long)
#define GNNE_SET_MEM0                 _IOWR('g', 12, unsigned long)
#define GNNE_SET_MEM1                 _IOWR('g', 13, unsigned long)
#define GNNE_SET_MEM2                 _IOWR('g', 14, unsigned long)
#define GNNE_SET_MEM3                 _IOWR('g', 15, unsigned long)
#define GNNE_GET_PC                   _IOWR('g', 16, unsigned long)
#define GNNE_GET_CTRL                 _IOWR('g', 17, unsigned long)
#define GNNE_GET_DSP_INTR_MASK        _IOWR('g', 18, unsigned long)
#define GNNE_GET_MEM0                 _IOWR('g', 19, unsigned long)
#define GNNE_GET_MEM1                 _IOWR('g', 20, unsigned long)
#define GNNE_GET_MEM2                 _IOWR('g', 21, unsigned long)
#define GNNE_GET_MEM3                 _IOWR('g', 22, unsigned long)
#define GNNE_GET_LOAD_STROE_PC_ADDR   _IOWR('g', 23, unsigned long)
#define GNNE_GET_TCU_MFU_PC_ADDR      _IOWR('g', 24, unsigned long)
#define GNNE_GET_CCR_STATUS0          _IOWR('g', 25, unsigned long)
#define GNNE_GET_CCR_STATUS1          _IOWR('g', 26, unsigned long)
#define GNNE_GET_CCR_STATUS2          _IOWR('g', 27, unsigned long)
#define GNNE_GET_CCR_STATUS3          _IOWR('g', 28, unsigned long)
```

範例代碼：

```shell
package/nncase_demo/src/mobilenetv2
```

## 4.16 二維

設定選項：

```shell
CONFIG_K510_2D_DRIVER
```

驅動檔案：

```shell
drivers/media/platform/canaan/kendryte_2d.c
```

相關設備樹：

```text
twod@92720000 {
    status = "okay";
    compatible = "k510, kendrty_2d";
    reg = <0x0 0x92720000 0x0 0x10000>;
    interrupt-parent = <0x6>;
    interrupts = <0x44 0x0>;
    clocks = <0x6f 0x70>;
    clock-names = "twod_apb", "twod_axi";
};
```

API： 裝置文件節點：/dev/kendryte_2d
程式設計介面： linux檔IO（open， close ， ioctl），詳見Linux man page
支援的ioctl命令：

```c
#define KENDRTY_2DROTATION_90     _IOWR('k', 0, unsigned long)
#define KENDRTY_2DROTATION_270    _IOWR('k', 1, unsigned long)

#define KENDRTY_2DROTATION_INPUT_ADDR     _IOWR('k', 2, unsigned long)
#define KENDRTY_2DROTATION_OUTPUT_ADDR    _IOWR('k', 3, unsigned long)
#define KENDRTY_2DROTATION_GET_REG_VAL    _IOWR('k', 4, unsigned long)
```

## 4.17 AES和SHA

設定選項：

```shell
CONFIG_CRYPTO_DEV_KENDRYTE_CRYP
```

驅動檔案：

```shell
drivers/crypto/kendryte/kendryte-aes.c
drivers/crypto/kendryte/kendryte-aes.h
drivers/crypto/kendryte/kendryte-hash.c
drivers/crypto/kendryte/kendryte-hash.h
```

相關設備樹：

```text
aes@91000000 {
    status = "okay";
    compatible = "canaan,k510-aes";
    reg = <0x0 0x91000000 0x0 0x10000>;
    clocks = <0x7>;
    resets = <0x4 0x9c 0x1 0x1f 0x0>;
    reset-names = "aes_rst";
    power-domains = <0x5 0x4>;
    dmas = <0x8 0x1 0xfff 0x0 0x21 0x8 0x1 0xfff 0x0 0x22>;
    dma-names = "tx", "rx";
};

sha@91010000 {
    status = "okay";
    compatible = "canaan,k510-sha";
    reg = <0x0 0x91010000 0x0 0x10000>;
    clocks = <0x9>;
    resets = <0x4 0x94 0x1 0x1f 0x0>;
    reset-names = "sha_rst";
    power-domains = <0x5 0x4>;
    dmas = <0x8 0x1 0xfff 0x0 0x20>;
    dma-names = "tx";
};
```

API： 裝置節點檔：`/sys/bus/platform/devices/91000000.aes`
`/sys/bus/platform/devices/91010000.sha`

程式使用socket訪問內核的驅動API，參考文檔位於`/Documentation/crypto/userspace-if.rst`

範例代碼：

```shell
package/crypto_demo/src
```

## 4.18 溫度監測——thermal

設定選項：

```shell
CONFIG_THERMAL
CONFIG_CANAAN_THERMAL
```

驅動檔案：

```shell
drivers/thermal/canaan_thermal.c
```

相關設備樹：

```text
tsensor@970e0300 {
    status = "okay";
    compatible = "canaan,k510-tsensor";
    reg = <0x0 0x970e0300 0x0 0x100>;
    interrupt-parent = <0x6>;
    interrupts = <0x1c 0x4>;
    clocks = <0x54>;
};
```

使用方法：

```shell
cd /sys/class/thermal/thermal_zone0/
echo enabled > mode
cat temp
```

## 4.19 2D 旋轉——twod

設定選項：

```shell
CONFIG_KENDRYTE_TWOD_SUPPORT
CONFIG_KENDRYTE_TWOD
```

驅動檔案：

```shell
drivers/video/canaan/twod/kendryte_td.c
drivers/video/canaan/twod/kendryte_td_reg.c
drivers/video/canaan/twod/kendryte_td.h
drivers/video/canaan/twod/kendryte_td_table.h
```

相關設備樹：

```text
twod@92720000 {
    status = "okay";
    compatible = "k510, kendrty_2d";
    reg = <0x0 0x92720000 0x0 0x10000>;
    interrupt-parent = <0x6>;
    interrupts = <0x44 0x0>;
    clocks = <0x6f 0x70>;
    clock-names = "twod_apb", "twod_axi";
};
```

# 5 注意事項

無

**翻譯免責聲明**  
為方便客戶，Canaan 使用 AI 翻譯程式將文字翻譯為多種語言，它可能包含錯誤。 我們不保證提供的譯文的準確性、可靠性或時效性。 對於因依賴已翻譯信息的準確性或可靠性而造成的任何損失或損害，Canaan 概不負責。 如果不同語言翻譯之間存在內容差異，以簡體中文版本為準。 

如果您要報告翻譯錯誤或不準確的問題，歡迎通過郵件與我們聯繫。