![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 Direct Rendering Manager Entwicklungshandbuch</font>**

<font face="黑体"  size=3>Dokumentversion: P0.1.0</font>

<font face="黑体"  size=3>Veröffentlicht: 2022-01-01</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Verzichtserklärung**</font>
Die Produkte, Dienstleistungen oder Funktionen, die Sie erwerben, unterliegen den kommerziellen Verträgen und Bedingungen von Beijing Canaan Jiesi Information Technology Co., Ltd. ("das Unternehmen", dasselbe im Folgenden), und alle oder ein Teil der in diesem Dokument beschriebenen Produkte, Dienstleistungen oder Funktionen fallen möglicherweise nicht in den Rahmen Ihres Kaufs oder Ihrer Nutzung. Sofern im Vertrag nicht anders vereinbart, lehnt das Unternehmen alle ausdrücklichen oder stillschweigenden Zusicherungen oder Gewährleistungen hinsichtlich der Genauigkeit, Zuverlässigkeit, Vollständigkeit, des Marketings, des spezifischen Zwecks und der Nichtverletzung von Zusicherungen, Informationen oder Inhalten dieses Dokuments ab. Sofern nicht anders vereinbart, wird dieses Dokument nur als Leitfaden für die Verwendung zur Verfügung gestellt.
Aufgrund von Produktversions-Upgrades oder anderen Gründen kann der Inhalt dieses Dokuments von Zeit zu Zeit ohne vorherige Ankündigung aktualisiert oder geändert werden.

**<font face="黑体"  size=3>Markenhinweise</font>**

"", "Canaan"-Symbol, Canaan und andere Marken von Canaan und andere Marken von Canaan <img src="../zh/images/canaan-logo.png" style="zoom:33%;" />sind Marken von Beijing Canaan Jiesi Information Technology Co., Ltd. Alle anderen Marken oder eingetragenen Warenzeichen, die in diesem Dokument erwähnt werden können, sind Eigentum ihrer jeweiligen Inhaber.

**<font face="黑体"  size=3>Copyright ©2022 Peking Canaan Jiesi Information Technology Co., Ltd</font>**
Dieses Dokument gilt nur für die Entwicklung und das Design der K510-Plattform, ohne die schriftliche Genehmigung des Unternehmens darf keine Einheit oder Einzelperson einen Teil oder den gesamten Inhalt dieses Dokuments in irgendeiner Form verbreiten.

**<font face="黑体"  size=3>Peking Canaan Jiesi Informationstechnologie Co., Ltd</font>**
URL: canaan-creative.com
Geschäftliche Anfragen: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# Vorwort
**<font face="黑体"  size=5>Zweck des Dokuments</font>**
Dieses Dokument ist ein Handbuch, das für Direct Rendering Manager entwickelt wurde, um Ingenieuren einen schnelleren Einstieg zu erleichtern.

**<font face="黑体"  size=5>Reader-Objekte</font>**

Die wichtigsten Personen, für die sich dieses Dokument (dieser Leitfaden) richtet:

- Softwareentwickler
- Mitarbeiter des technischen Supports

**<font face="黑体"  size=5>Revisionshistorie</font>**
 <font face="宋体"  size=2>In der Revisionshistorie wird eine Beschreibung jeder Dokumentaktualisierung gesammelt. Die neueste Version des Dokuments enthält Updates für alle vorherigen Versionen. </font>

| Die Versionsnummer   | Geändert von     | Datum der Überarbeitung | Revisionshinweise |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | Systemsoftwaregruppen | 2022-03-22 |          |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Inhalt</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Einleitung

Die derzeit von sdk verwendete Linux-Version ist 4.17.0. Linux, voller Name GNU/Linux, ist ein frei verwendbares und frei verbreitetes UNIX-ähnliches Betriebssystem mit einem Kernel, der erstmals am 5. Oktober 1991 von Linus Bennadict Torvaz veröffentlicht wurde, es ist hauptsächlich von den Ideen von Minix und Unix inspiriert und ist ein Multi-User-, Multi-Tasking-, Multi-Threaded- und Multi-CPU-basiertes Betriebssystem, das auf POSIX basiert. Es führt die wichtigsten Unix-Tool-Software, Anwendungen und Netzwerkprotokolle aus. Es unterstützt sowohl 32-Bit- als auch 64-Bit-Hardware. Linux erbt die netzwerkzentrierte Designphilosophie von Unix und ist ein stabiles Multi-User-Netzwerkbetriebssystem. Linux hat Hunderte von verschiedenen Distributionen, wie Community-basiertes Debian, ArchLinux und kommerziell entwickeltes Red Hat Enterprise Linux, SUSE, Oracle Linux usw.

# 2 Hardware-Einführung

## 2.1 Erfassungsmethode

Laden Sie das SDK herunter und kompilieren Sie es, das SDK lädt den Linux-Code beim Kompilieren herunter und kompiliert ihn.

Weitere Informationen zum Herunterladen und Kompilieren des SDK finden Sie unter[K510_SDK_Build_and_Burn_Guide](./K510_SDK_Build_and_Burn_Guide.md).

## 2.2 Treiberdateien und -verzeichnisse

```text
drivers/gpu/drm/canaan/
```

## 2.3 Anforderungen an die Entwicklungsumgebung

nicht

## 2.4 Betriebssystem

Die Unterstützung von Linux-Systemen und Versionsnummern ist in der folgenden Abbildung dargestellt:

| Nummerierung | Software-Ressourcen | illustrieren        |
| ---- | -------- | ----------- |
| 1    | Ubuntu   | 18.04/20.04 |
|      |          |             |
|      |          |             |
|      |          |             |

## 2.5 Software-Umgebung

Die Anforderungen an die Softwareumgebung sind in der folgenden Tabelle aufgeführt:

| Nummerierung | Software-Ressourcen | illustrieren |
| :--- | -------- | ---- |
| 1    | K510 SDK | V1.1 |
|      |          |      |
|      |          |      |
|      |          |      |

# 3Direct-Rendering-Manager

## 3.1 Referenzverbindungen

NVDIA DRM:<https://docs.nvidia.com/jetson/l4t-multimedia/group__direct__rendering__manager.html>

DRM Freedesktop:<https://cgit.freedesktop.org/mesa/drm>
<https://gitlab.freedesktop.org/mesa/drm>

## 3.2 Offizielle DRM-API
<!-- markdownlint-disable header-increment no-hard-tabs -->
##### ◆ drmModeAddFB ()

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

Erstellt einen Framebuffer.

Die Funktion erstellt einen Framebuffer mit einer angegebenen Größe und einem angegebenen Format, wobei das angegebene Pufferobjekt als Speicher-Backing-Speicher verwendet wird. Das Pufferobjekt kann ein "dummer Puffer" sein, der durch einen Aufruf von drmIoctl mit dem auf DRM_IOCTL_MODE_CREATE_DUMB festgelegten Anforderungsparameter erstellt wird, oder es kann ein dma-buf sein, der durch einen Aufruf der drmPrimeFDToHandle-Funktion importiert wird.

###### Nachbedingung

Wenn der Aufruf erfolgreich ist, muss die Anwendung den Framebuffer entfernen (freigeben), indem sie drmModeRmFB aufruft.

###### Parameter

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

###### Ertrag

```text
0 if framebuffer creation is successful, or -1 otherwise.
```

##### ◆ drmModeAddFB2 ()

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

Erstellt einen Framebuffer und gibt Format und Ebenen an.

Diese Funktion ähnelt :d rmModeAddFB, bietet jedoch weitere Optionen. Das Pixelformat der Pufferobjekte wird explizit angegeben, anstatt wie in drmModeAddFB depth+bpp zu sein. Außerdem werden multiplanare YUV-Formate unterstützt. Wie bei drmModeAddFB können die Pufferobjekt-Handles ein dummer Puffer oder importierte dma-bufs sein.

###### Nachbedingung

Wenn der Aufruf erfolgreich ist, muss die Anwendung den Framebuffer entfernen (freigeben), indem sie drmModeRmFB aufruft.

###### Anmerkung

Der Parameter flags wird derzeit nicht unterstützt.

###### Parameter

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

###### Ertrag

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

Erstellt einen Framebuffer und gibt Format und Ebenen an.
Diese Funktion ähnelt :d rmModeAddFB2, akzeptiert jedoch Modifikatoren.

###### Nachbedingung

Wenn der Aufruf erfolgreich ist, muss die Anwendung den Framebuffer entfernen (freigeben), indem sie drmModeRmFB aufruft.

###### Anmerkung

###### Parameter

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

###### Ertrag

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

Fügt einer atomaren Anforderung eine Eigenschaft hinzu.
Fügt einer atomaren Anforderung eine Eigenschaft und einen Wert hinzu.

###### Nachbedingung

###### Anmerkung

###### Parameter

```text
req:	     An atomic request.
object_id:	 Object ID of a CRTC, plane, or connector to be modified.
property_id: Property ID of the property to be modified.
value:	     The new value for the property.
```

###### Ertrag

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

Schreibt eine atomare Eigenschaftsänderungsanforderung an die Hardware fest.

Sendet alle Eigenschaftsänderungen in einer drmModeAtomicReqPtr-Struktur an die Hardware.

###### Nachbedingung

###### Anmerkung

###### Parameter

```text
fd:	The file descriptor of an open DRM device.
req:	The request object describing properties to commit.
flags:	Flags which influence the operation. The supported flags are:
        DRM_MODE_PAGE_FLIP_ASYNC: Commits values immediately when possible; does not latch new properties at the next vblank.
        DRM_MODE_ATOMIC_NONBLOCK: Commits values to hardware but does not wait for hardware to accept the new values.
        DRM_MODE_ATOMIC_TEST_ONLY: Validates input, but does not commit the values to hardware.
user_data :	Unused.
```

###### Ertrag

```text
0	if successful.
-1	if req is NULL.
-EINVAL	if DRM_CLIENT_CAP_ATOMIC is not enabled, the value of flags is illegal, or atomic property IDs in the request are not recognized.
```

##### ◆ drmModeAtomicFree()

```c
void drmModeAtomicFree	(	drmModeAtomicReqPtr 	req	)
```

Gibt eine atomare Anforderung frei.

Gibt ein von drmModeAtomicAlloc zugewiesenes drmModeAtomicReqPtr-Objekt und alle zugeordneten drmModeAtomicReqItemPtr-Objekte frei.

###### Nachbedingung

###### Anmerkung

###### Parameter

```text
req	:The atomic request object to be freed.
```

###### Ertrag

```text
NULL
```

##### ◆ drmModeFreeConnector()

```c
void drmModeFreeConnector	(	drmModeConnectorPtr 	ptr	)
```

Gibt einen Stecker frei.

Gibt eine von drmModeGetConnector zugewiesene drmModeConnectorPtr-Struktur frei.

###### Nachbedingung

###### Anmerkung

###### Parameter

```text
ptr	A pointer to the connector to be freed.
```

###### Ertrag

```text
null
```

##### ◆ drmModeFreeObjectProperties()

```c
void drmModeFreeObjectProperties	(	drmModeObjectPropertiesPtr 	ptr	)
```

Gibt eine Objekteigenschaftenstruktur frei.

Gibt eine drmModeObjectPropertiesPtr-Struktur frei, die von drmModeObjectGetProperties zugewiesen wurde.

###### Nachbedingung

###### Anmerkung

###### Parameter

```text
ptr	A pointer to the object properties structure to be freed.
```

###### Ertrag

```text
null
```

##### ◆ drmModeFreePlaneResources()

```c
void drmModeFreePlane	(	drmModePlanePtr 	ptr	)
```

Befreit ein Flugzeug.

Gibt eine drmModePlanePtr-Struktur frei, die von drmModeGetPlane zugewiesen wurde.

###### Nachbedingung

###### Anmerkung

###### Parameter

```text
ptr	A pointer to the plane to be freed.
```

###### Ertrag

```text
null
```

##### ◆ drmModeFreeProperty()

```c
void drmModeFreeProperty	(	drmModePropertyPtr 	ptr	)
```

Gibt eine Eigenschaftsstruktur frei.

Gibt eine drmModePropertyPtr-Struktur frei, die von drmModeGetProperty zugewiesen wurde.

###### Nachbedingung

###### Anmerkung

###### Parameter

```text
ptr	A pointer to a property structure returned by drmModeGetProperty.
```

###### Ertrag

```text
null
```

##### ◆ drmModeFreeResources()

```c
void drmModeFreeResources	(	drmModeResPtr 	ptr	)
```

Gibt eine Ressourceninformationsstruktur frei.

Gibt eine drmModeResPtr-Struktur frei, die von drmModeGetResources zugewiesen wurde.

###### Nachbedingung

###### Anmerkung

###### Parameter

```text
ptr	A pointer to the resource to be freed.
```

###### Ertrag

```text
null
```

##### ◆ drmModeGetConnector()

```c
drmModeConnectorPtr drmModeGetConnector	(	int 	fd,
                                           uint32_t 	connector_id 
)
```

Ruft Informationen für einen Connector ab.

Wenn connector_id gültig ist, ruft eine drmModeConnectorPtr-Struktur ab, die Informationen zu einem Konnektor enthält, z. B. verfügbare Modi, Verbindungsstatus, Konnektortyp und welcher Encoder (falls vorhanden) angeschlossen ist.

###### Nachbedingung

Wenn der Aufruf erfolgreich ist, muss die Anwendung die Connectorinformationsstruktur durch Aufrufen von drmModeFreeConnector freigeben.

###### Anmerkung

connector->mmWidth und connector->mmHeight sind derzeit auf Platzhalterwerte festgelegt.

###### Parameter

```text
fd :	        The file descriptor of an open DRM device.
connector_id:	The connector ID of the connector to be retrieved.
```

###### Ertrag

```text
A drmModeConnectorPtr structure if successful, or NULL if the connector is not found or the API is out of memory.
```

##### ◆ drmModeGetPlaneResources()

```c
drmModePlaneResPtr drmModeGetPlaneResources	(	int 	fd	)
```

Ruft Informationen zu Ebenen ab.

Ruft eine Liste der Ebenenressourcen für ein DRM-Gerät ab. Eine DRM-Anwendung ruft diese Funktion in der Regel frühzeitig auf, um die verfügbaren Anzeigeschichten zu identifizieren.

Standardmäßig enthalten die zurückgegebenen Informationen nur (reguläre) Ebenen vom Typ "Overlay" – nicht "Primäre" und "Cursor"-Ebenen. Wenn DRM_CLIENT_CAP_UNIVERSAL_PLANES mit drmSetClientCap aktiviert wurde, umfassen die zurückgegebenen Informationen "Primäre" Ebenen, die CTRCs darstellen, und "Cursor"-Ebenen, die Cursor darstellen. Dadurch können CRTCs und Cursor mit Ebenenfunktionen wie drmModeSetPlane bearbeitet werden.

###### Nachbedingung

Wenn der Aufruf erfolgreich ist, muss die Anwendung die Ebeneninformationsstruktur durch Aufrufen von drmModeFreePlaneResources freigeben.

###### Anmerkung

DRM implementiert derzeit keine Ebenen vom Typ "Cursor".

###### Parameter

```text
fd	The file descriptor of an open DRM device.
```

###### Ertrag

```text
A drmModeResPtr structure if successful, or NULL otherwise.
```

##### ◆ drmModeGetProperty()

```c
drmModePropertyPtr drmModeGetProperty	(	int 	fd,
                                            uint32_t 	propertyId 
)
```

Ruft eine Eigenschaftsstruktur ab, die eine Eigenschaft eines DRM-Objekts beschreibt.

Das DRM-Objekt kann eine Ebene, eine CRTC oder ein Konnektor sein.

Diese Funktion arbeitet mit einer drmModeObjectPropertiesPtr-Struktur, die von drmModeObjectGetProperties() zurückgegeben wird.

Die veränderbaren Eigenschaften hängen vom DRM-Objekttyp ab:

1. Für eine Ebene (Objekttyp DRM_MODE_OBJECT_PLANE):

    ```text
    "SRC_X", "SRC_Y", "SRC_W", "SRC_H", "zpos", "alpha" "CRTC_X",
    "CRTC_Y", "CRTC_W", "CRTC_H", "CRTC_ID", "FB_ID"
    ```

2. Für eine CRTC (Objekttyp DRM_MODE_OBJECT_CRTC) werden folgende Werte unterstützt:

    ```text
    "MODE_ID", "ACTIVE", "HDR_SUPPORTED", "HDR_METADATA_SMPTE_2086_ID"
    ```

3. Für einen Konnektor (Objekttyp DRM_MODE_OBJECT_CONNECTOR) lautet der unterstützte Wert:

    ```text
    "CRTC_ID"
    ```

Für DRM-Ebenen enthält das Feld für Enumerationen eine Liste von Schlüsselwortpaaren (name: Wert), die die Eigenschaften definieren.

```c
drmModePropertyPtr->enums[ ].name
drmModePropertyPtr->enums[ ].value
```

1. Unterstützte Werte für das Namensfeld sind oben definiert (z. B. "SRC_X", "SRC_Y" oder "SRC_W"). Dieses Feld ist änderbar.
2. Unterstützte Werte für die Wertfelder sind:

```text
"Primary", "Overlay", "Cursor" 
```

Dieses Feld ist schreibgeschützt.

Um den Ebenentyp zu identifizieren, durchlaufen Sie die folgende Liste, um die Enumeration zu finden, deren Wertfeld mit dem gesuchten übereinstimmt. Rufen Sie dann den Wert aus dem entsprechenden Namensfeld ab.

```c
drmModePropertyPtr->enums[ ] 
```

Zum Beispiel:

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

###### Nachbedingung

Wenn der Aufruf erfolgreich ist, muss die Anwendung die Eigenschaftsinformationsstruktur durch Aufrufen von drmModeFreeProperty freigeben.

###### Anmerkung

Der zpos-Wert für eine Ebene wird mit einem Offset von 10 relativ zur nächsten Ebene initialisiert. Dies soll eine flexible Konfiguration der Köpfe ermöglichen. Zum Beispiel:

1. "Primärer" Typ Flugzeug zpos = 10
2. Erste "Overlay"-Ebene zpos = 20
3. Nächstes "Overlay" Ebene zpos = 30
4. Etc.

Der zulässige Bereich für zpos ist [0, 255]. Ebenen mit numerisch größeren Werten für zPOs schließen Ebenen mit numerisch kleineren Werten aus.
Der Alphawert für eine Ebene bewirkt, dass eine ebenenweite Transparenz sowie das im Pufferobjekt enthaltene Alpha pro Pixel angewendet wird. Der zulässige Bereich für Alpha  ist , [0, 255]wobei 0 vollständig transparent ist und 255 angibt, dass nur Alpha pro Pixel einen Effekt hat. Bei Nicht-Alphapixelformaten gibt es kein Alpha pro Pixel, daher zeigt 255 vollständig undurchsichtig an.

###### Parameter

```text
fd:	The file descriptor of an open DRM device.
propertyId:	Property ID of the property object to be fetched.
```

###### Ertrag

```text
A drmModePropertyPtr if successful, or NULL otherwise.
```

##### ◆ drmModeGetResources()

```c
drmModeResPtr drmModeGetResources	(	int 	fd	)
```

Ruft Informationen zu den CRTCs, Encodern und Anschlüssen eines DRM-Geräts ab.

Ruft eine Liste der wichtigsten Ressourcen eines DRM-Geräts ab. Eine DRM-Anwendung ruft diese Funktion in der Regel frühzeitig auf, um verfügbare Anzeigen und andere Ressourcen zu identifizieren. Die Funktion meldet jedoch keine ebenen Ressourcen. Diese können mit drmModeGetPlaneResources abgefragt werden.

###### Nachbedingung

Wenn der Aufruf erfolgreich ist, muss die Anwendung die Ressourceninformationsstruktur durch Aufrufen von drmModeFreeResources freigeben.

###### Anmerkung

Die min_width, min_height, max_width und max_height Member der drmModeResPtr-Struktur werden auf Platzhalterwerte festgelegt.

###### Parameter

```text
fd	The file descriptor of an open DRM device.

```

###### Ertrag

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

Ruft alle Eigenschaften eines DRM-Objekts ab.

Ruft eine Objekteigenschaftenstruktur ab, die alle atomar veränderbaren Eigenschaften eines angegebenen DRM-Objekts sowie schreibgeschützte Eigenschaften beschreibt, die nicht in den entsprechenden drmModeCrtcPtr-, drmModeConnectorPtr- und drmModePlanePtr-Strukturen enthalten sind. Anschließend können Sie einzelne Eigenschaften mit drmModeGetProperty abrufen und ihre Werte mit drmModeAtomicAddProperty ändern.

Die drmModeObjectPropertiesPtr-Struktur enthält ein Array von Eigenschafts-IDs (props), ein Array entsprechender Eigenschaftswerte (prop_values) und die Anzahl der Elemente in jedem Array (count_props). Sie können den Namen einer Eigenschaft abrufen, indem Sie drmModeGetProperty für die Eigenschafts-ID aufrufen und sich das Namensfeld der zurückgegebenen drmModePropertyPtr-Struktur ansehen.

Um eine Eigenschaft atomar zu ändern, erstellen Sie ein drmModeAtomicReqPtr-Anforderungsobjekt, indem Sie drmModeAtomicAlloc aufrufen, und rufen Sie dann drmModeAtomicAddProperty auf, wobei Sie das drmModeAtomicReqPtr-Objekt, die Objekt-ID des zu ändernden Objekts, die Eigenschafts-ID der zu ändernden Eigenschaft und den neuen Wert der Eigenschaft angeben. Führen Sie dann einen Commit für die Anforderung mit drmModeAtomicCommit aus. Sie können mehrere Eigenschaften in einer atomaren Anforderung festlegen und sie in einem einzigen Vorgang festschreiben.

###### Nachbedingung

Wenn der Aufruf erfolgreich ist, muss die Anwendung die drmModeObjectPropertiesPtr-Struktur durch Aufrufen von drmModeFreeObjectProperties freigeben.

###### Anmerkung

Nicht alle Objekttypen werden unterstützt.

###### Parameter

```text
fd:	The file descriptor of an open DRM device.
object_id:	The object ID of the DRM object whose properties are to be retrieved.
object_type:	A symbol representing an object type. The following object types are supported:
    DRM_MODE_OBJECT_CRTC
    DRM_MODE_OBJECT_CONNECTOR
    DRM_MODE_OBJECT_PLANE
```

###### Ertrag

```text
A drmModeObjectPropertiesPtr object if successful, or NULL otherwise.
```

##### ◆ drmModeRmFB()

```c
int drmModeRmFB	(	int 	fd,
                    uint32_t 	fb_id 
)
```

Zerstört einen Framebuffer.

Zerstört (befreit) einen Framebuffer, der von drmModeAddFB oder drmModeAddFB2 zugewiesen wurde.

###### Nachbedingung

###### Anmerkung

###### Parameter

```text
fd	The file descriptor of an open DRM device.
fb_id	The ID of the framebuffer to destroy.
```

###### Ertrag

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

Legt eine CRTC-Konfiguration fest.

Wenn der DRM-Modus angegeben ist (wenn drm_mode nicht NULL ist), legt den Anzeigemodus auf der CRTC und die angegebenen Konnektoren fest. Neue Eigenschaften fb_id, x und y werden auf vblank festgelegt.

###### Nachbedingung

###### Anmerkung

Die Parameter fb_id, x und y akzeptieren den speziellen Eingabewert -1, der angibt, dass der Hardwarefenster-Framebuffer oder der entsprechende Offset nicht verändert werden soll. (Kernel-basierte DRM-Treiber akzeptieren -1 nur für fb_id. Sie geben den Fehlercode -ERANGE zurück, wenn -1 für x oder y angegeben wird.)
Es ist erlaubt, einen gültigen Modus und fb_id==-1 anzugeben, auch wenn derzeit kein Framebuffer an die CRTC angehängt ist. Die Funktion stellt den Anzeigemodus ein, lässt aber den CRTC-Framebuffer undefiniert.
Framebuffer, die auf einer CRTC festgelegt wurden, unabhängig davon, ob sie von drmModeSetCrtc, drmModePageFlip oder auf andere Weise festgelegt wurden, werden hinter Ebenen angezeigt. Die CRTC-Anzeigeschicht ist die niedrigste in der Stapelreihenfolge.

###### Parameter

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

###### Ertrag

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

Ändert den Framebuffer und die Position einer Ebene.

###### Nachbedingung

###### Anmerkung

Die crtc_... und src_... -Parameter akzeptieren den speziellen Eingabewert -1, der angibt, dass der Hardware-Offset-Wert nicht geändert werden soll. (Kernelbasierte DRM-Treiber geben den Fehlercode -ERANGE zurück, wenn dieser Wert angegeben wird.)
Auf Ebenen festgelegte Framebuffer werden über CRTCs angezeigt. Die Stapelreihenfolge von Ebenen wird durch die Reihenfolge angegeben, in der die Ebenen von drmModeGetPlaneResources gemeldet werden.
Alle drmModeSetPlane-Vorgänge werden mit vblank synchronisiert und blockiert.

###### Parameter

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

###### Ertrag

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

Aktiviert oder deaktiviert DRM-Features (-Funktionen).

###### Nachbedingung

###### Anmerkung

###### Parameter

```text

fd:	         The file descriptor of an open DRM device.
capability：	Specifies the capability to be enabled or disabled. Supported values are:
                    DRM_CLIENT_CAP_ATOMIC (disabled by default)
                    DRM_CLIENT_CAP_UNIVERSAL_PLANES (disabled by default)
value:  	 0 to disable the capability, or 1 to enable it.
```

###### Ertrag

```text
0 if successful, or -EINVAL otherwise.
```

##### ◆ drmWaitVBlank()

```c
int drmWaitVBlank	(	int 	fd,
drmVBlankPtr 	vbl 
)
```

Wartet auf ein vertikales Ausblendintervall (Vblank).

Wartet auf ein angegebenes Vblank oder fordert an, dass der registrierte Vblank-Handler aufgerufen wird, wenn ein angegebenes Vblank auftritt.

###### Nachbedingung

###### Anmerkung

unterstützt derzeit nicht alle drmVblankPtr-Felder.

###### Parameter

```text
fd:	    The file descriptor of an open DRM device.
vbl:	A description of the requested vblank. The vbl->type field must contain one of these values:
           DRM_VBLANK_ABSOLUTE: request.sequence is the vblank count since some point in the past, e.g. system boot.
           DRM_VBLANK_RELATIVE: request.sequence is the vblank count from the current value. e.g. 1 specifies the next vblank. The value may be bitwise ORed with any combination of these values:
           DRM_VBLANK_SECONDARY: Uses the secondary display's vblank.
           DRM_VBLANK_EVENT: Returns immediately and triggers the event callback instead of waiting for a specified vblank.
```

###### Ertrag

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

###### Nachbedingung

Fordert einen Seitenwechsel (Framebuffer-Änderung) für die angegebene CRTC an.

Plant einen Seitenwechsel in der angegebenen CRTC. Standardmäßig wird die CRTC neu programmiert, um den angegebenen Framebuffer nach der nächsten vertikalen Aktualisierung anzuzeigen.

###### Anmerkung

###### Parameter

```text
fd :	    The file descriptor of an open DRM device.
crtc_id :	CRTC ID of the CRTC whose framebuffer is to be changed.
fb_id :	    Framebuffer ID of the framebuffer to be displayed.
flags :	    Flags affecting the operation. Supported values are:
                  DRM_MODE_PAGE_FLIP_ASYNC: Flip immediately, not at vblank.
                  DRM_MODE_PAGE_FLIP_EVENT: Send page flip event.
user_data:	Data used by the page flip handler if vblank event was requested.
```

###### Ertrag

```text
0	if successful.
-EINVAL	if crtc_id or fb_id is invalid.
-errno	otherwise.
```
<!-- markdownlint-enable header-increment no-hard-tabs -->
## 3.3 k510 DRM hat eine Beschreibung der Verwendung der Rahmenfunktion hinzugefügt

Strukturdefinition

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

Makrodefinitionen

```c
define DRM_KENDRYTE_DRAW_FRAME         0x00

#define DRM_IOCTL_KENDRYTE_DRAW_FRAME   DRM_IOWR(DRM_COMMAND_BASE + \
                DRM_KENDRYTE_DRAW_FRAME, struct vo_draw_frame)
```

Frame-Funktion

```c
static int draw_frame(struct vo_draw_frame *frame)
{
    return drmIoctl(drm_dev.fd, DRM_IOCTL_KENDRYTE_DRAW_FRAME, frame);
}
```

**Haftungsausschluss**für Übersetzungen  
Für die Bequemlichkeit der Kunden verwendet Canaan einen KI-Übersetzer, um Text in mehrere Sprachen zu übersetzen, die Fehler enthalten können. Wir übernehmen keine Gewähr für die Genauigkeit, Zuverlässigkeit oder Aktualität der bereitgestellten Übersetzungen. Canaan haftet nicht für Verluste oder Schäden, die durch das Vertrauen auf die Richtigkeit oder Zuverlässigkeit der übersetzten Informationen verursacht werden. Wenn es einen inhaltlichen Unterschied zwischen den Übersetzungen in verschiedenen Sprachen gibt, ist die vereinfachte chinesische Version maßgebend.

Wenn Sie einen Übersetzungsfehler oder eine Ungenauigkeit melden möchten, können Sie uns gerne per E-Mail kontaktieren.
