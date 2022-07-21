![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">Guide de développement de K510 Direct Rendering Manager</font>**

<font face="黑体"  size=3>Version du document : P0.1.0</font>

<font face="黑体"  size=3>Date de publication : 2022-01-01</font>

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
Ce document est un manuel développé pour Direct Rendering Manager afin d'aider les ingénieurs à démarrer plus rapidement

**<font face="黑体"  size=5>Objets de lecture</font>**

Les principales personnes auxquelles ce document (ce guide) s'applique :

- Développeurs de logiciels
- Personnel de soutien technique

**<font face="黑体"  size=5>Historique des révisions</font>**
 <font face="宋体"  size=2>L'historique des révisions accumule une description de chaque mise à jour de document. La dernière version du document contient des mises à jour pour toutes les versions précédentes. </font>

| Le numéro de version   | Modifié par     | Date de révision | Notes de révision |
|  :-----  |-------   |  ------  |  ------  |
| Version 1.0.0 | Groupes de logiciels système | 2022-03-22 |          |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenu</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Introduction

La version Linux actuellement utilisée par sdk est 4.17.0. Linux, nom complet GNU/Linux, est un système d'exploitation de type UNIX libre d'utilisation et librement diffusé avec un noyau publié pour la première fois par Linus Bennadict Torvaz le 5 octobre 1991, il est principalement inspiré des idées de Minix et Unix, et est un système d'exploitation multi-utilisateur, multi-tâches, multi-thread et multi-CPU basé sur POSIX. Il exécute les principaux logiciels, applications et protocoles réseau de l'outil Unix. Il prend en charge le matériel 32 bits et 64 bits. Linux hérite de la philosophie de conception centrée sur le réseau d'Unix et est un système d'exploitation réseau multi-utilisateurs stable. Linux possède des centaines de distributions différentes, telles que Debian communautaire, archlinux et Red Hat Enterprise Linux, SUSE, Oracle Linux, etc. développés commercialement.

# 2 Introduction du matériel

## 2.1 Méthode d'acquisition

Téléchargez et compilez le SDK, le SDK téléchargera et compilera le code Linux lors de la compilation.

Pour plus d'informations sur le téléchargement et la compilation du Kit de développement logiciel (SDK), voir[K510_SDK_Build_and_Burn_Guide](./K510_SDK_Build_and_Burn_Guide.md).

## 2.2 Fichiers et répertoires de pilotes

```text
drivers/gpu/drm/canaan/
```

## 2.3 Exigences en matière d'environnement de développement

non

## 2.4 Système d'exploitation

La prise en charge du système Linux et du numéro de version est illustrée dans la figure suivante :

| numérotation | Ressources logicielles | illustrer        |
| ---- | -------- | ----------- |
| 1    | Ubuntu   | 18.04/20.04 |
|      |          |             |
|      |          |             |
|      |          |             |

## 2.5 Environnement logiciel

La configuration requise pour l'environnement logiciel est indiquée dans le tableau suivant :

| numérotation | Ressources logicielles | illustrer |
| :--- | -------- | ---- |
| 1    | Kit de développement logiciel (SDK) K510 | v1.1 |
|      |          |      |
|      |          |      |
|      |          |      |

# Gestionnaire de rendu 3Direct

## 3.1 Connexions de référence

nvdia drm:<https://docs.nvidia.com/jetson/l4t-multimedia/group__direct__rendering__manager.html>

drm freedesktop:<https://cgit.freedesktop.org/mesa/drm>
<https://gitlab.freedesktop.org/mesa/drm>

## 3.2 API officielle drm
<!-- markdownlint-disable header-increment no-hard-tabs -->
##### ◆ drmModeAddFB()

```c
int drmModeAddFB(int fd,
    uint32_t width,
    uint32_t height,
    uint8_t depth,
    uint8_t bpp,
    uint32_t pitch,
    uint32_t bo_handle,
    uint32_t *buf_id 
)
```

Crée un framebuffer.

La fonction crée un framebuffer avec une taille et un format spécifiés, en utilisant l'objet tampon spécifié comme magasin de sauvegarde de mémoire. L'objet buffer peut être un « buffer muet » créé par un appel à drmIoctl avec le paramètre request défini sur DRM_IOCTL_MODE_CREATE_DUMB, ou il peut s'agir d'un dma-buf importé par un appel à la fonction drmPrimeFDToHandle.

###### Postcondition

Si l'appel réussit, l'application doit supprimer (libérer) le framebuffer en appelant drmModeRmFB.

###### Paramètres

```text
Parameters
[in]	fd	The file descriptor of an open DRM device.
[in]	width	Framebuffer width in pixels.
[in]	height	Framebuffer height in pixels.
[in]	depth	Framebuffer depth in bits.
[in]	bpp	Framebuffer bits per pixel.
[in]	pitch	Framebuffer pitch in bytes.
[in]	bo_handle	A handle for a buffer object to provide memory backing.
[out]	buf_id	Receives the framebuffer ID of the created framebuffer if framebuffer creation is successful.
```

###### Retourne

```text
0 if framebuffer creation is successful, or -1 otherwise.
```

##### ◆ drmModeAddFB2()

```c
int drmModeAddFB2(int fd,
    uint32_t width,
    uint32_t height,
    uint32_t pixel_format,
    const uint32_t bo_handles[4],
    const uint32_t pitches[4],
    const uint32_t offsets[4],
    uint32_t *buf_id,
    uint32_t flags 
)
```

Crée un framebuffer, en spécifiant le format et les plans.

Cette fonction est similaire à :d rmModeAddFB, mais offre plus d'options. Le format de pixel des objets tampon est spécifié explicitement, au lieu d'être profondeur +bpp comme dans drmModeAddFB. En outre, les formats YUV multiplanaires sont pris en charge. Comme pour drmModeAddFB, la ou les poignées d'objet tampon peuvent être des tampons muets ou des dma-bufs importés.

###### Postcondition

Si l'appel réussit, l'application doit supprimer (libérer) le framebuffer en appelant drmModeRmFB.

###### Note

Le paramètre flags n'est actuellement pas pris en charge.

###### Paramètres

```text
[in]	fd	The file descriptor of an open DRM device.
[in]	width	Framebuffer width in pixels.
[in]	height	Framebuffer height in pixels.
[in]	pixel_format	Pixel format of the bo_handle(s).
[in]	bo_handles	An array of four handles for buffer objects to provide memory backing. Unused array elements must be NULL.
[in]	pitches	An array containing the pitches of the buffer objects in bytes.
[in]	offsets	An array containing the offsets of the buffer objects in bytes.
[out]	buf_id	Receives the framebuffer ID of the created framebuffer if framebuffer creation is successful.
[in]	flags	Creation flags.
```

###### Retourne

```text
0 if successful, or -1 otherwise.
```

##### ◆ drmModeAddFB2WithModifiers()

```c
int drmModeAddFB2WithModifiers	(	int 	fd,
uint32_t 	width,
uint32_t 	height,
uint32_t 	pixel_format,
const uint32_t 	bo_handles[4],
const uint32_t 	pitches[4],
const uint32_t 	offsets[4],
const uint64_t 	modifier[4],
uint32_t * 	buf_id,
uint32_t 	flags 
)
```

Crée un framebuffer, en spécifiant le format et les plans.
Cette fonction est similaire à :d rmModeAddFB2, mais accepte les modificateurs.

###### Postcondition

Si l'appel réussit, l'application doit supprimer (libérer) le framebuffer en appelant drmModeRmFB.

###### Note

###### Paramètres

```text
[in]	fd	The file descriptor of an open DRM device.
[in]	width	Framebuffer width in pixels.
[in]	height	Framebuffer height in pixels.
[in]	pixel_format	Pixel format of the bo_handle(s).
[in]	bo_handles	An array of four handles for buffer objects to provide memory backing. Unused array elements must be NULL.
[in]	pitches	An array containing the pitches of the buffer objects in bytes.
[in]	offsets	An array containing the offsets of the buffer objects in bytes.
[in]	modifier	An array containing the format modifiers. For multi-planar formats, each plane should have same modifier value. Supported modifiers can be obtained using IN_FORMATS plane property.
[out]	buf_id	Receives the framebuffer ID of the created framebuffer if framebuffer creation is successful.
[in]	flags	flags should be DRM_MODE_FB_MODIFIERS when modifiers are specified, otherwise 0.
```

###### Retourne

```text
0 if successful, or -1 otherwise.
```

##### ◆ drmModeAtomicAddProperty()

```c
int drmModeAtomicAddProperty	(	drmModeAtomicReqPtr 	req,
uint32_t 	object_id,
uint32_t 	property_id,
uint64_t 	value 
)
```

Ajoute une propriété à une demande atomique.
Ajoute une propriété et une valeur à une demande atomique.

###### Postcondition

###### Note

###### Paramètres

```text
req:	     An atomic request.
object_id:	 Object ID of a CRTC, plane, or connector to be modified.
property_id: Property ID of the property to be modified.
value:	     The new value for the property.
```

###### Retourne

```text
-1 :if req is NULL or the API is out of memory, otherwise it returns the number of properties in the atomic request

-EINVAL: if DRM_CLIENT_CAP_ATOMIC is not enabled.
```

##### ◆ drmModeAtomicCommit()

```c
int drmModeAtomicCommit	(	int 	fd,
                            drmModeAtomicReqPtr 	req,
                            uint32_t 	flags,
                            void * 	user_data 
)
```

Valide une demande de modification de propriété atomique sur le matériel.

Envoie toutes les modifications de propriété dans une structure drmModeAtomicReqPtr au matériel.

###### Postcondition

###### Note

###### Paramètres

```text
fd:	The file descriptor of an open DRM device.
req:	The request object describing properties to commit.
flags:	Flags which influence the operation. The supported flags are:
        DRM_MODE_PAGE_FLIP_ASYNC: Commits values immediately when possible; does not latch new properties at the next vblank.
        DRM_MODE_ATOMIC_NONBLOCK: Commits values to hardware but does not wait for hardware to accept the new values.
        DRM_MODE_ATOMIC_TEST_ONLY: Validates input, but does not commit the values to hardware.
user_data :	Unused.
```

###### Retourne

```text
0	if successful.
-1	if req is NULL.
-EINVAL	if DRM_CLIENT_CAP_ATOMIC is not enabled, the value of flags is illegal, or atomic property IDs in the request are not recognized.
```

##### ◆ drmModeAtomicFree()

```c
void drmModeAtomicFree	(	drmModeAtomicReqPtr 	req	)
```

Libère une requête atomique.

Libère un objet drmModeAtomicReqPtr alloué par drmModeAtomicAlloc et tous les objets drmModeAtomicReqItemPtr associés.

###### Postcondition

###### Note

###### Paramètres

```text
req	:The atomic request object to be freed.
```

###### Retourne

```text
NULL
```

##### ◆ drmModeFreeConnector()

```c
void drmModeFreeConnector	(	drmModeConnectorPtr 	ptr	)
```

Libère un connecteur.

Libère une structure drmModeConnectorPtr allouée par drmModeGetConnector.

###### Postcondition

###### Note

###### Paramètres

```text
ptr	A pointer to the connector to be freed.
```

###### Retourne

```text
null
```

##### ◆ drmModeFreeObjectProperties()

```c
void drmModeFreeObjectProperties	(	drmModeObjectPropertiesPtr 	ptr	)
```

Libère une structure de propriétés d'objet.

Libère une structure drmModeObjectPropertiesPtr allouée par drmModeObjectGetProperties.

###### Postcondition

###### Note

###### Paramètres

```text
ptr	A pointer to the object properties structure to be freed.
```

###### Retourne

```text
null
```

##### ◆ drmModeFreePlaneResources()

```c
void drmModeFreePlane	(	drmModePlanePtr 	ptr	)
```

Libère un avion.

Libère une structure drmModePlanePtr allouée par drmModeGetPlane.

###### Postcondition

###### Note

###### Paramètres

```text
ptr	A pointer to the plane to be freed.
```

###### Retourne

```text
null
```

##### ◆ drmModeFreeProperty()

```c
void drmModeFreeProperty	(	drmModePropertyPtr 	ptr	)
```

Libère une structure de propriété.

Libère une structure drmModePropertyPtr allouée par drmModeGetProperty.

###### Postcondition

###### Note

###### Paramètres

```text
ptr	A pointer to a property structure returned by drmModeGetProperty.
```

###### Retourne

```text
null
```

##### ◆ drmModeFreeResources()

```c
void drmModeFreeResources	(	drmModeResPtr 	ptr	)
```

Libère une structure d'informations sur les ressources.

Libère une structure drmModeResPtr allouée par drmModeGetResources.

###### Postcondition

###### Note

###### Paramètres

```text
ptr	A pointer to the resource to be freed.
```

###### Retourne

```text
null
```

##### ◆ drmModeGetConnector()

```c
drmModeConnectorPtr drmModeGetConnector	(	int 	fd,
                                           uint32_t 	connector_id 
)
```

Obtient des informations pour un connecteur.

Si connector_id est valide, récupère une structure drmModeConnectorPtr qui contient des informations sur un connecteur, telles que les modes disponibles, l'état de la connexion, le type de connecteur et l'encodeur (le cas échéant) connecté.

###### Postcondition

Si l'appel réussit, l'application doit libérer la structure d'informations du connecteur en appelant drmModeFreeConnector.

###### Note

connector->mmWidth et connector->mmHeight sont actuellement définis sur des valeurs d'espace réservé.

###### Paramètres

```text
fd :	        The file descriptor of an open DRM device.
connector_id:	The connector ID of the connector to be retrieved.
```

###### Retourne

```text
A drmModeConnectorPtr structure if successful, or NULL if the connector is not found or the API is out of memory.
```

##### ◆ drmModeGetPlaneResources()

```c
drmModePlaneResPtr drmModeGetPlaneResources	(	int 	fd	)
```

Obtient des informations sur les avions.

Obtient une liste des ressources planes pour un périphérique DRM. Une application DRM appelle généralement cette fonction tôt pour identifier les couches d'affichage disponibles.

Par défaut, les informations renvoyées incluent uniquement les plans de type " Superposition " (réguliers) - pas les plans « Primaire » et « Curseur ». Si DRM_CLIENT_CAP_UNIVERSAL_PLANES a été activé avec drmSetClientCap, les informations renvoyées incluent les plans « Principal » représentant les CTRAC et les plans « Curseur » représentant les Curseurs. Cela permet de manipuler les CRTC et les curseurs avec des fonctions planes telles que drmModeSetPlane.

###### Postcondition

Si l'appel réussit, l'application doit libérer la structure d'informations plane en appelant drmModeFreePlaneResources.

###### Note

DRM n'implémente actuellement pas de plans de type « Cursor ».

###### Paramètres

```text
fd	The file descriptor of an open DRM device.
```

###### Retourne

```text
A drmModeResPtr structure if successful, or NULL otherwise.
```

##### ◆ drmModeGetProperty()

```c
drmModePropertyPtr drmModeGetProperty	(	int 	fd,
                                            uint32_t 	propertyId 
)
```

Obtient une structure de propriété qui décrit une propriété d'un objet DRM.

L'objet DRM peut être un plan, un CRTC ou un connecteur.

Cette fonction fonctionne sur une structure drmModeObjectPropertiesPtr renvoyée par drmModeObjectGetProperties().

Les propriétés modifiables dépendent du type d'objet DRM :

1. Pour un plan (type d'objet DRM_MODE_OBJECT_PLANE) :

    ```text
    "SRC_X", "SRC_Y", "SRC_W", "SRC_H", "zpos", "alpha" "CRTC_X",
    "CRTC_Y", "CRTC_W", "CRTC_H", "CRTC_ID", "FB_ID"
    ```

2. Pour un CRTC (type d'objet DRM_MODE_OBJECT_CRTC), les valeurs prises en charge sont les suivantes :

    ```text
    "MODE_ID", "ACTIVE", "HDR_SUPPORTED", "HDR_METADATA_SMPTE_2086_ID"
    ```

3. Pour un connecteur (type d'objet DRM_MODE_OBJECT_CONNECTOR), la valeur prise en charge est :

    ```text
    "CRTC_ID"
    ```

Pour les plans DRM, le champ enums contient une liste de paires de mots-clés (nom : valeur) qui définit les propriétés.

```c
drmModePropertyPtr->enums[ ].name
drmModePropertyPtr->enums[ ].value
```

1. Les valeurs prises en charge pour le champ de nom sont définies ci-dessus (c.-à-d. « SRC_X », « SRC_Y » ou « SRC_W »). Ce champ est modifiable.
2. Les valeurs prises en charge pour les champs de valeur sont les suivantes :

```text
"Primary", "Overlay", "Cursor" 
```

Ce champ est en lecture seule.

Pour identifier le type de plan, parcourez la liste suivante pour localiser l'énumération dont le champ de valeur correspond à celui que vous recherchez. Ensuite, obtenez la valeur du champ de nom correspondant.

```c
drmModePropertyPtr->enums[ ] 
```

Par exemple:

```c
for (j = 0; j < props->count_enums; j++) {
    printf("\t\t%lld = %s\n", props->enums[j].value, props->enums[j].name);
    if (props->enums[j].value == value)
        name = props->enums[j].name;
}
if (props->count_enums && name) {
    /* The specified plane property value appears in the DRM properties. */
    /* Print the property name, which will be "Primary", "Overlay", or "Cursor". */
    printf("\tcon_value    : %s\n", name);
} else {
    /* The specified plane property value does not appear in the DRM properties. */
    /* Print the property value for which we were looking. */
    printf("\tcon_value    : %" PRIu64 "\n", value);
}
```

###### Postcondition

Si l'appel réussit, l'application doit libérer la structure d'informations de propriété en appelant drmModeFreeProperty.

###### Note

La valeur zpos d'un plan est initialisée avec un décalage de 10 par rapport au plan suivant. Il s'agit de permettre une configuration flexible des têtes. Par exemple:

1. Type « Primaire » Plan zpos = 10
2. Premier plan « superposition » zpos = 20
3. Suivant « Superposition » Plan zpos = 30
4. Etc.

La plage autorisée pour zpos est [0, 255]. Les plans avec des valeurs numériquement plus grandes pour zpos obstruent les plans avec des valeurs numériquement inférieures.
La valeur alpha d'un plan entraîne l'application d'une transparence à l'échelle du plan ainsi que de l'alpha par pixel contenu dans l'objet tampon. La plage autorisée pour l'alpha est [0, 255], où 0 est entièrement transparent et 255 indique que seul l'alpha par pixel a un effet. Pour les formats de pixels non alpha, il n'y a pas d'alpha par pixel, donc 255 indique une opacité totale.

###### Paramètres

```text
fd:	The file descriptor of an open DRM device.
propertyId:	Property ID of the property object to be fetched.
```

###### Retourne

```text
A drmModePropertyPtr if successful, or NULL otherwise.
```

##### ◆ drmModeGetResources()

```c
drmModeResPtr drmModeGetResources	(	int 	fd	)
```

Obtient des informations sur les CRTC, encodeurs et connecteurs d'un périphérique DRM.

Obtient une liste des principales ressources d'un périphérique DRM. Une application DRM appelle généralement cette fonction tôt pour identifier les affichages disponibles et d'autres ressources. Cependant, la fonction ne signale pas les ressources planes. Ceux-ci peuvent être interrogés avec drmModeGetPlaneResources.

###### Postcondition

Si l'appel réussit, l'application doit libérer la structure d'informations sur les ressources en appelant drmModeFreeResources.

###### Note

Les membres min_width, min_height, max_width et max_height de la structure drmModeResPtr sont définis sur des valeurs d'espace réservé.

###### Paramètres

```text
fd	The file descriptor of an open DRM device.

```

###### Retourne

```text
A drmModeResPtr structure if successful, or NULL otherwise.
```

##### ◆ drmModeObjectGetProperties()

```c
drmModeObjectPropertiesPtr drmModeObjectGetProperties	(	int 	fd,
                                                            uint32_t 	object_id,
                                                            uint32_t 	object_type 
)
```

Obtient toutes les propriétés d'un objet DRM.

Obtient une structure de propriétés d'objet qui décrit toutes les propriétés modifiables atomiquement d'un objet DRM spécifié, ainsi que les propriétés en lecture seule non incluses dans les structures drmModeCrtcPtr, drmModeConnectorPtr et drmModePlanePtr correspondantes. Vous pouvez ensuite récupérer des propriétés individuelles avec drmModeGetProperty et modifier leurs valeurs avec drmModeAtomicAddProperty.

La structure drmModeObjectPropertiesPtr contient un tableau d'ID de propriété (props), un tableau de valeurs de propriété correspondantes (prop_values) et le nombre d'éléments de chaque tableau (count_props). Vous pouvez obtenir le nom d'une propriété en appelant drmModeGetProperty sur l'ID de propriété et en examinant le champ de nom de la structure drmModePropertyPtr renvoyé.

Pour modifier une propriété de manière atomique, créez un objet de demande drmModeAtomicReqPtr en appelant drmModeAtomicAlloc, puis appelez drmModeAtomicAddProperty, en spécifiant l'objet drmModeAtomicReqPtr, l'ID d'objet de l'objet à modifier, l'ID de propriété de la propriété à modifier et la nouvelle valeur de la propriété. Validez ensuite la demande avec drmModeAtomicCommit. Vous pouvez définir plusieurs propriétés dans une requête atomique et les valider en une seule opération.

###### Postcondition

Si l'appel réussit, l'application doit libérer la structure drmModeObjectPropertiesPtr en appelant drmModeFreeObjectProperties.

###### Note

Tous les types d'objets ne sont pas pris en charge.

###### Paramètres

```text
fd:	The file descriptor of an open DRM device.
object_id:	The object ID of the DRM object whose properties are to be retrieved.
object_type:	A symbol representing an object type. The following object types are supported:
    DRM_MODE_OBJECT_CRTC
    DRM_MODE_OBJECT_CONNECTOR
    DRM_MODE_OBJECT_PLANE
```

###### Retourne

```text
A drmModeObjectPropertiesPtr object if successful, or NULL otherwise.
```

##### ◆ drmModeRmFB()

```c
int drmModeRmFB	(	int 	fd,
                    uint32_t 	fb_id 
)
```

Détruit un framebuffer.

Détruit (libère) un framebuffer alloué par drmModeAddFB ou drmModeAddFB2.

###### Postcondition

###### Note

###### Paramètres

```text
fd	The file descriptor of an open DRM device.
fb_id	The ID of the framebuffer to destroy.
```

###### Retourne

```text
0 if destruction is successful, or -ENOENT if the framebuffer is not found.
```

##### ◆ drmModeSetCrtc()

```c
int drmModeSetCrtc	(	int 	fd,
                        uint32_t 	crtc_id,
                        uint32_t 	fb_id,
                        uint32_t 	x,
                        uint32_t 	y,
                        uint32_t * 	connectors,
                        int 	count,
                        drmModeModeInfoPtr 	drm_mode 
)
```

Définit une configuration CRTC.

Si le mode DRM est spécifié (si drm_mode n'est pas NULL), définit le mode d'affichage sur le CRTC et le ou les connecteurs spécifiés. Les nouvelles propriétés fb_id, x et y seront définies sur vblank.

###### Postcondition

###### Note

Les paramètres fb_id, x et y acceptent la valeur d'entrée spéciale -1, qui indique que le tampon de cadre de la fenêtre matérielle ou le décalage correspondant ne doit pas être modifié. (Les pilotes DRM basés sur le noyau acceptent -1 uniquement pour fb_id. Ils renvoient le code d'erreur -ERANGE si on leur donne -1 pour x ou y.)
Il est permis de spécifier un mode valide et fb_id==-1, même si aucun tampon de trame n'est actuellement attaché au CRTC. La fonction définira le mode d'affichage, mais laissera le tampon de trame CRTC indéfini.
Les tampons de trame définis sur un CRTC, que ce soit par drmModeSetCrtc, drmModePageFlip ou tout autre moyen, sont affichés derrière des plans. La couche d'affichage CRTC est la plus basse dans l'ordre d'empilement.

###### Paramètres

```text
fd:	The      file descriptor of an open DRM device.
crtc_id	:    The ID of the CRTC to be set.
fb_id:	     ID of the framebuffer to display with this CRTC, or -1 to use the same CRTC as the previous operation.
x:	         Offset from left of active display region to place the framebuffer. If x is -1, the X offset is not changed.
y:	         Offset from top of active display region to place the framebuffer. If y is -1, the Y offset is not changed.
connectors:	 A pointer to a list of connectors to bind to the CRTC.
count:	     Number of connectors in the connectors list.
drm_mode:	 Mode to set, or NULL to use the same mode as the previous operation.
```

###### Retourne

```text
0:	      if successful.
-EINVAL:  if crtc_id is invalid.
-1:	      if count is invalid, or the list specified by connectors is incompatible with the CRTC.
-errno:	  otherwise.
```

##### ◆ drmModeSetPlane()

```c
int drmModeSetPlane	(	int 	fd,
                        uint32_t 	plane_id,
                        uint32_t 	crtc_id,
                        uint32_t 	fb_id,
                        uint32_t 	flags,
                        int32_t 	crtc_x,
                        int32_t 	crtc_y,
                        uint32_t 	crtc_w,
                        uint32_t 	crtc_h,
                        uint32_t 	src_x,
                        uint32_t 	src_y,
                        uint32_t 	src_w,
                        uint32_t 	src_h 
)
```

Modifie le tampon de trame et la position d'un plan.

###### Postcondition

###### Note

Le crtc_... et src_... les paramètres acceptent la valeur d'entrée spéciale -1, ce qui indique que la valeur de décalage matériel ne doit pas être modifiée. (Les pilotes DRM basés sur le noyau renvoient le code d'erreur -ERANGE lorsqu'ils reçoivent cette valeur.)
Les tampons de trame définis sur les plans sont affichés au-dessus des CRTC. L'ordre d'empilement des plans est indiqué par l'ordre dans lequel les plans sont signalés par drmModeGetPlaneResources.
Toutes les opérations drmModeSetPlane sont synchronisées avec vblank et sont bloquées.

###### Paramètres

```text
fd:	        The file descriptor of an open DRM device.
plane_id:	Plane ID of the plane to be changed.
crtc_id:	CRTC ID of the CRTC that the plane is on.
fb_id:	    Framebuffer ID of the framebuffer to display on the plane, or -1 to leave the framebuffer unchanged.
flags:   	Flags that control function behavior. No flags are currently supported for external use.
crtc_x: 	Offset from left of active display region to show plane.
crtc_y: 	Offset from top of active display region to show plane.
crtc_w: 	Width of output rectangle on display.
crtc_h: 	Height of output rectangle on display.
src_x:  	Clip offset from left of source framebuffer (Q16.16 fixed point).
src_y:  	Clip offset from top of source framebuffer (Q16.16 fixed point).
src_w:  	Width of source rectangle (Q16.16 fixed point).
src_h:  	Height of source rectangle (Q16.16 fixed point).
```

###### Retourne

```text
0:  	    if successful.
-EINVAL:	if plane_id or crtc_id is invalid.
-errno: 	otherwise.
```

##### ◆ drmSetClientCap()

```c
int drmSetClientCap	(	int 	fd,
                        uint64_t 	capability,
                        uint64_t 	value 
)
```

Active ou désactive les fonctionnalités DRM (capacités).

###### Postcondition

###### Note

###### Paramètres

```text

fd:	         The file descriptor of an open DRM device.
capability：	Specifies the capability to be enabled or disabled. Supported values are:
                    DRM_CLIENT_CAP_ATOMIC (disabled by default)
                    DRM_CLIENT_CAP_UNIVERSAL_PLANES (disabled by default)
value:  	 0 to disable the capability, or 1 to enable it.
```

###### Retourne

```text
0 if successful, or -EINVAL otherwise.
```

##### ◆ drmWaitVBlank()

```c
int drmWaitVBlank	(	int 	fd,
drmVBlankPtr 	vbl 
)
```

Attend un intervalle d'effacement vertical (vblank).

Attend un vblank spécifié ou demande que le gestionnaire vblank enregistré soit appelé lorsqu'un vblank spécifié se produit.

###### Postcondition

###### Note

ne prend actuellement pas en charge tous les champs drmVblankPtr.

###### Paramètres

```text
fd:	    The file descriptor of an open DRM device.
vbl:	A description of the requested vblank. The vbl->type field must contain one of these values:
           DRM_VBLANK_ABSOLUTE: request.sequence is the vblank count since some point in the past, e.g. system boot.
           DRM_VBLANK_RELATIVE: request.sequence is the vblank count from the current value. e.g. 1 specifies the next vblank. The value may be bitwise ORed with any combination of these values:
           DRM_VBLANK_SECONDARY: Uses the secondary display's vblank.
           DRM_VBLANK_EVENT: Returns immediately and triggers the event callback instead of waiting for a specified vblank.
```

###### Retourne

```text
0 if successful, or -1 otherwise.
```

##### ◆ drmModePageFlip()

```c
int drmModePageFlip	(	int 	fd,
uint32_t 	crtc_id,
uint32_t 	fb_id,
uint32_t 	flags,
void * 	user_data 
)
```

###### Postcondition

Demande un retournement de page (changement de tampon de cadre) sur le CRTC spécifié.

Planifie un retournement de page sur le CRTC spécifié. Par défaut, le CRTC sera reprogrammé pour afficher le framebuffer spécifié après la prochaine actualisation verticale.

###### Note

###### Paramètres

```text
fd :	    The file descriptor of an open DRM device.
crtc_id :	CRTC ID of the CRTC whose framebuffer is to be changed.
fb_id :	    Framebuffer ID of the framebuffer to be displayed.
flags :	    Flags affecting the operation. Supported values are:
                  DRM_MODE_PAGE_FLIP_ASYNC: Flip immediately, not at vblank.
                  DRM_MODE_PAGE_FLIP_EVENT: Send page flip event.
user_data:	Data used by the page flip handler if vblank event was requested.
```

###### Retourne

```text
0	if successful.
-EINVAL	if crtc_id or fb_id is invalid.
-errno	otherwise.
```
<!-- markdownlint-enable header-increment no-hard-tabs -->
## 3.3 k510 DRM a ajouté une description de l'utilisation de la fonction frame

Définition de la structure

```c
struct vo_draw_frame {
    uint32_t draw_en;       // 使能
    uint32_t line_x_start;  // start x
    uint32_t line_y_start;  // start y

    uint32_t line_x_end;    // stop x
    uint32_t line_y_end;    // stop y

    uint32_t frame_num;     // 画框的id

    uint32_t crtc_id;       // crtc id
};
```

Définitions de macro

```c
define DRM_KENDRYTE_DRAW_FRAME         0x00

#define DRM_IOCTL_KENDRYTE_DRAW_FRAME   DRM_IOWR(DRM_COMMAND_BASE + \
                DRM_KENDRYTE_DRAW_FRAME, struct vo_draw_frame)
```

Fonction Frame

```c
static int draw_frame(struct vo_draw_frame *frame)
{
    return drmIoctl(drm_dev.fd, DRM_IOCTL_KENDRYTE_DRAW_FRAME, frame);
}
```

**Clause de non-responsabilité en matière de**  
Pour la commodité des clients, Canaan utilise un traducteur IA pour traduire du texte en plusieurs langues, ce qui peut contenir des erreurs. Nous ne garantissons pas l'exactitude, la fiabilité ou l'actualité des traductions fournies. Canaan ne sera pas responsable de toute perte ou dommage causé par la confiance accordée à l'exactitude ou à la fiabilité des informations traduites. S'il existe une différence de contenu entre les traductions dans différentes langues, la version simplifiée en chinois prévaudra.

Si vous souhaitez signaler une erreur de traduction ou une inexactitude, n'hésitez pas à nous contacter par courrier.
