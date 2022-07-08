![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 U-boot Guida per gli sviluppatori</font>**

<font face="黑体"  size=3>Versione del documento: V1.0.0</font>

<font face="黑体"  size=3>Data di pubblicazione: 2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Disconoscimento**</font>
I prodotti, i servizi o le funzionalità acquistati saranno soggetti ai contratti e ai termini commerciali di Beijing Canaan Jiesi Information Technology Co., Ltd. ("la Società", la stessa di seguito), e tutti o parte dei prodotti, servizi o funzionalità descritti in questo documento potrebbero non rientrare nell'ambito dell'acquisto o dell'utilizzo. Salvo quanto diversamente concordato nel contratto, la Società declina ogni dichiarazione o garanzia, espressa o implicita, in merito all'accuratezza, affidabilità, completezza, marketing, scopo specifico e non aggressione di qualsiasi dichiarazione, informazione o contenuto di questo documento. Salvo diverso accordo, questo documento è fornito solo come guida per l'uso.
A causa di aggiornamenti della versione del prodotto o altri motivi, il contenuto di questo documento può essere aggiornato o modificato di volta in volta senza alcun preavviso. 

**<font face="黑体"  size=3>Avvisi sui marchi</font>**

""<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, l'icona "Canaan", Canaan e altri marchi di Canaan e altri marchi di Canaan sono marchi di Beijing Canaan Jiesi Information Technology Co., Ltd. Tutti gli altri marchi o marchi registrati che possono essere menzionati in questo documento sono di proprietà dei rispettivi proprietari. 

**<font face="黑体"  size=3>Copyright ©2022 Pechino Canaan Jiesi Information Technology Co., Ltd</font>**
Questo documento è applicabile solo allo sviluppo e alla progettazione della piattaforma K510, senza il permesso scritto della società, nessuna unità o individuo può diffondere parte o tutto il contenuto di questo documento in qualsiasi forma. 

**<font face="黑体"  size=3>Pechino Canaan Jiesi Information Technology Co., Ltd</font>**
URL: canaan-creative.com
Richieste commerciali: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# prefazione
**<font face="黑体"  size=5>Scopo </font>**del documento
Questo documento è un documento di supporto dell'SDK della scheda demo K510, che introduce principalmente contenuti relativi a uboot, come il file di configurazione della scheda demo k510, l'albero dei dispositivi, la posizione del driver e altre informazioni sotto uboot. 

**<font face="黑体"  size=5>Oggetti lettore</font>**

Le principali persone a cui si applica questo documento (questa guida):

- Sviluppatori di software
- Personale di supporto tecnico

**<font face="黑体"  size=5>Cronologia delle revisioni</font>**
 <font face="宋体"  size=2>La cronologia delle revisioni accumula una descrizione di ogni aggiornamento del documento. La versione più recente del documento contiene gli aggiornamenti per tutte le versioni precedenti. </font>

| Il numero di versione   | Modificato da     | Data della revisione | Note di revisione |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 · | Gruppi di software di sistema | 2022-03-09 |          |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenuto</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Introduzione a U-Boot

U-boot fa parte di sdk e la versione u-boot attualmente utilizzata dall'SDK è 2020.01. Uboot è un programma bootloader sviluppato dal gruppo tedesco DENX per una varietà di CPU embedded, UBoot non solo supporta l'avvio di sistemi Linux embedded, attualmente, supporta anche NetBSD, VxWorks, QNX, RTEMS, ARTOS, LynxOS sistema operativo embedded. Oltre a supportare la serie di processori PowerPC, UBoot può anche supportare MIPS, x86, ARM, NIOS, RISICV, ecc., Le funzioni principali sono l'inizializzazione della memoria, l'avvio dei sistemi Linux, più introduzione u-boot, fare riferimento a<https://www.denx.de/wiki/U-Boot>

# 2 Introduzione all'ambiente di sviluppo

- Sistema operativo

| numerazione | Risorse software | illustrare        |
| ---- | -------- | ----------- |
| 1    | Ubuntu ·   | 18.04/20.04 |

- Ambiente software

I requisiti dell'ambiente software sono illustrati nella tabella seguente:

| numerazione | Risorse software | illustrare |
| ---- | -------- | ---- |
| 1    | K510 SDK |      |

# 3 Come ottenerlo

Scarica e compila l'sdk, l'sdk scaricherà il codice uboot durante la compilazione e compilerà il codice uboot. Per ulteriori informazioni su come scaricare e compilare l'SDK, vedere[ K510_SDK_Build_and_Burn_Guide.md](./K510_SDK_Build_and_Burn_Guide.md)

# 4 Directory importanti e descrizioni dei file

Questo capitolo utilizza k510_evb_lp3_v1_1_defconfig compilati come esempio. Il metodo di compilazione sdk corrispondente è make CONF=k510_evb_lp3_v1_1_defconfig e la directory dopo la compilazione è la seguente:

![immagine-20210930135634105](../zh/images/uboot_guides/build_out.png)

k510_evb_lp3_v1_1_defconfig/build/uboot-custom --- la directory di codice e compilazione di uboot;

board/canaan/k510/uboot-sdcard.env--- file di configurazione della variabile di ambiente predefinita uboot

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/configs/k510_evb_lp3_v1_1_defconfig --uboot file di configurazione;

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/arch/riscv/dts/k510_evb_lp3_v1_1.dts---- file dell'albero del dispositivo;

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/include/configs/k510_evb_lp3_v1_1.h--- file di intestazione;

k510_evb_lp3_v1_1_defconfig/images/u-boot_burn.bin ---uboot lampeggia il firmware

buildroot-2020.02.11/boot/uboot ----buildroot nello script di compilazione su uboot, generalmente non ha bisogno di essere modificato;

File di configurazione Configs/k510_evb_lp3_v1_1_defconfig---sdk, BR2_TARGET_UBOOT_BOARD_DEFCONFIG specificare il file di configurazione di uboot;

# 5 uboot avvia il processo

_start (arch / riscv / cpu / start. S, linea 43)

board_init_f(common/board_f.c, linea 1013)

board_init_r(common/board_r.c, linea 845)

run_main_loop(common/board_r.c, linea 637)

# 6 uboot sotto la descrizione del driver

## 6.1 ddr driver

pensione/Canaan/k510_evb_lp3/ddr_init.c

## 6.2 unità eth

driver/net/macb.c

Albero dei dispositivi:

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

## 6.3 Unità porta seriale

driver/serial/ns16550.c

Albero dei dispositivi:

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

## 6.4 iomux

driver/pinctrl/pinctrl-single.c

Albero dei dispositivi:

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

## Unità da 6,5 mmc e scheda SD

driver/mmc/sdhci-cadence.c

Albero dei dispositivi

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

# 7 Variabile di ambiente predefinita Uboot

La variabile di ambiente predefinita per uboot si trova nella directory board/canaan/k510 dell'SDK, predefinita come file di testo:

uboot-emmc.itv

uboot-nfs.itv

uboot-sdcard.itv

Lo script POST dell'SDK chiamerà mkenvimage in fase di compilazione per compilare la definizione della variabile di ambiente di testo in un'immagine binaria che uboot può caricare e posizionare nella partizione di avvio.

Ecco alcuni esempi:

uboot-sdcard.itv

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

Nota: i bootarg dei parametri di avvio del kernel sono impostati dalla variabile di ambiente predefinita uboot e i bootarg in dts verranno sovrascritti. Vedi FAQ - Dove sono arrivati e passati i bootarg al kernel?

# 8 Aggiornamenti del programma Uboot

## 8.1 Metodo mirror di Flashing sdk

L'immagine sdk contiene già un programma uboot, che lampeggia direttamente l'immagine sdk, come ad esempio: k510_evb_lp3_v1_1_defconfig/images/sysimage-sdcard.img file

## 8.2 Linux aggiorna il programma uboot all'interno della scheda sD

Inserire il file u-boot_burn.bin nella directory tftp, configurare l'indirizzo IP della porta di rete del dispositivo e inserire la directory /root/sd/p1; Eseguire il comando tftp -gr u-boot_burn.bin xxx.xxx.xxx.xxx.xx;

## 8.3 Linux aggiorna il programma uboot all'interno di emmc

Inserire il file u-boot_burn.bin nella directory tftp, configurare l'indirizzo IP della porta di rete del dispositivo e scaricare il file sul dispositivo tramite tftp -gr u-boot_burn.bin xxx.xxx.xxx.xxx.xx;

Eseguire il comando dd if=u-boot_burn.bin of=/dev/mmcblk0p1 per scrivere il file sulla scheda mmc.

# 9 Domande frequenti

## 9.1 Come viene configurata la frequenza DDR?

R: Al momento, l'EVB può eseguire solo 800 e il CRB può impostare 800 o 1600. Metodo di impostazione della frequenza ddr della scheda CrB vedere uboot board\Canaan\k510_crb_lp3\ddr_param.h file, 800M corrisponde a #define DDR_800 1, 1600M corrisponde a #define DDR_1600 1.

## 9.2 Dove sono arrivati e passati i bootarg al kernel?

R: Ottenuto dai bootarg della variabile di ambiente uboot, uboot modificherà i parametri bootargs nell'albero del dispositivo di memoria in base al valore della variabile di ambiente bootargs all'avvio del kernel. Il codice pertinente è il seguente:

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

## 9.3 I parametri di avvio sono incoerenti con il file dell'albero del dispositivo compilato?

R: uboot ottiene dinamicamente le variabili di ambiente in base alla modalità di avvio e aggiorna l'albero dei dispositivi in memoria in base alle variabili di ambiente bootargs all'avvio del kernel. Dopo i parametri di avvio modificati, vedere il nodo /sys/firmware/devicetree/base/chosen.

## 9.4 Dove vengono salvate le variabili di ambiente uboot?

Risposta:

| Modalità di avvio | Uboot lettura e salvataggio posizione | File corrispondenti in fase di compilazione |
| :-: | :-: | :-: |
| Stivali EMMC | Emmc il file uboot-emmc.env per la seconda partizione | board\canaan\k510\uboot-emmc.itv |
| Avvio della scheda SD | Il file uboot-sd.env della prima partizione della scheda SD | board\canaan\k510\uboot-sd.env |

## 9.5 Come impostare qos?

R: I registri relativi a QOS sono QOS_CTRL0 QOS_CTRL1 QOS_CTRL2 QOS_CTRL3 QOS_CTRL4. Esempio:
Dopo aver impostato qos, le prestazioni della demo nncase sono migliorate

```c
*(uint32_t *)0x970E00FC = (0x2 << 8) | (0x2 << 12) | (0x2 << 16) | (0x2 << 20) | (0x2 << 24);
*(uint32_t *)0x970E0100 = (0x3 << 4) | 0x3;
*(uint32_t *)0x970E00F4 = (0x5 << 16) | (0x5 << 20);
```

**Traduzione Disclaimer**  
Per la comodità dei clienti, Canaan utilizza un traduttore AI per tradurre il testo in più lingue, che possono contenere errori. Non garantiamo l'accuratezza, l'affidabilità o la tempestività delle traduzioni fornite. Canaan non sarà responsabile per eventuali perdite o danni causati dall'affidamento sull'accuratezza o sull'affidabilità delle informazioni tradotte. Se c'è una differenza di contenuto tra le traduzioni in lingue diverse, prevarrà la versione cinese semplificata. 

Se desideri segnalare un errore di traduzione o un'inesattezza, non esitare a contattarci via mail.