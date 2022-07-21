![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 Direct Rendering Manager — podręcznik programowania</font>**

<font face="黑体"  size=3>Wersja dokumentu: P0.1.0</font>

<font face="黑体"  size=3>Opublikowano: 2022-01-01</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Zrzeczenie się**</font>
Zakupione produkty, usługi lub funkcje podlegają umowom handlowym i warunkom Beijing Canaan Jiesi Information Technology Co., Ltd. ("Spółka", ta sama poniżej), a wszystkie lub część produktów, usług lub funkcji opisanych w niniejszym dokumencie może nie być objęta zakresem zakupu lub użytkowania. O ile nie uzgodniono inaczej w umowie, Firma zrzeka się wszelkich oświadczeń lub gwarancji, wyraźnych lub dorozumianych, co do dokładności, niezawodności, kompletności, marketingu, konkretnego celu i nieagresji jakichkolwiek oświadczeń, informacji lub treści tego dokumentu. O ile nie uzgodniono inaczej, niniejszy dokument jest dostarczany jako wskazówka wyłącznie do użytku.
Ze względu na aktualizacje wersji produktu lub z innych powodów zawartość tego dokumentu może być od czasu do czasu aktualizowana lub modyfikowana bez powiadomienia.

**<font face="黑体"  size=3>Informacje o znakach towarowych</font>**

""<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, ikona "Canaan", Canaan i inne znaki towarowe Canaan oraz inne znaki towarowe Canaan są znakami towarowymi Beijing Canaan Jiesi Information Technology Co., Ltd. Wszystkie inne znaki towarowe lub zarejestrowane znaki towarowe, które mogą być wymienione w niniejszym dokumencie, są własnością ich odpowiednich właścicieli.

**<font face="黑体"  size=3>Prawa autorskie ©2022 Beijing Canaan Jiesi Information Technology Co., Ltd</font>**
Niniejszy dokument ma zastosowanie wyłącznie do rozwoju i projektowania platformy K510, bez pisemnej zgody firmy, żadna jednostka ani osoba fizyczna nie może rozpowszechniać części lub całości treści tego dokumentu w jakiejkolwiek formie.

**<font face="黑体"  size=3>Pekin Canaan Jiesi Information Technology Co Ltd</font>**
Adres internetowy: canaan-creative.com
Zapytania biznesowe: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# przedmowa
**<font face="黑体"  size=5>Przeznaczenie </font>**dokumentu
Ten dokument jest podręcznikiem opracowanym dla programu Direct Rendering Manager, aby pomóc inżynierom w szybszym rozpoczęciu pracy

**<font face="黑体"  size=5>Obiekty programu Reader</font>**

Główne osoby, których dotyczy ten dokument (ten przewodnik):

- Programiści
- Personel wsparcia technicznego

**<font face="黑体"  size=5>Historia</font>**
 zmian <font face="宋体"  size=2>Historia zmian gromadzi opis każdej aktualizacji dokumentu. Najnowsza wersja dokumentu zawiera aktualizacje dla wszystkich poprzednich wersji. </font>

| Numer wersji   | Zmodyfikowane przez     | Data aktualizacji | Uwagi do poprawek |
|  :-----  |-------   |  ------  |  ------  |
| Wersja 1.0.0 | Grupy oprogramowania systemowego | 2022-03-22 |          |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Treść</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Wstęp

Wersja Linuksa obecnie używana przez sdk to 4.17.0. Linux, pełna nazwa GNU/Linux, jest darmowym i swobodnie rozpowszechnianym systemem operacyjnym podobnym do UNIX-a z jądrem wydanym po raz pierwszy przez Linusa Bennadicta Torvaza 5 października 1991 roku, jest inspirowany głównie ideami Minix i Unix, i jest wieloużytkownikowym, wielozadaniowym, wielowątkowym i opartym na wielu procesorach systemem operacyjnym opartym na POSIX. Uruchamia główne oprogramowanie narzędzi uniksowych, aplikacje i protokoły sieciowe. Obsługuje zarówno sprzęt 32-bitowy, jak i 64-bitowy. Linux dziedziczy filozofię projektowania zorientowanego na sieć Uniksa i jest stabilnym sieciowym systemem operacyjnym dla wielu użytkowników. Linux ma setki różnych dystrybucji, takich jak oparty na społeczności debian, archlinux i komercyjnie opracowany Red Hat Enterprise Linux, SUSE, Oracle Linux itp.

# 2 Wprowadzenie do sprzętu

## 2.1 Metoda nabycia

Pobierz i skompiluj SDK, SDK pobierze i skompiluje kod Linuksa podczas kompilacji.

Aby uzyskać więcej informacji na temat pobierania i kompilowania zestawu SDK, zobacz[K510_SDK_Build_and_Burn_Guide](./K510_SDK_Build_and_Burn_Guide.md).

## 2.2 Pliki i katalogi sterowników

```text
drivers/gpu/drm/canaan/
```

## 2.3 Wymagania środowiska programistycznego

nie

## 2.4 System operacyjny

Obsługa systemu Linux i numeru wersji przedstawiono na poniższym rysunku:

| numerowanie | Zasoby dotyczące oprogramowania | Ilustrują        |
| ---- | -------- | ----------- |
| 1    | Ubuntu   | 18.04/20.04 |
|      |          |             |
|      |          |             |
|      |          |             |

## 2.5 Środowisko oprogramowania

Wymagania dotyczące środowiska oprogramowania przedstawiono w poniższej tabeli:

| numerowanie | Zasoby dotyczące oprogramowania | Ilustrują |
| :--- | -------- | ---- |
| 1    | K510 SDK | wersja 1.1 |
|      |          |      |
|      |          |      |
|      |          |      |

# 3Direct Rendering Manager

## 3.1 Połączenia referencyjne

nvdia drm:<https://docs.nvidia.com/jetson/l4t-multimedia/group__direct__rendering__manager.html>

drm freedesktop:<https://cgit.freedesktop.org/mesa/drm>
<https://gitlab.freedesktop.org/mesa/drm>

## 3.2 drm oficjalne api
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

Tworzy bufor ramki.

Funkcja tworzy bufor ramki o określonym rozmiarze i formacie, używając określonego obiektu buforu jako magazynu kopii zapasowych pamięci. Obiekt buffer może być "głupim buforem" utworzonym przez wywołanie drmIoctl z parametrem request ustawionym na DRM_IOCTL_MODE_CREATE_DUMB lub może być dma-buf importowanym przez wywołanie funkcji drmPrimeFDToHandle.

###### Postcondition

Jeśli wywołanie zakończy się pomyślnie, aplikacja musi usunąć (zwolnić) bufor ramki, wywołując drmModeRmFB.

###### Parametry

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

###### Zwraca

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

Tworzy bufor ramki, określając format i płaszczyzny.

Ta funkcja jest podobna do :d rmModeAddFB, ale oferuje więcej opcji. Format pikseli obiektów bufora jest określony jawnie, a nie głębokość + bpp, jak w drmModeAddFB. Obsługiwane są również wielopłaszczyznowe formaty YUV. Jeśli chodzi o drmModeAddFB, uchwyty obiektów bufora mogą być lub importowanymi dma-bufs.

###### Postcondition

Jeśli wywołanie zakończy się pomyślnie, aplikacja musi usunąć (zwolnić) bufor ramki, wywołując drmModeRmFB.

###### Nuta

Parametr flags nie jest obecnie obsługiwany.

###### Parametry

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

###### Zwraca

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

Tworzy bufor ramki, określając format i płaszczyzny.
Ta funkcja jest podobna do :d rmModeAddFB2, ale akceptuje modyfikatory.

###### Postcondition

Jeśli wywołanie zakończy się pomyślnie, aplikacja musi usunąć (zwolnić) bufor ramki, wywołując drmModeRmFB.

###### Nuta

###### Parametry

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

###### Zwraca

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

Dodaje właściwość do żądania atomowego.
Dodaje właściwość i wartość do żądania atomowego.

###### Postcondition

###### Nuta

###### Parametry

```text
req:	     An atomic request.
object_id:	 Object ID of a CRTC, plane, or connector to be modified.
property_id: Property ID of the property to be modified.
value:	     The new value for the property.
```

###### Zwraca

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

Zatwierdza żądanie zmiany właściwości atomowej do sprzętu.

Wysyła wszystkie zmiany właściwości w strukturze drmModeAtomicReqPtr do sprzętu.

###### Postcondition

###### Nuta

###### Parametry

```text
fd:	The file descriptor of an open DRM device.
req:	The request object describing properties to commit.
flags:	Flags which influence the operation. The supported flags are:
        DRM_MODE_PAGE_FLIP_ASYNC: Commits values immediately when possible; does not latch new properties at the next vblank.
        DRM_MODE_ATOMIC_NONBLOCK: Commits values to hardware but does not wait for hardware to accept the new values.
        DRM_MODE_ATOMIC_TEST_ONLY: Validates input, but does not commit the values to hardware.
user_data :	Unused.
```

###### Zwraca

```text
0	if successful.
-1	if req is NULL.
-EINVAL	if DRM_CLIENT_CAP_ATOMIC is not enabled, the value of flags is illegal, or atomic property IDs in the request are not recognized.
```

##### ◆ drmModeAtomicFree()

```c
void drmModeAtomicFree	(	drmModeAtomicReqPtr 	req	)
```

Zwalnia żądanie atomowe.

Zwalnia obiekt drmModeAtomicReqPtr przydzielony przez drmModeAtomicAlloc i wszystkie skojarzone obiekty drmModeAtomicReqItemPtr.

###### Postcondition

###### Nuta

###### Parametry

```text
req	:The atomic request object to be freed.
```

###### Zwraca

```text
NULL
```

##### ◆ drmModeFreeConnector()

```c
void drmModeFreeConnector	(	drmModeConnectorPtr 	ptr	)
```

Zwalnia złącze.

Zwalnia strukturę drmModeConnectorPtr przydzieloną przez drmModeGetConnector.

###### Postcondition

###### Nuta

###### Parametry

```text
ptr	A pointer to the connector to be freed.
```

###### Zwraca

```text
null
```

##### ◆ drmModeFreeObjectProperties()

```c
void drmModeFreeObjectProperties	(	drmModeObjectPropertiesPtr 	ptr	)
```

Zwalnia strukturę właściwości obiektu.

Zwalnia strukturę drmModeObjectPropertiesPtr przydzieloną przez drmModeObjectGetProperties.

###### Postcondition

###### Nuta

###### Parametry

```text
ptr	A pointer to the object properties structure to be freed.
```

###### Zwraca

```text
null
```

##### ◆ drmModeFreePlaneResources()

```c
void drmModeFreePlane	(	drmModePlanePtr 	ptr	)
```

Uwalnia samolot.

Zwalnia strukturę drmModePlanePtr przydzieloną przez drmModeGetPlane.

###### Postcondition

###### Nuta

###### Parametry

```text
ptr	A pointer to the plane to be freed.
```

###### Zwraca

```text
null
```

##### ◆ drmModeFreeProperty()

```c
void drmModeFreeProperty	(	drmModePropertyPtr 	ptr	)
```

Uwalnia strukturę właściwości.

Zwalnia strukturę drmModePropertyPtr przydzieloną przez drmModeGetProperty.

###### Postcondition

###### Nuta

###### Parametry

```text
ptr	A pointer to a property structure returned by drmModeGetProperty.
```

###### Zwraca

```text
null
```

##### ◆ drmModeFreeResources()

```c
void drmModeFreeResources	(	drmModeResPtr 	ptr	)
```

Zwalnia strukturę informacji o zasobach.

Zwalnia strukturę drmModeResPtr przydzieloną przez drmModeGetResources.

###### Postcondition

###### Nuta

###### Parametry

```text
ptr	A pointer to the resource to be freed.
```

###### Zwraca

```text
null
```

##### ◆ drmModeGetConnector()

```c
drmModeConnectorPtr drmModeGetConnector	(	int 	fd,
                                           uint32_t 	connector_id 
)
```

Pobiera informacje o łączniku.

Jeśli connector_id jest prawidłowa, pobiera strukturę drmModeConnectorPtr, która zawiera informacje o złączu, takie jak dostępne tryby, stan połączenia, typ złącza i który koder (jeśli istnieje) jest podłączony.

###### Postcondition

Jeśli wywołanie zakończy się pomyślnie, aplikacja musi zwolnić strukturę informacji o łączniku, wywołując drmModeFreeConnector.

###### Nuta

connector->mmWidth i connector->mmHeight są obecnie ustawione na wartości symboli zastępczych.

###### Parametry

```text
fd :	        The file descriptor of an open DRM device.
connector_id:	The connector ID of the connector to be retrieved.
```

###### Zwraca

```text
A drmModeConnectorPtr structure if successful, or NULL if the connector is not found or the API is out of memory.
```

##### ◆ drmModeGetPlaneResources()

```c
drmModePlaneResPtr drmModeGetPlaneResources	(	int 	fd	)
```

Pobiera informacje o samolotach.

Pobiera listę zasobów płaszczyzny dla urządzenia DRM. Aplikacja DRM zazwyczaj wywołuje tę funkcję wcześnie, aby zidentyfikować dostępne warstwy wyświetlania.

Domyślnie zwracane informacje zawierają tylko płaszczyzny typu "Nakładka" (zwykłe), a nie "Podstawowe" i "Kursor". Jeśli DRM_CLIENT_CAP_UNIVERSAL_PLANES został włączony z drmSetClientCap, zwracane informacje obejmują płaszczyzny "podstawowe" reprezentujące CTRC i płaszczyzny "Kursor" reprezentujące kursory. Umożliwia to manipulowanie CRTC i kursorami za pomocą funkcji płaszczyznowych, takich jak drmModeSetPlane.

###### Postcondition

Jeśli wywołanie zakończy się pomyślnie, aplikacja musi zwolnić strukturę informacji płaszczyzny, wywołując drmModeFreePlaneResources.

###### Nuta

DRM obecnie nie implementuje płaszczyzn typu "Kursor".

###### Parametry

```text
fd	The file descriptor of an open DRM device.
```

###### Zwraca

```text
A drmModeResPtr structure if successful, or NULL otherwise.
```

##### ◆ drmModeGetProperty()

```c
drmModePropertyPtr drmModeGetProperty	(	int 	fd,
                                            uint32_t 	propertyId 
)
```

Pobiera strukturę właściwości, która opisuje właściwość obiektu DRM.

ObiektEM DRM może być płaszczyzna, CRTC lub łącznik.

Ta funkcja działa na strukturze drmModeObjectPropertiesPtr zwracanej przez drmModeObjectGetProperties().

Modyfikowalne właściwości zależą od typu obiektu DRM:

1. Dla płaszczyzny (typ obiektu DRM_MODE_OBJECT_PLANE):

    ```text
    "SRC_X", "SRC_Y", "SRC_W", "SRC_H", "zpos", "alpha" "CRTC_X",
    "CRTC_Y", "CRTC_W", "CRTC_H", "CRTC_ID", "FB_ID"
    ```

2. W przypadku CRTC (typ obiektu DRM_MODE_OBJECT_CRTC) obsługiwane wartości to:

    ```text
    "MODE_ID", "ACTIVE", "HDR_SUPPORTED", "HDR_METADATA_SMPTE_2086_ID"
    ```

3. W przypadku łącznika (typ obiektu DRM_MODE_OBJECT_CONNECTOR) obsługiwana wartość to:

    ```text
    "CRTC_ID"
    ```

W przypadku płaszczyzn DRM pole enums zawiera listę par słów kluczowych (nazwa: wartość), która definiuje właściwości.

```c
drmModePropertyPtr->enums[ ].name
drmModePropertyPtr->enums[ ].value
```

1. Obsługiwane wartości pola nazwy są zdefiniowane powyżej (np. "SRC_X", "SRC_Y" lub "SRC_W"). To pole można modyfikować.
2. Obsługiwane wartości pól wartości to:

```text
"Primary", "Overlay", "Cursor" 
```

To pole jest tylko do odczytu.

Aby zidentyfikować typ płaszczyzny, wykonaj iterację poniższej listy, aby zlokalizować enum, którego pole wartości jest zgodne z szukanym polem. Następnie pobierz wartość z odpowiedniego pola nazwy.

```c
drmModePropertyPtr->enums[ ] 
```

Na przykład:

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

Jeśli wywołanie zakończy się pomyślnie, aplikacja musi zwolnić strukturę informacji o właściwościach, wywołując drmModeFreeProperty.

###### Nuta

Wartość zpos dla płaszczyzny jest inicjowana z przesunięciem 10 względem następnej płaszczyzny. Ma to pozwolić na elastyczną konfigurację głowic. Na przykład:

1. "Podstawowy" typ Samolot zpos = 10
2. Pierwsza "nakładka" Samolot zpos = 20
3. Następna "Nakładka" Płaszczyzna zpos = 30
4. Itd.

Dozwolony zakres dla zpos to [0, 255]. Płaszczyzny o wartościach liczbowo większych dla zpos occlude płaszczyzny o liczbach mniejszych.
Wartość alfa dla płaszczyzny powoduje zastosowanie przezroczystości dla całej płaszczyzny, jak również alfa dla piksela zawarta w obiekcie buffer. Dozwolony zakres dla alfa to [0, 255], gdzie 0 jest w pełni przezroczyste, a 255 wskazuje, że tylko na piksel alfa ma wpływ. W przypadku formatów pikseli innych niż alfa nie ma alfa na piksel, więc 255 oznacza w pełni nieprzezroczysty.

###### Parametry

```text
fd:	The file descriptor of an open DRM device.
propertyId:	Property ID of the property object to be fetched.
```

###### Zwraca

```text
A drmModePropertyPtr if successful, or NULL otherwise.
```

##### ◆ drmModeGetResources()

```c
drmModeResPtr drmModeGetResources	(	int 	fd	)
```

Pobiera informacje o CRTC, koderach i złączach urządzenia DRM.

Pobiera listę głównych zasobów urządzenia DRM. Aplikacja DRM zazwyczaj wywołuje tę funkcję wcześnie, aby zidentyfikować dostępne wyświetlacze i inne zasoby. Funkcja nie raportuje jednak zasobów płaszczyzny. Można je przeszukiwać za pomocą drmModeGetPlaneResources.

###### Postcondition

Jeśli wywołanie zakończy się pomyślnie, aplikacja musi zwolnić strukturę informacji o zasobach, wywołując drmModeFreeResources.

###### Nuta

Elementy członkowskie min_width, min_height, max_width i max_height struktury drmModeResPtr są ustawiane na wartości symboli zastępczych.

###### Parametry

```text
fd	The file descriptor of an open DRM device.

```

###### Zwraca

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

Pobiera wszystkie właściwości obiektu DRM.

Pobiera strukturę właściwości obiektu, która opisuje wszystkie atomowo modyfikowalne właściwości określonego obiektu DRM, a także właściwości tylko do odczytu, które nie są zawarte w odpowiednich strukturach drmModeCrtcPtr, drmModeConnectorPtr i drmModePlanePtr. Następnie można pobrać poszczególne właściwości za pomocą drmModeGetProperty i zmienić ich wartości za pomocą drmModeAtomicAddProperty.

Struktura drmModeObjectPropertiesPtr zawiera tablicę identyfikatorów właściwości (rekwizytów), tablicę odpowiadających im wartości właściwości (prop_values) oraz liczbę elementów w każdej tablicy (count_props). Nazwę właściwości można uzyskać, wywołując drmModeGetProperty na identyfikatorze właściwości i patrząc na pole nazwy zwróconej struktury drmModePropertyPtr.

Aby zmodyfikować właściwość atomowo, utwórz obiekt żądania drmModeAtomicReqPtr, wywołując drmModeAtomicAlloc, a następnie wywołaj drmModeAtomicAddProperty, określając obiekt drmModeAtomicReqPtr, identyfikator obiektu do zmodyfikowania, identyfikator właściwości właściwości do zmodyfikowania i nową wartość właściwości. Następnie zatwierdź żądanie za pomocą drmModeAtomicCommit. Można ustawić kilka właściwości w żądaniu atomowym i zatwierdzić je w jednej operacji.

###### Postcondition

Jeśli wywołanie zakończy się pomyślnie, aplikacja musi zwolnić strukturę drmModeObjectPropertiesPtr, wywołując drmModeFreeObjectProperties.

###### Nuta

Nie wszystkie typy obiektów są obsługiwane.

###### Parametry

```text
fd:	The file descriptor of an open DRM device.
object_id:	The object ID of the DRM object whose properties are to be retrieved.
object_type:	A symbol representing an object type. The following object types are supported:
    DRM_MODE_OBJECT_CRTC
    DRM_MODE_OBJECT_CONNECTOR
    DRM_MODE_OBJECT_PLANE
```

###### Zwraca

```text
A drmModeObjectPropertiesPtr object if successful, or NULL otherwise.
```

##### ◆ drmModeRmFB()

```c
int drmModeRmFB	(	int 	fd,
                    uint32_t 	fb_id 
)
```

Niszczy bufor ramki.

Niszczy (uwalnia) bufor ramki przydzielony przez drmModeAddFB lub drmModeAddFB2.

###### Postcondition

###### Nuta

###### Parametry

```text
fd	The file descriptor of an open DRM device.
fb_id	The ID of the framebuffer to destroy.
```

###### Zwraca

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

Ustawia konfigurację CRTC.

Jeśli określono tryb DRM (jeśli drm_mode nie jest NULL), ustawia tryb wyświetlania na CRTC i określonych złączach. Nowe właściwości fb_id, x i y zostaną ustawione na vblank.

###### Postcondition

###### Nuta

Parametry fb_id, x i y akceptują specjalną wartość wejściową -1, która wskazuje, że bufor ramki okna sprzętowego lub odpowiadające mu przesunięcie nie może zostać zmienione. (Sterowniki DRM oparte na jądrze akceptują -1 tylko dla fb_id. Zwracają kod błędu -ERANGE, jeśli podano -1 dla x lub y.)
Dozwolone jest określenie prawidłowego trybu i fb_id==-1, nawet jeśli żaden bufor ramki nie jest obecnie dołączony do CRTC. Funkcja ustawi tryb wyświetlania, ale pozostawi bufor ramki CRTC niezdefiniowany.
ramek ustawione na CRTC, czy to przez drmModeSetCrtc, drmModePageFlip, czy w jakikolwiek inny sposób, są wyświetlane za płaszczyznami. Warstwa wyświetlania CRTC jest najniższa w kolejności układania.

###### Parametry

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

###### Zwraca

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

Zmienia bufor ramki i położenie płaszczyzny.

###### Postcondition

###### Nuta

Do dyspozycji Gości jest crtc_... i src_... parametry akceptują specjalną wartość wejściową -1, która wskazuje, że wartość przesunięcia sprzętowego nie ma być zmieniana. (Sterowniki DRM oparte na jądrze zwracają kod błędu -ERANGE po podaniu tej wartości).
ramek ustawione na płaszczyznach są wyświetlane na wierzchu CRTC. Kolejność układania płaszczyzn jest wskazywana przez kolejność, w jakiej samoloty są zgłaszane przez drmModeGetPlaneResources.
Wszystkie operacje drmModeSetPlane są synchronizowane z vblank i blokują.

###### Parametry

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

###### Zwraca

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

Włącza lub wyłącza funkcje (możliwości) DRM.

###### Postcondition

###### Nuta

###### Parametry

```text

fd:	         The file descriptor of an open DRM device.
capability：	Specifies the capability to be enabled or disabled. Supported values are:
                    DRM_CLIENT_CAP_ATOMIC (disabled by default)
                    DRM_CLIENT_CAP_UNIVERSAL_PLANES (disabled by default)
value:  	 0 to disable the capability, or 1 to enable it.
```

###### Zwraca

```text
0 if successful, or -EINVAL otherwise.
```

##### ◆ drmWaitVBlank()

```c
int drmWaitVBlank	(	int 	fd,
drmVBlankPtr 	vbl 
)
```

Czeka na pionowy interwał wygaszania (vblank).

Czeka na określony vblank lub żąda, aby zarejestrowany program obsługi vblank został wywołany, gdy wystąpi określony vblank.

###### Postcondition

###### Nuta

obecnie nie obsługuje wszystkich pól drmVblankPtr.

###### Parametry

```text
fd:	    The file descriptor of an open DRM device.
vbl:	A description of the requested vblank. The vbl->type field must contain one of these values:
           DRM_VBLANK_ABSOLUTE: request.sequence is the vblank count since some point in the past, e.g. system boot.
           DRM_VBLANK_RELATIVE: request.sequence is the vblank count from the current value. e.g. 1 specifies the next vblank. The value may be bitwise ORed with any combination of these values:
           DRM_VBLANK_SECONDARY: Uses the secondary display's vblank.
           DRM_VBLANK_EVENT: Returns immediately and triggers the event callback instead of waiting for a specified vblank.
```

###### Zwraca

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

Żąda przerzucania strony (zmiany bufora ramki) w określonym kodzie CRTC.

Harmonogram przerzucania strony na określonym CRTC. Domyślnie CRTC zostanie przeprogramowany tak, aby wyświetlał określony bufor ramki po następnym odświeżeniu pionowym.

###### Nuta

###### Parametry

```text
fd :	    The file descriptor of an open DRM device.
crtc_id :	CRTC ID of the CRTC whose framebuffer is to be changed.
fb_id :	    Framebuffer ID of the framebuffer to be displayed.
flags :	    Flags affecting the operation. Supported values are:
                  DRM_MODE_PAGE_FLIP_ASYNC: Flip immediately, not at vblank.
                  DRM_MODE_PAGE_FLIP_EVENT: Send page flip event.
user_data:	Data used by the page flip handler if vblank event was requested.
```

###### Zwraca

```text
0	if successful.
-EINVAL	if crtc_id or fb_id is invalid.
-errno	otherwise.
```
<!-- markdownlint-enable header-increment no-hard-tabs -->
## 3.3 k510 DRM dodano opis wykorzystania funkcji ramki

Definicja struktury

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

Definicje makr

```c
define DRM_KENDRYTE_DRAW_FRAME         0x00

#define DRM_IOCTL_KENDRYTE_DRAW_FRAME   DRM_IOWR(DRM_COMMAND_BASE + \
                DRM_KENDRYTE_DRAW_FRAME, struct vo_draw_frame)
```

Funkcja ramki

```c
static int draw_frame(struct vo_draw_frame *frame)
{
    return drmIoctl(drm_dev.fd, DRM_IOCTL_KENDRYTE_DRAW_FRAME, frame);
}
```

**Zrzeczenie się odpowiedzialności za**tłumaczenie  
Dla wygody klientów Canaan używa tłumacza AI do tłumaczenia tekstu na wiele języków, które mogą zawierać błędy. Nie gwarantujemy dokładności, rzetelności ani terminowości dostarczonych tłumaczeń. Canaan nie ponosi odpowiedzialności za jakiekolwiek straty lub szkody spowodowane poleganiem na dokładności lub wiarygodności przetłumaczonych informacji. W przypadku różnic w treści tłumaczeń w różnych językach, pierwszeństwo ma chińska wersja uproszczona.

Jeśli chcesz zgłosić błąd lub niedokładność tłumaczenia, skontaktuj się z nami pocztą.
