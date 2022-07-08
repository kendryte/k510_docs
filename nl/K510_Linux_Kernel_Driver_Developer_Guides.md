![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 Linux Kernel Driver Developer's Guide</font>**

<font face="黑体"  size=3>Document versie: V1.0.0</font>

<font face="黑体"  size=3>Publicatiedatum: 2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Disclaimer**</font>
De producten, diensten of functies die u koopt, zijn onderworpen aan de commerciële contracten en voorwaarden van Beijing Canaan Jiesi Information Technology Co., Ltd. ("het Bedrijf", hierna hetzelfde), en alle of een deel van de producten, diensten of functies die in dit document worden beschreven, vallen mogelijk niet binnen het bereik van uw aankoop of gebruik. Tenzij anders overeengekomen in het contract, wijst het bedrijf alle verklaringen of garanties af, expliciet of impliciet, met betrekking tot de nauwkeurigheid, betrouwbaarheid, volledigheid, marketing, specifiek doel en niet-agressie van verklaringen, informatie of inhoud van dit document. Tenzij anders overeengekomen, wordt dit document uitsluitend verstrekt als leidraad voor gebruik.
Vanwege upgrades van de productversie of andere redenen kan de inhoud van dit document van tijd tot tijd zonder enige kennisgeving worden bijgewerkt of gewijzigd. 

**<font face="黑体"  size=3>Handelsmerkkennisgevingen</font>**

""<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, "Canaan" icoon, Kanaän en andere handelsmerken van Kanaän en andere handelsmerken van Kanaän zijn handelsmerken van Beijing Canaan Jiesi Information Technology Co., Ltd. Alle andere handelsmerken of geregistreerde handelsmerken die in dit document kunnen worden genoemd, zijn eigendom van hun respectieve eigenaars. 

**<font face="黑体"  size=3>Copyright ©2022 Beijing Canaan Jiesi Information Technology Co, Ltd</font>**
Dit document is alleen van toepassing op de ontwikkeling en het ontwerp van het K510-platform, zonder de schriftelijke toestemming van het bedrijf mag geen enkele eenheid of persoon een deel of de inhoud van dit document in welke vorm dan ook verspreiden. 

**<font face="黑体"  size=3>Beijing Canaan Jiesi Information Technology Co, Ltd</font>**
URL: canaan-creative.com
Zakelijke vragen: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# inleiding
**<font face="黑体"  size=5>Doel van het document</font>**
Dit document is een ondersteunend document voor de K510 SDK, dit document gaat voornamelijk over Linux-gerelateerde stuurprogramma's, configuratie, foutopsporing, enz

**<font face="黑体"  size=5>Reader Objecten</font>**

De belangrijkste personen op wie dit document (deze gids) van toepassing is:

- Softwareontwikkelaars
- Technisch ondersteunend personeel

**<font face="黑体"  size=5>Revisiegeschiedenis</font>**
 <font face="宋体"  size=2>De revisiegeschiedenis bevat een beschrijving van elke documentupdate. De nieuwste versie van het document bevat updates voor alle voorgaande versies. </font>

| Het versienummer   | Gewijzigd door     | Datum van herziening | Opmerkingen bij herziening |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | Systeemsoftwaregroepen | 2022-03-09 | SDK V1.5 vrijgegeven |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Inhoud</font>**

[INHOUDSOPGAVE]

<div style="page-break-after:always"></div>

# 1 Inleiding tot Linux Kernel

De Linux-versie die momenteel door sdk wordt gebruikt, is 4.17.0. Linux, volledige naam GNU/Linux, is een vrij te gebruiken en vrij verspreid UNIX-achtig besturingssysteem met een kernel die voor het eerst werd uitgebracht door Linus Bennadict Torvaz op 5 oktober 1991, het is voornamelijk geïnspireerd door de ideeën van Minix en Unix, en is een multi-user, multi-tasking, multi-threaded en multi-CPU-gebaseerd besturingssysteem gebaseerd op POSIX. Het draait belangrijke Unix-toolsoftware, applicaties en netwerkprotocollen. Het ondersteunt zowel 32-bits als 64-bits hardware. Linux erft Unix's netwerkgerichte ontwerpfilosofie en is een stabiel multi-user netwerkbesturingssysteem. Linux heeft honderden verschillende distributies, zoals community-based debian, archlinux en commercieel ontwikkelde Red Hat Enterprise Linux, SUSE, Oracle Linux, enz.

Ga voor meer informatie over de Linux-kernel naar:<https://docs.kernel.org/>

## 1.1 Hoe het te krijgen

Download en compileer de SDK, de SDK zal de Linux-code downloaden en compileren tijdens het compileren.

Zie K510_SDK_Build_and_Burn_Guide voor meer informatie over het downloaden en compileren[ van de SDK](./K510_SDK_Build_and_Burn_Guide.md). 

## 1.2 Vereisten voor ontwikkelomgevingen

- Besturingssysteem

| Nummering | Softwarebronnen | illustreren        |
| ---- | -------- | ----------- |
| 1    | Ubuntu   | 18.04/20.04 |

- De vereisten voor de softwareomgeving worden weergegeven in de volgende tabel:

| Nummering | Softwarebronnen | illustreren |
| ---- | -------- | ---- |
| 1    | K510 SDK | v1,5 |

# 2 Kernel standaard configuratiebestand en dts

Standaard pad naar kernelconfiguratiebestand:

arch/riscv/configs/k510_defconfig

De kernel ondersteunt twee development boards, K510 CRB en EVB, en de bijbehorende dts bestanden zijn als volgt:

arch/riscv/boot/dts/canaan/k510_crb_lp3_v0_1.dts

arch/riscv/boot/dts/canaan/k510_evb_lp3_v1_1.dts

In de map arch/riscv/boot/dts/canaan/k510_common staat de publieke dts-definitie op soc-niveau.

# 3 Foutopsporing

## 3.1 Debug linux kernel met JTAG

1. Installeer Andesight v3.2.1
2. Ga naar de ice directory onder de andesight installatie directory en voer ICEMAN uit

    ```shell
    #ICEman -Z v5 --smp
    ```

3. Met behulp van gdb debuggen, hier is de /dev/mem kernel code driver/char/mem.c als voorbeeld

    ```shell
    riscv64-linux-gdb --eval-command="target remote 192.168.200.100:1111"
    (gdb) symbol-file vmlinux
    (gdb) hbreak mmap_mem
    ```

4. De applicatie opent /dev/mem, roept mmap aan en voert het breekpunt in

# 4 Beschrijving van stuurprogramma's

## 4.1 UART

Configuratie-opties:

```shell
CONFIG_SERIAL_8250_DW
```

Driver bestanden:

```shell
/tty/serial/8250
```

Apparaatstructuur:

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

API: Apparaatbestandsknooppunt:

```shell
/dev/ttyS0
/dev/ttyS1/2/3    #目前dts中disable
```

Programmeerinterface: standaard seriële poort driver, refereer naar Linux man pagina

```shell
man termios
```

## 4.2 ETH

Configuratie-opties:

```shell
CONFIG_NET_CADENCE
```

Driver bestanden:

```shell
drivers/net/ethernet/cadence
```

Apparaatstructuur:

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

Apparaat:`eth0`
API-beschrijving: Standaard Ethernet-poortstuurprogramma, raadpleeg tcp / ip socket programmering; 

IP-configuratie van Ethernet-poort:

```shell
ifconfig eth0 xxx.xxx.xxx.xxx
```

## 4.3 EMMC

Configuratie-opties:

```shell
CONFIG_MMC_SDHCI_CADENCE
```

Driver bestanden:

```shell
drivers/mmc/host/sdhci-cadence.c
```

Apparaatstructuur:

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

Apparaten en partities:

```shell
[root@k510-test ~ ]$ ls -l /dev/ | grep mmcblk0
brw------- 179,  0 Jan 1 1970 mmcblk0      # emmc
brw------- 179,  8 Jan 1 1970 mmcblk0boot0
brw------- 179, 16 Jan 1 1970 mmcblk0boot1
brw------- 179,  1 Jan 1 1970 mmcblk0p1    # emmc第一个分区(boot)
brw------- 179,  2 Jan 1 1970 mmcblk0p2    # emmc第二个分区(kenrel,env,vfat)
brw------- 179,  3 Jan 1 1970 mmcblk0p3    # emmmc第三个分区(rootfs文件系统，ext2)
```

Driver API: Standaard driver, als een gewoon bestand om te lezen en te schrijven.

## 4.4 SD-KAART

Configuratie-opties:

```shell
CONFIG_MMC_SDHCI_CADENCE
```

Driver bestanden:

```shell
drivers/mmc/host/sdhci-cadence.c
```

Apparaatstructuur:

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

Uitrusting:

```shell
[root@k510-test ~ ]$ ls -l /dev/ | grep mmcblk1
brw------- 179, 24 mmcblk1      # sd卡设备
brw------- 179, 25 mmcblk1p1    # sd卡第一个分区(boot,kenrel,env,vfat)
brw------- 179, 26 mmcblk1p2    # sd卡第二个分区(rootfs文件系统，ext2)
brw------- 179, 27 mmcblk1p3    # sd卡第三个分区(用户分区)
```

Driver API: Standaard driver, als een gewoon bestand om te lezen en te schrijven.

## 4,5 WDT

Configuratie-opties:

```shell
CONFIG_DW_WATCHDOG
```

Driver bestanden:

```shell
drivers/watchdog/dw_wdt.c
```

Apparaatstructuur:

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

API: Apparaatbestandsknooppunt:

```shell
/dev/watchdog
/dev/watchdog0/1/2
```

Programmeerinterface: linux bestand IO (openen, sluiten, ioctl), zie Linux man pagina
Kernel broncode wordt geleverd met documentatie:`Documentation/watchdog/watchdog-api.txt`

## 4,6 PWM

Configuratie-opties:

```shell
CONFIG_PWM_GPIO
CONFIG_PWM_CANAAN
```

Driver bestanden:

```shell
drivers/pwm/pwm-canaan.c
drivers/pwm/pwm-gpio.c
```

Apparaatstructuur:

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

API: pwm driver in gebruikersstatus is toegankelijk via sysfs, `/sys/class/pwm/`

Programmeerinterface: Linux bestand IO (openen, lezen, schrijven), zie Linux man pagina

Kernel broncode wordt geleverd met documentatie:`Documentation/pwm.txt`

## 4,7 I2C

Configuratie-opties:

```shell
CONFIG_I2C_DESIGNWARE_CORE
CONFIG_I2C0_TEST_DRIVER
```

Driver bestanden:

```shell
drivers/misc/canaan/i2c/test-i2c0.c
drivers/i2c/busses/i2c-designware-platdrv.c
```

Apparaatstructuur:

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

API: De I2C-driver is een buschauffeur en wordt geïmplementeerd met behulp van het Linux-kernel I2C-subsysteemframework. User-state is toegankelijk via sysfs, of user-state tool programma's zoals i2c-tools kunnen worden gebruikt.

```shell
/sys/bus/i2c/devices/
```

Programmeerinterface: Linux-bestand IO (openen, lezen, schrijven), zie Linux man pagina
Kernel broncode wordt geleverd met documentatie:`Documentation/i2c/dev-interface`

## 4.8 USB OTG

Configuratie-opties:

```shell
USB_CANAAN_OTG20
```

Rijden:

```shell
drivers/usb/canaan_otg20/core_drv_mod
```

Apparaatstructuur:

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

USB als host, kan worden aangesloten op een U-schijf, als een apparaat, kan worden gebruikt als een U-schijf.

## 4,9 CLK

Configuratie-opties:

```shell
CONFIG_COMMON_CLK_CAN_K510
```

Driver bestanden:

```shell
drivers/reset/canaan/reset-k510.c
```

Apparaatstructuur:

```shell
arch/riscv/boot/dts/canaan/k510_common/clock_provider.dtsi
arch/riscv/boot/dts/canaan/k510_common/clock_consumer.dtsi
```

- `clock_provider.dtsi`Definieer alle klokknooppunten in
- `clock_consumer.dtsi`Verwijzingen in elke driver dts node

## 4.10 VERMOGEN

Configuratie-opties:

```shell
CONFIG_CANAAN_PM_DOMAIN
```

Driver bestanden:

```shell
drivers/soc/canaan/k510_pm_domains.c
```

Apparaatstructuur:

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

- `power_provider.dtsi` De dts node van de provideder is gedefinieerd
- `include/dt-bindings/soc/canaan,k510_pm_domains.h` Alle machtsdomeinen zijn gedefinieerd in
- `power_consumer.dtsi`De <a0> wordt vermeld in de respectievelijke dts-nodes van de drivers

## 4,11 OPNIEUW INSTELLEN

Configuratie-opties:

```shell
CONFIG_COMMON_RESET_K510
```

Driver bestanden:

```shell
drivers/reset/canaan/reset-k510.c
```

Apparaatstructuur:

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

- `reset_provider.dtsi` De dts node van de provideder is gedefinieerd
- `include/ dt-bindings/reset/canaan-k510-reset.h` Alle resetsignalen zijn gedefinieerd in
- `reset_consumer.dtsi`De <a0> wordt vermeld in de respectievelijke dts-nodes van de drivers

## 4,12 PINCTL

Configuratie-opties:

```shell
CONFIG_PINCTRL_K510
```

Driver bestanden:

```shell
drivers/pinctrl/canaan
```

Gerelateerde apparaatstructuur:

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

`iomux_provider.dtsi` De dts node van de provideder is gedefinieerd
`include/include/dt-bindings/pinctrl/k510.h`Alle IO-functienummers zijn gedefinieerd in
`iomux_consumer.dtsi`De <a0> wordt vermeld in de respectievelijke dts-nodes van de drivers

## 4,13 H264

Configuratie-opties:

```shell
CONFIG_ ALLEGRO_CODEC_DRIVER
```

Driver bestanden:

```shell
drivers/media/platform/canaan/al5r
```

Gerelateerde apparaatstructuur:

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

API: Apparaatbestandsknooppunt: `/dev/h264-codec`

Programmeerinterface: Linux bestand IO (openen, sluiten, ioctl), zie Linux man pagina

Ondersteunde IOCTL-opdrachten:

```c
#define AL_CMD_IP_WRITE_REG    _IOWR('q', 10, struct al5_reg)
#define AL_CMD_IP_READ_REG     _IOWR('q', 11, struct al5_reg)
#define AL_CMD_IP_WAIT_IRQ     _IOWR('q', 12, int)
#define AL_CMD_IP_IRQ_CNT      _IOWR('q', 13, int)
#define AL_CMD_IP_CLR_IRQ      _IOWR('q', 14, int)
```

Voorbeeldcode:`package/h264_demo/src`

## 4.14 DSP

Configuratie-opties:

```shell
CONFIG_ K510_DSP_DRIVER
```

Driver bestanden:

```shell
drivers/misc/canaan/k510-dsp
```

Gerelateerde apparaatstructuur:

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

API: Apparaatbestandsknooppunt: `/dev/k510-dsp`

Programmeerinterface: Linux bestand IO (openen, sluiten, ioctl), zie Linux man pagina

Ondersteunde ioctl commando's:

```c
#define DSP_CMD_BOOT       _IOWR('q', 1, unsigned long)
```

Voorbeeldcode:

```shell
package/dsp_app/src/
package/dsp_app_evb_lp3_v1_1/src/
```

## 4,15 GNNE

Configuratie-opties:

```shell
CONFIG_ K510_GNNE_DRIVER
```

Driver bestanden:

```shell
drivers/misc/canaan/gnne
```

Gerelateerde apparaatstructuur:

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

API: Apparaatbestandsknooppunt: /dev/k510-gnne
Programmeerinterface: Linux bestand IO (openen, sluiten, ioctl), zie Linux man pagina
Ondersteunde ioctl commando's:

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

Voorbeeldcode:

```shell
package/nncase_demo/src/mobilenetv2
```

## 4,16 TWOD

Configuratie-opties:

```shell
CONFIG_K510_2D_DRIVER
```

Driver bestanden:

```shell
drivers/media/platform/canaan/kendryte_2d.c
```

Gerelateerde apparaatstructuur:

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

API: Apparaatbestandsknooppunt: /dev/kendryte_2d
Programmeerinterface: Linux bestand IO (openen, sluiten, ioctl), zie Linux man pagina
Ondersteunde ioctl commando's:

```c
#define KENDRTY_2DROTATION_90     _IOWR('k', 0, unsigned long)
#define KENDRTY_2DROTATION_270    _IOWR('k', 1, unsigned long)

#define KENDRTY_2DROTATION_INPUT_ADDR     _IOWR('k', 2, unsigned long)
#define KENDRTY_2DROTATION_OUTPUT_ADDR    _IOWR('k', 3, unsigned long)
#define KENDRTY_2DROTATION_GET_REG_VAL    _IOWR('k', 4, unsigned long)
```

## 4.17 AES en SHA

Configuratie-opties:

```shell
CONFIG_CRYPTO_DEV_KENDRYTE_CRYP
```

Driver bestanden:

```shell
drivers/crypto/kendryte/kendryte-aes.c
drivers/crypto/kendryte/kendryte-aes.h
drivers/crypto/kendryte/kendryte-hash.c
drivers/crypto/kendryte/kendryte-hash.h
```

Gerelateerde apparaatstructuur:

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

API: Apparaatknooppuntbestanden:`/sys/bus/platform/devices/91000000.aes`
`/sys/bus/platform/devices/91010000.sha`

Programmeerinterface: Gebruikersstatusprogramma's gebruiken sockets om toegang te krijgen tot de stuurprogramma-API van de kernel, waar de referentiedocumentatie zich bevindt`/Documentation/crypto/userspace-if.rst`

Voorbeeldcode:

```shell
package/crypto_demo/src
```

## 4.18 Temperatuurbewaking - thermisch

Configuratie-opties:

```shell
CONFIG_THERMAL
CONFIG_CANAAN_THERMAL
```

Driver bestanden:

```shell
drivers/thermal/canaan_thermal.c
```

Gerelateerde apparaatstructuur:

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

Hoe te gebruiken:

```shell
cd /sys/class/thermal/thermal_zone0/
echo enabled > mode
cat temp
```

## 4.19 2D Rotatie - twod

Configuratie-opties:

```shell
CONFIG_KENDRYTE_TWOD_SUPPORT
CONFIG_KENDRYTE_TWOD
```

Driver bestanden:

```shell
drivers/video/canaan/twod/kendryte_td.c
drivers/video/canaan/twod/kendryte_td_reg.c
drivers/video/canaan/twod/kendryte_td.h
drivers/video/canaan/twod/kendryte_td_table.h
```

Gerelateerde apparaatstructuur:

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

# 5 Voorzorgsmaatregelen

niet

**Vertaling Disclaimer**  
Voor het gemak van klanten gebruikt Canaan een AI-vertaler om tekst in meerdere talen te vertalen, wat fouten kan bevatten. Wij garanderen niet de nauwkeurigheid, betrouwbaarheid of tijdigheid van de geleverde vertalingen. Canaan is niet aansprakelijk voor enig verlies of schade veroorzaakt door het vertrouwen op de nauwkeurigheid of betrouwbaarheid van de vertaalde informatie. Als er een inhoudelijk verschil is tussen de vertalingen in verschillende talen, prevaleert de vereenvoudigd Chinese versie. 

Als u een vertaalfout of onnauwkeurigheid wilt melden, neem dan gerust contact met ons op via e-mail.