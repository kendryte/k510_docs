![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 Guide du développeur du pilote du noyau Linux</font>**

<font face="黑体"  size=3>Version du document : V1.0.0</font>

<font face="黑体"  size=3>Date de publication : 2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Démenti**</font>
Les produits, services ou fonctionnalités que vous achetez sont soumis aux contrats commerciaux et aux conditions de Beijing Canaan Jiesi Information Technology Co., Ltd. (« la Société », les mêmes ci-après), et tout ou partie des produits, services ou fonctionnalités décrits dans ce document peuvent ne pas être dans le cadre de votre achat ou de votre utilisation. Sauf accord contraire dans le contrat, la Société décline toute représentation ou garantie, expresse ou implicite, quant à l'exactitude, la fiabilité, l'exhaustivité, le marketing, l'objectif spécifique et la non-agression de toute représentation, information ou contenu de ce document. Sauf convention contraire, le présent document est fourni à titre indicatif à titre indicatif d'utilisation seulement.
En raison de mises à niveau de la version du produit ou d'autres raisons, le contenu de ce document peut être mis à jour ou modifié de temps à autre sans préavis.

**<font face="黑体"  size=3>Avis sur les marques de commerce</font>**

«  »<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, l'icône « Canaan », Canaan et d'autres marques de commerce de Canaan et d'autres marques de commerce de Canaan sont des marques de commerce de Beijing Canaan Jiesi Information Technology Co., Ltd. Toutes les autres marques de commerce ou marques déposées qui peuvent être mentionnées dans ce document sont la propriété de leurs propriétaires respectifs.

**<font face="黑体"  size=3>Copyright ©2022 Beijing Canaan Jiesi Information Technology Co., Ltd</font>**
Ce document ne s'applique qu'au développement et à la conception de la plate-forme K510, sans l'autorisation écrite de la société, aucune unité ou individu ne peut diffuser une partie ou la totalité du contenu de ce document sous quelque forme que ce soit.

**<font face="黑体"  size=3>Beijing Canaan Jiesi Information Technology Co., Ltd</font>**
URL: canaan-creative.com
Demandes de renseignements des entreprises : salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# préface
**<font face="黑体"  size=5>Objet </font>**du document
Ce document est un document de support pour le SDK K510, ce document parle principalement des pilotes liés à Linux, de la configuration, du débogage, etc.

**<font face="黑体"  size=5>Objets de lecture</font>**

Les principales personnes auxquelles ce document (ce guide) s'applique :

- Développeurs de logiciels
- Personnel de soutien technique

**<font face="黑体"  size=5>Historique des révisions</font>**
 <font face="宋体"  size=2>L'historique des révisions accumule une description de chaque mise à jour de document. La dernière version du document contient des mises à jour pour toutes les versions précédentes. </font>

| Le numéro de version   | Modifié par     | Date de révision | Notes de révision |
|  :-----  |-------   |  ------  |  ------  |
| Version 1.0.0 | Groupes de logiciels système | 2022-03-09 | Lancement du SDK V1.5 |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenu</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Introduction au noyau Linux

La version Linux actuellement utilisée par sdk est 4.17.0. Linux, nom complet GNU/Linux, est un système d'exploitation de type UNIX libre d'utilisation et librement diffusé avec un noyau publié pour la première fois par Linus Bennadict Torvaz le 5 octobre 1991, il est principalement inspiré des idées de Minix et Unix, et est un système d'exploitation multi-utilisateur, multi-tâches, multi-thread et multi-CPU basé sur POSIX. Il exécute les principaux logiciels, applications et protocoles réseau de l'outil Unix. Il prend en charge le matériel 32 bits et 64 bits. Linux hérite de la philosophie de conception centrée sur le réseau d'Unix et est un système d'exploitation réseau multi-utilisateurs stable. Linux possède des centaines de distributions différentes, telles que Debian communautaire, archlinux et Red Hat Enterprise Linux, SUSE, Oracle Linux, etc. développés commercialement.

Pour plus d'informations sur le noyau Linux, veuillez visiter :<https://docs.kernel.org/>

## 1.1 Comment l'obtenir

Téléchargez et compilez le SDK, le SDK téléchargera et compilera le code Linux lors de la compilation.

Pour plus d'informations sur le téléchargement et la compilation du Kit de développement logiciel (SDK), voir[K510_SDK_Build_and_Burn_Guide](./K510_SDK_Build_and_Burn_Guide.md).

## 1.2 Exigences relatives à l'environnement de développement

- Système d’exploitation

| numérotation | Ressources logicielles | illustrer        |
| ---- | -------- | ----------- |
| 1    | Ubuntu   | 18.04/20.04 |

- La configuration requise pour l'environnement logiciel est indiquée dans le tableau suivant :

| numérotation | Ressources logicielles | illustrer |
| ---- | -------- | ---- |
| 1    | Kit de développement logiciel (SDK) K510 | v1.5 |

# 2 Fichier de configuration par défaut du noyau et dts

Chemin d'accès au fichier de configuration du noyau par défaut :

arch/riscv/configs/k510_defconfig

Le noyau prend en charge deux cartes de développement, K510 CRB et EVB, et les fichiers dts correspondants sont les suivants :

arch/riscv/boot/dts/canaan/k510_crb_lp3_v0_1.dts

arch/riscv/boot/dts/canaan/k510_evb_lp3_v1_1.dts

Dans le répertoire arch/riscv/boot/dts/canaan/k510_common se trouve la définition de dts publique au niveau soc.

# 3 Débogage

## 3.1 Déboguer le noyau Linux avec JTAG

1. Installer Andesight v3.2.1
2. Accédez au répertoire ice sous le répertoire d'installation andesight et exécutez ICEMAN

    ```shell
    #ICEman -Z v5 --smp
    ```

3. En utilisant le débogage gdb, voici le pilote de code du noyau /dev/mem/char/mem.c à titre d'exemple

    ```shell
    riscv64-linux-gdb --eval-command="target remote 192.168.200.100:1111"
    (gdb) symbol-file vmlinux
    (gdb) hbreak mmap_mem
    ```

4. L'application ouvre /dev/mem, appelle mmap et entre le point d'arrêt

# 4 Description du pilote

## 4.1 UART

Options de configuration :

```shell
CONFIG_SERIAL_8250_DW
```

Fichiers de pilote :

```shell
/tty/serial/8250
```

Arborescence des périphériques :

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

API : Nœud de fichier de périphérique :

```shell
/dev/ttyS0
/dev/ttyS1/2/3    #目前dts中disable
```

Interface de programmation: pilote de port série standard, reportez-vous à la page de manuel Linux

```shell
man termios
```

## 4.2 EPF

Options de configuration :

```shell
CONFIG_NET_CADENCE
```

Fichiers de pilote :

```shell
drivers/net/ethernet/cadence
```

Arborescence des périphériques :

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

Appareil:`eth0`
Description de l'API: Pilote de port Ethernet standard, veuillez vous référer à la programmation de socket tcp / ip;

Configuration IP du port Ethernet :

```shell
ifconfig eth0 xxx.xxx.xxx.xxx
```

## 4.3 EMMC

Options de configuration :

```shell
CONFIG_MMC_SDHCI_CADENCE
```

Fichiers de pilote :

```shell
drivers/mmc/host/sdhci-cadence.c
```

Arborescence des périphériques :

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

Périphériques et partitions :

```shell
[root@k510-test ~ ]$ ls -l /dev/ | grep mmcblk0
brw------- 179,  0 Jan 1 1970 mmcblk0      # emmc
brw------- 179,  8 Jan 1 1970 mmcblk0boot0
brw------- 179, 16 Jan 1 1970 mmcblk0boot1
brw------- 179,  1 Jan 1 1970 mmcblk0p1    # emmc第一个分区(boot)
brw------- 179,  2 Jan 1 1970 mmcblk0p2    # emmc第二个分区(kenrel,env,vfat)
brw------- 179,  3 Jan 1 1970 mmcblk0p3    # emmmc第三个分区(rootfs文件系统，ext2)
```

API du pilote: Pilote standard, comme un fichier ordinaire à lire et à écrire.

## 4.4 CARTE SD

Options de configuration :

```shell
CONFIG_MMC_SDHCI_CADENCE
```

Fichiers de pilote :

```shell
drivers/mmc/host/sdhci-cadence.c
```

Arborescence des périphériques :

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

Équipement:

```shell
[root@k510-test ~ ]$ ls -l /dev/ | grep mmcblk1
brw------- 179, 24 mmcblk1      # sd卡设备
brw------- 179, 25 mmcblk1p1    # sd卡第一个分区(boot,kenrel,env,vfat)
brw------- 179, 26 mmcblk1p2    # sd卡第二个分区(rootfs文件系统，ext2)
brw------- 179, 27 mmcblk1p3    # sd卡第三个分区(用户分区)
```

API du pilote: Pilote standard, comme un fichier ordinaire à lire et à écrire.

## 4.5 WDT

Options de configuration :

```shell
CONFIG_DW_WATCHDOG
```

Fichiers de pilote :

```shell
drivers/watchdog/dw_wdt.c
```

Arborescence des périphériques :

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

API : Nœud de fichier de périphérique :

```shell
/dev/watchdog
/dev/watchdog0/1/2
```

Interface de programmation: fichier linux IO (ouvrir, fermer, ioctl), voir la page de manuel Linux
Le code source du noyau est fourni avec la documentation :`Documentation/watchdog/watchdog-api.txt`

## 4.6 PWM

Options de configuration :

```shell
CONFIG_PWM_GPIO
CONFIG_PWM_CANAAN
```

Fichiers de pilote :

```shell
drivers/pwm/pwm-canaan.c
drivers/pwm/pwm-gpio.c
```

Arborescence des périphériques :

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

API: le pilote pwm à l'état utilisateur est accessible via sysfs, `/sys/class/pwm/`

Interface de programmation : fichier Linux IO (ouvrir, lire, écrire), voir la page de manuel Linux

Le code source du noyau est fourni avec la documentation :`Documentation/pwm.txt`

## 4,7 I2C

Options de configuration :

```shell
CONFIG_I2C_DESIGNWARE_CORE
CONFIG_I2C0_TEST_DRIVER
```

Fichiers de pilote :

```shell
drivers/misc/canaan/i2c/test-i2c0.c
drivers/i2c/busses/i2c-designware-platdrv.c
```

Arborescence des périphériques :

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

API: Le pilote I2C est un pilote de bus et est implémenté à l'aide du framework de sous-système I2C du noyau Linux. L'état utilisateur est accessible via sysfs, ou des programmes d'outils d'état utilisateur tels que i2c-tools peuvent être utilisés.

```shell
/sys/bus/i2c/devices/
```

Interface de programmation : fichier Linux IO (ouvrir, lire, écrire), voir la page de manuel Linux
Le code source du noyau est fourni avec la documentation :`Documentation/i2c/dev-interface`

## 4.8 USB OTG

Options de configuration :

```shell
USB_CANAAN_OTG20
```

Conduire:

```shell
drivers/usb/canaan_otg20/core_drv_mod
```

Arborescence des périphériques :

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

USB en tant qu'hôte, peut être connecté à un disque U, en tant que périphérique, peut être utilisé comme un disque U.

## 4.9 CLK

Options de configuration :

```shell
CONFIG_COMMON_CLK_CAN_K510
```

Fichiers de pilote :

```shell
drivers/reset/canaan/reset-k510.c
```

Arborescence des périphériques :

```shell
arch/riscv/boot/dts/canaan/k510_common/clock_provider.dtsi
arch/riscv/boot/dts/canaan/k510_common/clock_consumer.dtsi
```

- `clock_provider.dtsi`Définir tous les nœuds d'horloge dans
- `clock_consumer.dtsi`Références dans chaque nœud dts de pilote

## 4.10 PUISSANCE

Options de configuration :

```shell
CONFIG_CANAAN_PM_DOMAIN
```

Fichiers de pilote :

```shell
drivers/soc/canaan/k510_pm_domains.c
```

Arborescence des périphériques :

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

- `power_provider.dtsi` Le nœud dts du fournisseur est défini
- `include/dt-bindings/soc/canaan,k510_pm_domains.h` Tous les domaines d'alimentation sont définis dans
- `power_consumer.dtsi`Le <a0> est référencé dans les nœuds dts respectifs des pilotes

## 4.11 RÉINITIALISATION

Options de configuration :

```shell
CONFIG_COMMON_RESET_K510
```

Fichiers de pilote :

```shell
drivers/reset/canaan/reset-k510.c
```

Arborescence des périphériques :

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

- `reset_provider.dtsi` Le nœud dts du fournisseur est défini
- `include/ dt-bindings/reset/canaan-k510-reset.h` Tous les signaux de réinitialisation sont définis dans
- `reset_consumer.dtsi`Le <a0> est référencé dans les nœuds dts respectifs des pilotes

## 4.12 PINCTL

Options de configuration :

```shell
CONFIG_PINCTRL_K510
```

Fichiers de pilote :

```shell
drivers/pinctrl/canaan
```

Arborescence des périphériques associée :

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

`iomux_provider.dtsi` Le nœud dts du fournisseur est défini
`include/include/dt-bindings/pinctrl/k510.h`Tous les numéros de fonction d'E/S sont définis dans
`iomux_consumer.dtsi`Le <a0> est référencé dans les nœuds dts respectifs des pilotes

## 4,13 H264

Options de configuration :

```shell
CONFIG_ ALLEGRO_CODEC_DRIVER
```

Fichiers de pilote :

```shell
drivers/media/platform/canaan/al5r
```

Arborescence des périphériques associée :

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

API : Nœud de fichier de périphérique : `/dev/h264-codec`

Interface de programmation : fichier Linux IO(open, close, ioctl), voir la page de manuel Linux

Commandes IOCTL prises en charge :

```c
#define AL_CMD_IP_WRITE_REG    _IOWR('q', 10, struct al5_reg)
#define AL_CMD_IP_READ_REG     _IOWR('q', 11, struct al5_reg)
#define AL_CMD_IP_WAIT_IRQ     _IOWR('q', 12, int)
#define AL_CMD_IP_IRQ_CNT      _IOWR('q', 13, int)
#define AL_CMD_IP_CLR_IRQ      _IOWR('q', 14, int)
```

Exemple de code :`package/h264_demo/src`

## 4.14 DSP

Options de configuration :

```shell
CONFIG_ K510_DSP_DRIVER
```

Fichiers de pilote :

```shell
drivers/misc/canaan/k510-dsp
```

Arborescence des périphériques associée :

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

API : Nœud de fichier de périphérique : `/dev/k510-dsp`

Interface de programmation : fichier Linux IO(open, close, ioctl), voir la page de manuel Linux

Commandes ioctl prises en charge :

```c
#define DSP_CMD_BOOT       _IOWR('q', 1, unsigned long)
```

Exemple de code :

```shell
package/dsp_app/src/
package/dsp_app_evb_lp3_v1_1/src/
```

## 4.15 RNB

Options de configuration :

```shell
CONFIG_ K510_GNNE_DRIVER
```

Fichiers de pilote :

```shell
drivers/misc/canaan/gnne
```

Arborescence des périphériques associée :

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

API : Nœud de fichier de périphérique : /dev/k510-gnne
Interface de programmation : fichier Linux IO(open, close, ioctl), voir la page de manuel Linux
Commandes ioctl prises en charge :

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

Exemple de code :

```shell
package/nncase_demo/src/mobilenetv2
```

## 4.16 TWOD

Options de configuration :

```shell
CONFIG_K510_2D_DRIVER
```

Fichiers de pilote :

```shell
drivers/media/platform/canaan/kendryte_2d.c
```

Arborescence des périphériques associée :

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

API : Nœud de fichier de périphérique : /dev/kendryte_2d
Interface de programmation : fichier Linux IO(open, close, ioctl), voir la page de manuel Linux
Commandes ioctl prises en charge :

```c
#define KENDRTY_2DROTATION_90     _IOWR('k', 0, unsigned long)
#define KENDRTY_2DROTATION_270    _IOWR('k', 1, unsigned long)

#define KENDRTY_2DROTATION_INPUT_ADDR     _IOWR('k', 2, unsigned long)
#define KENDRTY_2DROTATION_OUTPUT_ADDR    _IOWR('k', 3, unsigned long)
#define KENDRTY_2DROTATION_GET_REG_VAL    _IOWR('k', 4, unsigned long)
```

## 4.17 AES et SHA

Options de configuration :

```shell
CONFIG_CRYPTO_DEV_KENDRYTE_CRYP
```

Fichiers de pilote :

```shell
drivers/crypto/kendryte/kendryte-aes.c
drivers/crypto/kendryte/kendryte-aes.h
drivers/crypto/kendryte/kendryte-hash.c
drivers/crypto/kendryte/kendryte-hash.h
```

Arborescence des périphériques associée :

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

API : Fichiers de nœud de périphérique :`/sys/bus/platform/devices/91000000.aes`
`/sys/bus/platform/devices/91010000.sha`

Interface de programmation : les programmes d'état utilisateur utilisent des sockets pour accéder à l'API du pilote du noyau, où se trouve la documentation de référence`/Documentation/crypto/userspace-if.rst`

Exemple de code :

```shell
package/crypto_demo/src
```

## 4.18 Surveillance de la température - thermique

Options de configuration :

```shell
CONFIG_THERMAL
CONFIG_CANAAN_THERMAL
```

Fichiers de pilote :

```shell
drivers/thermal/canaan_thermal.c
```

Arborescence des périphériques associée :

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

Comment utiliser :

```shell
cd /sys/class/thermal/thermal_zone0/
echo enabled > mode
cat temp
```

## 4.19 Rotation 2D - twod

Options de configuration :

```shell
CONFIG_KENDRYTE_TWOD_SUPPORT
CONFIG_KENDRYTE_TWOD
```

Fichiers de pilote :

```shell
drivers/video/canaan/twod/kendryte_td.c
drivers/video/canaan/twod/kendryte_td_reg.c
drivers/video/canaan/twod/kendryte_td.h
drivers/video/canaan/twod/kendryte_td_table.h
```

Arborescence des périphériques associée :

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

# 5 Précautions

non

**Clause de non-responsabilité en matière de**  
Pour la commodité des clients, Canaan utilise un traducteur IA pour traduire du texte en plusieurs langues, ce qui peut contenir des erreurs. Nous ne garantissons pas l'exactitude, la fiabilité ou l'actualité des traductions fournies. Canaan ne sera pas responsable de toute perte ou dommage causé par la confiance accordée à l'exactitude ou à la fiabilité des informations traduites. S'il existe une différence de contenu entre les traductions dans différentes langues, la version simplifiée en chinois prévaudra.

Si vous souhaitez signaler une erreur de traduction ou une inexactitude, n'hésitez pas à nous contacter par courrier.
