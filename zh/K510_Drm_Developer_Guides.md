![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 Direct Rendering Manager开发指南</font>**

<font face="黑体"  size=3>文档版本：P0.1.0</font>

<font face="黑体"  size=3>发布日期：2022-01-01</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**免责声明**</font>
您购买的产品、服务或特性等应受北京嘉楠捷思信息技术有限公司（“本公司”，下同）商业合同和条款的约束，本文档中描述的全部或部分产品、服务或特性可能不在您的购买或使用范围之内。除非合同另有约定，本公司不对本文档的任何陈述、信息、内容的准确性、可靠性、完整性、营销型、特定目的性和非侵略性提供任何明示或默示的声明或保证。除非另有约定，本文档仅作为使用指导的参考。
由于产品版本升级或其他原因，本文档内容将可能在未经任何通知的情况下，不定期进行更新或修改。

**<font face="黑体"  size=3>商标声明</font>**

“<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />”、“Canaan”图标、嘉楠和嘉楠其他商标均为北京嘉楠捷思信息技术有限公司的商标。本文档可能提及的其他所有商标或注册商标，由各自的所有人拥有。

**<font face="黑体"  size=3>版权所有©2022北京嘉楠捷思信息技术有限公司</font>**
本文档仅适用K510平台开发设计，非经本公司书面许可，任何单位和个人不得以任何形式对本文档的部分或全部内容传播。

**<font face="黑体"  size=3>北京嘉楠捷思信息技术有限公司</font>**
网址：canaan-creative.com
商务垂询：salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# 前言
**<font face="黑体"  size=5>文档目的</font>**
本文档为Direct Rendering Manager开发手册，旨在帮助工程师更快上手

**<font face="黑体"  size=5>读者对象</font>**

本文档（本指南）主要适用的人员：

- 软件开发人员
- 技术支持人员

**<font face="黑体"  size=5>修订记录</font>**
<font face="宋体"  size=2>修订记录累积了每次文档更新的说明。最新版本的文档包含以前所有版本的更新内容。</font>

| 版本号   | 修改者     | 修订日期 | 修订说明 |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | 系统软件组 | 2022-03-22 |          |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>目 录</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1简介

目前sdk使用的linux版本是4.17.0。Linux，全称GNU/Linux，是一种免费使用和自由传播的类UNIX操作系统，其内核由林纳斯·本纳第克特·托瓦兹于1991年10月5日首次发布，它主要受到Minix和Unix思想的启发，是一个基于POSIX的多用户、多任务、支持多线程和多CPU的操作系统。它能运行主要的Unix工具软件、应用程序和网络协议。它支持32位和64位硬件。Linux继承了Unix以网络为核心的设计思想，是一个性能稳定的多用户网络操作系统。Linux有上百种不同的发行版，如基于社区开发的debian、archlinux，和基于商业开发的Red Hat Enterprise Linux、SUSE、Oracle Linux等。

Direct Rendering Manager是[Linux 内核](https://en.wikipedia.org/wiki/Linux_kernel)的一个子系统，负责与现代[视频卡的](https://en.wikipedia.org/wiki/Video_cards)[GPU](https://en.wikipedia.org/wiki/Graphics_processing_unit)连接。DRM 公开了一个[API](https://en.wikipedia.org/wiki/Application_programming_interface)，[用户空间](https://en.wikipedia.org/wiki/User-space)程序可以使用该 API 向 GPU 发送命令和数据，并执行诸如配置显示器[模式设置等操作。](https://en.wikipedia.org/wiki/Mode_setting)DRM 最初是作为[X Server](https://en.wikipedia.org/wiki/X.Org_Server)[Direct Rendering Infrastructure](https://en.wikipedia.org/wiki/Direct_Rendering_Infrastructure)[[1\]](https://en.wikipedia.org/wiki/Direct_Rendering_Manager#cite_note-DRM_readme-1)[的内核空间](https://en.wikipedia.org/wiki/Kernel-space)组件开发的，但从那时起它已被其他图形堆栈替代方案（如[Wayland](https://en.wikipedia.org/wiki/Wayland_(display_server_protocol)) ）使用。

用户空间程序可以使用 DRM API 命令 GPU 进行[硬件加速](https://en.wikipedia.org/wiki/Hardware_acceleration) [3D 渲染](https://en.wikipedia.org/wiki/3D_rendering)和[视频解码](https://en.wikipedia.org/wiki/Video_decoding)，以及[GPGPU 计算](https://en.wikipedia.org/wiki/General-purpose_computing_on_graphics_processing_units)。

# 2硬件介绍

## 2.1获取方式

下载并编译sdk，sdk编译的时候会下载并编译linux代码。

sdk的下载编译方法请参考[K510_SDK_Build_and_Burn_Guide](./K510_SDK_Build_and_Burn_Guide.md)。

## 2.2驱动文件及目录

```text
drivers/gpu/drm/canaan/
```

## 2.3开发环境需求

无

## 2.4操作系统

Linux系统及版本号支持如下图所示：

| 编号 | 软件资源 | 说明        |
| ---- | -------- | ----------- |
| 1    | Ubuntu   | 18.04/20.04 |
|      |          |             |
|      |          |             |
|      |          |             |

## 2.5软件环境

软件环境要求如下表所示：

| 编号 | 软件资源 | 说明 |
| :--- | -------- | ---- |
| 1    | K510 SDK | v1.1 |
|      |          |      |
|      |          |      |
|      |          |      |

# 3Direct Rendering Manager

## 3.1 参考连接

nvdia drm:
<https://docs.nvidia.com/jetson/l4t-multimedia/group__direct__rendering__manager.html>

drm freedesktop:
<https://cgit.freedesktop.org/mesa/drm>
<https://gitlab.freedesktop.org/mesa/drm>

## 3.2 drm 官方常用api
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

Creates a framebuffer.

The function creates a framebuffer with a specified size and format, using the specified buffer object as the memory backing store. The buffer object can be a "dumb buffer" created by a call to drmIoctl with the request parameter set to DRM_IOCTL_MODE_CREATE_DUMB, or it can be a dma-buf imported by a call to the drmPrimeFDToHandle function.

###### Postcondition

If the call is successful, the application must remove (free) the framebuffer by calling drmModeRmFB.

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

###### Returns

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

Creates a framebuffer, specifying format and planes.

This function is similar to :drmModeAddFB, but offers more options. The buffer objects' pixel format is specified explicitly, instead of being depth+bpp as in drmModeAddFB. Also, multiplanar YUV formats are supported. As for drmModeAddFB, the buffer object handle(s) can be a dumb buffers or imported dma-bufs.

###### Postcondition

If the call is successful, the application must remove (free) the framebuffer by calling drmModeRmFB.

###### Note

The flags parameter is not currently supported.

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

###### Returns

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

Creates a framebuffer, specifying format and planes.
This function is similar to :drmModeAddFB2, but accepts modifiers.

###### Postcondition

If the call is successful, the application must remove (free) the framebuffer by calling drmModeRmFB.

###### Note

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

###### Returns

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

Adds a property to an atomic request.
Adds a property and value to an atomic request.

###### Postcondition

###### Note

###### Parameters

```text
req:	     An atomic request.
object_id:	 Object ID of a CRTC, plane, or connector to be modified.
property_id: Property ID of the property to be modified.
value:	     The new value for the property.
```

###### Returns

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

Commits an atomic property change request to hardware.

Sends all of the property changes in a drmModeAtomicReqPtr structure to hardware.

###### Postcondition

###### Note

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

###### Returns

```text
0	if successful.
-1	if req is NULL.
-EINVAL	if DRM_CLIENT_CAP_ATOMIC is not enabled, the value of flags is illegal, or atomic property IDs in the request are not recognized.
```

##### ◆ drmModeAtomicFree()

```c
void drmModeAtomicFree	(	drmModeAtomicReqPtr 	req	)
```

Frees an atomic request.

Frees a drmModeAtomicReqPtr object allocated by drmModeAtomicAlloc, and all of the associated drmModeAtomicReqItemPtr objects.

###### Postcondition

###### Note

###### Parameters

```text
req	:The atomic request object to be freed.
```

###### Returns

```text
NULL
```

##### ◆ drmModeFreeConnector()

```c
void drmModeFreeConnector	(	drmModeConnectorPtr 	ptr	)
```

Frees a connector.

Frees a drmModeConnectorPtr structure allocated by drmModeGetConnector.

###### Postcondition

###### Note

###### Parameters

```text
ptr	A pointer to the connector to be freed.
```

###### Returns

```text
null
```

##### ◆ drmModeFreeObjectProperties()

```c
void drmModeFreeObjectProperties	(	drmModeObjectPropertiesPtr 	ptr	)
```

Frees an object properties structure.

Frees a drmModeObjectPropertiesPtr structure allocated by drmModeObjectGetProperties.

###### Postcondition

###### Note

###### Parameters

```text
ptr	A pointer to the object properties structure to be freed.
```

###### Returns

```text
null
```

##### ◆ drmModeFreePlaneResources()

```c
void drmModeFreePlane	(	drmModePlanePtr 	ptr	)
```

Frees a plane.

Frees a drmModePlanePtr structure allocated by drmModeGetPlane.

###### Postcondition

###### Note

###### Parameters

```text
ptr	A pointer to the plane to be freed.
```

###### Returns

```text
null
```

##### ◆ drmModeFreeProperty()

```c
void drmModeFreeProperty	(	drmModePropertyPtr 	ptr	)
```

Frees a property structure.

Frees a drmModePropertyPtr structure allocated by drmModeGetProperty.

###### Postcondition

###### Note

###### Parameters

```text
ptr	A pointer to a property structure returned by drmModeGetProperty.
```

###### Returns

```text
null
```

##### ◆ drmModeFreeResources()

```c
void drmModeFreeResources	(	drmModeResPtr 	ptr	)
```

Frees a resource information structure.

Frees a drmModeResPtr structure allocated by drmModeGetResources.

###### Postcondition

###### Note

###### Parameters

```text
ptr	A pointer to the resource to be freed.
```

###### Returns

```text
null
```

##### ◆ drmModeGetConnector()

```c
drmModeConnectorPtr drmModeGetConnector	(	int 	fd,
                                           uint32_t 	connector_id 
)
```

Gets information for a connector.

If connector_id is valid, fetches a drmModeConnectorPtr structure which contains information about a connector, such as available modes, connection status, connector type, and which encoder (if any) is attached.

###### Postcondition

If the call is successful, the application must free the connector information structure by calling drmModeFreeConnector.

###### Note

connector->mmWidth and connector->mmHeight are currently set to placeholder values.

###### Parameters

```text
fd :	        The file descriptor of an open DRM device.
connector_id:	The connector ID of the connector to be retrieved.
```

###### Returns

```text
A drmModeConnectorPtr structure if successful, or NULL if the connector is not found or the API is out of memory.
```

##### ◆ drmModeGetPlaneResources()

```c
drmModePlaneResPtr drmModeGetPlaneResources	(	int 	fd	)
```

Gets information about planes.

Gets a list of plane resources for a DRM device. A DRM application typically calls this function early to identify the available display layers.

By default, the information returned includes only "Overlay" type (regular) planes – not "Primary" and "Cursor" planes. If DRM_CLIENT_CAP_UNIVERSAL_PLANES has been enabled with drmSetClientCap, the information returned includes "Primary" planes representing CTRCs, and "Cursor" planes representing Cursors. This allows CRTCs and Cursors to be manipulated with plane functions such as drmModeSetPlane.

###### Postcondition

If the call is successful, the application must free the plane information structure by calling drmModeFreePlaneResources.

###### Note

DRM currently does not implement "Cursor" type planes.

###### Parameters

```text
fd	The file descriptor of an open DRM device.
```

###### Returns

```text
A drmModeResPtr structure if successful, or NULL otherwise.
```

##### ◆ drmModeGetProperty()

```c
drmModePropertyPtr drmModeGetProperty	(	int 	fd,
                                            uint32_t 	propertyId 
)
```

Gets a property structure that describes a property of a DRM object.

The DRM object can be a plane, a CRTC, or a connector.

This function operates on a drmModeObjectPropertiesPtr structure returned by drmModeObjectGetProperties().

The modifiable properties depend on the DRM object type:

1. For a plane (object type DRM_MODE_OBJECT_PLANE):

    ```text
    "SRC_X", "SRC_Y", "SRC_W", "SRC_H", "zpos", "alpha" "CRTC_X",
    "CRTC_Y", "CRTC_W", "CRTC_H", "CRTC_ID", "FB_ID"
    ```

2. For a CRTC (object type DRM_MODE_OBJECT_CRTC), supported values are:

    ```text
    "MODE_ID", "ACTIVE", "HDR_SUPPORTED", "HDR_METADATA_SMPTE_2086_ID"
    ```

3. For a connector (object type DRM_MODE_OBJECT_CONNECTOR), the supported value is:

    ```text
    "CRTC_ID"
    ```

For DRM planes, the enums field holds a list of key-word pairs (name : value) that defines the properties.

```c
drmModePropertyPtr->enums[ ].name
drmModePropertyPtr->enums[ ].value
```

1. Supported values for the name field are defined above (i.e., "SRC_X", "SRC_Y", or "SRC_W"). This field is modifiable.
2. Supported values for the value fields are:

```text
"Primary", "Overlay", "Cursor" 
```

This field is read-only.

To identify the plane type, iterate through the following list to locate the enum whose value field matches the one you seek. Then, get the value from corresponding name field.

```c
drmModePropertyPtr->enums[ ] 
```

For example:

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

If the call is successful, the application must free the property information structure by calling drmModeFreeProperty.

###### Note

The zpos value for a plane is initialized with an offset of 10 relative to the next plane. This is to allow for flexible configuration of heads. For example:

1. "Primary" type Plane zpos = 10
2. First "Overlay" Plane zpos = 20
3. Next "Overlay" Plane zpos = 30
4. Etc.

The allowed range for zpos is [0, 255]. Planes with numerically greater values for zpos occlude planes with numerically lesser values.
The alpha value for a plane causes a plane-wide transparency to be applied as well as the per-pixel alpha contained in the buffer object. The allowed range for alpha is [0, 255], where 0 is fully transparent and 255 indicates that only per-pixel alpha has an effect. For non-alpha pixel formats, there is no per-pixel alpha, so 255 indicates fully opaque.

###### Parameters

```text
fd:	The file descriptor of an open DRM device.
propertyId:	Property ID of the property object to be fetched.
```

###### Returns

```text
A drmModePropertyPtr if successful, or NULL otherwise.
```

##### ◆ drmModeGetResources()

```c
drmModeResPtr drmModeGetResources	(	int 	fd	)
```

Gets information about a DRM device's CRTCs, encoders, and connectors.

Gets a list of a DRM device's major resources. A DRM application typically calls this function early to identify available displays and other resources. The function does not report plane resources, though. These can be queried with drmModeGetPlaneResources.

###### Postcondition

If the call is successful, the application must free the resource information structure by calling drmModeFreeResources.

###### Note

The drmModeResPtr structure's min_width, min_height, max_width, and max_height members are set to placeholder values.

###### Parameters

```text
fd	The file descriptor of an open DRM device.

```

###### Returns

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

Gets all properties of a DRM object.

Gets an object properties structure that describes all of the atomically modifiable properties of a specified DRM object, as well as read-only properties not included in the corresponding drmModeCrtcPtr, drmModeConnectorPtr, and drmModePlanePtr structures. You can then retrieve individual properties with drmModeGetProperty and change their values with drmModeAtomicAddProperty.

The drmModeObjectPropertiesPtr structure contains an array of property IDs (props), an array of corresponding property values (prop_values), and the number of elements in each array (count_props). You can get the name of a property by calling drmModeGetProperty on the property ID and looking at the returned drmModePropertyPtr structure's name field.

To modify a property atomically, create a drmModeAtomicReqPtr request object by calling drmModeAtomicAlloc, then call drmModeAtomicAddProperty, specifying the drmModeAtomicReqPtr object, the object ID of the object to modify, the property ID of the property to modify, and the property's new value. Then commit the request with drmModeAtomicCommit. You can set several properties in an atomic request and commit them in a single operation.

###### Postcondition

If the call is successful, the application must free the drmModeObjectPropertiesPtr structure by calling drmModeFreeObjectProperties.

###### Note

Not all object types are supported.

###### Parameters

```text
fd:	The file descriptor of an open DRM device.
object_id:	The object ID of the DRM object whose properties are to be retrieved.
object_type:	A symbol representing an object type. The following object types are supported:
    DRM_MODE_OBJECT_CRTC
    DRM_MODE_OBJECT_CONNECTOR
    DRM_MODE_OBJECT_PLANE
```

###### Returns

```text
A drmModeObjectPropertiesPtr object if successful, or NULL otherwise.
```

##### ◆ drmModeRmFB()

```c
int drmModeRmFB	(	int 	fd,
                    uint32_t 	fb_id 
)
```

Destroys a framebuffer.

Destroys (frees) a framebuffer allocated by drmModeAddFB or drmModeAddFB2.

###### Postcondition

###### Note

###### Parameters

```text
fd	The file descriptor of an open DRM device.
fb_id	The ID of the framebuffer to destroy.
```

###### Returns

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

Sets a CRTC configuration.

If the DRM mode is specified (if drm_mode is not NULL), sets the display mode on the CRTC and specified connector(s). New fb_id, x, and y properties will set at vblank.

###### Postcondition

###### Note

The fb_id, x, and y parameters accept the special input value -1, which indicates that the hardware window framebuffer or the corresponding offset is not to be changed. (Kernel based DRM drivers accept -1 only for fb_id. They return error code -ERANGE if given -1 for x or y.)
It is permitted to specify a valid mode and fb_id==-1, even if no framebuffer is currently attached to the CRTC. The function will set the display mode but will leave the CRTC framebuffer undefined.
Framebuffers set on a CRTC, whether by drmModeSetCrtc, drmModePageFlip, or any other means, are displayed behind planes. The CRTC display layer is the lowest in stacking order.

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

###### Returns

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

Changes a plane's framebuffer and position.

###### Postcondition

###### Note

The crtc_... and src_... parameters accept the special input value -1, which indicates that the hardware offset value is not to be changed. (Kernel based DRM drivers return the error code -ERANGE when given this value.)
Framebuffers set on planes are displayed on top of CRTCs. The stacking order of planes is indicated by the order that the planes are reported by drmModeGetPlaneResources.
All drmModeSetPlane operations are synced to vblank and are blocking.

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

###### Returns

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

Enables or disables DRM features (capabilities).

###### Postcondition

###### Note

###### Parameters

```text

fd:	         The file descriptor of an open DRM device.
capability：	Specifies the capability to be enabled or disabled. Supported values are:
                    DRM_CLIENT_CAP_ATOMIC (disabled by default)
                    DRM_CLIENT_CAP_UNIVERSAL_PLANES (disabled by default)
value:  	 0 to disable the capability, or 1 to enable it.
```

###### Returns

```text
0 if successful, or -EINVAL otherwise.
```

##### ◆ drmWaitVBlank()

```c
int drmWaitVBlank	(	int 	fd,
drmVBlankPtr 	vbl 
)
```

Waits for a vertical blanking interval (vblank).

Waits for a specified vblank, or requests that the registered vblank handler be called when a specified vblank occurs.

###### Postcondition

###### Note

currently does not support all drmVblankPtr fields.

###### Parameters

```text
fd:	    The file descriptor of an open DRM device.
vbl:	A description of the requested vblank. The vbl->type field must contain one of these values:
           DRM_VBLANK_ABSOLUTE: request.sequence is the vblank count since some point in the past, e.g. system boot.
           DRM_VBLANK_RELATIVE: request.sequence is the vblank count from the current value. e.g. 1 specifies the next vblank. The value may be bitwise ORed with any combination of these values:
           DRM_VBLANK_SECONDARY: Uses the secondary display's vblank.
           DRM_VBLANK_EVENT: Returns immediately and triggers the event callback instead of waiting for a specified vblank.
```

###### Returns

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

Requests a page flip (framebuffer change) on the specified CRTC.

Schedules a page flip on the specified CRTC. By default, the CRTC will be reprogrammed to display the specified framebuffer after the next vertical refresh.

###### Note

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

###### Returns

```text
0	if successful.
-EINVAL	if crtc_id or fb_id is invalid.
-errno	otherwise.
```
<!-- markdownlint-enable header-increment no-hard-tabs -->
## 3.3 k510 DRM 新增画框函数使用说明

结构体定义

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

宏定义

```c
define DRM_KENDRYTE_DRAW_FRAME         0x00

#define DRM_IOCTL_KENDRYTE_DRAW_FRAME   DRM_IOWR(DRM_COMMAND_BASE + \
                DRM_KENDRYTE_DRAW_FRAME, struct vo_draw_frame)
```

画框函数

```c
static int draw_frame(struct vo_draw_frame *frame)
{
    return drmIoctl(drm_dev.fd, DRM_IOCTL_KENDRYTE_DRAW_FRAME, frame);
}
```

**翻译免责声明**  
为方便客户，Canaan 使用 AI 翻译程序将文本翻译为多国语言，它可能包含错误。我们不保证提供的译文的准确性、可靠性或时效性。对于因依赖已翻译信息的准确性或可靠性而造成的任何损失或损害，Canaan 概不负责。如果不同语言翻译之间存在内容差异，以简体中文版本为准。

如果您要报告翻译错误或不准确的问题，欢迎通过邮件与我们联系。