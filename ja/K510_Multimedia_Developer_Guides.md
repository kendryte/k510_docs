![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510マルチメディア開発ガイド</font>**

<font face="黑体"  size=3>ドキュメントのバージョン: V1.0.0</font>

<font face="黑体"  size=3>発売日:2022-03-09</font>

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
## ドキュメントの目的
このドキュメントは、K510 Multimedia アプリ インスタンスの説明ドキュメントです。
## ターゲット読者
このドキュメントの対象ユーザー:
- ソフトウェア開発者
- テクニカル サポート スタッフ

## レコードを改訂します

| バージョン番号    | 変更者 | 改訂日| 修正の説明  |  
|  ------  |-------| -------| ------ |
| v1.0.0の    |システム ソフトウェア グループ | 2022-03-09 | SDK V1.5 リリース |
|     |     |      |   |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>目録</font>**

[目次]

# 1 エンコーダ API

## 1.1 ヘッダーファイルの説明

k510_buildroot/パッケージ/encode_app/enc_interface.h

## 1.2 API 関数の説明

### 1.2.1 VideoEncoder_Create

【説明】

ビデオ エンコーダーを作成します

【文法】

```c
EncoderHandle* VIdeoEncoder_Create(EncSettings *pCfg)
```

【パラメータ】

pCfg: エンコード構成パラメータを入力します

|            引数の名前             | 引数の解釈                                                     |                           値の範囲を取得します                           | コーディング モジュールが適用されます |
| :---------------------------: | :----------------------------------------------------------- | :----------------------------------------------------------: | ------------ |
|            チャンネル            | チャネル番号で、最大 8 つのエンコード チャネルをサポートします                                   |                            [0，7]                            | jpeg、avc    |
|             幅             | エンコードされたイメージの幅                                                 | avc[128,2048]: 、8 の倍数  jpeg: 最大 8192、16 の倍数 <br/> | jpeg、avc    |
|            高さ             | エンコードされたイメージの高さ                                                 | avc[64,2048]: 、8 の倍数  JPEG: 最大 8192、2 の倍<br/>数 | jpeg、avc    |
|           フレームレート           | フレーム レートは、いくつかの値を固定するように構成できます                                    |                       (25,30,50,60,75)                       | jpeg、avc    |
|            rcモード             | コードレート制御モード 0:CONST_QP 1:CBR 2:VBR<br />jpeg はCONST_QPに固定されています  |                       RateCtrlMode を参照してください                       | jpeg,avc    |
|            ビットレート            | CBR モードのターゲット コード レートまたは VBR モードでの最小コード レート                    |                        [10,20000000]                         | 卒中          |
|          最大ビットレート           | VBR モードでの最大コード レート                                          |                        [10,20000000]                         | 卒中          |
|            スライス QP            | 初期 QP 値、-1 は auto を表します                                        | avc:-1,jpeg:[0,51]<br/>[1,100]                | jpeg,avc    |
|             ミンQP             | 最小 qp 値                                                     |                         [0,スライスqp]                          | 卒中          |
|             マックスQP             | 最大 qp 値                                                     |                         [スライスqp,54]                         | 卒中          |
|            プロフィール            | SPS の profile_idc 引数: 0: base 1:main 2:high 3:jpeg       |                            [0,3]                             | jpeg,avc    |
|             レベル             | PS の level_idc パラメーター                                       |                           [10,42]                            | 卒中          |
|          アスペクト比          | スケールを表示します                                                     |                     AVC_AspectRatioを参照してください                      | jpeg,avc    |
|            FreqIDR            | 2 つの idr フレームの間隔                                              |                           [1,1000]                           | 卒中          |
|            ゴプレン             | Group Of Picture、つまり 2 つの I フレーム間の間隔                      |                           [1,1000]                           | 卒中          |
|          bEnableGDR           | イントラリフレッシュを有効にするかどうか                                             |                         [真、偽]                         | 卒中          |
|            gdrMode            | gdr リフレッシュモード:0、垂直リフレッシュ1、水平リフレッシュ                        |                       GDRCtrlMode を参照してください                        | 卒中          |
|          bEnableLTR           | 長期参照フレームを有効にするかどうか                                           |                         [真、偽]                         | 卒中          |
|          roiCtrlMode          | roi制御モード:0:roi 1:相対qp 2:絶対qpを使用しません                 |                       ROICtrlMode を参照してください                        | 卒中          |
|       EncSliceSplitCfg        | slice 分割配置                                               |                                                              | 卒中          |
|         bスプリットイネーブル          | Slice 分割がイネーブルかどうか                                           |                         [真、偽]                         | 卒中          |
|         u32スプリットモード          | Slice 分割モード: 0: ビット数で分割します。 <br />1:マクロブロック行で分割します|                            [0,1]                             | 卒中          |
|         u32スライスサイズ          | u32SplitMode=0 は、slice あたりの byte 数 <br />u32SplitMode=1 を表し、slice ごとに占めるマクロ ブロックの行数<br />を表します| u32スプリットモード= [100,65535]<br />0,u32スプリットモード= 1、[1、(画像高+15)/16] | 卒中          |
|          エントロピーモード          | エントロピーコーディング、0:CABAC 1:CAVLC                                |                      EncEntropyMode を参照してください                      | 卒中          |
|          encDblkCfg           | チャンク フィルタ構成                                                 |                                                              | 卒中          |
| disable_deblocking_filter_idc | 既定値の 0 は、H.264 コンコルドを参照してください                          |                            [0，2]                            | 卒中          |
|  slice_alpha_c0_offset_div2   | 既定値の 0 は、H.264 コンコルドを参照してください                          |                           [-6，6]                            | 卒中          |
|    slice_beta_offset_div2     | 既定値の 0 は、H.264 コンコルドを参照してください                          |                          [-6,   6]                           | 卒中          |

```c
typedef struct
{
    int                       channel;  //encode channel number
    unsigned short            width;
    unsigned short            height;
    unsigned char             FrameRate;
    RateCtrlMode              rcMode;
    unsigned int              BitRate;
    unsigned int              MaxBitRate;
    int                       SliceQP;  //auto: -1, or from 0 to 51
    int                       MinQP;//from 0 to SliceQP
    int                       MaxQP;//from SliceQP to 51
    AVC_Profile               profile;
    unsigned int              level;  //1 .. 51, 51 is 5.1
    AVC_AspectRatio           AspectRatio;
    int                       FreqIDR; //default value  : -1,IDR:number of frames between two IDR pictures;GDR:refresh period
    unsigned int              gopLen;  
    bool                      bEnableGDR;//gdr
    GDRCtrlMode               gdrMode;
    bool                      bEnableLTR;//Long Term reference

    ROICtrlMode               roiCtrlMode;
    EncSliceSplitCfg          sliceSplitCfg;
    EncEntropyMode            entropyMode;//Profile is set to AVC_MAIN or AVC_HIGH is valid
    EncDblkCfg                encDblkCfg;
}EncSettings;
typedef enum
{
    CONST_QP,
    CBR,
    VBR
} RateCtrlMode;
typedef enum
{
    AVC_C_BASELINE,
    AVC_MAIN,
    AVC_HIGH,
    JPEG
} AVC_Profile;
typedef enum
{
    ASPECT_RATIO_AUTO,
    ASPECT_RATIO_4_3,
    ASPECT_RATIO_16_9,
    ASPECT_RATIO_NONE
} AVC_AspectRatio;
typedef struct
{
    unsigned int          s32X;
    unsigned int          s32Y;
    unsigned int          u32Width;
    unsigned int          u32Height;
} RECT_S;
typedef struct
{
    unsigned int          uIndex;//index[0-7]
    bool                  bEnable;
    int                   uQpValue;
    RECT_S                stRect;
} EncROICfg;
typedef enum
{
    ROI_QP_TABLE_NONE,
    ROI_QP_TABLE_RELATIVE,//[-32,31],6 LSBs effective
    ROI_QP_TABLE_ABSOLUTE,//[0,51],6 LSBs effective
} ROICtrlMode;
typedef enum
{
    GDR_VERTICAL = 0,
    GDR_HORIZONTAL,
    GDR_CTRLMAX,
} GDRCtrlMode;
typedef struct
{
    bool bSplitEnable;
    unsigned int u32SplitMode; // 0:splite by byte; 1:splite by slice count
    unsigned int u32SliceSize;
}EncSliceSplitCfg;

typedef enum
{
    ENTROPY_MODE_CABAC = 0,
    ENTROPY_MODE_CAVLC,
}EncEntropyMode;

typedef struct
{
    unsigned int  disable_deblocking_filter_idc;//[0,2]
    int  slice_alpha_c0_offset_div2;//[-6,6]
    int  slice_beta_offset_div2;//[-6,6]
}EncDblkCfg;
```

【戻り値】

```c
typedef void* EncoderHandle
```

### 1.2.2 VideoEncoder_SetRoiCfg

【説明】

roi 設定は、最大 8 つの四角形領域をサポートし、システム内部では 0 ~ 7 のインデックス番号で ROI 領域を管理し、uIndex はユーザーが ROI のインデックス番号を設定することを示します。 ROI 領域は互いにオーバーレイでき、オーバーレイが発生すると、ROI 領域間の優先順位はインデックス番号 0 ~ 7 で順番に増加します。

エンコーダーの作成後から破棄前まで使用できます。 roi領域は、エンコード中に動的に調整できます。

【文法】

```c
EncStatus VideoEncoder_SetRoiCfg(EncoderHandle *hEnc,const EncROICfg*pEncRoiCfg);
```

【パラメータ】

hEnc: 作成時に返されるハンドル

pEncRoiCfg:roi ゾーン構成情報

```c
typedef struct
{
    unsigned int          s32X;
    unsigned int          s32Y;
    unsigned int          u32Width;
    unsigned int          u32Height;
}RECT_S;

typedef struct 
{
    unsigned int          uIndex;//index[0-7]
    bool                  bEnable;
    int                   uQpValue;
    RECT_S                stRect;
}EncROICfg;
```

引数の説明

```text
uIndex     - 指定该roi区域索引号，范围0-7最多支持8个区域
bEnable    - 指定该区域是否使能，只有使能的区域才有效
uQpValue   - qp值，可以是相对qp或绝对qp，qp模式由EncSettings中roiCtrlMode属性决定。绝对qp范围                  [0,51]，相对qp范围[-31,31]
stRect     - roi矩形区域，s32X矩形左上角x值，s32Y矩形左上角y值，u32Width矩形宽度，u32Height矩形高度
```

【戻り値】

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.3 VideoEncoder_SetLongTerm

【説明】

エンコードの次のフレームを長期参照フレームとして設定します。 エンコーダーの作成後から破棄前まで使用できます。 EncSettingsにおけるbEnableLTR属性は,この機能が有効かどうかを決定する.

【文法】

```c
EncStatus VideoEncoder_SetLongTerm(EncoderHandle *hEnc);
```

【パラメータ】

hEnc: 作成時に返されるハンドル

【戻り値】

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.4 VideoEncoder_UseLongTerm

【説明】

エンコードされた次のフレームは、長期参照フレームを使用するように設定します。 エンコーダーの作成後から破棄前まで使用できます。 EncSettingsにおけるbEnableLTR属性は,この機能が有効かどうかを決定する.

【文法】

```c
EncStatus VideoEncoder_UseLongTerm(EncoderHandle *hEnc);
```

【パラメータ】

hEnc: 作成時に返されるハンドル

【戻り値】

```c
typedef enum
{
    Enc_SUCCESS = 0,
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.5 VideoEncoder_InsertUserData

【説明】

ユーザー データを挿入します。

エンコーダーの作成後から破棄前まで使用でき、エンコード中にユーザー データの内容をリアルタイムで変更できます。 ユーザー データは、IDR フレームの SEI データ領域に挿入されます。

【文法】

```c
EncStatus      VideoEncoder_InsertUserData(EncoderHandle *hEnc,char*pUserData,unsigned int nlen);
```

【パラメータ】

hEnc: 作成時に返されるハンドル

pUserData: ユーザー データ ポインター

nlen: ユーザー データの長さ (0, 1024)

【戻り値】

```c
typedef enum
{
    Enc_SUCCESS = 0,
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.6 VideoEncoder_Destory

【説明】

ビデオ エンコーダーを破棄します

【文法】

```c
EncStatus VideoEncoder_Destroy(EncoderHandle *hEnc)
```

【パラメータ】

hEnc: 作成時に返されるハンドル

【戻り値】

```c
typedef enum
{
    Enc_SUCCESS = 0, 
    Enc_ERR = 1,
}EncStatus;
```

### 1.2.7 VideoEncoder_EncodeOneFrame

【説明】

ビデオ フレームをエンコードします

【文法】

```c
EncStatus VideoEncoder_EncodeOneFrame(EncoderHandle *hEnc, EncInputFrame *input)
```

【パラメータ】

hEnc: 作成時に返されるハンドル

input: YUV ビデオ データを入力します

```c
typedef struct
{
    unsigned short width;
    unsigned short height;
    unsigned short stride;
    unsigned char *data;
}EncInputFrame;
```

【戻り値】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.2.8 VideoEncoder_GetStream

【説明】

ビデオ エンコード ストリームのバグを取得します。注: このバッフル領域はエンコーダーによって内部的に割り当てられます。

【文法】

```c
EncStatus VideoEncoder_GetStream(EncoderHandle *hEnc, EncOutputStream *output)
```

【パラメータ】

hEnc: 作成時に返されるハンドル

output:出力符号化されたストリームデータbuffer,bufSizeが0より大きい場合にのみ出力がある

```c
typedef struct
{
    unsigned char *bufAddr;
    unsigned int bufSize; 
}EncOutputStream;
```

【戻り値】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.2.9 VideoEncoder_GetStream_ByExtBuf

【説明】

ビデオ エンコード ストリームのバグを取得します。注: このバッフル領域は、コンシューマがこの関数を呼び出す前に割り当てる必要があります。

【文法】

```c
EncStatus VideoEncoder_GetStream(EncoderHandle *hEnc, EncOutputStream *output)
```

【パラメータ】

hEnc: 作成時に返されるハンドル

output:出力符号化されたストリームデータbuffer,bufSizeが0より大きい場合にのみ出力がある

```c
typedef struct
{
    unsigned char *bufAddr;
    unsigned int bufSize; 
}EncOutputStream;
```

【戻り値】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

### 1.3.0 VideoEncoder_ReleaseStream

【説明】

ビデオ エンコード ストリームのバッフルを解放します

【文法】

```c
EncStatus VideoEncoder_ReleaseStream(EncoderHandle *hEnc, EncOutputStream *output)
```

【パラメータ】

- hEnc: 作成時に返されるハンドル
- output:VideoEncoder_GetStream返されるbuffer

【戻り値】

```c
Enc_SUCCESS = 0,
Enc_ERR = 1
```

# 2 ハードウェア構成図とソフトウェア アーキテクチャ

# 2.1 ハードウェア構成図

K510のハードウェアブロック図は次のとおりです。
![hardware_block_diagram](../zh/images/multimedia_guides/hardware_block_diagram.png)

video sensorから受信したデータは,MIPI DPHY,CSI,VI,ISP処理によりyuvソースデータを取得し,DDRに格納する. h264 encoderモジュールはDDRからデータを読み出し,符号化演算を行い,演算結果をDDRに格納する.

# 2.2 ソフトウェアアーキテクチャ

マルチメディア開発プラットフォームのソフトウェア アーキテクチャは次のとおりです。

![multimedia_block_diagram.png](../zh/images/multimedia_guides/multimedia_block_diagram.png)

そのうち、

- `libvenc`: h264 encoder core を呼び出す encoder ライブラリ
- `libmediactl`: センスを制御するための isp ライブラリ
- `libaudio3a`: オーディオを3a演算するためのaudio3aライブラリ
- `alsa-lib`: オーディオ インターフェイスを制御するオーディオ ライブラリ

# 3 Demo アプリケーション

## 3.1 アプリケーションのエンコード

プログラムは、`/app/encode_app`ディレクトリの下に配置されます:

- `encode_app`:Encode applicationプログラム
- テスト用の yuv ファイルはサイズが大きく、SDK パッケージには入れませんでした

実行します`encode_app`

| 引数の名前 | 引数の解釈 | 既定値です | 値の範囲を取得します | コーディング モジュールが適用されます |
|:-|:-|:-|:-|:-|
| ヘルプ | ヘルプ情報| | ||
| 割る | チャネルの数 | ヌル | [1,4] | jpeg、avc |
| ティッカー | チャンネル番号(0から開始) | ヌル | [0,3] | jpeg、avc |
| 私 | yuv ファイルを入力し、**nv12** 形式のみをサポートします| ヌル | v4l2 <br> xxx.yuv | jpeg、avc |
| 開発 | v4l2 デバイス名 | ヌル |**センサー0:** /dev/video3 /dev/video4 <br> <br>sensor1:<br> **/dev/video7 /  dev/** video8 <br> <br> | 卒中 |
| 又は | 出力| ヌル | rtsp <br> xxx.264 <br> xxx.MJPEG xxx <br> .JPEG | jpeg、avc |
| で | 出力イメージの幅 | 1920 | avc[128,2048]: 、8 の倍数  jpeg: 最大 8192、16 の倍数 <br> | jpeg、avc |
| h | 出力イメージの高さ | 1080 | avc[64,2048]: 、8 の倍数  JPEG: 最大 8192、2 の倍<br>数 | jpeg、avc |
| fps | カメラはフレームレートをキャプチャし、現在は30pfsのみをサポートしています | 30 | 30 | 卒中 |
| r | エンコードされた出力フレーム レート | 30 | fps または fps で割り切れる数値 | 卒中 |
| インフレーム | yuv フレーム数を入力します | 0 | [0,50] | jpeg、avc |
| アウトフレーム | 出力yuvフレーム数は、パラメータ-inframesよりも大きい場合、繰り返し符号化されます | 0 | [0,32767] | jpeg、avc |
| ゴップ | Group Of Picture、つまり 2 つの I フレーム間の間隔 | 25 | [1,1000] | 卒中 |
| rcmode | コード レート制御モード 0:CONST_QP 1:CBR 2:VBR を表します | ティッカー | [0,2] | 卒中 |
| ビットレート | CBR モードのターゲット コード レートまたは VBR モードの最小コード レート(単位 Kb) | 4000 | [1,20000] | 卒中 |
| 最大ビットレート | VBR モードでの最大コード レート (KB 単位) | 4000 | [1,20000] | 卒中 |
| プロフィール | SPS の profile_idc 引数: 0: base 1:main 2:high 3:jpeg | AVC_HIGH | [0,3] | jpeg、avc |
| レベル | SPS の level_idc パラメーター | 42 | [10,42] | 卒中 |
| スライスqp | 初期 QP 値、-1 は auto を表します | 25 | avc:-1,jpeg:[0,51]<br/>[1,100] | jpeg、avc |
| ミンクプ | 最小 QP 値 | 0 | [0,スライスqp] | 卒中 |
| マックスクプ | 最大 QP 値 | 54 | [スライスqp,54] | 卒中 |
| 有効化LTR | イネーブルはフレームを長期間参照し、パラメータはリフレッシュサイクルを指定します。 0: 更新サイクルは有効になりません。 正の数: 参照フレームを周期的に設定し、次のフレームは長期参照フレームを使用するように設定されます | 0 | [0,65535] | 卒中 |
| 王 | 複数の roi 領域を指定する roi プロファイル | ヌル | xxx.conf | 卒中 |
| アエ | エナデュースAE | 0 | 0-エナジネーブルAE<br>1-エナーブルAE | |
| コンファレンス | vl42プロファイルは、コマンドライン入力パラメータに基づいてv4l2構成パラメータを変更するプロファイルを指定します | ヌル | xxx.conf | 卒中 |

### 3.1.1 yuvファイル、出力ファイルを入力します

```shell
./encode_app -split 1 -ch 0 -i your_file.yuv -o out.264 -w 1920 -h 1080 -inframes 10 -outframes 30
./encode_app -split 1 -ch 0 -i your_file.yuv -o out.mjpeg -w 1920 -h 1080 -inframes 10 -outframes 30
```

### 3.1.2 入力v4l2、出力rtspプッシュストリーム

#### 3.1.2.1 シングルチャンネル

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

ffplay プル コマンドの例:

```shell
 ffplay -rtsp_transport tcp rtsp://192.168.137.11:8554/testStream
```

- `rtsp://192.168.137.11:8554/testStream`rtsp ストリーム url アドレスの -rtsp_transport tcp は、tcp を使用してオーディオおよびビデオ データを転送することを意味し (既定では udp を使用)、プレーヤー キャッシュによる遅延の増加を避けるために -fflags nobuffer オプションを追加します。

#### 3.1.2.2 シングルカメラデュアルチャンネル

```shell
./encode_app -split 2 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -ch 1 -i v4l2 -dev /dev/video4 -o rtsp -w 1280 -h 720 -conf video_sample.conf
```

ffplay プル コマンドも同じになります。

#### 3.1.2.3 デュアルカメラ

```shell
./encode_app -split 2 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -ch 1 -i v4l2 -dev /dev/video7 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

ffplay プル コマンドも同じになります。

#### 3.1.2.4 roi テスト

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -sliceqp -1 -bitrate 2048 -roi roi_1920x1080.conf -conf video_sample.conf
```

roi ファイル形式

```json
{
  "roiCtrMode": 1,
  "roiRegion": [
    {
      "qpValue": -15,
      "qpRegion": {
        "left": 0,
        "top": 0,
        "width": 500,
        "heigth": 500
      }
    }
  ]
}
```

パラメータの説明:

```text
roiCtrMode - 1:相对qp  2:绝对qp
roiRegion  - roi区域，为多个区域数组，最多支持8个区域。
qpValue    - 指定该区域使用的qp值，相对qp范围:[-31,31]     绝对qp范围:[0,51]
qpRegion   - roi矩形区域
left       - 矩形区域的左上角X坐标
top        - 矩形区域的左上角Y坐标
width      - 矩形区域的宽度
heigth     - 矩形区域的高度
```

ffplay プル コマンドも同じになります。

### 3.1.3 フレームレート変換

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -r 60 -o rtsp -w 1920 -h 1080 -conf video_sample.conf
```

ffplay プル コマンドも同じになります。

### 3.1.4 複数の入力フレームレート

現在、VGA@75fpsと720p60がサポートされています

```shell
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 640 -h 480 -fps 75 -r 75 -conf video_sample_vga480p75.conf
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1280 -h 720 -fps 60 -r 60 -conf video_sample_720p60.conf
```

ffplay プル コマンドも同じになります。

### 3.1.5 rtsp プッシュオーディオおよびビデオストリーム

```c
./encode_app -split 1 -ch 0 -i v4l2 -dev /dev/video3 -o rtsp -w 1920 -h 1080 -alsa 1 -ac 2 -ar 44100 -af 2 -ad hw:0 -conf video_sample.conf
```

ffplay プル コマンドも同じになります。

### 3.1.6 注意事項

- 動作環境:コアボードsensor:IMX219_SENSOR

- rtsp ストリーム アドレス形式: rtsp://ip アドレス: ポート番号/testStream で、ip アドレスとポート番号は可変であり、残りは固定されています。

  例えば、rtsp://192.168.137.11:8554/testStream、ipアドレスは192.168.137.11、ポート番号は8554である.

  ipアドレス:ボードのIPアドレスを開発し、ボードにifconfigを入力して取得します。

  ポート番号: 8554 + <通道号>*2、チャネル番号は、通常、0 (-ch 0,-ch 1...) から始まります。

- rtsp ストリームの再生方法: vlc または ffplay を使用して対応する rtsp ストリームを再生し、データ ストリームを udp または tcp プロトコルで送信できます。

  1)rtp over udp播放:ffplay -rtsp_transport udp rtsp://192.168.137.11:8554/testStream

  2)rtp over tcp 播放: ffplay -rtsp_transport tcp rtsp://192.168.137.11:8554/testStream

  udp over tcp で再生し、udp ドロップによる画面の花画面を避けることをお勧めします。

## 3.2 ffmpeg

ffmpeg は/usr/local/bin ディレクトリの下に配置されます。

- `ffmpeg`: ffmpegアプリケーション。

実行します`ffmpeg`

(1) encoder libk510_h264引数
| 引数の名前 | 引数の解釈 | 既定値です | 値の範囲を取得します |
|:-|:-|:-|:-|
| g | ゴップサイズ | 25 | 1~1000 |
| b | ビットレート | 4000000 | 0~20000000 |
| r | フレームレートは、ispが現在30fpsしかサポートしていないので、デコーダは30に設定する必要があります | 30 | 30 |
| idr_freq | IDR 周波数 | -1 (IDR なし) | -1~256 |
| ティッカー | cqpで符号化する場合は,qp値を配置する | -1(オート) | -1~100 |
| 最大レート | bitrate の最大値 | 0 | 20000000 |
| プロフィール | サポートされているprofile | 2(高) | 0 - ベースライン <br> 1 - メイン <br> 2 - 高 |
| レベル | level をエンコードします | 42 | 10~42 |
| だろう | 画面の縦横比 | 0(オート) | 0 - 自動  1 - 4:3 <br> 2 - 16:9 <br> 3 - なし <br> |
| ティッカー | チャンネル番号 | 0 | 0-7 |
| フレームトエンコード | エンコードされたフレームの数 | -1 (すべてのフレーム) | -1~16383 |

(2) encoder libk510_jpeg引数
| 引数の名前 | 引数の解釈 | 既定値です | 値の範囲を取得します |
|:-|:-|:-|:-|
| ティッカー | cqpで符号化する場合は,qp値を配置する | 25 | -1~100 |
| r | フレームレート | 30 | 25~60 |
| ティッカー | エンコードチャンネル | 0 | 0~7 |
| 最大レート | 最大ビットレート。(0=無視) | 4000000 | 0~20000000 |
| だろう | 縦横比 | 0(オート) | 0 - 自動  1 - 4:3 <br> 2 - 16:9 <br> 3 - なし <br> |

(3) device libk510_video引数
| 引数の名前 | 引数の解釈 | 既定値です | 値の範囲を取得します |
|:-|:-|:-|:-|
| ティッカー | フレームサイズ | ヌル | **エンコーダ用 libk510_h264:**: 最大 2048x2048 幅 8 倍  8 分の倍数 <br> 幅: 128 分、高さ:  64 <br> <br>エンコーダ用 libk510_jpeg:<br> <br> 最大 8192x8192 <br>**** <br> 幅 16 <br> 倍  高さ 2 倍 <br> |
| 経験値 | 露出パラメータ | 0 | 0~128 |
| アグティッカー | アナログゲイン | 0 | 0~232 |

(4) audio3a パラメータ
| 引数の名前 | 引数の解釈 | 既定値です | 値の範囲を取得します |
|:-|:-|:-|:-|
| sample_rate | オーディオ サンプル レート | 16000 | 1~65535 |
| アグティッカー | オーディオゲインモード | 3(AgcModeFixedDigital) | 0 - AgcModeUnchanged  1 - AgcModeAdaptiveAnalog 2 - AgcModeAdaptiveDigital <br> 3 - AgcModeFixedDigital <br> <br> |
| nsの | ノイズlevel | 3(非常に高い) | 0 - 低 <br> 1 - 中 <br> 2  - 高 <br> 3 - 超高 |
| dsp_task | auido3a の実行位置 | 1(dsp) | 0 - CPU <br>1 - dsp |

設定可能なパラメーターは、help コマンドで表示できます

```shell
ffmpeg -h encoder=libk510_h264 #查看k510编码器的参数
ffmpeg -h demuxer=v4l2 #查看demuxer的配置参数
ffmpeg -h filter=audio3a #查看audio3a的配置参数
```

ffmpeg の論理ボックスは次のとおりです。

![ffmpeg_block_diagram](../zh/images/multimedia_guides/ffmpeg_block_diagram.png)

audio3aは、受信したオーディオを3a演算して出力するためのものであり、その論理ブロック図は次のとおりです。

![ffmpeg_canaan_audio3a](../zh/images/multimedia_guides/ffmpeg_canaan_audio3a.png)

### 3.2.1 プログラムの実行手順

#### 3.2.1.1 rtp プッシュストリーム

##### 3.2.1.1.1. rtp プッシュビデオストリーム

ffmpeg 実行コマンドの例:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.102.231.29:1234
```

このうち10.102.231.29は受信側アドレスであり、実際の変更に応じて。
プログラムの実行中に "q" を押して実行を停止します。

ffplay はコマンドを受け取ります。

```shell
ffplay.exe -protocol_whitelist "file,udp,rtp" -i test.sdp -fflags nobuffer -analyzeduration 1000000 -flags low_delay
```

ここで、test.sdp は次の例に従って構成されます。

```text
SDP:
v=0
o=- 0 0 IN IP4 127.0.0.1
s=No Name
c=IN IP4 10.102.231.29
t=0 0
a=tool:libavformat 58.76.100
m=video 1234 RTP/AVP 96
a=rtpmap:96 H264/90000
a=fmtp:96 packetization-mode=1
```

.sdp パラメーターの説明:

- c=: メディア リンク情報; IN: ネットワークの種類。 IP4: アドレスの種類。 IP アドレスが続きます (受信側が存在する IP アドレスであり、送信側の IP ではないことに注意してください)。
- m=はメディアレベルのセッションの始まりです。 1234: ポート番号; RTP/AVP: トランスポート プロトコル; 96:rtp ヘッダーの payload 形式
実際の状況に応じて、受信側の IP アドレスとポート番号を変更し、rtp のポート番号が偶数である必要があります。

##### 3.2.1.1.2. rtp はオーディオストリームをプッシュします

ffmpeg 実行コマンドの例:

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f rtp rtp://10.100.232.11:1234
```

このうち10.100.232.11は受信側アドレスであり、実際の変更に応じて行う。

- ac: オーディオチャンネルの数を設定します
- ar: オーディオサンプルレートを設定します

ffplay はビデオ ストリームを受信するのと同じコマンドを受信し、sdp ファイルは次の例を参照します。

```text
SDP:
v=0
o=- 0 0 IN IP4 127.0.0.1
s=No Name
c=IN IP4 10.100.232.11
t=0 0
a=tool:libavformat 58.76.100
m=audio 1234 RTP/AVP 97
b=AS:128
a=rtpmap:97 MPEG4-GENERIC/32000/2
a=fmtp:97 profile-level-id=1;mode=AAC-hbr;sizelength=13;indexlength=3;indexdeltalength=3; config=129056E500
```

##### 3.2.1.1.3 rtp プッシュオーディオおよびビデオストリーム

ffmpeg 実行コマンドの例:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234 -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

ffplay はオーディオ ストリームを受信するのと同じコマンドを受信し、sdp ファイルは次の例を参照します。

```text
SDP:
v=0
o=- 0 0 IN IP4 127.0.0.1
s=No Name
t=0 0
a=tool:libavformat 58.76.100
m=video 1234 RTP/AVP 96
c=IN IP4 10.100.232.11
a=rtpmap:96 H264/90000
a=fmtp:96 packetization-mode=1
m=audio 1236 RTP/AVP 97
c=IN IP4 10.100.232.11
b=AS:128
a=rtpmap:97 MPEG4-GENERIC/32000/2
a=fmtp:97 profile-level-id=1;mode=AAC-hbr;sizelength=13;indexlength=3;indexdeltalength=3; config=129056E500
```

#### 3.2.1.2 rtsp プッシュストリーム

rtsp プッシュ ストリームの前に、rtsp サーバーを展開し、データ ストリームをサーバーにプッシュする必要があります。

##### 3.2.1.2.1 rtsp はビデオ ストリームをプッシュします

ffmpeg 実行コマンドの例:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -acodec copy -f rtsp rtsp://10.100.232.11:5544/live/test110
```

- `idr_freq`IDR フレーム間隔の場合、GOP の整数倍である必要があります。 rtsp プッシュ ストリームは、ストリームにプルするために IDR フレームを生成する必要があります。
- `rtsp://10.100.232.11:5544/live/test110`rtsp サーバーのプッシュ プル ストリーム url アドレス

ffplay プル コマンドの例:

```shell
ffplay.exe -protocol_whitelist "file,udp,rtp,tcp" -i rtsp://10.100.232.11:5544/live/test110
```

##### 3.2.1.2.2 rtspはオーディオストリームをプッシュします

ffmpeg 実行コマンドの例:

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f rtsp rtsp://10.100.232.11:5544/live/test110
```

ffplay プル コマンドは、rtsp がビデオ ストリームをプルするコマンドと同じです。

##### 3.2.1.2.3 rtspのつぶやきビデオストリーム

ffmpeg 実行コマンドの例:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -f alsa -ac 2 -ar 32000 -i hw:0 -idr_freq 25 -vcodec libk510_h264 -acodec aac -f rtsp rtsp://10.100.232.11:5544/live/test110
```

ffplay プル コマンドは、rtsp がビデオ ストリームをプルするコマンドと同じです。

#### 3.2.1.3 rtmp プッシュストリーム

rtmp プッシュ フローの前に、rtmp サーバーを展開し、データ ストリームをサーバーにプッシュする必要があります。 rtmp プロトコルをサポートするサーバーには、fms、nginx、srs などが含まれます。

##### 3.2.1.3.1 rtmpはビデオストリームをプッシュします

ffmpeg 実行コマンドの例:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`rtmp サーバーにストリームをプッシュする url アドレス  

ffplay プル コマンドの例:

```shell
ffplay -fflags nobuffer rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`rtmp サーバーからストリームをプルする url アドレス (プッシュ ストリームとプル ストリームのアドレスと同じ) の場合、-fflags nobuffer オプションは、プレーヤー キャッシュによる遅延の増加を回避します。

##### 3.2.1.3.2 rtmpはオーディオストリームをプッシュします

ffmpeg 実行コマンドの例:

```shell
ffmpeg -f alsa -ac 2 -ar 32000 -i hw:0 -acodec aac -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`rtmp サーバーにストリームをプッシュする url アドレス

ffplay プル コマンドは、rtmp がビデオ ストリームをプルするコマンドと同じです。

##### 3.2.1.3.3 rtmpのつぶやきビデオストリーム

ffmpeg 実行コマンドの例:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -f alsa -ac 2 -ar 32000 -i hw:0 -idr_freq 25 -vcodec libk510_h264 -acodec aac -f flv rtmp://10.100.232.11/live/1
```

- `rtmp://10.100.232.11/live/1`rtmp サーバーにストリームをプッシュする url アドレス

ffplay プル コマンドは、rtmp がビデオ ストリームをプルするコマンドと同じです。

#### 3.2.1.4 オーディオ3a

##### 3.2.1.4.1 audio を単独で実行します

(1) cpu 上で audio3a を実行します
ffmpeg 実行コマンドの例:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000:dsp_task=0 -f rtp rtp://10.100.232.11:1234
```

(2) dsp で audio3a を実行します
2 つの telnet ウィンドウを実行し、2 つのウィンドウで dsp task scheduler と ffmpeg をそれぞれ実行します (dsp task scheduler を最初に実行します)。
dsp task scheduler 実行コマンド インスタンス:

```shell
cd /app/dsp_app_new/
./dsp_app /app/dsp_scheduler/scheduler.bin
```

ffmpeg はコマンド インスタンスを実行します。

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000 -f rtp rtp://10.100.232.11:1234
```

##### 3.2.1.4.2audio3a と video を同時に実行します

(1) cpu 上で audio3a を実行します
2 つの telnet ウィンドウを実行し、audio3a と video を 2 つのウィンドウでそれぞれ実行します。
video コマンドの例:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234
```

audio3a コマンドの例:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000:dsp_task=0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

cpu 上で audio3a と video の両方を実行すると overflow が表示され、dsp で audio3a を実行することをお勧めします
(2) dsp で audio3a を実行します
3 つの telnet ウィンドウを実行し、audio3a 呼び出し、video、および dsp scheduler を 3 つのウィンドウでそれぞれ実行します (最初に dsp task scheduler を実行します)。
dsp task scheduler 実行コマンドは、audio3a を単独で実行するのと同じです。

audio3a コマンドの例:

```shell
ffmpeg -f alsa -ac 2 -ar 16000 -i hw:0 -af audio3a=sample_rate=16000 -f rtp rtp://10.100.232.11:1236
```

video コマンドの例:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234
```

- 10.100.232.11 は rtp 受信側の ip アドレスです。
- 受信側のffplayのSDPファイルの内容は,上記のffmpegコマンドを実行した後,印刷されたlogから得ることができる.

#### 3.2.1.5 v4l2

設定可能なパラメーターは、help コマンドで表示できます

```shell
ffmpeg -h demuxer=v4l2 #查看v4l2的配置参数
```

| 引数の名前 | 引数の解釈 | 既定値です | 値の範囲を取得します |
| :-- | :-- | :-- | :-- |
| s | 画像解像度 (1920x1080 など) | ヌル | |
| r | フレームレートは、現在30fpsのみをサポートしています | 30 | 30 |
| ISP | K510 ispハードウェアを開きます | 0 | 0-1 |
| buf_type | v4l2 buffer`类型` <br>1: V4L2_MEMORY_MMAP : -vcodec copy<br>2: V4L2_MEMORY_USERPTR: -vcodec libk510_h264 に適しています | 1 | 1~2 |
| コンファレンス | v4l2 設定ファイル | ヌル | |

ffmpeg 実行コマンドの例: 10.100.232.11 は受信側アドレスであり、実際の変更に基づきいます。

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_h264 -an -f rtp rtp://10.100.232.11:1234 -f alsa -ac 2 -ar 16000 -i hw:0 -acodec aac -vn -f rtp rtp://10.100.232.11:1236
```

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -i /dev/video3 -vcodec copy -y out.yuv
```

説明:

1. ランタイムは、実行ディレクトリ内のファイル`video_sampe.conf`を`imx219_0.conf``imx219_1.conf`検索し、構成する必要があります`/encode_app/`。
2. カメラがリアルタイムで入ってくるビデオはyuvファイルとして書かれており、yuvファイルが大きいため、ローカルddrまたはnfsの書き込み速度が追いついていないため、フレームが失う可能性があります。

#### 3.2.1.6 JPEG エンコード

ファイル出力:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_jpeg -y test.mjpeg
```

説明: ランタイムは、実行ディレクトリ内のファイルを検索`video_sampe.conf`し`imx219_0.conf`、`imx219_1.conf`構成する必要があります`/encode_app/`。

出力されたファイルtest.mjpegは、PC側でffplayで再生することができます

```shell
ffplay -i test.mjpeg
```

プッシュストリーム:

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -vcodec libk510_jpeg -an -f rtp rtp://10.100.232.11:1234
```

利用可能なffplayプルストリーム

#### 3.2.1.7 マルチプレクション

最大8ウェイの同時符号化が可能で、各パスのフレームサイズにフレームレートを乗じる加算し、1080p60のデータ量、-vcodecオプションh264またはJPEGを超えないようにすることができます。

```shell
ffmpeg -f v4l2 -s 1920x1080 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -filter_complex 'split=2[out1][out2]' -map '[out1]' -vcodec libk510_h264 -ch 0 -an -f rtp rtp://10.20.1.101:1234 -map '[out2]' -vcodec libk510_h264 -ch 1 -an -f rtp rtp://10.20.1.101:2236
```

```shell
ffmpeg -f v4l2 -s 480x360 -conf "video_sample.conf" -isp 1 -buf_type 2 -r 30 -i /dev/video3 -filter_complex 'split=8[out1][out2][out3][out4][out5][out6][out7][out8]' -map '[out1]' -vcodec libk510_h264 -b:v 300000 -ch 0 -an -f rtp rtp://10.20.1.101:1234 -map '[out2]' -vcodec libk510_h264 -b:v 300000 -ch 1 -an -f rtp rtp://10.20.1.101:2322 -map '[out3]' -vcodec libk510_h264 -b:v 300000 -ch 2 -an -f rtp rtp://10.20.1.101:3086 -map '[out4]' -vcodec libk510_h264 -b:v 300000 -ch 3 -an -f rtp rtp://10.20.1.101:4234 -map '[out5]' -vcodec libk510_h264 -b:v 300000 -ch 4 -an -f rtp rtp://10.20.1.101:5216 -map '[out6]' -vcodec libk510_h264 -b:v 300000 -ch 5 -an -f rtp rtp://10.20.1.101:6788 -map '[out7]' -vcodec libk510_h264 -b:v 300000 -ch 6 -an -f rtp rtp://10.20.1.101:7230 -map '[out8]' -vcodec libk510_h264 -b:v 300000 -ch 7 -an -f rtp rtp://10.20.1.101:8976
```

ffplay でストリームをプルする場合は、ビデオを 1 つだけプルするか、SDP ファイルのポート番号を変更して別のビデオを切り替えるか、複数の ffplay プル ストリームを開始します。

### 3.2.2 プログラム移植手順

`ffmpeg``ffmpeg`オープンソースコード4.4のバージョンに移植し、`xxx.patch`パッチパッケージに追加しました

- `ff_libk510_h264_encoder`: h264 ハードウェア エンコーディングを制御します`libvenc.so`
- `ff_libk510_jpeg_encoder`:制御JPEGハードウェアコーディング、参照`libvenc.so`
- v4l2:v4l2.cでは,k510ハードウェア関連コードを加え,v4l2 buffer型V4L2_MEMORY_USERPTRを実装し,参照`libmediactl.so`した.

#### 3.2.2.1 patch ビルドコマンド

（1）

```shell
quilt new -p ab xxx.patch #在patches目录下生成xxx.patch文件
quilt add <filename> #添加修改前的文件
### 修改代码 ###
quilt refresh #修改内容被添加到xxx.patch
```

（2）
xxx.patch を package/ffmpeg_canaan ディレクトリにコピーし、現在のパスに従って patch ファイルのファイル パスを変更します。

```shell
mv ../../patches/xxx.patch ../../package/ffmpeg_canaan
rm ../../patches/series
sed -i "s/\/dl\/ffmpeg_canaan\/ffmpeg-4.4//g" ../../package/ffmpeg_canaan/xxx.patch
```

#### 3.2.2.2 ffmpeg 設定

ファイルでは`package/ffmpeg_canaan/ffmpeg.mk`、configure オプションを使用して、CPU コアを変更し、ツール チェーンをコンパイルして`ff_k510_video_demuxer`、 と を`ff_libk510_jpeg_encoder`コンパイルできます`ff_libk510_h264_encoder`。

```shell
./configure \
    --cross-prefix=riscv64-linux- \
    --enable-cross-compile \
    --target-os=linux \
    --cc=riscv64-linux-gcc \
    --arch=riscv64 \
    --extra-ldflags="-L./" \
    --extra-ldflags="-ldl" \
    --extra-ldflags="-Wl,-rpath ." \
    --enable-static \
    --enable-libk510_video \
    --enable-libk510_h264 \
    --enable-libk510_jpeg \
    --enable-alsa \
    --disable-autodetect \
    --disable-ffplay \
    --disable-ffprobe \
    --disable-doc \
    --enalbe-audio3a \
    --enable-indev=v4l2 \
```

**免責事項を翻訳します**  
お客様の便宜のために、カナアンはAI翻訳プログラムを使用してテキストを複数の言語に翻訳し、エラーが含まれている可能性があります。 当社は、提供される翻訳の正確性、信頼性、または適時性を保証するものではありません。 カナアンは、翻訳された情報の正確性または信頼性への依存に起因するいかなる損失または損害についても責任を負いません。 異なる言語翻訳間でコンテンツの違いがある場合は、簡体字中国語版が優先されます。

翻訳エラーや不正確な問題を報告する場合は、メールでお問い合わせください。
