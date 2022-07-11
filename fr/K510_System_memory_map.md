![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 Carte mémoire système</font>**

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
Ce document est un document de description de l'exemple d'application K510 SDK.

**<font face="黑体"  size=5>Objets de lecture</font>**

Les principales personnes auxquelles ce document (ce guide) s'applique :

- Développeurs de logiciels
- Personnel de soutien technique

**<font face="黑体"  size=5>Historique des révisions</font>**
 <font face="宋体"  size=2>L'historique des révisions accumule une description de chaque mise à jour de document. La dernière version du document contient des mises à jour pour toutes les versions précédentes. </font>

| Le numéro de version   | Modifié par     | Date de révision | Notes de révision |
|  :-----  |-------   |  ------  |  ------  |
| Version 1.0.0 | Groupes de logiciels système | 2022-03-09 |   |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenu</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Planification de la mémoire système K510

Le plan de mémoire du K510 est illustré dans la figure suivante :

![](../zh/images/system_memory_map/k510-system-memory-map.png)

Il y a un DDR de 512 Mo sur la carte de référence K510 crb, avec un total de quatre zones prévues:

- Planification 0 ~ 240M pour le noyau Linux
- 240M ~ 496MB est prévu pour partager la mémoire, en utilisant la méthode de réservation du pool de mémoire CMA, de sorte que le sous-système de gestion de la mémoire du noyau Linux peut également allouer de la mémoire à partir du pool CMA en l'absence d'utilisation de la mémoire de partage
- 496M ~ 510M est prévu pour l'utilisation DSP
- 510M ~ 512M est prévu pour l'utilisation du logo

# 2 Description de l'arborescence des périphériques

La planification de la mémoire du K510 est décrite de manière réservée, à travers les nœuds de mémoire réservée de l'arborescence des périphériques. Les informations pertinentes sur le nœud de l'arborescence des périphériques sont les suivantes :

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

# 3 Configuration liée à Buildroot

Le plan de mémoire système est décrit dans dts du noyau Linux, mais l'adresse de chargement du firmware dsp doit être configurée dans buildroot :

configs/k510_crb_lp3_v0_1_defconfig :

configs/k510_crb_lp3_v1_2_defconfig :

BR2_TARGET_EVB_FIRMWARE_LOAD_ADD=0x1f000000

**Clause de non-responsabilité en matière de**  
Pour la commodité des clients, Canaan utilise un traducteur IA pour traduire du texte en plusieurs langues, ce qui peut contenir des erreurs. Nous ne garantissons pas l'exactitude, la fiabilité ou l'actualité des traductions fournies. Canaan ne sera pas responsable de toute perte ou dommage causé par la confiance accordée à l'exactitude ou à la fiabilité des informations traduites. S'il existe une différence de contenu entre les traductions dans différentes langues, la version simplifiée en chinois prévaudra.

Si vous souhaitez signaler une erreur de traduction ou une inexactitude, n'hésitez pas à nous contacter par courrier.
