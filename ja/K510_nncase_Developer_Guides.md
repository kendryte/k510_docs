![カナンカバー.png](http://s2.loli.net/2022/03/30/7UG1IxrOXTo2QKw.png)

**<font face="黑体" size="6" style="float:right">K510 nncase 開発者ガイド</font>**

<font face="黑体"  size=3>ドキュメントのバージョン: V1.0.1</font>

<font face="黑体"  size=3>発売日:2022-05-10</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**免責事項**</font>
お客様が購入した製品、サービス、または機能は、北京Jiayuan Jetts情報技術有限公司(以下「当社」、以下同じ)の商業契約および条件の対象となり、本書に記載されている製品、サービス、または機能の全部または一部がお客様の購入または使用の範囲外となる場合があります。 契約に別段の定めがない限り、当社は、本書の記述、情報、内容の正確性、信頼性、完全性、マーケティング、特定目的、非攻撃性について、明示または黙示を問わず、いかなる表明または保証も行いません。 特に断りのない限り、このドキュメントは使用ガイダンスの参照としてのみ使用してください。
このドキュメントの内容は、製品バージョンのアップグレードまたはその他の理由により、予告なく随時更新または変更されることがあります。 

**<font face="黑体"  size=3>商標表示</font>**

「<img src="http://s2.loli.net/2022/03/30/xN21jbhnwSFyGRD.png" style="zoom:33%;" />」アイコン、カナン、その他の商標は、北京Jiayuan Jets情報技術有限公司の商標です。 本書で言及されるその他すべての商標または登録商標は、それぞれの所有者が所有しています。 

**<font face="黑体"  size=3>©著作権2022北京Jiayuan Jetth情報技術有限公司</font>**
このドキュメントは、K510プラットフォーム開発設計にのみ適用され、当社の書面による許可なく、いかなるユニットまたは個人も、このドキュメントの一部または全部をいかなる形式でも配布することはできません。 

**<font face="黑体"  size=3>北京Jiayuan Jetth情報技術有限公司</font>**
URL: canaan-creative.com
ビジネスお問い合わせ:salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# 序文
**<font face="黑体"  size=5>ドキュメントの目的</font>**
このドキュメントは、nncase/K510 compiler の使用説明書で、ユーザーが nncase をインストールする方法、compiler APIs コンパイル ニューラル ネットワーク モデルを呼び出す方法、および runtime APIs を呼び出して AI 推論プログラムを記述する方法を提供します

**<font face="黑体"  size=5>リーダー オブジェクト</font>**

このドキュメント (このガイド) は、主に次の担当者に適用されます。

- ソフトウェア開発者
- テクニカル サポート スタッフ

**<font face="黑体"  size=5>用語と頭字語</font>**

| 用語 | 説明/フルネーム                              |
| ---- | -------------------------------------- |
| ティッカー  | Post-training quantization, トレーニング後の定量 |
| ティッカー  | mean-square error, 二乗平均誤差            |
|      |                                        |

**<font face="黑体"  size=5>レコードを改訂します</font>**
 <font face="宋体"  size=2>リビジョン レコードには、ドキュメントが更新されるたびに説明が蓄積されます。 ドキュメントの最新バージョンには、以前のすべてのバージョンの更新が含まれています。 </font>

| バージョン番号   | 変更者     | 改訂日 | 修正の説明 |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.1 | チャン・ヤン | 2022-05-10 | nncase_v1.6.1. |
| V1.0.0 | チャン・ヤン/チャン・ジチャオ/ヤン・ハオキ | 2022-05-06 | nncase_v1.6.0 |
| V0.9.0 | チャン・ヤン | 2022-04-01 | nncase_v1.5.0 |
| V0.8.0の | チャン・ヤン/チャン・ジチャオ | 2022-03-03 | nncase_v1.4.0. |
| V0.7.0 | チャン・ヤン | 2022-01-28 | nncase_v1.3.0. |
| V0.6.0の | チャン・ヤン | 2021-12-31 | nncase_v1.2.0. |
| V0.5.0 | チャン・ヤン | 2021-12-03 | nncase_v1.1.0. |
| V0.4.0 | チャン・ヤン/ヤン・ハオキ/チェン・カイ | 2021-10-29 | nncase_v1.0.0 |
| V0.3.0 | チャン・ヤン/ヤン・ハオキ | 2021-09-28 | nncase_v1.0.0_rc1 |
| V0.2.0 | チャン・ヤン/ヤン・ハオキ | 2021-09-02 | nncase_v1.0.0_ベータ2 |
| V0.1.0 | チャン・ヤン/ヤン・ハオキ | 2021-08-31 | nncase_v1.0.0_ベータ1 |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>目録</font>**

[目次]

<div style="page-break-after:always"></div>

# 1 開発環境の概要

## 1.1 オペレーティング システム

- ウブンツ18.04 / 20.04

## 1.2 ソフトウェア環境

ソフトウェア環境の要件を次の表に示します。

| 序数 | ソフトウェア リソース        | 命令                        |
| ---- | --------------- | --------------------------- |
| 1    | ニシキヘビ          | パイソン 3.6/3.7/3.8/3.9/3.10 |
| 2    | ピップ3            | pip3 バージョン > = 20.3 です            |
| 3    | オンクス            | onnx バージョンは 1.9.0 です             |
| 4    | onnx 単純化 | onnx-simplifier バージョンは 0.3.6 です  |
| 5    | onnxoptimizer   | onnxoptimizer バージョンは 0.2.6 です    |

## 1.3 ハードウェア環境

ハードウェア環境の要件を次の表に示します。

| 序数 | ハードウェア リソース     | 命令 |
| ---- | ------------ | ---- |
| 1    | K510 CRB     |      |
| 2    | SDカードとリーダー |      |

# 2 nncase の概要

## 2.1nncaseとは何ですか?

nncase は AI アクセラレータ用に設計されたニューラル ネットワーク コンパイラで、現在サポートされている target には cpu/K210/K510 などがあります

nncase が提供する機能

- マルチ入力マルチ出力ネットワークをサポートし、マルチブランチファブリックをサポートします
- ヒープ メモリを必要としない静的メモリ割り当て
- 演算子のマージと最適化
- float および uint8/int8 量子化推論がサポートされています
- 浮動小数点モデルとクオンタイズキャリブレーションセットを使用して、トレーニング後のクオンタイズをサポートします
- ゼロコピーロードをサポートするフラットモデル

nncase がサポートするニューラル ネットワーク フレームワーク

- tflite
- オンクス
- カフェ

## 2.2 プロダクト利点

- **シンプルなエンド ツー エンドの展開**

  ユーザーとの対話回数を減らします。 ユーザーは、CPU、GPU モデル、および KPU への展開と同じツールとプロセスを使用して展開できます。 複雑なパラメータを設定したり、使用しきい値を下げたりすることなく、AI アルゴリズムの反復サイクルを加速できます。
- **既存のAIエコロジーをフルに活用**

  業界で広く使用されているフレームワークに添付されています。 一方では、可視性を高め、成熟した生態系の配当を楽しむことができます。 一方、中小規模の開発者の開発コストを削減し、業界で実績のあるモデルやアルゴリズムを直接展開できます。
- **ハードウェアのパフォーマンスを最大限に引き出します**

  NPUの利点は、CPUやGPUよりもパフォーマンスが高く、DL Compilerがハードウェアのパフォーマンスを十分に発揮できることです。 Compiler は、新しいモデル構造のパフォーマンスを適応的に最適化する必要があるため、手動最適化に加えて、新しい自動最適化手法を探索する必要があります。
- **拡張性と保守性**

  K210、K510、および将来のチップをサポートする AI モデル展開。 アーキテクチャ レベルでスケーラビリティを提供する必要があります。 新しいターゲットを追加するコストは小さく、できるだけ多くのモジュールを再利用できます。 新製品の研究開発をスピードアップし、DL Compilerの技術蓄積を実現します。

## 2.3 nncase アーキテクチャ

<img src="https://i.loli.net/2021/08/18/IQR12SOJdzxTUZH.png" alt="nncase_arch.png" style="zoom:67%;" />

nnncase ソフトウェア スタックには、現在 compiler と runtime の 2 つの部分が含まれています。

**Compiler:** PC でニューラル ネットワーク モデルをコンパイルし、最終的に kmodel ファイルを生成するために使用されます。 主にimporter, IR, Evaluator, Quantize, Transform最適化, Tiling, Partition, Schedule, Codegenなどのモジュールが含まれています. 

- Importer: 他のニューラル ネットワーク フレームワークのモデルを nncase にインポートします
- IR: 中間表現, importer によってインポートされた Neutral IR (デバイスに依存しない) と Neutral IR が lowering 変換によって生成された Target IR (デバイス関連) に分割されます。
- Evaluator: Evaluator は IR の解釈実行能力を提供し、Constant Folding/PTQ Calibration などのシナリオでよく使用されます
- Transform: IR 変換やグラフのトラバースの最適化などに使用されます
- Quantize: トレーニング後のクオンタイズ、クオンタイズするテンコールへのクオンタイズタグの追加、入力された補正セットに基づくエヴァルタtorの呼び出し、tensorのデータ範囲の収集、クオンタイズ/アンチクオンタイズノードの挿入、最後に不要なクオンタイズ/アンチクオンタイズノードの排除の最適化など
- Tiling: NPU の低メモリ容量に制限され、大きなブロック計算を分割する必要があります。 また、計算に大量のデータ多重がある場合に Tiling パラメータを選択すると、遅延と帯域幅に影響します
- Partition: 図を MomoduleType で分割し、分割された各サブプロットは RuntimeModule に対応し、異なるタイプの RuntimeModule は異なる Device (cpu/K510) に対応します。
- Schedule: 最適化されたグラフのデータ依存関係に基づいて計算順序を生成し、バグを割り当てます
- Codegen: ModuleType に対応するcodegen をサブプロットごとに個別に呼び出して、RuntimeModule を生成します

**Runtime**: ユーザーアプリに統合され、kmodel/設定入力データ/KPU実行/出力データの取得などの機能を提供します

# 3 nncase をインストールします

nncase ツール チェーン compiler セクションには、nncase と K510 compiler が含まれています。

- nncase wheel パッケージは[ nncase github で](https://github.com/kendryte/nncase/releases/tag/v1.6.0)リリースされ、Python 3.6/3.7/3.8/3.9/3.10 をサポートしており、オペレーティング システムと Python に応じて適切なバージョンを選択してダウンロードできます
- K510 compiler wheel パッケージは、nncase sdk のx86_64ディレクトリの下にあり、Python バージョンに依存せず、直接インストールできます

ユーザーは Ubuntu 環境を持っていない場合は、[nncase docker](https://github.com/kendryte/nncase/blob/master/docs/build.md#docker)(Ubuntu 20.04 + Python 3.8) を使用できます

```shell
cd /path/to/nncase_sdk
docker pull registry.cn-hangzhou.aliyuncs.com/kendryte/nncase:latest
docker run -it --rm -v `pwd`:/mnt -w /mnt registry.cn-hangzhou.aliyuncs.com/kendryte/nncase:latest /bin/bash -c "/bin/bash"
```

Ubuntu 20.04 + Python 3.8 インストールnncase を例にとります

```shell
wget -P x86_64 https://github.com/kendryte/nncase/releases/download/v1.6.0/nncase-1.6.0.20220505-cp38-cp38-manylinux_2_24_x86_64.whl
pip3 install x86_64/*.whl
```
<!-- markdownlint-disable no-emphasis-as-header -->
# 4 コンパイル/推論モデル

nncase は、**PC でディープ ラーニング モデルをコンパイル/推論するための** Python API s を提供します

## 4.1 サポートされている演算子

### 4.1.1 tflite演算子

| 演算子                | サポート対象 |
| ----------------------- | ------------ |
| 米国船級協会                     | ✅            |
| 足す                     | ✅            |
| ARG_MAX                 | ✅            |
| ARG_MIN                 | ✅            |
| AVERAGE_POOL_2D         | ✅            |
| BATCH_MATMUL            | ✅            |
| キャスト                    | ✅            |
| セイル                    | ✅            |
| 連結           | ✅            |
| CONV_2D                 | ✅            |
| 体                     | ✅            |
| 習慣                  | ✅            |
| DEPTHWISE_CONV_2D       | ✅            |
| 情報                     | ✅            |
| 等しい                   | ✅            |
| 経験値                     | ✅            |
| EXPAND_DIMS             | ✅            |
| 床                   | ✅            |
| FLOOR_DIV               | ✅            |
| FLOOR_MOD               | ✅            |
| FULLY_CONNECTED         | ✅            |
| 尚                 | ✅            |
| GREATER_EQUAL           | ✅            |
| L2_NORMALIZATION        | ✅            |
| LEAKY_RELU              | ✅            |
| レス                    | ✅            |
| LESS_EQUAL              | ✅            |
| 丸太                     | ✅            |
| ロジスティック                | ✅            |
| MAX_POOL_2D             | ✅            |
| 最大                 | ✅            |
| 意味する                    | ✅            |
| 最低限                 | ✅            |
| 私                     | ✅            |
| ネグ                     | ✅            |
| NOT_EQUAL               | ✅            |
| パッド                     | ✅            |
| パドブ2                   | ✅            |
| MIRROR_PAD              | ✅            |
| パック                    | ✅            |
| えい                     | ✅            |
| REDUCE_MAX              | ✅            |
| REDUCE_MIN              | ✅            |
| REDUCE_PROD             | ✅            |
| ルル                    | ✅            |
| プレル                   | ✅            |
| ルル6                   | ✅            |
| 形状                 | ✅            |
| RESIZE_BILINEAR         | ✅            |
| RESIZE_NEAREST_NEIGHBOR | ✅            |
| 丸い                   | ✅            |
| ティッカー                   | ✅            |
| 形                   | ✅            |
| 無し                     | ✅            |
| 切る                   | ✅            |
| ソフトマックス                 | ✅            |
| SPACE_TO_BATCH_ND       | ✅            |
| 絞る                 | ✅            |
| BATCH_TO_SPACE_ND       | ✅            |
| STRIDED_SLICE           | ✅            |
| ティッカー                    | ✅            |
| 正方形                  | ✅            |
| サブ                     | ✅            |
| 和                     | ✅            |
| 生臭い                    | ✅            |
| 瓦                    | ✅            |
| 転置               | ✅            |
| TRANSPOSE_CONV          | ✅            |
| 量子化する                | ✅            |
| FAKE_QUANT              | ✅            |
| 量子化解除              | ✅            |
| 集める                  | ✅            |
| GATHER_ND               | ✅            |
| ONE_HOT                 | ✅            |
| SQUARED_DIFFERENCE      | ✅            |
| LOG_SOFTMAX             | ✅            |
| 割る                   | ✅            |
| HARD_SWISH              | ✅            |

### 4.1.2 onnx演算子

| 演算子              | サポート対象 |
| --------------------- | ------------ |
| 米国船級協会                   | ✅            |
| アコス                  | ✅            |
| アコシュ                 | ✅            |
| そして                   | ✅            |
| 引数マックス                | ✅            |
| アルグミン                | ✅            |
| 塩辛い                  | ✅            |
| アシン                 | ✅            |
| 足す                   | ✅            |
| 平均プール           | ✅            |
| バッチ正規化    | ✅            |
| キャスト                  | ✅            |
| セイル                  | ✅            |
| 宛先                  | ✅            |
| 刈る                  | ✅            |
| 連結                | ✅            |
| 定数              | ✅            |
| 定数オブシェイプ       | ✅            |
| コンバージョン                  | ✅            |
| コンバートランスポーズ         | ✅            |
| 体                   | ✅            |
| コッシュ                  | ✅            |
| カムサム                | ✅            |
| 深度と空間          | ✅            |
| 逆量子化線形      | ✅            |
| ディビジョン                   | ✅            |
| 落ち零れ               | ✅            |
| 生命                   | ✅            |
| 経験値                   | ✅            |
| 膨らむ                | ✅            |
| 等しい                 | ✅            |
| 押し潰す               | ✅            |
| 床                 | ✅            |
| 集める                | ✅            |
| ギャザーン              | ✅            |
| ジェム                  | ✅            |
| グローバル平均プール     | ✅            |
| グローバルマックスプール         | ✅            |
| 尚               | ✅            |
| GreaterOrEqual        | ✅            |
| ハードマックス               | ✅            |
| ハードシグモイド           | ✅            |
| ハードスウィッシュ             | ✅            |
| 同一性              | ✅            |
| インスタンス正規化 | ✅            |
| Lp正規化       | ✅            |
| リーキーレル             | ✅            |
| レス                  | ✅            |
| レッサーイコール           | ✅            |
| 丸太                   | ✅            |
| ログソフトマックス            | ✅            |
| ティッカー                   | ✅            |
| ティッカー                  | ✅            |
| マトムル                | ✅            |
| マックスプール               | ✅            |
| マックス                   | ✅            |
| 分                   | ✅            |
| 私                   | ✅            |
| ネグ                   | ✅            |
| じゃない                   | ✅            |
| ワンホット                | ✅            |
| パッド                   | ✅            |
| えい                   | ✅            |
| PRelu                 | ✅            |
| 量子化線形        | ✅            |
| ランダムノーマル          | ✅            |
| ランダムノーマルライク      | ✅            |
| ランダムユニフォーム         | ✅            |
| ランダムユニフォームライク     | ✅            |
| リデュースL1              | ✅            |
| リデュースL2              | ✅            |
| ReduceLogSum          | ✅            |
| ReduceLogSumExp       | ✅            |
| リデュースマックス             | ✅            |
| ReduceMean            | ✅            |
| リデュース最小             | ✅            |
| ReduceProd            | ✅            |
| リデュースサム             | ✅            |
| ReduceSumSquare       | ✅            |
| レル                  | ✅            |
| 形状               | ✅            |
| リサイズ                | ✅            |
| リバースシーケンス       | ✅            |
| ロイアライン              | ✅            |
| 丸い                 | ✅            |
| 村                  | ✅            |
| 形                 | ✅            |
| 看板                  | ✅            |
| 無し                   | ✅            |
| 出生                  | ✅            |
| シグモイド               | ✅            |
| 大きさ                  | ✅            |
| 切る                 | ✅            |
| ソフトマックス               | ✅            |
| ソフトプラス              | ✅            |
| ソフトサイン              | ✅            |
| スペースツーデプス          | ✅            |
| 割る                 | ✅            |
| 平方キロメートル                  | ✅            |
| 絞る               | ✅            |
| サブ                   | ✅            |
| 和                   | ✅            |
| 生臭い                  | ✅            |
| 瓦                  | ✅            |
| トップK                  | ✅            |
| 転置             | ✅            |
| トリル                 | ✅            |
| アップサンプル              | ✅            |
| アンスクイーズ             | ✅            |
| どこ                 | ✅            |

### 4.1.3 caffe演算子

| 演算子              | サポート対象 |
| --------------------- | ------------ |
| インプット                 | ✅            |
| 連結                | ✅            |
| コンヴォリューション           | ✅            |
| エルトワイズ               | ✅            |
| 下取り               | ✅            |
| レル                  | ✅            |
| 形状               | ✅            |
| 切る                 | ✅            |
| ソフトマックス               | ✅            |
| 割る                 | ✅            |
| 継続インジケータ | ✅            |
| プーリング               | ✅            |
| バッチノーム             | ✅            |
| 規模                 | ✅            |
| 逆               | ✅            |
| ティッカー                  | ✅            |
| インナープロダクト          | ✅            |

## 4.2 モデル APIs をコンパイルします

現在コンパイルモデルAPIはtflite/onnx/caffeなどのディープラーニングフレームワークをサポートしています。

### 4.2.1 コンパイルオプション

**機能の説明**

compileOptions クラスで、nncase コンパイル オプションを設定します

**クラス定義**

```python
py::class_<compile_options>(m, "CompileOptions")
    .def(py::init())
    .def_readwrite("target", &compile_options::target)
    .def_readwrite("quant_type", &compile_options::quant_type)
    .def_readwrite("w_quant_type", &compile_options::w_quant_type)
    .def_readwrite("use_mse_quant_w", &compile_options::use_mse_quant_w)
    .def_readwrite("split_w_to_act", &compile_options::split_w_to_act)
    .def_readwrite("preprocess", &compile_options::preprocess)
    .def_readwrite("swapRB", &compile_options::swapRB)
    .def_readwrite("mean", &compile_options::mean)
    .def_readwrite("std", &compile_options::std)
    .def_readwrite("input_range", &compile_options::input_range)
    .def_readwrite("output_range", &compile_options::output_range)
    .def_readwrite("input_shape", &compile_options::input_shape)
    .def_readwrite("letterbox_value", &compile_options::letterbox_value)
    .def_readwrite("input_type", &compile_options::input_type)
    .def_readwrite("output_type", &compile_options::output_type)
    .def_readwrite("input_layout", &compile_options::input_layout)
    .def_readwrite("output_layout", &compile_options::output_layout)
    .def_readwrite("model_layout", &compile_options::model_layout)
    .def_readwrite("is_fpga", &compile_options::is_fpga)
    .def_readwrite("dump_ir", &compile_options::dump_ir)
    .def_readwrite("dump_asm", &compile_options::dump_asm)
    .def_readwrite("dump_quant_error", &compile_options::dump_quant_error)
    .def_readwrite("dump_dir", &compile_options::dump_dir)
    .def_readwrite("benchmark_only", &compile_options::benchmark_only);
```

各属性について以下に説明する

| プロパティ名         | 型   | 必要かどうか | 説明                                                         |
| ---------------- | ------ | -------- | ------------------------------------------------------------ |
| ターゲット           | 糸 | はい       | 'k210' 、'k510' などのコンパイルターゲットを指定します。                               |
| quant_type       | 糸 | いいえ       | 'uint8', 'int8' などのデータクオンタイズの種類を指定します。                          |
| w_quant_type     | 糸 | いいえ       | 'uint8', 'int8', デフォルト 'uint8' などの重み量子化タイプを指定します。           |
| use_mse_quant_w  | ブール   | いいえ       | 重み量子化で最小二乗誤差 (mean-square error, MSE) アルゴリズムを使用して量子化パラメータを最適化するかどうかを指定します |
| split_w_to_act   | ブール   | いいえ       | ウェイト データの一部をアクティブ化データにバランスさせるかどうかを指定します                       |
| 前処理       | ブール   | いいえ       | 前処理をオンにするかどうかは、デフォルトでは False です                                  |
| スワップRB           | ブール   | いいえ       | RGB 入力データの赤と青の 2 つのチャネル (RGB - > BGR または BGR - > RGB) を交換するかどうかは、デフォルトで False です |
| 意味する             | リスト   | いいえ       | 正規化されたパラメータ平均は、デフォルトで前処理されます[0, 0, 0]                        |
| 標準              | リスト   | いいえ       | 正規化されたパラメータ分散を前処理します(デフォルト)[1, 1, 1]                        |
| input_range      | リスト   | いいえ       | 入力データの逆量子化後の対応する浮動小数点数の範囲。デフォルトは[0，1]               |
| output_range     | リスト   | いいえ       | 固定小数点データを出力する前に浮動小数点数に対応する範囲で、デフォルトでは空です                     |
| input_shape      | リスト   | いいえ       | 入力データのshapeを指定input_shape,input_shapeのlayoutはinput layoutと一致する必要があり,入力データのinput_shapeがモデルのinput shapeと一致しない場合にはletterbox操作(resize/padなど)を行う. |
| letterbox_value  | 浮く  | いいえ       | 前処理の letterbox のパディング値を指定します                                  |
| input_type       | 糸 | いいえ       | 入力データの種類を指定します(デフォルトは 'float32')。                          |
| output_type      | 糸 | いいえ       | 出力データの種類を指定します ('float32', 'uint8' (クオンタイズを指定する場合のみ)。デフォルトは 'float32' |
| input_layout     | 糸 | いいえ       | 入力データの layout を指定します, 例えば 'NCHW', 'NHWC'. 入力データlayoutがモデル自体layoutと異なる場合、nncaseはtransposeを挿入して変換します |
| output_layout    | 糸 | いいえ       | 出力データの layout を指定します, 例えば 'NCHW', 'NHWC'. 出力データ layout がモデル自体の layout と異なる場合、nncase は変換のために transpose に挿入されます |
| model_layout     | 糸 | いいえ       | モデルの layout を指定し、デフォルトでは空で、tflite モデル layout が 'NCHW'、Onnx および Caffe モデル layout が 'NHWC' の場合に指定する必要があります |
| is_fpga          | ブール   | いいえ       | kmodel を fpga に使用するかどうかを指定します。デフォルトは False です                          |
| dump_ir          | ブール   | いいえ       | dum IR を指定し、デフォルトは False です                                 |
| dump_asm         | ブール   | いいえ       | dump asm アセンブラー ファイル (デフォルトは False) を指定します                        |
| dump_quant_error | ブール   | いいえ       | dump 量子化前と定量化後のモデル エラーを指定します                               |
| dump_dir         | 糸 | いいえ       | 前にdump_irなどのスイッチを指定した後、ここでは dump のディレクトリを指定し、デフォルトでは空の文字列を指定します  |
| benchmark_only   | ブール   | いいえ       | kmodel を benchmark にのみ使用するかどうかを指定し、デフォルトでは False です                   |

> 1. input rangeは浮動小数点数の範囲、すなわち入力データ型がuint8である、input rangeは浮動小数点まで逆量子化された範囲(0~1でもよい)である、自由に指定することができる.
> 2. input_shapeは、例えば、input_layout[1，224，224，3]がNCHWの場合、input_shapeとして指定する必要があるinput_layoutに従って指定する必要があります[1,3,224,224]。 input_layoutが NHWC の場合、input_shapeは指定する必要があります[1,224,224,3]。 
> 3. mean と std は浮動小数点数に対して normalize の引数を持ち,ユーザは自由に指定できる.
> 4. letterbox 機能を使用する場合は、入力 size を 1.5 MB 以内に制限し、シングル channel の size を 0.75 MB 内に制限する必要があります。
>
> たとえば、次のようになります。
>
> 1. 入力データ型をuint8に設定し,input_rangeに設定[0,255]すれば,逆量子化の役割は型変換のみを行い,uint8のデータをfloat32に変換し,meanとstdパラメータは0〜255のデータで指定することができる
> 2. 入力データ型を uint8 に設定input_range[0,1]、固定小数点数を範囲の浮動小数点数に逆量子化[0,1]し、mean と std を新しい浮動小数点数範囲で指定する必要があります。 

前処理の流れは次のとおりです (図の緑のノードはオプションです)。

![前処理.png](https://i.loli.net/2021/11/08/fhBLsozUTCbt4dp.png)

**コード例**

CompileOptions をインスタンス化し、各プロパティの値を構成します

```python
# compile_options
compile_options = nncase.CompileOptions()
compile_options.target = target
compile_options.input_type = 'float32'  # or 'uint8' 'int8'
compile_options.output_type = 'float32'  # or 'uint8' 'int8'. Only work in PTQ
compile_options.output_range = []  # Only work in PTQ and output type is not "float32"
compile_options.preprocess = True # if False, the args below will unworked
compile_options.swapRB = True
compile_options.input_shape = [1,224,224,3] # keep layout same as input layout
compile_options.input_layout = 'NHWC'
compile_options.output_layout = 'NHWC'
compile_options.model_layout = '' # Specific it when tflite model with "NCHW" layout and Onnx(Caffe) model with "NHWC" layout
compile_options.mean = [0,0,0]
compile_options.std = [1,1,1]
compile_options.input_range = [0,1]
compile_options.letterbox_value = 114. # pad what you want
compile_options.dump_ir = True
compile_options.dump_asm = True
compile_options.dump_dir = 'tmp'
```

### 4.2.2 インポートオプション

**機能の説明**

importOptions クラスは、nncase インポート オプションを設定するために使用されます

**クラス定義**

```python
py::class_<import_options>(m, "ImportOptions")
    .def(py::init())
    .def_readwrite("output_arrays", &import_options::output_arrays);
```

各属性について以下に説明する

| プロパティ名      | 型   | 必要かどうか | 説明     |
| ------------- | ------ | -------- | -------- |
| output_arrays | 糸 | いいえ       | 出力名 |

**コード例**

ImportOptions をインスタンス化し、各プロパティの値を構成します

```python
# import_options
import_options = nncase.ImportOptions()
import_options.output_arrays = 'output' # Your output node name
```

### 4.2.3 PTQTensorOptions

**機能の説明**

PTQTensorOptions クラスで、nncase PTQ オプションを設定するために使用されます

**クラス定義**

```python
py::class_<ptq_tensor_options>(m, "PTQTensorOptions")
    .def(py::init())
    .def_readwrite("calibrate_method", &ptq_tensor_options::calibrate_method)
    .def_readwrite("samples_count", &ptq_tensor_options::samples_count)
    .def("set_tensor_data", [](ptq_tensor_options &o, py::bytes bytes) {
        uint8_t *buffer;
        py::ssize_t length;
        if (PyBytes_AsStringAndSize(bytes.ptr(), reinterpret_cast<char **>(&buffer), &length))
            throw std::invalid_argument("Invalid bytes");
        o.tensor_data.assign(buffer, buffer + length);
    });
```

各属性について以下に説明する

| フィールド名         | 型   | 必要かどうか | 説明                                                                                  |
| ---------------- | ------ | -------- | ------------------------------------------------------------------------------------- |
| calibrate_method | 糸 | いいえ       | キャリブレーション方法 , サポート 'no_clip', 'l2', 'kld_m0', 'kld_m1', 'kld_m2', 'cdf', デフォルトは'no_clip' |
| samples_count    | int    | いいえ       | サンプルの数                                                                              |

#### set_tensor_data()

**機能の説明**

補正データを設定します

**インターフェイス定義**

```python
set_tensor_data(calib_data)
```

**パラメータを入力します**

| 引数の名前   | 型   | 必要かどうか | 説明     |
| ---------- | ------ | -------- | -------- |
| calib_data | バイト[] | はい       | データを修正します |

**戻り値**

該当なし

**コード例**

```python
# ptq_options
ptq_options = nncase.PTQTensorOptions()
ptq_options.samples_count = cfg.generate_calibs.batch_size
ptq_options.set_tensor_data(np.asarray([sample['data'] for sample in self.calibs]).tobytes())
```

### 4.2.4 コンパイラ

**機能の説明**

ニューラル ネットワーク モデルをコンパイルする Compiler クラス

**クラス定義**

```python
py::class_<compiler>(m, "Compiler")
    .def(py::init(&compiler::create))
    .def("import_tflite", &compiler::import_tflite)
    .def("import_onnx", &compiler::import_onnx)
    .def("import_caffe", &compiler::import_caffe)
    .def("compile", &compiler::compile)
    .def("use_ptq", py::overload_cast<ptq_tensor_options>(&compiler::use_ptq))
    .def("gencode", [](compiler &c, std::ostream &stream) { c.gencode(stream); })
    .def("gencode_tobytes", [](compiler &c) {
        std::stringstream ss;
        c.gencode(ss);
        return py::bytes(ss.str());
    })
    .def("create_evaluator", [](compiler &c, uint32_t stage) {
        auto &graph = c.graph(stage);
        return std::make_unique<graph_evaluator>(c.target(), graph);
    });
```

**コード例**

```python
compiler = nncase.Compiler(compile_options)
```

#### import_tflite()

**機能の説明**

tflite モデルをインポートします

**インターフェイス定義**

```python
import_tflite(model_content, import_options)
```

**パラメータを入力します**

| 引数の名前       | 型          | 必要かどうか | 説明           |
| -------------- | ------------- | -------- | -------------- |
| model_content  | バイト[]        | はい       | 読み取られたモデルの内容 |
| import_options | インポートオプション | はい       | インポート オプション       |

**戻り値**

該当なし

**コード例**

```python
model_content = read_model_file(model)
compiler.import_tflite(model_content, import_options)
```

#### import_onnx()

**機能の説明**

onnx モデルをインポートします

**インターフェイス定義**

```python
import_onnx(model_content, import_options)
```

**パラメータを入力します**

| 引数の名前       | 型          | 必要かどうか | 説明           |
| -------------- | ------------- | -------- | -------------- |
| model_content  | バイト[]        | はい       | 読み取られたモデルの内容 |
| import_options | インポートオプション | はい       | インポート オプション       |

**戻り値**

該当なし

**コード例**

```python
model_content = read_model_file(model)
compiler.import_onnx(model_content, import_options)
```

#### import_caffe()

**機能の説明**

caffe モデルをインポートします

> ユーザーは、ローカル マシンで caffe をコンパイル/インストールする必要があります。

**インターフェイス定義**

```python
import_caffe(caffemodel, prototxt)
```

**パラメータを入力します**

| 引数の名前   | 型   | 必要かどうか | 説明                 |
| ---------- | ------ | -------- | -------------------- |
| カフェモデル | バイト[] | はい       | caffemodel コンテンツを読み取ります |
| プロトトクト   | バイト[] | はい       | 読み取られた prototxt コンテンツ   |

**戻り値**

該当なし

**コード例**

```python
# import
caffemodel = read_model_file('test.caffemodel')
prototxt = read_model_file('test.prototxt')
compiler.import_caffe(caffemodel, prototxt)
```

#### use_ptq()

**機能の説明**

PTQ設定オプションを設定します

**インターフェイス定義**

```python
use_ptq(ptq_options)
```

**パラメータを入力します**

| 引数の名前    | 型             | 必要かどうか | 説明        |
| ----------- | ---------------- | -------- | ----------- |
| ptq_options | PTQTensorOptions | はい       | PTQ 設定オプション |

**戻り値**

該当なし

**コード例**

```python
compiler.use_ptq(ptq_options)
```

#### コンパイル()

**機能の説明**

ニューラル ネットワーク モデルをコンパイルします

**インターフェイス定義**

```python
compile()
```

**パラメータを入力します**

該当なし

**戻り値**

該当なし

**コード例**

```python
compiler.compile()
```

#### gencode_tobytes()

**機能の説明**

コード バイト ストリームを生成します

**インターフェイス定義**

```python
gencode_tobytes()
```

**パラメータを入力します**

該当なし

**戻り値**

バイト[]

**コード例**

```python
kmodel = compiler.gencode_tobytes()
with open(os.path.join(infer_dir, 'test.kmodel'), 'wb') as f:
    f.write(kmodel)
```

## 4.3 モデルサンプルをコンパイルします

次の例で使用するモデルと python コンパイル スクリプト

- モデルは/path/to/nncase_sdk/examples/models/サブディレクトリにあります
- python コンパイル スクリプトは/path/to/nncase_sdk/examples/scripts サブディレクトリにあります

### 4.3.1 float32 tflite モデルをコンパイルします

- mobilenetv2_tflite_fp32_image.pyスクリプトは次のとおりです

```python
import nncase
import os
import argparse

def read_model_file(model_file):
    with open(model_file, 'rb') as f:
        model_content = f.read()
    return model_content

def main():
    parser = argparse.ArgumentParser(prog="nncase")
    parser.add_argument("--target", type=str, help='target to run')
    parser.add_argument("--model", type=str, help='model file')
    args = parser.parse_args()

    # compile_options
    dump_dir = 'tmp/mobilenetv2_tflite_fp32_image'
    compile_options = nncase.CompileOptions()
    compile_options.target = args.target
    compile_options.dump_ir = True
    compile_options.dump_asm = True
    compile_options.dump_dir = dump_dir

    # compiler
    compiler = nncase.Compiler(compile_options)

    # import_options
    import_options = nncase.ImportOptions()

    # import
    model_content = read_model_file(args.model)
    compiler.import_tflite(model_content, import_options)

    # compile
    compiler.compile()

    # kmodel
    kmodel = compiler.gencode_tobytes()
    with open(os.path.join(dump_dir, 'test.kmodel'), 'wb') as f:
        f.write(kmodel)

if __name__ == '__main__':
    main()
```

- mobilenetv2 の tflite モデルをコンパイルするには、次のコマンドを実行しますが、target は k510 です

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_tflite_fp32_image.py --target k510 --model models/mobilenet_v2_1.0_224.tflite
```

### 4.3.2 float32 onnx モデルをコンパイルします

- onnx モデルでは、[onNX Simplifier ](https://github.com/daquexian/onnx-simplifier)を使用して単純化し、次に nncase を使用してコンパイルすることをお勧めします
- mobilenetv2_onnx_fp32_image.py スクリプトは次のとおりです

```python
import os
import onnxsim
import onnx
import nncase
import argparse

def parse_model_input_output(model_file):
    onnx_model = onnx.load(model_file)
    input_all = [node.name for node in onnx_model.graph.input]
    input_initializer = [node.name for node in onnx_model.graph.initializer]
    input_names = list(set(input_all) - set(input_initializer))
    input_tensors = [node for node in onnx_model.graph.input if node.name in input_names]

    # input
    inputs= []
    for _, e in enumerate(input_tensors):
        onnx_type = e.type.tensor_type
        input_dict = {}
        input_dict['name'] = e.name
        input_dict['dtype'] = onnx.mapping.TENSOR_TYPE_TO_NP_TYPE[onnx_type.elem_type]
        input_dict['shape'] = [(i.dim_value if i.dim_value != 0 else d) for i, d in zip(
            onnx_type.shape.dim, [1, 3, 224, 224])]
        inputs.append(input_dict)


    return onnx_model, inputs

def onnx_simplify(model_file, dump_dir):
    onnx_model, inputs = parse_model_input_output(model_file)
    onnx_model = onnx.shape_inference.infer_shapes(onnx_model)
    input_shapes = {}
    for input in inputs:
        input_shapes[input['name']] = input['shape']

    onnx_model, check = onnxsim.simplify(onnx_model, input_shapes=input_shapes)
    assert check, "Simplified ONNX model could not be validated"

    model_file = os.path.join(dump_dir, 'simplified.onnx')
    onnx.save_model(onnx_model, model_file)
    return model_file


def read_model_file(model_file):
    with open(model_file, 'rb') as f:
        model_content = f.read()
    return model_content


def main():
    parser = argparse.ArgumentParser(prog="nncase")
    parser.add_argument("--target", type=str, help='target to run')
    parser.add_argument("--model", type=str, help='model file')
    args = parser.parse_args()

    dump_dir = 'tmp/mobilenetv2_onnx_fp32_image'
    if not os.path.exists(dump_dir):
        os.makedirs(dump_dir)

    # onnx simplify
    model_file = onnx_simplify(args.model, dump_dir)

    # compile_options
    compile_options = nncase.CompileOptions()
    compile_options.target = args.target
    compile_options.dump_ir = True
    compile_options.dump_asm = True
    compile_options.dump_dir = dump_dir

    # compiler
    compiler = nncase.Compiler(compile_options)

    # import_options
    import_options = nncase.ImportOptions()

    # import
    model_content = read_model_file(model_file)
    compiler.import_onnx(model_content, import_options)

    # compile
    compiler.compile()

    # kmodel
    kmodel = compiler.gencode_tobytes()
    with open(os.path.join(dump_dir, 'test.kmodel'), 'wb') as f:
        f.write(kmodel)

if __name__ == '__main__':
    main()
```

- mobilenetv2 の onnx モデルをコンパイルするには、次のコマンドを実行しますが、target は k510 です

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_onnx_fp32_image.py --target k510 --model models/mobilenetv2-7.onnx
```

### 4.3.3 float32 caffe モデルをコンパイルします

- caffe wheel包は[kendryte caffeから](https://github.com/kendryte/caffe/releases)取得した
- conv2d_caffe_fp32.py スクリプトは次のとおりです

```python
import nncase
import os
import argparse

def read_model_file(model_file):
    with open(model_file, 'rb') as f:
        model_content = f.read()
    return model_content

def main():
    parser = argparse.ArgumentParser(prog="nncase")
    parser.add_argument("--target", type=str, help='target to run')
    parser.add_argument("--caffemodel", type=str, help='caffemodel file')
    parser.add_argument("--prototxt", type=str, help='prototxt file')
    args = parser.parse_args()

    # compile_options
    dump_dir = 'tmp/conv2d_caffe_fp32'
    compile_options = nncase.CompileOptions()
    compile_options.target = args.target
    compile_options.dump_ir = True
    compile_options.dump_asm = True
    compile_options.dump_dir = dump_dir

    # compiler
    compiler = nncase.Compiler(compile_options)

    # import_options
    import_options = nncase.ImportOptions()

    # import
    caffemodel = read_model_file(args.caffemodel)
    prototxt = read_model_file(args.prototxt)
    compiler.import_caffe(caffemodel, prototxt)

    # compile
    compiler.compile()

    # kmodel
    kmodel = compiler.gencode_tobytes()
    with open(os.path.join(dump_dir, 'test.kmodel'), 'wb') as f:
        f.write(kmodel)

if __name__ == '__main__':
    main()
```

- conv2d の caffe モデルをコンパイルするには、次のコマンドを実行しますが、target は k510 です

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/conv2d_caffe_fp32.py --target k510 --caffemodel models/test.caffemodel --prototxt models/test.prototxt
```

### 4.3.4 コンパイルは、float32 onnx モデルを追加する前に処理します

- onnx モデルでは、[onNX Simplifier ](https://github.com/daquexian/onnx-simplifier)を使用して単純化し、次に nncase を使用してコンパイルすることをお勧めします
- mobilenetv2_onnx_fp32_preprocess.pyスクリプトは次のとおりです

```python
import os
import onnxsim
import onnx
import nncase
import argparse

def parse_model_input_output(model_file):
    onnx_model = onnx.load(model_file)
    input_all = [node.name for node in onnx_model.graph.input]
    input_initializer = [node.name for node in onnx_model.graph.initializer]
    input_names = list(set(input_all) - set(input_initializer))
    input_tensors = [node for node in onnx_model.graph.input if node.name in input_names]

    # input
    inputs= []
    for _, e in enumerate(input_tensors):
        onnx_type = e.type.tensor_type
        input_dict = {}
        input_dict['name'] = e.name
        input_dict['dtype'] = onnx.mapping.TENSOR_TYPE_TO_NP_TYPE[onnx_type.elem_type]
        input_dict['shape'] = [(i.dim_value if i.dim_value != 0 else d) for i, d in zip(
            onnx_type.shape.dim, [1, 3, 224, 224])]
        inputs.append(input_dict)


    return onnx_model, inputs

def onnx_simplify(model_file, dump_dir):
    onnx_model, inputs = parse_model_input_output(model_file)
    onnx_model = onnx.shape_inference.infer_shapes(onnx_model)
    input_shapes = {}
    for input in inputs:
        input_shapes[input['name']] = input['shape']

    onnx_model, check = onnxsim.simplify(onnx_model, input_shapes=input_shapes)
    assert check, "Simplified ONNX model could not be validated"

    model_file = os.path.join(dump_dir, 'simplified.onnx')
    onnx.save_model(onnx_model, model_file)
    return model_file


def read_model_file(model_file):
    with open(model_file, 'rb') as f:
        model_content = f.read()
    return model_content


def main():
    parser = argparse.ArgumentParser(prog="nncase")
    parser.add_argument("--target", type=str, help='target to run')
    parser.add_argument("--model", type=str, help='model file')
    args = parser.parse_args()

    dump_dir = 'tmp/mobilenetv2_onnx_fp32_preprocess'
    if not os.path.exists(dump_dir):
        os.makedirs(dump_dir)

    # onnx simplify
    model_file = onnx_simplify(args.model, dump_dir)

    # compile_options
    compile_options = nncase.CompileOptions()
    compile_options.target = args.target
    compile_options.input_type = 'uint8'
    compile_options.preprocess = True
    compile_options.swapRB = True
    compile_options.input_layout = 'NHWC'
    compile_options.output_layout = 'NCHW'
    compile_options.input_shape = [1, 256, 256, 3]
    compile_options.mean = [0.485, 0.456, 0.406]
    compile_options.std = [0.229, 0.224, 0.225]
    compile_options.input_range = [0, 1]
    compile_options.dump_ir = True
    compile_options.dump_asm = True
    compile_options.dump_dir = dump_dir

    # compiler
    compiler = nncase.Compiler(compile_options)

    # import_options
    import_options = nncase.ImportOptions()

    # import
    model_content = read_model_file(model_file)
    compiler.import_onnx(model_content, import_options)

    # compile
    compiler.compile()

    # kmodel
    kmodel = compiler.gencode_tobytes()
    with open(os.path.join(dump_dir, 'test.kmodel'), 'wb') as f:
        f.write(kmodel)

if __name__ == '__main__':
    main()
```

- 次のコマンドを実行して、追加前処理の mobilenetv2 の onnx モデルをコンパイルし、target は k510 です

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_onnx_fp32_preprocess.py --target k510 --model models/mobilenetv2-7.onnx
```

### 4.3.5 uint8 量子化tflite モデルをコンパイルします

- mobilenetv2_tflite_uint8_image.pyスクリプトは次のとおりです

```python
import nncase
import os
import argparse
import numpy as np

def read_model_file(model_file):
    with open(model_file, 'rb') as f:
        model_content = f.read()
    return model_content

def generate_data(shape, batch):
    shape[0] *= batch
    data = np.random.rand(*shape).astype(np.float32)
    return data

def main():
    parser = argparse.ArgumentParser(prog="nncase")
    parser.add_argument("--target", type=str, help='target to run')
    parser.add_argument("--model", type=str, help='model file')
    args = parser.parse_args()

    input_shape = [1, 224, 224, 3]

    # compile_options
    dump_dir = 'tmp/mobilenetv2_tflite_uint8_image'
    compile_options = nncase.CompileOptions()
    compile_options.target = args.target
    compile_options.input_type = 'float32'
    compile_options.input_layout = 'NHWC'
    compile_options.output_layout = 'NHWC'
    compile_options.dump_ir = True
    compile_options.dump_asm = True
    compile_options.dump_dir = dump_dir

    # compiler
    compiler = nncase.Compiler(compile_options)

    # import_options
    import_options = nncase.ImportOptions()

    # quantize model
    compile_options.quant_type = 'uint8'

    # ptq_options
    ptq_options = nncase.PTQTensorOptions()
    ptq_options.samples_count = 10
    ptq_options.set_tensor_data(generate_data(input_shape, ptq_options.samples_count).tobytes())

    # import
    model_content = read_model_file(args.model)
    compiler.import_tflite(model_content, import_options)

    # compile
    compiler.use_ptq(ptq_options)
    compiler.compile()

    # kmodel
    kmodel = compiler.gencode_tobytes()
    with open(os.path.join(dump_dir, 'test.kmodel'), 'wb') as f:
        f.write(kmodel)

if __name__ == '__main__':
    main()
```

- uint8 量子化された mobilenetv2 の tflite モデルをコンパイルするには、次のコマンドを実行します(target は k510)

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_tflite_uint8_image.py --target k510 --model models/mobilenet_v2_1.0_224.tflite
```

## 4.4 推論モデル APIs

コンパイルモデルAPIsに加えて、nncaseは、PC上で生成されたkmodelをコンパイルする前に推論可能な推論モデルAPIsを提供し、nncase推論結果と対応するディープラーニングフレームワークのruntimeの結果との一貫性を検証するために使用されます。

### 4.4.1 メモリ範囲

**機能の説明**

メモリ範囲を表す MemoryRange クラス

**クラス定義**

```python
py::class_<memory_range>(m, "MemoryRange")
    .def_readwrite("location", &memory_range::memory_location)
    .def_property(
        "dtype", [](const memory_range &range) { return to_dtype(range.datatype); },
        [](memory_range &range, py::object dtype) { range.datatype = from_dtype(py::dtype::from_args(dtype)); })
    .def_readwrite("start", &memory_range::start)
    .def_readwrite("size", &memory_range::size);
```

各属性について以下に説明する

| プロパティ名 | 型           | 必要かどうか | 説明                                                                       |
| -------- | -------------- | -------- | -------------------------------------------------------------------------- |
| 場所 | int            | いいえ       | メモリ位置, 0 は input, 1 はoutput, 2 は rdata, 3 は data, 4 はshared_dataを表す |
| dtype    | python データ型 | いいえ       | データ型                                                                   |
| 始める    | int            | いいえ       | メモリの開始アドレス                                                               |
| 大きさ     | int            | いいえ       | メモリ サイズ                                                                   |

**コード例**

MemoryRange をインスタンス化します

```python
mr = nncase.MemoryRange()
```

### 4.4.2 ランタイムテンソル

**機能の説明**

ランタイム tensor を表す RuntimeTensor クラス

**クラス定義**

```python
py::class_<runtime_tensor>(m, "RuntimeTensor")
    .def_static("from_numpy", [](py::array arr) {
        auto src_buffer = arr.request();
        auto datatype = from_dtype(arr.dtype());
        auto tensor = host_runtime_tensor::create(
            datatype,
            to_rt_shape(src_buffer.shape),
            to_rt_strides(src_buffer.itemsize, src_buffer.strides),
            gsl::make_span(reinterpret_cast<gsl::byte *>(src_buffer.ptr), src_buffer.size * src_buffer.itemsize),
            [=](gsl::byte *) { arr.dec_ref(); })
                          .unwrap_or_throw();
        arr.inc_ref();
        return tensor;
    })
    .def("copy_to", [](runtime_tensor &from, runtime_tensor &to) {
        from.copy_to(to).unwrap_or_throw();
    })
    .def("to_numpy", [](runtime_tensor &tensor) {
        auto host = tensor.as_host().unwrap_or_throw();
        auto src_map = std::move(hrt::map(host, hrt::map_read).unwrap_or_throw());
        auto src_buffer = src_map.buffer();
        return py::array(
            to_dtype(tensor.datatype()),
            tensor.shape(),
            to_py_strides(runtime::get_bytes(tensor.datatype()), tensor.strides()),
            src_buffer.data());
    })
    .def_property_readonly("dtype", [](runtime_tensor &tensor) {
        return to_dtype(tensor.datatype());
    })
    .def_property_readonly("shape", [](runtime_tensor &tensor) {
        return to_py_shape(tensor.shape());
    });
```

各属性について以下に説明する

| プロパティ名 | 型 | 必要かどうか | 説明             |
| -------- | ---- | -------- | ---------------- |
| dtype    | int  | いいえ       | tensor のデータ型 |
| 形    | リスト | いいえ       | tensorの形状     |

#### from_numpy()

**機能の説明**

nnumpy.ndarrayからRuntimeTensorオブジェクトを構築します

**インターフェイス定義**

```python
from_numpy(py::array arr)
```

**パラメータを入力します**

| 引数の名前 | 型          | 必要かどうか | 説明              |
| -------- | ------------- | -------- | ----------------- |
| arr      | numpy.ndarray | はい       | numpy.ndarray オブジェクト |

**戻り値**

ランタイムテンソル

**コード例**

```python
tensor = nncase.RuntimeTensor.from_numpy(self.inputs[i]['data'])
```

#### copy_to()

**機能の説明**

コピーRuntimeTensor

**インターフェイス定義**

```python
copy_to(RuntimeTensor to)
```

**パラメータを入力します**

| 引数の名前 | 型          | 必要かどうか | 説明              |
| -------- | ------------- | -------- | ----------------- |
| 宛先       | ランタイムテンソル | はい       | RuntimeTensor オブジェクト |

**戻り値**

該当なし

**コード例**

```python
sim.get_output_tensor(i).copy_to(to)
```

#### to_numpy()

**機能の説明**

RuntimeTensor をnumpy.ndarray オブジェクトに変換します

**インターフェイス定義**

```python
to_numpy()
```

**パラメータを入力します**

該当なし

**戻り値**

numpy.ndarray オブジェクト

**コード例**

```python
arr = sim.get_output_tensor(i).to_numpy()
```

### 4.4.3 シミュレータ

**機能の説明**

SIMulator クラスは、PC 上で kmodel を推論するために使用されます

**クラス定義**

```python
py::class_<interpreter>(m, "Simulator")
    .def(py::init())
    .def("load_model", [](interpreter &interp, gsl::span<const gsl::byte> buffer) { interp.load_model(buffer).unwrap_or_throw(); })
    .def_property_readonly("inputs_size", &interpreter::inputs_size)
    .def_property_readonly("outputs_size", &interpreter::outputs_size)
    .def("get_input_desc", &interpreter::input_desc)
    .def("get_output_desc", &interpreter::output_desc)
    .def("get_input_tensor", [](interpreter &interp, size_t index) { return interp.input_tensor(index).unwrap_or_throw(); })
    .def("set_input_tensor", [](interpreter &interp, size_t index, runtime_tensor tensor) { return interp.input_tensor(index, tensor).unwrap_or_throw(); })
    .def("get_output_tensor", [](interpreter &interp, size_t index) { return interp.output_tensor(index).unwrap_or_throw(); })
    .def("set_output_tensor", [](interpreter &interp, size_t index, runtime_tensor tensor) { return interp.output_tensor(index, tensor).unwrap_or_throw(); })
    .def("run", [](interpreter &interp) { interp.run().unwrap_or_throw(); });
```

各属性について以下に説明する

| プロパティ名     | 型 | 必要かどうか | 説明     |
| ------------ | ---- | -------- | -------- |
| inputs_size  | int  | いいえ       | 数を入力します |
| outputs_size | int  | いいえ       | 出力の数 |

**コード例**

Simulator をインスタンス化します

```python
sim = nncase.Simulator()
```

#### load_model()

**機能の説明**

kmodel をロードします

**インターフェイス定義**

```python
load_model(model_content)
```

**パラメータを入力します**

| 引数の名前      | 型   | 必要かどうか | 説明         |
| ------------- | ------ | -------- | ------------ |
| model_content | バイト[] | はい       | kmodel バイト ストリーム |

**戻り値**

該当なし

**コード例**

```python
sim.load_model(kmodel)
```

#### get_input_desc()

**機能の説明**

指定したインデックスへの入力の説明情報を取得します

**インターフェイス定義**

```python
get_input_desc(index)
```

**パラメータを入力します**

| 引数の名前 | 型 | 必要かどうか | 説明       |
| -------- | ---- | -------- | ---------- |
| インデックス    | int  | はい       | 入力のインデックス |

**戻り値**

メモリ範囲

**コード例**

```python
input_desc_0 = sim.get_input_desc(0)
```

#### get_output_desc()

**機能の説明**

指定したインデックスの出力の説明情報を取得します

**インターフェイス定義**

```python
get_output_desc(index)
```

**パラメータを入力します**

| 引数の名前 | 型 | 必要かどうか | 説明       |
| -------- | ---- | -------- | ---------- |
| インデックス    | int  | はい       | 出力のインデックス |

**戻り値**

メモリ範囲

**コード例**

```python
output_desc_0 = sim.get_output_desc(0)
```

#### get_input_tensor()

**機能の説明**

指定したインデックスへの入力の RuntimeTensor を取得します

**インターフェイス定義**

```python
get_input_tensor(index)
```

**パラメータを入力します**

| 引数の名前 | 型 | 必要かどうか | 説明             |
| -------- | ---- | -------- | ---------------- |
| インデックス    | int  | はい       | tensorのインデックスを入力します |

**戻り値**

ランタイムテンソル

**コード例**

```python
input_tensor_0 = sim.get_input_tensor(0)
```

#### set_input_tensor()

**機能の説明**

指定したインデックスの入力の RuntimeTensor を設定します

**インターフェイス定義**

```python
set_input_tensor(index, tensor)
```

**パラメータを入力します**

| 引数の名前 | 型          | 必要かどうか | 説明                    |
| -------- | ------------- | -------- | ----------------------- |
| インデックス    | int           | はい       | RuntimeTensorのインデックスを入力します |
| テンソル   | ランタイムテンソル | はい       | RuntimeTensor と入力します       |

**戻り値**

該当なし

**コード例**

```python
sim.set_input_tensor(0, nncase.RuntimeTensor.from_numpy(self.inputs[0]['data']))
```

#### get_output_tensor()

**機能の説明**

指定したインデックスの出力の RuntimeTensor を取得します

**インターフェイス定義**

```python
get_output_tensor(index)
```

**パラメータを入力します**

| 引数の名前 | 型 | 必要かどうか | 説明                    |
| -------- | ---- | -------- | ----------------------- |
| インデックス    | int  | はい       | RuntimeTensorのインデックスを出力します |

**戻り値**

ランタイムテンソル

**コード例**

```python
output_arr_0 = sim.get_output_tensor(0).to_numpy()
```

#### set_output_tensor()

**機能の説明**

指定したインデックスの出力の RuntimeTensor を設定します

**インターフェイス定義**

```python
set_output_tensor(index, tensor)
```

**パラメータを入力します**

| 引数の名前 | 型          | 必要かどうか | 説明                    |
| -------- | ------------- | -------- | ----------------------- |
| インデックス    | int           | はい       | RuntimeTensorのインデックスを出力します |
| テンソル   | ランタイムテンソル | はい       | 出力RuntimeTensor       |

**戻り値**

該当なし

**コード例**

```python
sim.set_output_tensor(0, tensor)
```

#### run()

**機能の説明**

kmodel 推論を実行します

**インターフェイス定義**

```python
run()
```

**パラメータを入力します**

該当なし

**戻り値**

該当なし

**コード例**

```python
sim.run()
```

## 4.5 推論モデルの例

**前提条件**: mobilenetv2_onnx_fp32_image.pyスクリプトは mobilenetv2-7.onnx モデルをコンパイルしました

mobilenetv2_onnx_simu.pyは/path/to/nncase_sdk/examples/scripts サブディレクトリにあり、内容は次のとおりです

```python
import os
import copy
import argparse
import numpy as np
import onnxruntime as ort
import nncase

def read_model_file(model_file):
    with open(model_file, 'rb') as f:
        model_content = f.read()
    return model_content

def cosine(gt, pred):
    return (gt @ pred) / (np.linalg.norm(gt, 2) * np.linalg.norm(pred, 2))

def main():
    parser = argparse.ArgumentParser(prog="nncase")
    parser.add_argument("--model_file", type=str, help='original model file')
    parser.add_argument("--kmodel_file", type=str, help='kmodel file')
    parser.add_argument("--input_file", type=str, help='input bin file for kmodel')
    args = parser.parse_args()

    # create simulator
    sim = nncase.Simulator()

    # read kmodel
    kmodel = read_model_file(args.kmodel_file)

    # load kmodel
    sim.load_model(kmodel)

    # read input.bin
    input_tensor=sim.get_input_tensor(0).to_numpy()
    input = np.fromfile(args.input_file, input_tensor.dtype).reshape(input_tensor.shape)

    # set input for simulator
    sim.set_input_tensor(0, nncase.RuntimeTensor.from_numpy(input))

    # simulator inference
    nncase_results = []
    sim.run()
    for i in range(sim.outputs_size):
        nncase_result = sim.get_output_tensor(i).to_numpy()
        nncase_results.append(copy.deepcopy(nncase_result))

    # cpu inference
    cpu_results = []
    ort_session = ort.InferenceSession(args.model_file)
    input_name = ort_session.get_inputs()[0].name
    output_name = ort_session.get_outputs()[0].name
    cpu_results = ort_session.run([output_name], { input_name : input })

    # compare
    for i in range(sim.outputs_size):
        cos = cosine(np.reshape(nncase_results[i], (-1)), np.reshape(cpu_results[i], (-1)))
        print('output {0} cosine similarity : {1}'.format(i, cos))

if __name__ == '__main__':
    main()
```

推論スクリプトを実行します

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_onnx_simu.py --model_file models/mobilenetv2-7.onnx --kmodel_file tmp/mobilenetv2_onnx_fp32_image/test.kmodel --input_file mobilenetv2_onnx_fp32_image/data/input_0_0.bin
```

nncase simulatorとcpu推論結果を以下のように比較した

```shell
... ...
output 0 cosine similarity : 0.9992437958717346
```

# 5 nncase ランタイム ライブラリ

## 5.1 nncase Runtime の概要

nncase runtimeは、AI装置にkmodel/設定入力データをロード/KPU演算/取得出力データ等を実行するためのものである.

現在、APIs の **C++ バージョンのみが利用可能**で、関連するヘッダー ファイルと nncase sdk/riscv64 ディレクトリの静的ライブラリがあります

```bash
$ tree -L 3 riscv64/
riscv64/
├── include
│   ├── gsl
│   │   └── gsl-lite.hpp
│   ├── gsl-lite
│   │   └── gsl-lite.hpp
│   ├── mpark
│   │   ├── config.hpp
│   │   ├── in_place.hpp
│   │   ├── lib.hpp
│   │   └── variant.hpp
│   └── nncase
│       ├── functional
│       ├── kernels
│       ├── runtime
│       └── version.h
└── lib
    ├── cmake
    │   ├── nncasefunctional
    │   ├── nncase_rt_modules_k510
    │   └── nncaseruntime
    ├── libnncase.functional.a
    ├── libnncase.rt_modules.k510.a
    └── libnncase.runtime.a

13 directories, 10 files
```

## 5.2 ランタイム API

### 5.2.1 クラスruntime_tensor

モデルの入出力データを格納する tensor

#### hrt::create()

**機能の説明**

runtime_tensorを作成します

**インターフェイス定義**

```C++
(1) NNCASE_API result<runtime_tensor> create(datatype_t datatype, runtime_shape_t shape, memory_pool_t pool = pool_cpu_only, uintptr_t physical_address = 0) noexcept;

(2) NNCASE_API result<runtime_tensor> create(datatype_t datatype, runtime_shape_t shape, gsl::span<gsl::byte> data, bool copy, memory_pool_t pool = pool_cpu_only, uintptr_t physical_address = 0) noexcept;
```

**パラメータを入力します**

| 引数の名前         | 型                  | 必要かどうか | 説明                              |
| ---------------- | --------------------- | -------- | --------------------------------- |
| データ型         | datatype_t            | はい       | dt_float32などのデータ型            |
| 形            | runtime_shape_t       | はい       | tensorの形状                      |
| データ             | gsl::span\<gsl::byte> | はい       | ユーザー状態データバッフル                  |
| 写し             | ブール                  | はい       | コピーするかどうか                          |
| プール             | memory_pool_t         | いいえ       | メモリ プールの種類 (既定値はpool_cpu_only) |
| physical_address | uintptr_t             | いいえ       | 物理アドレス、既定値は 0 です               |

**戻り値**

結果<runtime_tensor>

コード例

```c++
// create input
auto in_shape = interp.input_shape(0);
auto input_tensor = host_runtime_tensor::create(dt_float32, in_shape,
                                                {(gsl::byte *)mat.data, mat.cols * mat.rows * mat.elemSize()},
                                                true, hrt::pool_shared).expect("cannot create input tensor");
```

### 5.2.2 クラスインタプリタ

interpreter は、load_model()/run()/input_tensor()/output_tensor()などのコア関数を提供する nncase runtime の実行インスタンスです。

#### load_model()

**機能の説明**

kmodel モデルをロードします

**インターフェイス定義**

```C++
 NNCASE_NODISCARD result<void> load_model(gsl::span<const gsl::byte> buffer) noexcept;
```

**パラメータを入力します**

| 引数の名前 | 型                            | 必要かどうか | 説明          |
| -------- | ------------------------------- | -------- | ------------- |
| バッファ   | gsl::span `<const gsl::byte>` | はい       | kmodel バッファ |

**戻り値**

結果 `<void>`

**コード例**

```c++
template <class T>
std::vector<T>read_binary_file(const char *file_name)
{
  std::ifstream ifs(file_name, std::ios::binary);
  ifs.seekg(0, ifs.end);
  size_t len = ifs.tellg();
  std::vector<T> vec(len / sizeof(T), 0);
  ifs.seekg(0, ifs.beg);
  ifs.read(reinterpret_cast<char*>(vec.data()), len);
  ifs.close();
  return vec;
}

interpreter interp;
auto model = read_binary_file<unsigned char>(kmodel);
interp.load_model({(const gsl::byte *)model.data(), model.size()}).expect("cannot load model.");
```

#### inputs_size()

**機能の説明**

モデル入力の数を取得します

**インターフェイス定義**

```C++
size_t inputs_size() const noexcept;
```

**パラメータを入力します**

該当なし

**戻り値**

size_t

**コード例**

```c++
auto inputs_size = interp.inputs_size();
```

#### outputs_size()

**機能の説明**

モデル出力の数を取得します

**インターフェイス定義**

```C++
size_t outputs_size() const noexcept;
```

**パラメータを入力します**

該当なし

**戻り値**

size_t

**コード例**

```c++
auto outputs_size = interp.outputs_size();
```

#### input_shape()

**機能の説明**

モデルが入力を指定するシェープを取得します

**インターフェイス定義**

```C++
const runtime_shape_t &input_shape(size_t index) const noexcept;
```

**パラメータを入力します**

| 引数の名前 | 型   | 必要かどうか | 説明       |
| -------- | ------ | -------- | ---------- |
| インデックス    | size_t | はい       | 入力のインデックス |

**戻り値**

runtime_shape_t

**コード例**

```c++
auto in_shape = interp.input_shape(0);
```

#### output_shape()

**機能の説明**

モデル指定出力のシェープを取得します

**インターフェイス定義**

```C++
const runtime_shape_t &output_shape(size_t index) const noexcept;
```

**パラメータを入力します**

| 引数の名前 | 型   | 必要かどうか | 説明       |
| -------- | ------ | -------- | ---------- |
| インデックス    | size_t | はい       | 出力のインデックス |

**戻り値**

runtime_shape_t

**コード例**

```c++
auto out_shape = interp.output_shape(0);
```

#### input_tensor()

**機能の説明**

指定したインデックスの input tensor を取得/設定します

**インターフェイス定義**

```C++
(1) result<runtime_tensor> input_tensor(size_t index) noexcept;
(2) result<void> input_tensor(size_t index, runtime_tensor tensor) noexcept;
```

**パラメータを入力します**

| 引数の名前 | 型           | 必要かどうか | 説明                     |
| -------- | -------------- | -------- | ------------------------ |
| インデックス    | size_t         | はい       | kmodel バッファ            |
| テンソル   | runtime_tensor | はい       | 対応する runtime tensor を入力します |

**戻り値**

(1)result を返します<runtime_tensor>

(2) レスレットを返します `<void>`

**コード例**

```c++
// set input
interp.input_tensor(0, input_tensor).expect("cannot set input tensor");
```

#### output_tensor()

**機能の説明**

指定したインデックスの output tensor を取得/設定します

**インターフェイス定義**

```C++
(1) result<runtime_tensor> output_tensor(size_t index) noexcept;
(2) result<void> output_tensor(size_t index, runtime_tensor tensor) noexcept;
```

**パラメータを入力します**

| 引数の名前 | 型           | 必要かどうか | 説明                     |
| -------- | -------------- | -------- | ------------------------ |
| インデックス    | size_t         | はい       |                          |
| テンソル   | runtime_tensor | はい       | 対応する runtime tensor を入力します |

**戻り値**

(1)result を返します<runtime_tensor>

(2) レスレットを返します `<void>`

**コード例**

```c++
// get output
auto output_tensor = interp.output_tensor(0).expect("cannot get output tensor");
auto mapped_buf = std::move(hrt::map(output_tensor, hrt::map_read).unwrap_or_throw());
float *output_data = reinterpret_cast<float *>(mapped_buf.buffer().data());
auto out_shape = interp.output_shape(0);
auto it = std::max_element(output_data, output_data + compute_size(out_shape));
size_t idx = it - output_data;
std::cout << "image classification result: " << labels[idx] << "(" << *it << ")" << std::endl;
```

#### run()

**機能の説明**

kpu 計算を実行します

**インターフェイス定義**

```C++
result<void> run() noexcept;
```

**パラメータを入力します**

該当なし

**戻り値**

結果 `<void>`

**コード例**

```c++
// run
interp.run().expect("error occurred in running model");
```

## 5.3 Runtime の例

サンプル コードは/path/to/nncase_sdk/examples/mobilenetv2_onnx_fp32_imageにあります

**前置条件**

- mobilenetv2_onnx_fp32_image.pyスクリプトは mobilenetv2-7.onnx モデルをコンパイルしました
- この例は OpenCV ライブラリに依存しているため、サンプルの CMakeLists .txtで OpenCV へのパスを指定する必要があります。

**アプリをクロスコンパイルします**

```shell
cd /path/to/nncase_sdk/examples
./build.sh
```

最後に、out/bin ディレクトリの下にmobilenetv2_onnx_fp32_imageを生成します

**k510 EVB上板が動作します**

以下のファイルをk510 EVBボードにコピーします

| ファイルです                        | 備考                                                         |
| --------------------------- | ------------------------------------------------------------ |
| mobilenetv2_onnx_fp32_image | examples ビルドをクロスコンパイルします                                         |
| test.kmodel                 | mobilenetv2_onnx_fp32_image.pyを使用して、mobilenetv2-7.onnx ビルドをコンパイルします |
| cat.pngとlabels_1000.txt    | /path/to/nncase_sdk/examples/mobilenetv2_onnx_fp32_image/data/サブディレクトリの下にあります |

```bash
$ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mnt/zhangyang/nncase_check/lib/gomp:/mnt/zhangyang/nncase_check/lib/opencv
$ ./mobilenetv2_onnx_fp32_image test.kmodel cat.png labels_1000.txt
case ./mobilenetv2_onnx_fp32_image build at Mar  1 2022 16:31:29
interp.run() duration: 12.6642 ms
image classification result: tiger cat(9.25)
```

# 6 関数型プログラミング ライブラリ (ランタイム サポート)

## 6.1 Functionalのプロフィール

nncase Functionalは,ユーザがモデルを前後に処理する際の使いやすさを高めるために用いられる

現在、APIs の C++ バージョンのみが利用可能です, 関連するヘッダー ファイルとライブラリは、nncase sdk の riscv64 ディレクトリの下にあります。

## 6.2 アプリ

### 6.2.1 正方形

**機能の説明**

計算平方は、現在、入力uint8/int8をサポート、出力もuint8/int8であり、入力が固定小数点である、出力が浮動小数点である場合には量子化パラメータを設定する必要がある.

**インターフェイス定義**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`square`](#ops_8h_1adff2f60c7c045a9840519eab2c04d127)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**パラメータを入力します**

| 引数の名前  | 型           | 必要かどうか | 説明                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | はい       | 入力します                |
| `dtype` | datatype_t     | はい       | 出力tensor datatype |

**戻り値**

`result<runtime_tensor>`

**コード例**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto squared = F::square(input, output_type).unwrap_or_throw();
```

### 6.2.2 平方

**機能の説明**

ルート番号の値を算出する、現在は入力uint8/int8をサポートし、出力もuint8/int8である、入力が固定小数点であり、出力が浮動小数点である場合には量子化パラメータを設定必要がある.

**インターフェイス定義**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`sqrt`](#ops_8h_1a53f8dde3dd4e27058b5dc743eb5dd076)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**パラメータを入力します**

| 引数の名前  | 型           | 必要かどうか | 説明                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | はい       | 入力します                |
| `dtype` | datatype_t     | はい       | 出力tensor datatype |

**戻り値**

`result<runtime_tensor>`

**コード例**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::sqrt(input, output_type).unwrap_or_throw();
```

### 6.2.3 ログ

**機能の説明**

log値を計算すると、入力の負数がNanに変換され、現在は入力uint8/int8がサポートされ、出力もuint8/int8となり、入力が固定小数点で出力が浮動小数点である場合には量子化パラメータを設定する必要がある.

**インターフェイス定義**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`log`](#ops_8h_1a91df53276c3f1511427d4ac1a0140b71)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**パラメータを入力します**

| 引数の名前  | 型           | 必要かどうか | 説明                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | はい       | 入力します                |
| `dtype` | datatype_t     | はい       | 出力tensor datatype |

**戻り値**

`result<runtime_tensor>`

**コード例**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::log(input, output_type).unwrap_or_throw();
```

### 6.2.4 経験値

**機能の説明**

exp値の算出は、現在、入力uint8/int8をサポートており、出力もuint8/int8である、入力が固定小数点であり、出力が浮動小数点である場合には量子化パラメータを設定必要がある.

**インターフェイス定義**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`exp`](#ops_8h_1a2c6ce457805a5ba515fa7454fb4aede0)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**パラメータを入力します**

| 引数の名前  | 型           | 必要かどうか | 説明                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | はい       | 入力します                |
| `dtype` | datatype_t     | はい       | 出力tensor datatype |

**戻り値**

`result<runtime_tensor>`

**コード例**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::exp(input, output_type).unwrap_or_throw();
```

### 6.2.5 なし

**機能の説明**

sin値を算出する、現在は入力uint8/int8をサポートし、出力もuint8/int8である、入力が固定小数点であり、出力が浮動小数点である場合には量子化パラメータを設定必要がある.

**インターフェイス定義**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`sin`](#ops_8h_1a9605b2b0dc9a6892ce878bda14586890)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**パラメータを入力します**

| 引数の名前  | 型           | 必要かどうか | 説明                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | はい       | 入力します                |
| `dtype` | datatype_t     | はい       | 出力tensor datatype |

**戻り値**

`result<runtime_tensor>`

**コード インスタンス**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::sin(input, output_type).unwrap_or_throw();
```

### 6.2.6 本文

**機能の説明**

cos値の算出は、現在、入力uint8/int8をサポート、出力もuint8/int8であり、入力が固定小数点である、出力が浮動小数点である場合には量子化パラメータを設定する必要がある.

**インターフェイス定義**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`cos`](#ops_8h_1a71d36c13c82f4c411f24d030cf333249)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**パラメータを入力します**

| 引数の名前  | 型           | 必要かどうか | 説明                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | はい       | 入力します                |
| `dtype` | datatype_t     | はい       | 出力tensor datatype |

**戻り値**

`result<runtime_tensor>`

**コード インスタンス**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::cos(input, output_type).unwrap_or_throw();
```

### 6.2.7ラウンド

**機能の説明**

round値の算出は、現在、入力uint8/int8をサポートており、出力もuint8/int8である、入力が固定小数点であり、出力が浮動小数点である場合には量子化パラメータを設定必要がある.

**インターフェイス定義**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`round`](#ops_8h_1a81db8ac4866004f75fb65db876262785)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**パラメータを入力します**

| 引数の名前  | 型           | 必要かどうか | 説明                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | はい       | 入力します                |
| `dtype` | datatype_t     | はい       | 出力tensor datatype |

**戻り値**

`result<runtime_tensor>`

**コード インスタンス**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::round(input, output_type).unwrap_or_throw();
```

### 6.2.8階建て

**機能の説明**

floor値の計算は、現在、入力uint8/int8をサポートており、出力もuint8/int8である、入力が固定小数点であり、出力が浮動小数点である場合には量子化パラメータを設定必要がある.

**インターフェイス定義**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`floor`](#ops_8h_1a1079af8fe9fb6edbb2906d91fac12635)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**パラメータを入力します**

| 引数の名前  | 型           | 必要かどうか | 説明                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | はい       | 入力します                |
| `dtype` | datatype_t     | はい       | 出力tensor datatype |

**戻り値**

`result<runtime_tensor>`

**コード インスタンス**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::floor(input, output_type).unwrap_or_throw();
```

### 6.2.9 セイル

**機能の説明**

ceil値の算出は、現在、入力uint8/int8をサポートており、出力もuint8/int8である、入力が固定小数点であり、出力が浮動小数点である場合には量子化パラメータを設定必要がある.

**インターフェイス定義**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`ceil`](#ops_8h_1ad3b78c97f1e5348a26de7e5ba2396fb7)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**パラメータを入力します**

| 引数の名前  | 型           | 必要かどうか | 説明                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | はい       | 入力します                |
| `dtype` | datatype_t     | はい       | 出力tensor datatype |

**戻り値**

`result<runtime_tensor>`

**コード インスタンス**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::ceil(input, output_type).unwrap_or_throw();
```

### 6.2.10腹筋

**機能の説明**

abs値の算出は、現在、入力uint8/int8をサポートており、出力もuint8/int8である、入力が固定小数点であり、出力が浮動小数点である場合には量子化パラメータを設定必要がある.

**インターフェイス定義**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`abs`](#ops_8h_1ad8290dc793bae0dc22b3baf9e0f80c14)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**パラメータを入力します**

| 引数の名前  | 型           | 必要かどうか | 説明                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | はい       | 入力します                |
| `dtype` | datatype_t     | はい       | 出力tensor datatype |

**戻り値**

`result<runtime_tensor>`

**コード インスタンス**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::abs(input, output_type).unwrap_or_throw();
```

### 6.2.11ネグ

**機能の説明**

neg値の算出は、現在、入力uint8/int8をサポートており、出力もuint8/int8である、入力が固定小数点であり、出力が浮動小数点である場合には量子化パラメータを設定必要がある.

**インターフェイス定義**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`neg`](#ops_8h_1aa1b7858802e1afce78db72163c5210d8)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**パラメータを入力します**

| 引数の名前  | 型           | 必要かどうか | 説明                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | はい       | 入力します                |
| `dtype` | datatype_t     | はい       | 出力tensor datatype |

**戻り値**

`result<runtime_tensor>`

**コード インスタンス**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::neg(input, output_type).unwrap_or_throw();
```

### 6.2.12 量子化

**機能の説明**

入力dt_bfloat16、データのdt_float32、出力dt_int8、またはdt_uint8出力

**インターフェイス定義**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`quantize`](#ops_8h_1ad8ad779083b5c08da520d2f1c2469c3a)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**パラメータを入力します**

| 引数の名前  | 型           | 必要かどうか | 説明                                |
| --------- | -------------- | -------- | ----------------------------------- |
| `input` | runtime_tensor | はい       | 入力、タイプは float32 または bfloat16 である必要があります |
| `dtype` | datatype_t     | はい       | 出力tensor datatype                 |

**戻り値**

`result<runtime_tensor>`

**コード インスタンス**

```cpp
auto quantized = F::quantize(input, dt_int8).unwrap_or_throw();
```

### 6.2.13 逆量子化

**機能の説明**

uint8 or int8 と入力し、float or bfloat データに変換します。 なお、逆量子化には、事前にデータに対して正しい量子化パラメータを設定必要がある.

**インターフェイス定義**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`dequantize`](#ops_8h_1ab91a262349baf393c91abad6f393de24)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**パラメータを入力します**

| 引数の名前  | 型           | 必要かどうか | 説明                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | はい       | 入力します                |
| `dtype` | datatype_t     | はい       | 出力tensor datatype |

**戻り値**

`result<runtime_tensor>`

**コード インスタンス**

```cpp
input.quant_param({ 0, 1 });
auto dequantized = F::dequantize(input, output_type).unwrap_or_throw();
```

### 6.2.14 クロップ

**機能の説明**

bboxsを与えると、元のtensorからトリミング、resizeが新しいtensorに出力される. dt_bfloat16、dt_float32、dt_int8、dt_uint8タイプの出力を受け入れ、同じタイプを出力します。

**インターフェイス定義**

`NNCASE_API inline result<runtime::runtime_tensor> crop(runtime::runtime_tensor &input, runtime::runtime_tensor &bbox, size_t out_h, size_t out_w, image_resize_mode_t resize_mode, bool align_corners, bool half_pixel_centers) noexcept`

**パラメータを入力します**

| 引数の名前           | 型                | 必要かどうか | 説明                                                                                     |
| ------------------ | ------------------- | -------- | ---------------------------------------------------------------------------------------- |
| インプット              | runtime_tensor      | はい       | データを入力するには、 [n,c,h,w] フォーマットの配置が必要です       |
| ボックス               | runtime_tensor      | はい       | bbox データを入力するには、 [1,1,m,4] フォーマットレイアウト[y0,x0,y1,x1]が必要です[フロート32,ブフロート16] |
| out_h              | size_t              | はい       | 出力データ height                                                                           |
| out_w              | size_t              | はい       | データ width を入力します                                                                            |
| resize_mode        | image_resize_mode_t | はい       | resize メソッド モード                                                                           |
| align_corners      | ブール                | はい       | resize かどうか align_corners                                                    |
| half_pixel_centers | ブール                | はい       | resize が pixel 中心揃えかどうか                                                                  |

**戻り値**

`result<runtime_tensor>`

**コード インスタンス**

```cpp
auto bbox = get_rand_bbox(input_shape, roi_amount);
auto &&[out_h, out_w] = get_rand_out_hw();
auto output_opt = F::crop(input, bbox, out_h, out_w, resize_mode).unwrap_or_throw();
```

### 6.2.15 サイズ変更

**機能の説明**

出力高さの幅を指定して、入力tensor resizeを新しいサイズにします。 dt_bfloat16、dt_float32、dt_int8、dt_uint8タイプの出力を受け入れ、同じタイプを出力します。

**インターフェイス定義**

`NNCASE_API inline result<runtime::runtime_tensor> resize(runtime::runtime_tensor &input, size_t out_h, size_t out_w, image_resize_mode_t resize_mode, bool align_corners, bool half_pixel_centers) noexcept`

**パラメータを入力します**

| 引数の名前           | 型                | 必要かどうか | 説明                                                                               |
| ------------------ | ------------------- | -------- | ---------------------------------------------------------------------------------- |
| インプット              | runtime_tensor      | はい       | データを入力するには、 [n,c,h,w] フォーマットの配置が必要です。 データが uint8 または int8 の場合は、データ量子化パラメータの正確性を確保してください |
| out_h              | size_t              | はい       | 出力データ height                                                                     |
| out_w              | size_t              | はい       | データ width を入力します                                                                      |
| resize_mode        | image_resize_mode_t | はい       | resize メソッド モード                                                                     |
| align_corners      | ブール                | はい       | resize かどうか align_corners                                              |
| half_pixel_centers | ブール                | はい       | resize が pixel 中心揃えかどうか                                                            |

**戻り値**

`result<runtime_tensor>`

**コード インスタンス**

```cpp
auto &&[out_h, out_w] = get_rand_out_hw();
auto output_opt = F::resize(input, out_h, out_w, resize_mode, false, false).unwrap_or_throw();
```

### 6.2.16パッド

**機能の説明**

各次元でpaddingデータは、dt_bfloat16、dt_float32、dt_int8、dt_uint8タイプの出力を受け入れ、同じタイプを出力します。

**インターフェイス定義**

`NNCASE_API inline result<runtime::runtime_tensor> pad(runtime::runtime_tensor &input, runtime_paddings_t &paddings, pad_mode_t pad_mode, float fill_v)`

**パラメータを入力します**

| 引数の名前 | 型               | 必要かどうか | 説明                                                                                                                                       |
| -------- | ------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| インプット    | runtime_tensor     | はい       | 入力データ、データが uint8 または int8 の場合は、データ量子化パラメータの正確性を確認します                                                                                  |
| 心地  | runtime_paddings_t | はい       | 各次元のpadding値は、逆の順序に注意してください. たとえば、pading 値は `[ {2,3}, {1,3} ]`、最後の 1 次元の前に papad 2 を表し、後ろの papad 3. 最後の 2 次元のフロントパッド 1 と背面のパッド 2 を表します |
| pad_mode | pad_mode_t         | はい       | 現在、const モードのみがサポートされています                                                                                                                   |
| fill_v   | 浮く              | はい       | 値を入力します                                                                                                                                     |

**戻り値**

`result<runtime_tensor>`

**コード インスタンス**

```cpp
runtime_paddings_t paddings{ { 0, 0 }, { 0, 0 }, { 0, 0 }, { 1, 2 } };
auto output = F::pad(input, paddings, pad_constant, pad_value).unwrap_or_throw();
```
<!-- markdownlint-enable no-emphasis-as-header -->
# 7 ホワイト ペーパーを定量化します

## 7.1 分類モデルの定量化に関するホワイト ペーパー

| 分類モデル     | cpu 精度 (Top-1) | 浮動小数点精度(Top-1) | uint8 精度 (Top-1) | int8 精度 (Top-1) |
| ------------ | -------------- | --------------- | ---------------- | --------------- |
| アレックスネット      | 0.531          | 0.53            | 該当なし              | 0.52            |
| デンスネット121 | 0.732          | 0.732           | 0.723            | 該当なし             |
| 開始 v3 | 0.766          | 0.765           | 0.773            | 0.77            |
| インセプション v4 | 0.789          | 0.789           | 0.793            | 0.792           |
| モバイルネットv1の | 0.731          | 0.73            | 0.723            | 0.718           |
| モバイルネットv2の | 0.713          | 0.715           | 0.713            | 0.719           |
| resnet50 v2  | 0.747          | 0.74            | 0.748            | 0.749           |
| VGG 16       | 0.689          | 0.687           | 0.690            | 0.689           |

> この表は、主に量子化のパフォーマンスを比較するために、CPU 精度は完全な ImageNet 検証セット データであり、浮動小数点精度と量子化精度は、データのサブセット テストの結果として、シーケンス番号に従って最初に表示される検証セット 1000 クラスの画像です。
>
> AlexnetとDenseNetのテスト結果は古いデータであり,いずれも検証セットの上位1000枚の画像をデータサブセットとしてテスト結果であり,N/Aは当時のテストデータのサブセットがCPUと異なるため,比較しない.
>
> 選択したネットワークは、必ずしも公式または前処理などとの違いから生じるため、公式のパフォーマンスとは異なる場合があります。

## 7.2 検出モデルの定量化に関するホワイト ペーパー

1. ヨロブ3

    | ココアピ                                                      | 公式結果 | CPU 浮動小数点精度 | gnne浮動小数点精度 | uint8 精度 | int8 精度 |
    | ------------------------------------------------------------ | -------- | ----------- | ------------ | --------- | -------- |
    | 平均精度 (AP) @ [IoU = 0.50:0.95\|エリア = すべて \|最大デット = 100] | 0.314    | 0.307       | 0.306        | 0.295     | 0.288    |
    | 平均精度 (AP) @ [IoU = 0.50\|エリア = すべて \|最大デット = 100] | 0.559    | 0.555       | 0.554        | 0.555     | 0.554    |
    | 平均精度 (AP) @ [IoU = 0.75\|エリア = すべて \|最大デット = 100] | 0.318    | 0.308       | 0.307        | 0.287     | 0.275    |
    | 平均精度 (AP) @ [IoU = 0.50:0.95\|面積 = 小さい \|最大デット = 100] | 0.142    | 0.150       | 0.149        | 0.147     | 0.144    |
    | 平均精度 (AP) @ [IoU= 0.50:0.95\|面積 = 中 \|最大デット = 100] | 0.341    | 0.332       | 0.332        | 0.322     | 0.316    |
    | 平均精度 (AP) @ [IoU = 0.50:0.95\|面積 = 大 \|最大デット = 100] | 0.464    | 0.437       | 0.437        | 0.414     | 0.404    |
    | 平均リコール (AR) @ [IoU= 0.50:0.95\|エリア = すべて \|最大デット = 1] | 0.278    | 0.270       | 0.271        | 0.262     | 0.256    |
    | 平均リコール (AR) @ [IoU= 0.50:0.95\|エリア = すべて \|最大デット = 10] | 0.419    | 0.412       | 0.412        | 0.399     | 0.392    |
    | 平均リコール (AR) @ [IoU = 0.50:0.95\|エリア = すべて \|最大デット = 100] | 0.442    | 0.433       | 0.433        | 0.421     | 0.414    |
    | 平均リコール (AR) @ [IoU = 0.50:0.95\|面積 = 小さい \|最大デット = 100] | 0.239    | 0.251       | 0.251        | 0.248     | 0.246    |
    | 平均リコール (AR) @ [IoU= 0.50:0.95\|面積 = 中 \|最大デット = 100] | 0.482    | 0.462       | 0.463        | 0.451     | 0.443    |
    | 平均リコール (AR) @ [IoU = 0.50:0.95\|面積 = 大 \|最大デット = 100] | 0.611    | 0.586       | 0.585        | 0.559     | 0.550    |

2. ssd-mobilenetv1

    | ココアピ                                                                    | 公式結果 | CPU 浮動小数点精度 | gnne浮動小数点精度 | uint8 精度 | int8 精度 |
    | -------------------------------------------------------------------------- | -------- | ----------- | ------------ | --------- | -------- |
    | 平均精度(AP)@ [IoU = 0.50:0.95\|エリア = すべて \|最大デット = 100]   | 0.184    | 0.184       | 0.184        | 0.183     | 0.183    |
    | 平均精度(AP)@ [IoU = 0.50\|エリア = すべて \|最大デット = 100]        | 0.306    | 0.307       | 0.306        | 0.305     | 0.306    |
    | 平均精度(AP)@ [IoU = 0.75\|エリア = すべて \|最大デット = 100]        | 0.191    | 0.192       | 0.190        | 0.189     | 0.190    |
    | 平均精度 (AP) @ [IoU = 0.50:0.95\|面積 = 小さい \|最大デット = 100] | 0.017    | 0.017       | 0.017        | 0.017     | 0.017    |
    | 平均精度 (AP) @ [IoU= 0.50:0.95\|面積 = 中 \|最大デット = 100] | 0.157    | 0.157       | 0.157        | 0.156     | 0.155    |
    | 平均精度 (AP) @ [IoU = 0.50:0.95\|面積 = 大 \|最大デット = 100] | 0.371    | 0.372       | 0.371        | 0.370     | 0.369    |
    | 平均リコール (AR)@ [IoU= 0.50:0.95\|エリア = すべて \|最大デット = 1]         | 0.180    | 0.180       | 0.180        | 0.181     | 0.181    |
    | 平均リコール (AR)@ [IoU= 0.50:0.95\|エリア = すべて \|最大デット = 10]        | 0.242    | 0.242       | 0.242        | 0.243     | 0.243    |
    | 平均リコール (AR)@ [IoU = 0.50:0.95\|エリア = すべて \|最大デット = 100]      | 0.242    | 0.242       | 0.242        | 0.243     | 0.243    |
    | 平均リコール (AR)@ [IoU = 0.50:0.95\|面積 = 小さい \|最大デット = 100]    | 0.026    | 0.026       | 0.026        | 0.026     | 0.026    |
    | 平均リコール (AR)@ [IoU= 0.50:0.95\|面積 = 中 \|最大デット = 100]    | 0.206    | 0.206       | 0.206        | 0.206     | 0.205    |
    | 平均リコール (AR)@ [IoU = 0.50:0.95\|面積 = 大 \|最大デット = 100]    | 0.489    | 0.491       | 0.490        | 0.490     | 0.491    |

3. ヨロブ5S

    | ココアピ                                                                    | 公式結果 | CPU 浮動小数点精度 | gnne浮動小数点精度 | uint8 精度 | int8 精度 |
    | -------------------------------------------------------------------------- | -------- | ----------- | ------------ | --------- | -------- |
    | 平均精度(AP)@ [IoU = 0.50:0.95\|エリア = すべて \|最大デット = 100]   | 0.367    | 0.365       | 0.335        | 0.334     | 0.335    |
    | 平均精度(AP)@ [IoU = 0.50\|エリア = すべて \|最大デット = 100]        | 0.555    | 0.552       | 0.518        | 0.518     | 0.518    |
    | 平均精度(AP)@ [IoU = 0.75\|エリア = すべて \|最大デット = 100]        | 0.398    | 0.395       | 0.364        | 0.363     | 0.362    |
    | 平均精度 (AP) @ [IoU = 0.50:0.95\|面積 = 小さい \|最大デット = 100] | 0.223    | 0.220       | 0.199        | 0.199     | 0.197    |
    | 平均精度 (AP) @ [IoU= 0.50:0.95\|面積 = 中 \|最大デット = 100] | 0.419    | 0.418       | 0.387        | 0.386     | 0.386    |
    | 平均精度 (AP) @ [IoU = 0.50:0.95\|面積 = 大 \|最大デット = 100] | 0.463    | 0.459       | 0.423        | 0.422     | 0.423    |
    | 平均リコール (AR)@ [IoU= 0.50:0.95\|エリア = すべて \|最大デット = 1]         | 0.306    | 0.306       | 0.288        | 0.287     | 0.287    |
    | 平均リコール (AR)@ [IoU= 0.50:0.95\|エリア = すべて \|最大デット = 10]        | 0.518    | 0.518       | 0.487        | 0.486     | 0.487    |
    | 平均リコール (AR)@ [IoU = 0.50:0.95\|エリア = すべて \|最大デット = 100]      | 0.576    | 0.576       | 0.540        | 0.539     | 0.540    |
    | 平均リコール (AR)@ [IoU = 0.50:0.95\|面積 = 小さい \|最大デット = 100]    | 0.391    | 0.399       | 0.350        | 0.350     | 0.347    |
    | 平均リコール (AR)@ [IoU= 0.50:0.95\|面積 = 中 \|最大デット = 100]    | 0.641    | 0.640       | 0.606        | 0.605     | 0.607    |
    | 平均リコール (AR)@ [IoU = 0.50:0.95\|面積 = 大 \|最大デット = 100]    | 0.716    | 0.710       | 0.680        | 0.683     | 0.685    |

# 8 よくある質問

1.安装ホイール时报错: "xxx.whl はこのプラットフォームでサポートされているホイールではありません。**

Q: 安装nncase wheel包, 出现ERROR: nncase-1.0.0.20210830-cp37-cp37m-manylinux_2_24_x86_64.whl はこのプラットフォームでサポートされているホイールではありません。

A: pip > = 20.3 をアップグレードします

```shell
sudo pip3 install --upgrade pip
```

**2.CRBがApp推論プログラムを実行すると,誤りは"std::bad_alloc"**

Q: CRB は App 推論プログラムを実行し、"std::bad_alloc" 例外をスローします

```shell
$ ./cpp.sh
case ./yolov3_bfloat16 build at Sep 16 2021 18:12:03
terminate called after throwing an instance of 'std::bad_alloc'
  what():  std::bad_alloc
```

A: std:: bad_alloc例外は、通常、メモリ割り当ての失敗が原因で発生します。

- 生成されたkmodelが現在のシステム使用可能メモリを超えているかどうかを確認します(例えば、yolov3 bfloat16 kmodelサイズは121MB、現在のLinux空きメモリは70MBのみであり、例外がスローされます)。  超える場合は、トレーニング後のクオンタイズを使用して kmodel サイズを小さくしてみてください。
- アプリにメモリ リークがないかどうかを確認します

3.App**推論プログラムを実行すると[..t_runtime_tensor.cpp:310 (作成)] data.size_bytes() = = size = false (bool) になります**

Q: simulator は App 推論プログラムを実行し、"[..t_runtime_tensor.cpp:310 (作成)] data.size_bytes() == size = false (bool)" 例外をスローします

A: 入力シェープと各要素が占有するバイト数 (fp32/uint8) に焦点を当てて、入力 tensor 情報の設定を確認します。

**免責事項を翻訳します**  
お客様の便宜のために、カナアンはAI翻訳プログラムを使用してテキストを複数の言語に翻訳し、エラーが含まれている可能性があります。 当社は、提供される翻訳の正確性、信頼性、または適時性を保証するものではありません。 カナアンは、翻訳された情報の正確性または信頼性への依存に起因するいかなる損失または損害についても責任を負いません。 異なる言語翻訳間でコンテンツの違いがある場合は、簡体字中国語版が優先されます。 

翻訳エラーや不正確な問題を報告する場合は、メールでお問い合わせください。