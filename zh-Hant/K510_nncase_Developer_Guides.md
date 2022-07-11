![迦南蓋.png](http://s2.loli.net/2022/03/30/7UG1IxrOXTo2QKw.png)

**<font face="黑体" size="6" style="float:right">K510 nncase 開發者指南</font>**

<font face="黑体"  size=3>文件版本：V1.0.1</font>

<font face="黑体"  size=3>發佈日期：2022-05-10</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**免責聲明**</font>
您購買的產品、服務或特性等應受北京嘉楠捷思資訊技術有限公司（“本公司”，下同）商業合同和條款的約束，本文檔中描述的全部或部分產品、服務或特性可能不在您的購買或使用範圍之內。 除非合同另有約定，本公司不對本文檔的任何陳述、資訊、內容的準確性、可靠性、完整性、行銷型、特定目的性和非侵略性提供任何明示或默示的聲明或保證。 除非另有約定，本文檔僅作為使用指導的參考。
由於產品版本升級或其他原因，本文檔內容將可能在未經任何通知的情況下，不定期進行更新或修改。

**<font face="黑体"  size=3>商標聲明</font>**

“<img src="http://s2.loli.net/2022/03/30/xN21jbhnwSFyGRD.png" style="zoom:33%;" />”、“Canaan”圖示、嘉楠和嘉楠其他商標均為北京嘉楠捷思資訊技術有限公司的商標。 本文檔可能提及的其他所有商標或註冊商標，由各自的所有人擁有。

**<font face="黑体"  size=3>版權所有©2022北京嘉楠捷思資訊技術有限公司</font>**
本文檔僅適用K510平台開發設計，非經本公司書面許可，任何單位和個人不得以任何形式對本文檔的部分或全部內容傳播。

**<font face="黑体"  size=3>北京嘉楠捷思資訊技術有限公司</font>**
網址：canaan-creative.com
商務垂詢：salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# 前言
**<font face="黑体"  size=5>文件目的</font>**
本文檔為nncase/K510 compiler的使用說明文檔，提供給使用者如何安裝nncase， 如何調用compiler APIs編譯神經網路模型和runtime APIs編寫AI推理程式.

**<font face="黑体"  size=5>讀者物件</font>**

本文檔（本指南）主要適用的人員：

- 軟體開發人員
- 技術支持人員

**<font face="黑体"  size=5>術語及縮略詞</font>**

| 術語 | 解釋/全稱                              |
| ---- | -------------------------------------- |
| PTQ  | Post-training quantization， 訓練後量化 |
| 微分方程式  | mean-square error， 均方誤差            |
|      |                                        |

**<font face="黑体"  size=5>修訂記錄</font>**
 <font face="宋体"  size=2>修訂記錄累積了每次文檔更新的說明。 最新版本的文件包含以前所有版本的更新內容。 </font>

| 版本號   | 修改者     | 修訂日期 | 修訂說明 |
|  :-----  |-------   |  ------  |  ------  |
| 1.0.1 版 | 張揚 | 2022-05-10 | nncase_v1.6.1 |
| 1.0.0 版 | 張揚/張濟昭/楊浩琪 | 2022-05-06 | nncase_v1.6.0 |
| 版本0.9.0 | 張揚 | 2022-04-01 | nncase_v1.5.0 |
| 版本0.8.0 | 張揚/張濟昭 | 2022-03-03 | nncase_v1.4.0 |
| 版本0.7.0 | 張揚 | 2022-01-28 | nncase_v1.3.0 |
| 版本0.6.0 | 張揚 | 2021-12-31 | nncase_v1.2.0 |
| 0.5.0 版 | 張揚 | 2021-12-03 | nncase_v1.1.0 |
| 版本0.4.0 | 張揚/楊浩琪/鄭啟航 | 2021-10-29 | nncase_v1.0.0 |
| 0.3.0 版 | 張揚/楊浩琪 | 2021-09-28 | nncase_v1.0.0_rc1 |
| 0.2.0 版 | 張揚/楊浩琪 | 2021-09-02 | nncase_v1.0.0_beta2 |
| 0.1.0 版 | 張揚/楊浩琪 | 2021-08-31 | nncase_v1.0.0_beta1 |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>目 錄</font>**

[目錄]

<div style="page-break-after:always"></div>

# 1 開發環境簡介

## 1.1 操作系統

- Ubuntu 18.04/20.04

## 1.2 軟體環境

軟體環境要求如下表所示：

| 序號 | 軟體資源        | 說明                        |
| ---- | --------------- | --------------------------- |
| 1    | 蟒          | Python 3.6/3.7/3.8/3.9/3.10 |
| 2    | 點3            | pip3版本 >= 20.3            |
| 3    | onnx            | onnx版本為1.9.0             |
| 4    | onnx-simplify | onnx-simplifier版本為0.3.6  |
| 5    | onnxoptimizer   | onnxoptimizer版本為0.2.6    |

## 1.3 硬體環境

硬體環境要求如下表所示：

| 序號 | 硬體資源     | 說明 |
| ---- | ------------ | ---- |
| 1    | K510 斷續器     |      |
| 2    | SD卡及讀卡機 |      |

# 2 nncase簡介

## 2.1 什麼是nncase

nncase是一個為 AI 加速器設計的神經網路編譯器， 目前支援的 target 有cpu /K210/K510 等

nncase提供的功能

- 支援多輸入多輸出網路，支援多分支結構
- 靜態記憶體分配，不需要堆記憶體
- 算子合併和優化
- 支援 float 和uint8/int8量化推理
- 支持訓練後量化，使用浮點模型和量化校準集
- 平坦模型，支持零拷貝載入

nncase支持的神經網路框架

- 斷續器
- onnx
- 咖啡

## 2.2 產品優勢

- **簡單的端到端部署**

  減少與使用者交互的次數。 使用者使用和部署 CPU、GPU 模型相同的工具和流程就可完成在 KPU 上的部署。 無需設置複雜的參數，降低使用門檻，加速 AI 演算法的反覆運算週期。
- **充分利用現有AI生態**

  依附於業內廣泛使用的框架。 一方面可以提高知名度，享受到成熟生態的紅利。 另一方面可以降低中小開發商的開發成本，業界成熟的模型和演算法可以直接部署。
- **充分發揮硬體性能**

  NPU的優勢就在於效能比CPU、GPU高，DL Compiler必須能夠充分發揮硬體的性能。 Compiler還需要對新模型結構自適應地優化性能，因此需要在手工優化之外探索一條新的自動優化技術。
- **可擴展性和可維護性**

  能夠支援 K210、K510 以及將來晶片的 AI 模型部署。 需要在架構層面提供一定的可擴充性。 增加新 Target 的代價要小，能夠盡可能複用更多的模組。 加快新產品的研發速度實現 DL Compiler 的技術積累。

## 2.3 nncase架構

<img src="https://i.loli.net/2021/08/18/IQR12SOJdzxTUZH.png" alt="nncase_arch.png" style="zoom:67%;" />

nnncase軟體棧目前包括compiler和runtime兩部分。

**Compiler：** 用於在PC上編譯神經網路模型，最終生成kmodel檔。 主要包括importer， IR， Evaluator， Quantize， Transform優化， Tiling， Partition， Schedule， Codegen等模組。

- Importer： 將其它神經網路框架的模型導入到nncase中
- IR： 中間表示， 分為importer導入的Neutral IR（設備無關）和Neutral IR經lowering轉換生成的Target IR（設備相關）
- Evaluator： Evaluator提供IR的解釋執行能力，常被用於Constant Folding/PTQ Calibration等場景
- Transform： 用於IR轉換和圖的遍歷優化等
- Quantize： 訓練後量化， 對要量化的tensor加入量化標記， 根據輸入的校正集， 調用 Evaluator進行解釋執行， 收集tensor的數據範圍， 插入量化/反量化結點， 最後優化消除不必要的量化/反量化結點等
- Tiling： 受限於NPU較低的記憶體容量，需要將大塊計算進行拆分. 另外， 計算存在大量數據復用時選擇Tiling參數會對時延和頻寬產生影響
- Partition： 將圖按ModuleType進行切分， 切分后的每個子圖會對應RuntimeModule， 不同類型的RuntimeModule對應不同的Device（cpu/K510）
- Schedule： 根據優化後圖中的數據依賴關係生成計算順序並分配Buffer
- Codegen： 對每個子圖分別調用ModuleType對應的codegen，生成RuntimeModule

**Runtime**： 整合於使用者App， 提供載入kmodel/設置輸入資料/KPU執行/獲取輸出數據等功能.

# 3 安裝nncase

nncase工具鏈compiler部分包括nncase和K510 compiler， 均需安裝相應wheel包.

- nncase wheel包在[nncase github](https://github.com/kendryte/nncase/releases/tag/v1.6.0)發佈， 支援Python 3.6/3.7/3.8/3.9/3.10， 使用者可根據操作系統和Python選擇相應版本下載 .
- K510 compiler wheel包在nncase sdk的x86_64目錄下， 不依賴Python版本， 可直接安裝

使用者若沒有Ubuntu環境， 可使用[nncase docker](https://github.com/kendryte/nncase/blob/master/docs/build.md#docker)（Ubuntu 20.04 + Python 3.8）

```shell
cd /path/to/nncase_sdk
docker pull registry.cn-hangzhou.aliyuncs.com/kendryte/nncase:latest
docker run -it --rm -v `pwd`:/mnt -w /mnt registry.cn-hangzhou.aliyuncs.com/kendryte/nncase:latest /bin/bash -c "/bin/bash"
```

下面以Ubuntu 20.04 + Python 3.8安裝nncase為例

```shell
wget -P x86_64 https://github.com/kendryte/nncase/releases/download/v1.6.0/nncase-1.6.0.20220505-cp38-cp38-manylinux_2_24_x86_64.whl
pip3 install x86_64/*.whl
```
<!-- markdownlint-disable no-emphasis-as-header -->
# 4 編譯/推理模型

nncase提供了**Python API**s， 用於在PC上編譯/推理深度學習模型.

## 4.1 支援的算子

### 4.1.1 tflite算子

| 算子                | 受支援 |
| ----------------------- | ------------ |
| 斷續器                     | ✅            |
| 加                     | ✅            |
| ARG_MAX                 | ✅            |
| ARG_MIN                 | ✅            |
| AVERAGE_POOL_2D         | ✅            |
| BATCH_MATMUL            | ✅            |
| 投                    | ✅            |
| 中鋁                    | ✅            |
| 串聯           | ✅            |
| CONV_2D                 | ✅            |
| 身體                     | ✅            |
| 習慣                  | ✅            |
| DEPTHWISE_CONV_2D       | ✅            |
| 迪維                     | ✅            |
| 平等                   | ✅            |
| 經驗值                     | ✅            |
| EXPAND_DIMS             | ✅            |
| 地板                   | ✅            |
| FLOOR_DIV               | ✅            |
| FLOOR_MOD               | ✅            |
| FULLY_CONNECTED         | ✅            |
| 大                 | ✅            |
| GREATER_EQUAL           | ✅            |
| L2_NORMALIZATION        | ✅            |
| LEAKY_RELU              | ✅            |
| 少                    | ✅            |
| LESS_EQUAL              | ✅            |
| 日誌                     | ✅            |
| 物流                | ✅            |
| MAX_POOL_2D             | ✅            |
| 最大                 | ✅            |
| 意味著                    | ✅            |
| 最低                 | ✅            |
| 我                     | ✅            |
| 負極                     | ✅            |
| NOT_EQUAL               | ✅            |
| 墊                     | ✅            |
| 帕德維2                   | ✅            |
| MIRROR_PAD              | ✅            |
| 包                    | ✅            |
| 戰俘                     | ✅            |
| REDUCE_MAX              | ✅            |
| REDUCE_MIN              | ✅            |
| REDUCE_PROD             | ✅            |
| 雷魯                    | ✅            |
| 普魯                   | ✅            |
| 迴路6                   | ✅            |
| 重塑                 | ✅            |
| RESIZE_BILINEAR         | ✅            |
| RESIZE_NEAREST_NEIGHBOR | ✅            |
| 圓                   | ✅            |
| 斷續器                   | ✅            |
| 形狀                   | ✅            |
| 沒有                     | ✅            |
| 片                   | ✅            |
| SOFTMAX                 | ✅            |
| SPACE_TO_BATCH_ND       | ✅            |
| 擠                 | ✅            |
| BATCH_TO_SPACE_ND       | ✅            |
| STRIDED_SLICE           | ✅            |
| SQRT                    | ✅            |
| 廣場                  | ✅            |
| 子                     | ✅            |
| 和                     | ✅            |
| 腥                    | ✅            |
| 瓦                    | ✅            |
| 轉置               | ✅            |
| TRANSPOSE_CONV          | ✅            |
| 量化                | ✅            |
| FAKE_QUANT              | ✅            |
| 去量化              | ✅            |
| 收集                  | ✅            |
| GATHER_ND               | ✅            |
| ONE_HOT                 | ✅            |
| SQUARED_DIFFERENCE      | ✅            |
| LOG_SOFTMAX             | ✅            |
| 分裂                   | ✅            |
| HARD_SWISH              | ✅            |

### 4.1.2 onnx算子

| 算子              | 受支援 |
| --------------------- | ------------ |
| 腹肌                   | ✅            |
| 阿科斯                  | ✅            |
| 阿科什                 | ✅            |
| 和                   | ✅            |
| 阿格麥克斯                | ✅            |
| 阿格敏                | ✅            |
| 鹹                  | ✅            |
| 阿辛                 | ✅            |
| 加                   | ✅            |
| 平均池           | ✅            |
| 批次規範化    | ✅            |
| 投                  | ✅            |
| 錫爾                  | ✅            |
| 自                  | ✅            |
| 剪輯                  | ✅            |
| 康卡特                | ✅            |
| 不斷              | ✅            |
| ConstantOfShape       | ✅            |
| 轉化                  | ✅            |
| ConvTranspose         | ✅            |
| 身體                   | ✅            |
| 科什                  | ✅            |
| CumSum                | ✅            |
| 深度到空間          | ✅            |
| DequantizeLinear      | ✅            |
| 迪夫                   | ✅            |
| 輟學               | ✅            |
| 生命                   | ✅            |
| 到期日                   | ✅            |
| 擴大                | ✅            |
| 平等                 | ✅            |
| 扁平 化               | ✅            |
| 地板                 | ✅            |
| 收集                | ✅            |
| 聚集              | ✅            |
| 寶石                  | ✅            |
| 全球平均池     | ✅            |
| GlobalMaxPool         | ✅            |
| 大               | ✅            |
| 大等        | ✅            |
| 哈迪麥克斯               | ✅            |
| 硬西格莫           | ✅            |
| 硬絞痛             | ✅            |
| 身份              | ✅            |
| 實例規範化 | ✅            |
| LpNormalization       | ✅            |
| LeakyRelu             | ✅            |
| 少                  | ✅            |
| LessOrequal           | ✅            |
| 日誌                   | ✅            |
| LogSoftmax            | ✅            |
| 斷續器                   | ✅            |
| 斷續器                  | ✅            |
| 馬特穆爾                | ✅            |
| 最大池               | ✅            |
| 麥克斯                   | ✅            |
| 最小值                   | ✅            |
| 我                   | ✅            |
| 否定                   | ✅            |
| 不                   | ✅            |
| 一個熱                | ✅            |
| 墊                   | ✅            |
| 戰俘                   | ✅            |
| 普魯                 | ✅            |
| 量化線性        | ✅            |
| 隨機正態          | ✅            |
| 隨機正常類      | ✅            |
| 隨機均勻         | ✅            |
| 隨機類似     | ✅            |
| 還原L1              | ✅            |
| 還原L2              | ✅            |
| ReduceLogSum          | ✅            |
| ReduceLogSumExp       | ✅            |
| ReduceMax             | ✅            |
| ReduceMean            | ✅            |
| ReduceMin             | ✅            |
| ReduceProd            | ✅            |
| 減少和             | ✅            |
| ReduceSumSquare       | ✅            |
| 雷魯                  | ✅            |
| 重塑               | ✅            |
| 調整                | ✅            |
| 反向序列       | ✅            |
| 羅伊阿利恩              | ✅            |
| 圓                 | ✅            |
| 村                  | ✅            |
| 形狀                 | ✅            |
| 標誌                  | ✅            |
| 沒有                   | ✅            |
| 出生                  | ✅            |
| 乙狀結腸               | ✅            |
| 大小                  | ✅            |
| 片                 | ✅            |
| Softmax               | ✅            |
| Softplus              | ✅            |
| 軟簽名              | ✅            |
| 太空深度          | ✅            |
| 分裂                 | ✅            |
| Sqrt                  | ✅            |
| 擠               | ✅            |
| 子                   | ✅            |
| 和                   | ✅            |
| 腥                  | ✅            |
| 瓦                  | ✅            |
| 托普凱                  | ✅            |
| 轉置             | ✅            |
| 三鹿                 | ✅            |
| 上採樣              | ✅            |
| 解壓縮             | ✅            |
| 哪裡                 | ✅            |

### 4.1.3 caffe算子

| 算子              | 受支援 |
| --------------------- | ------------ |
| 輸入                 | ✅            |
| 康卡特                | ✅            |
| 卷積           | ✅            |
| 埃爾特維斯               | ✅            |
| 以舊換新               | ✅            |
| relu                  | ✅            |
| 重塑               | ✅            |
| 片                 | ✅            |
| Softmax               | ✅            |
| 分裂                 | ✅            |
| 延續指示器 | ✅            |
| 池               | ✅            |
| BatchNorm             | ✅            |
| 規模                 | ✅            |
| 反向               | ✅            |
| 斷續器                  | ✅            |
| 內部產品          | ✅            |

## 4.2 編譯模型APIs

目前編譯模型API支援tflite/onnx/caffe等深度學習框架.

### 4.2.1 編譯選項

**功能描述**

CompileOptions類， 用於配置nncase編譯選項

**類定義**

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

各屬性說明如下

| 屬性名稱         | 類型   | 是否必須 | 描述                                                         |
| ---------------- | ------ | -------- | ------------------------------------------------------------ |
| 目標           | 字串 | 是       | 指定編譯目標， 如'k210'， 'k510'                               |
| quant_type       | 字串 | 否       | 指定數據量化類型， 如'uint8'， 'int8'                          |
| w_quant_type     | 字串 | 否       | 指定權重量化類型， 如'uint8'， 'int8'， 預設為'uint8'           |
| use_mse_quant_w  | 布爾   | 否       | 指定權重量化時是否使用最小化均方誤差（mean-square error， MSE）演算法優化量化參數 |
| split_w_to_act   | 布爾   | 否       | 指定是否將部分權重數據平衡到激活數據中                       |
| 預處理       | 布爾   | 否       | 是否開啟前處理，預設為False                                  |
| 交換RB           | 布爾   | 否       | 是否交換RGB輸入數據的紅和藍兩個通道（RGB-->BGR或者BGR-->RGB），預設為False |
| 意味著             | 清單   | 否       | 前處理標準化參數均值，預設為[0, 0, 0]                        |
| 性病              | 清單   | 否       | 前處理標準化參數方差，預設為[1, 1, 1]                        |
| input_range      | 清單   | 否       | 輸入數據反量化后對應浮點數的範圍，預設為[0，1]               |
| output_range     | 清單   | 否       | 輸出定點數據前對應浮點數的範圍，預設為空                     |
| input_shape      | 清單   | 否       | 指定輸入數據的shape，input_shape的layout需要與input layout保持一致，輸入數據的input_shape與模型的input shape不一致時會進行letterbox操作（resize/pad等） |
| letterbox_value  | 浮  | 否       | 指定前處理letterbox的填充值                                  |
| input_type       | 字串 | 否       | 指定輸入資料的類型， 預設為『float32』                          |
| output_type      | 字串 | 否       | 指定輸出資料的類型， 如'float32'， 'uint8'（僅用於指定量化情況下）， 預設為'float32' |
| input_layout     | 字串 | 否       | 指定輸入數據的layout， 如'NCHW'， 'NHWC'. 若輸入數據layout與模型本身layout不同， nncase會插入transpose進行轉換 |
| output_layout    | 字串 | 否       | 指定輸出數據的layout， 如'NCHW'， 'NHWC'. 若輸出數據layout與模型本身layout不同， nncase會插入transpose進行轉換 |
| model_layout     | 字串 | 否       | 指定模型的layout，預設為空，當tflite模型layout為'NCHW'，Onnx和Caffe模型layout為'NHWC'時需指定 |
| is_fpga          | 布爾   | 否       | 指定kmodel是否用於fpga， 預設為False                          |
| dump_ir          | 布爾   | 否       | 指定是否dump IR， 預設為False                                 |
| dump_asm         | 布爾   | 否       | 指定是否dump asm彙編檔， 預設為False                        |
| dump_quant_error | 布爾   | 否       | 指定是否dump量化前後的模型誤差                               |
| dump_dir         | 字串 | 否       | 前面指定dump_ir等開關後， 這裡指定dump的目錄， 預設為空字串  |
| benchmark_only   | 布爾   | 否       | 指定kmodel是否只用於benchmark， 預設為False                   |

> 1. input range為浮點數的範圍，即如果輸入數據類型為uint8，則input range為反量化到浮點之後的範圍（可以不為0~1），可以自由指定.
> 2. input_shape需要按照input_layout進行指定，以[1，224，224，3]為例，如果input_layout為NCHW，則input_shape需指定為[1,3,224,224]; input_layout為NHWC，則input_shape需指定為[1,224,224,3];
> 3. mean和std為浮點數進行normalize的參數，用戶可以自由指定;
> 4. 使用letterbox功能時，需要限制輸入size在1.5MB內，單channel的size在0.75MB內;
>
> 例如：
>
> 1. 輸入數據類型設定為uint8，input_range設定為[0,255]，則反量化的作用只是進行類型轉化，將uint8的數據轉化為float32，mean和std參數仍然可以按照0~255的數據進行指定.
> 2. 輸入數據類型設定為uint8，input_range設定為[0,1]，則會將定點數反量化為範圍為[0,1]的浮點數， mean 和std需要按照新的浮點數範圍進行指定。

前處理流程如下（圖中綠色節點皆為可選）：

![預處理.png](https://i.loli.net/2021/11/08/fhBLsozUTCbt4dp.png)

**代碼示例**

實例化CompileOptions， 配置各屬性的值

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

### 4.2.2 導入選項

**功能描述**

ImportOptions類， 用於配置nncase導入選項

**類定義**

```python
py::class_<import_options>(m, "ImportOptions")
    .def(py::init())
    .def_readwrite("output_arrays", &import_options::output_arrays);
```

各屬性說明如下

| 屬性名稱      | 類型   | 是否必須 | 描述     |
| ------------- | ------ | -------- | -------- |
| output_arrays | 字串 | 否       | 輸出名稱 |

**代碼示例**

實例化ImportOptions， 配置各屬性的值

```python
# import_options
import_options = nncase.ImportOptions()
import_options.output_arrays = 'output' # Your output node name
```

### 4.2.3 PTQ張量選項

**功能描述**

PTQTensorOptions類， 用於配置nncase PTQ選項

**類定義**

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

各屬性說明如下

| 欄位名稱         | 類型   | 是否必須 | 描述                                                                                  |
| ---------------- | ------ | -------- | ------------------------------------------------------------------------------------- |
| calibrate_method | 字串 | 否       | 校準方法 ， 支援'no_clip'， 'l2'， 'kld_m0'， 'kld_m1'， 'kld_m2'， 'cdf'， 預設是'no_clip' |
| samples_count    | 整型    | 否       | 樣本個數                                                                              |

#### set_tensor_data（）

**功能描述**

設置校正數據

**介面定義**

```python
set_tensor_data(calib_data)
```

**輸入參數**

| 參數名稱   | 類型   | 是否必須 | 描述     |
| ---------- | ------ | -------- | -------- |
| calib_data | 位元組[] | 是       | 校正數據 |

**返回值**

不適用

**代碼示例**

```python
# ptq_options
ptq_options = nncase.PTQTensorOptions()
ptq_options.samples_count = cfg.generate_calibs.batch_size
ptq_options.set_tensor_data(np.asarray([sample['data'] for sample in self.calibs]).tobytes())
```

### 4.2.4 編譯器

**功能描述**

Compiler類， 用於編譯神經網路模型

**類定義**

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

**代碼示例**

```python
compiler = nncase.Compiler(compile_options)
```

#### import_tflite（）

**功能描述**

導入tflite模型

**介面定義**

```python
import_tflite(model_content, import_options)
```

**輸入參數**

| 參數名稱       | 類型          | 是否必須 | 描述           |
| -------------- | ------------- | -------- | -------------- |
| model_content  | 位元組[]        | 是       | 讀取的模型內容 |
| import_options | 匯入選項 | 是       | 匯入選項       |

**返回值**

不適用

**代碼示例**

```python
model_content = read_model_file(model)
compiler.import_tflite(model_content, import_options)
```

#### import_onnx（）

**功能描述**

導入onnx模型

**介面定義**

```python
import_onnx(model_content, import_options)
```

**輸入參數**

| 參數名稱       | 類型          | 是否必須 | 描述           |
| -------------- | ------------- | -------- | -------------- |
| model_content  | 位元組[]        | 是       | 讀取的模型內容 |
| import_options | 匯入選項 | 是       | 匯入選項       |

**返回值**

不適用

**代碼示例**

```python
model_content = read_model_file(model)
compiler.import_onnx(model_content, import_options)
```

#### import_caffe（）

**功能描述**

導入caffe模型

> 使用者需在本地機器自行編譯/安裝caffe.

**介面定義**

```python
import_caffe(caffemodel, prototxt)
```

**輸入參數**

| 參數名稱   | 類型   | 是否必須 | 描述                 |
| ---------- | ------ | -------- | -------------------- |
| 咖啡模型 | 位元組[] | 是       | 讀取的caffemodel內容 |
| prototxt   | 位元組[] | 是       | 讀取的prototxt內容   |

**返回值**

不適用

**代碼示例**

```python
# import
caffemodel = read_model_file('test.caffemodel')
prototxt = read_model_file('test.prototxt')
compiler.import_caffe(caffemodel, prototxt)
```

#### use_ptq（）

**功能描述**

設置PTQ配置選項

**介面定義**

```python
use_ptq(ptq_options)
```

**輸入參數**

| 參數名稱    | 類型             | 是否必須 | 描述        |
| ----------- | ---------------- | -------- | ----------- |
| ptq_options | PTQTensorOptions | 是       | PTQ配置選項 |

**返回值**

不適用

**代碼示例**

```python
compiler.use_ptq(ptq_options)
```

#### 編譯（）

**功能描述**

編譯神經網路模型

**介面定義**

```python
compile()
```

**輸入參數**

不適用

**返回值**

不適用

**代碼示例**

```python
compiler.compile()
```

#### gencode_tobytes（）

**功能描述**

生成代碼位元組流

**介面定義**

```python
gencode_tobytes()
```

**輸入參數**

不適用

**返回值**

位元組[]

**代碼示例**

```python
kmodel = compiler.gencode_tobytes()
with open(os.path.join(infer_dir, 'test.kmodel'), 'wb') as f:
    f.write(kmodel)
```

## 4.3 編譯模型示例

下面示例中使用到的模型和python編譯腳本

- 模型位於/path/to/nncase_sdk/examples/models/子目錄
- python編譯腳本位於/path/to/nncase_sdk/examples/scripts子目錄

### 4.3.1 編譯float32 tflite模型

- mobilenetv2_tflite_fp32_image.py腳本如下

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

- 執行如下命令即可編譯mobilenetv2的tflite模型， target為k510

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_tflite_fp32_image.py --target k510 --model models/mobilenet_v2_1.0_224.tflite
```

### 4.3.2 編譯float32 onnx模型

- 針對onnx模型， 建議先使用[ONNX Simplifier](https://github.com/daquexian/onnx-simplifier)進行簡化， 然後再使用nncase編譯.
- mobilenetv2_onnx_fp32_image.py 腳本如下

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

- 執行如下命令即可編譯mobilenetv2的onnx模型， target為k510

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_onnx_fp32_image.py --target k510 --model models/mobilenetv2-7.onnx
```

### 4.3.3 編譯float32 caffe模型

- caffe wheel包從[kendryte caffe](https://github.com/kendryte/caffe/releases)獲取
- conv2d_caffe_fp32.py 腳本如下

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

- 執行如下命令即可編譯conv2d的caffe模型， target為k510

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/conv2d_caffe_fp32.py --target k510 --caffemodel models/test.caffemodel --prototxt models/test.prototxt
```

### 4.3.4 編譯添加前處理float32 onnx模型

- 針對onnx模型， 建議先使用[ONNX Simplifier](https://github.com/daquexian/onnx-simplifier)進行簡化， 然後再使用nncase編譯.
- mobilenetv2_onnx_fp32_preprocess.py腳本如下

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

- 執行如下命令即可編譯添加前處理的mobilenetv2的onnx模型， target為k510

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_onnx_fp32_preprocess.py --target k510 --model models/mobilenetv2-7.onnx
```

### 4.3.5 編譯uint8量化tflite模型

- mobilenetv2_tflite_uint8_image.py腳本如下

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

- 執行如下命令即可編譯uint8量化的mobilenetv2的tflite模型， target為k510

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_tflite_uint8_image.py --target k510 --model models/mobilenet_v2_1.0_224.tflite
```

## 4.4 推理模型APIs

除了編譯模型APIs， nncase還提供了推理模型的APIs， 在PC上可推理前面編譯生成的kmodel， 用來驗證nncase推理結果和相應深度學習框架的runtime的結果是否一致等.

### 4.4.1 記憶體範圍

**功能描述**

MemoryRange類， 用於表示記憶體範圍

**類定義**

```python
py::class_<memory_range>(m, "MemoryRange")
    .def_readwrite("location", &memory_range::memory_location)
    .def_property(
        "dtype", [](const memory_range &range) { return to_dtype(range.datatype); },
        [](memory_range &range, py::object dtype) { range.datatype = from_dtype(py::dtype::from_args(dtype)); })
    .def_readwrite("start", &memory_range::start)
    .def_readwrite("size", &memory_range::size);
```

各屬性說明如下

| 屬性名稱 | 類型           | 是否必須 | 描述                                                                       |
| -------- | -------------- | -------- | -------------------------------------------------------------------------- |
| 位置 | 整型            | 否       | 記憶體位置， 0表示input， 1表示output， 2表示rdata， 3表示data， 4表示shared_data |
| d型    | python數據類型 | 否       | 數據類型                                                                   |
| 開始    | 整型            | 否       | 記憶體起始位址                                                               |
| 大小     | 整型            | 否       | 記憶體大小                                                                   |

**代碼示例**

實例化MemoryRange

```python
mr = nncase.MemoryRange()
```

### 4.4.2 運行時擴展

**功能描述**

RuntimeTensor類， 用於表示運行時tensor

**類定義**

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

各屬性說明如下

| 屬性名稱 | 類型 | 是否必須 | 描述             |
| -------- | ---- | -------- | ---------------- |
| d型    | 整型  | 否       | tensor的數據類型 |
| 形狀    | 清單 | 否       | tensor的形狀     |

#### from_numpy（）

**功能描述**

從numpy.ndarray構造RuntimeTensor物件

**介面定義**

```python
from_numpy(py::array arr)
```

**輸入參數**

| 參數名稱 | 類型          | 是否必須 | 描述              |
| -------- | ------------- | -------- | ----------------- |
| 到達      | numpy.ndarray | 是       | numpy.ndarray物件 |

**返回值**

運行時擴展器

**代碼示例**

```python
tensor = nncase.RuntimeTensor.from_numpy(self.inputs[i]['data'])
```

#### copy_to（）

**功能描述**

拷貝RuntimeTensor

**介面定義**

```python
copy_to(RuntimeTensor to)
```

**輸入參數**

| 參數名稱 | 類型          | 是否必須 | 描述              |
| -------- | ------------- | -------- | ----------------- |
| 自       | 運行時擴展器 | 是       | RuntimeTensor物件 |

**返回值**

不適用

**代碼示例**

```python
sim.get_output_tensor(i).copy_to(to)
```

#### to_numpy（）

**功能描述**

將RuntimeTensor轉換為numpy.ndarray物件

**介面定義**

```python
to_numpy()
```

**輸入參數**

不適用

**返回值**

numpy.ndarray物件

**代碼示例**

```python
arr = sim.get_output_tensor(i).to_numpy()
```

### 4.4.3 模擬器

**功能描述**

Simulator類， 用於在PC上推理kmodel

**類定義**

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

各屬性說明如下

| 屬性名稱     | 類型 | 是否必須 | 描述     |
| ------------ | ---- | -------- | -------- |
| inputs_size  | 整型  | 否       | 輸入個數 |
| outputs_size | 整型  | 否       | 輸出個數 |

**代碼示例**

實例化Simulator

```python
sim = nncase.Simulator()
```

#### load_model（）

**功能描述**

載入kmodel

**介面定義**

```python
load_model(model_content)
```

**輸入參數**

| 參數名稱      | 類型   | 是否必須 | 描述         |
| ------------- | ------ | -------- | ------------ |
| model_content | 位元組[] | 是       | kmodel位元節流 |

**返回值**

不適用

**代碼示例**

```python
sim.load_model(kmodel)
```

#### get_input_desc（）

**功能描述**

獲取指定索引的輸入的描述資訊

**介面定義**

```python
get_input_desc(index)
```

**輸入參數**

| 參數名稱 | 類型 | 是否必須 | 描述       |
| -------- | ---- | -------- | ---------- |
| 指數    | 整型  | 是       | 輸入的索引 |

**返回值**

記憶體範圍

**代碼示例**

```python
input_desc_0 = sim.get_input_desc(0)
```

#### get_output_desc（）

**功能描述**

獲取指定索引的輸出的描述資訊

**介面定義**

```python
get_output_desc(index)
```

**輸入參數**

| 參數名稱 | 類型 | 是否必須 | 描述       |
| -------- | ---- | -------- | ---------- |
| 指數    | 整型  | 是       | 輸出的索引 |

**返回值**

記憶體範圍

**代碼示例**

```python
output_desc_0 = sim.get_output_desc(0)
```

#### get_input_tensor（）

**功能描述**

獲取指定索引的輸入的RuntimeTensor

**介面定義**

```python
get_input_tensor(index)
```

**輸入參數**

| 參數名稱 | 類型 | 是否必須 | 描述             |
| -------- | ---- | -------- | ---------------- |
| 指數    | 整型  | 是       | 輸入tensor的索引 |

**返回值**

運行時擴展器

**代碼示例**

```python
input_tensor_0 = sim.get_input_tensor(0)
```

#### set_input_tensor（）

**功能描述**

設置指定索引的輸入的RuntimeTensor

**介面定義**

```python
set_input_tensor(index, tensor)
```

**輸入參數**

| 參數名稱 | 類型          | 是否必須 | 描述                    |
| -------- | ------------- | -------- | ----------------------- |
| 指數    | 整型           | 是       | 輸入RuntimeTensor的索引 |
| 張肌   | 運行時擴展器 | 是       | 輸入RuntimeTensor       |

**返回值**

不適用

**代碼示例**

```python
sim.set_input_tensor(0, nncase.RuntimeTensor.from_numpy(self.inputs[0]['data']))
```

#### get_output_tensor（）

**功能描述**

獲取指定索引的輸出的RuntimeTensor

**介面定義**

```python
get_output_tensor(index)
```

**輸入參數**

| 參數名稱 | 類型 | 是否必須 | 描述                    |
| -------- | ---- | -------- | ----------------------- |
| 指數    | 整型  | 是       | 輸出RuntimeTensor的索引 |

**返回值**

運行時擴展器

**代碼示例**

```python
output_arr_0 = sim.get_output_tensor(0).to_numpy()
```

#### set_output_tensor（）

**功能描述**

設置指定索引的輸出的RuntimeTensor

**介面定義**

```python
set_output_tensor(index, tensor)
```

**輸入參數**

| 參數名稱 | 類型          | 是否必須 | 描述                    |
| -------- | ------------- | -------- | ----------------------- |
| 指數    | 整型           | 是       | 輸出RuntimeTensor的索引 |
| 張肌   | 運行時擴展器 | 是       | 輸出RuntimeTensor       |

**返回值**

不適用

**代碼示例**

```python
sim.set_output_tensor(0, tensor)
```

#### 執行（）

**功能描述**

運行kmodel推理

**介面定義**

```python
run()
```

**輸入參數**

不適用

**返回值**

不適用

**代碼示例**

```python
sim.run()
```

## 4.5 推理模型示例

**前置條件**： mobilenetv2_onnx_fp32_image.py腳本已編譯過mobilenetv2-7.onnx模型

mobilenetv2_onnx_simu.py位於/path/to/nncase_sdk/examples/scripts子目錄， 內容如下

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

執行推理腳本

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_onnx_simu.py --model_file models/mobilenetv2-7.onnx --kmodel_file tmp/mobilenetv2_onnx_fp32_image/test.kmodel --input_file mobilenetv2_onnx_fp32_image/data/input_0_0.bin
```

nncase simulator和cpu推理結果對比如下

```shell
... ...
output 0 cosine similarity : 0.9992437958717346
```

# 5 nncase 運行時庫

## 5.1 nncase Runtime 簡介

nncase runtime用於在AI設備載入kmodel/設置輸入數據/執行KPU計算/獲取輸出數據等.

目前只提供**C++版本**的APIs， 相關的頭文件和靜態庫在nncase sdk/riscv64目錄下.

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

## 5.2 運行時介面

### 5.2.1 類runtime_tensor

用於存儲模型輸入/輸出數據的tensor

#### hrt：：create（）

**功能描述**

創建runtime_tensor

**介面定義**

```C++
(1) NNCASE_API result<runtime_tensor> create(datatype_t datatype, runtime_shape_t shape, memory_pool_t pool = pool_cpu_only, uintptr_t physical_address = 0) noexcept;

(2) NNCASE_API result<runtime_tensor> create(datatype_t datatype, runtime_shape_t shape, gsl::span<gsl::byte> data, bool copy, memory_pool_t pool = pool_cpu_only, uintptr_t physical_address = 0) noexcept;
```

**輸入參數**

| 參數名稱         | 類型                  | 是否必須 | 描述                              |
| ---------------- | --------------------- | -------- | --------------------------------- |
| 數據類型         | datatype_t            | 是       | 數據類型， 如dt_float32            |
| 形狀            | runtime_shape_t       | 是       | tensor的形狀                      |
| 數據             | gsl：：span\<gsl：：byte> | 是       | 用戶態數據buffer                  |
| 複製             | 布爾                  | 是       | 是否拷貝                          |
| 池             | memory_pool_t         | 否       | 記憶體池類型， 預設值為pool_cpu_only |
| physical_address | uintptr_t             | 否       | 物理位址， 預設值為0               |

**返回值**

結果<runtime_tensor>

代碼示例

```c++
// create input
auto in_shape = interp.input_shape(0);
auto input_tensor = host_runtime_tensor::create(dt_float32, in_shape,
                                                {(gsl::byte *)mat.data, mat.cols * mat.rows * mat.elemSize()},
                                                true, hrt::pool_shared).expect("cannot create input tensor");
```

### 5.2.2 類解釋器

interpreter是nncase runtime的運行實例， 它提供了load_model（）/run（）/input_tensor（）/output_tensor（）等核心功能函數.

#### load_model（）

**功能描述**

載入kmodel模型

**介面定義**

```C++
 NNCASE_NODISCARD result<void> load_model(gsl::span<const gsl::byte> buffer) noexcept;
```

**輸入參數**

| 參數名稱 | 類型                            | 是否必須 | 描述          |
| -------- | ------------------------------- | -------- | ------------- |
| 緩衝區   | gsl：：span `<const gsl::byte>` | 是       | 千米德爾緩衝液 |

**返回值**

結果 `<void>`

**代碼示例**

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

#### inputs_size（）

**功能描述**

獲取模型輸入的個數

**介面定義**

```C++
size_t inputs_size() const noexcept;
```

**輸入參數**

不適用

**返回值**

size_t

**代碼示例**

```c++
auto inputs_size = interp.inputs_size();
```

#### outputs_size（）

**功能描述**

獲取模型輸出的個數

**介面定義**

```C++
size_t outputs_size() const noexcept;
```

**輸入參數**

不適用

**返回值**

size_t

**代碼示例**

```c++
auto outputs_size = interp.outputs_size();
```

#### input_shape（）

**功能描述**

獲取模型指定輸入的shape

**介面定義**

```C++
const runtime_shape_t &input_shape(size_t index) const noexcept;
```

**輸入參數**

| 參數名稱 | 類型   | 是否必須 | 描述       |
| -------- | ------ | -------- | ---------- |
| 指數    | size_t | 是       | 輸入的索引 |

**返回值**

runtime_shape_t

**代碼示例**

```c++
auto in_shape = interp.input_shape(0);
```

#### output_shape（）

**功能描述**

獲取模型指定輸出的shape

**介面定義**

```C++
const runtime_shape_t &output_shape(size_t index) const noexcept;
```

**輸入參數**

| 參數名稱 | 類型   | 是否必須 | 描述       |
| -------- | ------ | -------- | ---------- |
| 指數    | size_t | 是       | 輸出的索引 |

**返回值**

runtime_shape_t

**代碼示例**

```c++
auto out_shape = interp.output_shape(0);
```

#### input_tensor（）

**功能描述**

獲取/設置指定索引的input tensor

**介面定義**

```C++
(1) result<runtime_tensor> input_tensor(size_t index) noexcept;
(2) result<void> input_tensor(size_t index, runtime_tensor tensor) noexcept;
```

**輸入參數**

| 參數名稱 | 類型           | 是否必須 | 描述                     |
| -------- | -------------- | -------- | ------------------------ |
| 指數    | size_t         | 是       | 千米德爾緩衝液            |
| 張肌   | runtime_tensor | 是       | 輸入對應的runtime tensor |

**返回值**

（1） 返回result<runtime_tensor>

（2） 返回result `<void>`

**代碼示例**

```c++
// set input
interp.input_tensor(0, input_tensor).expect("cannot set input tensor");
```

#### output_tensor（）

**功能描述**

獲取/設置指定索引的output tensor

**介面定義**

```C++
(1) result<runtime_tensor> output_tensor(size_t index) noexcept;
(2) result<void> output_tensor(size_t index, runtime_tensor tensor) noexcept;
```

**輸入參數**

| 參數名稱 | 類型           | 是否必須 | 描述                     |
| -------- | -------------- | -------- | ------------------------ |
| 指數    | size_t         | 是       |                          |
| 張肌   | runtime_tensor | 是       | 輸入對應的runtime tensor |

**返回值**

（1） 返回result<runtime_tensor>

（2） 返回result `<void>`

**代碼示例**

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

#### 執行（）

**功能描述**

執行kpu計算

**介面定義**

```C++
result<void> run() noexcept;
```

**輸入參數**

不適用

**返回值**

結果 `<void>`

**代碼示例**

```c++
// run
interp.run().expect("error occurred in running model");
```

## 5.3 Runtime示例

示例代碼位於/path/to/nncase_sdk/examples/mobilenetv2_onnx_fp32_image

**前置條件**

- mobilenetv2_onnx_fp32_image.py腳本已編譯過mobilenetv2-7.onnx模型
- 由於該示例依賴OpenCV庫，需要在示例的CMakeLists.txt中指定OpenCV的路徑。

**交叉編譯app**

```shell
cd /path/to/nncase_sdk/examples
./build.sh
```

最後在out/bin目錄下生成mobilenetv2_onnx_fp32_image

**k510 EVB上板運行**

將下面幾個文件拷貝到k510 EVB板上

| 檔                        | 備註                                                         |
| --------------------------- | ------------------------------------------------------------ |
| mobilenetv2_onnx_fp32_image | 交叉編譯examples生成                                         |
| test.kmodel                 | 使用mobilenetv2_onnx_fp32_image.py編譯mobilenetv2-7.onnx生成 |
| cat.png和labels_1000.txt    | 位於/path/to/nncase_sdk/examples/mobilenetv2_onnx_fp32_image/data/子目錄下 |

```bash
$ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mnt/zhangyang/nncase_check/lib/gomp:/mnt/zhangyang/nncase_check/lib/opencv
$ ./mobilenetv2_onnx_fp32_image test.kmodel cat.png labels_1000.txt
case ./mobilenetv2_onnx_fp32_image build at Mar  1 2022 16:31:29
interp.run() duration: 12.6642 ms
image classification result: tiger cat(9.25)
```

# 6 函數式程式設計庫（執行時支援）

## 6.1 Functional簡介

nncase Functional用於提升使用者對模型進行前後處理時的易用性

目前只提供C++版本的APIs， 相關的頭文件和庫在nncase sdk的riscv64目錄下.

## 6.2 應用程式介面

### 6.2.1 平方

**功能描述**

計算平方，目前支援輸入uint8/int8，輸出也為uint8/int8，注意輸入為定點且輸出為浮點時需要設置量化參數.

**介面定義**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`square`](#ops_8h_1adff2f60c7c045a9840519eab2c04d127)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**輸入參數**

| 參數名稱  | 類型           | 是否必須 | 描述                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | 是       | 輸入                |
| `dtype` | datatype_t     | 是       | 輸出tensor datatype |

**返回值**

`result<runtime_tensor>`

**代碼示例**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto squared = F::square(input, output_type).unwrap_or_throw();
```

### 6.2.2 平方呎

**功能描述**

計算根號值，目前支援輸入uint8/int8，輸出也為uint8/int8，注意輸入為定點且輸出為浮點時需要設置量化參數.

**介面定義**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`sqrt`](#ops_8h_1a53f8dde3dd4e27058b5dc743eb5dd076)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**輸入參數**

| 參數名稱  | 類型           | 是否必須 | 描述                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | 是       | 輸入                |
| `dtype` | datatype_t     | 是       | 輸出tensor datatype |

**返回值**

`result<runtime_tensor>`

**代碼示例**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::sqrt(input, output_type).unwrap_or_throw();
```

### 6.2.3 日誌

**功能描述**

計算log值，輸入的負數會被轉換為Nan，目前支援輸入uint8/int8，輸出也為uint8/int8，注意輸入為定點且輸出為浮點時需要設置量化參數.

**介面定義**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`log`](#ops_8h_1a91df53276c3f1511427d4ac1a0140b71)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**輸入參數**

| 參數名稱  | 類型           | 是否必須 | 描述                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | 是       | 輸入                |
| `dtype` | datatype_t     | 是       | 輸出tensor datatype |

**返回值**

`result<runtime_tensor>`

**代碼示例**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::log(input, output_type).unwrap_or_throw();
```

### 6.2.4 到期

**功能描述**

計算exp值，目前支援輸入uint8/int8，輸出也為uint8/int8，注意輸入為定點且輸出為浮點時需要設置量化參數.

**介面定義**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`exp`](#ops_8h_1a2c6ce457805a5ba515fa7454fb4aede0)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**輸入參數**

| 參數名稱  | 類型           | 是否必須 | 描述                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | 是       | 輸入                |
| `dtype` | datatype_t     | 是       | 輸出tensor datatype |

**返回值**

`result<runtime_tensor>`

**代碼示例**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::exp(input, output_type).unwrap_or_throw();
```

### 6.2.5 無

**功能描述**

計算sin值，目前支援輸入uint8/int8，輸出也為uint8/int8，注意輸入為定點且輸出為浮點時需要設置量化參數.

**介面定義**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`sin`](#ops_8h_1a9605b2b0dc9a6892ce878bda14586890)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**輸入參數**

| 參數名稱  | 類型           | 是否必須 | 描述                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | 是       | 輸入                |
| `dtype` | datatype_t     | 是       | 輸出tensor datatype |

**返回值**

`result<runtime_tensor>`

**代碼實例**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::sin(input, output_type).unwrap_or_throw();
```

### 6.2.6 本體

**功能描述**

計算cos值，目前支援輸入uint8/int8，輸出也為uint8/int8，注意輸入為定點且輸出為浮點時需要設置量化參數.

**介面定義**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`cos`](#ops_8h_1a71d36c13c82f4c411f24d030cf333249)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**輸入參數**

| 參數名稱  | 類型           | 是否必須 | 描述                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | 是       | 輸入                |
| `dtype` | datatype_t     | 是       | 輸出tensor datatype |

**返回值**

`result<runtime_tensor>`

**代碼實例**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::cos(input, output_type).unwrap_or_throw();
```

### 6.2.7 圓形

**功能描述**

計算round值，目前支援輸入uint8/int8，輸出也為uint8/int8，注意輸入為定點且輸出為浮點時需要設置量化參數.

**介面定義**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`round`](#ops_8h_1a81db8ac4866004f75fb65db876262785)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**輸入參數**

| 參數名稱  | 類型           | 是否必須 | 描述                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | 是       | 輸入                |
| `dtype` | datatype_t     | 是       | 輸出tensor datatype |

**返回值**

`result<runtime_tensor>`

**代碼實例**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::round(input, output_type).unwrap_or_throw();
```

### 6.2.8 樓

**功能描述**

計算floor值，目前支援輸入uint8/int8，輸出也為uint8/int8，注意輸入為定點且輸出為浮點時需要設置量化參數.

**介面定義**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`floor`](#ops_8h_1a1079af8fe9fb6edbb2906d91fac12635)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**輸入參數**

| 參數名稱  | 類型           | 是否必須 | 描述                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | 是       | 輸入                |
| `dtype` | datatype_t     | 是       | 輸出tensor datatype |

**返回值**

`result<runtime_tensor>`

**代碼實例**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::floor(input, output_type).unwrap_or_throw();
```

### 6.2.9 西耳

**功能描述**

計算ceil值，目前支援輸入uint8/int8，輸出也為uint8/int8，注意輸入為定點且輸出為浮點時需要設置量化參數.

**介面定義**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`ceil`](#ops_8h_1ad3b78c97f1e5348a26de7e5ba2396fb7)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**輸入參數**

| 參數名稱  | 類型           | 是否必須 | 描述                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | 是       | 輸入                |
| `dtype` | datatype_t     | 是       | 輸出tensor datatype |

**返回值**

`result<runtime_tensor>`

**代碼實例**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::ceil(input, output_type).unwrap_or_throw();
```

### 6.2.10 腹肌

**功能描述**

計算abs值，目前支援輸入uint8/int8，輸出也為uint8/int8，注意輸入為定點且輸出為浮點時需要設置量化參數.

**介面定義**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`abs`](#ops_8h_1ad8290dc793bae0dc22b3baf9e0f80c14)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**輸入參數**

| 參數名稱  | 類型           | 是否必須 | 描述                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | 是       | 輸入                |
| `dtype` | datatype_t     | 是       | 輸出tensor datatype |

**返回值**

`result<runtime_tensor>`

**代碼實例**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::abs(input, output_type).unwrap_or_throw();
```

### 6.2.11 否定

**功能描述**

計算neg值，目前支援輸入uint8/int8，輸出也為uint8/int8，注意輸入為定點且輸出為浮點時需要設置量化參數.

**介面定義**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`neg`](#ops_8h_1aa1b7858802e1afce78db72163c5210d8)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**輸入參數**

| 參數名稱  | 類型           | 是否必須 | 描述                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | 是       | 輸入                |
| `dtype` | datatype_t     | 是       | 輸出tensor datatype |

**返回值**

`result<runtime_tensor>`

**代碼實例**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::neg(input, output_type).unwrap_or_throw();
```

### 6.2.12 量化

**功能描述**

輸入dt_bfloat16， dt_float32 數據，輸出dt_int8或 dt_uint8輸出

**介面定義**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`quantize`](#ops_8h_1ad8ad779083b5c08da520d2f1c2469c3a)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**輸入參數**

| 參數名稱  | 類型           | 是否必須 | 描述                                |
| --------- | -------------- | -------- | ----------------------------------- |
| `input` | runtime_tensor | 是       | 輸入， 類型必須為float32 或 bfloat16 |
| `dtype` | datatype_t     | 是       | 輸出tensor datatype                 |

**返回值**

`result<runtime_tensor>`

**代碼實例**

```cpp
auto quantized = F::quantize(input, dt_int8).unwrap_or_throw();
```

### 6.2.13 量化

**功能描述**

輸入 uint8 or int8 輸入，轉換到 float or bfloat數據. 注意，用戶必須提前為數據設置好正確的量化參數用於反量化.

**介面定義**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`dequantize`](#ops_8h_1ab91a262349baf393c91abad6f393de24)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**輸入參數**

| 參數名稱  | 類型           | 是否必須 | 描述                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | 是       | 輸入                |
| `dtype` | datatype_t     | 是       | 輸出tensor datatype |

**返回值**

`result<runtime_tensor>`

**代碼實例**

```cpp
input.quant_param({ 0, 1 });
auto dequantized = F::dequantize(input, output_type).unwrap_or_throw();
```

### 6.2.14 裁剪

**功能描述**

給定bboxs，從原始tensor中裁剪並resize輸出到新tensor中. 接受dt_bfloat16， dt_float32， dt_int8， dt_uint8類型輸出，輸出相同類型.

**介面定義**

`NNCASE_API inline result<runtime::runtime_tensor> crop(runtime::runtime_tensor &input, runtime::runtime_tensor &bbox, size_t out_h, size_t out_w, image_resize_mode_t resize_mode, bool align_corners, bool half_pixel_centers) noexcept`

**輸入參數**

| 參數名稱           | 類型                | 是否必須 | 描述                                                                                     |
| ------------------ | ------------------- | -------- | ---------------------------------------------------------------------------------------- |
| 輸入              | runtime_tensor      | 是       | 輸入資料，需要 [n，c，h，w] 格式排布 ，如果資料為uint8或int8 請保證數據量化參數的正確性       |
| bbox               | runtime_tensor      | 是       | 輸入bbox資料， 需要 [1，1，米，4] 格式排布， 內部資料為[y0，x0，y1，x1]， 類型為[浮點32，bfloat16] |
| out_h              | size_t              | 是       | 輸出數據height                                                                           |
| out_w              | size_t              | 是       | 輸入數據width                                                                            |
| resize_mode        | image_resize_mode_t | 是       | resize方法模式                                                                           |
| align_corners      | 布爾                | 是       | resize 是否 align_corners                                                    |
| half_pixel_centers | 布爾                | 是       | resize是否pixel中心對齊                                                                  |

**返回值**

`result<runtime_tensor>`

**代碼實例**

```cpp
auto bbox = get_rand_bbox(input_shape, roi_amount);
auto &&[out_h, out_w] = get_rand_out_hw();
auto output_opt = F::crop(input, bbox, out_h, out_w, resize_mode).unwrap_or_throw();
```

### 6.2.15 調整大小

**功能描述**

給定輸出高度 寬度，把輸入tensor resize到新尺寸. 接受dt_bfloat16， dt_float32， dt_int8， dt_uint8類型輸出，輸出相同類型.

**介面定義**

`NNCASE_API inline result<runtime::runtime_tensor> resize(runtime::runtime_tensor &input, size_t out_h, size_t out_w, image_resize_mode_t resize_mode, bool align_corners, bool half_pixel_centers) noexcept`

**輸入參數**

| 參數名稱           | 類型                | 是否必須 | 描述                                                                               |
| ------------------ | ------------------- | -------- | ---------------------------------------------------------------------------------- |
| 輸入              | runtime_tensor      | 是       | 輸入資料，需要 [n，c，h，w] 格式排布， 如果資料為uint8或int8 請保證資料量化參數的正確性 |
| out_h              | size_t              | 是       | 輸出數據height                                                                     |
| out_w              | size_t              | 是       | 輸入數據width                                                                      |
| resize_mode        | image_resize_mode_t | 是       | resize方法模式                                                                     |
| align_corners      | 布爾                | 是       | resize 是否 align_corners                                              |
| half_pixel_centers | 布爾                | 是       | resize是否pixel中心對齊                                                            |

**返回值**

`result<runtime_tensor>`

**代碼實例**

```cpp
auto &&[out_h, out_w] = get_rand_out_hw();
auto output_opt = F::resize(input, out_h, out_w, resize_mode, false, false).unwrap_or_throw();
```

### 6.2.16 墊

**功能描述**

在每個維度上padding數據，接受dt_bfloat16， dt_float32， dt_int8， dt_uint8類型輸出，輸出相同類型.

**介面定義**

`NNCASE_API inline result<runtime::runtime_tensor> pad(runtime::runtime_tensor &input, runtime_paddings_t &paddings, pad_mode_t pad_mode, float fill_v)`

**輸入參數**

| 參數名稱 | 類型               | 是否必須 | 描述                                                                                                                                       |
| -------- | ------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| 輸入    | runtime_tensor     | 是       | 輸入數據，如果數據為uint8或int8 請保證數據量化參數的正確性                                                                                  |
| 填充  | runtime_paddings_t | 是       | 每個維度的padding值， 注意順序為逆向. 比如padding值為 `[ {2,3}, {1,3} ]`表示在最後一維前面pad 2，後面pad 3. 倒數第二維前面pad 1， 後面pad 2 |
| pad_mode | pad_mode_t         | 是       | 目前暫時只支援const 模式                                                                                                                   |
| fill_v   | 浮              | 是       | 填充值                                                                                                                                     |

**返回值**

`result<runtime_tensor>`

**代碼實例**

```cpp
runtime_paddings_t paddings{ { 0, 0 }, { 0, 0 }, { 0, 0 }, { 1, 2 } };
auto output = F::pad(input, paddings, pad_constant, pad_value).unwrap_or_throw();
```
<!-- markdownlint-enable no-emphasis-as-header -->
# 7 量化白皮書

## 7.1 分類模型量化白皮書

| 分類模型     | cpu精度（Top-1） | 浮點精度（Top-1） | uint8精度（Top-1） | int8精度（Top-1） |
| ------------ | -------------- | --------------- | ---------------- | --------------- |
| 亞歷克斯內特      | 0.531          | 0.53            | 不適用              | 0.52            |
| 密集網 121 | 0.732          | 0.732           | 0.723            | 不適用             |
| 成立 v3 | 0.766          | 0.765           | 0.773            | 0.77            |
| 成立 v4 | 0.789          | 0.789           | 0.793            | 0.792           |
| 移動網路 v1 | 0.731          | 0.73            | 0.723            | 0.718           |
| 移動網路 v2 | 0.713          | 0.715           | 0.713            | 0.719           |
| resnet50 v2  | 0.747          | 0.74            | 0.748            | 0.749           |
| vgg 16       | 0.689          | 0.687           | 0.690            | 0.689           |

> 本表格主要為了對比量化的性能，cpu精度為完整ImageNet驗證集數據，浮點和量化精度為驗證集中1000類按照序號首先出現的圖片作為數據子集測試的結果。
>
> Alexnet和DenseNet的測試結果為舊數據，均為驗證集前1000張圖像作為數據子集的測試結果，N/A為當時的測試數據子集與CPU不同，因此不作為比較。
>
> 因為所選網路不一定來源於官方或者預處理等存在差異，可能與官方性能有所不同。

## 7.2 檢測模型量化白皮書

1. 約洛夫3

    | 可可皮                                                      | 官方結果 | CPU浮點精度 | gnne浮點精度 | uint8精度 | int8精度 |
    | ------------------------------------------------------------ | -------- | ----------- | ------------ | --------- | -------- |
    | 平均精度 （AP） @ [IoU = 0.50：0.95\|面積 = 全部 \|最大集數 = 100] | 0.314    | 0.307       | 0.306        | 0.295     | 0.288    |
    | 平均精度 （AP） @ [IoU = 0.50\|面積 = 全部 \|最大集數 = 100] | 0.559    | 0.555       | 0.554        | 0.555     | 0.554    |
    | 平均精度 （AP） @ [IoU = 0.75\|面積 = 全部 \|最大集數 = 100] | 0.318    | 0.308       | 0.307        | 0.287     | 0.275    |
    | 平均精度 （AP） @ [IoU = 0.50：0.95\|面積 = 小 \|最大集數 = 100] | 0.142    | 0.150       | 0.149        | 0.147     | 0.144    |
    | 平均精度 （AP） @ [IoU= 0.50：0.95\|面積 = 中 \|最大集數 = 100] | 0.341    | 0.332       | 0.332        | 0.322     | 0.316    |
    | 平均精度 （AP） @ [IoU = 0.50：0.95\|面積 = 大 \|最大集數 = 100] | 0.464    | 0.437       | 0.437        | 0.414     | 0.404    |
    | 平均召回率 （AR） @ [IoU= 0.50：0.95\|面積 = 全部 \|最大集數 = 1] | 0.278    | 0.270       | 0.271        | 0.262     | 0.256    |
    | 平均召回率 （AR） @ [IoU= 0.50：0.95\|面積 = 全部 \|最大集數 = 10] | 0.419    | 0.412       | 0.412        | 0.399     | 0.392    |
    | 平均召回率 （AR） @ [IoU = 0.50：0.95\|面積 = 全部 \|最大集數 = 100] | 0.442    | 0.433       | 0.433        | 0.421     | 0.414    |
    | 平均召回率 （AR） @ [IoU = 0.50：0.95\|面積 = 小 \|最大集數 = 100] | 0.239    | 0.251       | 0.251        | 0.248     | 0.246    |
    | 平均召回率 （AR） @ [IoU= 0.50：0.95\|面積 = 中 \|最大集數 = 100] | 0.482    | 0.462       | 0.463        | 0.451     | 0.443    |
    | 平均召回率 （AR） @ [IoU = 0.50：0.95\|面積 = 大 \|最大集數 = 100] | 0.611    | 0.586       | 0.585        | 0.559     | 0.550    |

2. ssd-mobilenetv1

    | 可可皮                                                                    | 官方結果 | CPU浮點精度 | gnne浮點精度 | uint8精度 | int8精度 |
    | -------------------------------------------------------------------------- | -------- | ----------- | ------------ | --------- | -------- |
    | 平均精度 （AP）@ [IoU = 0.50：0.95\|面積 = 全部 \|最大集數 = 100]   | 0.184    | 0.184       | 0.184        | 0.183     | 0.183    |
    | 平均精度 （AP）@ [IoU = 0.50\|面積 = 全部 \|最大集數 = 100]        | 0.306    | 0.307       | 0.306        | 0.305     | 0.306    |
    | 平均精度 （AP）@ [IoU = 0.75\|面積 = 全部 \|最大集數 = 100]        | 0.191    | 0.192       | 0.190        | 0.189     | 0.190    |
    | 平均精度 （AP） @ [IoU = 0.50：0.95\|面積 = 小 \|最大集數 = 100] | 0.017    | 0.017       | 0.017        | 0.017     | 0.017    |
    | 平均精度 （AP） @ [IoU= 0.50：0.95\|面積 = 中 \|最大集數 = 100] | 0.157    | 0.157       | 0.157        | 0.156     | 0.155    |
    | 平均精度 （AP） @ [IoU = 0.50：0.95\|面積 = 大 \|最大集數 = 100] | 0.371    | 0.372       | 0.371        | 0.370     | 0.369    |
    | 平均召回率@ [IoU= 0.50：0.95\|面積 = 全部 \|最大集數 = 1]         | 0.180    | 0.180       | 0.180        | 0.181     | 0.181    |
    | 平均召回率@ [IoU= 0.50：0.95\|面積 = 全部 \|最大集數 = 10]        | 0.242    | 0.242       | 0.242        | 0.243     | 0.243    |
    | 平均召回率@ [IoU = 0.50：0.95\|面積 = 全部 \|最大集數 = 100]      | 0.242    | 0.242       | 0.242        | 0.243     | 0.243    |
    | 平均召回率@ [IoU = 0.50：0.95\|面積 = 小 \|最大集數 = 100]    | 0.026    | 0.026       | 0.026        | 0.026     | 0.026    |
    | 平均召回率@ [IoU= 0.50：0.95\|面積 = 中 \|最大集數 = 100]    | 0.206    | 0.206       | 0.206        | 0.206     | 0.205    |
    | 平均召回率@ [IoU = 0.50：0.95\|面積 = 大 \|最大集數 = 100]    | 0.489    | 0.491       | 0.490        | 0.490     | 0.491    |

3. 約洛夫5s

    | 可可皮                                                                    | 官方結果 | CPU浮點精度 | gnne浮點精度 | uint8精度 | int8精度 |
    | -------------------------------------------------------------------------- | -------- | ----------- | ------------ | --------- | -------- |
    | 平均精度 （AP）@ [IoU = 0.50：0.95\|面積 = 全部 \|最大集數 = 100]   | 0.367    | 0.365       | 0.335        | 0.334     | 0.335    |
    | 平均精度 （AP）@ [IoU = 0.50\|面積 = 全部 \|最大集數 = 100]        | 0.555    | 0.552       | 0.518        | 0.518     | 0.518    |
    | 平均精度 （AP）@ [IoU = 0.75\|面積 = 全部 \|最大集數 = 100]        | 0.398    | 0.395       | 0.364        | 0.363     | 0.362    |
    | 平均精度 （AP） @ [IoU = 0.50：0.95\|面積 = 小 \|最大集數 = 100] | 0.223    | 0.220       | 0.199        | 0.199     | 0.197    |
    | 平均精度 （AP） @ [IoU= 0.50：0.95\|面積 = 中 \|最大集數 = 100] | 0.419    | 0.418       | 0.387        | 0.386     | 0.386    |
    | 平均精度 （AP） @ [IoU = 0.50：0.95\|面積 = 大 \|最大集數 = 100] | 0.463    | 0.459       | 0.423        | 0.422     | 0.423    |
    | 平均召回率@ [IoU= 0.50：0.95\|面積 = 全部 \|最大集數 = 1]         | 0.306    | 0.306       | 0.288        | 0.287     | 0.287    |
    | 平均召回率@ [IoU= 0.50：0.95\|面積 = 全部 \|最大集數 = 10]        | 0.518    | 0.518       | 0.487        | 0.486     | 0.487    |
    | 平均召回率@ [IoU = 0.50：0.95\|面積 = 全部 \|最大集數 = 100]      | 0.576    | 0.576       | 0.540        | 0.539     | 0.540    |
    | 平均召回率@ [IoU = 0.50：0.95\|面積 = 小 \|最大集數 = 100]    | 0.391    | 0.399       | 0.350        | 0.350     | 0.347    |
    | 平均召回率@ [IoU= 0.50：0.95\|面積 = 中 \|最大集數 = 100]    | 0.641    | 0.640       | 0.606        | 0.605     | 0.607    |
    | 平均召回率@ [IoU = 0.50：0.95\|面積 = 大 \|最大集數 = 100]    | 0.716    | 0.710       | 0.680        | 0.683     | 0.685    |

# 8 常見問題

1.安裝車輪時報錯：「xxx.whl 不是此平台上支持的車輪。**

問：安裝 nncase wheel包， 出現ERROR： nncase-1.0.0.20210830-cp37-cp37m-manylinux_2_24_x86_64.whl 在此平臺上不支持的車輪。

A： 升級 pip >= 20.3

```shell
sudo pip3 install --upgrade pip
```

2.CRB運行App推理程式時， 報錯“std：：bad_alloc”**

Q： CRB上運行App推理程式， 拋出“std：：bad_alloc”異常

```shell
$ ./cpp.sh
case ./yolov3_bfloat16 build at Sep 16 2021 18:12:03
terminate called after throwing an instance of 'std::bad_alloc'
  what():  std::bad_alloc
```

A： std：：bad_alloc異常通常是因為記憶體分配失敗導致的， 可做如下排查.

- 檢查生成的kmodel是否超過當前系統可用記憶體（如yolov3 bfloat16 kmodel大小為121MB， 當前linux可用記憶體只有70MB， 則會拋出該異常）.  若超過， 可嘗試使用訓練後量化來減小kmodel大小.
- 檢查App是否存在記憶體洩露

3.**運行App推理程序時[..t_runtime_tensor.cpp：310 （建立）] data.size_bytes（） == size = false （bool）**

Q： simulator運行App推理程式， 拋出“[..t_runtime_tensor.cpp：310 （建立）] data.size_bytes（） == size = false （bool）”異常

A： 檢查設定的輸入tensor資訊， 重點是輸入shape和每個元素佔用的位元組數（fp32/uint8）

**翻譯免責聲明**  
為方便客戶，Canaan 使用 AI 翻譯程式將文字翻譯為多種語言，它可能包含錯誤。 我們不保證提供的譯文的準確性、可靠性或時效性。 對於因依賴已翻譯信息的準確性或可靠性而造成的任何損失或損害，Canaan 概不負責。 如果不同語言翻譯之間存在內容差異，以簡體中文版本為準。

如果您要報告翻譯錯誤或不準確的問題，歡迎通過郵件與我們聯繫。
