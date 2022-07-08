![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 AIアプリケーションガイド</font>**

<font face="黑体"  size=3>ドキュメントのバージョン: V1.0.0</font>

<font face="黑体"  size=3>発売日:2022-03-07</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**免責事項**</font>
お客様が購入した製品、サービス、または機能は、北京Jiayuan Jetts情報技術有限公司(以下「当社」、以下同じ)の商業契約および条件の対象となり、本書に記載されている製品、サービス、または機能の全部または一部がお客様の購入または使用の範囲外となる場合があります。 契約に別段の定めがない限り、当社は、本書の記述、情報、内容の正確性、信頼性、完全性、マーケティング、特定目的、非攻撃性について、明示または黙示を問わず、いかなる表明または保証も行いません。 特に断りのない限り、このドキュメントは使用ガイダンスの推論としてのみ機能します。
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
このドキュメントは、K510 AI アプリケーションのコンパニオン ドキュメントであり、エンジニアが k510 AI アプリケーションの作成と適用を理解するのに役立ちます。 

**<font face="黑体"  size=5>リーダー オブジェクト</font>**

このドキュメント (このガイド) は、主に次の担当者に適用されます。

- ソフトウェア開発者
- テクニカル サポート スタッフ

**<font face="黑体"  size=5>レコードを改訂します</font>**
 <font face="宋体"  size=2>リビジョン レコードには、ドキュメントが更新されるたびに説明が蓄積されます。 ドキュメントの最新バージョンには、以前のすべてのバージョンの更新が含まれています。 </font>

| バージョン番号   | 変更者     | 改訂日 | 修正の説明 |
| :-----  |-------    |  ------ | ------  |
| V1.0.0  | AI製品部  | 2022-03-07 |      |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>目録</font>**

[目次]

<div style="page-break-after:always"></div>

# 1 はじめに

このドキュメントでは、K510 AI アプリケーションの作成と適用について説明します。 K510 AIチップに基づくAIアプリケーション開発には、次のような段階があります。

モデルの準備: トレーニング済みのモデルを PC 側で検証し (静的画像推論を使用して)、モデルの正確性を確保します

モデル生成:訓練されたモデルをnncase compilerでコンパイルし,kmodelを生成する

モデル検証: 生成された kmodel は、nncase simulator を使用して精度検証を行います

AIアプリケーションの作成:ビデオ/画像の読み取り、入力の前処理、モデル推論、モデル後処理を完了します

AI アプリケーションのコンパイル: クロスコンパイル ツール チェーンを使用して、K510 AI アプリケーションのコンパイルを完了します

展開と調整: コンパイルされた AI アプリケーションを K510 ハードウェア製品に接続し、実際のシナリオで機能の調整を行います

K510 AIチップ上でのAIアプリケーション開発の全体的なアーキテクチャを次の図に示します。

![](../zh/images/ai_demo/image-ai-demo.png)

このドキュメントでは、320x320 解像度の YOLOV5s の onnx モデルを例にとり、K510 AI アプリケーションのプロセス全体の作成と適用について説明します。

# 2 モデルの準備

推論のためのYOLOV5sのonnxモデルは/docs/utils/AI_Application/aidemo_sdk/models/onnxサブディレクトリにあります(ファイルがない場合は [models をダウンロードしてください](https://github.com/kendryte/k510_docs/releases/download/v1.5/models.tar.gz))  解凍)、静的画像は/docs/utils/AI_Application/aidemo_sdk/examples/python_inference_on_PC/dataサブディレクトリにあり、スクリプトは/docs/utils/AI_Application/aidemo_sdk/examples/python_inference_on_PCサブディレクトリにあります。 

スクリプト コマンドプロンプトに従って、yolov5_image.pyスクリプトを実行し、静止画の推論結果を取得します。 出力画像の検出ボックスが正しいことを確認することで、モデルの正確性を検出します。

```shell
usage: yolov5_image.py [-h] [--image_path IMAGE_PATH]
                       [--image_out_path IMAGE_OUT_PATH]
                       [--onnx_path ONNX_PATH]
                       [--confidence_threshold CONFIDENCE_THRESHOLD]
                       [--nms_threshold NMS_THRESHOLD]

object detect

optional arguments:
  -h, --help            show this help message and exit
  --image_path IMAGE_PATH
                        input image path
  --image_out_path IMAGE_OUT_PATH
                        output image path
  --onnx_path ONNX_PATH
                        onnx model path
  --confidence_threshold CONFIDENCE_THRESHOLD
                        confidence_threshold
  --nms_threshold NMS_THRESHOLD
                        nms_threshold
```

# 3 モデル生成

モデル生成はnncase compilerに依存しており,nncase compilerの具体的な使用規則については[K510_nncase_Developer_Guides.mdを参照](./K510_nncase_Developer_Guides.md)することができる. YOLOV5s を生成する kmodel のスクリプトは、/docs/utils/AI_Application/aidemo_sdk/scripts サブディレクトリにあります。 

スクリプト コマンドのプロンプトに従って、gen_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.pyを実行して、適切な kmodel を生成します。

```shell
usage: gen_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py [-h] [--target TARGET] [--dump_dir DUMP_DIR] [--onnx ONNX] [--kmodel KMODEL]

optional arguments:
  -h, --help           show this help message and exit
  --target TARGET      target to run
  --dump_dir DUMP_DIR  temp folder to dump
  --onnx ONNX          onnx model path
  --kmodel KMODEL      kendryte model path
```

CPU での前処理を最小限に抑えるために、スクリプトのコンパイル オプションは次のように構成されることに注意してください。

```python
compile_options.input_type = 'uint8'
compile_options.preprocess = True
compile_options.input_layout = 'NCHW'
compile_options.output_layout = 'NHWC'
compile_options.input_shape = [1, 3, 320, 320]
compile_options.mean = [0, 0, 0]
compile_options.std = [255, 255, 255]
compile_options.input_range = [0, 255]
```

# 4 モデル検証

モデル検証はnncase simulatorに依存しており,nncase simulatorの具体的な使用規則については[K510_nncase_Developer_Guides.mdを参照することができる](./K510_nncase_Developer_Guides.md). YOLOV5s の kmodel スクリプトが/docs/utils/AI_Application/aidemo_sdk/scripts サブディレクトリにあることを確認します。 

スクリプト コマンドプロンプトに従って、simu_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.pyを実行して、対応する kmodel が正しく生成されていることを確認します。

```shell
usage: sim_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py [-h] [--onnx ONNX] [--kmodel KMODEL]

optional arguments:
  -h, --help       show this help message and exit
  --onnx ONNX      original model file
  --kmodel KMODEL  kmodel file
```

cosine similarity が 1 または 1 に近い場合、生成された kmodel の正確性が保証されます。

```text
output 0 cosine similarity : 0.9999450445175171
output 1 cosine similarity : 0.9999403953552246
output 2 cosine similarity : 0.9999019503593445
```

# 5 AI アプリケーションを作成します

モデル検証はnncase runtimeに依存しており,nncase runtimeの具体的な使用規則については[K510_nncase_Developer_Guides.mdを参照できる](./K510_nncase_Developer_Guides.md). AI アプリケーション リファレンス `k510_buildroot/package/ai/code/object_detect`。 まず、ターゲットインストルメンテーションインスタンスを作成し、kmodel入出力用の領域を割り当てる必要があります。 

```c++
objectDetect od(obj_thresh, nms_thresh, net_len, {valid_width, valid_height});
od.load_model(kmodel_path);  // load kmodel
od.prepare_memory();  // memory allocation
```

zero memory copyを実装するために,ISP出力アドレスをkmodel入力アドレスに関連付ける

```c++
// define cv::Mat for ai input
// padding offset is (valid_width - valid_height) / 2 * valid_width
cv::Mat rgb24_img_for_ai(net_len, net_len, CV_8UC3, od.virtual_addr_input[0] + (valid_width - valid_height) / 2 * valid_width);
```

ISP 出力の幅と高さを設定します

```c++
 /****fixed operation for video operation****/
 mtx.lock();
 cv::VideoCapture capture;
 capture.open(5);
 // video setting
 capture.set(cv::CAP_PROP_CONVERT_RGB, 0);
 capture.set(cv::CAP_PROP_FRAME_WIDTH, net_len);
 capture.set(cv::CAP_PROP_FRAME_HEIGHT, net_len);
 // RRRRRR....GGGGGGG....BBBBBB, CHW
 capture.set(cv::CAP_PROP_FOURCC, V4L2_PIX_FMT_RGB24);
 mtx.unlock();
```

ISP の実際の出力高さ、video_height_r の異なるチャネル間の高さオフセットvideo_height、適切な video プロファイルを構成します

```json
"/dev/video5":{
    "video5_used":1,
    "video5_width":320,
    "video5_height":320,
    "video5_height_r":240,
    "video5_out_format":0
}
```

入出力アドレスを kmodel のinput_tensorとoutput_tensorに関連付けます

```c++
od.set_input(0);
od.set_output();
```

kmodel を実行し、出力結果を取得し、後処理を行います

```c++
{
    ScopedTiming st("od run", enable_profile);
    od.run();
}

{
    ScopedTiming st("od get output", enable_profile);
    od.get_output();
}
std::vector<BoxInfo> result;
{
    ScopedTiming st("post process", enable_profile);
    od.post_process(result);
}
```

最終的に、検出ボックスをOSDに描画し、出力を表示します

```c++
{
    ScopedTiming st("draw osd", enable_profile);
    obj_cnt = 0;
        for (auto r : result)
        {
        if (obj_cnt < 32)
        {
            struct vo_draw_frame frame;
            frame.crtc_id = drm_dev.crtc_id;
            frame.draw_en = 1;
            frame.frame_num = obj_cnt;
            frame.line_y_start = r.x2 * DRM_INPUT_WIDTH / valid_width;
            frame.line_x_start = r.x1 * DRM_INPUT_WIDTH / valid_width;
            frame.line_x_end = r.y1 * DRM_INPUT_HEIGHT / valid_height + DRM_OFFSET_HEIGHT;
            frame.line_y_end = r.y2 * DRM_INPUT_HEIGHT / valid_height + DRM_OFFSET_HEIGHT;
            draw_frame(&frame);

            cv::Point origin;
            origin.x = (int)(r.x1 * DRM_INPUT_WIDTH / valid_width);
            origin.y = (int)(r.y1 * DRM_INPUT_HEIGHT / valid_height + 10);
            std::string text = od.labels[r.label] + ":" + std::to_string(round(r.score * 100) / 100.0).substr(0,4);
            cv::putText(img_argb, text, origin, cv::FONT_HERSHEY_COMPLEX, 1.5, cv::Scalar(0, 0, 255, 255), 1, 8, 0);
        }
        obj_cnt += 1;
    }
}
```

# 6 AI アプリケーションをコンパイルします

クロスコンパイル ツール チェーンを使用すると、AI アプリケーションのコンパイルに関する特定の使用規則が[参照K510_SDK_Build_and_Burn_Guide](./K510_SDK_Build_and_Burn_Guide.md)。 

**免責事項を翻訳します**  
お客様の便宜のために、カナアンはAI翻訳プログラムを使用してテキストを複数の言語に翻訳し、エラーが含まれている可能性があります。 当社は、提供される翻訳の正確性、信頼性、または適時性を保証するものではありません。 カナアンは、翻訳された情報の正確性または信頼性への依存に起因するいかなる損失または損害についても責任を負いません。 異なる言語翻訳間でコンテンツの違いがある場合は、簡体字中国語版が優先されます。 

翻訳エラーや不正確な問題を報告する場合は、メールでお問い合わせください。