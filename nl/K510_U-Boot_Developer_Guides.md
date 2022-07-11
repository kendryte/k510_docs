![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 U-boot Ontwikkelaarshandleiding</font>**

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
Dit document is een K510 demo board sdk ondersteunend document, voornamelijk introductie van uboot gerelateerde inhoud, zoals k510 demo board configuratiebestand, apparaat boom, driver locatie en andere informatie onder uboot.

**<font face="黑体"  size=5>Reader Objecten</font>**

De belangrijkste personen op wie dit document (deze gids) van toepassing is:

- Softwareontwikkelaars
- Technisch ondersteunend personeel

**<font face="黑体"  size=5>Revisiegeschiedenis</font>**
 <font face="宋体"  size=2>De revisiegeschiedenis bevat een beschrijving van elke documentupdate. De nieuwste versie van het document bevat updates voor alle voorgaande versies. </font>

| Het versienummer   | Gewijzigd door     | Datum van herziening | Opmerkingen bij herziening |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | Systeemsoftwaregroepen | 2022-03-09 |          |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Inhoud</font>**

[INHOUDSOPGAVE]

<div style="page-break-after:always"></div>

# 1 Inleiding tot U-Boot

U-boot maakt deel uit van de SDK en de u-boot-versie die momenteel door de SDK wordt gebruikt, is 2020.01. Uboot is een bootloader-programma ontwikkeld door de Duitse DENX-groep voor een verscheidenheid aan ingebedde CPU's, UBoot ondersteunt niet alleen het opstarten van ingebedde Linux-systemen, momenteel ondersteunt het ook NetBSD, VxWorks, QNX, RTEMS, ARTOS, LynxOS embedded besturingssysteem. Naast het ondersteunen van de PowerPC-serie processors, kan UBoot ook MIPS, x86, ARM, NIOS, RISICV, enz. Ondersteunen, de belangrijkste functies zijn het initialiseren van geheugen, het opstarten van Linux-systemen, meer u-boot introductie, raadpleeg<https://www.denx.de/wiki/U-Boot>

# 2 Inleiding tot de ontwikkelomgeving

- Besturingssysteem

| Nummering | Softwarebronnen | illustreren        |
| ---- | -------- | ----------- |
| 1    | Ubuntu   | 18.04/20.04 |

- Software omgeving

De vereisten voor de softwareomgeving worden weergegeven in de volgende tabel:

| Nummering | Softwarebronnen | illustreren |
| ---- | -------- | ---- |
| 1    | K510 SDK |      |

# 3 Hoe het te krijgen

Download en compileer de sdk, de sdk downloadt de uboot-code bij het compileren en compileert de uboot-code. Zie K510_SDK_Build_and_Burn_Guide.md voor meer informatie over het downloaden en compileren van de SDK[.](./K510_SDK_Build_and_Burn_Guide.md)

# 4 Belangrijke mappen en bestandsbeschrijvingen

In dit hoofdstuk worden gecompileerde k510_evb_lp3_v1_1_defconfig als voorbeeld gebruikt. De bijbehorende sdk-compilatiemethode is make CONF=k510_evb_lp3_v1_1_defconfig en de map na compilatie is als volgt:

![afbeelding-20210930135634105](../zh/images/uboot_guides/build_out.png)

k510_evb_lp3_v1_1_defconfig/build/uboot-custom --- code- en compilatiemap van uboot;

board/canaan/k510/uboot-sdcard.env--- uboot standaard omgevingsvariabele configuratiebestand

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/configs/k510_evb_lp3_v1_1_defconfig --uboot configuratiebestand;

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/arch/riscv/dts/k510_evb_lp3_v1_1.dts---- apparaatstructuurbestand;

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/include/configs/k510_evb_lp3_v1_1.h--- headerbestand;

k510_evb_lp3_v1_1_defconfig/images/u-boot_burn.bin ---uboot flitst de firmware

buildroot-2020.02.11/boot/uboot ----buildroot in het compilatiescript over uboot, hoeft over het algemeen niet te worden gewijzigd;

Configs/k510_evb_lp3_v1_1_defconfig---sdk configuratiebestand, BR2_TARGET_UBOOT_BOARD_DEFCONFIG het configuratiebestand van uboot op te geven;

# 5 uboot start het proces

_start (arch / riscv / cpu / start. S, lijn 43)

board_init_f(gemeenschappelijk/board_f.c. lijn 1013)

board_init_r(gemeenschappelijk/board_r.c, lijn 845)

run_main_loop(gemeenschappelijk/board_r.c. lijn 637)

# 6 uboot onder driver beschrijving

## 6.1 DDR-stuurprogramma

bestuur/Kanaän/k510_evb_lp3/ddr_init.c

## 6.2 eth aandrijving

drivers/net/macb.c

Apparaatstructuur:

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

## 6.3 Seriële poortaandrijving

drivers/serial/ns16550.c

Apparaatstructuur:

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

drivers/pinctrl/pinctrl-single.c

Apparaatstructuur:

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

## 6,5 mmc en SD-kaart drive

drivers/mmc/sdhci-cadence.c

Apparaatstructuur

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

# 7 Uboot standaard omgevingsvariabele

De standaardomgevingsvariabele voor uboot bevindt zich in de map board/canaan/k510 van de SDK, vooraf gedefinieerd als tekstbestand:

uboot-emmc.nlv

uboot-nfs.nld

uboot-sdcard.nld

Het POST-script van de SDK roept mkenvimage aan tijdens het compileren om de definitie van de tekstomgevingsvariabele te compileren in een binaire afbeelding die uboot kan laden en in de opstartpartitie kan plaatsen.

Hier zijn enkele voorbeelden:

uboot-sdcard.nld

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

Opmerking: De opstartparameter van de kernel wordt ingesteld door de standaardomgevingsvariabele van uboot en de bootargs in dts worden overschreven. Zie FAQ - Waar zijn bootargs naar de kernel gekomen en doorgegeven?

# 8 Uboot programma-updates

## 8.1 Flashing sdk mirror methode

De sdk-installatiekopie bevat al een uboot-programma, waarmee de sdk-image rechtstreeks wordt geflitst, zoals: k510_evb_lp3_v1_1_defconfig/images/sysimage-sdcard.img file

## 8.2 Linux update het uboot programma in de sD-kaart

Plaats het u-boot_burn.bin-bestand in de tftp-map, configureer het ip-adres van de netwerkpoort van het apparaat en voer de map /root/sd/p1 in; Voer de opdracht tftp -gr u-boot_burn.bin xxx.xxx.xxx.xxx.xx uit;

## 8.3 Linux werkt het uboot-programma in emmc bij

Plaats het u-boot_burn.bin-bestand in de tftp-map, configureer het IP-adres van de netwerkpoort van het apparaat en download het bestand naar het apparaat via tftp -gr u-boot_burn.bin xxx.xxx.xxx.xxx.xx;

Voer de opdracht dd if=u-boot_burn.bin of=/dev/mmcblk0p1 uit om het bestand naar de mmc-kaart te schrijven.

# 9 Veelgestelde vragen

## 9.1 Hoe wordt de DDR-frequentie geconfigureerd?

A: Op dit moment kan de EVB alleen 800 draaien en de CRB kan 800 of 1600 instellen. CrB board ddr frequentie instelling methode zie uboot board\Canaan\k510_crb_lp3\ddr_param.h bestand, 800M komt overeen met #define DDR_800 1, 1600M komt overeen met #define DDR_1600 1.

## 9.2 Waar zijn bootargs vandaan gekomen en naar de kernel gegaan?

A: Verkregen uit de uboot omgevingsvariabele bootargs, zal uboot de bootargs parameters in de geheugen apparaat boom wijzigen volgens de bootargs omgeving variabele waarde bij het opstarten van de kernel. De relevante code is als volgt:

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

## 9.3 Zijn de opstartparameters inconsistent met het gecompileerde apparaatstructuurbestand?

A: uboot verkrijgt dynamisch de omgevingsvariabelen volgens de opstartmodus en werkt de apparaatstructuur in het geheugen bij volgens de bootargs-omgevingsvariabelen bij het opstarten van de kernel. Zie na de gewijzigde opstartparameters het knooppunt /sys/firmware/devicetree/base/chosen.

## 9.4 Waar worden uboot-omgevingsvariabelen opgeslagen?

Antwoorden:

| Opstartmodus | uboot lees en bewaar locatie | Compileertijd overeenkomstige bestanden |
| :-: | :-: | :-: |
| EMMC laarzen | Emmc het uboot-emmc.env bestand voor de tweede partitie | board\canaan\k510\uboot-emmc.env |
| Sd-kaart opstarten | Het uboot-sd.env bestand van de eerste partitie van de sd-kaart | board\canaan\k510\uboot-sd.env |

## 9.5 Hoe qos instellen?

A: QOS-gerelateerde registers zijn QOS_CTRL0 QOS_CTRL1 QOS_CTRL2 QOS_CTRL3 QOS_CTRL4. Voorbeeld:
Na het instellen van qos zijn de prestaties van de nncase-demo verbeterd

```c
*(uint32_t *)0x970E00FC = (0x2 << 8) | (0x2 << 12) | (0x2 << 16) | (0x2 << 20) | (0x2 << 24);
*(uint32_t *)0x970E0100 = (0x3 << 4) | 0x3;
*(uint32_t *)0x970E00F4 = (0x5 << 16) | (0x5 << 20);
```

**Vertaling Disclaimer**  
Voor het gemak van klanten gebruikt Canaan een AI-vertaler om tekst in meerdere talen te vertalen, wat fouten kan bevatten. Wij garanderen niet de nauwkeurigheid, betrouwbaarheid of tijdigheid van de geleverde vertalingen. Canaan is niet aansprakelijk voor enig verlies of schade veroorzaakt door het vertrouwen op de nauwkeurigheid of betrouwbaarheid van de vertaalde informatie. Als er een inhoudelijk verschil is tussen de vertalingen in verschillende talen, prevaleert de vereenvoudigd Chinese versie.

Als u een vertaalfout of onnauwkeurigheid wilt melden, neem dan gerust contact met ons op via e-mail.
