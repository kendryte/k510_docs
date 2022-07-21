![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 U-boot Guide du développeur</font>**

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
Ce document est un document de support du sdk de la carte de démonstration K510, introduisant principalement du contenu lié à uboot, tel que le fichier de configuration de la carte de démonstration k510, l'arborescence des périphériques, l'emplacement du pilote et d'autres informations sous uboot.

**<font face="黑体"  size=5>Objets de lecture</font>**

Les principales personnes auxquelles ce document (ce guide) s'applique :

- Développeurs de logiciels
- Personnel de soutien technique

**<font face="黑体"  size=5>Historique des révisions</font>**
 <font face="宋体"  size=2>L'historique des révisions accumule une description de chaque mise à jour de document. La dernière version du document contient des mises à jour pour toutes les versions précédentes. </font>

| Le numéro de version   | Modifié par     | Date de révision | Notes de révision |
|  :-----  |-------   |  ------  |  ------  |
| Version 1.0.0 | Groupes de logiciels système | 2022-03-09 |          |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenu</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Introduction à U-Boot

U-boot fait partie du sdk, et la version u-boot actuellement utilisée par le SDK est 2020.01. Uboot est un programme de chargeur de démarrage développé par le groupe allemand DENX pour une variété de processeurs embarqués, UBoot prend non seulement en charge le démarrage des systèmes Linux embarqués, actuellement, il prend également en charge NetBSD, VxWorks, QNX, RTEMS, ARTOS, LynxOS système d'exploitation embarqué. En plus de prendre en charge la série de processeurs PowerPC, UBoot peut également prendre en charge MIPS, x86, ARM, NIOS, RISICV, etc., les principales fonctions sont l'initialisation de la mémoire, le démarrage des systèmes Linux, plus d'introduction u-boot, veuillez vous référer à<https://www.denx.de/wiki/U-Boot>

# 2 Introduction à l'environnement de développement

- Système d’exploitation

| numérotation | Ressources logicielles | illustrer        |
| ---- | -------- | ----------- |
| 1    | Ubuntu   | 18.04/20.04 |

- Environnement logiciel

La configuration requise pour l'environnement logiciel est indiquée dans le tableau suivant :

| numérotation | Ressources logicielles | illustrer |
| ---- | -------- | ---- |
| 1    | Kit de développement logiciel (SDK) K510 |      |

# 3 Comment l'obtenir

Téléchargez et compilez le sdk, le sdk téléchargera le code uboot lors de la compilation et compilera le code uboot. Pour plus d'informations sur le téléchargement et la compilation du Kit de développement logiciel (SDK), consultez[K510_SDK_Build_and_Burn_Guide.md](./K510_SDK_Build_and_Burn_Guide.md)

# 4 Répertoires importants et descriptions de fichiers

Ce chapitre utilise des k510_evb_lp3_v1_1_defconfig compilés comme exemple. La méthode de compilation sdk correspondante est make CONF=k510_evb_lp3_v1_1_defconfig, et le répertoire après la compilation est le suivant :

![image-20210930135634105](../zh/images/uboot_guides/build_out.png)

k510_evb_lp3_v1_1_defconfig/build/uboot-custom --- le répertoire de code et de compilation d'uboot ;

board/canaan/k510/uboot-sdcard.env--- fichier de configuration de variable d'environnement par défaut uboot

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/configs/k510_evb_lp3_v1_1_defconfig fichier de configuration --uboot ;

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/arch/riscv/dts/k510_evb_lp3_v1_1.dts---- fichier d'arborescence de périphériques ;

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/include/configs/k510_evb_lp3_v1_1.h--- fichier d'en-tête ;

k510_evb_lp3_v1_1_defconfig/images/u-boot_burn.bin ---uboot clignote le firmware

buildroot-2020.02.11/boot/uboot ----buildroot dans le script de compilation sur uboot, n'a généralement pas besoin d'être modifié ;

Configs/k510_evb_lp3_v1_1_defconfig---sdk fichier de configuration, BR2_TARGET_UBOOT_BOARD_DEFCONFIG spécifier le fichier de configuration de uboot ;

# 5 uboot démarre le processus

_start (arch / riscv / cpu / start. S, ligne 43)

board_init_f(commun/board_f.c, ligne 1013)

board_init_r(commun/board_r.c,ligne 845)

run_main_loop(commun/board_r.c, ligne 637)

# 6 uboot sous description du pilote

## Pilote ddr 6.1

conseil/Canaan/k510_evb_lp3/ddr_init.c

## 6.2 lecteur eth

drivers/net/macb.c

Arborescence des périphériques :

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

## 6.3 Lecteur de port série

pilotes/série/ns16550.c

Arborescence des périphériques :

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

pilotes/pinctrl/pinctrl-single.c

Arborescence des périphériques :

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

## 6,5 mmc et lecteur de carte SD

pilotes/mmc/sdhci-cadence.c

Arborescence des périphériques

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

# 7 Variable d'environnement Uboot par défaut

La variable d'environnement par défaut pour uboot se trouve dans le répertoire board/canaan/k510 du SDK, prédéfini sous forme de fichier texte :

uboot-emmc.env

uboot-nfs.env

uboot-sdcard.env

Le script POST du SDK appelle mkenvimage au moment de la compilation pour compiler la définition de la variable d'environnement de texte dans une image binaire que uboot peut charger et placer dans la partition de démarrage.

Voici quelques exemples :

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

Remarque : Les bootargs du paramètre de démarrage du noyau sont définis par la variable d'environnement par défaut uboot, et les bootargs dans dts seront écrasés. Voir FAQ - Où les bootargs ont-ils obtenu et passé au noyau ?

# 8 Mises à jour du programme Uboot

## 8.1 Méthode de miroir sdk clignotant

L'image sdk contient déjà un programme uboot, clignotant directement l'image sdk, tel que : k510_evb_lp3_v1_1_defconfig/images/sysimage-sdcard.img file

## 8.2 Linux mettre à jour le programme uboot à l'intérieur de la carte sD

Placez le fichier u-boot_burn.bin dans le répertoire tftp, configurez l'adresse IP du port réseau du périphérique et entrez le répertoire /root/sd/p1 ; Exécutez la commande tftp -gr u-boot_burn.bin xxx.xxx.xxx.xxx.xx ;

## 8.3 Linux met à jour le programme uboot dans emmc

Placez le fichier u-boot_burn.bin dans le répertoire tftp, configurez l'adresse IP du port réseau du périphérique et téléchargez le fichier sur le périphérique via tftp -gr u-boot_burn.bin xxx.xxx.xxx.xxx.xx;

Exécutez la commande dd if=u-boot_burn.bin of=/dev/mmcblk0p1 pour écrire le fichier sur la carte mmc.

# 9 Foire aux questions

## 9.1 Comment la fréquence DDR est-elle configurée ?

R: À l'heure actuelle, l'EVB ne peut en exécuter que 800, et le CRB peut en définir 800 ou 1600. Méthode de réglage de fréquence ddr de la carte CrB voir uboot board\Canaan\k510_crb_lp3\ddr_param.h fichier, 800M correspond à #define DDR_800 1, 1600M correspond à #define DDR_1600 1.

## 9.2 Où les bootargs sont-ils arrivés et passés au noyau ?

R : Obtenu à partir de la variable d'environnement uboot bootargs, uboot modifie les paramètres bootargs dans l'arborescence des périphériques mémoire en fonction de la valeur de la variable d'environnement bootargs lors du démarrage du noyau. Le code pertinent est le suivant :

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

## 9.3 Les paramètres de démarrage sont-ils incompatibles avec le fichier d'arborescence de périphérique compilé ?

R : uboot obtient dynamiquement les variables d'environnement en fonction du mode de démarrage et met à jour l'arborescence des périphériques en mémoire en fonction des variables d'environnement bootargs lors du démarrage du noyau. Après les paramètres de démarrage modifiés, reportez-vous au nœud /sys/firmware/devicetree/base/chosen.

## 9.4 Où les variables d'environnement uboot sont-elles enregistrées ?

Répondre:

| Mode de démarrage | uboot lire et enregistrer l'emplacement | Fichiers correspondants au moment de la compilation |
| :-: | :-: | :-: |
| Bottes EMMC | Emmc le fichier uboot-emmc.env pour la deuxième partition | carte\canaan\k510\uboot-emmc.env |
| Démarrage de la carte SD | Le fichier uboot-sd.env de la première partition de la carte sd | board\canaan\k510\uboot-sd.env |

## 9.5 Comment configurer qos ?

R : Les registres liés au QOS sont QOS_CTRL0 QOS_CTRL1 QOS_CTRL2 QOS_CTRL3 QOS_CTRL4. Exemple:
Après avoir défini qos, les performances de démonstration de nncase se sont améliorées

```c
*(uint32_t *)0x970E00FC = (0x2 << 8) | (0x2 << 12) | (0x2 << 16) | (0x2 << 20) | (0x2 << 24);
*(uint32_t *)0x970E0100 = (0x3 << 4) | 0x3;
*(uint32_t *)0x970E00F4 = (0x5 << 16) | (0x5 << 20);
```

**Clause de non-responsabilité en matière de**  
Pour la commodité des clients, Canaan utilise un traducteur IA pour traduire du texte en plusieurs langues, ce qui peut contenir des erreurs. Nous ne garantissons pas l'exactitude, la fiabilité ou l'actualité des traductions fournies. Canaan ne sera pas responsable de toute perte ou dommage causé par la confiance accordée à l'exactitude ou à la fiabilité des informations traduites. S'il existe une différence de contenu entre les traductions dans différentes langues, la version simplifiée en chinois prévaudra.

Si vous souhaitez signaler une erreur de traduction ou une inexactitude, n'hésitez pas à nous contacter par courrier.
