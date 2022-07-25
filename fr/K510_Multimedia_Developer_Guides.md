![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 Guide du développeur multimédia</font>**

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
## Objet du document
Ce document est un document explicatif pour l'exemple d'application multimédia K510.
## Public cible
À qui s'adresse le présent document :
- Développeurs de logiciels
- Personnel de soutien technique

## Historique des révisions

| Le numéro de version    | Modifié par | Date de révision| Notes de révision  |  
|  ------  |-------| -------| ------ |
| v1.0.0    |Groupes de logiciels système | 2022-03-09 | Lancement du SDK V1.5 |
|     |     |      |   |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenu</font>**

[TOC]

# 1 API d'encodeur

## 1.1 Description du fichier d'en-tête

k510_buildroot/paquet/encode_app/enc_interface.h

## 1.2 Descriptions des fonctions de l'API

### 1.2.1 VideoEncoder_Create

【Description】

Créer un encodeur vidéo

【Grammaire】

```c
EncoderHandle* VIdeoEncoder_Create(EncSettings *pCfg)
```

【Paramètres】

pCfg : Entrez les paramètres de configuration de codage

|            Nom du paramètre             | Interprétation des paramètres                                                     |                           La plage de valeurs                           | Modules d'encodage applicables |
| :---------------------------: | :----------------------------------------------------------- | :----------------------------------------------------------: | ------------ |
|            canal            | Numéro de canal, prend en charge jusqu'à 8 canaux codés                                   |                            [0，7]                            | jpeg、avc    |
|             Largeur             | Encode la largeur de l'image                                                 | avc: [128,2048], multiple de 8 <br/> jpeg: jusqu'à 8192, multiple de 16 | jpeg、avc    |
|            hauteur             | Encoder la hauteur de l'image                                                 | avc: [64,2048], multiple de 8 <br/> jpeg: jusqu'à 8192, multiple de 2 | jpeg、avc    |
|           FrameRate           | Fréquence d'images, qui ne peut être configurée qu'à quelques valeurs fixes                                    |                       (25,30,50,60,75)                       | jpeg、avc    |
|            rcMode             | Le mode de contrôle du débit binaire 0:CONST_QP 1:CBR 2:VBR<br />jpeg est fixé à CONST_QP  |                       Voir RateCtrlMode                       | jpeg，avc    |
|            Débit binaire            | Débit binaire cible en mode CBR ou débit binaire le plus bas en mode VBR                    |                        [10,20000000]                         | avc          |
|          MaxBitRate           | Le débit binaire le plus élevé en mode VBR                                          |                        [10,20000000]                         | avc          |
|            SliceQP            | Valeur QP initiale, -1 pour auto                                        |                avc:-1,[0,51]<br/>jpeg:[1,100]                | jpeg，avc    |
|             MinQP             | La valeur qp minimale                                                     |                         [0,sliceqp]                          | avc          |
|             MaxQP             | La valeur qp maximale                                                     |                         [trancheqp,54]                         | avc          |
|            profil            | profile_idc paramètres dans SPS: 0: base 1: main 2: high 3: jpeg       |                            [0,3]                             | jpeg，avc    |
|             niveau             | level_idc paramètres dans PS                                       |                           [10,42]                            | avc          |
|          AspectRatio          | Échelle d'affichage                                                     |                     Voir AVC_AspectRatio                      | jpeg，avc    |
|            FreqIDR            | Intervalle entre deux trames idr                                              |                           [1,1000]                           | avc          |
|            gopLen             | Group Of Picture, l'intervalle entre deux images I                      |                           [1,1000]                           | avc          |
|          bEnableGDR           | S'il faut activer l'actualisation dans le cadre                                             |                         [vrai,faux]                         | avc          |
|            gdrMode            | Mode d'actualisation gdr: 0, actualisation verticale 1, rafraîchissement horizontal                        |                       Voir GDRCtrlMode                        | avc          |
|          bEnableLTR           | Si les cadres de référence à long terme sont activés                                           |                         [vrai,faux]                         | avc          |
|          roiCtrlMode          | Mode de contrôle roi: 0: Ne pas utiliser roi 1: qp relatif 2: qp absolu                 |                       Voir ROICtrlMode                        | avc          |
|       EncSliceSplitCfg        | déploiement fractionné en tranches                                               |                                                              | avc          |
|         bSplitEnable          | Si le fractionnement de tranche est activé                                           |                         [vrai,faux]                         | avc          |
|         u32SplitMode          | Mode de segmentation des tranches : 0 : Fractionné par bits. <br />1: Fractionner par lignes de macrobloc        |                            [0,1]                             | avc          |
|         u32SliceTaille          | u32SplitMode=0, indiquant le nombre d'octets par tranche<br /> u32SplitMode=1, représente le nombre<br /> de lignes de macrobloc par tranche| u32SplitMode=[100,65535]<br />0,u32SplitMode=1,[1, (hauteur de l'image +15)/16] | avc          |
|          entropyMode          | Codage entropie, 0: CABAC 1: CAVLC                                |                      Voir EncEntropyMode                      | avc          |
|          encDblkCfg           | Configuration du filtrage des blocs                                                 |                                                              | avc          |
| disable_deblocking_filter_idc | La valeur par défaut est 0, ce qui signifie Accord H.264                          |                            [0，2]                            | avc          |
|  slice_alpha_c0_offset_div2   | La valeur par défaut est 0, ce qui signifie Accord H.264                          |                           [-6，6]                            | avc          |
|    slice_beta_offset_div2     | La valeur par défaut est 0, ce qui signifie Accord H.264                          |                          [-6,   6]                           | avc          |

```c
typedef struct
{
    int                       channel;  //encode channel number
    unsigned short            width;
    unsigned short            height;
    unsigned char             FrameRate;
    RateCtrlMode              rcMode;
    unsigned int              BitRate;
    unsigned int              MaxBitRate;
    int                       SliceQP;  //auto: -1, or from 0 to 51
    int                       MinQP;//from 0 to SliceQP
    int                       MaxQP;//from SliceQP to 51
    AVC_Profile               profile;
    unsigned int              level;  //1 .. 51, 51 is 5.1
    AVC_AspectRatio           AspectRatio;
    int                       FreqIDR; //default value  : -1,IDR:number of frames between two IDR pictures;GDR:refresh period
    unsigned int              gopLen;  
    bool                      bEnableGDR;//gdr
    GDRCtrlMode               gdrMode;
    bool                      bEnableLTR;//Long Term reference

    ROICtrlMode               roiCtrlMode;
    EncSliceSplitCfg          sliceSplitCfg;
    EncEntropyMode            entropyMode;//Profile is set to AVC_MAIN or AVC_HIGH is valid
    EncDblkCfg                encDblkCfg;
}EncSettings;
typedef enum
{
    CONST_QP,
    CBR,
    VBR
} RateCtrlMode;
typedef enum
{
    AVC_C_BASELINE,
    AVC_MAIN,
    AVC_HIGH,
    JPEG
} AVC_Profile;
typedef enum
{
    ASPECT_RATIO_AUTO,
    ASPECT_RATIO_4_3,
    ASPECT_RATIO_16_9,
    ASPECT_RATIO_NONE
} AVC_AspectRatio;
typedef struct
{
    unsigned int          s32X;
    unsigned int          s32Y;
    unsigned int          u32Width;
    unsigned int          u32Height;
} RECT_S;
typedef struct
{
    unsigned int          uIndex;//index[0-7]
    bool                  bEnable;
    int                   uQpValue;
    RECT_S                stRect;
} EncROICfg;
typedef enum
{
    ROI_QP_TABLE_NONE,
    ROI_QP_TABLE_RELATIVE,//[-32,31],6 LSBs effective
    ROI_QP_TABLE_ABSOLUTE,//[0,51],6 LSBs effective
} ROICtrlMode;
typedef enum
{
    GDR_VERTICAL = 0,
    GDR_HORIZONTAL,
    GDR_CTRLMAX,
} GDRCtrlMode;
typedef struct
{
    bool bSplitEnable;
    unsigned int u32SplitMode; // 0:splite by byte; 1:splite by slice count
    unsigned int u32SliceSize;
}EncSliceSplitCfg;

typedef enum
{
    ENTROPY_MODE_CABAC = 0,
    ENTROPY_MODE_CAVLC,
}EncEntropyMode;

typedef struct
{
    unsigned int  disable_deblocking_filter_idc;//[0,2]
    int  slice_alpha_c0_offset_div2;//[-6,6]
    int  slice_beta_offset_div2;//[-6,6]
}EncDblkCfg;
```

【Valeur de retour】

```c
typedef void* EncoderHandle
```

### 1.2.2 VideoEncoder_SetRoiCfg

【Description】

réglage roi, support jusqu'à 8 zones rectangulaires, le système selon le numéro d'index de 0 ~ 7 pour gérer la zone ROI, uIndex indique que l'utilisateur définit le numéro d'index du ROI. Les régions roi peuvent être superposées les unes aux autres, et lorsqu'une superposition se produit, la priorité entre les régions ROI augmente séquentiellement de l'indice 0 à 7.

Il peut être utilisé après la création de l'encodeur et avant sa destruction. La région de retour sur investissement peut être ajustée dynamiquement pendant le processus d'encodage.

【Grammaire】

```c
EncStatus VideoEncoder_SetRoiCfg(EncoderHandle *hEnc,const EncROICfg*pEncRoiCfg);
```

【Paramètres】

hEnc : le handle renvoyé au moment de la création

pEncRoiCfg : informations de configuration de la zone roi

```c
typedef struct
{
    unsigned int          s32X;
    unsigned int          s32Y;
    unsigned int          u32Width;
    unsigned int          u32Height;
}RECT_S;

typedef struct 
{
    unsigned int          uIndex;//index[0-7]
    bool                  bEnable;
    int                   uQpValue;
    RECT_S                stRect;
}EncROICfg;
```

Description des paramètres

```text
uIndex     - 指定该roi区域索引号，范围0-7最多支持8个区域
bEnable    - 指定该区域是否使能，只有使能的区域才有效
uQpValue   - qp值，可以是相对qp或绝对qp，qp模式由EncSettings中roiCtrlMode属性决定。绝对qp范围                  [0,51]，相对qp范围[-31,31]
stRect     - roi矩形区域，s32X矩形左上角x值，s32Y矩形左上角y值，u32Width矩形宽度，u32Height矩形高度
```

【Valeur de retour】

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.3 VideoEncoder_SetLongTerm

【Description】

Définit l'image suivante du codage sur un cadre de référence à long terme. Il peut être utilisé après la création de l'encodeur et avant sa destruction. L'attribut bEnableLTR dans EncSettings détermine si la fonctionnalité est activée.

【Grammaire】

```c
EncStatus VideoEncoder_SetLongTerm(EncoderHandle *hEnc);
```

【Paramètres】

hEnc : le handle renvoyé au moment de la création

【Valeur de retour】

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.4 VideoEncoder_UseLongTerm

【Description】

Définit le codage sur l'image suivante à l'aide d'un cadre de référence à long terme. Il peut être utilisé après la création de l'encodeur et avant sa destruction. L'attribut bEnableLTR dans EncSettings détermine si la fonctionnalité est activée.

【Grammaire】

```c
EncStatus VideoEncoder_UseLongTerm(EncoderHandle *hEnc);
```

【Paramètres】

hEnc : le handle renvoyé au moment de la création

【Valeur de retour】

```c
typedef enum
{
    Enc_SUCCESS = 0,
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.5 VideoEncoder_InsertUserData

【Description】

Insérez des données utilisateur.

Il peut être utilisé après la création de l'encodeur et avant sa destruction, et le contenu des données utilisateur peut être modifié en temps réel pendant le processus d'encodage. Les données utilisateur seront insérées dans la zone de données SEI du cadre IDR.

【Grammaire】

```c
EncStatus      VideoEncoder_InsertUserData(EncoderHandle *hEnc,char*pUserData,unsigned int nlen);
```

【Paramètres】

hEnc : le handle renvoyé au moment de la création

pUserData : pointeur vers les données utilisateur

nlen: Longueur des données utilisateur (0, 1024)

【Valeur de retour】

```c
typedef enum
{
    Enc_SUCCESS = 0,
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.6 VideoEncoder_Destory

【Description】

Détruire l'encodeur vidéo

【Grammaire】

```c
EncStatus VideoEncoder_Destroy(EncoderHandle *hEnc)
```

【Paramètres】

hEnc : le handle renvoyé au moment de la création

【Valeur de retour】

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.7 VideoEncoder_EncodeOneFrame

【Description】

Encoder une image vidéo

【Grammaire】

```c
EncStatus VideoEncoder_EncodeOneFrame(EncoderHandle *hEnc, EncInputFrame *input)
```

【Paramètres】

hEnc : le handle renvoyé au moment de la création

entrée: Entrez les données vidéo YUV

```c
typedef struct
{
    unsigned short width;
    unsigned short height;
    unsigned short stride;
    unsigned char *data;
}EncInputFrame;
```

【Valeur de retour】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.2.8 VideoEncoder_GetStream

【Description】

Obtient la mémoire tampon du flux de codage vidéo, Remarque : Cet espace tampon est alloué en interne par l'encodeur.

【Grammaire】

```c
EncStatus VideoEncoder_GetStream(EncoderHandle *hEnc, EncOutputStream *output)
```

【Paramètres】

hEnc : le handle renvoyé au moment de la création

sortie: Sortie du tampon de données de flux codé, bufSize est supérieur à 0 pour avoir la sortie

```c
typedef struct
{
    unsigned char *bufAddr;
    unsigned int bufSize; 
}EncOutputStream;
```

【Valeur de retour】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.2.9 VideoEncoder_GetStream_ByExtBuf

【Description】

Obtient la mémoire tampon du flux de codage vidéo, Remarque : L'espace tampon doit être alloué par le consommateur avant d'appeler cette fonction.

【Grammaire】

```c
EncStatus VideoEncoder_GetStream(EncoderHandle *hEnc, EncOutputStream *output)
```

【Paramètres】

hEnc : le handle renvoyé au moment de la création

sortie: Sortie du tampon de données de flux codé, bufSize est supérieur à 0 pour avoir la sortie

```c
typedef struct
{
    unsigned char *bufAddr;
    unsigned int bufSize; 
}EncOutputStream;
```

【Valeur de retour】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.3.0 VideoEncoder_ReleaseStream

【Description】

Libérez la mémoire tampon du flux d'encodage vidéo

【Grammaire】

```c
EncStatus VideoEncoder_ReleaseStream(EncoderHandle *hEnc, EncOutputStream *output)
```

【Paramètres】

- hEnc : le handle renvoyé au moment de la création
- sortie:VideoEncoder_GetStream le tampon renvoyé

【Valeur de retour】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

# 2 Diagramme de structure matérielle et architecture logicielle

# 2.1 Diagramme de structure matérielle

Le schéma fonctionnel matériel du K510 est le suivant :
![hardware_block_diagram](../zh/images/multimedia_guides/hardware_block_diagram.png)

Les données reçues du capteur vidéo sont traitées par MIPI DPHY, CSI, VI, isP pour obtenir les données source yuv et stockées dans le DDR. Le module d'encodeur h264 lit les données du DDR, effectue des opérations de codage et stocke les résultats des opérations dans le DDR.

# 2.2 Architecture logicielle

L'architecture logicielle de la plateforme de développement multimédia est la suivante :

![multimedia_block_diagram.png](../zh/images/multimedia_guides/multimedia_block_diagram.png)

il s'y trouve

- `libvenc`: Bibliothèque d'encodeur pour appeler le noyau de l'encodeur h264
- `libmediactl`: Bibliothèque Isp pour le contrôle des capteurs
- `libaudio3a`: Bibliothèque Audio3a pour les opérations 3a sur audio
- `alsa-lib`: Bibliothèque audio pour le contrôle de l'interface audio

# 3 Application de démonstration

## 3.1 Encoder l'application

Le programme est placé`/app/encode_app` dans le répertoire:

- `encode_app`: Programme d'application d'encodage
- Le fichier yuv utilisé pour les tests est de grande taille et ne rentre pas dans le package SDK

Courir`encode_app`

| Nom du paramètre | Interprétation des paramètres | Valeur par défaut | La plage de valeurs | Modules d'encodage applicables |
|:-|:-|:-|:-|:-|
| Aide | Informations d'aide| | ||
| fendre | Le nombre de canaux | ZÉRO | [1,4] | jpeg、avc |
| Ch | Numéro de canal (basé sur 0) | ZÉRO | [0,3] | jpeg、avc |
| Je | Entrez le fichier YUV, seul le **format nv12 est pris en charge**  | ZÉRO | v4l2 <br> xxx.yuv | jpeg、avc |
| Dev | Nom du périphérique v4l2 | ZÉRO | **sensor0:** /dev/video3 /dev/video4 <br> <br>sensor1:<br> **/dev/video7 /** dev/ <br> video8 <br> | avc |
| ou | sortie| ZÉRO | rtsp <br> xxx.264 <br> xxx.MJPEG <br> xxx.JPEG | jpeg、avc |
| dans | Largeur de l'image de sortie | 1920 | avc: [128,2048], multiple de 8 <br> jpeg: jusqu'à 8192, multiple de 16 | jpeg、avc |
| h | Hauteur de l'image de sortie | 1080 | avc: [64,2048], multiple de 8 <br> jpeg: jusqu'à 8192, multiple de 2 | jpeg、avc |
| fps | La caméra capture les fréquences d'images, qui ne prennent actuellement en charge que 30pfs | 30 | 30 | avc |
| r | Fréquence d'images de sortie codée | 30 | Le nombre qui peut être divisible ou divisible par fps | avc |
| cadres | Entrez le nombre d'images yuv | 0 | [0,50] | jpeg、avc |
| cadres externes | La sortie des trames yuv, si elle est plus grande que le paramètre -inframes, sera un codage répété | 0 | [0,32767] | jpeg、avc |
| Gop | Group Of Picture, l'intervalle entre deux images I | 25 | [1,1000] | avc |
| rcmode | Représente le mode de contrôle du débit binaire 0:CONST_QP 1:CBR 2:VBR | CBR | [0,2] | avc |
| débit binaire | Débit binaire cible en mode CBR ou débit binaire le plus bas en mode VBR, en Ko | 4000 | [1,20000] | avc |
| maxbitrate | Le débit binaire le plus élevé en mode VBR, en Ko | 4000 | [1,20000] | avc |
| profil | profile_idc paramètres dans SPS: 0: base 1: main 2: high 3: jpeg | AVC_HIGH | [0,3] | jpeg、avc |
| niveau | level_idc paramètres dans SPS | 42 | [10,42] | avc |
| sliceqp | Valeur QP initiale, -1 pour auto | 25 | avc:-1,[0,51]<br/>jpeg:[1,100] | jpeg、avc |
| minqp | La valeur QP minimale | 0 | [0,sliceqp] | avc |
| maxqp | La valeur QP maximale | 54 | [trancheqp,54] | avc |
| activerLTR | Active les trames de référence à long terme et les paramètres spécifient la période d'actualisation. 0 : Le cycle d'actualisation n'est pas activé. Positif : définit périodiquement le cadre de référence et l'image suivante est définie pour utiliser le cadre de référence long | 0 | [0,65535] | avc |
| roi | Fichier de configuration roi, qui spécifie plusieurs régions roi | ZÉRO | xxx.conf | avc |
| Æ | Activer AE | 0 | 0 - N'active pas AE<br>1 - Activer AE | |
| Conf | Le fichier de configuration vl42 modifie les paramètres de configuration v4l2 en fonction du fichier de configuration spécifié et des paramètres d'entrée de ligne de commande | ZÉRO | xxx.conf | avc |

### 3.1.1 Entrez le fichier yuv et sortez le fichier

```shell
./encode_app -split 1 -ch 0 -i your_file.yuv -o out.264 -w 1920 -h 1080 -inframes 10 -outframes 30
./encode_app -split 1 -ch 0 -i your_file.yuv -o out.mjpeg -w 1920 -h 1080 -inframes 10 -outframes 30
```

### 3.1.2 Entrée v4l2, sortie rtsp push stream

#### 3.1.2.1 Canal unique

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

Exemple de commande ffplay pull :

```shell
 ffplay -rtsp_transport tcp rtsp://192.168.137.11:8554/testStream
```

- `rtsp://192.168.137.11:8554/testStream`Pour l'adresse URL du flux rtsp, -rtsp_transport tcp signifie utiliser tcp pour transmettre des données audio et vidéo (udp est utilisé par défaut), et l'option -fflags nobuffer peut être ajoutée pour éviter une latence accrue due à la mise en cache du lecteur.

#### 3.1.2.2 Double canal à caméra unique

```shell
./encode_app -split 2 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -ch 1 -i v4l2 -dev /dev/video4 -o rtsp -w 1280 -h 720 -conf video_sample.conf
```

La commande ffplay pull stream est la même que ci-dessus.

#### 3.1.2.3 Caméras doubles

```shell
./encode_app -split 2 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -ch 1 -i v4l2 -dev /dev/video7 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

La commande ffplay pull stream est la même que ci-dessus.

#### 3.1.2.4 Test de retour sur investissement

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -sliceqp -1 -bitrate 2048 -roi roi_1920x1080.conf -conf video_sample.conf
```

Format de fichier roi

```json
{
  "roiCtrMode": 1,
  "roiRegion": [
    {
      "qpValue": -15,
      "qpRegion": {
        "left": 0,
        "top": 0,
        "width": 500,
        "heigth": 500
      }
    }
  ]
}
```

Description du paramètre :

```text
roiCtrMode - 1:相对qp  2:绝对qp
roiRegion  - roi区域，为多个区域数组，最多支持8个区域。
qpValue    - 指定该区域使用的qp值，相对qp范围:[-31,31]     绝对qp范围:[0,51]
qpRegion   - roi矩形区域
left       - 矩形区域的左上角X坐标
top        - 矩形区域的左上角Y坐标
width      - 矩形区域的宽度
heigth     - 矩形区域的高度
```

La commande ffplay pull stream est la même que ci-dessus.

### 3.1.3 Transformation de la fréquence d'images

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -r 60 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

La commande ffplay pull stream est la même que ci-dessus.

### 3.1.4 Fréquences d'images d'entrée multiples

VGA@75fps et 720p60 sont actuellement pris en charge

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 640 -h 480 -fps 75 -r 75 -conf video_sample_vga480p75.conf
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1280 -h 720 -fps 60 -r 60 -conf video_sample_720p60.conf
```

La commande ffplay pull stream est la même que ci-dessus.

### 3.1.5 rtsp push flux audio et vidéo

```c
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -alsa 1 -ac 2 -ar 44100 -af 2 -ad hw:0 -conf video_sample.conf
```

La commande ffplay pull stream est la même que ci-dessus.

### 3.1.6 Précautions

- Environnement d'exploitation: Capteur de carte centrale: IMX219_SENSOR

- Format d'adresse de flux rtsp: adresse rtsp://ip: numéro de port / testStream, où l'adresse IP et le numéro de port sont variables et le reste est fixe.

  Tels que: rtsp://192.168.137.11:8554/testStream, où l'adresse IP est 192.168.137.11, le numéro de port est 8554.

  Adresse IP : l'adresse IP de la carte de développement, entrez ifconfig sur la carte à obtenir.

  Numéro de port : 8554 + <通道号>*2, les numéros de canal commencent généralement par 0 (-ch 0, -ch 1...).

- Lire le mode de flux RTSP: le flux RTSP correspondant peut être lu via vlc ou ffplay, et le flux de données peut être transmis via le protocole udp ou TCP.

  1) rtp over udp播放:ffplay -rtsp_transport udp rtsp://192.168.137.11:8554/testStream

  2) rtp sur tcp 播放: ffplay -rtsp_transport tcp rtsp://192.168.137.11:8554/testStream

  Il est recommandé d'utiliser rtp sur tcp pour jouer afin d'éviter l'écran causé par la perte de paquets udp.

## 3.2 ffmpeg

ffmpeg est placé dans le répertoire /usr/local/bin.

- `ffmpeg`: application ffmpeg.

Courir`ffmpeg`

(1) Paramètre de libk510_h264 de l'encodeur
| Nom du paramètre | Interprétation des paramètres | Valeur par défaut | La plage de valeurs |
|:-|:-|:-|:-|
| g | gop taille | 25 | 1 ~ 1000 |
| b | débit binaire | 4000000 | 0 ~ 20000000 |
| r | Fréquence d'images, puisque les FAI ne prennent actuellement en charge que 30fps, de sorte que le décodeur doit être réglé sur 30 | 30 | 30 |
| idr_freq | Fréquence IDR | -1 (pas de IDR) | -1 ~ 256 |
| Qp | Lors de l'encodage avec cqp, configurez la valeur qp | -1(auto) | -1 ~ 100 |
| maxrate | La valeur maximale du débit binaire | 0 | 20000000 |
| profil | Profils pris en charge | 2 (élevé) | 0 - ligne de base <br> 1 - principal <br> 2 - élevé |
| niveau | Niveau d'encodage | 42 | 10 ~ 42 |
| serait | Format d'écran | 0(auto) | 0 - auto <br> 1 - 4:3 <br> 2 - 16:9 <br> 3 - aucun |
| Ch | numéro de canal | 0 | 0-7 |
| framesToEncode | Le nombre d'images codées | -1 (toutes les images) | -1 ~ 16383 |

(2) Paramètres de libk510_jpeg de l'encodeur
| Nom du paramètre | Interprétation des paramètres | Valeur par défaut | La plage de valeurs |
|:-|:-|:-|:-|
| Qp | Lors de l'encodage avec cqp, configurez la valeur qp | 25 | -1 ~ 100 |
| r | fréquence d'images | 30 | 25 ~ 60 |
| Ch | canal d'encodage | 0 | 0 ~ 7 |
| maxrate | Débit binaire maximal. (0=ignorer) | 4000000 | 0 ~ 20000000 |
| serait | rapport d'aspect | 0(auto) | 0 - auto <br> 1 - 4:3 <br> 2 - 16:9 <br> 3 - aucun |

(3) Paramètre de libk510_video de l'appareil
| Nom du paramètre | Interprétation des paramètres | Valeur par défaut | La plage de valeurs |
|:-|:-|:-|:-|
| Wh | taille du cadre | ZÉRO | **pour encodeur libk510_h264:**:<br>  jusqu'à 2048x2048 <br> largeur multiple de 8 <br> hauteur multiple de 8 <br> min. largeur: 128 <br> min. hauteur: 64 <br> **pour encodeur libk510_jpeg:** <br> jusqu'à 8192x8192 <br> largeur multiple de 16 <br> hauteur multiple de 2 |
| Exp | paramètre d'exposition | 0 | 0 ~ 128 |
| Agc | gain analogique | 0 | 0 ~ 232 |

(4) paramètre audio3a
| Nom du paramètre | Interprétation des paramètres | Valeur par défaut | La plage de valeurs |
|:-|:-|:-|:-|
| sample_rate | Fréquence d'échantillonnage audio | 16000 | 1 ~ 65535 |
| Agc | Mode de gain audio | 3(AgcModeFixedDigital) | 0 - AgcModeUnchanged <br> 1 - AgcModeAdaptiveAnalog <br> 2 - AgcModeAdaptiveDigital <br> 3 - AgcModeFixedDigital |
| Ns | Niveau sonore | 3(Très élevé) | 0 - Faible <br> 1 - Modéré <br> 2 - Élevé <br> 3 - Très Élevé |
| dsp_task | Position de course Auido3a | 1(dsp) | 0 - cpu <br>1 - dsp |

Les paramètres configurables peuvent être visualisés via la commande d'aide

```shell
ffmpeg -h encoder=libk510_h264 #查看k510编码器的参数
ffmpeg -h demuxer=v4l2 #查看demuxer的配置参数
ffmpeg -h filter=audio3a #查看audio3a的配置参数
```

La boîte logique pour ffmpeg est la suivante :

![ffmpeg_block_diagram](../zh/images/multimedia_guides/ffmpeg_block_diagram.png)

audio3a est utilisé pour effectuer des opérations 3a sur l'audio reçu et le sortir, et son schéma logique est le suivant :

![ffmpeg_canaan_audio3a](../zh/images/multimedia_guides/ffmpeg_canaan_audio3a.png)

### 3.2.1 Instructions d'utilisation du programme

#### 3.2.1.1 push de flux rtp

##### 3.2.1.1.1. flux vidéo push rtp

Exemple de commande ffmpeg run :

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.102.231.29:1234
```

Lorsque 10.102.231.29 est l'adresse de réception, elle est modifiée en fonction de la situation réelle.
Appuyez sur « q » pendant que le programme est en cours d'exécution pour arrêter de fonctionner.

ffplay reçoit la commande :

```shell
ffplay.exe -protocol_whitelist "file,udp,rtp" -i test.sdp -fflags nobuffer -analyzeduration 1000000 -flags low_delay
```

Test.sdp est configuré comme suit.

```text
SDP:
v=0
o=- 0 0 IN IP4 127.0.0.1
s=No Name
c=IN IP4 10.102.231.29
t=0 0
a=tool:libavformat 58.76.100
m=video 1234 RTP/AVP 96
a=rtpmap:96 H264/90000
a=fmtp:96 packetization-mode=1
```

Description du paramètre .sdp :

- c=: Informations sur les liens avec les médias; IN: Type de réseau; IP4: Type d'adresse; Suivi de l'adresse IP (notez qu'il s'agit de l'adresse IP où se trouve le destinataire, et non de l'adresse IP de l'expéditeur)
- m= est le début d'une session au niveau du média, type video:media ; 1234 : Numéro de port; RTP/AVP : Protocole de transport; 96 : Format de charge utile dans l'en-tête rtp
Modifiez l'adresse IP et le numéro de port du récepteur en fonction de la situation réelle et notez que le numéro de port de rtp doit être pair.

##### 3.2.1.1.2. flux audio push rtp

Exemple de commande ffmpeg run :

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f rtp rtp://10.100.232.11:1234
```

Lorsque 10.100.232.11 est l'adresse de réception, elle est modifiée en fonction de la situation réelle.

- ac : définit le nombre de canaux audio
- ar : définit la fréquence d'échantillonnage audio

La commande ffplay receive est identique à la réception d'un flux vidéo et le fichier sdp fait référence à l'exemple suivant.

```text
SDP:
v=0
o=- 0 0 IN IP4 127.0.0.1
s=No Name
c=IN IP4 10.100.232.11
t=0 0
a=tool:libavformat 58.76.100
m=audio 1234 RTP/AVP 97
b=AS:128
a=rtpmap:97 MPEG4-GENERIC/32000/2
a=fmtp:97 profile-level-id=1;mode=AAC-hbr;sizelength=13;indexlength=3;indexdeltalength=3; config=129056E500
```

##### 3.2.1.1.3 flux audio et vidéo push rtp

Exemple de commande ffmpeg run :

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234 -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

La commande ffplay receive est identique à la réception d'un flux audio et le fichier sdp fait référence à l'exemple suivant.

```text
SDP:
v=0
o=- 0 0 IN IP4 127.0.0.1
s=No Name
t=0 0
a=tool:libavformat 58.76.100
m=video 1234 RTP/AVP 96
c=IN IP4 10.100.232.11
a=rtpmap:96 H264/90000
a=fmtp:96 packetization-mode=1
m=audio 1236 RTP/AVP 97
c=IN IP4 10.100.232.11
b=AS:128
a=rtpmap:97 MPEG4-GENERIC/32000/2
a=fmtp:97 profile-level-id=1;mode=AAC-hbr;sizelength=13;indexlength=3;indexdeltalength=3; config=129056E500
```

#### 3.2.1.2 flux push rtsp

Avant que rtsp ne pousse le flux, vous devez déployer le serveur rtsp pour envoyer le flux de données au serveur.

##### 3.2.1.2.1 flux vidéo push rtsp

Exemple de commande ffmpeg run :

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -acodec copy -f rtsp rtsp://10.100.232.11:5544/live/test110
```

- `idr_freq`Pour l'intervalle d'image IDR, un multiple entier du GOP est requis. Les flux RTSP doivent générer des trames IDR à extraire vers les flux.
- `rtsp://10.100.232.11:5544/live/test110`Adresse URL du flux push-pull du serveur RTSP

Exemple de commande ffplay pull :

```shell
ffplay.exe -protocol_whitelist "file,udp,rtp,tcp" -i rtsp://10.100.232.11:5544/live/test110
```

##### 3.2.1.2.2 rtsp push flux audio

Exemple de commande ffmpeg run :

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f rtsp rtsp://10.100.232.11:5544/live/test110
```

La commande ffplay pull stream est identique à la commande rtsp pull video stream.

##### 3.2.1.2.3 flux audio vidéo push rtsp

Exemple de commande ffmpeg run :

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -f alsa -ac 2 -ar 32000 -i hw:0 -idr_freq 25 -vcodec libk510_h264 -acodec aac -f rtsp rtsp://10.100.232.11:5544/live/test110
```

La commande ffplay pull stream est identique à la commande rtsp pull video stream.

#### 3.2.1.3 flux push rtmp

Avant la diffusion en continu rtmp, vous devez déployer le serveur rtmp pour envoyer le flux de données au serveur. Les serveurs qui prennent en charge le protocole RTMP incluent fms, nginx, srs, etc.

##### 3.2.1.3.1 rtmp pousse les flux vidéo

Exemple de commande ffmpeg run :

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`Adresse URL permettant de pousser le flux vers le serveur rtmp  

Exemple de commande ffplay pull :

```shell
ffplay -fflags nobuffer rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`Pour extraire l'adresse URL du flux du serveur rtmp (les flux push sont les mêmes que l'adresse du flux pull), l'option -fflags nobuffer pour éviter une latence accrue due à la mise en cache du lecteur.

##### 3.2.1.3.2 flux audio push rtmp

Exemple de commande ffmpeg run :

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`Adresse URL permettant de pousser le flux vers le serveur rtmp

La commande ffplay pull stream est identique à la commande rtmp pull video stream.

##### 3.2.1.3.3 flux audio et vidéo push rtmp

Exemple de commande ffmpeg run :

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -f alsa -ac 2 -ar 32000 -i hw:0 -idr_freq 25 -vcodec libk510_h264 -acodec aac -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`Adresse URL permettant de pousser le flux vers le serveur rtmp

La commande ffplay pull stream est identique à la commande rtmp pull video stream.

#### 3.2.1.4 audio3a

##### 3.2.1.4.1 Exécuter l'audio séparément

(1) Exécutez audio3a sur le processeur
Exemple de commande ffmpeg run :

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000:dsp_task=0 -f rtp rtp://10.100.232.11:1234
```

(2) Exécuter audio3a sur dsp
Exécutez deux fenêtres telnet, exécutez le planificateur de tâches dsp et ffmpeg dans les deux fenêtres (exécutez d'abord le planificateur de tâches dsp)
Le planificateur de tâches dsp exécute l'instance de commande :

```shell
cd /app/dsp_app_new/
./dsp_app /app/dsp_scheduler/scheduler.bin
```

Exemple de commande ffmpeg run :

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000 -f rtp rtp://10.100.232.11:1234
```

##### 3.2.1.4.2 Exécuter audio3a et vidéo en même temps

(1) Exécutez audio3a sur le processeur
Exécutez deux fenêtres telnet, exécutez audio3a et video dans les deux fenêtres.
Exemple de commande vidéo :

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234
```

Exemple de commande audio3a :

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000:dsp_task=0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

Exécuter audio3a et vidéo sur le processeur en même temps produira un débordement, il est recommandé d'exécuter audio3a sur dsp
(2) Exécuter audio3a sur dsp
Exécutez trois fenêtres telnet, exécutez des appels audio3a, de la vidéo et un planificateur dsp sur chacune des trois fenêtres
La commande d'exécution du planificateur de tâches dsp est identique à l'exécution d'audio3a seul.

Exemple de commande audio3a :

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000 -f rtp rtp://10.100.232.11:1236
```

Exemple de commande vidéo :

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234
```

- 10.100.232.11 est l'adresse IP du récepteur rtp.
- Le contenu du fichier SDP du terminal de réception ffplay peut être obtenu à partir du journal imprimé après avoir exécuté la commande ffmpeg ci-dessus.

#### 3.2.1.5 v4l2

Les paramètres configurables peuvent être visualisés via la commande d'aide

```shell
ffmpeg -h demuxer=v4l2 #查看v4l2的配置参数
```

| Nom du paramètre | Interprétation des paramètres | Valeur par défaut | La plage de valeurs |
| :-- | :-- | :-- | :-- |
| s | Résolution d'image, telle que 1920x1080 | ZÉRO | |
| r | Fréquence d'images, ne prend actuellement en charge que 30fps | 30 | 30 |
| FAI | Allumez le matériel du fournisseur de services Internet k510 | 0 | 0-1 |
| buf_type |Tampon  `类型` v4l2 <br>1 : V4L2_MEMORY_MMAP : pour -vcodec copie<br>2 : V4L2_MEMORY_USERPTR : pour -vcodec libk510_h264 | 1 | 1~2 |
| Conf | Fichier de configuration v4l2 | ZÉRO | |

Exemple de commande d'exécution ffmpeg : où 10.100.232.11 est l'adresse de réception, modifiée en fonction de la situation réelle.

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234 -f alsa -ac 2 -ar 16000 -i hw:0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -i /dev/video3 -vcodec copy -y out.yuv
```

Illustrer:

1. Le runtime doit être trouvé dans le répertoire d'exécution`video_sampe.conf`, `imx219_0.conf`et les `imx219_1.conf`fichiers sont configurés, et les trois fichiers sont sous`/encode_app/` le répertoire.
2. La vidéo fournie en temps réel par la caméra est écrite sous forme de fichier YUV, et comme le fichier YUV est très volumineux, la vitesse d'écriture DDR ou NFS locale ne peut pas suivre, ce qui peut entraîner une perte d'image.

#### 3.2.1.6 Codage JPEG

Sortie de fichier:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_jpeg -y test.mjpeg
```

Description : le runtime doit se trouver dans le répertoire d'exécution`video_sampe.conf`, `imx219_0.conf`les `imx219_1.conf`fichiers sont configurés et les trois fichiers se trouvent sous`/encode_app/` le répertoire.

Le fichier de sortie test.mjpeg peut être lu côté PC avec ffplay

```shell
ffplay -i test.mjpeg
```

Push Stream :

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_jpeg -an -f rtp rtp://10.100.232.11:1234
```

Les flux d'extraction Ffplay sont disponibles

#### 3.2.1.7 Codage de multiplexage

Prend en charge jusqu'à 8 encodage simultané, vous pouvez utiliser la taille d'image de chaque canal multipliée par la fréquence d'images puis ajoutée, ne pas dépasser la quantité de données de 1080p60, -vcodec peut choisir h264 ou jpeg.

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -filter_complex 'split=2[out1][out2]' -map '[out1]' -vcodec libk510_h264 -ch 0 -an -f rtp rtp://10.20.1.101:1234 -map '[out2]' -vcodec libk510_h264 -ch 1 -an -f rtp rtp://10.20.1.101:2236
```

```shell
ffmpeg -f v4l2 -s 480x360 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -filter_complex 'split=8[out1][out2][out3][out4][out5][out6][out7][out8]' -map '[out1]' -vcodec libk510_h264 -b:v 300000 -ch 0 -an -f rtp rtp://10.20.1.101:1234 -map '[out2]' -vcodec libk510_h264 -b:v 300000 -ch 1 -an -f rtp rtp://10.20.1.101:2322 -map '[out3]' -vcodec libk510_h264 -b:v 300000 -ch 2 -an -f rtp rtp://10.20.1.101:3086 -map '[out4]' -vcodec libk510_h264 -b:v 300000 -ch 3 -an -f rtp rtp://10.20.1.101:4234 -map '[out5]' -vcodec libk510_h264 -b:v 300000 -ch 4 -an -f rtp rtp://10.20.1.101:5216 -map '[out6]' -vcodec libk510_h264 -b:v 300000 -ch 5 -an -f rtp rtp://10.20.1.101:6788 -map '[out7]' -vcodec libk510_h264 -b:v 300000 -ch 6 -an -f rtp rtp://10.20.1.101:7230 -map '[out8]' -vcodec libk510_h264 -b:v 300000 -ch 7 -an -f rtp rtp://10.20.1.101:8976
```

Lorsque vous utilisez ffplay pour extraire des flux, veillez à ne tirer qu'une seule vidéo, à changer la vidéo d'autres routes en modifiant le numéro de port dans le fichier SDP ou à démarrer plusieurs flux ffplay.

### 3.2.2 Instructions de portage du programme

`ffmpeg``ffmpeg`Porté sur la version open source 4.4,`xxx.patch` ajouté pour le Service Pack

- `ff_libk510_h264_encoder`: Contrôle de l'encodage matériel h264, référencé`libvenc.so`
- `ff_libk510_jpeg_encoder`: Contrôle l'encodage matériel jpeg, référencé`libvenc.so`
- v4l2 : dans v4l2.c, le code matériel k510 a été ajouté et le type de tampon v4l2 V4L2_MEMORY_USERPTR et référencé`libmediactl.so`.

#### 3.2.2.1 Commande de génération de correctifs

（1）

```shell
quilt new -p ab xxx.patch #在patches目录下生成xxx.patch文件
quilt add <filename> #添加修改前的文件
### 修改代码 ###
quilt refresh #修改内容被添加到xxx.patch
```

（2）
Copiez xxx.patch dans le répertoire package/ffmpeg_canaan et modifiez le chemin d'accès au fichier patch en fonction du chemin d'accès actuel.

```shell
mv ../../patches/xxx.patch ../../package/ffmpeg_canaan
rm ../../patches/series
sed -i "s/\/dl\/ffmpeg_canaan\/ffmpeg-4.4//g" ../../package/ffmpeg_canaan/xxx.patch
```

#### 3.2.2.2 Configuration ffmpeg

Dans le `package/ffmpeg_canaan/ffmpeg.mk`fichier, le cœur du processeur peut être modifié, la chaîne d'outils de compilation et l'activation peut être effectuée via l'option configee`ff_k510_video_demuxer`.`ff_libk510_jpeg_encoder` `ff_libk510_h264_encoder`

```shell
./configure \
    --cross-prefix=riscv64-linux- \
    --enable-cross-compile \
    --target-os=linux \
    --cc=riscv64-linux-gcc \
    --arch=riscv64 \
    --extra-ldflags="-L./" \
    --extra-ldflags="-ldl" \
    --extra-ldflags="-Wl,-rpath ." \
    --enable-static \
    --enable-libk510_video \
    --enable-libk510_h264 \
    --enable-libk510_jpeg \
    --enable-alsa \
    --disable-autodetect \
    --disable-ffplay \
    --disable-ffprobe \
    --disable-doc \
    --enalbe-audio3a \
    --enable-indev=v4l2 \
```

**Clause de non-responsabilité en matière de**  
Pour la commodité des clients, Canaan utilise un traducteur IA pour traduire du texte en plusieurs langues, ce qui peut contenir des erreurs. Nous ne garantissons pas l'exactitude, la fiabilité ou l'actualité des traductions fournies. Canaan ne sera pas responsable de toute perte ou dommage causé par la confiance accordée à l'exactitude ou à la fiabilité des informations traduites. S'il existe une différence de contenu entre les traductions dans différentes langues, la version simplifiée en chinois prévaudra.

Si vous souhaitez signaler une erreur de traduction ou une inexactitude, n'hésitez pas à nous contacter par courrier.
