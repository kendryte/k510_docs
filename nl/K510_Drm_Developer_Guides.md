![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 Direct Rendering Manager Ontwikkelingshandleiding</font>**

<font face="黑体"  size=3>Document versie: P0.1.0</font>

<font face="黑体"  size=3>Publicatiedatum: 2022-01-01</font>

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
Dit document is een handleiding die is ontwikkeld voor Direct Rendering Manager om ingenieurs te helpen sneller aan de slag te gaan

**<font face="黑体"  size=5>Reader Objecten</font>**

De belangrijkste personen op wie dit document (deze gids) van toepassing is:

- Softwareontwikkelaars
- Technisch ondersteunend personeel

**<font face="黑体"  size=5>Revisiegeschiedenis</font>**
 <font face="宋体"  size=2>De revisiegeschiedenis bevat een beschrijving van elke documentupdate. De nieuwste versie van het document bevat updates voor alle voorgaande versies. </font>

| Het versienummer   | Gewijzigd door     | Datum van herziening | Opmerkingen bij herziening |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | Systeemsoftwaregroepen | 2022-03-22 |          |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Inhoud</font>**

[INHOUDSOPGAVE]

<div style="page-break-after:always"></div>

# 1 Inleiding

De Linux-versie die momenteel door sdk wordt gebruikt, is 4.17.0. Linux, volledige naam GNU/Linux, is een vrij te gebruiken en vrij verspreid UNIX-achtig besturingssysteem met een kernel die voor het eerst werd uitgebracht door Linus Bennadict Torvaz op 5 oktober 1991, het is voornamelijk geïnspireerd door de ideeën van Minix en Unix, en is een multi-user, multi-tasking, multi-threaded en multi-CPU-gebaseerd besturingssysteem gebaseerd op POSIX. Het draait belangrijke Unix-toolsoftware, applicaties en netwerkprotocollen. Het ondersteunt zowel 32-bits als 64-bits hardware. Linux erft Unix's netwerkgerichte ontwerpfilosofie en is een stabiel multi-user netwerkbesturingssysteem. Linux heeft honderden verschillende distributies, zoals community-based debian, archlinux en commercieel ontwikkelde Red Hat Enterprise Linux, SUSE, Oracle Linux, enz.

# 2 Hardware introductie

## 2.1 Acquisitie methode

Download en compileer de SDK, de SDK zal de Linux-code downloaden en compileren tijdens het compileren.

Zie K510_SDK_Build_and_Burn_Guide voor meer informatie over het downloaden en compileren[van de SDK](./K510_SDK_Build_and_Burn_Guide.md).

## 2.2 Stuurprogrammabestanden en mappen

```text
drivers/gpu/drm/canaan/
```

## 2.3 Vereisten voor ontwikkelomgevingen

niet

## 2.4 Besturingssysteem

Ondersteuning voor Linux-systemen en versienummers wordt weergegeven in de volgende afbeelding:

| Nummering | Softwarebronnen | illustreren        |
| ---- | -------- | ----------- |
| 1    | Ubuntu   | 18.04/20.04 |
|      |          |             |
|      |          |             |
|      |          |             |

## 2.5 Software-omgeving

De vereisten voor de softwareomgeving worden weergegeven in de volgende tabel:

| Nummering | Softwarebronnen | illustreren |
| :--- | -------- | ---- |
| 1    | K510 SDK | v1,1 |
|      |          |      |
|      |          |      |
|      |          |      |

# 3Direct Rendering Manager

## 3.1 Referentieverbindingen

nvdia drm:<https://docs.nvidia.com/jetson/l4t-multimedia/group__direct__rendering__manager.html>

drm freedesktop:<https://cgit.freedesktop.org/mesa/drm>
<https://gitlab.freedesktop.org/mesa/drm>

## 3.2 drm officiële api
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

Hiermee maakt u een framebuffer.

De functie maakt een framebuffer met een opgegeven grootte en indeling, waarbij het opgegeven bufferobject wordt gebruikt als geheugenback-uparchief. Het bufferobject kan een "domme buffer" zijn die wordt gemaakt door een aanroep van drmIoctl met de parameter request ingesteld op DRM_IOCTL_MODE_CREATE_DUMB, of het kan een dma-buf zijn die is geïmporteerd door een aanroep naar de functie drmPrimeFDToHandle.

###### Postconditie

Als de aanroep succesvol is, moet de toepassing de framebuffer verwijderen (gratis) door drmModeRmFB aan te roepen.

###### Parameters

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

###### Retourneert

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

Hiermee maakt u een framebuffer, waarbij indeling en vlakken worden opgegeven.

Deze functie is vergelijkbaar met :d rmModeAddFB, maar biedt meer opties. De pixelindeling van de bufferobjecten wordt expliciet opgegeven, in plaats van diepte+bpp zoals in drmModeAddFB. Ook worden multiplanaire YUV-indelingen ondersteund. Wat drmModeAddFB betreft, kunnen de bufferobjecthandgreep(en) een domme buffer of geïmporteerde dma-bufs zijn.

###### Postconditie

Als de aanroep succesvol is, moet de toepassing de framebuffer verwijderen (gratis) door drmModeRmFB aan te roepen.

###### Notitie

De parameter flags wordt momenteel niet ondersteund.

###### Parameters

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

###### Retourneert

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

Hiermee maakt u een framebuffer, waarbij indeling en vlakken worden opgegeven.
Deze functie is vergelijkbaar met :d rmModeAddFB2, maar accepteert modifiers.

###### Postconditie

Als de aanroep succesvol is, moet de toepassing de framebuffer verwijderen (gratis) door drmModeRmFB aan te roepen.

###### Notitie

###### Parameters

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

###### Retourneert

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

Hiermee voegt u een eigenschap toe aan een atomaire aanvraag.
Hiermee voegt u een eigenschap en waarde toe aan een atomaire aanvraag.

###### Postconditie

###### Notitie

###### Parameters

```text
req:	     An atomic request.
object_id:	 Object ID of a CRTC, plane, or connector to be modified.
property_id: Property ID of the property to be modified.
value:	     The new value for the property.
```

###### Retourneert

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

Hiermee wordt een wijzigingsaanvraag voor atomaire eigenschappen toegewezen aan hardware.

Verzendt alle eigenschapswijzigingen in een drmModeAtomicReqPtr-structuur naar hardware.

###### Postconditie

###### Notitie

###### Parameters

```text
fd:	The file descriptor of an open DRM device.
req:	The request object describing properties to commit.
flags:	Flags which influence the operation. The supported flags are:
        DRM_MODE_PAGE_FLIP_ASYNC: Commits values immediately when possible; does not latch new properties at the next vblank.
        DRM_MODE_ATOMIC_NONBLOCK: Commits values to hardware but does not wait for hardware to accept the new values.
        DRM_MODE_ATOMIC_TEST_ONLY: Validates input, but does not commit the values to hardware.
user_data :	Unused.
```

###### Retourneert

```text
0	if successful.
-1	if req is NULL.
-EINVAL	if DRM_CLIENT_CAP_ATOMIC is not enabled, the value of flags is illegal, or atomic property IDs in the request are not recognized.
```

##### ◆ drmModeAtomicFree()

```c
void drmModeAtomicFree	(	drmModeAtomicReqPtr 	req	)
```

Bevrijdt een atomair verzoek.

Hiermee wordt een drmModeAtomicReqPtr-object vrijgemaakt dat is toegewezen door drmModeAtomicAlloc en alle bijbehorende drmModeAtomicReqItemPtr-objecten.

###### Postconditie

###### Notitie

###### Parameters

```text
req	:The atomic request object to be freed.
```

###### Retourneert

```text
NULL
```

##### ◆ drmModeFreeConnector()

```c
void drmModeFreeConnector	(	drmModeConnectorPtr 	ptr	)
```

Bevrijdt een connector.

Bevrijdt een drmModeConnectorPtr-structuur toegewezen door drmModeGetConnector.

###### Postconditie

###### Notitie

###### Parameters

```text
ptr	A pointer to the connector to be freed.
```

###### Retourneert

```text
null
```

##### ◆ drmModeFreeObjectProperties()

```c
void drmModeFreeObjectProperties	(	drmModeObjectPropertiesPtr 	ptr	)
```

Hiermee maakt u een objecteigenschappenstructuur vrij.

Bevrijdt een drmModeObjectPropertiesPtr-structuur toegewezen door drmModeObjectGetProperties.

###### Postconditie

###### Notitie

###### Parameters

```text
ptr	A pointer to the object properties structure to be freed.
```

###### Retourneert

```text
null
```

##### ◆ drmModeFreePlaneResources()

```c
void drmModeFreePlane	(	drmModePlanePtr 	ptr	)
```

Bevrijdt een vliegtuig.

Bevrijdt een drmModePlanePtr-structuur toegewezen door drmModeGetPlane.

###### Postconditie

###### Notitie

###### Parameters

```text
ptr	A pointer to the plane to be freed.
```

###### Retourneert

```text
null
```

##### ◆ drmModeFreeProperty()

```c
void drmModeFreeProperty	(	drmModePropertyPtr 	ptr	)
```

Bevrijdt een eigendomsstructuur.

Bevrijdt een drmModePropertyPtr-structuur toegewezen door drmModeGetProperty.

###### Postconditie

###### Notitie

###### Parameters

```text
ptr	A pointer to a property structure returned by drmModeGetProperty.
```

###### Retourneert

```text
null
```

##### ◆ drmModeFreeResources()

```c
void drmModeFreeResources	(	drmModeResPtr 	ptr	)
```

Hiermee maakt u een resource-informatiestructuur vrij.

Bevrijdt een drmModeResPtr-structuur toegewezen door drmModeGetResources.

###### Postconditie

###### Notitie

###### Parameters

```text
ptr	A pointer to the resource to be freed.
```

###### Retourneert

```text
null
```

##### ◆ drmModeGetConnector()

```c
drmModeConnectorPtr drmModeGetConnector	(	int 	fd,
                                           uint32_t 	connector_id 
)
```

Hiermee wordt informatie opgehaald voor een connector.

Als connector_id geldig is, haalt u een drmModeConnectorPtr-structuur op die informatie bevat over een connector, zoals beschikbare modi, verbindingsstatus, connectortype en welk coderingsprogramma (indien aanwezig) is aangesloten.

###### Postconditie

Als de aanroep succesvol is, moet de toepassing de connectorinformatiestructuur vrijmaken door drmModeFreeConnector aan te roepen.

###### Notitie

connector->mmBreedte en connector->mmHeight zijn momenteel ingesteld op tijdelijke aanduidingen.

###### Parameters

```text
fd :	        The file descriptor of an open DRM device.
connector_id:	The connector ID of the connector to be retrieved.
```

###### Retourneert

```text
A drmModeConnectorPtr structure if successful, or NULL if the connector is not found or the API is out of memory.
```

##### ◆ drmModeGetPlaneResources()

```c
drmModePlaneResPtr drmModeGetPlaneResources	(	int 	fd	)
```

Krijgt informatie over vliegtuigen.

Hiermee wordt een lijst met vliegtuigbronnen voor een DRM-apparaat opgehaald. Een DRM-toepassing roept deze functie meestal vroeg aan om de beschikbare weergavelagen te identificeren.

Standaard bevat de geretourneerde informatie alleen vlakken van het type "Overlay" (gewone vlakken) - niet de vlakken "Primair" en "Cursor". Als DRM_CLIENT_CAP_UNIVERSAL_PLANES is ingeschakeld met drmSetClientCap, bevat de geretourneerde informatie 'Primaire' vlakken die CTRCs vertegenwoordigen en 'Cursor'-vlakken die Cursors vertegenwoordigen. Hierdoor kunnen CRTC's en cursors worden gemanipuleerd met vliegtuigfuncties zoals drmModeSetPlane.

###### Postconditie

Als de aanroep succesvol is, moet de toepassing de vlakinformatiestructuur vrijmaken door drmModeFreePlaneResources aan te roepen.

###### Notitie

DRM implementeert momenteel geen vlakken van het type "Cursor".

###### Parameters

```text
fd	The file descriptor of an open DRM device.
```

###### Retourneert

```text
A drmModeResPtr structure if successful, or NULL otherwise.
```

##### ◆ drmModeGetProperty()

```c
drmModePropertyPtr drmModeGetProperty	(	int 	fd,
                                            uint32_t 	propertyId 
)
```

Hiermee wordt een eigenschapsstructuur opgehaald die een eigenschap van een DRM-object beschrijft.

Het DRM-object kan een vlak, een CRTC of een connector zijn.

Deze functie werkt op een drmModeObjectPropertiesPtr-structuur die wordt geretourneerd door drmModeObjectGetProperties().

De aanpasbare eigenschappen zijn afhankelijk van het DRM-objecttype:

1. Voor een vlak (objecttype DRM_MODE_OBJECT_PLANE):

    ```text
    "SRC_X", "SRC_Y", "SRC_W", "SRC_H", "zpos", "alpha" "CRTC_X",
    "CRTC_Y", "CRTC_W", "CRTC_H", "CRTC_ID", "FB_ID"
    ```

2. Voor een CRTC (objecttype DRM_MODE_OBJECT_CRTC) zijn ondersteunde waarden:

    ```text
    "MODE_ID", "ACTIVE", "HDR_SUPPORTED", "HDR_METADATA_SMPTE_2086_ID"
    ```

3. Voor een connector (objecttype DRM_MODE_OBJECT_CONNECTOR) is de ondersteunde waarde:

    ```text
    "CRTC_ID"
    ```

Voor DRM-vlakken bevat het veld opsommingen een lijst met trefwoordparen (naam : waarde) die de eigenschappen definiëren.

```c
drmModePropertyPtr->enums[ ].name
drmModePropertyPtr->enums[ ].value
```

1. Ondersteunde waarden voor het naamveld zijn hierboven gedefinieerd (d.w.z. "SRC_X", "SRC_Y" of "SRC_W"). Dit veld kan worden gewijzigd.
2. Ondersteunde waarden voor de waardevelden zijn:

```text
"Primary", "Overlay", "Cursor" 
```

Dit veld is alleen-lezen.

Als u het vlaktype wilt identificeren, doorloopt u de volgende lijst om het opsommingsteken te vinden waarvan het waardeveld overeenkomt met het veld dat u zoekt. Haal vervolgens de waarde op uit het bijbehorende naamveld.

```c
drmModePropertyPtr->enums[ ] 
```

Bijvoorbeeld:

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

###### Postconditie

Als de aanroep is geslaagd, moet de toepassing de eigenschapsinformatiestructuur vrijmaken door drmModeFreeProperty aan te roepen.

###### Notitie

De zpos-waarde voor een vlak wordt geïnitialiseerd met een verschuiving van 10 ten opzichte van het volgende vlak. Dit is om een flexibele configuratie van koppen mogelijk te maken. Bijvoorbeeld:

1. "Primair" type Vlak zpos = 10
2. Eerste "Overlay" Plane zpos = 20
3. Volgende "Overlay" Plane zpos = 30
4. Enz.

Het toegestane bereik voor zpos is [0, 255]. Vlakken met numeriek grotere waarden voor zpos sluiten vlakken af met numeriek lagere waarden.
De alfawaarde voor een vlak zorgt ervoor dat een vlakbrede transparantie wordt toegepast, evenals de alfa per pixel in het bufferobject. Het toegestane bereik voor alfa is [0, 255], waarbij 0 volledig transparant is en 255 aangeeft dat alleen alfa per pixel een effect heeft. Voor niet-alfapixelindelingen is er geen alfa per pixel, dus 255 geeft volledig ondoorzichtig aan.

###### Parameters

```text
fd:	The file descriptor of an open DRM device.
propertyId:	Property ID of the property object to be fetched.
```

###### Retourneert

```text
A drmModePropertyPtr if successful, or NULL otherwise.
```

##### ◆ drmModeGetResources()

```c
drmModeResPtr drmModeGetResources	(	int 	fd	)
```

Hier wordt informatie opgehaald over de CRTC's, encoders en connectoren van een DRM-apparaat.

Hiermee krijgt u een lijst met de belangrijkste bronnen van een DRM-apparaat. Een DRM-toepassing roept deze functie meestal vroeg aan om beschikbare beeldschermen en andere bronnen te identificeren. De functie rapporteert echter geen vliegtuigbronnen. Deze kunnen worden opgevraagd met drmModeGetPlaneResources.

###### Postconditie

Als de aanroep succesvol is, moet de toepassing de broninformatiestructuur vrijmaken door drmModeFreeResources aan te roepen.

###### Notitie

De leden min_width, min_height, max_width en max_height van de drmModeResPtr-structuur zijn ingesteld op tijdelijke waarden.

###### Parameters

```text
fd	The file descriptor of an open DRM device.

```

###### Retourneert

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

Hiermee worden alle eigenschappen van een DRM-object opgehaald.

Hiermee wordt een objecteigenschappenstructuur opgehaald die alle atomair aanpasbare eigenschappen van een opgegeven DRM-object beschrijft, evenals alleen-lezen eigenschappen die niet zijn opgenomen in de bijbehorende drmModeCrtcPtr-, drmModeConnectorPtr- en drmModePlanePtr-structuren. U kunt vervolgens afzonderlijke eigenschappen ophalen met drmModeGetProperty en hun waarden wijzigen met drmModeAtomicAddProperty.

De drmModeObjectPropertiesPtr-structuur bevat een array met eigenschaps-id's (rekwisieten), een array met overeenkomstige eigenschapswaarden (prop_values) en het aantal elementen in elke array (count_props). U kunt de naam van een eigenschap verkrijgen door drmModeGetProperty aan te roepen op de eigenschaps-id en naar het naamveld van de geretourneerde drmModePropertyPtr-structuur te kijken.

Als u een eigenschap atomiceel wilt wijzigen, maakt u een drmModeAtomicReqPtr-aanvraagobject door drmModeAtomicAlloc aan te roepen en vervolgens drmModeAtomicAddProperty aan te roepen, waarbij u het object drmModeAtomicReqPtr, de object-id van het te wijzigen object, de eigenschaps-id van de eigenschap die u wilt wijzigen en de nieuwe waarde van de eigenschap opgeeft. Voer vervolgens het verzoek in met drmModeAtomicCommit. U kunt verschillende eigenschappen instellen in een atomaire aanvraag en deze in één bewerking vastleggen.

###### Postconditie

Als de aanroep succesvol is, moet de toepassing de drmModeObjectPropertiesPtr-structuur vrijmaken door drmModeFreeObjectProperties aan te roepen.

###### Notitie

Niet alle objecttypen worden ondersteund.

###### Parameters

```text
fd:	The file descriptor of an open DRM device.
object_id:	The object ID of the DRM object whose properties are to be retrieved.
object_type:	A symbol representing an object type. The following object types are supported:
    DRM_MODE_OBJECT_CRTC
    DRM_MODE_OBJECT_CONNECTOR
    DRM_MODE_OBJECT_PLANE
```

###### Retourneert

```text
A drmModeObjectPropertiesPtr object if successful, or NULL otherwise.
```

##### ◆ drmModeRmFB()

```c
int drmModeRmFB	(	int 	fd,
                    uint32_t 	fb_id 
)
```

Vernietigt een framebuffer.

Vernietigt (bevrijdt) een framebuffer toegewezen door drmModeAddFB of drmModeAddFB2.

###### Postconditie

###### Notitie

###### Parameters

```text
fd	The file descriptor of an open DRM device.
fb_id	The ID of the framebuffer to destroy.
```

###### Retourneert

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

Hiermee stelt u een CRTC-configuratie in.

Als de DRM-modus is opgegeven (als drm_mode niet NULL is), stelt u de weergavemodus in op de CRTC en opgegeven connector(en). Nieuwe eigenschappen fb_id, x en y worden ingesteld op vblank.

###### Postconditie

###### Notitie

De parameters fb_id, x en y accepteren de speciale invoerwaarde -1, die aangeeft dat de hardware window framebuffer of de bijbehorende offset niet mag worden gewijzigd. (Kernelgebaseerde DRM-stuurprogramma's accepteren -1 alleen voor fb_id. Ze retourneren foutcode -ERANGE als ze -1 voor x of y krijgen.)
Het is toegestaan om een geldige modus en fb_id==-1 op te geven, zelfs als er momenteel geen framebuffer aan de CRTC is gekoppeld. De functie stelt de weergavemodus in, maar laat de CRTC-framebuffer ongedefinieerd.
Framebuffers die zijn ingesteld op een CRTC, hetzij door drmModeSetCrtc, drmModePageFlip of een andere manier, worden achter vlakken weergegeven. De CRTC-weergavelaag is de laagste in stapelvolgorde.

###### Parameters

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

###### Retourneert

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

Hiermee wijzigt u de framebuffer en positie van een vlak.

###### Postconditie

###### Notitie

De crtc_... en src_... parameters accepteren de speciale invoerwaarde -1, wat aangeeft dat de hardware-offsetwaarde niet mag worden gewijzigd. (Op kernel gebaseerde DRM-stuurprogramma's retourneren de foutcode -ERANGE wanneer deze waarde wordt gegeven.)
Framebuffers die op vliegtuigen zijn ingesteld, worden weergegeven bovenop CRTC's. De stapelvolgorde van vliegtuigen wordt aangegeven door de volgorde waarin de vliegtuigen worden gerapporteerd door drmModeGetPlaneResources.
Alle drmModeSetPlane-bewerkingen worden gesynchroniseerd met vblank en worden geblokkeerd.

###### Parameters

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

###### Retourneert

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

Hiermee schakelt u DRM-functies (mogelijkheden) in of uit.

###### Postconditie

###### Notitie

###### Parameters

```text

fd:	         The file descriptor of an open DRM device.
capability：	Specifies the capability to be enabled or disabled. Supported values are:
                    DRM_CLIENT_CAP_ATOMIC (disabled by default)
                    DRM_CLIENT_CAP_UNIVERSAL_PLANES (disabled by default)
value:  	 0 to disable the capability, or 1 to enable it.
```

###### Retourneert

```text
0 if successful, or -EINVAL otherwise.
```

##### ◆ drmWaitVBlank()

```c
int drmWaitVBlank	(	int 	fd,
drmVBlankPtr 	vbl 
)
```

Wacht op een verticaal blankingsinterval (vblank).

Wacht op een opgegeven vblank of vraagt om de geregistreerde vblank-handler aan te roepen wanneer een opgegeven vblank optreedt.

###### Postconditie

###### Notitie

ondersteunt momenteel niet alle drmVblankPtr-velden.

###### Parameters

```text
fd:	    The file descriptor of an open DRM device.
vbl:	A description of the requested vblank. The vbl->type field must contain one of these values:
           DRM_VBLANK_ABSOLUTE: request.sequence is the vblank count since some point in the past, e.g. system boot.
           DRM_VBLANK_RELATIVE: request.sequence is the vblank count from the current value. e.g. 1 specifies the next vblank. The value may be bitwise ORed with any combination of these values:
           DRM_VBLANK_SECONDARY: Uses the secondary display's vblank.
           DRM_VBLANK_EVENT: Returns immediately and triggers the event callback instead of waiting for a specified vblank.
```

###### Retourneert

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

###### Postconditie

Hiermee wordt een paginaomslag (framebufferwijziging) op de opgegeven CRTC aangevraagd.

Hiermee plant u een paginaomslag op de opgegeven CRTC. Standaard wordt de CRTC opnieuw geprogrammeerd om de opgegeven framebuffer weer te geven na de volgende verticale vernieuwing.

###### Notitie

###### Parameters

```text
fd :	    The file descriptor of an open DRM device.
crtc_id :	CRTC ID of the CRTC whose framebuffer is to be changed.
fb_id :	    Framebuffer ID of the framebuffer to be displayed.
flags :	    Flags affecting the operation. Supported values are:
                  DRM_MODE_PAGE_FLIP_ASYNC: Flip immediately, not at vblank.
                  DRM_MODE_PAGE_FLIP_EVENT: Send page flip event.
user_data:	Data used by the page flip handler if vblank event was requested.
```

###### Retourneert

```text
0	if successful.
-EINVAL	if crtc_id or fb_id is invalid.
-errno	otherwise.
```
<!-- markdownlint-enable header-increment no-hard-tabs -->
## 3.3 k510 DRM heeft een beschrijving van het gebruik van de framefunctie toegevoegd

Struct definitie

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

Macrodefinities

```c
define DRM_KENDRYTE_DRAW_FRAME         0x00

#define DRM_IOCTL_KENDRYTE_DRAW_FRAME   DRM_IOWR(DRM_COMMAND_BASE + \
                DRM_KENDRYTE_DRAW_FRAME, struct vo_draw_frame)
```

Frame functie

```c
static int draw_frame(struct vo_draw_frame *frame)
{
    return drmIoctl(drm_dev.fd, DRM_IOCTL_KENDRYTE_DRAW_FRAME, frame);
}
```

**Vertaling Disclaimer**  
Voor het gemak van klanten gebruikt Canaan een AI-vertaler om tekst in meerdere talen te vertalen, wat fouten kan bevatten. Wij garanderen niet de nauwkeurigheid, betrouwbaarheid of tijdigheid van de geleverde vertalingen. Canaan is niet aansprakelijk voor enig verlies of schade veroorzaakt door het vertrouwen op de nauwkeurigheid of betrouwbaarheid van de vertaalde informatie. Als er een inhoudelijk verschil is tussen de vertalingen in verschillende talen, prevaleert de vereenvoudigd Chinese versie.

Als u een vertaalfout of onnauwkeurigheid wilt melden, neem dan gerust contact met ons op via e-mail.
