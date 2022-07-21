![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 Direct Rendering Manager開發指南</font>**

<font face="黑体"  size=3>文件版本：P0.1.0</font>

<font face="黑体"  size=3>發佈日期：2022-01-01</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**免責聲明**</font>
您購買的產品、服務或特性等應受北京嘉楠捷思資訊技術有限公司（“本公司”，下同）商業合同和條款的約束，本文檔中描述的全部或部分產品、服務或特性可能不在您的購買或使用範圍之內。 除非合同另有約定，本公司不對本文檔的任何陳述、資訊、內容的準確性、可靠性、完整性、行銷型、特定目的性和非侵略性提供任何明示或默示的聲明或保證。 除非另有約定，本文檔僅作為使用指導的參考。
由於產品版本升級或其他原因，本文檔內容將可能在未經任何通知的情況下，不定期進行更新或修改。

**<font face="黑体"  size=3>商標聲明</font>**

“<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />”、“Canaan”圖示、嘉楠和嘉楠其他商標均為北京嘉楠捷思資訊技術有限公司的商標。 本文檔可能提及的其他所有商標或註冊商標，由各自的所有人擁有。

**<font face="黑体"  size=3>版權所有©2022北京嘉楠捷思資訊技術有限公司</font>**
本文檔僅適用K510平台開發設計，非經本公司書面許可，任何單位和個人不得以任何形式對本文檔的部分或全部內容傳播。

**<font face="黑体"  size=3>北京嘉楠捷思資訊技術有限公司</font>**
網址：canaan-creative.com
商務垂詢：salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# 前言
**<font face="黑体"  size=5>文件目的</font>**
本文檔為Direct Rendering Manager開發手冊，旨在幫助工程師更快上手

**<font face="黑体"  size=5>讀者物件</font>**

本文檔（本指南）主要適用的人員：

- 軟體開發人員
- 技術支持人員

**<font face="黑体"  size=5>修訂記錄</font>**
 <font face="宋体"  size=2>修訂記錄累積了每次文檔更新的說明。 最新版本的文件包含以前所有版本的更新內容。 </font>

| 版本號   | 修改者     | 修訂日期 | 修訂說明 |
|  :-----  |-------   |  ------  |  ------  |
| 1.0.0 版 | 系統軟體組 | 2022-03-22 |          |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>目 錄</font>**

[目錄]

<div style="page-break-after:always"></div>

# 1簡介

目前sdk使用的linux版本是4.17.0。 Linux，全稱GNU/Linux，是一種免費使用和自由傳播的類UNIX操作系統，其內核由林納斯·本納第克特·托瓦茲於1991年10月5日首次發佈，它主要受到Minix和Unix思想的啟發，是一個基於POSIX的多使用者、多任務、支援多線程和多CPU的操作系統。 它能運行主要的Unix工具軟體、應用程式和網路協定。 它支援32位和64位硬體。 Linux繼承了Unix以網路為核心的設計思想，是一個性能穩定的多用戶網路操作系統。 Linux有上百種不同的發行版，如基於社區開發的debian、archlinux，和基於商業開發的Red Hat Enterprise Linux、SUSE、Oracle Linux等。

# 2硬體介紹

## 2.1獲取方式

下載並編譯sdk，sdk編譯的時候會下載並編譯linux代碼。

sdk的下載編譯方法請參考[K510_SDK_Build_and_Burn_Guide](./K510_SDK_Build_and_Burn_Guide.md)。

## 2.2驅動檔及目錄

```text
drivers/gpu/drm/canaan/
```

## 2.3開發環境需求

無

## 2.4作業系統

Linux系統及版本號支援如下圖所示：

| 編號 | 軟體資源 | 說明        |
| ---- | -------- | ----------- |
| 1    | 烏班圖   | 18.04/20.04 |
|      |          |             |
|      |          |             |
|      |          |             |

## 2.5軟體環境

軟體環境要求如下表所示：

| 編號 | 軟體資源 | 說明 |
| :--- | -------- | ---- |
| 1    | K510 開發工具組 | 版本1.1 |
|      |          |      |
|      |          |      |
|      |          |      |

# 3直接渲染管理器

## 3.1 參考連接

nvdia drm：<https://docs.nvidia.com/jetson/l4t-multimedia/group__direct__rendering__manager.html>

drm freedesktop：<https://cgit.freedesktop.org/mesa/drm>
<https://gitlab.freedesktop.org/mesa/drm>

## 3.2 drm 官方常用api
<!-- markdownlint-disable header-increment no-hard-tabs -->
##### ◆ drmModeAddFB（）

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

創建幀緩衝區。

該函數使用指定的緩衝區對象作為記憶體支援存儲，創建具有指定大小和格式的幀緩衝區。緩衝區物件可以是調用drmIoctl創建的「啞緩衝區」，其請求參數設置為 DRM_IOCTL_MODE_CREATE_DUMB，也可以是通過調用drmPrimeFDToHandle函數導入的 dma-buf。

###### 後置條件

如果調用成功，應用程式必須通過調用drmModeRmFB來刪除（釋放）幀緩衝區。

###### 參數

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

###### 返回

```text
0 if framebuffer creation is successful, or -1 otherwise.
```

##### ◆ drmModeAddFB2（）

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

創建幀緩衝器，指定格式和平面。

此功能類似於：d rmModeAddFB，但提供了更多選項。緩衝區對象的圖元格式是顯式指定的，而不是像在drmModeAddFB中那樣是 depth+bpp。此外，還支援多平面 YUV 格式。至於drmModeAddFB，緩衝區物件句柄可以是啞緩衝區或導入的dma-bufs。

###### 後置條件

如果調用成功，應用程式必須通過調用drmModeRmFB來刪除（釋放）幀緩衝區。

###### 注意

當前不支援 flags 參數。

###### 參數

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

###### 返回

```text
0 if successful, or -1 otherwise.
```

##### ◆ drmModeAddFB2WithModifiers（）

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

創建幀緩衝器，指定格式和平面。
此函數類似於：d rmModeAddFB2，但接受修飾符。

###### 後置條件

如果調用成功，應用程式必須通過調用drmModeRmFB來刪除（釋放）幀緩衝區。

###### 注意

###### 參數

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

###### 返回

```text
0 if successful, or -1 otherwise.
```

##### ◆ drmModeAtomicAddProperty（）

```c
int drmModeAtomicAddProperty	(	drmModeAtomicReqPtr 	req,
uint32_t 	object_id,
uint32_t 	property_id,
uint64_t 	value 
)
```

將屬性添加到原子請求。
將屬性和值添加到原子請求。

###### 後置條件

###### 注意

###### 參數

```text
req:	     An atomic request.
object_id:	 Object ID of a CRTC, plane, or connector to be modified.
property_id: Property ID of the property to be modified.
value:	     The new value for the property.
```

###### 返回

```text
-1 :if req is NULL or the API is out of memory, otherwise it returns the number of properties in the atomic request

-EINVAL: if DRM_CLIENT_CAP_ATOMIC is not enabled.
```

##### ◆ drmModeAtomicCommit（）

```c
int drmModeAtomicCommit	(	int 	fd,
                            drmModeAtomicReqPtr 	req,
                            uint32_t 	flags,
                            void * 	user_data 
)
```

向硬體提交原子屬性更改請求。

將DrmModeAtomicReqPtr結構中的所有屬性更改發送到硬體。

###### 後置條件

###### 注意

###### 參數

```text
fd:	The file descriptor of an open DRM device.
req:	The request object describing properties to commit.
flags:	Flags which influence the operation. The supported flags are:
        DRM_MODE_PAGE_FLIP_ASYNC: Commits values immediately when possible; does not latch new properties at the next vblank.
        DRM_MODE_ATOMIC_NONBLOCK: Commits values to hardware but does not wait for hardware to accept the new values.
        DRM_MODE_ATOMIC_TEST_ONLY: Validates input, but does not commit the values to hardware.
user_data :	Unused.
```

###### 返回

```text
0	if successful.
-1	if req is NULL.
-EINVAL	if DRM_CLIENT_CAP_ATOMIC is not enabled, the value of flags is illegal, or atomic property IDs in the request are not recognized.
```

##### ◆ drmModeAtomicFree（）

```c
void drmModeAtomicFree	(	drmModeAtomicReqPtr 	req	)
```

釋放原子請求。

釋放由drmModeAtomicAlloc分配的drmModeAtomicReqPtr物件，以及所有關聯的drmModeAtomicReqItemPtr物件。

###### 後置條件

###### 注意

###### 參數

```text
req	:The atomic request object to be freed.
```

###### 返回

```text
NULL
```

##### ◆ drmModeFreeConnector（）

```c
void drmModeFreeConnector	(	drmModeConnectorPtr 	ptr	)
```

釋放連接器。

釋放由drmModeGetConnector分配的drmModeConnectorPtr結構。

###### 後置條件

###### 注意

###### 參數

```text
ptr	A pointer to the connector to be freed.
```

###### 返回

```text
null
```

##### ◆ drmModeFreeObjectProperties（）

```c
void drmModeFreeObjectProperties	(	drmModeObjectPropertiesPtr 	ptr	)
```

釋放物件屬性結構。

釋放由drmModeObjectGetProperties分配的drmModeObjectGetProperties 的drmModeObjectPropertiesPtr 結構。

###### 後置條件

###### 注意

###### 參數

```text
ptr	A pointer to the object properties structure to be freed.
```

###### 返回

```text
null
```

##### ◆ drmModeFreePlaneResources（）

```c
void drmModeFreePlane	(	drmModePlanePtr 	ptr	)
```

釋放飛機。

釋放由drmModeGetPlane分配的drmModePlanePtr結構。

###### 後置條件

###### 注意

###### 參數

```text
ptr	A pointer to the plane to be freed.
```

###### 返回

```text
null
```

##### ◆ drmModeFreeProperty（）

```c
void drmModeFreeProperty	(	drmModePropertyPtr 	ptr	)
```

釋放屬性結構。

釋放由drmModeGetProperty分配的drmModePropertyPtr結構。

###### 後置條件

###### 注意

###### 參數

```text
ptr	A pointer to a property structure returned by drmModeGetProperty.
```

###### 返回

```text
null
```

##### ◆ drmModeFreeResources（）

```c
void drmModeFreeResources	(	drmModeResPtr 	ptr	)
```

釋放資源信息結構。

釋放由drmModeGetResources分配的drmModeResPtr結構。

###### 後置條件

###### 注意

###### 參數

```text
ptr	A pointer to the resource to be freed.
```

###### 返回

```text
null
```

##### ◆ drmModeGetConnector（）

```c
drmModeConnectorPtr drmModeGetConnector	(	int 	fd,
                                           uint32_t 	connector_id 
)
```

獲取連接器的資訊。

如果connector_id有效，則獲取一個drmModeConnectorPtr結構，其中包含有關連接器的資訊，如可用模式、連接狀態、連接器類型以及附加的編碼器（如果有）。

###### 後置條件

如果調用成功，應用程式必須通過調用drmModeFreeConnector來釋放連接器信息結構。

###### 注意

連接器>mm寬度和連接器>mm高度當前設置為佔位元值。

###### 參數

```text
fd :	        The file descriptor of an open DRM device.
connector_id:	The connector ID of the connector to be retrieved.
```

###### 返回

```text
A drmModeConnectorPtr structure if successful, or NULL if the connector is not found or the API is out of memory.
```

##### ◆ drmModeGetPlaneResources（）

```c
drmModePlaneResPtr drmModeGetPlaneResources	(	int 	fd	)
```

獲取有關平面的資訊。

獲取DRM設備的平面資源清單。DRM 應用程式通常提前調用此函數以識別可用的顯示層。

默認情況下，返回的資訊僅包括「疊加」類型（常規）平面，不包括“主”和“游標”平面。如果已使用drmSetClientCap啟用了DRM_CLIENT_CAP_UNIVERSAL_PLANES，則返回的資訊包括表示 CTR 的“主”平面和表示遊標的“遊標”平面。這允許使用平面函數（如drmModeSetPlane）操作CC和遊標。

###### 後置條件

如果調用成功，應用程式必須通過調用DrmModeFreePlaneResources來釋放平面信息結構。

###### 注意

DRM 當前不實現「遊標」類型平面。

###### 參數

```text
fd	The file descriptor of an open DRM device.
```

###### 返回

```text
A drmModeResPtr structure if successful, or NULL otherwise.
```

##### ◆ drmModeGetProperty（）

```c
drmModePropertyPtr drmModeGetProperty	(	int 	fd,
                                            uint32_t 	propertyId 
)
```

獲取描述DRM對象的屬性的屬性結構。

DRM 物件可以是平面、CRTC 或連接器。

此函數對drmModeObjectGetProperties（） 傳回的drmModeObjectPropertiesPtr 結構進行操作。

可修改的屬性取決於DRM物件類型：

1. 對於平面（物件類型DRM_MODE_OBJECT_PLANE）：

    ```text
    "SRC_X", "SRC_Y", "SRC_W", "SRC_H", "zpos", "alpha" "CRTC_X",
    "CRTC_Y", "CRTC_W", "CRTC_H", "CRTC_ID", "FB_ID"
    ```

2. 對於CRTC（物件類型DRM_MODE_OBJECT_CRTC），支援的值包括：

    ```text
    "MODE_ID", "ACTIVE", "HDR_SUPPORTED", "HDR_METADATA_SMPTE_2086_ID"
    ```

3. 對於連接器（物件類型 DRM_MODE_OBJECT_CONNECTOR），支援的值為：

    ```text
    "CRTC_ID"
    ```

對於DRM平面，枚舉字位包含定義屬性的關鍵字對（名稱：值）的清單。

```c
drmModePropertyPtr->enums[ ].name
drmModePropertyPtr->enums[ ].value
```

1. 名稱欄位的受支援值在上面定義（即“SRC_X”、“SRC_Y”或“SRC_W”）。此欄位是可修改的。
2. 值欄位支援的值包括：

```text
"Primary", "Overlay", "Cursor" 
```

此欄位是唯讀的。

若要標識平面類型，請迴圈訪問以下清單以查找其值欄位與所查找欄位匹配的枚舉。然後，從相應的名稱欄位獲取值。

```c
drmModePropertyPtr->enums[ ] 
```

例如：

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

###### 後置條件

如果調用成功，應用程式必須通過調用drmModeFreeProperty來釋放屬性信息結構。

###### 注意

平面的 zpos 值初始化為相對於下一個平面的偏移量為 10。這是為了允許靈活配置磁頭。例如：

1. “主”型平面 zpos = 10
2. 第一個“疊加”平面 zpos = 20
3. 下一個“疊加”平面 zpos = 30
4. 等。

zpos 的允許範圍是 [0, 255]。zpos 數值較大的平面會遮擋數值較小的平面。
平面的Alpha值會導致應用平面範圍的透明度以及緩衝區物件中包含的每圖元Alpha。alpha 的允許範圍是 [0, 255]，其中 0 表示完全透明，255 表示只有每圖元 alpha 才有影響。對於非 Alpha 像素格式，沒有每圖元 Alpha，因此 255 表示完全不透明。

###### 參數

```text
fd:	The file descriptor of an open DRM device.
propertyId:	Property ID of the property object to be fetched.
```

###### 返回

```text
A drmModePropertyPtr if successful, or NULL otherwise.
```

##### ◆ drmModeGetResources（）

```c
drmModeResPtr drmModeGetResources	(	int 	fd	)
```

獲取有關DRM設備的CC、編碼器和連接器的資訊。

獲取DRM設備的主要資源的清單。DRM 應用程式通常提前調用此函數以識別可用的顯示器和其他資源。但是，該函數不報告平面資源。這些可以通過drmModeGetPlaneResources進行查詢。

###### 後置條件

如果調用成功，應用程式必須通過調用drmModeFreeResources來釋放資源信息結構。

###### 注意

drmModeResPtr 結構的min_width、min_height、max_width和max_height成員設置為佔位元值。

###### 參數

```text
fd	The file descriptor of an open DRM device.

```

###### 返回

```text
A drmModeResPtr structure if successful, or NULL otherwise.
```

##### ◆ drmModeObjectGetProperties（）

```c
drmModeObjectPropertiesPtr drmModeObjectGetProperties	(	int 	fd,
                                                            uint32_t 	object_id,
                                                            uint32_t 	object_type 
)
```

獲取DRM物件的所有屬性。

獲取一個物件屬性結構，該結構描述指定DRM物件的所有可原子修改屬性，以及相應的drmModeCrtcPtr、drmModeConnectorPtr和drmModePlanePtr 結構中未包含的只讀屬性。然後，您可以使用drmModeGetProperty檢索各個屬性，並使用drmModeAtomicAddProperty更改其值。

drmModeObjectPropertiesPtr 結構包含一個屬性 ID 陣列 （props）、一個對應屬性值數組 （prop_values） 以及每個數位中的元素數 （count_props）。您可以通過在屬性 ID 上調用 drmModeGetProperty 並查看返回的 drmModePropertyPtr 結構的名稱欄位來獲取屬性的名稱。

要以原子方式修改屬性，請通過調用drmModeAtomicAlloc來創建一個drmModeAtomicReqPtr請求物件，然後調用drmModeAtomicAddProperty，指定drmModeAtomicReqPtr物件、要修改的物件的物件 ID、要修改的屬性的屬性 ID 以及屬性的新值。然後使用drmModeAtomicCommit提交請求。您可以在原子請求中設置多個屬性，並在單個操作中提交它們。

###### 後置條件

如果調用成功，應用程式必須通過調用drmModeFreeObjectProperties來釋放drmModeObjectPropertiesPtr結構。

###### 注意

並非所有物件類型都受支援。

###### 參數

```text
fd:	The file descriptor of an open DRM device.
object_id:	The object ID of the DRM object whose properties are to be retrieved.
object_type:	A symbol representing an object type. The following object types are supported:
    DRM_MODE_OBJECT_CRTC
    DRM_MODE_OBJECT_CONNECTOR
    DRM_MODE_OBJECT_PLANE
```

###### 返回

```text
A drmModeObjectPropertiesPtr object if successful, or NULL otherwise.
```

##### ◆ drmModeRmFB（）

```c
int drmModeRmFB	(	int 	fd,
                    uint32_t 	fb_id 
)
```

銷毀幀緩衝器。

銷毀（釋放）由drmModeAddFB或drmModeAddFB2分配的幀緩衝器。

###### 後置條件

###### 注意

###### 參數

```text
fd	The file descriptor of an open DRM device.
fb_id	The ID of the framebuffer to destroy.
```

###### 返回

```text
0 if destruction is successful, or -ENOENT if the framebuffer is not found.
```

##### ◆ drmModeSetCrtc（）

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

設置CRTC配置。

如果指定了DRM模式（如果drm_mode不為NULL），則在CRTC和指定的連接器上設置顯示模式。新的fb_id、x 和 y 屬性將設置為 vblank。

###### 後置條件

###### 注意

fb_id、x 和 y 參數接受特殊輸入值 -1，表示硬體視窗幀緩衝器或相應的偏移量不被更改。（基於內核的DRM驅動程式僅接受 fb_id的 -1。它們返回錯誤代碼 -ERANGE（如果給定 -1 表示 x 或 y）。
允許指定有效模式並fb_id==-1，即使當前沒有幀緩衝器連接到CRTC也是如此。該函數將設置顯示模式，但將保留CRTC緩衝器未定義。
在CRTC上設置的幀緩衝器，無論是通過drmModeSetCrtc，drmModePageFlip還是任何其他方式，都顯示在平面後面。CRTC 顯示層在堆疊順序上是最低的。

###### 參數

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

###### 返回

```text
0:	      if successful.
-EINVAL:  if crtc_id is invalid.
-1:	      if count is invalid, or the list specified by connectors is incompatible with the CRTC.
-errno:	  otherwise.
```

##### ◆ drmModeSetPlane（）

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

更改平面的幀緩衝器和位置。

###### 後置條件

###### 注意

crtc_...和src_...參數接受特殊輸入值 -1，表示硬體偏移值不更改。（基於內核的DRM驅動程式在給定此值時傳回錯誤代碼 -ERANGE。
平面上設置的幀緩衝器顯示在CCTC的頂部。平面的堆疊順序由drmModeGetPlaneResources 報告平面的順序指示。
所有 drmModeSetPlane 操作都同步到 vblank 並處於阻塞狀態。

###### 參數

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

###### 返回

```text
0:  	    if successful.
-EINVAL:	if plane_id or crtc_id is invalid.
-errno: 	otherwise.
```

##### ◆ drmSetClientCap（）

```c
int drmSetClientCap	(	int 	fd,
                        uint64_t 	capability,
                        uint64_t 	value 
)
```

啟用或禁用DRM功能（功能）。

###### 後置條件

###### 注意

###### 參數

```text

fd:	         The file descriptor of an open DRM device.
capability：	Specifies the capability to be enabled or disabled. Supported values are:
                    DRM_CLIENT_CAP_ATOMIC (disabled by default)
                    DRM_CLIENT_CAP_UNIVERSAL_PLANES (disabled by default)
value:  	 0 to disable the capability, or 1 to enable it.
```

###### 返回

```text
0 if successful, or -EINVAL otherwise.
```

##### ◆ drmWaitVBlank（）

```c
int drmWaitVBlank	(	int 	fd,
drmVBlankPtr 	vbl 
)
```

等待垂直消隱間隔 （vblank）。

等待指定的 vblank，或在發生指定的 vblank 時請求調用已註冊的 vblank 處理程式。

###### 後置條件

###### 注意

當前不支援所有drmVblankPtr欄位。

###### 參數

```text
fd:	    The file descriptor of an open DRM device.
vbl:	A description of the requested vblank. The vbl->type field must contain one of these values:
           DRM_VBLANK_ABSOLUTE: request.sequence is the vblank count since some point in the past, e.g. system boot.
           DRM_VBLANK_RELATIVE: request.sequence is the vblank count from the current value. e.g. 1 specifies the next vblank. The value may be bitwise ORed with any combination of these values:
           DRM_VBLANK_SECONDARY: Uses the secondary display's vblank.
           DRM_VBLANK_EVENT: Returns immediately and triggers the event callback instead of waiting for a specified vblank.
```

###### 返回

```text
0 if successful, or -1 otherwise.
```

##### ◆ drmModePageFlip（）

```c
int drmModePageFlip	(	int 	fd,
uint32_t 	crtc_id,
uint32_t 	fb_id,
uint32_t 	flags,
void * 	user_data 
)
```

###### 後置條件

請求在指定的CRTC上翻頁（幀緩衝器更改）。

計劃在指定的CRTC上翻頁。默認情況下，CRTC 將被重新程式設計，以便在下一次垂直刷新後顯示指定的幀緩衝器。

###### 注意

###### 參數

```text
fd :	    The file descriptor of an open DRM device.
crtc_id :	CRTC ID of the CRTC whose framebuffer is to be changed.
fb_id :	    Framebuffer ID of the framebuffer to be displayed.
flags :	    Flags affecting the operation. Supported values are:
                  DRM_MODE_PAGE_FLIP_ASYNC: Flip immediately, not at vblank.
                  DRM_MODE_PAGE_FLIP_EVENT: Send page flip event.
user_data:	Data used by the page flip handler if vblank event was requested.
```

###### 返回

```text
0	if successful.
-EINVAL	if crtc_id or fb_id is invalid.
-errno	otherwise.
```
<!-- markdownlint-enable header-increment no-hard-tabs -->
## 3.3 k510 DRM 新增畫框函數使用說明

結構體定義

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

宏定義

```c
define DRM_KENDRYTE_DRAW_FRAME         0x00

#define DRM_IOCTL_KENDRYTE_DRAW_FRAME   DRM_IOWR(DRM_COMMAND_BASE + \
                DRM_KENDRYTE_DRAW_FRAME, struct vo_draw_frame)
```

畫框函數

```c
static int draw_frame(struct vo_draw_frame *frame)
{
    return drmIoctl(drm_dev.fd, DRM_IOCTL_KENDRYTE_DRAW_FRAME, frame);
}
```

**翻譯免責聲明**  
為方便客戶，Canaan 使用 AI 翻譯程式將文字翻譯為多種語言，它可能包含錯誤。 我們不保證提供的譯文的準確性、可靠性或時效性。 對於因依賴已翻譯信息的準確性或可靠性而造成的任何損失或損害，Canaan 概不負責。 如果不同語言翻譯之間存在內容差異，以簡體中文版本為準。

如果您要報告翻譯錯誤或不準確的問題，歡迎通過郵件與我們聯繫。
