![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">Guide de génération et de gravure du SDK K510</font>**

<font face="黑体"  size=3>Version du document : V1.0.0</font>

<font face="黑体"  size=3>Date de publication : 2022-03-07</font>

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

| Le numéro de version   | Modifié par     | Date de révision | Notes de révision |
|  :-----  |-------   |  ------  |  ------  |
| Version 1.0.0 | Division des produits d'IA | 2022-03-07 |          |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenu</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Introduction

Ce document décrit le contenu de la section de construction de l'environnement de développement, comme le téléchargement, la compilation et la gravure du Kit de développement logiciel (SDK) K510.

# 2 k510 sdk

## 2.1 k510 sdk télécharger

Adresse du projet SDK k510 : <https://github.com/kendryte/k510_buildroot>

Obtenez le SDK k510 :

```shell
git clone https://github.com/kendryte/k510_buildroot.git
```

## 2.2 Présentation du package sdk k510

Le SDK K510 est un environnement de développement Linux embarqué basé sur le buildroot comme framework de base, basé sur le noyau Linux K510 (linux version 4.17.0), u-boot (u-boot version 2020.01), riscv-pk-k510 (BBL) package de code source, la structure de répertoire K510 SDK est illustrée dans la figure suivante.

![](../zh/images/sdk_build/image-buildroot.png)

 Les fichiers du SDK K510 sont décrits comme suit :

| **lime**        | **Description du contenu**                                                 |
| --------------- | ------------------------------------------------------------ |
| planche           | Dossier, qui est K510 divers fichiers de configuration et scripts, tels que le fichier de configuration pour générer des images (genimage-xxx.cfg), les scripts post-image buildroot, les variables d'environnement par défaut U-Boot, etc. |
| Config.in       | Il indique le package qui nécessite une compilation buildroot. |
| configurations         | Dossier, où se trouve le fichier de configuration de compilation par défaut de la carte. Enregistre actuellement les fichiers de configuration de compilation par défaut pour les cartes K510 CRB-V0.1, K510 CRB-V1.2 et K510 EVB :<br /> -`k510_crb_lp3_v1_2_defconfig`<br />-`k510_crb_lp3_v0_1_defconfig`<br />- `k510_evb_lp3_v1_1_defconfig` |
| external.desc   | Fichier de configuration du mécanisme externe de Buildroot. |
| external.mk     | |
| Makefile        | Makefile principal du SDK k510. |
| colis         | Les dossiers, qui sont principalement des applications K510, Config.in le contenu du fichier détermineront quelles applications sont compilées sous ce répertoire. |
| Correctifs         | Dossier, où est le fichier de correctif buildroot, Makefile décompresse le code source lorsque le fichier de correctif dans ce répertoire dans le répertoire de code source correspondant. |
| pkg-télécharger    | Folder, qui est un package compressé du dossier dl. |
| README.md       | Instructions relatives au SDK. |
| release_note.md | |
| chaîne d'outils       | , où se trouve la chaîne d'outils de compilation croisée. |
| Dl              | Dossier, est le paquet d'extraction dl dans pkg-download, s'il y a d'autres paquets ajoutés sera également téléchargé dans ce répertoire. |

## Version du sdk k510 2.3

Lorsque vous gravez l'image générée par le kit de développement logiciel (sdk) k510 sur la carte, les informations de version sont imprimées, comme illustré dans la figure suivante :

```text
#############SDK VERSION############################################
MX2_DEV_0106-02e87077-20220428-153936CST-xxxxx-server
####################################################################
```

Une fois le démarrage terminé, entrez ce qui suit dans le terminal shell pour afficher les informations de version du SDK :

```shell
cat /etc/version/release_version
#############SDK VERSION############################################
MX2_REL_0106-02e87077-20220428-153936CST-xxxx-server
####################################################################
```

**Remarque : Les informations ci-dessus peuvent varier en fonction de la version du sdk k510**. 

# 3 environnement de compilation docker

Après avoir téléchargé le sdk k510, exécutez la commande suivante dans le répertoire parent du sdk pour démarrer le docker :

```shell
sh k510_buildroot/tools/docker/run_k510_docker.sh
```

Les opérations de compilation suivantes sont effectuées dans docker par défaut.
Si vous devez configurer un environnement local, reportez-vous à la section[ Configuration de l'environnement local](#env_set)

# 4 Compiler

## 4.1 Préparation de la compilation

### 4.1.1 Télécharger le paquet de code source (facultatif, peut accélérer la compilation)

Exécutez la commande suivante pour télécharger le package source :

```shell
make dl
```

## 4.2 Compilation

K510_buildroot/config contient des fichiers de configuration de compilation pour trois cartes de développement, à savoir`k510_crb_lp3_v0_1_defconfig` , ,`k510_crb_lp3_v1_2_defconfig` et `k510_evb_lp3_v1_1_defconfig`, ce document est illustré en sélectionnant k510_crb_lp3_v1_2_defconfig comme cible** de compilation**. 

Dans l'environnement docker k510, entrez la commande suivante pour lancer la compilation :

```shell
make CONF=k510_crb_lp3_v1_2_defconfig
```

![](../zh/images/sdk_build/image-make.png)

Le message suivant indique que la compilation s'est terminée avec succès.

![](../zh/images/sdk_build/image-uboot_r.png)

Une fois la compilation terminée, le dossier est généré`k510_crb_lp3_v1_2_defconfig`. 

![image-20220311121912711](../zh/images/sdk_build/image-makeout.png)

Chacun de ces documents est décrit comme suit :

| **lime**    | **Description du contenu**                                                 |
| ----------- | ------------------------------------------------------------ |
| Makefile    | Compilez l'image pour utiliser Makefile.                                     |
| construire       | Répertoire de compilation de tous les packages sources. Par exemple, noyau linux, u-boot, BBL, busybox, etc., le code source sera extrait dans le répertoire de build et compilé. |
| hôte        | Tous les chemins d'installation du package hôte, la chaîne d'outils seront également copiés dans ce répertoire pour créer des environnements de compilation croisée. |
| Images      | Compilez le répertoire de fichiers cibles résultant (voir les instructions ci-dessous pour plus de détails)                     |
| nand_target | Répertoire brut du système de fichiers racine (utilisé pour générer des images NandFlash)                  |
| cible      | Répertoire brut du système de fichiers racine (pour générer des images eMMC et de carte SD à utiliser)                 |

K510_crb_lp3_v1_2_defconfig/images est une image gravée, dans laquelle la description de chaque fichier est la suivante.

| **lime**                   | **Description du contenu**                                                 |
| -------------------------- | ------------------------------------------------------------ |
| bootm-bbl.img              | Image du noyau Linux+bbl (fichier cible bpl du noyau empaqueté pour uboot boot bbl) |
| k510.dtb                   | Arborescence des périphériques                                                       |
| sysimage-emmc.img          | emmc graver des fichiers : l'ensemble du paquet a été empaqueté uboot_burn, noyau et bbl              |
| sysImage-sdcard.img        | fichiers de gravure sdcard : l'ensemble du paquet a été empaqueté uboot_burn, noyau et bbl            |
| sysImage-nand.img          | nand burn files: L'ensemble du paquet a été empaqueté uboot_burn, noyau et bbl              |
| u-boot.bin                 | Fichier binaire uboot                                             |
| u-boot_burn.bin            | uboot grave des fichiers                                               |
| uboot-emmc.env             | Variable d'environnement uboot : utilisée pour le démarrage d'emmc                                  |
| uboot-sd.env               | Variable d'environnement uboot : utilisée pour le démarrage de la carte sdcard                                |
| uboot-nand.env             | Variable d'environnement uboot : utilisée pour le démarrage de nand                                  |
| vmlinux                    | Fichier image du noyau Linux (avec informations de débogage elf)                           |
| rootfs.ext2                | Fichier image rootfs ext2 au format Buildroot                             |
| sysimage-sdcard-debian.img | sdcard burn files: images de carte (rootfs au format debian)                     |

K510_crb_lp3_v1_2_defconfig/build est le code source de tous les objets compilés, dont plusieurs sont des documents importants décrits ci-dessous.

| **lime**         | **Description du contenu**                  |
| ---------------- | ----------------------------- |
| linux-xxx        | Le répertoire source du noyau Linux compilé |
| uboot-xxx        | Le répertoire source Uboot compilé       |
| riscv-hp-k510-xxx| Répertoire source bbl où le code est compilé         |
| ...              |                               |

Remarque : xxx est le numéro de version. Lorsque les références aux chemins de kernle, bbl et uboot dans les sections ultérieures, xxx représentent toutes des numéros de version.

** Besoin d'une attention particulière:** Lors du nettoyage, tout ce qui se trouve sous le dossier k510_crb_lp3_v1_2_defconfig sera supprimé. Par conséquent, si vous devez modifier le noyau, le code bbl ou uboot, ne le modifiez pas directement dans le répertoire de build, vous pouvez vous référer au chapitre 5 pour utiliser la méthode de remplacement de la source.

## 4.1 Configurer buildroot

Entrez la commande buildroot de configuration dans l'environnement docker k510 :

```shell
make CONF=k510_crb_lp3_v1_2_defconfig menuconfig
```

Les résultats de l'exécution sont les suivants :

![](../zh/images/sdk_build/image-make_men.png)

![](../zh/images/sdk_build/image-make_menu.png)

Après avoir terminé la configuration, enregistrer et quitter, vous devez également exécuter la commande buildroot configuration save suivante :

```shell
make CONF=k510_crb_lp3_v1_2_defconfig savedefconfig
```

Les résultats de l'exécution sont les suivants :

![](../zh/images/sdk_build/image-make_savedef.png)

Une fois l'opération ci-dessus terminée, l'utilisateur peut entrer la commande suivante pour recompiler :

```shell
make CONF=k510_crb_lp3_v1_2_defconfig
```

## 4.2 Configurer U-Boot

Lorsque vous devez modifier la configuration uboot, vous pouvez entrer le répertoire k510_crb_lp3_v1_2_defconfig et entrer la commande suivante pour démarrer la configuration U-Boot :

```shell
make uboot-menuconfig
```

Les résultats de l'exécution sont les suivants :

![](../zh/images/sdk_build/image-uboot_men.png)

![](../zh/images/sdk_build/image-uboot_menu.png)

Lorsque vous quittez le menuuonfig après avoir terminé la configuration, sélectionnez Enregistrer la configuration et vous devez exécuter la commande d'enregistrement de configuration suivante :

```shell
make uboot-savedefconfig
```

Les résultats de l'exécution sont les suivants :

![](../zh/images/sdk_build/image-uboot_savedefconfig.png)

Enfin, dans le répertoire k510_crb_lp3_v1_2_defconfig, entrez la commande suivante pour démarrer la compilation :

```shell
make uboot-rebuild
```

Voir la description dans la section suivante pour plus d'informations.

## 4.3 Compiler le U-Boot

Le code source U-Boot compilé est stocké dans le répertoire k510_crb_lp3_v1_2_defconfig/build/uboot-xxx, et le U-Boot doit être recompilé que l'utilisateur modifie le code source U-Boot ou reconfigure uboot.

Entrez le répertoire k510_crb_lp3_v1_2_defconfig et entrez la commande suivante pour recompiler U-Boot :

```shell
make uboot-rebuild
```

Les résultats de l'exécution sont les suivants :

![](../zh/images/sdk_build/image-uboot-rebuild.png)

Une fois la compilation terminée, un nouveau fichier u-boot .bin est généré dans le répertoire k510_crb_lp3_v1_2_defconfig/images.

Si vous souhaitez régénérer le fichier image gravé avec un nouveau u-boot,`k510_crb_lp3_v1_2_defconfig` exécutez :dans le répertoire

```shell
make
```

Les résultats de l'exécution sont les suivants :

![](../zh/images/sdk_build/image-make_u.png)

Une fois la compilation terminée, vous verrez les informations générées par le fichier image suivant.

![](../zh/images/sdk_build/image-uboot_r.png)

## 4.4 Configurer le noyau Linux

Lorsque vous devez modifier la configuration du noyau, vous pouvez entrer dans le répertoire k510_crb_lp3_v1_2_defconfig et entrer la commande suivante pour démarrer la configuration du noyau :

```shell
make linux-menuconfig
```

Les résultats de l'exécution sont les suivants :

![](../zh/images/sdk_build/image-linux_men.png)

![](../zh/images/sdk_build/image-linux_menu.png)

Lorsque vous quittez menuufig après avoir modifié la configuration, sélectionnez Enregistrer la configuration, puis exécutez la commande d'enregistrement de configuration suivante :

```shell
make linux-savedefconfig
```

Les résultats de l'exécution sont les suivants :

![](../zh/images/sdk_build/image-linux_savedefconfig.png)

Enfin, dans le répertoire k510_crb_lp3_v1_2_defconfig, entrez la commande suivante pour démarrer la compilation :

```shell
make linux-rebuild
```

Voir la description dans la section suivante pour plus d'informations.

## 4.5 Compiler le noyau Linux

K510_crb_lp3_v1_2_defconfig/build/linux-xxx contient le code source Linux compilé, que l'utilisateur modifie le code source Linux ou reconfigure Linux, il doit être recompilé.

Entrez le répertoire k510_crb_lp3_v1_2_defconfig et entrez la commande suivante pour recompiler linux :

```shell
make linux-rebuild
```

Les résultats de l'exécution sont les suivants :

![](../zh/images/sdk_build/image-linux_rebuild.png)

Après la compilation, un nouveau vmlinux est généré dans le répertoire k510_crb_lp3_v1_2_defconfig/images.

L'image du noyau Linux doit être empaquetée avec bbl, après avoir réécrit le noyau Linux, vous devez recompiler le bbl pour générer une nouvelle image bbl/kernel pour le démarrage, alors entrez les deux commandes suivantes.

```shell
make riscv-pk-k510-dirclean
make riscv-pk-k510
```

Les résultats de l'exécution sont les suivants :

![](../zh/images/sdk_build/image-riscv.png)

Une fois la compilation terminée, une `k510_crb_lp3_v1_2_defconfig/images`nouvelle compilation est générée dans le répertoire`bootm-bbl.img`. 

Enfin, entrez make dans le répertoire k510_crb_lp3_v1_2_defconfig et utilisez le nouveau package bootm-bbl.img pour générer des fichiers image emmc et de carte SD.

```shell
make
```

Les résultats de l'exécution sont les suivants :

![](../zh/images/sdk_build/image-make_u.png)

Une fois la compilation terminée, vous verrez les informations générées par le fichier image suivant.

![](../zh/images/sdk_build/image-uboot_r.png)

## 4.6 Compiler les dts

Le fichier de l'arborescence des périphériques se trouve dans le répertoire k510_buildroot/k510_crb_lp3_v1_2_defconfig/build/linux-4.17/arch/riscv/boot/dts/canaan, et lorsque l'utilisateur modifie uniquement l'arborescence des périphériques, seule l'arborescence des périphériques peut être compilée et décompilée.

Écrivez un script mkdtb-local.sh qui se lit comme suit :

```shell
# !/bin/sh

set -Eeuo pipefail

export BUILDROOT="$(dirname "$(realpath "$0")")"
export VARIANT="${1:-k510_crb_lp3_v1_2}"

if [[ "$VARIANT" = *_defconfig ]]; then
        VARIANT="${VARIANT:0:-10}"
fi

export KERNEL_BUILD_DIR="$BUILDROOT/${VARIANT}_defconfig/build/linux-4.17"
export BINARIES_DIR="$BUILDROOT/${VARIANT}_defconfig/images"
export PATH+=":$BUILDROOT/toolchain/nds64le-linux-glibc-v5d/bin"

riscv64-linux-cpp -nostdinc -I "${KERNEL_BUILD_DIR}/include" -I "${KERNEL_BUILD_DIR}/arch" -undef -x assembler-with-cpp "${KERNEL_BUILD_DIR}/arch/riscv/boot/dts/canaan/${VARIANT}.dts" "${BINARIES_DIR}/${VARIANT}.dts.tmp"

"${KERNEL_BUILD_DIR}/scripts/dtc/dtc" -I dts -o "${BINARIES_DIR}/k510.dtb" "${BINARIES_DIR}/${VARIANT}.dts.tmp"
"${KERNEL_BUILD_DIR}/scripts/dtc/dtc" -I dtb -O dts "${BINARIES_DIR}/k510.dtb" -o "${BINARIES_DIR}/all.dts"

echo "DONE"
echo "${BINARIES_DIR}/k510.dtb"
echo "${BINARIES_DIR}/all.dts"
```

Placez le mkdtb-local.sh dans le répertoire K510_buildroot et exécutez la commande suivante pour compiler l'arborescence des périphériques de la carte k510_crb_lp3_v1_2_defconfig :

```shell
./mkdtb-local.sh k510_crb_lp3_v1_2_defconfig
```

Les résultats de l'exécution sont les suivants :

![](../zh/images/sdk_build/image-mdk_dts.png)

K510.dtb dans le répertoire k510_crb_lp3_v1_2_defconfig/images est le fichier de base de données de l'arborescence des périphériques nouvellement généré et all.dts est le fichier d'arborescence des périphériques décompilé.

## 4.7 Compiler l'application

Les utilisateurs peuvent se référer à `package/hello_world` l'écriture de fichiers Config.in et makefile pour créer leurs propres applications, et les applications utilisateur sont placées dans le répertoire k510_buildroot/package. 

Le processus de compilation d'une application est illustré en plaçant hello_world projets dans k510_buildroot/package à titre d'exemple.

Modifiez les fichiers Config.in dans le répertoire k510_buildroot de l'environnement d'hébergement.

![](../zh/images/sdk_build/image-vi_config.png)

Dans la Config.in, ajoutez le chemin d'accès où se trouve package/hello_world/Config.in et enregistrez.

![](../zh/images/sdk_build/image-config_list.png)

Entrez la commande buildroot de configuration dans l'environnement docker k510 :

```shell
make CONF=k510_crb_lp3_v1_2_defconfig menuconfig
```

Les résultats de l'exécution sont les suivants :

![](../zh/images/sdk_build/image-build_menu.png)

La page de configuration buildroot s'affiche, sélectionnez l'option Étendue, puis sélectionnez la hello_world, puis enregistrez et quittez.

![](../zh/images/sdk_build/image-extern_option.png)

Entrez la commande Enregistrer la configuration dans le répertoire k510_buildroot.

```shell
make CONF=k510_crb_lp3_v1_2_defconfig savedefconfig
```

Les résultats de l'exécution sont les suivants :

![](../zh/images/sdk_build/image-build_savedef.png)

1) Si c'est la première fois que vous compilez, les étapes sont les suivantes:

Dans le répertoire k510_buildroot, entrez la commande suivante pour compiler l'ensemble du programme du projet et empaqueter hello dans des fichiers image emmc et carte SD.

```shell
make CONF=k510_crb_lp3_v1_2_defconfig
```

Les résultats de l'exécution sont les suivants :

![](../zh/images/sdk_build/image-build_make_def.png)

Dans le répertoire k510_buildroot/k510_crb_lp3_v1_2_defconfig/target, vous pouvez voir l'application hello résultante, qui indique si l'application a été compilée correctement.

![](../zh/images/sdk_build/image-hello.png)

2) S'il a été compilé, compilez simplement l'application et empaquetez-la dans l'image de gravure, procédez comme suit:

Entrez le répertoire k510_buildroot/k510_crb_lp3_v1_2_defconfig et entrez la commande suivante pour compiler l'application hello.

```shell
make hello_world-rebuild
```

Les résultats de l'exécution sont les suivants :

![](../zh/images/sdk_build/image-app_build-1.png)

Allez dans le répertoire k510_buildroot/k510_crb_lp3_v1_2_defconfig et entrez la commande make pour empaqueter hello dans les fichiers image emmc et sd card.

```shell
make
```

Les résultats de l'exécution sont les suivants :

![](../zh/images/sdk_build/image-app-build-2.png)

# 5 Développer à l'aide du SDK K510

## 5.1 Code source du noyau Linux / BBL / uboot

La version uboot utilisée par ce SDK est 2020.01, le répertoire du correctif uboot est package/patches/uboot et le répertoire après l'application de correctifs est k510_xxx_defconfig/build/uboot-2020.01.

Le répertoire de correctifs du noyau utilisé par ce sdk est 4.17, le répertoire de correctifs du noyau est package/patches/linux et le répertoire patché est k510_xxx_defconfig/build/linux-4.17.

Le BBL de ce sdk est placé en tant que package cible dans le package/riscv-pk-k510/directory, et la source et le numéro de version du bbl sont spécifiés dans le riscv-pk-k510.mk :

```text
RISCV_PK_K510_VERSION = 1e666d6c5dbab220d2ca57fbd9bec49702599b75
RISCV_PK_K510_SITE = git@github.com:kendryte/k510_BBL.git
RISCV_PK_K510_SITE_METHOD = git
```

## 5.2 Développer le noyau Linux / BBL / uboot

Chaque pacification compilée sous Buildroot, y compris le noyau Linux / BBL / uboot, est implémentée en téléchargeant tarball, décompressant, configurant, compilant, installant et d'autres étapes de gestion de paquet unifiées, donc bien que tout le code source puisse être vu dans le répertoire k510_buildroot / k510_crb_lp3_v1_2_defconfig / build, il n'y a pas d'informations de contrôle de version. Même si le code est téléchargé à partir d'un dépôt git.

Bien que le code source kernel/BBL/uboot contenant les données du référentiel git puisse être vu dans le répertoire dl/, buildroot ne met en cache que le code source dans le répertoire dl et il n'est pas recommandé de développer directement dans ce répertoire.

Pour le modèle de développement, buildroot fournit un moyen de OVERRIDE_SRCDIR.

En termes simples, vous pouvez ajouter un fichier local.mk sous le répertoire k510_crb_lp3_v1_2_defconfig et l'ajouter:

```text
<pkg1>_OVERRIDE_SRCDIR = /path/to/pkg1/sources
```

- LINUX est le nom de paquet du noyau
- UBOOT est le nom PACKAGE de uboot
- RISCV_PK_K510 est le nom de package du bbl

Prenons le noyau Linux comme exemple pour décrire comment l'utiliser.
En supposant que j'ai cloné le code du noyau dans le répertoire /data/yourname/workspace/k510_linux_kernel et apporté des modifications, et que je souhaite compiler sous buildroot et le tester sur la carte crb v1.2, vous pouvez créer un local.mk dans le répertoire k510_crb_lp3_v1_2_defconfig et ajouter ce qui suit :

```text
LINUX_OVERRIDE_SRCDIR = /data/yourname/workspace/k510_linux_kernel
```

Exécuter dans le répertoire k510_crb_lp3_v1_2_defconfig

```shell
make linux-rebuild
```

Vous pouvez voir que le noyau a été recompilé dans le répertoire build/linux-custom, en utilisant le code modifié sous /data/yourname/workspace/k510_linux_kernel.
UBOOT et BBL sont similaires. De cette façon, vous pouvez modifier directement le code du noyau et réécrire le noyau sous buildroot, et compiler incrémentiellement l'image à tester.
Remarque : Le code source de override sera ajouté au suffixe de custom dans le nom de répertoire du répertoire k510_crb_lp3_v1_2_defconfig/build pour distinguer la source de chaque package dans la configuration par défaut de buildroot. Par exemple, dans l'exemple du noyau Linux ci-dessus, la compilation verra que le code spécifié par le overrideide est compilé dans le répertoire k510_crb_lp3_v1_2_defconfig/build/linux-custom, plutôt que dans le répertoire k510_crb_lp3_v1_2_defconfig/build/linux-xxx que nous avons vu précédemment.

Pour les autres codes du répertoire de package, ou les paquets natifs buildroot, il est possible de développer sous le framework buildroot de cette manière.

# 6 Graver l'image

K510 prend en charge le mode de démarrage sdcard et eMMC, chaque fois que la compilation dans le répertoire k510_buildroot/k510_crb_lp3_v1_2_defconfig/image génère des fichiers image sysimage-sdcard.img et sysimg-emmc.img, les deux fichiers peuvent être gravés sur sdcard et eMMC respectivement.

Le K510 détermine le mode de démarrage de la puce par l'état des broches matérielles boot0 et BOOT1, veuillez vous référer à la section des instructions de démarrage de la carte de développement pour des paramètres spécifiques.

| DÉMARRAGE1   | BOOT0   | Mode de démarrage      |
| ------- | ------- | ------------ |
| 0(ON)   | 0(ON)   | Démarrage du port série      |
| 0(ON)   | 1(DÉSACTIVÉ)  | Les bottes de la carte SD      |
| 1(DÉSACTIVÉ)  | 0(ON)   | Bottes NANDFLASH |
| 1(DÉSACTIVÉ)  | 1(DÉSACTIVÉ)  | Bottes EMMC      |

![](../zh/images/hw_crb_v1_2/clip_hw_3_9.jpg)

## 6.1 Graver l'image sur la carte SD

### 6.1.1 ubuntu gravé

Avant d'insérer la carte sD dans l'hôte, entrez :

```shell
ls -l /dev/sd*
```

Affichez le périphérique de stockage actuel.

Après avoir inséré la carte sD dans l'hôte, entrez-la à nouveau:

```shell
ls -l /dev/sd*
```

En regardant le périphérique de stockage à l'heure actuelle, le nouvel ajout est le nœud de périphérique de carte SD.

Après avoir inséré la carte sD dans l'hôte, le résultat d'exécution de la commande ls est le suivant :

![](../zh/images/sdk_build/image-dev_sd.png)

/dev/sdc est le nœud de périphérique de carte SD. **Remarque : Le nœud de périphérique de carte SD généré dans l'environnement utilisateur peut ne pas être /dev/sdc, et les opérations suivantes doivent être modifiées en fonction du nœud réel. **

Entrez le répertoire k510_buildroot/k510_crb_lp3_v1_2_defconfig/image sous l'hôte et entrez la commande dd pour graver sysimage-sdcard.img sur le sdk :

```shell
sudo dd if=sysimage-sdcard.img of=/dev/sdc bs=1M oflag=sync
```

Le résultat d'exécution sous l'hôte est le suivant :

![](../zh/images/sdk_build/image-dd.png)

### 6.1.2 Graver sous Windows

Sous Windows, la carte sD peut être gravée par l'outil Banane Etcher (adresse de téléchargement de l'outil Balena Etcher<https://www.balena.io/etcher/>). 

1) Insérez la carte TF dans le PC, puis lancez l'outil ColumnEtcher, cliquez sur le bouton « Flash à partir du fichier » de l'interface de l'outil, sélectionnez le firmware à graver, comme illustré dans la figure suivante.

![](../zh/images/sdk_build/image-sd_pre0.png)

2) Cliquez sur le bouton « Sélectionner la cible » de l'interface de l'outil et sélectionnez la carte SD cible.

![](../zh/images/sdk_build/image-pre1.png)

3) Cliquez sur le bouton « Flash » pour commencer à clignoter, le processus de clignotement a un affichage de la barre de progression, flash Finish sera invité après la fin du clignotement.

| ![](../zh/images/sdk_build/clip_image_p1.jpg) | ![](../zh/images/sdk_build/clip_image_p2.jpg) |
| --------------------------------------- | --------------------------------------- |
|                                         |                                         |

4) Lorsque le clignotement est terminé, insérez la carte SD dans l'emplacement de la carte de développement, sélectionnez BOOT pour démarrer à partir de SD, et enfin la carte de développement peut être mise sous tension pour démarrer à partir de la carte SD.

## 6.2 Graver l'image sur emmc

Pour graver le fichier sysimage-emmc.img sur l'eMMC intégré, à l'aide du sdk, dans l'environnement ubuntu, le sysimage-emmc.img est stocké dans la partition utilisateur du sdk, puis le sdk est inséré dans la carte et mis sous tension.

Avant de graver l'image emmc, vous devez démonter le système de fichiers lié à emmc, veuillez vous référer aux étapes suivantes pour le démonter.

```shell
mount | grep emmc
```

Le résultat de l'exécution est le suivant :

![](../zh/images/sdk_build/image-emmc_1.png)

Entrez la commande suivante pour désinstaller et vérifier.

```shell
umount /root/emmc/p2
umount /root/emmc/p3
umount /root/emmc/p4
mount | grep emmc
```

Le résultat de l'exécution est le suivant :

![](../zh/images/sdk_build/image-emmc_2.png)

Enfin, entrez le chemin d'accès où se trouve l'image, entrez la commande suivante pour graver eMMC.

```shell
dd if=sysimage-emmc.img of=/dev/mmcblk0 bs=1M
```

Le résultat de l'exécution est le suivant :

![](../zh/images/sdk_build/image-emmc3.png)

**Remarque: Le processus de gravure est lent, cela prend environ 30 secondes, veuillez être patient.**

Lorsque le clignotement est terminé, sélectionnez BOOT to Boot from EMMC, puis mettez la carte sous tension pour démarrer à partir d'EMMC.

# 7 Environnement de compilation configuré par l'utilisateur <a id="env_set"> </a>

Si vous n'utilisez pas l'environnement docker ci-dessus, vous pouvez configurer votre propre environnement de développement en vous référant à la commande suivante à ubuntu18.04 / 20.04, si vous n'avez pas l'autorisation, veuillez l`sudo`'utiliser. 

```shell
apt-get update
apt-get upgrade
apt-get install libc6-i386 libc6-dev-i386

apt-get install mtools
apt-get install dosfstools
apt-get install python
apt-get install python-pip
python2 -m pip install pycrypto

apt-get install python3.7
apt-get install python3-pip
python3.7 -m pip install --upgrade pip
ln -sf /usr/bin/python3.7 /usr/bin/python3
python3 -m pip install onnx==1.9.0 onnx-simplifier==0.3.6 onnxoptimizer==0.2.6 onnxruntime==1.8.0 -i https://pypi.tuna.tsinghua.edu.cn/simple

#进行下一步，需进入k510_buildroot/nncase目录，将nncase_v1.4.0.tgz解压后进入k510_buildroot/nncase/nncase_v1.4.0目录，输入如下命令安装*.whl
python3 -m pip install x86_64/*.whl
#运行python3 -m pip show nncase，若看到nncase版本信息则表示AI应用程序环境部署成功。
python3 -m pip show nncase

python3 -m pip install xlrd==1.2.0
python3 -m  pip install pystache
dpkg --add-architecture i386
apt update
apt install libncurses5:i386
apt-get install wget
apt-get install cpio
apt-get install unzip
apt-get install rsync
apt-get install bc
apt-get install libssl-dev
pip3 install pycryptodome
```

**Clause de non-responsabilité en matière de**  
Pour la commodité des clients, Canaan utilise un traducteur IA pour traduire du texte en plusieurs langues, ce qui peut contenir des erreurs. Nous ne garantissons pas l'exactitude, la fiabilité ou l'actualité des traductions fournies. Canaan ne sera pas responsable de toute perte ou dommage causé par la confiance accordée à l'exactitude ou à la fiabilité des informations traduites. S'il existe une différence de contenu entre les traductions dans différentes langues, la version simplifiée en chinois prévaudra. 

Si vous souhaitez signaler une erreur de traduction ou une inexactitude, n'hésitez pas à nous contacter par courrier.