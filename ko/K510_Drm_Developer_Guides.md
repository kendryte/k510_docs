![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 Direct Rendering Manager 개발 가이드</font>**

<font face="黑体"  size=3>문서 버전: P0.1.0</font>

<font face="黑体"  size=3>게시 날짜: 2022-01-01</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**면책 조항**</font>
귀하가 구매한 제품, 서비스 또는 기능은 베이징 Jiananges 정보 기술 유한 회사(이하 "회사")의 상업 계약 및 약관의 적용을 받으며, 이 문서에 설명된 제품, 서비스 또는 기능의 전부 또는 일부는 구매 또는 사용의 범위를 벗어납니다. 계약에 달리 합의하지 않는 한, 회사는 본 문서의 진술, 정보, 내용의 정확성, 신뢰성, 완전성, 마케팅, 특정 목적 및 비침략성에 대해 명시적 또는 묵시적으로 어떠한 진술이나 보증도 하지 않습니다. 달리 합의하지 않는 한, 이 문서는 사용 지침의 참조로만 사용됩니다.
이 문서의 내용은 제품 버전 업그레이드 또는 기타 이유로 인해 예고 없이 수시로 업데이트되거나 수정될 수 있습니다. 

**<font face="黑体"  size=3>상표 고지</font>**

베이징 <img src="../zh/images/canaan-logo.png" style="zoom:33%;" />Jianan Jets 정보 기술 유한 공사의 상표는 Jianan, Jianan 및 Jianan의 다른 상표입니다. 이 문서에 언급될 수 있는 기타 모든 상표 또는 등록 상표는 해당 소유자가 소유합니다. 

**<font face="黑体"  size=3>저작권 ©2022 베이징 Jiananjets 정보 기술 유한 회사</font>**
이 문서는 K510 플랫폼 개발 및 설계에만 적용되며, 어떠한 단위나 개인도 회사의 서면 허가 없이 이 문서의 일부 또는 전부를 어떤 형태로든 배포할 수 없습니다. 

**<font face="黑体"  size=3>베이징 Jiananjets 정보 기술 유한 회사</font>**
웹 사이트: canaan-creative.com
비즈니스 문의: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# 서문
**<font face="黑体"  size=5>문서의 목적</font>**
이 문서는 엔지니어가 더 빠르게 작업할 수 있도록 설계된 Direct Rendering Manager용 설명서를 개발합니다

**<font face="黑体"  size=5>독자 개체입니다</font>**

이 문서(이 가이드)가 주로 적용되는 사람:

- 소프트웨어 개발자
- 기술 지원 담당자

**<font face="黑体"  size=5>레코드를 수정합니다</font>**
 <font face="宋体"  size=2>개정 레코드에는 각 문서 업데이트에 대한 설명이 누적됩니다. 문서의 최신 버전에는 이전 버전의 모든 업데이트가 포함되어 있습니다. </font>

| 버전 번호입니다   | 수정자     | 개정일입니다 | 개정 지침 |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | 시스템 소프트웨어 그룹입니다 | 2022-03-22 |          |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>카탈로그</font>**

[목차]

<div style="page-break-after:always"></div>

# 1 소개

현재 sdk에서 사용하는 Linux 버전은 4.17.0입니다. Linux, 전체 이름 GNU/Linux, 무료 사용 및 무료 확산 클래스 UNIX 운영 체제, 리누스 베나딕트 토바즈에 의해 처음 출시 된 커널 1991년 10월 5일, 주로 미니 엑스와 유닉스 아이디어에서 영감을, POSIX 기반 다중 사용자, 멀티 태스킹, 멀티 스레드 및 멀티 CPU 운영 체제. 주요 유닉스 도구 소프트웨어, 응용 프로그램 및 네트워크 프로토콜을 실행합니다. 32비트 및 64비트 하드웨어를 지원합니다. Linux는 유닉스의 네트워크 중심 설계 아이디어를 계승하며 안정적인 다중 사용자 네트워크 운영 체제입니다. Linux에는 커뮤니티 기반 Debian, archlinux, 상용 개발 기반 Red Hat Enterprise Linux, SUSE, Oracle Linux 등 수백 가지 배포판이 있습니다.

Direct Rendering Manager는 최신 [비디오 카드의 ](https://en.wikipedia.org/wiki/Linux_kernel)GPU 연결을 담당하는 [Linux 커널](https://en.wikipedia.org/wiki/Video_cards)[의 하위 시스템입니다](https://en.wikipedia.org/wiki/Graphics_processing_unit). DRM은[](https://en.wikipedia.org/wiki/Application_programming_interface) [사용자 공간 ](https://en.wikipedia.org/wiki/User-space)프로그램이 GPU에 명령과 데이터를 보내고 디스플레이 모드 설정 구성과 같은 작업을 수행하는 데 사용할 수 있는 API를[ 노출합니다. ](https://en.wikipedia.org/wiki/Mode_setting)DRM은 원래 [X Server](https://en.wikipedia.org/wiki/X.Org_Server)[Direct Rendering Infrastructure](https://en.wikipedia.org/wiki/Direct_Rendering_Infrastructure)[[1\]](https://en.wikipedia.org/wiki/Direct_Rendering_Manager#cite_note-DRM_readme-1)[의 커널 공간 ](https://en.wikipedia.org/wiki/Kernel-space)구성 요소로 개발되었지만, 그 이후로 다른 그래픽 스택 대안(예:[ Wayland )를](https://en.wikipedia.org/wiki/Wayland_(display_server_protocol)) 사용합니다. 

사용자 공간 프로그램은 DRM API 명령 GPU를 사용하여[ 하드웨어 가속](https://en.wikipedia.org/wiki/Hardware_acceleration) [3D 렌더링](https://en.wikipedia.org/wiki/3D_rendering) 및 [비디오 디코딩](https://en.wikipedia.org/wiki/Video_decoding)뿐만 아니라[ GPUPU 계산을](https://en.wikipedia.org/wiki/General-purpose_computing_on_graphics_processing_units) 수행할 수 있습니다. 

# 2 하드웨어 소개

## 2.1 획득 방법

sdk를 다운로드하고 컴파일하면 sdk가 컴파일될 때 linux 코드가 다운로드되고 컴파일됩니다.

sdk의 다운로드 및 컴파일 방법은[ K510_SDK_Build_and_Burn_Guide ](./K510_SDK_Build_and_Burn_Guide.md)참조하십시오. 

## 2.2 파일 및 디렉토리를 구동합니다

```text
drivers/gpu/drm/canaan/
```

## 2.3 개발 환경 요구 사항

아니요, 없습니다

## 2.4 운영 체제

Linux 시스템 및 버전 번호 지원은 다음 그림과 같습니다.

| 번호입니다 | 소프트웨어 리소스 | 설명합니다        |
| ---- | -------- | ----------- |
| 1    | 우분투   | 18.04/20.04 |
|      |          |             |
|      |          |             |
|      |          |             |

## 2.5 소프트웨어 환경

소프트웨어 환경 요구 사항은 다음 표에 나와 있습니다.

| 번호입니다 | 소프트웨어 리소스 | 설명합니다 |
| :--- | -------- | ---- |
| 1    | K510 SDK | v1.1 버전 |
|      |          |      |
|      |          |      |
|      |          |      |

# 3직접 렌더링 관리자

## 3.1 연결 참조

엔비디아 DRM:<https://docs.nvidia.com/jetson/l4t-multimedia/group__direct__rendering__manager.html>

DRM 프리 데스크톱 :<https://cgit.freedesktop.org/mesa/drm>
<https://gitlab.freedesktop.org/mesa/drm>

## 3.2 drm 공식 사용 api
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

프레임 버퍼를 만듭니다.

이 함수는 지정된 버퍼 개체를 메모리 백업 저장소로 사용하여 지정된 크기와 형식의 프레임 버퍼를 만듭니다. 버퍼 객체는 요청 매개 변수가 DRM_IOCTL_MODE_CREATE_DUMB로 설정된 drmIoctl 호출에 의해 생성 된 "멍청한 버퍼"이거나 drmPrimeFDToHandle 함수에 대한 호출로 가져온 dma-buf 일 수 있습니다.

###### 사후 조건

호출이 성공하면 응용 프로그램은 drmModeRmFB를 호출하여 프레임 버퍼를 제거(해제)해야 합니다.

###### 매개 변수

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

###### 반환

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

형식과 평면을 지정하는 프레임 버퍼를 만듭니다.

이 기능은 :d rmModeAddFB와 유사하지만 더 많은 옵션을 제공합니다. 버퍼 객체의 픽셀 형식은 drmModeAddFB에서와 같이 depth+bpp가 아닌 명시적으로 지정됩니다. 또한 다중 평면 YUV 형식도 지원됩니다. drmModeAddFB의 경우, 버퍼 객체 핸들은 바보 버퍼 또는 가져온 dma-bufs 일 수 있습니다.

###### 사후 조건

호출이 성공하면 응용 프로그램은 drmModeRmFB를 호출하여 프레임 버퍼를 제거(해제)해야 합니다.

###### 메모

flags 매개변수는 현재 지원되지 않습니다.

###### 매개 변수

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

###### 반환

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

형식과 평면을 지정하는 프레임 버퍼를 만듭니다.
이 함수는 :d rmModeAddFB2와 유사하지만 수정자를 허용합니다.

###### 사후 조건

호출이 성공하면 응용 프로그램은 drmModeRmFB를 호출하여 프레임 버퍼를 제거(해제)해야 합니다.

###### 메모

###### 매개 변수

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

###### 반환

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

원자 요청에 속성을 추가합니다.
원자 요청에 속성과 값을 추가합니다.

###### 사후 조건

###### 메모

###### 매개 변수

```text
req:	     An atomic request.
object_id:	 Object ID of a CRTC, plane, or connector to be modified.
property_id: Property ID of the property to be modified.
value:	     The new value for the property.
```

###### 반환

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

하드웨어에 원자 속성 변경 요청을 커밋합니다.

drmModeAtomicReqPtr 구조의 모든 속성 변경 사항을 하드웨어로 보냅니다.

###### 사후 조건

###### 메모

###### 매개 변수

```text
fd:	The file descriptor of an open DRM device.
req:	The request object describing properties to commit.
flags:	Flags which influence the operation. The supported flags are:
        DRM_MODE_PAGE_FLIP_ASYNC: Commits values immediately when possible; does not latch new properties at the next vblank.
        DRM_MODE_ATOMIC_NONBLOCK: Commits values to hardware but does not wait for hardware to accept the new values.
        DRM_MODE_ATOMIC_TEST_ONLY: Validates input, but does not commit the values to hardware.
user_data :	Unused.
```

###### 반환

```text
0	if successful.
-1	if req is NULL.
-EINVAL	if DRM_CLIENT_CAP_ATOMIC is not enabled, the value of flags is illegal, or atomic property IDs in the request are not recognized.
```

##### ◆ drmModeAtomicFree()

```c
void drmModeAtomicFree	(	drmModeAtomicReqPtr 	req	)
```

원자 요청을 해제합니다.

drmModeAtomicAlloc에 의해 할당된 drmModeAtomicReqPtr 객체와 연관된 모든 drmModeAtomicReqItemPtr 객체를 해제합니다.

###### 사후 조건

###### 메모

###### 매개 변수

```text
req	:The atomic request object to be freed.
```

###### 반환

```text
NULL
```

##### ◆ drmModeFreeConnector()

```c
void drmModeFreeConnector	(	drmModeConnectorPtr 	ptr	)
```

커넥터를 해제합니다.

drmModeGetConnector에 의해 할당된 drmModeConnectorPtr 구조를 해제합니다.

###### 사후 조건

###### 메모

###### 매개 변수

```text
ptr	A pointer to the connector to be freed.
```

###### 반환

```text
null
```

##### ◆ drmModeFreeObjectProperties()

```c
void drmModeFreeObjectProperties	(	drmModeObjectPropertiesPtr 	ptr	)
```

객체 속성 구조를 해제합니다.

drmModeObjectPropertiesPtr 구조를 해제하여 drmModeObjectGetProperties에 의해 할당됩니다.

###### 사후 조건

###### 메모

###### 매개 변수

```text
ptr	A pointer to the object properties structure to be freed.
```

###### 반환

```text
null
```

##### ◆ drmModeFreePlaneResources()

```c
void drmModeFreePlane	(	drmModePlanePtr 	ptr	)
```

비행기를 해제합니다.

drmModeGetPlane에 의해 할당된 drmModePlanePtr 구조를 해제합니다.

###### 사후 조건

###### 메모

###### 매개 변수

```text
ptr	A pointer to the plane to be freed.
```

###### 반환

```text
null
```

##### ◆ drmModeFreeProperty()

```c
void drmModeFreeProperty	(	drmModePropertyPtr 	ptr	)
```

속성 구조를 해제합니다.

drmModeGetProperty에 의해 할당된 drmModePropertyPtr 구조를 해제합니다.

###### 사후 조건

###### 메모

###### 매개 변수

```text
ptr	A pointer to a property structure returned by drmModeGetProperty.
```

###### 반환

```text
null
```

##### ◆ drmModeFreeResources()

```c
void drmModeFreeResources	(	drmModeResPtr 	ptr	)
```

리소스 정보 구조를 해제합니다.

drmModeGetResources에 의해 할당된 drmModeResPtr 구조를 해제합니다.

###### 사후 조건

###### 메모

###### 매개 변수

```text
ptr	A pointer to the resource to be freed.
```

###### 반환

```text
null
```

##### ◆ drmModeGetConnector()

```c
drmModeConnectorPtr drmModeGetConnector	(	int 	fd,
                                           uint32_t 	connector_id 
)
```

커넥터에 대한 정보를 가져옵니다.

connector_id가 유효한 경우 사용 가능한 모드, 연결 상태, 커넥터 유형 및 연결된 인코더(있는 경우)와 같은 커넥터에 대한 정보가 포함된 drmModeConnectorPtr 구조를 가져옵니다.

###### 사후 조건

호출이 성공하면 응용 프로그램은 drmModeFreeConnector를 호출하여 커넥터 정보 구조를 해제해야 합니다.

###### 메모

커넥터->mm너비 및 커넥터->mmHeight는 현재 자리 표시자 값으로 설정되어 있습니다.

###### 매개 변수

```text
fd :	        The file descriptor of an open DRM device.
connector_id:	The connector ID of the connector to be retrieved.
```

###### 반환

```text
A drmModeConnectorPtr structure if successful, or NULL if the connector is not found or the API is out of memory.
```

##### ◆ drmModeGetPlaneResources()

```c
drmModePlaneResPtr drmModeGetPlaneResources	(	int 	fd	)
```

평면에 대한 정보를 가져옵니다.

DRM 장치에 대한 평면 리소스 목록을 가져옵니다. DRM 애플리케이션은 일반적으로 사용 가능한 디스플레이 레이어를 식별하기 위해 이 함수를 일찍 호출합니다.

기본적으로 반환되는 정보에는 "기본" 및 "커서" 평면이 아닌 "오버레이" 유형(일반) 평면만 포함됩니다. drmSetClientCap을 사용하여 DRM_CLIENT_CAP_UNIVERSAL_PLANES을 사용하도록 설정한 경우 반환되는 정보에는 CTRC를 나타내는 "기본" 평면과 커서를 나타내는 "커서" 평면이 포함됩니다. 이를 통해 CRTC 및 커서를 drmModeSetPlane과 같은 평면 함수로 조작할 수 있습니다.

###### 사후 조건

호출이 성공하면 응용 프로그램은 drmModeFreePlaneResources를 호출하여 평면 정보 구조를 해제해야 합니다.

###### 메모

DRM은 현재 "커서"유형 평면을 구현하지 않습니다.

###### 매개 변수

```text
fd	The file descriptor of an open DRM device.
```

###### 반환

```text
A drmModeResPtr structure if successful, or NULL otherwise.
```

##### ◆ drmModeGetProperty()

```c
drmModePropertyPtr drmModeGetProperty	(	int 	fd,
                                            uint32_t 	propertyId 
)
```

DRM 개체의 속성을 설명하는 속성 구조를 가져옵니다.

DRM 개체는 평면, CRTC 또는 커넥터일 수 있습니다.

이 함수는 drmModeObjectGetProperties()에서 반환된 drmModeObjectPropertiesPtr 구조에서 작동합니다.

수정 가능한 속성은 DRM 개체 유형에 따라 다릅니다.

1. 평면(객체 유형 DRM_MODE_OBJECT_PLANE)의 경우:

    ```text
    "SRC_X", "SRC_Y", "SRC_W", "SRC_H", "zpos", "alpha" "CRTC_X",
    "CRTC_Y", "CRTC_W", "CRTC_H", "CRTC_ID", "FB_ID"
    ```

2. CRTC(개체 유형 DRM_MODE_OBJECT_CRTC)의 경우 지원되는 값은 다음과 같습니다.

    ```text
    "MODE_ID", "ACTIVE", "HDR_SUPPORTED", "HDR_METADATA_SMPTE_2086_ID"
    ```

3. 커넥터(개체 유형 DRM_MODE_OBJECT_CONNECTOR)의 경우 지원되는 값은 다음과 같습니다.

    ```text
    "CRTC_ID"
    ```

DRM 평면의 경우 열거형 필드에는 속성을 정의하는 키워드 쌍(이름: 값) 목록이 있습니다.

```c
drmModePropertyPtr->enums[ ].name
drmModePropertyPtr->enums[ ].value
```

1. 이름 필드에 대해 지원되는 값은 위에 정의되어 있습니다(예: "SRC_X", "SRC_Y" 또는 "SRC_W"). 이 필드는 수정할 수 있습니다.
2. 값 필드에 대해 지원되는 값은 다음과 같습니다.

```text
"Primary", "Overlay", "Cursor" 
```

이 필드는 읽기 전용입니다.

평면 유형을 식별하려면 다음 목록을 반복하여 값 필드가 원하는 것과 일치하는 열거형을 찾습니다. 그런 다음 해당 이름 필드에서 값을 가져옵니다.

```c
drmModePropertyPtr->enums[ ] 
```

예를 들어:

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

###### 사후 조건

호출이 성공하면 응용 프로그램은 drmModeFreeProperty를 호출하여 속성 정보 구조를 해제해야 합니다.

###### 메모

평면의 zpos 값은 다음 평면을 기준으로 오프셋 10으로 초기화됩니다. 이것은 머리의 유연한 구성을 허용하기위한 것입니다. 예를 들어:

1. "기본" 유형 평면 zpos = 10
2. 첫 번째 "오버레이"평면 zpos = 20
3. 다음 "오버레이"평면 zpos = 30
4. 등.

zpos에 허용되는 범위는 입니다 [0, 255]. zpos에 대해 숫자로 더 큰 값을 가진 평면은 숫자로 더 작은 값을 갖는 평면을 폐색합니다.
평면의 알파 값을 사용하면 버퍼 객체에 포함된 픽셀당 알파뿐만 아니라 평면 전체 투명도가 적용됩니다. 알파에 허용되는 범위는 0이 [0, 255]완전히 투명하고 255는 픽셀당 알파만 효과가 있음을 나타냅니다. 알파가 아닌 픽셀 형식의 경우 픽셀당 알파가 없으므로 255는 완전히 불투명함을 나타냅니다.

###### 매개 변수

```text
fd:	The file descriptor of an open DRM device.
propertyId:	Property ID of the property object to be fetched.
```

###### 반환

```text
A drmModePropertyPtr if successful, or NULL otherwise.
```

##### ◆ drmModeGetResources()

```c
drmModeResPtr drmModeGetResources	(	int 	fd	)
```

DRM 장치의 CRTC, 인코더 및 커넥터에 대한 정보를 가져옵니다.

DRM 장치의 주요 리소스 목록을 가져옵니다. DRM 응용 프로그램은 일반적으로 사용 가능한 디스플레이 및 기타 리소스를 식별하기 위해 이 함수를 일찍 호출합니다. 하지만 이 함수는 평면 리소스를 보고하지 않습니다. drmModeGetPlaneResources를 사용하여 쿼리할 수 있습니다.

###### 사후 조건

호출이 성공하면 응용 프로그램은 drmModeFreeResources를 호출하여 리소스 정보 구조를 해제해야 합니다.

###### 메모

drmModeResPtr 구조의 min_width, min_height, max_width 및 max_height 멤버는 자리 표시자 값으로 설정됩니다.

###### 매개 변수

```text
fd	The file descriptor of an open DRM device.

```

###### 반환

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

DRM 개체의 모든 속성을 가져옵니다.

지정된 DRM 개체의 원자적으로 수정할 수 있는 모든 속성과 해당 drmModeCrtcPtr, drmModeConnectorPtr 및 drmModePlanePtr 구조에 포함되지 않은 읽기 전용 속성을 설명하는 개체 속성 구조를 가져옵니다. 그런 다음 drmModeGetProperty를 사용하여 개별 속성을 검색하고 drmModeAtomicAddProperty를 사용하여 해당 값을 변경할 수 있습니다.

drmModeObjectPropertiesPtr 구조체에는 속성 ID(props) 배열, 해당 속성 값(prop_values)의 배열 및 각 배열의 요소 수(count_props)가 포함되어 있습니다. 속성 ID에서 drmModeGetProperty를 호출하고 반환된 drmModePropertyPtr 구조체의 이름 필드를 확인하여 속성의 이름을 가져올 수 있습니다.

속성을 원자적으로 수정하려면 drmModeAtomicAlloc을 호출하여 drmModeAtomicReqPtr 요청 개체를 만든 다음 drmModeAtomicAddProperty를 호출하여 drmModeAtomicReqPtr 개체, 수정할 개체의 개체 ID, 수정할 속성의 속성 ID 및 속성의 새 값을 지정합니다. 그런 다음 drmModeAtomicCommit을 사용하여 요청을 커밋하십시오. 원자 요청에서 여러 속성을 설정하고 단일 작업으로 커밋 할 수 있습니다.

###### 사후 조건

호출이 성공하면 응용 프로그램은 drmModeFreeObjectProperties를 호출하여 drmModeObjectPropertiesPtr 구조를 해제해야 합니다.

###### 메모

모든 개체 유형이 지원되는 것은 아닙니다.

###### 매개 변수

```text
fd:	The file descriptor of an open DRM device.
object_id:	The object ID of the DRM object whose properties are to be retrieved.
object_type:	A symbol representing an object type. The following object types are supported:
    DRM_MODE_OBJECT_CRTC
    DRM_MODE_OBJECT_CONNECTOR
    DRM_MODE_OBJECT_PLANE
```

###### 반환

```text
A drmModeObjectPropertiesPtr object if successful, or NULL otherwise.
```

##### ◆ drmModeRmFB()

```c
int drmModeRmFB	(	int 	fd,
                    uint32_t 	fb_id 
)
```

프레임 버퍼를 파괴합니다.

drmModeAddFB 또는 drmModeAddFB2에 의해 할당된 프레임 버퍼를 파괴(해제)합니다.

###### 사후 조건

###### 메모

###### 매개 변수

```text
fd	The file descriptor of an open DRM device.
fb_id	The ID of the framebuffer to destroy.
```

###### 반환

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

CRTC 구성을 설정합니다.

DRM 모드가 지정된 경우(drm_mode이 NULL이 아닌 경우) CRTC 및 지정된 커넥터에서 디스플레이 모드를 설정합니다. 새 fb_id, x 및 y 속성은 vblank에서 설정됩니다.

###### 사후 조건

###### 메모

fb_id, x 및 y 매개 변수는 하드웨어 윈도우 프레임 버퍼 또는 해당 오프셋이 변경되지 않음을 나타내는 특수 입력 값 -1을 허용합니다. 커널 기반 DRM 드라이버는 fb_id에 대해서만 -1을 허용합니다. x 또는 y에 대해 -1이 지정된 경우 오류 코드 -ERANGE를 반환합니다.)
현재 CRTC에 연결된 프레임 버퍼가 없더라도 유효한 모드와 fb_id==-1을 지정할 수 있습니다. 이 함수는 디스플레이 모드를 설정하지만 CRTC 프레임 버퍼는 정의되지 않은 상태로 둡니다.
drmModeSetCrtc, drmModePageFlip 또는 다른 수단에 관계없이 CRTC에 설정된 프레임 버퍼가 평면 뒤에 표시됩니다. CRTC 디스플레이 레이어는 스태킹 순서에서 가장 낮습니다.

###### 매개 변수

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

###### 반환

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

평면의 프레임 버퍼와 위치를 변경합니다.

###### 사후 조건

###### 메모

crtc_... 그리고 src_ ... 매개 변수는 하드웨어 오프셋 값이 변경되지 않음을 나타내는 특수 입력 값 -1을 받아들입니다. (커널 기반 DRM 드라이버는 이 값이 주어지면 오류 코드 -ERANGE를 반환합니다.)
평면에 설정된 프레임 버퍼는 CRTC 위에 표시됩니다. 평면의 겹침 순서는 drmModeGetPlaneResources에서 평면을 보고하는 순서로 표시됩니다.
모든 drmModeSetPlane 작업이 vblank에 동기화되고 차단됩니다.

###### 매개 변수

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

###### 반환

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

DRM 기능(기능)을 사용하거나 사용하지 않도록 설정합니다.

###### 사후 조건

###### 메모

###### 매개 변수

```text

fd:	         The file descriptor of an open DRM device.
capability：	Specifies the capability to be enabled or disabled. Supported values are:
                    DRM_CLIENT_CAP_ATOMIC (disabled by default)
                    DRM_CLIENT_CAP_UNIVERSAL_PLANES (disabled by default)
value:  	 0 to disable the capability, or 1 to enable it.
```

###### 반환

```text
0 if successful, or -EINVAL otherwise.
```

##### ◆ drmWaitVBlank()

```c
int drmWaitVBlank	(	int 	fd,
drmVBlankPtr 	vbl 
)
```

수직 블랭킹 간격(vblank)을 기다립니다.

지정된 vblank를 기다리거나 지정된 vblank가 발생할 때 등록된 vblank 처리기를 호출하도록 요청합니다.

###### 사후 조건

###### 메모

현재 모든 drmVblankPtr 필드를 지원하지는 않습니다.

###### 매개 변수

```text
fd:	    The file descriptor of an open DRM device.
vbl:	A description of the requested vblank. The vbl->type field must contain one of these values:
           DRM_VBLANK_ABSOLUTE: request.sequence is the vblank count since some point in the past, e.g. system boot.
           DRM_VBLANK_RELATIVE: request.sequence is the vblank count from the current value. e.g. 1 specifies the next vblank. The value may be bitwise ORed with any combination of these values:
           DRM_VBLANK_SECONDARY: Uses the secondary display's vblank.
           DRM_VBLANK_EVENT: Returns immediately and triggers the event callback instead of waiting for a specified vblank.
```

###### 반환

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

###### 사후 조건

지정된 CRTC에서 페이지 뒤집기(프레임 버퍼 변경)를 요청합니다.

지정된 CRTC에서 페이지 플립을 예약합니다. 기본적으로 CRTC는 다음 수직 새로 고침 후에 지정된 프레임 버퍼를 표시하도록 다시 프로그래밍됩니다.

###### 메모

###### 매개 변수

```text
fd :	    The file descriptor of an open DRM device.
crtc_id :	CRTC ID of the CRTC whose framebuffer is to be changed.
fb_id :	    Framebuffer ID of the framebuffer to be displayed.
flags :	    Flags affecting the operation. Supported values are:
                  DRM_MODE_PAGE_FLIP_ASYNC: Flip immediately, not at vblank.
                  DRM_MODE_PAGE_FLIP_EVENT: Send page flip event.
user_data:	Data used by the page flip handler if vblank event was requested.
```

###### 반환

```text
0	if successful.
-EINVAL	if crtc_id or fb_id is invalid.
-errno	otherwise.
```
<!-- markdownlint-enable header-increment no-hard-tabs -->
## 3.3 k510 DRM에 새로운 프레임 함수 사용 지침이 추가되었습니다

구조 정의

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

매크로 정의입니다

```c
define DRM_KENDRYTE_DRAW_FRAME         0x00

#define DRM_IOCTL_KENDRYTE_DRAW_FRAME   DRM_IOWR(DRM_COMMAND_BASE + \
                DRM_KENDRYTE_DRAW_FRAME, struct vo_draw_frame)
```

프레임 함수입니다

```c
static int draw_frame(struct vo_draw_frame *frame)
{
    return drmIoctl(drm_dev.fd, DRM_IOCTL_KENDRYTE_DRAW_FRAME, frame);
}
```

**번역 면책 조항**  
고객의 편의를 위해 Canan은 AI 번역 프로그램을 사용하여 오류를 포함할 수 있는 여러 언어로 텍스트를 번역합니다. 당사는 제공된 번역의 정확성, 신뢰성 또는 적시성을 보장하지 않습니다. Canan은 번역된 정보의 정확성이나 신뢰성에 의존하여 발생하는 손실이나 손해에 대해 책임을 지지 않습니다. 언어 번역 간에 콘텐츠 차이가 있는 경우 중국어 간체 버전이 우선합니다. 

번역 오류 또는 부정확한 문제를 신고하려면 이메일로 문의하시기 바랍니다.