![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 Direct Rendering Manager 開発ガイド</font>**

<font face="黑体"  size=3>ドキュメントのバージョン: P0.1.0</font>

<font face="黑体"  size=3>発売日: 2022-01-01</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**免責事項**</font>
お客様が購入した製品、サービス、または機能は、北京Jiayuan Jetts情報技術有限公司(以下「当社」、以下同じ)の商業契約および条件の対象となり、本書に記載されている製品、サービス、または機能の全部または一部がお客様の購入または使用の範囲外となる場合があります。 契約に別段の定めがない限り、当社は、本書の記述、情報、内容の正確性、信頼性、完全性、マーケティング、特定目的、非攻撃性について、明示または黙示を問わず、いかなる表明または保証も行いません。 特に断りのない限り、このドキュメントは使用ガイダンスの参照としてのみ使用してください。
このドキュメントの内容は、製品バージョンのアップグレードまたはその他の理由により、予告なく随時更新または変更されることがあります。 

**<font face="黑体"  size=3>商標表示</font>**

「<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />」アイコン、カナン、その他の商標は、北京Jiayuan Jets情報技術有限公司の商標です。 本書で言及されるその他すべての商標または登録商標は、それぞれの所有者が所有しています。 

**<font face="黑体"  size=3>©著作権2022北京Jiayuan Jetth情報技術有限公司</font>**
このドキュメントは、K510プラットフォーム開発設計にのみ適用され、当社の書面による許可なく、いかなるユニットまたは個人も、このドキュメントの一部または全部をいかなる形式でも配布することはできません。 

**<font face="黑体"  size=3>北京Jiayuan Jetth情報技術有限公司</font>**
URL: canaan-creative.com
ビジネスお問い合わせ:salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# 序文
**<font face="黑体"  size=5>ドキュメントの目的</font>**
このドキュメントでは、Direct Rendering Manager のマニュアルを開発し、エンジニアがより迅速に作業できるように設計されています

**<font face="黑体"  size=5>リーダー オブジェクト</font>**

このドキュメント (このガイド) は、主に次の担当者に適用されます。

- ソフトウェア開発者
- テクニカル サポート スタッフ

**<font face="黑体"  size=5>レコードを改訂します</font>**
 <font face="宋体"  size=2>リビジョン レコードには、ドキュメントが更新されるたびに説明が蓄積されます。 ドキュメントの最新バージョンには、以前のすべてのバージョンの更新が含まれています。 </font>

| バージョン番号   | 変更者     | 改訂日 | 修正の説明 |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | システム ソフトウェア グループ | 2022-03-22 |          |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>目録</font>**

[目次]

<div style="page-break-after:always"></div>

# 1はじめに

現在、sdk で使用されている Linux のバージョンは 4.17.0 です。 Linux は、すべて GNU/Linux と呼ばれ、1991 年 10 月 5 日に Linas Bennadkte Tovaz によって最初にリリースされたカーネルを持つ、POSIX ベースのマルチユーザー、マルチタスク、マルチスレッドおよびマルチ CPU 対応のオペレーティング システムである Miniix と Unix の思想に触発された、自由に使用および配布できるクラス UNIX オペレーティング システムです。 主要な Unix ツール ソフトウェア、アプリケーション、およびネットワーク プロトコルを実行できます。 32 ビット ハードウェアと 64 ビット ハードウェアの両方をサポートします。 Linux は、Unix のネットワーク中心の設計思想を継承し、安定したパフォーマンスを持つマルチユーザー ネットワーク オペレーティング システムです。 Linux には、コミュニティベースの debian、archlinux、商用開発に基づく Red Hat Enterprise Linux、SUSE、Oracle Linux など、数百の異なるディストリビューションがあります。

Direct Rendering Manager は [Linux カーネル](https://en.wikipedia.org/wiki/Linux_kernel)のサブシステムであり、最新の[ビデオカードとの](https://en.wikipedia.org/wiki/Video_cards)[ GPU](https://en.wikipedia.org/wiki/Graphics_processing_unit) 接続を担当しています。 DRM は[](https://en.wikipedia.org/wiki/Application_programming_interface)、[ユーザー空間](https://en.wikipedia.org/wiki/User-space)プログラムが GPU にコマンドとデータを送信し、ディスプレイ モード設定の構成などの操作を実行するために使用できる API[ を公開します。 ](https://en.wikipedia.org/wiki/Mode_setting)DRM は、もともと[ X Server](https://en.wikipedia.org/wiki/X.Org_Server)[Direct Rendering Infrastructure](https://en.wikipedia.org/wiki/Direct_Rendering_Infrastructure)[[1\] ](https://en.wikipedia.org/wiki/Direct_Rendering_Manager#cite_note-DRM_readme-1)[のカーネル空間](https://en.wikipedia.org/wiki/Kernel-space)コンポーネントとして開発されましたが、それ以来、他のグラフィックス スタックの代替手段 (例:[ Wayland](https://en.wikipedia.org/wiki/Wayland_(display_server_protocol)) ) を使用します。 

ユーザー空間プログラムは、DRM API コマンド GPU を使用して、[ハードウェア アクセラレーション](https://en.wikipedia.org/wiki/Hardware_acceleration) [3D レンダリング](https://en.wikipedia.org/wiki/3D_rendering)と[ビデオ デコード](https://en.wikipedia.org/wiki/Video_decoding)、および [GPGPU 計算を実行できます](https://en.wikipedia.org/wiki/General-purpose_computing_on_graphics_processing_units)。 

# 2 ハードウェアの概要

## 2.1 取得方法

sdk をダウンロードしてコンパイルし、sdk がコンパイルされると linux コードをダウンロードしてコンパイルします。

sdk のダウンロード コンパイル方法については、K510_SDK_Build_and_Burn_Guideを参照してください[](./K510_SDK_Build_and_Burn_Guide.md)。 

## 2.2 ドライブファイルとディレクトリ

```text
drivers/gpu/drm/canaan/
```

## 2.3 開発環境の必要性

なし

## 2.4 オペレーティング システム

Linux システムとバージョン番号のサポートは、次の図のようになります。

| 番号 | ソフトウェア リソース | 命令        |
| ---- | -------- | ----------- |
| 1    | ウブンツ   | 18.04/20.04 |
|      |          |             |
|      |          |             |
|      |          |             |

## 2.5 ソフトウェア環境

ソフトウェア環境の要件を次の表に示します。

| 番号 | ソフトウェア リソース | 命令 |
| :--- | -------- | ---- |
| 1    | K510 SDK | v1.1の |
|      |          |      |
|      |          |      |
|      |          |      |

# 3ダイレクトレンダリングマネージャ

## 3.1 参照接続

nvdia drm:<https://docs.nvidia.com/jetson/l4t-multimedia/group__direct__rendering__manager.html>

DRMフリーデスクトップ:<https://cgit.freedesktop.org/mesa/drm>
<https://gitlab.freedesktop.org/mesa/drm>

## 3.2 drm 公式に一般的に使用される API
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

フレームバッファを作成します。

この関数は、指定されたバッファー オブジェクトをメモリ バッキング ストアとして使用して、指定されたサイズと形式のフレーム バッファーを作成します。バッファー オブジェクトは、要求パラメーターを DRM_IOCTL_MODE_CREATE_DUMB に設定して drmIoctl の呼び出しによって作成された "ダム バッファー" にすることも、drmPrimeFDToHandle 関数の呼び出しによってインポートされた dma-buf にすることもできます。

###### 事後条件

呼び出しが成功した場合、アプリケーションは drmModeRmFB を呼び出してフレーム バッファーを削除 (解放) する必要があります。

###### パラメーター

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

###### 収益

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

フォーマットと平面を指定するフレームバッファを作成します。

この関数は :d rmModeAddFB に似ていますが、より多くのオプションを提供します。バッファー オブジェクトのピクセル形式は、drmModeAddFB のように深さ + bpp ではなく、明示的に指定されます。また、マルチプレーナ YUV 形式もサポートされています。drmModeAddFB に関しては、バッファオブジェクトハンドルはダムバッファまたはインポートされた dma-buf にすることができます。

###### 事後条件

呼び出しが成功した場合、アプリケーションは drmModeRmFB を呼び出してフレーム バッファーを削除 (解放) する必要があります。

###### 手記

flags パラメーターは現在サポートされていません。

###### パラメーター

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

###### 収益

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

フォーマットと平面を指定するフレームバッファを作成します。
この関数は :d rmModeAddFB2 に似ていますが、修飾子を受け入れます。

###### 事後条件

呼び出しが成功した場合、アプリケーションは drmModeRmFB を呼び出してフレーム バッファーを削除 (解放) する必要があります。

###### 手記

###### パラメーター

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

###### 収益

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

アトミック要求にプロパティを追加します。
アトミック要求にプロパティと値を追加します。

###### 事後条件

###### 手記

###### パラメーター

```text
req:	     An atomic request.
object_id:	 Object ID of a CRTC, plane, or connector to be modified.
property_id: Property ID of the property to be modified.
value:	     The new value for the property.
```

###### 収益

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

アトミックなプロパティ変更要求をハードウェアにコミットします。

drmModeAtomicReqPtr 構造体内のすべてのプロパティ変更をハードウェアに送信します。

###### 事後条件

###### 手記

###### パラメーター

```text
fd:	The file descriptor of an open DRM device.
req:	The request object describing properties to commit.
flags:	Flags which influence the operation. The supported flags are:
        DRM_MODE_PAGE_FLIP_ASYNC: Commits values immediately when possible; does not latch new properties at the next vblank.
        DRM_MODE_ATOMIC_NONBLOCK: Commits values to hardware but does not wait for hardware to accept the new values.
        DRM_MODE_ATOMIC_TEST_ONLY: Validates input, but does not commit the values to hardware.
user_data :	Unused.
```

###### 収益

```text
0	if successful.
-1	if req is NULL.
-EINVAL	if DRM_CLIENT_CAP_ATOMIC is not enabled, the value of flags is illegal, or atomic property IDs in the request are not recognized.
```

##### ◆ drmModeAtomicFree()

```c
void drmModeAtomicFree	(	drmModeAtomicReqPtr 	req	)
```

アトミック要求を解放します。

drmModeAtomicReqPtr オブジェクトと、関連するすべての drmModeAtomicReqItemPtr オブジェクトを解放します。

###### 事後条件

###### 手記

###### パラメーター

```text
req	:The atomic request object to be freed.
```

###### 収益

```text
NULL
```

##### ◆ drmModeFreeConnector()

```c
void drmModeFreeConnector	(	drmModeConnectorPtr 	ptr	)
```

コネクタを解放します。

drmModeGetConnector によって割り当てられた drmModeConnectorPtr 構造体を解放します。

###### 事後条件

###### 手記

###### パラメーター

```text
ptr	A pointer to the connector to be freed.
```

###### 収益

```text
null
```

##### ◆ drmModeFreeObjectProperties()

```c
void drmModeFreeObjectProperties	(	drmModeObjectPropertiesPtr 	ptr	)
```

オブジェクトのプロパティ構造を解放します。

drmModeObjectGetProperties によって割り当てられた drmModeObjectPropertiesPtr 構造体を解放します。

###### 事後条件

###### 手記

###### パラメーター

```text
ptr	A pointer to the object properties structure to be freed.
```

###### 収益

```text
null
```

##### ◆ drmModeFreePlaneResources()

```c
void drmModeFreePlane	(	drmModePlanePtr 	ptr	)
```

飛行機を解放します。

drmModeGetPlane によって割り当てられた drmModePlanePtr 構造体を解放します。

###### 事後条件

###### 手記

###### パラメーター

```text
ptr	A pointer to the plane to be freed.
```

###### 収益

```text
null
```

##### ◆ drmModeFreeProperty()

```c
void drmModeFreeProperty	(	drmModePropertyPtr 	ptr	)
```

プロパティ構造を解放します。

drmModeGetProperty によって割り当てられた drmModePropertyPtr 構造体を解放します。

###### 事後条件

###### 手記

###### パラメーター

```text
ptr	A pointer to a property structure returned by drmModeGetProperty.
```

###### 収益

```text
null
```

##### ◆ drmModeFreeResources()

```c
void drmModeFreeResources	(	drmModeResPtr 	ptr	)
```

リソース情報構造を解放します。

drmModeGetResources によって割り当てられた drmModeResPtr 構造体を解放します。

###### 事後条件

###### 手記

###### パラメーター

```text
ptr	A pointer to the resource to be freed.
```

###### 収益

```text
null
```

##### ◆ drmModeGetConnector()

```c
drmModeConnectorPtr drmModeGetConnector	(	int 	fd,
                                           uint32_t 	connector_id 
)
```

コネクタの情報を取得します。

connector_idが有効な場合、使用可能なモード、接続状態、コネクタの種類、接続されているエンコーダー (存在する場合) など、コネクタに関する情報を含む drmModeConnectorPtr 構造体を取得します。

###### 事後条件

呼び出しが成功した場合、アプリケーションは drmModeFreeConnector を呼び出してコネクタ情報構造を解放する必要があります。

###### 手記

コネクタ >mm幅とコネクタ>mm高さは現在、プレースホルダ値に設定されています。

###### パラメーター

```text
fd :	        The file descriptor of an open DRM device.
connector_id:	The connector ID of the connector to be retrieved.
```

###### 収益

```text
A drmModeConnectorPtr structure if successful, or NULL if the connector is not found or the API is out of memory.
```

##### ◆ drmModeGetPlaneResources()

```c
drmModePlaneResPtr drmModeGetPlaneResources	(	int 	fd	)
```

平面に関する情報を取得します。

DRM デバイスのプレーン リソースの一覧を取得します。DRM アプリケーションは通常、この関数を早期に呼び出して、使用可能な表示レイヤーを識別します。

デフォルトでは、返される情報には「オーバーレイ」タイプ(通常の)平面のみが含まれ、「プライマリ」プレーンと「カーソル」プレーンは含まれません。drmSetClientCap でDRM_CLIENT_CAP_UNIVERSAL_PLANESが有効になっている場合、返される情報には、CTRC を表す "プライマリ" プレーンと、カーソルを表す "カーソル" プレーンが含まれます。これにより、CRTC とカーソルを drmModeSetPlane などのプレーン関数で操作できます。

###### 事後条件

呼び出しが成功した場合、アプリケーションは drmModeFreePlaneResources を呼び出してプレーン情報構造を解放する必要があります。

###### 手記

DRMは現在、「カーソル」タイプのプレーンを実装していません。

###### パラメーター

```text
fd	The file descriptor of an open DRM device.
```

###### 収益

```text
A drmModeResPtr structure if successful, or NULL otherwise.
```

##### ◆ drmModeGetProperty()

```c
drmModePropertyPtr drmModeGetProperty	(	int 	fd,
                                            uint32_t 	propertyId 
)
```

DRM オブジェクトのプロパティを記述するプロパティ構造を取得します。

DRM オブジェクトには、平面、CRTC、またはコネクタを指定できます。

この関数は、drmModeObjectGetProperties() によって返される drmModeObjectPropertiesPtr 構造体に対して動作します。

変更可能なプロパティは、DRM オブジェクトの種類によって異なります。

1. 平面 (オブジェクト タイプ DRM_MODE_OBJECT_PLANE) の場合:

    ```text
    "SRC_X", "SRC_Y", "SRC_W", "SRC_H", "zpos", "alpha" "CRTC_X",
    "CRTC_Y", "CRTC_W", "CRTC_H", "CRTC_ID", "FB_ID"
    ```

2. CRTC (オブジェクト・タイプ DRM_MODE_OBJECT_CRTC) の場合、サポートされる値は次のとおりです。

    ```text
    "MODE_ID", "ACTIVE", "HDR_SUPPORTED", "HDR_METADATA_SMPTE_2086_ID"
    ```

3. コネクタ (オブジェクト タイプ DRM_MODE_OBJECT_CONNECTOR) の場合、サポートされる値は次のとおりです。

    ```text
    "CRTC_ID"
    ```

DRM プレーンの場合、列挙型フィールドには、プロパティを定義するキーワードのペア (名前 : value) のリストが保持されます。

```c
drmModePropertyPtr->enums[ ].name
drmModePropertyPtr->enums[ ].value
```

1. name フィールドでサポートされている値は上記で定義されています (つまり、"SRC_X"、"SRC_Y"、または "SRC_W")。このフィールドは変更可能です。
2. 値フィールドでサポートされている値は次のとおりです。

```text
"Primary", "Overlay", "Cursor" 
```

このフィールドは読み取り専用です。

平面タイプを識別するには、次のリストを反復処理して、value フィールドが目的の列挙型と一致する列挙型を見つけます。次に、対応する名前フィールドから値を取得します。

```c
drmModePropertyPtr->enums[ ] 
```

例えば：

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

###### 事後条件

呼び出しが成功した場合、アプリケーションは drmModeFreeProperty を呼び出してプロパティ情報構造を解放する必要があります。

###### 手記

平面の zpos 値は、次の平面に対するオフセット 10 で初期化されます。これは、ヘッドの柔軟な構成を可能にするためです。例えば：

1. "プライマリ" タイプの平面 zpos = 10
2. 最初の "オーバーレイ" 平面 zpos = 20
3. 次の "オーバーレイ"平面zpos = 30
4. 等。

zpos の許容範囲は です[0, 255]。zpos の数値が大きい平面は、数値的に小さい値を持つ平面を閉塞します。
平面のアルファ値を指定すると、平面全体の透明度と、バッファー オブジェクトに含まれるピクセルごとのアルファが適用されます。アルファに許可される範囲は です。[0, 255]0 は完全に透明で、255 はピクセルごとのアルファのみが効果を持つことを示します。アルファ以外のピクセル形式の場合、ピクセルごとのアルファは存在しないため、255 は完全に不透明であることを示します。

###### パラメーター

```text
fd:	The file descriptor of an open DRM device.
propertyId:	Property ID of the property object to be fetched.
```

###### 収益

```text
A drmModePropertyPtr if successful, or NULL otherwise.
```

##### ◆ drmModeGetResources()

```c
drmModeResPtr drmModeGetResources	(	int 	fd	)
```

DRM デバイスの CRTC、エンコーダー、およびコネクタに関する情報を取得します。

DRM デバイスの主要なリソースの一覧を取得します。DRM アプリケーションは通常、この関数を早期に呼び出して、使用可能なディスプレイやその他のリソースを識別します。ただし、この関数はプレーン リソースを報告しません。これらは drmModeGetPlaneResources で照会できます。

###### 事後条件

呼び出しが成功した場合、アプリケーションは drmModeFreeResources を呼び出してリソース情報構造を解放する必要があります。

###### 手記

drmModeResPtr 構造体のmin_width、min_height、max_width、およびmax_heightメンバーはプレースホルダー値に設定されます。

###### パラメーター

```text
fd	The file descriptor of an open DRM device.

```

###### 収益

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

DRM オブジェクトのすべてのプロパティを取得します。

指定された DRM オブジェクトのアトミックに変更可能なすべてのプロパティと、対応する drmModeCrtcPtr、drmModeConnectorPtr、および drmModePlanePtr 構造体に含まれていない読み取り専用プロパティを記述するオブジェクト プロパティ構造体を取得します。その後、drmModeGetProperty を使用して個々のプロパティを取得し、drmModeAtomicAddProperty を使用してその値を変更できます。

drmModeObjectPropertiesPtr 構造体には、プロパティ ID (小道具) の配列、対応するプロパティ値の配列 (prop_values)、および各配列内の要素の数 (count_props) が含まれています。プロパティの名前を取得するには、プロパティ ID に対して drmModeGetProperty を呼び出し、返された drmModePropertyPtr 構造体の名前フィールドを確認します。

プロパティをアトミックに変更するには、drmModeAtomicAlloc を呼び出して drmModeAtomicReqPtr 要求オブジェクトを作成し、drmModeAtomicAddProperty を呼び出して、drmModeAtomicReqPtr オブジェクト、変更するオブジェクトのオブジェクト ID、変更するプロパティのプロパティ ID、およびプロパティの新しい値を指定します。次に、drmModeAtomicCommit を使用して要求をコミットします。アトミック要求に複数のプロパティを設定し、1 回の操作でコミットできます。

###### 事後条件

呼び出しが成功した場合、アプリケーションは drmModeFreeObjectProperties を呼び出して、drmModeObjectPropertiesPtr 構造体を解放する必要があります。

###### 手記

すべてのオブジェクト・タイプがサポートされているわけではありません。

###### パラメーター

```text
fd:	The file descriptor of an open DRM device.
object_id:	The object ID of the DRM object whose properties are to be retrieved.
object_type:	A symbol representing an object type. The following object types are supported:
    DRM_MODE_OBJECT_CRTC
    DRM_MODE_OBJECT_CONNECTOR
    DRM_MODE_OBJECT_PLANE
```

###### 収益

```text
A drmModeObjectPropertiesPtr object if successful, or NULL otherwise.
```

##### ◆ drmModeRmFB()

```c
int drmModeRmFB	(	int 	fd,
                    uint32_t 	fb_id 
)
```

フレームバッファを破棄します。

drmModeAddFB または drmModeAddFB2 によって割り当てられたフレームバッファを破棄 (解放) します。

###### 事後条件

###### 手記

###### パラメーター

```text
fd	The file descriptor of an open DRM device.
fb_id	The ID of the framebuffer to destroy.
```

###### 収益

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

CRTC 構成を設定します。

DRM モードが指定されている場合 (drm_modeが NULL でない場合)、CRTC および指定されたコネクタの表示モードを設定します。新しいfb_id、x、および y プロパティは vblank に設定されます。

###### 事後条件

###### 手記

fb_id、x、および y パラメーターは、ハードウェア・ウィンドウ・フレーム・バッファーまたは対応するオフセットを変更しないことを示す特殊な入力値 -1 を受け入れます。(カーネルベースのDRMドライバは、fb_idに対してのみ-1を受け入れます。x または y に -1 を指定すると、エラー・コード -ERANGE が戻されます。
有効なモードを指定し、CRTC にフレームバッファが現在アタッチされていない場合でも、fb_id==-1 を指定できます。この関数は表示モードを設定しますが、CRTC フレームバッファは未定義のままにします。
CRTC に設定されたフレームバッファは、drmModeSetCrtc、drmModePageFlip、またはその他の手段のいずれによっても、平面の背後に表示されます。CRTC 表示層は、重なり順で最下位です。

###### パラメーター

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

###### 収益

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

平面のフレームバッファと位置を変更します。

###### 事後条件

###### 手記

crtc_...そしてsrc_...パラメーターは、ハードウェア・オフセット値が変更されないことを示す特殊な入力値 -1 を受け入れます。(カーネルベースの DRM ドライバーは、この値を指定するとエラーコード -ERANGE を返します。
平面上に設定されたフレームバッファは、CRTC の上に表示されます。プレーンの重なり順は、プレーンが drmModeGetPlaneResources によって報告される順序によって示されます。
すべての drmModeSetPlane 操作は vblank に同期され、ブロックされています。

###### パラメーター

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

###### 収益

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

DRM の機能 (機能) を有効または無効にします。

###### 事後条件

###### 手記

###### パラメーター

```text

fd:	         The file descriptor of an open DRM device.
capability：	Specifies the capability to be enabled or disabled. Supported values are:
                    DRM_CLIENT_CAP_ATOMIC (disabled by default)
                    DRM_CLIENT_CAP_UNIVERSAL_PLANES (disabled by default)
value:  	 0 to disable the capability, or 1 to enable it.
```

###### 収益

```text
0 if successful, or -EINVAL otherwise.
```

##### ◆ drmWaitVBlank()

```c
int drmWaitVBlank	(	int 	fd,
drmVBlankPtr 	vbl 
)
```

垂直ブランキング間隔 (vblank) を待機します。

指定された vblank を待機するか、指定された vblank が発生したときに登録済みの vblank ハンドラーを呼び出すように要求します。

###### 事後条件

###### 手記

現在、すべての drmVblankPtr フィールドをサポートしているわけではありません。

###### パラメーター

```text
fd:	    The file descriptor of an open DRM device.
vbl:	A description of the requested vblank. The vbl->type field must contain one of these values:
           DRM_VBLANK_ABSOLUTE: request.sequence is the vblank count since some point in the past, e.g. system boot.
           DRM_VBLANK_RELATIVE: request.sequence is the vblank count from the current value. e.g. 1 specifies the next vblank. The value may be bitwise ORed with any combination of these values:
           DRM_VBLANK_SECONDARY: Uses the secondary display's vblank.
           DRM_VBLANK_EVENT: Returns immediately and triggers the event callback instead of waiting for a specified vblank.
```

###### 収益

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

###### 事後条件

指定された CRTC のページ反転 (フレームバッファーの変更) を要求します。

指定された CRTC のページめくりをスケジュールします。デフォルトでは、CRTC は、次の垂直リフレッシュ後に指定されたフレームバッファを表示するように再プログラムされます。

###### 手記

###### パラメーター

```text
fd :	    The file descriptor of an open DRM device.
crtc_id :	CRTC ID of the CRTC whose framebuffer is to be changed.
fb_id :	    Framebuffer ID of the framebuffer to be displayed.
flags :	    Flags affecting the operation. Supported values are:
                  DRM_MODE_PAGE_FLIP_ASYNC: Flip immediately, not at vblank.
                  DRM_MODE_PAGE_FLIP_EVENT: Send page flip event.
user_data:	Data used by the page flip handler if vblank event was requested.
```

###### 収益

```text
0	if successful.
-EINVAL	if crtc_id or fb_id is invalid.
-errno	otherwise.
```
<!-- markdownlint-enable header-increment no-hard-tabs -->
## 3.3 k510 DRM の新しいフレーム関数の使用説明

構造体の定義

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

マクロ定義

```c
define DRM_KENDRYTE_DRAW_FRAME         0x00

#define DRM_IOCTL_KENDRYTE_DRAW_FRAME   DRM_IOWR(DRM_COMMAND_BASE + \
                DRM_KENDRYTE_DRAW_FRAME, struct vo_draw_frame)
```

ボックス関数

```c
static int draw_frame(struct vo_draw_frame *frame)
{
    return drmIoctl(drm_dev.fd, DRM_IOCTL_KENDRYTE_DRAW_FRAME, frame);
}
```

**免責事項を翻訳します**  
お客様の便宜のために、カナアンはAI翻訳プログラムを使用してテキストを複数の言語に翻訳し、エラーが含まれている可能性があります。 当社は、提供される翻訳の正確性、信頼性、または適時性を保証するものではありません。 カナアンは、翻訳された情報の正確性または信頼性への依存に起因するいかなる損失または損害についても責任を負いません。 異なる言語翻訳間でコンテンツの違いがある場合は、簡体字中国語版が優先されます。 

翻訳エラーや不正確な問題を報告する場合は、メールでお問い合わせください。