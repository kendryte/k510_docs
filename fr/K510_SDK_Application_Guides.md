![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">Guide d'application du SDK K510</font>**

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

| Le numéro de version | Modifié par     | Date de révision   | Notes de révision     |
| :----- | ---------- | ---------- | ------------ |
| Version 1.0.0 | Groupes de logiciels système | 2022-03-09 | Lancement du SDK V1.5 |
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

# 1 Application de démonstration

## 1.1 Programme de démonstration ai

### 1.1.1 Description

Le code source du programme de démonstration de nncase se trouve dans le répertoire sous le répertoire SDK`package/ai`, et la structure de répertoires est la suivante :

```shell
$ tree -L 2 ai
ai
├── ai.hash
├── ai.mk
├── code
│   ├── build.sh
│   ├── cmake
│   ├── CMakeLists.txt
│   ├── common
│   ├── face_alignment
│   ├── face_detect
│   ├── face_expression
│   ├── face_landmarks
│   ├── face_recog
│   ├── hand_image_classify
│   ├── head_pose_estimation
│   ├── imx219_0.conf
│   ├── imx219_1.conf
│   ├── license_plate_recog
│   ├── object_detect
│   ├── object_detect_demo
│   ├── openpose
│   ├── person_detect
│   ├── retinaface_mb_320
│   ├── self_learning
│   ├── shell
│   ├── simple_pose
│   ├── video_192x320.conf
│   ├── video_object_detect_320.conf
│   ├── video_object_detect_320x320.conf
│   ├── video_object_detect_432x368.conf
│   ├── video_object_detect_512.conf
│   ├── video_object_detect_640.conf
│   └── video_object_detect_640x480.conf
└── Config.in
```

Vous pouvez vous référer au code source de la retinaface_mb_320 et`CMakeLists.txt` ajouter un nouveau programme de démonstration nncase. 

Pour la compilation du modèle, voir`nncase_demo.mk` les POST_INSTALL_TARGET_HOOKS* qui y sont définies *:

```text
NNCASE_DEMO_DEPENDENCIES += mediactl_lib nncase_linux_runtime opencv4 libdrm
define NNCASE_DEMO_COMPILE_MODEL
    mkdir -p $(TARGET_DIR)/app/ai/kmodel/kmodel_compile/retinaface_mb_320
    cd $(@D) && /usr/bin/python3 retinaface_mb_320/rf_onnx.py --quant_type uint8 --model ai_kmodel_data/model_file/retinaface/retinaface_mobile0.25_320.onnx
    cp $(@D)/rf.kmodel $(TARGET_DIR)/app/ai/kmodel/kmodel_compile/retinaface_mb_320/rf_uint8.kmodel
    cd $(@D) && /usr/bin/python3 retinaface_mb_320/rf_onnx.py --quant_type bf16 --model ai_kmodel_data/model_file/retinaface/retinaface_mobile0.25_320.onnx
    cp $(@D)/rf.kmodel $(TARGET_DIR)/app/ai/kmodel/kmodel_compile/retinaface_mb_320/rf_bf16.kmodel

NNCASE_DEMO_POST_INSTALL_TARGET_HOOKS += NNCASE_DEMO_COMPILE_MODEL
```

La compilation du modèle nécessite un environnement nncase, et pour la construction de l'environnement nncase, reportez-vous à k510_nncase_Developer_Guides.md. À l'avenir, le nncase dispose d'une mise à jour et le sdk buildroot sera mis à jour vers le nncase de manière synchrone.

### 1.1.2 Rétine

Fonction: Détection de visage, détection de repère de visage

Parcours du programme :
`/app/ai/shell`
Courir:
Exécuter un modèle `./retinaface_mb_320_bf16.sh`non quantitatif
Effectuer le modèle de quantification uint8,`./retinaface_mb_320_uint8.sh`

Il y a des paramètres pour QOS dans le script, les mêmes que pour les deux démos suivantes.

```shell
#devmem phyaddr width value
devmem 0x970E00fc 32 0x0fffff00
devmem 0x970E0100 32 0x000000ff
devmem 0x970E00f4 32 0x00550000
```

Lors de l'exécution d'une démo, il est nécessaire de s'assurer que l'affichage de l'écran est normal, c'est-à-dire d'ajuster la QoS liée à l'affichage à une priorité élevée.
QOS_CTRL0.ax25mp écriture QoS = 5
QOS_CTRL0.ax25mp lecture QoS = 5
QOS_CTRL2.ispf2k écrire QoS = 0xf
QOS_CTRL2.ispf2k lire QoS = 0xf
QOS_CTRL2.ispr2k écrire QoS = 0xf
QOS_CTRL2.ispr2k lire QoS = 0xf
QOS_CTRL2.isp3dtof écrire QoS = 0xf
QOS_CTRL3.display lire QoS = 0xf
QOS_CTRL3.display écrire QoS = 0xf

Décalage 0(QOS_CTRL0)[0x00f4]
 du registre de contrôle QOS ![qos ctrl0](../zh/images/sdk_application/demo_nncase_qos_ctrl0.png)

Décalage 
 [0x00f8]du registre de contrôle QOS 1 (QOS_CTRL1)![ qos ctrl1](../zh/images/sdk_application/demo_nncase_qos_ctrl1.png)

Décalage 
 [0x00fc]du registre de contrôle QOS 2 (QOS_CTRL2)![ qos ctrl2](../zh/images/sdk_application/demo_nncase_qos_ctrl2.png)

Décalage 
 [0x0100]du registre de contrôle QOS 3 (QOS_CTRL3)![ qos ctrl3](../zh/images/sdk_application/demo_nncase_qos_ctrl3.png)

La compilation et l'installation du modèle sont détaillées dans le paquet de fichiers/ai/ai.mk :

Compiler le chemin du script :
package/ai/code/retinaface_mb_320/rf_onnx.py

### 1.1.3 object_detect

Fonction: Détection de classification d'objets, classification 80

Parcours du programme :`/app/ai/shell`

Courir:
Exécuter un modèle `./object_detect_demo_bf16.sh`non quantitatif
Effectuer le modèle de quantification uint8,`./object_detect_demo_uint8.sh`

La compilation et l'installation du modèle sont détaillées dans le paquet de fichiers/ai/ai.mk

Compiler le chemin du script :
package/ai/code/object_detect_demo/od_onnx.py

## 1.2 ffmpeg

`ffmpeg``ffmpeg-4.4`Porté sur du code open source, ajouté`0001-buildroot-ffmpeg-0.1.patch` pour les Service Packs

- `ff_k510_video_demuxer`: Contrôle l'entrée du FAI, référencé`libvideo.so`
- `ff_libk510_h264_encoder`: Contrôle de l'encodage matériel h264, référencé`libvenc.so`

Les paramètres configurables peuvent être visualisés via la directive d'aide

```shell
ffmpeg -h encoder=libk510_h264 #查看k510编码器的参数
ffmpeg -h demuxer=libk510_video #查看demuxer的配置参数
```

Pour obtenir des instructions d'exécution détaillées, reportez-vous à[ K510_Multimedia_Developer_Guides.md](./K510_Multimedia_Developer_Guides.md)

## 1.3 alsa_demo

Le programme de démonstration alsa est placé dans`/app/alsa_demo` le répertoire :

Préparation de l'exécution :
(1) Branchez le casque

Exécutez la démo alsa:

```shell
cd /app/alsa_demo/
./alsa_demo c #录音到文件capture.pcm，demo程序仅作参考，可以参考package/alsa_demo的源码。
./alsa_demo p #播放capture.pcm
```

## 1.4 Démo TWOD

Comment exécuter la rotation:

```shell
cd /app/twod_app
./twod-rotation-app
```

Copiez l'.yuv d'impression sur le moniteur YUV et définissez la taille 1080 x 1920, format d'affichage nv12, le résultat est le suivant
![sortie.yuv](../zh/images/sdk_application/driver-twod-output-1080x1920.jpg)

Utilisation du scaler

```shell
cd /app/twod_app
./twod-scaler-app
```

Copiez l'.yuv d'impression sur le moniteur YUV et définissez la taille 640x480, format d'affichage nv12, le résultat est le suivant
![ouput.yuv](../zh/images/sdk_application/driver-twod-output-640x480.jpg)

Comment exécuter rgb2yuv:

```shell
cd /app/twod_app
./twod-osd2yuv-app
```

Copiez l'.yuv d'impression sur le moniteur YUV et définissez la taille 320x240, format d'affichage nv12, le résultat est le suivant
![ouput.yuv](../zh/images/sdk_application/twod-osd2yuv-app.jpg)

Exécutez l'utilisation de yuv2rgb:

```shell
cd /app/twod_app
./twod-scaler-output-rgb888-app
```

Copiez l'.yuv sur le moniteur rgb888 et définissez la taille 640x480, le format d'affichage rgb24, le résultat est le suivant
![ouput.yuv](../zh/images/sdk_application/driver-twod-output-640x480.jpg)

Exécuter la sortie yuv sur l'utilisation de l'osd superposé:

```shell
cd /app/twod_app
./twod-scaler-overlay-osd-app
```

Copiez l'.yuv d'impression sur le moniteur pour définir la taille 640x480, format d'affichage nv12, le résultat est le suivant
![ouput.yuv](../zh/images/sdk_application/twod-scaler-overlay-osd-app.jpg)

API:

```c
/* 创建内存 */
twod_create_fb()
/* 配置原图片参数 */   
twod_set_src_picture()
/* 配置输出图片参数 */ 
twod_set_des_picture()
/* 设置 scaler */     
twod_set_scaler()
/* 等待操作完成 */     
twod_wait_vsync()
/* Invali cache */   
twod_InvalidateCache()
/* flash cache */     
twod_flashdateCache()
/* 释放内存*/     
twod_free_mem()
/* 设置旋转 */  
twod_set_rot()
```

## 1.5 Démo RTC

Le pilote RTC enregistre le nœud de périphérique build /dev/rtc0.

La couche application suit la méthode de programmation RTC standard dans le pilote d'appel système Linux, et il est recommandé de désactiver l'impression des informations du noyau via la console shell avant d'exécuter la routine de référence.

```shell
echo 0 > /proc/sys/kernel/printk
```

Accédez au répertoire /app/rtc et entrez la commande suivante pour démarrer l'application rtc.

```shell
cd /app/rtc
./rtc 2021-11-3 21:10:59
```

Le résultat de l'exécution du programme est:

![](../zh/images/sdk_application/image-rtc.png)

L'extrait de code principal du programme de démonstration RTC est le suivant, veuillez vous référer au code sous le dossier package/rtc pour plus de détails.

```c
/*解析参数，获取当前年月日、时分秒*/
if(argc !=3) {
    fprintf(stdout, "useage:\t ./rtc year-month-day hour:minute:second\n");
    fprintf(stdout, "example: ./rtc 2021-10-11 19:54:30\n");
    return -1;
}

sscanf(argv[1], "%d-%d-%d",  &year, &month, &day);
sscanf(argv[2], "%d:%d:%d",  &hour, &minute, &second);

/*打开RTC设备，设备节点是：/dev/rtc0 */
fd = open("/dev/rtc0", O_RDONLY);
if (fd == -1) {
    perror("/dev/rtc0");
    exit(errno);
}

/* 设置RTC时间。*/
retval = ioctl(fd, RTC_SET_TIME, &rtc_tm);
if (retval == -1) {
    perror("ioctl");
    exit(errno);
}

/* 休眠 2秒。 */
sleep(2);

/* 读取RTC当前时间。*/
retval = ioctl(fd, RTC_RD_TIME, &rtc_tm);
if (retval == -1) {
    perror("ioctl");
    exit(errno);
}

/* 打印 RTC当前时间。*/
fprintf(stdout, "\nRTC date/time: %d/%d/%d %02d:%02d:%02d\n",
        rtc_tm.tm_mday, rtc_tm.tm_mon + 1, rtc_tm.tm_year + 1900,
        rtc_tm.tm_hour, rtc_tm.tm_min, rtc_tm.tm_sec);
```

## 1.6 Démo WDT

Le K510 dispose d'un total de trois chiens de garde et le pilote WDT enregistre les nœuds de périphérique generate /dev/watchdog0, /dev/watchdog1, /dev/watchdog2.

La couche d'application suit la méthode de programmation WDT standard dans le pilote d'appel système Linux, le premier paramètre de l'application wathdog peut être 0, 1, représenter watchdog0, watchdog1, respectivement, le deuxième paramètre représente le délai d'expiration (unité secondes) qui peut être défini, par exemple, la commande suivante indique le début de watchdog0, watchdog0 temps de débordement de 40 secondes.

```shell
cd /app/watchdog
./watchdog 0 40
```

Une fois le programme démarré, il alimentera le chien de garde toutes les 1 seconde à intervalles réguliers, lorsque le caractère d'arrêt est entré dans le terminal shell, que l'application cesse de nourrir le chien et que le chien de garde réinitialisera le redémarrage de l'appareil après le dépassement du délai d'expiration des paramètres, veuillez vous référer au code sous le dossier package / watchdog pour plus de détails.

Le résultat de l'exécution du programme est:

![](../zh/images/sdk_application/image-watchdog.png)

**Remarque**: Le module de surveillance k510 actuel a une fréquence d'horloge de travail de 757575 Hz, et le temps d'expiration en secondes doit être converti en délai d'expiration de la fréquence d'horloge de travail réelle du chien de garde, qui est calculée comme 2^ n / 757575, de sorte que le délai d'expiration réel sera supérieur ou égal au délai d'expiration d'entrée. 

Le délai d'expiration réel est calculé comme suit :

1) Entrez 40, 2^25/757575=44 > 40, 2^24/757575=22 < 40, il est donc réglé sur 44 secondes;

2) Entrez 155, 2^27/757575= 177 > 155, il est donc réglé sur 177 secondes;

3) Entrez 2000, 2^31/757575=2834 > 2000, il est donc réglé sur 2834 secondes;

## 1.7 Démo UART

K510 a un total de 4 ports série, le pilote actuel dans les ports série 2, 3 n'est pas activé, le pilote du port série 0 s'enregistrera pour générer des nœuds de périphérique /dev/ttyS0.

La couche d'application suit la méthode de programmation UART standard dans le pilote d'appel système Linux. Le premier paramètre de l'application uart peut être 0 et 1, qui représentent respectivement uart0 et uart1.

La carte de développement utilise un réseau câblé pour se connecter au routeur, de sorte que la carte de développement et le PC de débogage dans un réseau, lorsque la carte de développement est sous tension, il obtiendra automatiquement l'IP, entrera la commande ifconfig dans le terminal série shell de la carte de développement pour obtenir l'adresse IP, et le PC de débogage utilise cette IP pour ouvrir une fenêtre telent en connectant la carte de développement via la connexion telent. Par exemple, l'opération de débogage d'un PC pour connecter une carte de développement à l'aide de telent via MobaXterm est illustrée dans la figure suivante.

![](../zh/images/sdk_application/image-uart-mobaxterm.png)

Entrez la commande suivante dans la fenêtre du terminal telent pour démarrer le travail du port série 0.

```shell
cd /app/uart
./uart 0
```

Entrez le contenu que vous souhaitez envoyer dans la fenêtre telent, vous pouvez voir les données reçues dans la fenêtre du terminal série shell, veuillez vous référer au code sous le dossier package/crb_demo/uart pour plus de détails.
Par exemple, l'entrée de la fenêtre telent :

![](../zh/images/sdk_application/image-uart-telent.png)

La fenêtre correspondante du terminal série Shell affiche :

![](../zh/images/sdk_application/image-uart-shell.png)

## 1.8 Démo de l'ETH

La couche d'application suit le pilote d'appel de méthode de programmation ETH standard dans les systèmes Linux.

### 1.8.1 Client

Le périphérique en tant que client, entrez le répertoire /app/client, entrez la commande suivante pour démarrer l'application cliente, le premier paramètre de l'application ETH indique l'adresse IP du serveur pour établir la liaison TCP, par exemple, entrez la commande suivante pour démarrer le programme ETH et le serveur 10.20.1.13 pour établir la communication.

```shell
cd /app/client
./client 10.20.1.13
```

Connectez le serveur pour communiquer via le protocole tcp, exécutez le programme serveur sur une autre machine ubuntu, veuillez vous référer au dossier package / app / client pour plus de détails.

Afficher les journaux du côté de l'appareil :

![](../zh/images/sdk_application/image-client.png)

### 1.8.2 Serveur

L'appareil entre dans le répertoire /app/server en tant que serveur, par exemple, entrez la commande suivante pour démarrer le programme serveur.

```shell
cd /app/server
./server
```

Exécutez le programme client sur une autre machine ubuntu, connectez le serveur via le protocole tcp pour communiquer, pour plus de détails, veuillez vous référer au dossier package / crb_demo / serveur.

Afficher les journaux du côté de l'appareil :

 ![](../zh/images/sdk_application/image-server.png)

## 1.9 Démo SDMMC

Le K510 dispose d'un total de 3 contrôleurs principaux SDMMC, la carte de développement SDMMC0 est utilisée pour connecter eMMC, SDMMC1 est utilisé pour les modules WIFI et le contrôleur SDMMC2 est utilisé pour connecter des cartes SD.

Le pilote SDMMC s'enregistre pour générer /dev/mmcblk0 et le pilote EMMC s'enregistre en tant que nœud de périphérique /dev/mmcblk1.

La carte SD sera automatiquement montée sur /root/data après le démarrage du système, entrez dans le répertoire /app/write_read_file, le premier paramètre de l'application SDMMC indique le fichier à lire et à écrire, tel que la carte SD montée sur /root/data, vous pouvez lire et écrire des fichiers sous le répertoire /root/data/, d'abord écrire puis lire, Entrez la commande suivante pour démarrer l'application SDMMC pour lire et écrire sur la carte SD et calculer la vitesse de lecture et d'écriture (unité m/s).

```shell
cd /app/write_read_file
./write_read_file /root/data/test.txt
```

Pour activer la lecture et l'écriture des données 1G sur la carte SD, veuillez vous référer au dossier / application / write_read_file dossier.

![](../zh/images/sdk_application/image-sdmmc.png)

## 1.10 Démo SHA/AES

La démo SHA/AES utilise le noyau Linux pour exporter AF_ALG type d'interface Netlink et utilise l'API de chiffrement du noyau dans l'espace utilisateur. Reportez-vous à la section .<https://www.kernel.org/doc/html/latest/crypto/userspace-if.html> 

Paramètre:
-h Imprime les informations d'aide
Type d'algorithme -t : hash, skcipher
-n Noms d'algorithmes : sha256, ecb(aes), cbc(aes)
Opération de décryptage -x
-k AES KEY (chaîne hexadécimale)
-v AES IV (chaîne hexadécimale)

![](../zh/images/sdk_application/image_crypto_help.png)

Test sha256 :

```shell
cd /app/crypto
echo -n "This is a test file, hello world" > plain.txt
./crypto -t hash -n "sha256" plain.txt sha256.txt
xxd -p -c 32 sha256.txt
sha256sum plain.txt
```

![](../zh/images/sdk_application/image_crypto_sha256.png)

Ecb(aes) 128 test:

```shell
cd /app/crypto
echo -n "This is a test file, hello world" > plain.txt
./crypto -t skcipher -n "ecb(aes)" -k 00112233445566778899aabbccddeeff plain.txt ecb_aes_en.bin
./crypto -t skcipher -n "ecb(aes)" -k 00112233445566778899aabbccddeeff  -x ecb_aes_en.bin ecb_aes_de.bin
cmp ecb_aes_de.bin plain.txt
cat ecb_aes_de.bin
```

![](../zh/images/sdk_application/image_crypto_ecb.png)

cbc(aes) 128 test

```shell
cd /app/crypto
echo -n "This is a test file, hello world" > plain.txt
./crypto -t skcipher -n "cbc(aes)" -k 00112233445566778899aabbccddeeff -v 00112233445566778899aabbccddeeff plain.txt cbc_aes_en.bin
./crypto -t skcipher -n "cbc(aes)" -k 00112233445566778899aabbccddeeff -v 00112233445566778899aabbccddeeff -x cbc_aes_en.bin cbc_aes_de.bin
cmp cbc_aes_de.bin plain.txt
cat cbc_aes_de.bin
```

![](../zh/images/sdk_application/image_crypto_cbc.png)

Le cryptage AES-ECB-128 et aes-cbc-128 nécessite un alignement de 16 octets du texte brut, et l'insuffisant sera automatiquement rempli de 0.

## 1.11 Démo TRNG

La démo TRNG produit un nombre aléatoire de la longueur spécifiée en lisant le périphérique de caractères /dev/hwrng, sorti sous forme de chaîne hexadécimale.

La signification du paramètre d'entrée de ./trng :

-h Imprime les informations d'aide

-b Spécifie la longueur du nombre aléatoire de sortie, en octets

![](../zh/images/sdk_application/image_trng.png)

## 1.12 Démo DRM

La démo Drm démontre les capacités multicouches du matériel vo.

Vo a un total de 8 couches:

1) Calque d'arrière-plan, peut être configuré couleur d'arrière-plan.

2) Layer0 est une couche vidéo, prend en charge YUV422 et YUV420, prend en charge les formats NV12 et NV21, peut être mis en correspondance du côté de la taille et prend en charge la mise à l'échelle et la réduction du matériel.

3) Layer1-layer3 est une couche vidéo, prenant en charge YUV422 et YUV420, prenant en charge les formats NV12 et NV21, et le côté taille peut être assorti.

4) Layer4-layer6 est la couche OSD qui prend en charge plusieurs formats ARGB.

Une fois le tableau démarré, entrez le répertoire /app/drm_demo et entrez la commande :

```shell
cd /app/drm_demo
./drm_demo
```

Lancez drm_demo application, drm_demo affiché :

![](../zh/images/sdk_application/image_drm_demo.png)

## 1.13 démo V4L2_DRM

v4l2_drm démo démontre la fonctionnalité de l'entrée et de l'affichage de la caméra.

Une fois le tableau démarré, entrez le répertoire /app/mediactl_lib et entrez la commande :

```shell
cd /app/mediactl_lib
./v4l2_drm.out -f video_drm_1080x1920.conf -e 1
或者
./v4l2_drm.out -f video_drm_1920x1080.conf
```

Lancez l'application v4l2_drm.out et v4l2_drm.out :

![](../zh/images/sdk_application/image_v4l2_drm_demo.png)

## 1.14 Démo LVGL

Accédez à /app/lvgl et exécutez la commande suivante :

```shell
cd /app/lvgl
./lvgl
```

L'effet d'affichage est le suivant :![](../zh/images/sdk_application/image_lvgl.png)

## 1.15 Démo PWM

Le pilote PWM enregistre les nœuds de périphériques generate /sys/class/pwm/pwmchip0 et /sys/class/pwm/pwmchip3.

Cet exemple peut être configuré et activé pour pwm0 et pwm1 respectivement, dans le répertoire /app/pwm, le premier paramètre de l'application pwm indique la période de réglage de pwm, l'unité est ns, le deuxième paramètre définit l'heure de « ON » dans un cycle de pwm, l'unité est ns, le troisième paramètre peut être 0, 1, représentant pwm0 et pwm1, par exemple, entrez la commande suivante pour activer pwm0, le cycle est 1s, le cycle d'utilisation est 100000000/ 500000000 *100% = 50%, veuillez vous référer au dossier / application / pwm pour les codes détaillés.

```shell
cd /app/pwm
./pwm 1000000000 500000000 0
```

Le résultat de l'exécution du programme est:

![](../zh/images/sdk_application/image-pwm.png)

En connectant la broche 28 de la carte de développement K510 CRB1.2 J15 à travers l'oscilloscope, un motif de forme d'onde d'une période de 1 seconde et d'un rapport cyclique de 50% peut être observé sur l'oscilloscope.

## 1.16 Démo WIFI

Une fois le pilote du module WiFi chargé, la carte réseau sans fil wlan0 est générée, qui suit le pilote de port réseau standard et fait normalement référence à la programmation de socket TCP / IP.

1) Ouvrez « Mobile Hotspot » dans le bloc-notes, puis définissez le nom et le mot de passe du hotspot
2) Démarrez NetAssist sur le bloc-notes, configurez le type de protocole, l'adresse IP de l'hôte local, le port de l'hôte local, les paramètres de réception, les paramètres d'envoi et les données à envoyer, comme illustré dans la figure suivante :

![](../zh/images/sdk_application/image_wifi_1.png)

3) Le format de paramètre du programme de test wifi est:

```shell
./wifi <AP name> <password> <local ip> <server ip>
```

Par exemple, entrez le répertoire /app/wifi, entrez la commande pour démarrer le programme de test wifi et le résultat d'exécution du programme est le suivant :

![](../zh/images/sdk_application/image_wifi_2.png)

## 1.17 GPIO_KEYS démo

Le pilote de clé utilise le noyau Linux lui-même intégré au pilote générique de clés GPU basé sur le sous-système d'entrée, et une fois le pilote chargé, le nœud de surveillance des événements eventX est généré dans le répertoire /dev/input et X est le numéro de séquence du nœud d'événement, qui peut être affiché via cat /proc/bus/input/devices

gpio-keys routine bloquant la lecture des événements de rapport clé et l'impression des informations d'événement, ses informations comprennent l'encodage de clé et l'action de clé, le code de clé pour identifier l'identité de clé, l'action clé est divisée en pressé et relâché, dans la libération de clé lorsque la routine calculera la durée de la pression sur la touche

Le résultat de l'exécution du programme est illustré dans la figure suivante :![](../zh/images/sdk_application/image-gpio-keys.png)

**Clause de non-responsabilité en matière de**  
Pour la commodité des clients, Canaan utilise un traducteur IA pour traduire du texte en plusieurs langues, ce qui peut contenir des erreurs. Nous ne garantissons pas l'exactitude, la fiabilité ou l'actualité des traductions fournies. Canaan ne sera pas responsable de toute perte ou dommage causé par la confiance accordée à l'exactitude ou à la fiabilité des informations traduites. S'il existe une différence de contenu entre les traductions dans différentes langues, la version simplifiée en chinois prévaudra. 

Si vous souhaitez signaler une erreur de traduction ou une inexactitude, n'hésitez pas à nous contacter par courrier.