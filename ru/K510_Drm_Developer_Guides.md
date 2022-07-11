![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">Руководство по разработке менеджера прямого рендеринга K510</font>**

<font face="黑体"  size=3>Версия документа: P0.1.0</font>

<font face="黑体"  size=3>Опубликовано: 2022-01-01</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Отказ**</font>
Продукты, услуги или функции, которые вы покупаете, регулируются коммерческими контрактами и условиями Beijing Canaan Jiesi Information Technology Co., Ltd. («Компания», то же самое далее), и все или часть продуктов, услуг или функций, описанных в этом документе, могут не входить в сферу вашей покупки или использования. Если иное не оговорено в договоре, Компания отказывается от всех заявлений или гарантий, явных или подразумеваемых, в отношении точности, надежности, полноты, маркетинга, конкретной цели и ненападения любых заявлений, информации или содержания этого документа. Если не согласовано иное, настоящий документ предоставляется только в качестве руководства для использования.
В связи с обновлением версии продукта или по другим причинам содержимое этого документа может время от времени обновляться или изменяться без какого-либо уведомления.

**<font face="黑体"  size=3>Уведомления о товарных знаках</font>**

""<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, значок "Canaan", Canaan и другие товарные знаки Canaan и другие товарные знаки Canaan являются товарными знаками Beijing Canaan Jiesi Information Technology Co., Ltd. Все другие товарные знаки или зарегистрированные товарные знаки, которые могут быть упомянуты в этом документе, принадлежат их соответствующим владельцам.

**<font face="黑体"  size=3>Copyright ©2022 Пекин Ханаан Цзеси Информационные технологии Co., Ltd</font>**
Настоящий документ применим только к разработке и проектированию платформы K510, без письменного разрешения компании, ни одно подразделение или частное лицо не может распространять часть или все содержание этого документа в любой форме.

**<font face="黑体"  size=3>Пекин Ханаан Цзеси Информационные Технологии Co., Ltd</font>**
URL: canaan-creative.com
Бизнес-запросы: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# предисловие
**<font face="黑体"  size=5>Назначение </font>**документа
Этот документ представляет собой руководство, разработанное для Direct Rendering Manager, чтобы помочь инженерам быстрее приступить к работе

**<font face="黑体"  size=5>Объекты чтения</font>**

Основные люди, к которым относится этот документ (это руководство):

- Разработчики программного обеспечения
- Персонал технической поддержки

**<font face="黑体"  size=5>История изменений</font>**
 <font face="宋体"  size=2>Журнал изменений накапливает описание каждого обновления документа. Последняя версия документа содержит обновления для всех предыдущих версий. </font>

| Номер версии   | Изменено     | Дата пересмотра | Примечания к пересмотру |
|  :-----  |-------   |  ------  |  ------  |
| Версия 1.0.0 | Группы системного программного обеспечения | 2022-03-22 |          |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Содержание</font>**

[ОГЛАВЛЕНИЯ]

<div style="page-break-after:always"></div>

# 1 Введение

Версия Linux, используемая в настоящее время SDK, - 4.17.0. Linux, полное название GNU/Linux, является свободно используемой и свободно распространяемой UNIX-подобной операционной системой с ядром, впервые выпущенным Линусом Беннадиктом Торвазом 5 октября 1991 года, она в основном вдохновлена идеями Minix и Unix, и является многопользовательской, многозадачной, многопоточной и многопроцессорной операционной системой на основе POSIX. Он запускает основное программное обеспечение Unix, приложения и сетевые протоколы. Он поддерживает как 32-разрядное, так и 64-разрядное оборудование. Linux наследует философию проектирования Unix, ориентированную на сеть, и является стабильной многопользовательской сетевой операционной системой. Linux имеет сотни различных дистрибутивов, таких как debian, archlinux и коммерчески разработанные Red Hat Enterprise Linux, SUSE, Oracle Linux и т. Д.

# 2 Введение в аппаратное обеспечение

## 2.1 Метод приобретения

Загрузите и скомпилируйте SDK, SDK загрузит и скомпилирует код Linux при компиляции.

Дополнительные сведения о загрузке и компиляции пакета SDK см. в разделе[K510_SDK_Build_and_Burn_Guide](./K510_SDK_Build_and_Burn_Guide.md).

## 2.2 Файлы драйверов и каталоги

```text
drivers/gpu/drm/canaan/
```

## 2.3 Требования к среде разработки

не

## 2.4 Операционная система

Поддержка системы Linux и номера версии показана на следующем рисунке:

| нумерация | Программные ресурсы | иллюстрировать        |
| ---- | -------- | ----------- |
| 1    | Убунту   | 18.04/20.04 |
|      |          |             |
|      |          |             |
|      |          |             |

## 2.5 Программная среда

Требования к программной среде приведены в следующей таблице:

| нумерация | Программные ресурсы | иллюстрировать |
| :--- | -------- | ---- |
| 1    | K510 SDK | Версия 1.1 |
|      |          |      |
|      |          |      |
|      |          |      |

# 3Прямой менеджер рендеринга

## 3.1 Справочные соединения

nvdia drm:<https://docs.nvidia.com/jetson/l4t-multimedia/group__direct__rendering__manager.html>

drm freedesktop:<https://cgit.freedesktop.org/mesa/drm>
<https://gitlab.freedesktop.org/mesa/drm>

## 3.2 drm официальный API
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

Создает фреймбуфер.

Функция создает фреймбуфер с заданным размером и форматом, используя указанный объект буфера в качестве резервного хранилища памяти. Объект буфера может быть "тупым буфером", созданным вызовом drmIoctl с параметром request, равным DRM_IOCTL_MODE_CREATE_DUMB, или dma-buf, импортированным вызовом функции drmPrimeFDToHandle.

###### Постусловие

Если вызов выполнен успешно, приложение должно удалить (освободить) фреймбуфер, вызвав drmModeRmFB.

###### Параметры

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

###### Возвращает

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

Создает фреймбуфер, задавая формат и плоскости.

Эта функция похожа на :d rmModeAddFB, но предлагает больше опций. Формат пикселей буферных объектов указан явно, а не глубина+bpp, как в drmModeAddFB. Также поддерживаются многопланарные форматы YUV. Что касается drmModeAddFB, то дескрипторы буферных объектов могут быть тупыми буферами или импортированными dma-bufs.

###### Постусловие

Если вызов выполнен успешно, приложение должно удалить (освободить) фреймбуфер, вызвав drmModeRmFB.

###### Заметка

Параметр flags в настоящее время не поддерживается.

###### Параметры

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

###### Возвращает

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

Создает фреймбуфер, задавая формат и плоскости.
Эта функция аналогична :d rmModeAddFB2, но принимает модификаторы.

###### Постусловие

Если вызов выполнен успешно, приложение должно удалить (освободить) фреймбуфер, вызвав drmModeRmFB.

###### Заметка

###### Параметры

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

###### Возвращает

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

Добавляет свойство в атомарный запрос.
Добавляет свойство и значение в атомарный запрос.

###### Постусловие

###### Заметка

###### Параметры

```text
req:	     An atomic request.
object_id:	 Object ID of a CRTC, plane, or connector to be modified.
property_id: Property ID of the property to be modified.
value:	     The new value for the property.
```

###### Возвращает

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

Фиксирует запрос на изменение атомарных свойств на оборудовании.

Отправляет все изменения свойств в структуре drmModeAtomicReqPtr на оборудование.

###### Постусловие

###### Заметка

###### Параметры

```text
fd:	The file descriptor of an open DRM device.
req:	The request object describing properties to commit.
flags:	Flags which influence the operation. The supported flags are:
        DRM_MODE_PAGE_FLIP_ASYNC: Commits values immediately when possible; does not latch new properties at the next vblank.
        DRM_MODE_ATOMIC_NONBLOCK: Commits values to hardware but does not wait for hardware to accept the new values.
        DRM_MODE_ATOMIC_TEST_ONLY: Validates input, but does not commit the values to hardware.
user_data :	Unused.
```

###### Возвращает

```text
0	if successful.
-1	if req is NULL.
-EINVAL	if DRM_CLIENT_CAP_ATOMIC is not enabled, the value of flags is illegal, or atomic property IDs in the request are not recognized.
```

##### ◆ drmModeAtomicFree()

```c
void drmModeAtomicFree	(	drmModeAtomicReqPtr 	req	)
```

Освобождает атомарный запрос.

Освобождает объект drmModeAtomicReqPtr, выделенный drmModeAtomicAlloc, и все связанные с ним объекты drmModeAtomicReqItemPtr.

###### Постусловие

###### Заметка

###### Параметры

```text
req	:The atomic request object to be freed.
```

###### Возвращает

```text
NULL
```

##### ◆ drmModeFreeConnector()

```c
void drmModeFreeConnector	(	drmModeConnectorPtr 	ptr	)
```

Освобождает разъем.

Освобождает структуру drmModeConnectorPtr, выделенную drmModeGetConnector.

###### Постусловие

###### Заметка

###### Параметры

```text
ptr	A pointer to the connector to be freed.
```

###### Возвращает

```text
null
```

##### ◆ drmModeFreeObjectProperties()

```c
void drmModeFreeObjectProperties	(	drmModeObjectPropertiesPtr 	ptr	)
```

Освобождает структуру свойств объекта.

Освобождает структуру drmModeObjectPropertiesPtr, выделенную drmModeObjectGetProperties.

###### Постусловие

###### Заметка

###### Параметры

```text
ptr	A pointer to the object properties structure to be freed.
```

###### Возвращает

```text
null
```

##### ◆ drmModeFreePlaneResources()

```c
void drmModeFreePlane	(	drmModePlanePtr 	ptr	)
```

Освобождает самолет.

Освобождает структуру drmModePlanePtr, выделенную drmModeGetPlane.

###### Постусловие

###### Заметка

###### Параметры

```text
ptr	A pointer to the plane to be freed.
```

###### Возвращает

```text
null
```

##### ◆ drmModeFreeProperty()

```c
void drmModeFreeProperty	(	drmModePropertyPtr 	ptr	)
```

Освобождает структуру недвижимости.

Освобождает структуру drmModePropertyPtr, выделенную drmModeGetProperty.

###### Постусловие

###### Заметка

###### Параметры

```text
ptr	A pointer to a property structure returned by drmModeGetProperty.
```

###### Возвращает

```text
null
```

##### ◆ drmModeFreeResources()

```c
void drmModeFreeResources	(	drmModeResPtr 	ptr	)
```

Освобождает информационную структуру ресурса.

Освобождает структуру drmModeResPtr, выделенную drmModeGetResources.

###### Постусловие

###### Заметка

###### Параметры

```text
ptr	A pointer to the resource to be freed.
```

###### Возвращает

```text
null
```

##### ◆ drmModeGetConnector()

```c
drmModeConnectorPtr drmModeGetConnector	(	int 	fd,
                                           uint32_t 	connector_id 
)
```

Получает сведения для соединителя.

Если connector_id является допустимым, извлекает структуру drmModeConnectorPtr, содержащую информацию о соединителе, такую как доступные режимы, состояние подключения, тип разъема и какой кодировщик (если таковой имеется) подключен.

###### Постусловие

Если вызов выполнен успешно, приложение должно освободить информационную структуру соединителя, вызвав drmModeFreeConnector.

###### Заметка

Connector->mmWidth и connector->mmHeight в настоящее время имеют значения заполнителей.

###### Параметры

```text
fd :	        The file descriptor of an open DRM device.
connector_id:	The connector ID of the connector to be retrieved.
```

###### Возвращает

```text
A drmModeConnectorPtr structure if successful, or NULL if the connector is not found or the API is out of memory.
```

##### ◆ drmModeGetPlaneResources()

```c
drmModePlaneResPtr drmModeGetPlaneResources	(	int 	fd	)
```

Получает сведения о самолетах.

Получает список ресурсов плоскости для устройства DRM. Приложение DRM обычно вызывает эту функцию на ранней стадии, чтобы определить доступные слои отображения.

По умолчанию возвращаемая информация включает только плоскости типа «Наложение» (обычные), а не «Основные» и «Курсорные». Если DRM_CLIENT_CAP_UNIVERSAL_PLANES был включен с помощью drmSetClientCap, возвращаемая информация включает в себя "Основные" плоскости, представляющие CTRC, и "Курсорные" плоскости, представляющие Курсоры. Это позволяет манипулировать ЭЛТ И Курсорами с помощью плоских функций, таких как drmModeSetPlane.

###### Постусловие

Если вызов выполнен успешно, приложение должно освободить информационную структуру плоскости, вызвав drmModeFreePlaneResources.

###### Заметка

DRM в настоящее время не реализует плоскости типа «Курсор».

###### Параметры

```text
fd	The file descriptor of an open DRM device.
```

###### Возвращает

```text
A drmModeResPtr structure if successful, or NULL otherwise.
```

##### ◆ drmModeGetProperty()

```c
drmModePropertyPtr drmModeGetProperty	(	int 	fd,
                                            uint32_t 	propertyId 
)
```

Получает структуру свойств, описывающую свойство объекта DRM.

Объект DRM может быть плоскостью, CRTC или соединителем.

Эта функция работает со структурой drmModeObjectPropertiesPtr, возвращаемой drmModeObjectGetProperties().

Изменяемые свойства зависят от типа объекта DRM:

1. Для плоскости (тип объекта DRM_MODE_OBJECT_PLANE):

    ```text
    "SRC_X", "SRC_Y", "SRC_W", "SRC_H", "zpos", "alpha" "CRTC_X",
    "CRTC_Y", "CRTC_W", "CRTC_H", "CRTC_ID", "FB_ID"
    ```

2. Для CRTC (тип объекта DRM_MODE_OBJECT_CRTC) поддерживаются следующие значения:

    ```text
    "MODE_ID", "ACTIVE", "HDR_SUPPORTED", "HDR_METADATA_SMPTE_2086_ID"
    ```

3. Для соединителя (тип объекта DRM_MODE_OBJECT_CONNECTOR) поддерживается следующее значение:

    ```text
    "CRTC_ID"
    ```

Для плоскостей DRM поле перечисления содержит список пар ключ-слово (имя: значение), которые определяют свойства.

```c
drmModePropertyPtr->enums[ ].name
drmModePropertyPtr->enums[ ].value
```

1. Поддерживаемые значения для поля имени определены выше (например, "SRC_X", "SRC_Y" или "SRC_W"). Это поле можно изменять.
2. Поддерживаемые значения для полей значений:

```text
"Primary", "Overlay", "Cursor" 
```

Это поле доступно только для чтения.

Чтобы определить тип плоскости, выполните итерацию по следующему списку, чтобы найти перечисление, поле значения которого совпадает с искомым. Затем получите значение из соответствующего поля имени.

```c
drmModePropertyPtr->enums[ ] 
```

Например:

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

###### Постусловие

Если вызов выполнен успешно, приложение должно освободить структуру сведений о свойствах, вызвав drmModeFreeProperty.

###### Заметка

Значение zpos для плоскости инициализируется со смещением 10 относительно следующей плоскости. Это обеспечивает гибкую конфигурацию головок. Например:

1. "Первичный" тип Плоскость zpos = 10
2. Первая "накладная" плоскость zpos = 20
3. Следующая "накладная" плоскость zpos = 30
4. И так далее.

Допустимый диапазон для zpos равен [0, 255]. Плоскости с численно большими значениями для zpos закрывают плоскости с численно меньшими значениями.
Значение альфа-канала для плоскости приводит к применению прозрачности всей плоскости, а также к альфа-каналу на пиксель, содержащемуся в объекте буфера. Допустимый диапазон для альфа-канала равен [0, 255], где 0 полностью прозрачен, а 255 указывает, что только альфа-канал на пиксель имеет эффект. Для форматов, отличных от альфа-пикселей, альфа-канала на пиксель отсутствует, поэтому 255 указывает на полную непрозрачность.

###### Параметры

```text
fd:	The file descriptor of an open DRM device.
propertyId:	Property ID of the property object to be fetched.
```

###### Возвращает

```text
A drmModePropertyPtr if successful, or NULL otherwise.
```

##### ◆ drmModeGetResources()

```c
drmModeResPtr drmModeGetResources	(	int 	fd	)
```

Получает сведения о ЭЛТ, энкодерах и соединителях устройства DRM.

Получает список основных ресурсов устройства DRM. Приложение DRM обычно вызывает эту функцию на ранней стадии, чтобы определить доступные дисплеи и другие ресурсы. Однако функция не сообщает о ресурсах плоскости. Их можно запрашивать с помощью drmModeGetPlaneResources.

###### Постусловие

Если вызов выполнен успешно, приложение должно освободить информационную структуру ресурса, вызвав drmModeFreeResources.

###### Заметка

для min_width, min_height, max_width и max_height членов структуры drmModeResPtr установлены значения заполнителей.

###### Параметры

```text
fd	The file descriptor of an open DRM device.

```

###### Возвращает

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

Получает все свойства объекта DRM.

Получает структуру свойств объекта, описывающую все атомарно изменяемые свойства заданного объекта DRM, а также свойства только для чтения, не включенные в соответствующие структуры drmModeCrtcPtr, drmModeConnectorPtr и drmModePlanePtr. Затем можно извлечь отдельные свойства с помощью drmModeGetProperty и изменить их значения с помощью drmModeAtomicAddProperty.

Структура drmModeObjectPropertiesPtr содержит массив идентификаторов свойств (props), массив соответствующих значений свойств (prop_values) и количество элементов в каждом массиве (count_props). Имя свойства можно получить, вызвав drmModeGetProperty по идентификатору свойства и просмотрев поле имени возвращаемой структуры drmModePropertyPtr.

Чтобы изменить свойство атомарно, создайте объект запроса drmModeAtomicReqPtr, вызвав drmModeAtomicAlloc, а затем вызовите drmModeAtomicAddProperty, указав объект drmModeAtomicReqPtr, идентификатор изменяемого объекта, идентификатор свойства изменяемого свойства и новое значение свойства. Затем зафиксируйте запрос с помощью drmModeAtomicCommit. Можно задать несколько свойств в атомарном запросе и зафиксировать их в одной операции.

###### Постусловие

Если вызов выполнен успешно, приложение должно освободить структуру drmModeObjectPropertiesPtr, вызвав drmModeFreeObjectProperties.

###### Заметка

Поддерживаются не все типы объектов.

###### Параметры

```text
fd:	The file descriptor of an open DRM device.
object_id:	The object ID of the DRM object whose properties are to be retrieved.
object_type:	A symbol representing an object type. The following object types are supported:
    DRM_MODE_OBJECT_CRTC
    DRM_MODE_OBJECT_CONNECTOR
    DRM_MODE_OBJECT_PLANE
```

###### Возвращает

```text
A drmModeObjectPropertiesPtr object if successful, or NULL otherwise.
```

##### ◆ drmModeRmFB()

```c
int drmModeRmFB	(	int 	fd,
                    uint32_t 	fb_id 
)
```

Уничтожает фреймбуфер.

Уничтожает (освобождает) фреймбуфер, выделенный drmModeAddFB или drmModeAddFB2.

###### Постусловие

###### Заметка

###### Параметры

```text
fd	The file descriptor of an open DRM device.
fb_id	The ID of the framebuffer to destroy.
```

###### Возвращает

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

Задает конфигурацию CRTC.

Если указан режим DRM (если drm_mode не NULL), задает режим отображения на CRTC и указанных разъемах. Новые свойства fb_id, x и y будут установлены в vblank.

###### Постусловие

###### Заметка

Параметры fb_id, x и y принимают специальное входное значение -1, которое указывает, что аппаратный оконный фреймбуфер или соответствующее смещение не подлежит изменению. (Драйверы DRM на основе ядра принимают -1 только для fb_id. Они возвращают код ошибки -ERANGE, если задано -1 для x или y.)
Разрешается указывать допустимый режим и fb_id==-1, даже если фреймбуфер в настоящее время не прикреплен к CRTC. Функция установит режим отображения, но оставит фреймбуфер CRTC неопределенным.
Фреймбуферы, установленные на CRTC, будь то drmModeSetCrtc, drmModePageFlip или любые другие средства, отображаются за плоскостями. Уровень отображения CRTC является самым низким в порядке наложения.

###### Параметры

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

###### Возвращает

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

Изменяет фреймбуфер и положение самолета.

###### Постусловие

###### Заметка

В crtc_... и src_... параметры принимают специальное входное значение -1, которое указывает, что значение аппаратного смещения не подлежит изменению. (Драйверы DRM на основе ядра возвращают код ошибки -ERANGE при присвоении этого значения.)
Фреймбуферы, установленные на плоскостях, отображаются поверх ЭЛТ. Порядок укладки плоскостей обозначается порядком, в котором плоскости сообщаются drmModeGetPlaneResources.
Все операции drmModeSetPlane синхронизируются с vblank и блокируются.

###### Параметры

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

###### Возвращает

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

Включает или отключает функции (возможности) DRM.

###### Постусловие

###### Заметка

###### Параметры

```text

fd:	         The file descriptor of an open DRM device.
capability：	Specifies the capability to be enabled or disabled. Supported values are:
                    DRM_CLIENT_CAP_ATOMIC (disabled by default)
                    DRM_CLIENT_CAP_UNIVERSAL_PLANES (disabled by default)
value:  	 0 to disable the capability, or 1 to enable it.
```

###### Возвращает

```text
0 if successful, or -EINVAL otherwise.
```

##### ◆ drmWaitVBlank()

```c
int drmWaitVBlank	(	int 	fd,
drmVBlankPtr 	vbl 
)
```

Ожидает вертикального интервала гашения (vblank).

Ожидает указанного vblank или запрашивает вызов зарегистрированного обработчика vblank при возникновении указанного vblank.

###### Постусловие

###### Заметка

В настоящее время поддерживает не все поля drmVblankPtr.

###### Параметры

```text
fd:	    The file descriptor of an open DRM device.
vbl:	A description of the requested vblank. The vbl->type field must contain one of these values:
           DRM_VBLANK_ABSOLUTE: request.sequence is the vblank count since some point in the past, e.g. system boot.
           DRM_VBLANK_RELATIVE: request.sequence is the vblank count from the current value. e.g. 1 specifies the next vblank. The value may be bitwise ORed with any combination of these values:
           DRM_VBLANK_SECONDARY: Uses the secondary display's vblank.
           DRM_VBLANK_EVENT: Returns immediately and triggers the event callback instead of waiting for a specified vblank.
```

###### Возвращает

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

###### Постусловие

Запрашивает перелистывание страницы (изменение фреймбуфера) в указанном CRTC.

Планирует пролистывание страницы на указанном CRTC. По умолчанию CRTC будет перепрограммирован для отображения указанного фреймбуфера после следующего вертикального обновления.

###### Заметка

###### Параметры

```text
fd :	    The file descriptor of an open DRM device.
crtc_id :	CRTC ID of the CRTC whose framebuffer is to be changed.
fb_id :	    Framebuffer ID of the framebuffer to be displayed.
flags :	    Flags affecting the operation. Supported values are:
                  DRM_MODE_PAGE_FLIP_ASYNC: Flip immediately, not at vblank.
                  DRM_MODE_PAGE_FLIP_EVENT: Send page flip event.
user_data:	Data used by the page flip handler if vblank event was requested.
```

###### Возвращает

```text
0	if successful.
-EINVAL	if crtc_id or fb_id is invalid.
-errno	otherwise.
```
<!-- markdownlint-enable header-increment no-hard-tabs -->
## 3.3 k510 DRM добавил описание использования функции кадра

Определение структуры

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

Определения макросов

```c
define DRM_KENDRYTE_DRAW_FRAME         0x00

#define DRM_IOCTL_KENDRYTE_DRAW_FRAME   DRM_IOWR(DRM_COMMAND_BASE + \
                DRM_KENDRYTE_DRAW_FRAME, struct vo_draw_frame)
```

Функция кадра

```c
static int draw_frame(struct vo_draw_frame *frame)
{
    return drmIoctl(drm_dev.fd, DRM_IOCTL_KENDRYTE_DRAW_FRAME, frame);
}
```

**Отказ от ответственности за**перевод  
Для удобства клиентов Canaan использует переводчик AI для перевода текста на несколько языков, которые могут содержать ошибки. Мы не гарантируем точность, надежность или своевременность предоставленных переводов. Компания Canaan не несет ответственности за любые убытки или ущерб, вызванные доверием к точности или надежности переведенной информации. При наличии разницы в содержании переводов на разные языки преимущественную силу имеет упрощенная версия на китайском языке.

Если вы хотите сообщить об ошибке или неточности перевода, пожалуйста, не стесняйтесь обращаться к нам по почте.
