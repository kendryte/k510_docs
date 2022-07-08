![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 Direct Rendering Manager Guía de desarrollo</font>**

<font face="黑体"  size=3>Versión del documento: P0.1.0</font>

<font face="黑体"  size=3>Publicado: 2022-01-01</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Renuncia**</font>
Los productos, servicios o características que compre estarán sujetos a los contratos comerciales y términos de Beijing Canaan Jiesi Information Technology Co., Ltd. ("la Compañía", la misma en adelante), y todos o parte de los productos, servicios o características descritos en este documento pueden no estar dentro del alcance de su compra o uso. Salvo que se acuerde lo contrario en el contrato, la Compañía renuncia a todas las representaciones o garantías, expresas o implícitas, en cuanto a la precisión, confiabilidad, integridad, marketing, propósito específico y no agresión de cualquier representación, información o contenido de este documento. A menos que se acuerde lo contrario, este documento se proporciona como una guía para su uso solamente.
Debido a actualizaciones de la versión del producto u otras razones, el contenido de este documento puede actualizarse o modificarse de vez en cuando sin previo aviso. 

**<font face="黑体"  size=3>Avisos de marcas comerciales</font>**

""<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, el icono de "Canaan", Canaan y otras marcas comerciales de Canaan y otras marcas comerciales de Canaan son marcas comerciales de Beijing Canaan Jiesi Information Technology Co., Ltd. Todas las demás marcas comerciales o marcas registradas que puedan mencionarse en este documento son propiedad de sus respectivos propietarios. 

**<font face="黑体"  size=3>Derechos de autor ©2022 Beijing Canaan Jiesi Information Technology Co., Ltd</font>**
Este documento solo es aplicable al desarrollo y diseño de la plataforma K510, sin el permiso por escrito de la empresa, ninguna unidad o individuo puede difundir parte o la totalidad del contenido de este documento en ninguna forma. 

**<font face="黑体"  size=3>Beijing Canaan Jiesi Información Technology Co., Ltd</font>**
URL: canaan-creative.com
Consultas comerciales: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# prefacio
**<font face="黑体"  size=5>Propósito del documento</font>**
Este documento es un manual desarrollado para Direct Rendering Manager para ayudar a los ingenieros a comenzar más rápido

**<font face="黑体"  size=5>Objetos reader</font>**

Las principales personas a las que se aplica este documento (esta guía):

- Desarrolladores de software
- Personal de soporte técnico

**<font face="黑体"  size=5>Historial 
 </font>**de revisiones <font face="宋体"  size=2>El historial de revisiones acumula una descripción de cada actualización del documento. La versión más reciente del documento contiene actualizaciones para todas las versiones anteriores. </font>

| El número de versión   | Modificado por     | Fecha de revisión | Notas de revisión |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | Grupos de software del sistema | 2022-03-22 |          |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenido</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Introducción

La versión de Linux utilizada actualmente por el sdk es 4.17.0. Linux, nombre completo GNU/Linux, es un sistema operativo tipo UNIX de uso libre y libre difusión con un kernel lanzado por primera vez por Linus Bennadict Torvaz el 5 de octubre de 1991, se inspira principalmente en las ideas de Minix y Unix, y es un sistema operativo multiusuario, multitarea, multihilo y multifutable basado en POSIX. Ejecuta el principal software de herramientas Unix, aplicaciones y protocolos de red. Es compatible con hardware de 32 bits y 64 bits. Linux hereda la filosofía de diseño centrada en la red de Unix y es un sistema operativo de red multiusuario estable. Linux tiene cientos de distribuciones diferentes, como debian basado en la comunidad, archlinux y Red Hat Enterprise Linux, SUSE, Oracle Linux, etc. desarrollados comercialmente.

Direct Rendering Manager es un subsistema [del kernel de Linux](https://en.wikipedia.org/wiki/Linux_kernel) que es responsable[ de la conexión de la GPU a ](https://en.wikipedia.org/wiki/Video_cards)[las tarjetas de video modernas](https://en.wikipedia.org/wiki/Graphics_processing_unit). El DRM expone una[ API ](https://en.wikipedia.org/wiki/Application_programming_interface)que los programas [de espacio de usuario ](https://en.wikipedia.org/wiki/User-space)pueden usar para enviar comandos y datos a la GPU y realizar acciones como configurar los[ ajustes del modo de visualización. ](https://en.wikipedia.org/wiki/Mode_setting)DRM se desarrolló originalmente como un[ componente de espacio de kernel de](https://en.wikipedia.org/wiki/X.Org_Server)[ la infraestructura de ](https://en.wikipedia.org/wiki/Direct_Rendering_Infrastructure)renderizado directo[ de X Server[](https://en.wikipedia.org/wiki/Direct_Rendering_Manager#cite_note-DRM_readme-1)[1], ](https://en.wikipedia.org/wiki/Kernel-space)pero desde entonces ha sido reemplazado por otras alternativas de pila de gráficos como[ Wayland](https://en.wikipedia.org/wiki/Wayland_(display_server_protocol))) usos. 

Los programas de espacio de usuario pueden usar la API DRM para ordenar la GPU para la[ representación 3D](https://en.wikipedia.org/wiki/Hardware_acceleration) acelerada por[  hardware ](https://en.wikipedia.org/wiki/3D_rendering)y [la decodificación de video](https://en.wikipedia.org/wiki/Video_decoding), así como [la computación GPGPU](https://en.wikipedia.org/wiki/General-purpose_computing_on_graphics_processing_units). 

# 2 Introducción al hardware

## 2.1 Método de adquisición

Descargue y compile el SDK, el SDK descargará y compilará el código de Linux al compilar.

Para obtener más información acerca de cómo descargar y compilar el SDK, consulte[ K510_SDK_Build_and_Burn_Guide](./K510_SDK_Build_and_Burn_Guide.md). 

## 2.2 Archivos y directorios de controladores

```text
drivers/gpu/drm/canaan/
```

## 2.3 Requisitos del entorno de desarrollo

no

## 2.4 Sistema operativo

El sistema Linux y el soporte del número de versión se muestran en la siguiente figura:

| numeración | Recursos de software | ilustrar        |
| ---- | -------- | ----------- |
| 1    | Ubuntu   | 18.04/20.04 |
|      |          |             |
|      |          |             |
|      |          |             |

## 2.5 Entorno de software

Los requisitos del entorno de software se muestran en la tabla siguiente:

| numeración | Recursos de software | ilustrar |
| :--- | -------- | ---- |
| 1    | K510 SDK | v1.1 |
|      |          |      |
|      |          |      |
|      |          |      |

# 3Direct Rendering Manager

## 3.1 Conexiones de referencia

nvdia drm:<https://docs.nvidia.com/jetson/l4t-multimedia/group__direct__rendering__manager.html>

drm freedesktop:<https://cgit.freedesktop.org/mesa/drm>
<https://gitlab.freedesktop.org/mesa/drm>

## 3.2 drm api oficial
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

La función crea un framebuffer con un tamaño y formato especificados, utilizando el objeto de búfer especificado como almacén de respaldo de memoria. El objeto de búfer puede ser un "búfer tonto" creado por una llamada a drmIoctl con el parámetro de solicitud establecido en DRM_IOCTL_MODE_CREATE_DUMB, o puede ser un dma-buf importado por una llamada a la función drmPrimeFDToHandle.

###### Postcondición

Si la llamada se realiza correctamente, la aplicación debe quitar (liberar) el framebuffer llamando a drmModeRmFB.

###### Parámetros

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

###### Devuelve

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

Crea un framebuffer, especificando el formato y los planos.

Esta función es similar a :d rmModeAddFB, pero ofrece más opciones. El formato de píxel de los objetos de búfer se especifica explícitamente, en lugar de ser depth+bpp como en drmModeAddFB. Además, se admiten formatos YUV multiplanares. En cuanto a drmModeAddFB, los identificadores de objetos de búfer pueden ser búferes tontos o dma-bufs importados.

###### Postcondición

Si la llamada se realiza correctamente, la aplicación debe quitar (liberar) el framebuffer llamando a drmModeRmFB.

###### Nota

El parámetro flags no se admite actualmente.

###### Parámetros

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

###### Devuelve

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

Crea un framebuffer, especificando el formato y los planos.
Esta función es similar a :d rmModeAddFB2, pero acepta modificadores.

###### Postcondición

Si la llamada se realiza correctamente, la aplicación debe quitar (liberar) el framebuffer llamando a drmModeRmFB.

###### Nota

###### Parámetros

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

###### Devuelve

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

Agrega una propiedad a una solicitud atómica.
Agrega una propiedad y un valor a una solicitud atómica.

###### Postcondición

###### Nota

###### Parámetros

```text
req:	     An atomic request.
object_id:	 Object ID of a CRTC, plane, or connector to be modified.
property_id: Property ID of the property to be modified.
value:	     The new value for the property.
```

###### Devuelve

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

Confirma una solicitud de cambio de propiedad atómica en el hardware.

Envía todos los cambios de propiedad en una estructura drmModeAtomicReqPtr al hardware.

###### Postcondición

###### Nota

###### Parámetros

```text
fd:	The file descriptor of an open DRM device.
req:	The request object describing properties to commit.
flags:	Flags which influence the operation. The supported flags are:
        DRM_MODE_PAGE_FLIP_ASYNC: Commits values immediately when possible; does not latch new properties at the next vblank.
        DRM_MODE_ATOMIC_NONBLOCK: Commits values to hardware but does not wait for hardware to accept the new values.
        DRM_MODE_ATOMIC_TEST_ONLY: Validates input, but does not commit the values to hardware.
user_data :	Unused.
```

###### Devuelve

```text
0	if successful.
-1	if req is NULL.
-EINVAL	if DRM_CLIENT_CAP_ATOMIC is not enabled, the value of flags is illegal, or atomic property IDs in the request are not recognized.
```

##### ◆ drmModeAtomicFree()

```c
void drmModeAtomicFree	(	drmModeAtomicReqPtr 	req	)
```

Libera una solicitud atómica.

Libera un objeto drmModeAtomicReqPtr asignado por drmModeAtomicAlloc y todos los objetos drmModeAtomicReqItemPtr asociados.

###### Postcondición

###### Nota

###### Parámetros

```text
req	:The atomic request object to be freed.
```

###### Devuelve

```text
NULL
```

##### ◆ drmModeFreeConnector()

```c
void drmModeFreeConnector	(	drmModeConnectorPtr 	ptr	)
```

Libera un conector.

Libera una estructura drmModeConnectorPtr asignada por drmModeGetConnector.

###### Postcondición

###### Nota

###### Parámetros

```text
ptr	A pointer to the connector to be freed.
```

###### Devuelve

```text
null
```

##### ◆ drmModeFreeObjectProperties()

```c
void drmModeFreeObjectProperties	(	drmModeObjectPropertiesPtr 	ptr	)
```

Libera una estructura de propiedades de objeto.

Libera una estructura drmModeObjectPropertiesPtr asignada por drmModeObjectGetProperties.

###### Postcondición

###### Nota

###### Parámetros

```text
ptr	A pointer to the object properties structure to be freed.
```

###### Devuelve

```text
null
```

##### ◆ drmModeFreePlaneResources()

```c
void drmModeFreePlane	(	drmModePlanePtr 	ptr	)
```

Libera un avión.

Libera una estructura drmModePlanePtr asignada por drmModeGetPlane.

###### Postcondición

###### Nota

###### Parámetros

```text
ptr	A pointer to the plane to be freed.
```

###### Devuelve

```text
null
```

##### ◆ drmModeFreeProperty()

```c
void drmModeFreeProperty	(	drmModePropertyPtr 	ptr	)
```

Libera una estructura de propiedad.

Libera una estructura drmModePropertyPtr asignada por drmModeGetProperty.

###### Postcondición

###### Nota

###### Parámetros

```text
ptr	A pointer to a property structure returned by drmModeGetProperty.
```

###### Devuelve

```text
null
```

##### ◆ drmModeFreeResources()

```c
void drmModeFreeResources	(	drmModeResPtr 	ptr	)
```

Libera una estructura de información de recursos.

Libera una estructura drmModeResPtr asignada por drmModeGetResources.

###### Postcondición

###### Nota

###### Parámetros

```text
ptr	A pointer to the resource to be freed.
```

###### Devuelve

```text
null
```

##### ◆ drmModeGetConnector()

```c
drmModeConnectorPtr drmModeGetConnector	(	int 	fd,
                                           uint32_t 	connector_id 
)
```

Obtiene información para un conector.

Si connector_id es válido, obtiene una estructura drmModeConnectorPtr que contiene información sobre un conector, como los modos disponibles, el estado de la conexión, el tipo de conector y el codificador (si lo hay) conectado.

###### Postcondición

Si la llamada se realiza correctamente, la aplicación debe liberar la estructura de información del conector llamando a drmModeFreeConnector.

###### Nota

connector->mmWidth y connector->mmHeight están establecidos actualmente en valores de marcador de posición.

###### Parámetros

```text
fd :	        The file descriptor of an open DRM device.
connector_id:	The connector ID of the connector to be retrieved.
```

###### Devuelve

```text
A drmModeConnectorPtr structure if successful, or NULL if the connector is not found or the API is out of memory.
```

##### ◆ drmModeGetPlaneResources()

```c
drmModePlaneResPtr drmModeGetPlaneResources	(	int 	fd	)
```

Obtiene información sobre los aviones.

Obtiene una lista de recursos de plano para un dispositivo DRM. Una aplicación DRM normalmente llama a esta función temprano para identificar las capas de visualización disponibles.

De forma predeterminada, la información devuelta incluye solo planos de tipo "Superposición" (regulares), no planos "Primario" y "Cursor". Si DRM_CLIENT_CAP_UNIVERSAL_PLANES se ha habilitado con drmSetClientCap, la información devuelta incluye planos "Primarios" que representan CTRC y planos "Cursor" que representan Cursores. Esto permite manipular los QRTC y los cursores con funciones de plano como drmModeSetPlane.

###### Postcondición

Si la llamada se realiza correctamente, la aplicación debe liberar la estructura de información del plano llamando a drmModeFreePlaneResources.

###### Nota

DRM actualmente no implementa planos de tipo "Cursor".

###### Parámetros

```text
fd	The file descriptor of an open DRM device.
```

###### Devuelve

```text
A drmModeResPtr structure if successful, or NULL otherwise.
```

##### ◆ drmModeGetProperty()

```c
drmModePropertyPtr drmModeGetProperty	(	int 	fd,
                                            uint32_t 	propertyId 
)
```

Obtiene una estructura de propiedades que describe una propiedad de un objeto DRM.

El objeto DRM puede ser un plano, un CRTC o un conector.

Esta función funciona en una estructura drmModeObjectPropertiesPtr devuelta por drmModeObjectGetProperties().

Las propiedades modificables dependen del tipo de objeto DRM:

1. Para un plano (tipo objeto DRM_MODE_OBJECT_PLANE):

    ```text
    "SRC_X", "SRC_Y", "SRC_W", "SRC_H", "zpos", "alpha" "CRTC_X",
    "CRTC_Y", "CRTC_W", "CRTC_H", "CRTC_ID", "FB_ID"
    ```

2. Para un CRTC (tipo de objeto DRM_MODE_OBJECT_CRTC), los valores admitidos son:

    ```text
    "MODE_ID", "ACTIVE", "HDR_SUPPORTED", "HDR_METADATA_SMPTE_2086_ID"
    ```

3. Para un conector (tipo objeto DRM_MODE_OBJECT_CONNECTOR), el valor admitido es:

    ```text
    "CRTC_ID"
    ```

Para los planos DRM, el campo enums contiene una lista de pares clave-palabra (nombre: valor) que define las propiedades.

```c
drmModePropertyPtr->enums[ ].name
drmModePropertyPtr->enums[ ].value
```

1. Los valores admitidos para el campo de nombre se definen anteriormente (es decir, "SRC_X", "SRC_Y" o "SRC_W"). Este campo es modificable.
2. Los valores admitidos para los campos de valor son:

```text
"Primary", "Overlay", "Cursor" 
```

Este campo es de solo lectura.

Para identificar el tipo de plano, recorra en iteración la lista siguiente para localizar la enumeración cuyo campo de valor coincida con el que busca. A continuación, obtenga el valor del campo de nombre correspondiente.

```c
drmModePropertyPtr->enums[ ] 
```

Por ejemplo:

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

###### Postcondición

Si la llamada se realiza correctamente, la aplicación debe liberar la estructura de información de la propiedad llamando a drmModeFreeProperty.

###### Nota

El valor zpos de un plano se inicializa con un desplazamiento de 10 en relación con el siguiente plano. Esto es para permitir una configuración flexible de los cabezales. Por ejemplo:

1. Tipo "primario" Plano zpos = 10
2. Primer plano "superpuesto" zpos = 20
3. Siguiente "Superposición" Plano zpos = 30
4. Etc.

El rango permitido para zpos es [0, 255]. Los planos con valores numéricamente mayores para zpos ocluyen planos con valores numéricamente menores.
El valor alfa de un plano hace que se aplique una transparencia de todo el plano, así como el alfa por píxel contenido en el objeto de búfer. El rango permitido para alfa es [0, 255], donde 0 es totalmente transparente y 255 indica que solo el alfa por píxel tiene un efecto. Para los formatos de píxeles no alfa, no hay alfa por píxel, por lo que 255 indica totalmente opaco.

###### Parámetros

```text
fd:	The file descriptor of an open DRM device.
propertyId:	Property ID of the property object to be fetched.
```

###### Devuelve

```text
A drmModePropertyPtr if successful, or NULL otherwise.
```

##### ◆ drmModeGetResources()

```c
drmModeResPtr drmModeGetResources	(	int 	fd	)
```

Obtiene información sobre los CRTC, codificadores y conectores de un dispositivo DRM.

Obtiene una lista de los principales recursos de un dispositivo DRM. Una aplicación DRM normalmente llama a esta función temprano para identificar pantallas disponibles y otros recursos. Sin embargo, la función no informa de los recursos del plano. Estos se pueden consultar con drmModeGetPlaneResources.

###### Postcondición

Si la llamada se realiza correctamente, la aplicación debe liberar la estructura de información de recursos llamando a drmModeFreeResources.

###### Nota

Los miembros min_width, min_height, max_width y max_height de la estructura drmModeResPtr se establecen en valores de marcador de posición.

###### Parámetros

```text
fd	The file descriptor of an open DRM device.

```

###### Devuelve

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

Obtiene todas las propiedades de un objeto DRM.

Obtiene una estructura de propiedades de objeto que describe todas las propiedades modificables atómicamente de un objeto DRM especificado, así como las propiedades de solo lectura no incluidas en las estructuras drmModeCrtcPtr, drmModeConnectorPtr y drmModePlanePtr correspondientes. A continuación, puede recuperar propiedades individuales con drmModeGetProperty y cambiar sus valores con drmModeAtomicAddProperty.

La estructura drmModeObjectPropertiesPtr contiene una matriz de identificadores de propiedad (props), una matriz de valores de propiedad correspondientes (prop_values) y el número de elementos de cada matriz (count_props). Puede obtener el nombre de una propiedad llamando a drmModeGetProperty en el id de propiedad y mirando el campo de nombre de la estructura drmModePropertyPtr devuelto.

Para modificar una propiedad atómicamente, cree un objeto de solicitud drmModeAtomicReqPtr llamando a drmModeAtomicAlloc y, a continuación, llame a drmModeAtomicAddProperty, especificando el objeto drmModeAtomicReqPtr, el identificador de objeto del objeto que se va a modificar, el identificador de propiedad de la propiedad que se va a modificar y el nuevo valor de la propiedad. A continuación, confirme la solicitud con drmModeAtomicCommit. Puede establecer varias propiedades en una solicitud atómica y confirmarlas en una sola operación.

###### Postcondición

Si la llamada se realiza correctamente, la aplicación debe liberar la estructura drmModeObjectPropertiesPtr llamando a drmModeFreeObjectProperties.

###### Nota

No se admiten todos los tipos de objetos.

###### Parámetros

```text
fd:	The file descriptor of an open DRM device.
object_id:	The object ID of the DRM object whose properties are to be retrieved.
object_type:	A symbol representing an object type. The following object types are supported:
    DRM_MODE_OBJECT_CRTC
    DRM_MODE_OBJECT_CONNECTOR
    DRM_MODE_OBJECT_PLANE
```

###### Devuelve

```text
A drmModeObjectPropertiesPtr object if successful, or NULL otherwise.
```

##### ◆ drmModeRmFB()

```c
int drmModeRmFB	(	int 	fd,
                    uint32_t 	fb_id 
)
```

Destruye un framebuffer.

Destruye (libera) un framebuffer asignado por drmModeAddFB o drmModeAddFB2.

###### Postcondición

###### Nota

###### Parámetros

```text
fd	The file descriptor of an open DRM device.
fb_id	The ID of the framebuffer to destroy.
```

###### Devuelve

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

Establece una configuración crtc.

Si se especifica el modo DRM (si drm_mode no es NULL), establece el modo de visualización en el CRTC y los conectores especificados. Las nuevas propiedades fb_id, x e y se establecerán en vblank.

###### Postcondición

###### Nota

Los parámetros fb_id, x e y aceptan el valor de entrada especial -1, que indica que no se debe cambiar el framebuffer de la ventana de hardware o el desplazamiento correspondiente. (Los controladores DRM basados en kernel aceptan -1 solo para fb_id. Devuelven el código de error -ERANGE si se les da -1 para x o y.)
Se permite especificar un modo válido y fb_id ==-1, incluso si actualmente no hay ningún framebuffer conectado al CRTC. La función establecerá el modo de visualización, pero dejará el framebuffer CRTC sin definir.
Los framebuffers establecidos en un CRTC, ya sea por drmModeSetCrtc, drmModePageFlip o cualquier otro medio, se muestran detrás de los planos. La capa de visualización CRTC es la más baja en orden de apilamiento.

###### Parámetros

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

###### Devuelve

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

Cambia el framebuffer y la posición de un plano.

###### Postcondición

###### Nota

El crtc_... y src_... los parámetros aceptan el valor de entrada especial -1, que indica que no se debe cambiar el valor de desplazamiento de hardware. (Los controladores DRM basados en kernel devuelven el código de error -ERANGE cuando se les da este valor).
Los framebuffers colocados en planos se muestran en la parte superior de los CGRC. El orden de apilamiento de los aviones se indica mediante el orden en que drmModeGetPlaneResources informa de los planos.
Todas las operaciones de drmModeSetPlane se sincronizan con vblank y se bloquean.

###### Parámetros

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

###### Devuelve

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

Habilita o deshabilita las características (capacidades) de DRM.

###### Postcondición

###### Nota

###### Parámetros

```text

fd:	         The file descriptor of an open DRM device.
capability：	Specifies the capability to be enabled or disabled. Supported values are:
                    DRM_CLIENT_CAP_ATOMIC (disabled by default)
                    DRM_CLIENT_CAP_UNIVERSAL_PLANES (disabled by default)
value:  	 0 to disable the capability, or 1 to enable it.
```

###### Devuelve

```text
0 if successful, or -EINVAL otherwise.
```

##### ◆ drmWaitVBlank()

```c
int drmWaitVBlank	(	int 	fd,
drmVBlankPtr 	vbl 
)
```

Espera un intervalo de borrado vertical (vblank).

Espera un vblank especificado o solicita que se llame al controlador vblank registrado cuando se produce un vblank especificado.

###### Postcondición

###### Nota

actualmente no es compatible con todos los campos drmVblankPtr.

###### Parámetros

```text
fd:	    The file descriptor of an open DRM device.
vbl:	A description of the requested vblank. The vbl->type field must contain one of these values:
           DRM_VBLANK_ABSOLUTE: request.sequence is the vblank count since some point in the past, e.g. system boot.
           DRM_VBLANK_RELATIVE: request.sequence is the vblank count from the current value. e.g. 1 specifies the next vblank. The value may be bitwise ORed with any combination of these values:
           DRM_VBLANK_SECONDARY: Uses the secondary display's vblank.
           DRM_VBLANK_EVENT: Returns immediately and triggers the event callback instead of waiting for a specified vblank.
```

###### Devuelve

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

###### Postcondición

Solicita un cambio de página (cambio de framebuffer) en el CRTC especificado.

Programa un cambio de página en la CRTC especificada. De forma predeterminada, el CRTC se reprogramará para mostrar el framebuffer especificado después de la siguiente actualización vertical.

###### Nota

###### Parámetros

```text
fd :	    The file descriptor of an open DRM device.
crtc_id :	CRTC ID of the CRTC whose framebuffer is to be changed.
fb_id :	    Framebuffer ID of the framebuffer to be displayed.
flags :	    Flags affecting the operation. Supported values are:
                  DRM_MODE_PAGE_FLIP_ASYNC: Flip immediately, not at vblank.
                  DRM_MODE_PAGE_FLIP_EVENT: Send page flip event.
user_data:	Data used by the page flip handler if vblank event was requested.
```

###### Devuelve

```text
0	if successful.
-EINVAL	if crtc_id or fb_id is invalid.
-errno	otherwise.
```
<!-- markdownlint-enable header-increment no-hard-tabs -->
## 3.3 k510 DRM agregó una descripción del uso de la función de marco

Definición de estructura

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

Definiciones de macros

```c
define DRM_KENDRYTE_DRAW_FRAME         0x00

#define DRM_IOCTL_KENDRYTE_DRAW_FRAME   DRM_IOWR(DRM_COMMAND_BASE + \
                DRM_KENDRYTE_DRAW_FRAME, struct vo_draw_frame)
```

Función de marco

```c
static int draw_frame(struct vo_draw_frame *frame)
{
    return drmIoctl(drm_dev.fd, DRM_IOCTL_KENDRYTE_DRAW_FRAME, frame);
}
```

**Descargo de responsabilidad de **traducción  
Para la comodidad de los clientes, Canaan utiliza un traductor de IA para traducir texto a varios idiomas, que pueden contener errores. No garantizamos la exactitud, fiabilidad o puntualidad de las traducciones proporcionadas. Canaan no será responsable de ninguna pérdida o daño causado por la confianza en la exactitud o fiabilidad de la información traducida. Si existe una diferencia de contenido entre las traducciones en diferentes idiomas, prevalecerá la versión en chino simplificado. 

Si desea informar de un error o inexactitud de traducción, no dude en ponerse en contacto con nosotros por correo.