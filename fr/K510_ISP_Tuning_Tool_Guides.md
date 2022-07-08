![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">Guides de l'outil de réglage du fournisseur de services Internet K510</font>**

<font face="黑体"  size=3>Version du document : V1.0.0</font>

<font face="黑体"  size=3>Date de publication : 2022-03-31</font>

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
Ce document est une documentation de l'outil de réglage isp. 

**<font face="黑体"  size=5>Objets de lecture</font>**

Le public principal de ce document est constitué d'ingénieurs logiciels expérimentés, d'ingénieurs en algorithmes d'images, de concepteurs de systèmes et d'intégrateurs de systèmes qui souhaitent mettre en œuvre des applications et des pilotes propriétaires.

**<font face="黑体"  size=5>Historique des révisions</font>**
 <font face="宋体"  size=2>L'historique des révisions accumule une description de chaque mise à jour de document. La dernière version du document contient des mises à jour pour toutes les versions précédentes. </font>

| Le numéro de version   | Modifié par     | Date de révision | Notes de révision |
|  :-----  |-------   |  ------  |  ------  |
| Version 1.0.0 | Groupes de logiciels système | 2022-03-31 | Lancement du SDK V1.6 |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenu</font>**

[TOC]

<div style="page-break-after:always"></div>

# Introduction à l'infrastructure de l'outil de réglage isp

Cette section décrit les outils de réglage du FAI et les descriptions des flux de données fournis aux processeurs de niveau supérieur pour contrôler l'optimisation globale de l'image du FAI.

```text
+----------------------------------------------------+
|                                                    |
|                      K510                          |
|                                                    |
|    +-------+        +--------------------------+   |
|    |       |        |                          |   |
|    |  ISP  +------> |   v4l2_drm_isptool.out   |   |
|    |       |        |                          |   |
|    +-------+        +-------------+------------+   |
|                                   |                |
|                                   |                |
|    +-----------------+            |                |
|    |                 |            |                |
|    |   isp-tuningd   | <----------+                |
|    |                 |                             |
|    +^-+--------------+                             |
|     | |                                            |
|     | |                                            |
+----------------------------------------------------+
      | |
      | |
+-------------------------------+
|     | |                       |
|     | |       PC              |
|     | |                       |
|    ++-v------------------+    |
|    |                     |    |
|    |  ISP Tuning Tool    |    |
|    |                     |    |
|    +---------------------+    |
|                               |
+-------------------------------+
```

## Régler le trafic de l'outil

Le protocole de communication peut être trouvé dans la documentation dans le référentiel de code client, et l'outil se compose de deux parties, l'une est le client isp-tuningd s'exécutant sur le PC, le programme est situé dans le /app/mediactl_lib/isp-tuningd, et l'autre partie est le serveur s'exécutant sur le K510. Par défaut, le port TCP 9982 est utilisé pour la communication.

### client

L'outil de réglage ISP est une application qui s'exécute sur un PC. En plus de pouvoir définir des registres, l'étalonnage AWB et l'étalonnage CCM sont également pris en charge.

### Côté serveur

isp-tuningd reçoit une image yuv (NV12) en taille de 3133440 octets de l'entrée standard et la diffuse à tous les clients, nous pouvons utiliser v4l2_drm_isptool, il démarrera automatiquement isp-tuningd et enverra les données d'image, l'utilisation spécifique est cohérente avec le v4l2_drm. Nous pouvons l'exécuter avec la commande suivante

```shell
cd /app/mediactl_lib
./v4l2_drm_isptool -f video_drm_1080x1920.conf
```

# Options de réglage des FAI

De nombreux registres et tables sont fournis dans le FOURNISSEUR DE SERVICES INTERNET K510 pour le contrôle et le réglage. Le réglage des registres matériels des FAI est très important pour la qualité de l'image. À l'heure actuelle, sur la plate-forme K510, le processus de réglage d'image n'est implémenté que via TCP Socket.

## Fenêtre principale de l'outil de réglage

Cette section décrit les fonctionnalités de ces panneaux dans la fenêtre de réglage.

La figure 3-1 montre l'ensemble du panneau de l'opérateur sur la fenêtre de réglage

- Le panneau 1 est le** menu **qui peut éventuellement charger le fichier ISP configuré ou effectuer un étalonnage. 
- Le panneau 2 est le **panneau de configuration de la connexion**, remplissez l'adresse IP et le numéro de port de la carte de développement (port par défaut 9982) et cliquez sur le bouton vert de connexion pour vous connecter. 
- Le panneau 3 est le** panneau de registre**, si vous devez définir ou lire le registre n'est pas dans celui-ci, vous pouvez utiliser ce panneau pour définir et lire. 
- Le panneau 4 est un **panneau de sélection **de paramètres de réglage, l'utilisateur peut sélectionner divers paramètres ou groupes de paramètres en fonction du texte de l'invite du panneau, les registres de ces sélections seront affichés sur le panneau 5. 
- Le panneau 5 est le **panneau Paramètres de réglage**, qui permet de définir ou d'obtenir des valeurs de paramètre à partir du serveur de réglage. 
- Le panneau 6 est un panneau d**'affichage d'image**, qui affiche la sortie d'image par le FAI et peut cliquer sur le bouton de pause au milieu lorsqu'il n'est pas nécessaire de jouer tout le temps. 

![Figure 3-1 Fenêtre principale de l'outil de réglage](../zh/images/sdk_application/clip_image033.png)

L'outil de réglage ISP** n'**acquiert pas automatiquement toutes les valeurs de registre après la connexion, et si vous devez obtenir toutes les valeurs de registre, vous pouvez cliquer sur le** bouton Lire sur le côté droit du panneau de configuration** de connexion pour extraire toutes les valeurs de registre actuelles. 

# Étalonnage et étalonnage

Cette section décrit les instructions d'étalonnage et d'étalonnage à l'aide des outils de réglage ISP, notamment la balance des blancs automatique (AWB), la matrice de correction des couleurs (CCM), le gamma et les ombres d'objectif (LSC).

## AWB

### Préparatifs

1. Boîte à lumière standard avec source lumineuse D65 standard
2. Carte couleur standard 24, actuellement seule la carte couleur X-RITE est prise en charge
3. Une caméra prête pour l'étalonnage peut produire une image originale du capteur ou une image traitée
4. ISP n'ouvre également que le module de correction du niveau de noir et de l'algorithme de dé-mosaïque, CSC et autres modules de conversion de format doivent faire attention à la symétrie (matrice est une matrice inverse), en plus de la réduction du bruit, la netteté et d'autres modules ont peu d'impact, mais aussi essayer de fermer, les modules non linéaires et les modules de traitement des couleurs (GAMMA, large dynamique, AWB, CCM, réglage de la saturation, etc.) doivent être désactivés

### Obtient l'image

1. L'appareil photo est dirigé vers la carte 24 couleurs, assurez-vous que la carte 24 couleurs remplit toute l'image, puis saisissez l'image, sur laquelle vous pouvez cliquer pour suspendre la lecture sans garantir la précision, comme illustré dans la figure suivante

    ![Figure 4-1 24 cartes couleur sont prises](../zh/images/sdk_application/clip_image014.jpg)

2. L'image capturée doit faire attention à la luminosité et à l'obscurité modérées, et trop lumineuse et trop sombre affectera l'étalonnage

### délimiter

Cliquez sur « Calibration » dans la barre de menus, sélectionnez « AWB » pour effectuer l'étalonnage, et le programme sélectionnera automatiquement la carte de couleur

![Figure 4-2 Sélecteur de couleur de boîte automatique](../zh/images/sdk_application/clip_image016.jpg)

Appuyez sur n'importe quelle touche pour continuer, en faisant apparaître l'image une fois la balance des blancs terminée

![Figure 4-3 Étalonnage AWB complet](../zh/images/sdk_application/clip_image018.jpg)

S'il n'y a pas de problème, continuez à appuyer sur n'importe quelle touche, l'outil affichera une boîte de dialogue demandant si le paramètre est raisonnable, oui le remplira dans les registres liés à l'interface principale, sinon abandonnez le résultat de l'étalonnage, si c'est le cas, l'outil continuera à demander s'il faut écrire dans le registre du périphérique.

## CC

Conformément à l'étalonnage AWB, il ne sera pas répété.

## Gamma

La formule de la courbe gamma standard est
$$
Y=aX^b
$$
Où $b $ est le coefficient gamma, qui est généralement inférieur à 1 à l'extrémité de l'imagerie et supérieur à 1 à l'extrémité de l'affichage. La valeur de $a$ peut être calculée sur la base de la valeur de $b$

$$
a=\frac{256}{256^b}
$$
Le principe de la formule est que l'entrée est 256, ce qui est toujours 256 après correction Gamma.

Lorsque le coefficient gamma b est de 0,5, la courbe est représentée dans la figure suivante

![](../zh/images/sdk_application/clip_image025.png)

## LSC

### Préparatifs

- Une prise de vue capture une photo au format RAW

### principe

Étant donné que le centre de l'objectif est incompatible avec la transmission de la lumière environnante, la luminosité de l'image est inégale, de sorte que l'ajustement de la courbe génère une surface corrective pour compenser ce problème.

La correction est illustrée dans la figure ci-dessous

![Avant correction](../zh/images/sdk_application/clip_image029.png)

Après correction, il est illustré dans la figure suivante

![Après correction](../zh/images/sdk_application/clip_image031.png)

**Clause de non-responsabilité en matière de**  
Pour la commodité des clients, Canaan utilise un traducteur IA pour traduire du texte en plusieurs langues, ce qui peut contenir des erreurs. Nous ne garantissons pas l'exactitude, la fiabilité ou l'actualité des traductions fournies. Canaan ne sera pas responsable de toute perte ou dommage causé par la confiance accordée à l'exactitude ou à la fiabilité des informations traduites. S'il existe une différence de contenu entre les traductions dans différentes langues, la version simplifiée en chinois prévaudra. 

Si vous souhaitez signaler une erreur de traduction ou une inexactitude, n'hésitez pas à nous contacter par courrier.