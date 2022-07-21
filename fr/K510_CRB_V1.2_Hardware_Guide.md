![](../zh/images/canaan-cover.png)
&nbsp;
&nbsp;
**<font face="黑体" size="6" style="float:right">Guides matériels K510 CRB V1.2</font>**

<font face="黑体" size=100>&nbsp;
&nbsp;
&nbsp;</font>

<font face="黑体"  size=3>Version du document : V1.0.0</font>

<font face="黑体"  size=3>Date de publication : 2022-03-15</font>

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
Ce document est un document d'accompagnement du sdk K510 et est destiné à aider les ingénieurs à comprendre la compilation et la gravure du sdk K510.

**<font face="黑体"  size=5>Objets de lecture</font>**

Les principales personnes auxquelles ce document (ce guide) s'applique :

- Développeurs de logiciels
- Personnel de soutien technique

**<font face="黑体"  size=5>Historique des révisions</font>**
 <font face="宋体"  size=2>L'historique des révisions accumule une description de chaque mise à jour de document. La dernière version du document contient des mises à jour pour toutes les versions précédentes. </font>

| Le numéro de version | Modifié par    | Date de révision   | Notes de révision           |
| :----- | --------- | ---------- | ------------------ |
| Version 1.0.0 | Division des produits d'IA | 2022-03-15 | |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenu</font>**

[Toc]

<div style="page-break-after:always"></div>

# 1 Vue d'ensemble

&emsp; &emsp; K510 CRB est une plate-forme de développement matériel pour la puce Canaan Kendryte K510 AI qui intègre la conception de référence, le débogage et les tests de puce, et la vérification du développement de produits utilisateur, qui est utilisée pour démontrer la puissance de calcul puissante et les fonctions de la puce K510. Dans le même temps, il fournit aux clients des conceptions de référence matérielles basées sur des puces K510, de sorte que les clients n'ont pas besoin de modifier ou simplement de modifier le circuit de module de la conception de référence, et peuvent compléter le travail de développement matériel du produit avec les puces K510 comme noyau.

&emsp; &emsp; K510 CRB prend en charge le développement matériel, la conception de logiciels d'application, le débogage et le fonctionnement de la puce K510, car compte tenu des différents environnements d'utilisation, la puce est une vérification entièrement fonctionnelle, de sorte que les différentes interfaces sont complètes et la conception est relativement complète. Le K510 CRB peut être connecté à un PC via un câble USB, utilisé comme système de développement de base, ou à un système de développement et un environnement de démonstration plus complets, en connectant les périphériques et composants suivants :

- alimentation

- Périphérique de stockage TF Card

- Écran LCD MIPI DSI

- Module de caméra MIPI CSI

- Module de caméra DVP

- Câble réseau Ethernet

- Écran HDMI

- Casque ou haut-parleurs

- Développer les pièces de rechange

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-K510_Core.png">
</div>

  <center>Figure 1-1 Rendu CRB K510</center>

    **禁止事项**

  1. Il est interdit de brancher et de débrancher le module de base et les modules périphériques en direct!
  2. Il est interdit de faire fonctionner ce produit directement sans les mesures de décharge d'électricité statique ou sans protection statique.
  3. Il est interdit d'utiliser des solvants organiques ou des liquides corrosifs pour nettoyer ce produit.
  4. Il est interdit d'effectuer des opérations telles que le taraudage et la torsion qui peuvent causer des dommages physiques.

    **Précautions**

  1. Veuillez noter qu'après la décharge électrostatique du corps humain, avant d'utiliser ce produit, il est recommandé de porter un bracelet électrostatique.
  2. Avant le fonctionnement, vérifiez la tension d'alimentation et la tension de l'adaptateur du fond de panier dans la plage autorisée décrite dans ce document.
  3. Assurez-vous de lire ce document et les considérations dans le fichier d'ingénierie avant de concevoir.
  4. Notez que l'utilisation de produits dans un environnement à haute température, humidité élevée et forte corrosion nécessite un traitement spécial tel que la dissipation de la chaleur, le drainage et l'étanchéité.
  5. S'il vous plaît ne pas réparer et démonter vous-même, sinon vous ne pourrez pas profiter d'un service après-vente gratuit.

<div style="page-break-after:always"></div>

## 1.1 Schéma fonctionnel du système

&emsp; &emsp; Le schéma fonctionnel du système est utilisé pour décrire les principes de conception du CRB K510 et la relation entre les composants, afin que l'utilisation du CRB K510 et les développeurs puissent avoir une compréhension intuitive de l'architecture et des principes de l'ensemble du système.

&emsp; &emsp; Pour plus d'informations sur les fonctionnalités du K510, reportez-vous à la fiche technique complète du K510.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_1_2.png">
</div>

<center>Figure 1-2 Composition du CRB K510</center>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_1_3.png">
</div>

<center>Figure 1-3 Schéma fonctionnel du système CRB K510 </center>

<div style="page-break-after:always"></div>

&emsp; &emsp; Le kit de développement K510 CRB se compose principalement des composants suivants :

| Pièces | quantité |
| :-: | :-: |
| Carte mère K510 CRB | 1 |
| USB type C线缆 | 2 |
| Câble Micro USB OTG | 1 |
| Écran MIPI DSI avec une résolution de 1920x1080 | 1 |
| Sous-carte de caméra MIPI CSI, capteur d'image Sony IMX219 intégré deux | 1 |
| Boîtier de protection en acrylique | 1 |

<div style="page-break-after:always"></div>

## 1.2 Aperçu de la fonction

&emsp; &emsp; Le SDK K510 est basé sur buildroot comme framework de base, avec le noyau Linux K510 (linux version 4.17.0), u-boot (u-boot version 2020.01), riscv-pk-k510

&emsp; &emsp; Les principales caractéristiques de K510 CRB V1.2 (s'il n'y a pas de déclarations spéciales, les versions de CRB décrites plus loin dans ce document sont V1.2) sont les suivantes :

- PMIC : Gestion de l'alimentation
- LPDDR3EE 32 bits, capacité totale 512 Mo
- eMMC 8 bits, capacité totale 4 Go
- QSPI NAND, capacité totale 128MByte
- Carte TF: Prend en charge l'extension externe du stockage de la carte TF.
- USB OTG: Mise à niveau du système, prise en charge de la commutation hôte / périphérique
- SDIO WIFI: Prend en charge la fonction Internet sans fil et la connexion Bluetooth
- Audio: Prise en charge de l'entrée et de la sortie vocales
- PDM MIC: Fonction de réveil VAD
- Uart & JTAG Debug : cartes de développement utilisées par Debug
- Entrée vidéo: Double entrée de caméra MIPI CSI 2 voies
- Sortie vidéo: MIPI DSI 4lane, écran 1080P
- RGMII : connexion Gigabit Ethernet
- HDMI : Interface multimédia haute définition
- Interfaces étendues : alimentation, GPIO, I2C, SPI
- Clés, indicateurs

<div style="page-break-after:always"></div>

# 2 Introduction aux ressources matérielles

## 2.1 Rendus globaux

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_1.png" width=80%>
</div>

<center> Figure 2-1 Carte mère avant </center>

<div style="page-break-after:always"></div>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_2.png" width=80%>
</div>

<center> Figure 2-1 À l'arrière de la carte mère </center>

<div style="page-break-after:always"></div>

## 2.2 Schéma de structure et d'interface

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_3.png" width=120%>
</div>

<center> Figure 2-3 Position de chaque périphérique à l'avant de la carte mère </center>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2-4.png" width=120%>
</div>

<center> Figure 2-4 Arrière de la carte mère </center>

<div style="page-break-after:always"></div>

## 2.3 Schéma fonctionnel de l'alimentation

&emsp; &emsp; Le K510 CRB utilise DC-5V comme puissance d'entrée de l'ensemble de la carte, fournissant DC-5V pour le module central K510 CORE, et 1,8V et 3,3V pour les autres périphériques du fond de panier via deux DC-DC.

## 2.4 Adresse de l'appareil I2C

<center>Tableau 2-1 Tableau d'adresses des périphériques I2C</center>

| nom | Broches (SCL, SDA) | adresse | remarque |
| :-: | :-: | :-: | :-: |
| écran tactile | IO_103、IO_102 | 0x14 ou 0x5D | |
| HDMI | IO_117、IO_116 | 0x3B | |
| Audio Codec | IO_117、IO_116 | 0x1A | |
| Caméra MIPI CSI0 | IO_120、IO_121 | 0x10 | |
| Caméra MIPI CSI1 | IO_47、IO_48   | 0x10 | |

## 2.5 Schémas

&emsp; &emsp; Le schéma de référence de la carte de développement K510 CRB doit être[téléchargé dès sa sortie](https://github.com/kendryte/k510_docs/releases).

<div style="page-break-after:always"></div>

# 3 Introduction à chaque section du tableau de développement

## 3.1 Modules de base

&emsp; &emsp; Avant d'utiliser K510 CRB pour l'apprentissage et le développement, il est recommandé de se référer à l'architecture détaillée de la puce dans le manuel K510, afin que vous puissiez avoir une compréhension plus approfondie de l'alimentation, du stockage, des ressources informatiques et des périphériques du K510, ce qui est propice à la familiarité et au développement de la solution de puce. La carte centrale K510 est illustrée à la Figure 3-1.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_1.png">
</div>

<center>Figure 3-1 Module central K510</center>

<div style="page-break-after:always"></div>

## 3.2 Alimentation d'entrée

&emsp; &emsp; K510 CRB utilise une alimentation externe 5V, deux interfaces USB de type C intégrées, peut être utilisé pour alimenter la carte de développement, dont l'interface UART est utilisée pour se connecter à l'ordinateur, l'interface USB de l'ORDINATEUR ne peut fournir que 500mA de courant, en cas d'alimentation insuffisante, veuillez utiliser l'adaptateur en même temps pour alimenter DC: 5V. L'interface est illustrée dans la figure suivante.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_2.png" width=60%>
</div>

<center> Figure 3-2 Connecteur d'entrée d'alimentation </center>

**Remarque: Limitez l'utilisation de l'alimentation 5V, lorsque vous utilisez l'adaptateur de charge rapide, essayez de ne pas connecter d'autres appareils tels que les téléphones mobiles en même temps, afin de ne pas provoquer une sortie incorrecte de l'adaptateur de charge rapide d'une alimentation supérieure à 5V, entraînant des dommages à la partie alimentation de la carte de développement.**
&emsp; &emsp; Utilisez le commutateur à bascule K2 pour la mise sous tension et la mise hors tension, comme illustré dans la figure suivante.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-3.jpg" width=50%>
</div>

<center>Figure 3-3 Description de l'interrupteur d'alimentation</center>

<div style="page-break-after:always"></div>

## 3.3 Périphériques de stockage

&emsp; &emsp; Le K510 CRB comprend une variété de périphériques de stockage à bord, y compris DDR, eMMC, NAND Flash et TF Card.

### 3.3.1 eMMC

&emsp; &emsp; Une mémoire eMMC de 4 G octets à bord du CRB K510, située sur le module principal, peut être utilisée pour stocker des données telles que le code de démarrage et les fichiers utilisateur.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-eMMC.png" width=70%>
</div>

<center>Figure 3-4 Mémoire eMMC</center>

### 3.3.2 NandFlash

&emsp; &emsp; Le CRB K510 comprend 128 Mo d'octets de mémoire flash NAND, qui peuvent être utilisés pour stocker des données telles que le code de démarrage et les fichiers utilisateur.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_5.jpg " width=75%>
</div>

<center>Figure 3-5 Mémoire flash NAND</center>

### 3.3.2 Carte TF

&emsp; &emsp; Le K510 CRB dispose d'un support de carte TF à bord qui peut être connecté en externe à une carte TF pour stocker des données telles que le code de démarrage et les fichiers utilisateur.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_6.png">
</div>

<center>Figure 3-6 Support de carte TF</center>

<div style="page-break-after:always"></div>

## 3.4 Frappes

&emsp; &emsp; Le K510 CRB contient deux boutons tactiles utilisateur qui permettent aux utilisateurs de personnaliser les boutons d'appui pour qu'ils se déclenchent en tant qu'entrées système ou autres fonctions liées au logiciel.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_7.jpg" width=50%>
</div>

<center>Figure 3-7 Touches</center>

## 3.5 LED

&emsp; &emsp; Le K510 CRB dispose d'une diode électroluminescente à bord qui est connectée directement à la broche GPIO de la puce K510.

&emsp; &emsp; Le K510 CRB est embarqué dans une LED colorée WS2812 qui est connectée directement à la broche GPIO de la puce K510.

&emsp; &emsp; Les deux LED sont programmées sur mesure pour allumer ou éteindre et peuvent être utilisées comme sorties système ou indications d'état liées au logiciel.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_8.jpg" width=60%>
</div>

<center>Figure 3-8 Voyant</center>

<div style="page-break-after:always"></div>

## 3.6 Mode de démarrage et réinitialisation

&emsp; &emsp; Le K510 CRB dispose d'une variété de périphériques de stockage à bord, et le mode de démarrage est sélectionné en configurant les niveaux des broches de démarrage, BOOT0 et BOOT1, avec 0 et 1 représentant les niveaux bas et élevés.

&emsp; &emsp; Sur le pcb, le mode de démarrage est sélectionné par le commutateur DIP illustré dans la figure suivante, et le module principal a été conçu pour tirer boot0 et BOOT1, et le côté du voyant de numérotation marquant ON représente le bit pull down correspondant effectif, et l'autre côté de ON correspond à OFF représente le pull-up effectif.

&emsp; &emsp; Le K510 détermine le mode de démarrage de la puce en fonction de l'état des broches matérielles boot0 et BOOT1, et la sélection du mode de démarrage est indiquée dans le tableau suivant.

<center>Tableau 2-1 Modes de démarrage</center>

| DÉMARRAGE1   | BOOT0   | Mode de démarrage      |
| ------- | ------- | ------------ |
| 0(ON)   | 0(ON)   | Démarrage du port série      |
| 0(ON)   | 1(DÉSACTIVÉ)  | Les bottes de la carte SD      |
| 1(DÉSACTIVÉ)  | 0(ON)   | Bottes NANDFLASH |
| 1(DÉSACTIVÉ)  | 1(DÉSACTIVÉ)  | Bottes EMMC      |

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_9.jpg" width=60%>
</div>

<center>Figure 3-9 Commutateur de réinitialisation et commutateur DIP du mode de démarrage</center>

&emsp; &emsp; Le bouton de réinitialisation embarqué K510 CRB est K2 dans la Figure 3-9, qui peut être pressé pour effectuer une opération de réinitialisation matérielle du système.

<div style="page-break-after:always"></div>

## 3.7 Entrée et sortie audio

&emsp; &emsp; Le K510 CRB utilise la puce de codec audio de Nuvoton, NAU88C22, pour implémenter des fonctions d'entrée et de sortie pour la parole. Comprend un microphone intégré, une prise casque standard de 3,5 mm et un connecteur de haut-parleur 2P.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-10.jpg" width=60%>
</div>

<center>Figure 3-10 Audio</center>

## Prise USB OTG 3.8

&emsp; &emsp; La prise USB OTG intégrée K510 CRB peut être utilisée pour implémenter la fonctionnalité hôte/périphérique USB.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_11.jpg">
</div>

<center>Figure 3-11 Siège USB-OTG</center>

<div style="page-break-after:always"></div>

## 3.9 Interface UART

&emsp; &emsp; K510 CRB Afin de faciliter le développement et le débogage des utilisateurs, le K510 CRB dispose d'une interface UART USB-> à bord, qui peut être exploitée par la communication du port série USART et le débogage du K510 via le câble PC-USB. L'utilisation initiale peut nécessiter le chargement du pilote, comme indiqué à la section 4.2. L'interface UART intégrée est illustrée dans la figure ci-dessous.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_12.jpg" width=50%>
</div>

<center>Figure 3-12 Interface USB-UART</center>

## Module 3.10 WIFI/BT

&emsp; &emsp; Le K510 CRB comprend un module WIFI/BT 2-en-1 AP6212 pour étendre la carte de développement pour la connectivité réseau et les fonctions de communication Bluetooth, comme indiqué dans l'interface embarquée ci-dessous.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-13.jpg" width=40%>
</div>

<center>Figure 3-13 Module WIFI/BT</center>

<div style="page-break-after:always"></div>

## 3.11 Ethernet

&emsp; &emsp; Le K510 CRB dispose d'un support Gigabit Ethernet intégré, et le K510 est implémenté via une puce PHY externe avec une interface RGMII. L'interface embarquée est illustrée dans la figure suivante.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_14.jpg" width=60%>
</div>

<center>Figure 3-14 Interface Ethernet</center>

## Sortie hdmi 3.12

&emsp; &emsp; Le support femelle HDMI-A intégré K510 CRB peut être connecté à l'écran externe via un câble HDMI standard, à l'aide de la conversion de sortie de l'interface mipi dsi du K510. L'interface embarquée est illustrée dans la figure suivante.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_15.jpg" width=60%>
</div>

<center>Figure 3-15 Interface HDMI</center>

 **Remarque**: Étant donné que les écrans HDMI et TFT 1080P utilisent des pilotes mipi dsi, ils ne peuvent choisir qu'un seul des deux écrans, ne peuvent pas être utilisés en même temps, passez par la broche de contrôle GPIO pour sélectionner l'une des sorties.

<div style="page-break-after:always"></div>

## 3.13 Vidéo dans

&emsp; &emsp; Le K510 CRB tire mipi CSI, DVP, alimentation et GPIO partiel via un connecteur carte à carte à pas de 0,8 mm pour obtenir l'entrée de la caméra dans différents scénarios et différentes situations de demande. L'interface embarquée est illustrée dans la figure suivante. Les définitions d'interface sont présentées dans le tableau suivant.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-16.jpg">
</div>

<center>Figure 3-16 Interface Video IN</center>

<center>Tableau 3-2 Définitions de l'interface Video IN</center>

| numérotation | définition             | numérotation | définition                       |
| ---- | ---------------- | ---- | --------------- |
| 1    | VDD_5V           | 60   | GPIO_1V8_59_DVP_D12      |
| 2    | VDD_5V           | 59   | GPIO_1V8_58_DVP_D11      |
| 3    | VDD_5V           | 58   | GPIO_1V8_50_DVP_D3       |
| 4    | VDD_5V           | 57   | GPIO_1V8_51_DVP_D4       |
| 5    | GND              | 56   | GPIO_1V8_60_DVP_D13      |
| 6    | GND              | 55   | GPIO_1V8_55_DVP_D8       |
| 7    | MIPI_CSI_D0_P    | 54   | GPIO_1V8_61_DVP_D14      |
| 8    | MIPI_CSI_D0_N    | 53   | GPIO_1V8_52_DVP_D5       |
| 9    | GND              | 52   | GPIO_1V8_47_DVP_D0       |
| 10   | MIPI_CSI_CLK0_P  | 51   | GPIO_1V8_56_DVP_D9       |
| 11   | MIPI_CSI_CLK0_N  | 50   | GPIO_1V8_53_DVP_D6       |
| 12   | GND              | 49   | GPIO_1V8_57_DVP_D10      |
| 13   | MIPI_CSI_D1_P    | 48   | GPIO_1V8_48_DVP_D1       |
| 14   | MIPI_CSI_D1_N    | 47   | GPIO_1V8_54_DVP_D7       |
| 15   | GND              | 46   | GPIO_1V8_64_DVP_HREF     |
| 16   | MIPI_CSI_D2_N    | 45   | GPIO_1V8_49_DVP_D2       |
| 17   | MIPI_CSI_D2_P    | 44   | GPIO_1V8_65_DVP_DEN      |
| 18   | GND              | 43   | GPIO_1V8_66_DVP_PCLK     |
| 19   | MIPI_CSI_CLK1_N  | 42   | GPIO_1V8_62_DVP_D15      |
| 20   | MIPI_CSI_CLK1_P  | 41   | GPIO_1V8_63_DVP_VSYNC    |
| 21   | GND              | 40   | GPIO_1V8_82 |
| 22   | MIPI_CSI_D3_N    | 39   | GPIO_1V8_67  |
| 23   | MIPI_CSI_D3_P    | 38   | GPIO_1V8_68  |
| 24   | GND              | 37   | GPIO_1V8_72  |
| 25   | MIPI_CSI_I2C_SCL | 36   | GPIO_1V8_73  |
| 26   | MIPI_CSI_I2C_SCA | 35   | GPIO_1V8_74  |
| 27   | GND              | 34   | GND          |
| 28   | GND              | 33   | GND          |
| 29   | 1V8              | 32   | 3V3          |
| 30   | 1V8              | 31   | 3V3          |

**Remarque**: Faites attention à la plage de niveau des broches connectées lors de la connexion externe pour éviter que la mauvaise entrée de tension n'endommage définitivement la puce K510.

<div style="page-break-after:always"></div>

## 3.14 Sortie vidéo

&emsp; &emsp; Le K510 CRB dispose d'un rabat 30P de pas de 0,5 mm sous le connecteur FPC pour la connexion à un écran LCD externe, comme illustré dans la figure ci-dessous. Les définitions d'interface sont présentées dans le tableau suivant.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-17.jpg">
</div>

<center>Figure 3-17 Interface de sortie vidéo</center>

<center>Tableau 3-3 Définitions de l'interface de sortie vidéo</center>

| numérotation | définition              | numérotation | définition             |
| ---- | ----------------- | ---- | ---------------- |
| 1    | GND               | 16   | MIPI_DSI_D1_N    |
| 2    | GND               | 17   | MIPI_DSI_D1_P    |
| 3    | VDD_5V            | 18   | GND              |
| 4    | VDD_5V            | 19   | MIPI_DSI_CLK_N   |
| 5    | VDD_3V3           | 20   | MIPI_DSI_CLK_P   |
| 6    | VDD_3V3           | 21   | GND              |
| 7    | GND               | 22   | MIPI_DSI_D0_N    |
| 8    | TOUCH_1V8_I2C_SCL | 23   | MIPI_DSI_D0_P    |
| 9    | TOUCH_1V8_I2C_SDA | 24   | GND              |
| 10   | TOUCH_1V8_INT     | 25   | MIPI_DSI_D3_N    |
| 11   | TOUCH_1V8_RST     | 26   | MIPI_DSI_D3_P    |
| 12   | GND               | 27   | GND              |
| 13   | MIPI_DSI_D2_N     | 28   | MIPI_DSI_LCD_RST |
| 14   | MIPI_DSI_D2_P     | 29   | MIPI_DSI_LCD_EN  |
| 15   | GND               | 30   | GND              |

<div style="page-break-after:always"></div>

## 3.15 Extension de l'interface

&emsp; &emsp; Afin de faciliter la mise en œuvre de fonctions d'extension personnalisées pour les utilisateurs, une broche d'extension 30P 2,54 mm est réservée sur le CRB K510, ce qui conduit à une alimentation et à une partie du GPIO, que l'utilisateur peut utiliser via le logiciel iomux pour mapper des ressources matérielles telles que I2C, UART, SPI au GPIO correspondant pour obtenir une connexion externe et l'extension des fonctions correspondantes. L'interface embarquée est illustrée dans la figure suivante. Les définitions détaillées sont présentées dans le tableau suivant.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw-3-18.jpg">
</div>

<center>Figure 3-18 Interface d'extension de broche 40P</center>

<center>Tableau 3-4 Définitions d'interface étendues</center>

| numérotation | définition         | numérotation | définition         |
| ---- | ------------ | ---- | ------------ |
| 1    | VDD_1V8      | 2    | GND          |
| 3    | VDD_1V8      | 4    | GND          |
| 5    | VDD_3V3      | 6    | GND          |
| 7    | VDD_3V3      | 8    | GND          |
| 9    | VDD_5V       | 10   | GND          |
| 11   | VDD_5V       | 12   | GPIO_1V8_95  |
| 13   | GPIO_3V3_114 | 14   | GPIO_3V3_115 |
| 15   | GPIO_1V8_92  | 16   | GPIO_1V8_96  |
| 17   | GPIO_1V8_105 | 18   | GPIO_1V8_107 |
| 19   | GPIO_1V8_104 | 20   | GPIO_1V8_106 |
| 21   | GPIO_1V8_118 | 22   | GPIO_1V8_119 |
| 23   | GPIO_1V8_93  | 24   | GPIO_1V8_94  |
| 25   | GPIO_3V3_125 | 26   | GPIO_3V3_124 |
| 27   | GPIO_3V3_127 | 28   | GPIO_3V3_126 |
| 29   | GND          | 30   | GND          |

**Remarque**: Faites attention à la plage de niveau des broches connectées lors de la connexion externe pour éviter que la mauvaise entrée de tension n'endommage définitivement la puce K510.

<div style="page-break-after:always"></div>

# 4 Utilisation de la carte de développement

## 4.1 Installation du pilote

&emsp; &emsp; Le K510 CRB a ch340E intégré pour implémenter la fonction de communication USB-UART, de sorte que le pilote correspondant doit être installé avant utilisation.

&emsp; &emsp; Utilisez le pilote dans le package ou téléchargez-le et installez-le à l'adresse suivante.

&emsp;&emsp;<http://www.wch.cn/product/CH340.html>

## 4.2 Gravure du firmware

&emsp; &emsp; Veuillez vous référer à[la](./K510_SDK_Build_and_Burn_Guide.md)documentation K510_SDK_Build_and_Burn_Guide.

## 4.3 Allumer et éteindre

&emsp; &emsp; 1) Installez le câble d'alimentation et le câble de débogage USB.

&emsp; &emsp; 2) Commutateur DIP sélectionné pour démarrer à partir de la carte TF.

&emsp; &emsp; 3) Allumez l'interrupteur en basculant l'interrupteur comme indiqué à la section 3.2.

## 4.4 Débogage du port série

&emsp; &emsp; Une fois le pilote installé, mettez le CRB K510 sous tension, auquel cas le port apparaît dans le Gestionnaire de périphériques - Port du PC.

&emsp; &emsp; À l'aide de l'outil de débogage de port série, ouvrez le numéro de port du périphérique, débit en bauds 115200.

&emsp; &emsp; Comme le montre la figure suivante, le périphérique est « COM6 », qui est affiché dans le Gestionnaire de périphériques PC.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_4_1.jpg">
</div>

<center>Figure 4-1 Gestionnaire de périphériques une fois l'installation du pilote terminée</center>

**Clause de non-responsabilité en matière de**  
Pour la commodité des clients, Canaan utilise un traducteur IA pour traduire du texte en plusieurs langues, ce qui peut contenir des erreurs. Nous ne garantissons pas l'exactitude, la fiabilité ou l'actualité des traductions fournies. Canaan ne sera pas responsable de toute perte ou dommage causé par la confiance accordée à l'exactitude ou à la fiabilité des informations traduites. S'il existe une différence de contenu entre les traductions dans différentes langues, la version simplifiée en chinois prévaudra.

Si vous souhaitez signaler une erreur de traduction ou une inexactitude, n'hésitez pas à nous contacter par courrier.
