![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 U-Boot Entwicklerhandbuch</font>**

<font face="黑体"  size=3>Dokumentversion: V1.0.0</font>

<font face="黑体"  size=3>Veröffentlicht: 2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Verzichtserklärung**</font>
Die Produkte, Dienstleistungen oder Funktionen, die Sie erwerben, unterliegen den kommerziellen Verträgen und Bedingungen von Beijing Canaan Jiesi Information Technology Co., Ltd. ("das Unternehmen", dasselbe im Folgenden), und alle oder ein Teil der in diesem Dokument beschriebenen Produkte, Dienstleistungen oder Funktionen fallen möglicherweise nicht in den Rahmen Ihres Kaufs oder Ihrer Nutzung. Sofern im Vertrag nicht anders vereinbart, lehnt das Unternehmen alle ausdrücklichen oder stillschweigenden Zusicherungen oder Gewährleistungen hinsichtlich der Genauigkeit, Zuverlässigkeit, Vollständigkeit, des Marketings, des spezifischen Zwecks und der Nichtverletzung von Zusicherungen, Informationen oder Inhalten dieses Dokuments ab. Sofern nicht anders vereinbart, wird dieses Dokument nur als Leitfaden für die Verwendung zur Verfügung gestellt.
Aufgrund von Produktversions-Upgrades oder anderen Gründen kann der Inhalt dieses Dokuments von Zeit zu Zeit ohne vorherige Ankündigung aktualisiert oder geändert werden.

**<font face="黑体"  size=3>Markenhinweise</font>**

"", "Canaan"-Symbol, Canaan und andere Marken von Canaan und andere Marken von Canaan <img src="../zh/images/canaan-logo.png" style="zoom:33%;" />sind Marken von Beijing Canaan Jiesi Information Technology Co., Ltd. Alle anderen Marken oder eingetragenen Warenzeichen, die in diesem Dokument erwähnt werden können, sind Eigentum ihrer jeweiligen Inhaber.

**<font face="黑体"  size=3>Copyright ©2022 Peking Canaan Jiesi Information Technology Co., Ltd</font>**
Dieses Dokument gilt nur für die Entwicklung und das Design der K510-Plattform, ohne die schriftliche Genehmigung des Unternehmens darf keine Einheit oder Einzelperson einen Teil oder den gesamten Inhalt dieses Dokuments in irgendeiner Form verbreiten.

**<font face="黑体"  size=3>Peking Canaan Jiesi Informationstechnologie Co., Ltd</font>**
URL: canaan-creative.com
Geschäftliche Anfragen: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# Vorwort
**<font face="黑体"  size=5>Zweck des Dokuments</font>**
Dieses Dokument ist ein K510 Demo Board SDK unterstützendes Dokument, das hauptsächlich uboot-bezogene Inhalte wie die Konfigurationsdatei des K510-Demoboards, den Gerätebaum, den Treiberstandort und andere Informationen unter uboot vorstellt.

**<font face="黑体"  size=5>Reader-Objekte</font>**

Die wichtigsten Personen, für die sich dieses Dokument (dieser Leitfaden) richtet:

- Softwareentwickler
- Mitarbeiter des technischen Supports

**<font face="黑体"  size=5>Revisionshistorie</font>**
 <font face="宋体"  size=2>In der Revisionshistorie wird eine Beschreibung jeder Dokumentaktualisierung gesammelt. Die neueste Version des Dokuments enthält Updates für alle vorherigen Versionen. </font>

| Die Versionsnummer   | Geändert von     | Datum der Überarbeitung | Revisionshinweise |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | Systemsoftwaregruppen | 2022-03-09 |          |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Inhalt</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Einführung in U-Boot

U-Boot ist Teil des SDK, und die derzeit vom SDK verwendete U-Boot-Version ist 2020.01. Uboot ist ein Bootloader-Programm, das von der deutschen DENX-Gruppe für eine Vielzahl von Embedded-CPUs entwickelt wurde, UBoot unterstützt nicht nur das Booten von Embedded-Linux-Systemen, sondern derzeit auch NetBSD, VxWorks, QNX, RTEMS, ARTOS, LynxOS Embedded-Betriebssystem. Neben der Unterstützung der PowerPC-Prozessorserie kann UBoot auch MIPS, x86, ARM, NIOS, RISICV usw. unterstützen, die Hauptfunktionen sind die Initialisierung des Speichers, das Booten von Linux-Systemen, mehr u-boot-Einführung, siehe<https://www.denx.de/wiki/U-Boot>

# 2 Einführung in die Entwicklungsumgebung

- Betriebssystem

| Nummerierung | Software-Ressourcen | illustrieren        |
| ---- | -------- | ----------- |
| 1    | Ubuntu   | 18.04/20.04 |

- Software-Umgebung

Die Anforderungen an die Softwareumgebung sind in der folgenden Tabelle aufgeführt:

| Nummerierung | Software-Ressourcen | illustrieren |
| ---- | -------- | ---- |
| 1    | K510 SDK |      |

# 3 Wie bekomme ich es?

Laden Sie das SDK herunter und kompilieren Sie es, das SDK lädt den uboot-Code beim Kompilieren herunter und kompiliert den uboot-Code. Weitere Informationen zum Herunterladen und Kompilieren des SDK finden Sie unter[K510_SDK_Build_and_Burn_Guide.md](./K510_SDK_Build_and_Burn_Guide.md)

# 4 Wichtige Verzeichnisse und Dateibeschreibungen

In diesem Kapitel werden kompilierte k510_evb_lp3_v1_1_defconfig als Beispiel verwendet. Die entsprechende SDK-Kompilierungsmethode ist make CONF=k510_evb_lp3_v1_1_defconfig, und das Verzeichnis nach der Kompilierung lautet wie folgt:

![Bild-20210930135634105](../zh/images/uboot_guides/build_out.png)

k510_evb_lp3_v1_1_defconfig/build/uboot-custom --- das Code- und Kompilierungsverzeichnis von uboot;

board/canaan/k510/uboot-sdcard.env--- Konfigurationsdatei der Standardumgebungsvariablen uboot

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/configs/k510_evb_lp3_v1_1_defconfig --uboot-Konfigurationsdatei;

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/arch/riscv/dts/k510_evb_lp3_v1_1.dts---- Gerätestrukturdatei;

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/include/configs/k510_evb_lp3_v1_1.h--- Header-Datei;

k510_evb_lp3_v1_1_defconfig/images/u-boot_burn.bin ---uboot flasht die Firmware

buildroot-2020.02.11/boot/uboot ----buildroot im Kompilierungsskript über uboot, muss im Allgemeinen nicht geändert werden;

Configs/k510_evb_lp3_v1_1_defconfig---sdk-Konfigurationsdatei, BR2_TARGET_UBOOT_BOARD_DEFCONFIG die Konfigurationsdatei von uboot angeben;

# 5 uboot startet den Vorgang

_start(arch/riscv/cpu/start. S, Linie 43)

board_init_f(common/board_f.c, Zeile 1013)

board_init_r(Common/board_r.c, Zeile 845)

run_main_loop(common/board_r.c, Zeile 637)

# 6 uboot unter Treiberbeschreibung

## 6.1 DDR-Treiber

Board/Kanaan/k510_evb_lp3/ddr_init.c

## 6.2 ETH-Antrieb

Treiber/net/macb.c

Gerätestruktur:

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

## 6.3 Serielles Laufwerk

Treiber/seriell/ns16550.c

Gerätestruktur:

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

## 6,4 iomux

Treiber/pinctrl/pinctrl-single.c

Gerätestruktur:

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

## 6,5-mmC- und SD-Kartenlaufwerk

Treiber/mmc/sdhci-cadence.c

Gerätebaum

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

# 7 Uboot-Standard-Umgebungsvariable

Die Standard-Umgebungsvariable für uboot befindet sich im Verzeichnis board/canaan/k510 des SDK, das als Textdatei vordefiniert ist:

uboot-emmc.env

uboot-nfs.env

uboot-sdcard.env

Das POST-Skript des SDK ruft mkenvimage zur Kompilierzeit auf, um die Definition der Textumgebungsvariablen in ein binäres Image zu kompilieren, das uboot laden und in der Boot-Partition platzieren kann.

Hier einige Beispiele:

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

Hinweis: Der Kernel-Boot-Parameter bootargs wird durch die Standard-Umgebungsvariable von uboot gesetzt, und die bootargs in dts werden überschrieben. Siehe FAQ - Wo sind Bootargs hergekommen und an den Kernel weitergegeben worden?

# 8 Uboot-Programm-Updates

## 8.1 Flashing SDK-Spiegelungsmethode

Das SDK-Image enthält bereits ein uboot-Programm, das das SDK-Image direkt blinkt, z. B.: Datei k510_evb_lp3_v1_1_defconfig/images/sysimage-sdcard.img

## 8.2 Linux-Update des uboot-Programms in der sD-Karte

Legen Sie die Datei u-boot_burn.bin im Verzeichnis tftp ab, konfigurieren Sie die IP-Adresse des Netzwerkports des Geräts und geben Sie das Verzeichnis /root/sd/p1 ein. Führen Sie den Befehl tftp -gr u-boot_burn.bin xxx.xxx.xxx.xxx.xx aus.

## 8.3 Linux aktualisiert das uboot-Programm in emmc

Legen Sie die u-boot_burn.bin-Datei im tftp-Verzeichnis ab, konfigurieren Sie die IP-Adresse des Netzwerkports des Geräts und laden Sie die Datei über tftp -gr u-boot_burn.bin xxx.xxx.xxx.xxx.xx auf das Gerät herunter.

Führen Sie den Befehl dd if=u-boot_burn.bin of=/dev/mmcblk0p1 aus, um die Datei auf die mmc-Karte zu schreiben.

# 9 Häufig gestellte Fragen

## 9.1 Wie wird die DDR-Frequenz konfiguriert?

A: Derzeit kann der EVB nur 800 und der CRB 800 oder 1600 einstellen. CrB board ddr frequency setting method see uboot board\Canaan\k510_crb_lp3\ddr_param.h file, 800M entspricht #define DDR_800 1, 1600M entspricht #define DDR_1600 1.

## 9.2 Wo sind Bootargs hergekommen und an den Kernel weitergegeben worden?

A: Aus der uboot-Umgebungsvariablen bootargs bezogen, ändert uboot beim Booten des Kernels die Bootargs-Parameter im Speichergerätebaum entsprechend dem Wert der Umgebungsvariablen bootargs. Der entsprechende Code lautet wie folgt:

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

## 9.3 Sind die Startparameter inkonsistent mit der kompilierten Gerätestrukturdatei?

A: uboot ruft die Umgebungsvariablen dynamisch entsprechend dem Boot-Modus ab und aktualisiert den Gerätebaum im Speicher entsprechend den Bootargs-Umgebungsvariablen beim Booten des Kernels. Nach den geänderten Boot-Parametern siehe /sys/firmware/devicetree/base/chosen node.

## 9.4 Wo werden uboot-Umgebungsvariablen gespeichert?

Antwort:

| Startmodus | uboot Lese- und Speicherort | Entsprechende Dateien zur Kompilierzeit |
| :-: | :-: | :-: |
| EMMC-Stiefel | Emmc die Datei uboot-emmc.env für die zweite Partition | board\canaan\k510\uboot-emmc.env |
| Booten der SD-Karte | Die Datei uboot-sd.env der ersten Partition der SD-Karte | board\canaan\k510\uboot-sd.env |

## 9.5 Wie richte ich qos ein?

A: QOS-bezogene Register sind QOS_CTRL0 QOS_CTRL1 QOS_CTRL2 QOS_CTRL3 QOS_CTRL4. Beispiel:
Nach dem Festlegen von qos hat sich die Leistung der nncase-Demo verbessert

```c
*(uint32_t *)0x970E00FC = (0x2 << 8) | (0x2 << 12) | (0x2 << 16) | (0x2 << 20) | (0x2 << 24);
*(uint32_t *)0x970E0100 = (0x3 << 4) | 0x3;
*(uint32_t *)0x970E00F4 = (0x5 << 16) | (0x5 << 20);
```

**Haftungsausschluss**für Übersetzungen  
Für die Bequemlichkeit der Kunden verwendet Canaan einen KI-Übersetzer, um Text in mehrere Sprachen zu übersetzen, die Fehler enthalten können. Wir übernehmen keine Gewähr für die Genauigkeit, Zuverlässigkeit oder Aktualität der bereitgestellten Übersetzungen. Canaan haftet nicht für Verluste oder Schäden, die durch das Vertrauen auf die Richtigkeit oder Zuverlässigkeit der übersetzten Informationen verursacht werden. Wenn es einen inhaltlichen Unterschied zwischen den Übersetzungen in verschiedenen Sprachen gibt, ist die vereinfachte chinesische Version maßgebend.

Wenn Sie einen Übersetzungsfehler oder eine Ungenauigkeit melden möchten, können Sie uns gerne per E-Mail kontaktieren.
