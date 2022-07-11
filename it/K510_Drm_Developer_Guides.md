![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">Guida allo sviluppo di K510 Direct Rendering Manager</font>**

<font face="黑体"  size=3>Versione del documento: P0.1.0</font>

<font face="黑体"  size=3>Data di pubblicazione: 2022-01-01</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Disconoscimento**</font>
I prodotti, i servizi o le funzionalità acquistati saranno soggetti ai contratti e ai termini commerciali di Beijing Canaan Jiesi Information Technology Co., Ltd. ("la Società", la stessa di seguito), e tutti o parte dei prodotti, servizi o funzionalità descritti in questo documento potrebbero non rientrare nell'ambito dell'acquisto o dell'utilizzo. Salvo quanto diversamente concordato nel contratto, la Società declina ogni dichiarazione o garanzia, espressa o implicita, in merito all'accuratezza, affidabilità, completezza, marketing, scopo specifico e non aggressione di qualsiasi dichiarazione, informazione o contenuto di questo documento. Salvo diverso accordo, questo documento è fornito solo come guida per l'uso.
A causa di aggiornamenti della versione del prodotto o altri motivi, il contenuto di questo documento può essere aggiornato o modificato di volta in volta senza alcun preavviso.

**<font face="黑体"  size=3>Avvisi sui marchi</font>**

""<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, l'icona "Canaan", Canaan e altri marchi di Canaan e altri marchi di Canaan sono marchi di Beijing Canaan Jiesi Information Technology Co., Ltd. Tutti gli altri marchi o marchi registrati che possono essere menzionati in questo documento sono di proprietà dei rispettivi proprietari.

**<font face="黑体"  size=3>Copyright ©2022 Pechino Canaan Jiesi Information Technology Co., Ltd</font>**
Questo documento è applicabile solo allo sviluppo e alla progettazione della piattaforma K510, senza il permesso scritto della società, nessuna unità o individuo può diffondere parte o tutto il contenuto di questo documento in qualsiasi forma.

**<font face="黑体"  size=3>Pechino Canaan Jiesi Information Technology Co., Ltd</font>**
URL: canaan-creative.com
Richieste commerciali: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# prefazione
**<font face="黑体"  size=5>Scopo </font>**del documento
Questo documento è un manuale sviluppato per Direct Rendering Manager per aiutare i tecnici a iniziare più velocemente

**<font face="黑体"  size=5>Oggetti lettore</font>**

Le principali persone a cui si applica questo documento (questa guida):

- Sviluppatori di software
- Personale di supporto tecnico

**<font face="黑体"  size=5>Cronologia delle revisioni</font>**
 <font face="宋体"  size=2>La cronologia delle revisioni accumula una descrizione di ogni aggiornamento del documento. La versione più recente del documento contiene gli aggiornamenti per tutte le versioni precedenti. </font>

| Il numero di versione   | Modificato da     | Data della revisione | Note di revisione |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 · | Gruppi di software di sistema | 2022-03-22 |          |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenuto</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Introduzione

La versione linux attualmente utilizzata da sdk è 4.17.0. Linux, nome completo GNU/Linux, è un sistema operativo UNIX-to-use e liberamente diffuso con un kernel rilasciato per la prima volta da Linus Bennadict Torvaz il 5 ottobre 1991, è principalmente ispirato alle idee di Minix e Unix, ed è un sistema operativo multi-utente, multi-tasking, multi-threaded e multi-CPU-based basato su POSIX. Esegue i principali software, applicazioni e protocolli di rete degli strumenti Unix. Supporta hardware sia a 32 bit che a 64 bit. Linux eredita la filosofia di progettazione incentrata sulla rete di Unix ed è un sistema operativo di rete multiutente stabile. Linux ha centinaia di distribuzioni diverse, come debian basata sulla comunità, archlinux e Red Hat Enterprise Linux, SUSE, Oracle Linux, ecc.

# 2 Introduzione all'hardware

## 2.1 Metodo di acquisizione

Scarica e compila l'SDK, l'SDK scaricherà e compilerà il codice Linux durante la compilazione.

Per ulteriori informazioni su come scaricare e compilare l'SDK, vedere[K510_SDK_Build_and_Burn_Guide](./K510_SDK_Build_and_Burn_Guide.md).

## 2.2 File e directory dei driver

```text
drivers/gpu/drm/canaan/
```

## 2.3 Requisiti dell'ambiente di sviluppo

non

## 2.4 Sistema operativo

Il supporto del sistema Linux e del numero di versione è illustrato nella figura seguente:

| numerazione | Risorse software | illustrare        |
| ---- | -------- | ----------- |
| 1    | Ubuntu ·   | 18.04/20.04 |
|      |          |             |
|      |          |             |
|      |          |             |

## 2.5 Ambiente software

I requisiti dell'ambiente software sono illustrati nella tabella seguente:

| numerazione | Risorse software | illustrare |
| :--- | -------- | ---- |
| 1    | K510 SDK | V1.1 |
|      |          |      |
|      |          |      |
|      |          |      |

# 3Direct Rendering Manager

## 3.1 Connessioni di riferimento

nvdia drm:<https://docs.nvidia.com/jetson/l4t-multimedia/group__direct__rendering__manager.html>

drm freedesktop:<https://cgit.freedesktop.org/mesa/drm>
<https://gitlab.freedesktop.org/mesa/drm>

## 3.2 API ufficiale drm
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

Crea un framebuffer.

La funzione crea un framebuffer con dimensioni e formato specificati, utilizzando l'oggetto buffer specificato come archivio di supporto della memoria. L'oggetto buffer può essere un "dumb buffer" creato da una chiamata a drmIoctl con il parametro request impostato su DRM_IOCTL_MODE_CREATE_DUMB oppure può essere un dma-buf importato da una chiamata alla funzione drmPrimeFDToHandle.

###### Postcondizione

Se la chiamata ha esito positivo, l'applicazione deve rimuovere (liberamente) il framebuffer chiamando drmModeRmFB.

###### Parametri

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

###### Rendiconto

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

Crea un framebuffer, specificando il formato e i piani.

Questa funzione è simile a :d rmModeAddFB, ma offre più opzioni. Il formato pixel degli oggetti buffer viene specificato in modo esplicito, invece di essere depth+bpp come in drmModeAddFB. Inoltre, sono supportati i formati YUV multiplanari. Per quanto riguarda drmModeAddFB, gli handle degli oggetti buffer possono essere buffer stupidi o dma-buf importati.

###### Postcondizione

Se la chiamata ha esito positivo, l'applicazione deve rimuovere (liberamente) il framebuffer chiamando drmModeRmFB.

###### Nota

Il parametro flags non è attualmente supportato.

###### Parametri

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

###### Rendiconto

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

Crea un framebuffer, specificando il formato e i piani.
Questa funzione è simile a :d rmModeAddFB2, ma accetta modificatori.

###### Postcondizione

Se la chiamata ha esito positivo, l'applicazione deve rimuovere (liberamente) il framebuffer chiamando drmModeRmFB.

###### Nota

###### Parametri

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

###### Rendiconto

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

Aggiunge una proprietà a una richiesta atomica.
Aggiunge una proprietà e un valore a una richiesta atomica.

###### Postcondizione

###### Nota

###### Parametri

```text
req:	     An atomic request.
object_id:	 Object ID of a CRTC, plane, or connector to be modified.
property_id: Property ID of the property to be modified.
value:	     The new value for the property.
```

###### Rendiconto

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

Esegue il commit di una richiesta di modifica della proprietà atomica nell'hardware.

Invia tutte le modifiche alle proprietà in una struttura drmModeAtomicReqPtr all'hardware.

###### Postcondizione

###### Nota

###### Parametri

```text
fd:	The file descriptor of an open DRM device.
req:	The request object describing properties to commit.
flags:	Flags which influence the operation. The supported flags are:
        DRM_MODE_PAGE_FLIP_ASYNC: Commits values immediately when possible; does not latch new properties at the next vblank.
        DRM_MODE_ATOMIC_NONBLOCK: Commits values to hardware but does not wait for hardware to accept the new values.
        DRM_MODE_ATOMIC_TEST_ONLY: Validates input, but does not commit the values to hardware.
user_data :	Unused.
```

###### Rendiconto

```text
0	if successful.
-1	if req is NULL.
-EINVAL	if DRM_CLIENT_CAP_ATOMIC is not enabled, the value of flags is illegal, or atomic property IDs in the request are not recognized.
```

##### ◆ drmModeAtomicFree()

```c
void drmModeAtomicFree	(	drmModeAtomicReqPtr 	req	)
```

Libera una richiesta atomica.

Libera un oggetto drmModeAtomicReqPtr allocato da drmModeAtomicAlloc e tutti gli oggetti drmModeAtomicReqItemPtr associati.

###### Postcondizione

###### Nota

###### Parametri

```text
req	:The atomic request object to be freed.
```

###### Rendiconto

```text
NULL
```

##### ◆ drmModeFreeConnector()

```c
void drmModeFreeConnector	(	drmModeConnectorPtr 	ptr	)
```

Libera un connettore.

Libera una struttura drmModeConnectorPtr allocata da drmModeGetConnector.

###### Postcondizione

###### Nota

###### Parametri

```text
ptr	A pointer to the connector to be freed.
```

###### Rendiconto

```text
null
```

##### ◆ drmModeFreeObjectProperties()

```c
void drmModeFreeObjectProperties	(	drmModeObjectPropertiesPtr 	ptr	)
```

Libera una struttura delle proprietà di un oggetto.

Libera una struttura drmModeObjectPropertiesPtr allocata da drmModeObjectGetProperties.

###### Postcondizione

###### Nota

###### Parametri

```text
ptr	A pointer to the object properties structure to be freed.
```

###### Rendiconto

```text
null
```

##### ◆ drmModeFreePlaneResources()

```c
void drmModeFreePlane	(	drmModePlanePtr 	ptr	)
```

Libera un aereo.

Libera una struttura drmModePlanePtr allocata da drmModeGetPlane.

###### Postcondizione

###### Nota

###### Parametri

```text
ptr	A pointer to the plane to be freed.
```

###### Rendiconto

```text
null
```

##### ◆ drmModeFreeProperty()

```c
void drmModeFreeProperty	(	drmModePropertyPtr 	ptr	)
```

Libera una struttura di proprietà.

Libera una struttura drmModePropertyPtr allocata da drmModeGetProperty.

###### Postcondizione

###### Nota

###### Parametri

```text
ptr	A pointer to a property structure returned by drmModeGetProperty.
```

###### Rendiconto

```text
null
```

##### ◆ drmModeFreeResources()

```c
void drmModeFreeResources	(	drmModeResPtr 	ptr	)
```

Libera una struttura di informazioni sulle risorse.

Libera una struttura drmModeResPtr allocata da drmModeGetResources.

###### Postcondizione

###### Nota

###### Parametri

```text
ptr	A pointer to the resource to be freed.
```

###### Rendiconto

```text
null
```

##### ◆ drmModeGetConnector()

```c
drmModeConnectorPtr drmModeGetConnector	(	int 	fd,
                                           uint32_t 	connector_id 
)
```

Ottiene informazioni per un connettore.

Se connector_id è valido, recupera una struttura drmModeConnectorPtr che contiene informazioni su un connettore, ad esempio le modalità disponibili, lo stato della connessione, il tipo di connettore e l'eventuale codificatore collegato.

###### Postcondizione

Se la chiamata ha esito positivo, l'applicazione deve liberare la struttura delle informazioni del connettore chiamando drmModeFreeConnector.

###### Nota

connector->mmWidth e connector->mmHeight sono attualmente impostati su valori segnaposto.

###### Parametri

```text
fd :	        The file descriptor of an open DRM device.
connector_id:	The connector ID of the connector to be retrieved.
```

###### Rendiconto

```text
A drmModeConnectorPtr structure if successful, or NULL if the connector is not found or the API is out of memory.
```

##### ◆ drmModeGetPlaneResources()

```c
drmModePlaneResPtr drmModeGetPlaneResources	(	int 	fd	)
```

Ottiene informazioni sugli aerei.

Ottiene un elenco di risorse del piano per un dispositivo DRM. Un'applicazione DRM in genere chiama questa funzione in anticipo per identificare i livelli di visualizzazione disponibili.

Per impostazione predefinita, le informazioni restituite includono solo i piani di tipo "Overlay" (regolari), non i piani "Primario" e "Cursore". Se DRM_CLIENT_CAP_UNIVERSAL_PLANES è stato abilitato con drmSetClientCap, le informazioni restituite includono i piani "Primari" che rappresentano i CRTC e i piani "Cursor" che rappresentano i cursori. Ciò consente di manipolare CRTC e cursori con funzioni piane come drmModeSetPlane.

###### Postcondizione

Se la chiamata ha esito positivo, l'applicazione deve liberare la struttura delle informazioni sul piano chiamando drmModeFreePlaneResources.

###### Nota

DRM attualmente non implementa piani di tipo "Cursore".

###### Parametri

```text
fd	The file descriptor of an open DRM device.
```

###### Rendiconto

```text
A drmModeResPtr structure if successful, or NULL otherwise.
```

##### ◆ drmModeGetProperty()

```c
drmModePropertyPtr drmModeGetProperty	(	int 	fd,
                                            uint32_t 	propertyId 
)
```

Ottiene una struttura di proprietà che descrive una proprietà di un oggetto DRM.

L'oggetto DRM può essere un piano, un CRTC o un connettore.

Questa funzione opera su una struttura drmModeObjectPropertiesPtr restituita da drmModeObjectGetProperties().

Le proprietà modificabili dipendono dal tipo di oggetto DRM:

1. Per un piano (tipo di oggetto DRM_MODE_OBJECT_PLANE):

    ```text
    "SRC_X", "SRC_Y", "SRC_W", "SRC_H", "zpos", "alpha" "CRTC_X",
    "CRTC_Y", "CRTC_W", "CRTC_H", "CRTC_ID", "FB_ID"
    ```

2. Per un CRTC (tipo di oggetto DRM_MODE_OBJECT_CRTC), i valori supportati sono:

    ```text
    "MODE_ID", "ACTIVE", "HDR_SUPPORTED", "HDR_METADATA_SMPTE_2086_ID"
    ```

3. Per un connettore (tipo di oggetto DRM_MODE_OBJECT_CONNECTOR), il valore supportato è:

    ```text
    "CRTC_ID"
    ```

Per i piani DRM, il campo enums contiene un elenco di coppie chiave-parola (nome: valore) che definisce le proprietà.

```c
drmModePropertyPtr->enums[ ].name
drmModePropertyPtr->enums[ ].value
```

1. I valori supportati per il campo del nome sono definiti sopra (ad esempio, "SRC_X", "SRC_Y" o "SRC_W"). Questo campo è modificabile.
2. I valori supportati per i campi valore sono:

```text
"Primary", "Overlay", "Cursor" 
```

Questo campo è di sola lettura.

Per identificare il tipo di piano, scorrere l'elenco seguente per individuare l'enumerazione il cui campo valore corrisponde a quello cercato. Quindi, ottieni il valore dal campo del nome corrispondente.

```c
drmModePropertyPtr->enums[ ] 
```

Per esempio:

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

###### Postcondizione

Se la chiamata ha esito positivo, l'applicazione deve liberare la struttura delle informazioni sulla proprietà chiamando drmModeFreeProperty.

###### Nota

Il valore zpos per un piano viene inizializzato con un offset di 10 rispetto al piano successivo. Questo per consentire una configurazione flessibile delle teste. Per esempio:

1. Tipo "Primario" Piano zpos = 10
2. Primo piano "Overlay" zpos = 20
3. Successivo "Sovrapposizione" Piano zpos = 30
4. And so on.

L'intervallo consentito per zpos è [0, 255]. Piani con valori numericamente maggiori per piani occlude zpos con valori numericamente inferiori.
Il valore alfa per un piano determina l'applicazione di una trasparenza a livello di piano e dell'alfa per pixel contenuto nell'oggetto buffer. L'intervallo consentito per alfa è [0, 255], dove 0 è completamente trasparente e 255 indica che solo alfa per pixel ha un effetto. Per i formati di pixel non alfa, non esiste un alfa per pixel, quindi 255 indica completamente opaco.

###### Parametri

```text
fd:	The file descriptor of an open DRM device.
propertyId:	Property ID of the property object to be fetched.
```

###### Rendiconto

```text
A drmModePropertyPtr if successful, or NULL otherwise.
```

##### ◆ drmModeGetResources()

```c
drmModeResPtr drmModeGetResources	(	int 	fd	)
```

Ottiene informazioni sui CRTC, i codificatori e i connettori di un dispositivo DRM.

Ottiene un elenco delle risorse principali di un dispositivo DRM. Un'applicazione DRM in genere chiama questa funzione in anticipo per identificare i display disponibili e altre risorse. Tuttavia, la funzione non segnala le risorse del piano. Questi possono essere interrogati con drmModeGetPlaneResources.

###### Postcondizione

Se la chiamata ha esito positivo, l'applicazione deve liberare la struttura delle informazioni sulle risorse chiamando drmModeFreeResources.

###### Nota

I membri min_width, min_height, max_width e max_height della struttura drmModeResPtr sono impostati su valori segnaposto.

###### Parametri

```text
fd	The file descriptor of an open DRM device.

```

###### Rendiconto

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

Ottiene tutte le proprietà di un oggetto DRM.

Ottiene una struttura delle proprietà dell'oggetto che descrive tutte le proprietà modificabili atomicamente di un oggetto DRM specificato, nonché le proprietà di sola lettura non incluse nelle strutture drmModeCrtcPtr, drmModeConnectorPtr e drmModePlanePtr corrispondenti. È quindi possibile recuperare singole proprietà con drmModeGetProperty e modificarne i valori con drmModeAtomicAddProperty.

La struttura drmModeObjectPropertiesPtr contiene una matrice di ID proprietà (props), una matrice di valori di proprietà corrispondenti (prop_values) e il numero di elementi in ogni matrice (count_props). È possibile ottenere il nome di una proprietà chiamando drmModeGetProperty nell'ID della proprietà e guardando il campo del nome della struttura drmModePropertyPtr restituito.

Per modificare una proprietà atomicamente, creare un oggetto richiesta drmModeAtomicReqPtr chiamando drmModeAtomicAlloc, quindi chiamare drmModeAtomicAddProperty, specificando l'oggetto drmModeAtomicReqPtr, l'ID oggetto dell'oggetto da modificare, l'ID proprietà della proprietà da modificare e il nuovo valore della proprietà. Quindi eseguire il commit della richiesta con drmModeAtomicCommit. È possibile impostare diverse proprietà in una richiesta atomica ed eseguirne il commit in un'unica operazione.

###### Postcondizione

Se la chiamata ha esito positivo, l'applicazione deve liberare la struttura drmModeObjectPropertiesPtr chiamando drmModeFreeObjectProperties.

###### Nota

Non tutti i tipi di oggetto sono supportati.

###### Parametri

```text
fd:	The file descriptor of an open DRM device.
object_id:	The object ID of the DRM object whose properties are to be retrieved.
object_type:	A symbol representing an object type. The following object types are supported:
    DRM_MODE_OBJECT_CRTC
    DRM_MODE_OBJECT_CONNECTOR
    DRM_MODE_OBJECT_PLANE
```

###### Rendiconto

```text
A drmModeObjectPropertiesPtr object if successful, or NULL otherwise.
```

##### ◆ drmModeRmFB()

```c
int drmModeRmFB	(	int 	fd,
                    uint32_t 	fb_id 
)
```

Distrugge un framebuffer.

Distrugge (libera) un framebuffer allocato da drmModeAddFB o drmModeAddFB2.

###### Postcondizione

###### Nota

###### Parametri

```text
fd	The file descriptor of an open DRM device.
fb_id	The ID of the framebuffer to destroy.
```

###### Rendiconto

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

Imposta una configurazione CRTC.

Se viene specificata la modalità DRM (se drm_mode non è NULL), imposta la modalità di visualizzazione sul CRTC e sui connettori specificati. Le nuove proprietà fb_id, x e y verranno impostate su vblank.

###### Postcondizione

###### Nota

I parametri fb_id, x e y accettano il valore di input speciale -1, che indica che il framebuffer della finestra hardware o l'offset corrispondente non devono essere modificati. (I driver DRM basati su kernel accettano -1 solo per fb_id. Restituiscono il codice di errore -ERANGE se viene dato -1 per x o y.)
È consentito specificare una modalità valida e fb_id==-1, anche se nessun framebuffer è attualmente collegato al CRTC. La funzione imposterà la modalità di visualizzazione ma lascerà il framebuffer CRTC indefinito.
I framebuffer impostati su un CRTC, sia da drmModeSetCrtc, drmModePageFlip o qualsiasi altro mezzo, vengono visualizzati dietro i piani. Il livello di visualizzazione CRTC è il più basso in ordine di sovrapposizione.

###### Parametri

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

###### Rendiconto

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

Modifica il framebuffer e la posizione di un piano.

###### Postcondizione

###### Nota

Il crtc_... e src_... i parametri accettano il valore di input speciale -1, che indica che il valore di offset hardware non deve essere modificato. (I driver DRM basati su kernel restituiscono il codice di errore -ERANGE quando viene assegnato questo valore.)
I framebuffer impostati sui piani vengono visualizzati sopra i CRTC. L'ordine di sovrapposizione dei piani è indicato dall'ordine in cui i piani vengono segnalati da drmModeGetPlaneResources.
Tutte le operazioni drmModeSetPlane vengono sincronizzate con vblank e vengono bloccate.

###### Parametri

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

###### Rendiconto

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

Abilita o disabilita le funzionalità (funzionalità) DRM.

###### Postcondizione

###### Nota

###### Parametri

```text

fd:	         The file descriptor of an open DRM device.
capability：	Specifies the capability to be enabled or disabled. Supported values are:
                    DRM_CLIENT_CAP_ATOMIC (disabled by default)
                    DRM_CLIENT_CAP_UNIVERSAL_PLANES (disabled by default)
value:  	 0 to disable the capability, or 1 to enable it.
```

###### Rendiconto

```text
0 if successful, or -EINVAL otherwise.
```

##### ◆ drmWaitVBlank()

```c
int drmWaitVBlank	(	int 	fd,
drmVBlankPtr 	vbl 
)
```

Attende un intervallo di blanking verticale (vblank).

Attende un vblank specificato o richiede che il gestore vblank registrato venga chiamato quando si verifica un vblank specificato.

###### Postcondizione

###### Nota

attualmente non supporta tutti i campi drmVblankPtr.

###### Parametri

```text
fd:	    The file descriptor of an open DRM device.
vbl:	A description of the requested vblank. The vbl->type field must contain one of these values:
           DRM_VBLANK_ABSOLUTE: request.sequence is the vblank count since some point in the past, e.g. system boot.
           DRM_VBLANK_RELATIVE: request.sequence is the vblank count from the current value. e.g. 1 specifies the next vblank. The value may be bitwise ORed with any combination of these values:
           DRM_VBLANK_SECONDARY: Uses the secondary display's vblank.
           DRM_VBLANK_EVENT: Returns immediately and triggers the event callback instead of waiting for a specified vblank.
```

###### Rendiconto

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

###### Postcondizione

Richiede un capovolgimento di pagina (modifica del framebuffer) sul CRTC specificato.

Pianifica un capovolgimento di pagina sul CRTC specificato. Per impostazione predefinita, il CRTC verrà riprogrammato per visualizzare il framebuffer specificato dopo il successivo aggiornamento verticale.

###### Nota

###### Parametri

```text
fd :	    The file descriptor of an open DRM device.
crtc_id :	CRTC ID of the CRTC whose framebuffer is to be changed.
fb_id :	    Framebuffer ID of the framebuffer to be displayed.
flags :	    Flags affecting the operation. Supported values are:
                  DRM_MODE_PAGE_FLIP_ASYNC: Flip immediately, not at vblank.
                  DRM_MODE_PAGE_FLIP_EVENT: Send page flip event.
user_data:	Data used by the page flip handler if vblank event was requested.
```

###### Rendiconto

```text
0	if successful.
-EINVAL	if crtc_id or fb_id is invalid.
-errno	otherwise.
```
<!-- markdownlint-enable header-increment no-hard-tabs -->
## 3.3 k510 DRM ha aggiunto una descrizione dell'uso della funzione frame

Definizione della struttura

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

Definizioni macro

```c
define DRM_KENDRYTE_DRAW_FRAME         0x00

#define DRM_IOCTL_KENDRYTE_DRAW_FRAME   DRM_IOWR(DRM_COMMAND_BASE + \
                DRM_KENDRYTE_DRAW_FRAME, struct vo_draw_frame)
```

Funzione frame

```c
static int draw_frame(struct vo_draw_frame *frame)
{
    return drmIoctl(drm_dev.fd, DRM_IOCTL_KENDRYTE_DRAW_FRAME, frame);
}
```

**Traduzione Disclaimer**  
Per la comodità dei clienti, Canaan utilizza un traduttore AI per tradurre il testo in più lingue, che possono contenere errori. Non garantiamo l'accuratezza, l'affidabilità o la tempestività delle traduzioni fornite. Canaan non sarà responsabile per eventuali perdite o danni causati dall'affidamento sull'accuratezza o sull'affidabilità delle informazioni tradotte. Se c'è una differenza di contenuto tra le traduzioni in lingue diverse, prevarrà la versione cinese semplificata.

Se desideri segnalare un errore di traduzione o un'inesattezza, non esitare a contattarci via mail.
