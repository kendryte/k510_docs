![Kanaan-Cover.png](http://s2.loli.net/2022/03/30/7UG1IxrOXTo2QKw.png)

**<font face="黑体" size="6" style="float:right">K510 nncase Entwicklerhandbuch</font>**

<font face="黑体"  size=3>Dokumentversion: V1.0.1</font>

<font face="黑体"  size=3>Veröffentlicht: 2022-05-10</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Verzichtserklärung**</font>
Die Produkte, Dienstleistungen oder Funktionen, die Sie erwerben, unterliegen den kommerziellen Verträgen und Bedingungen von Beijing Canaan Jiesi Information Technology Co., Ltd. ("das Unternehmen", dasselbe im Folgenden), und alle oder ein Teil der in diesem Dokument beschriebenen Produkte, Dienstleistungen oder Funktionen fallen möglicherweise nicht in den Rahmen Ihres Kaufs oder Ihrer Nutzung. Sofern im Vertrag nicht anders vereinbart, lehnt das Unternehmen alle ausdrücklichen oder stillschweigenden Zusicherungen oder Gewährleistungen hinsichtlich der Genauigkeit, Zuverlässigkeit, Vollständigkeit, des Marketings, des spezifischen Zwecks und der Nichtverletzung von Zusicherungen, Informationen oder Inhalten dieses Dokuments ab. Sofern nicht anders vereinbart, wird dieses Dokument nur als Leitfaden für die Verwendung zur Verfügung gestellt.
Aufgrund von Produktversions-Upgrades oder anderen Gründen kann der Inhalt dieses Dokuments von Zeit zu Zeit ohne vorherige Ankündigung aktualisiert oder geändert werden.

**<font face="黑体"  size=3>Markenhinweise</font>**

"", "Canaan"-Symbol, Canaan und andere Marken von Canaan und andere Marken von Canaan <img src="http://s2.loli.net/2022/03/30/xN21jbhnwSFyGRD.png" style="zoom:33%;" />sind Marken von Beijing Canaan Jiesi Information Technology Co., Ltd. Alle anderen Marken oder eingetragenen Warenzeichen, die in diesem Dokument erwähnt werden können, sind Eigentum ihrer jeweiligen Inhaber.

**<font face="黑体"  size=3>Copyright ©2022 Peking Canaan Jiesi Information Technology Co., Ltd</font>**
Dieses Dokument gilt nur für die Entwicklung und das Design der K510-Plattform, ohne die schriftliche Genehmigung des Unternehmens darf keine Einheit oder Einzelperson einen Teil oder den gesamten Inhalt dieses Dokuments in irgendeiner Form verbreiten.

**<font face="黑体"  size=3>Peking Canaan Jiesi Informationstechnologie Co., Ltd</font>**
URL: canaan-creative.com
Geschäftliche Anfragen: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# Vorwort
**<font face="黑体"  size=5>Zweck des Dokuments</font>**
Dieses Dokument ist ein Beschreibungsdokument für die Verwendung des nncase/K510-Compilers, das Benutzern die Installation von nncase, den Aufruf der Compiler-APIs zum Kompilieren neuronaler Netzwerkmodelle und Laufzeit-APIs zum Schreiben von KI-Inferenzprogrammen

**<font face="黑体"  size=5>Reader-Objekte</font>**

Die wichtigsten Personen, für die sich dieses Dokument (dieser Leitfaden) richtet:

- Softwareentwickler
- Mitarbeiter des technischen Supports

**<font face="黑体"  size=5>Begriffe und Akronyme</font>**

| Ausdruck | Erläuterung/vollständiger Name                              |
| ---- | -------------------------------------- |
| PTQ  | Post-Trainings-Quantisierung, Post-Trainings-Quantisierung |
|| Mittlerer quadratischer Fehler, mittlerer quadratischer Fehler            |
|      |                                        |

**<font face="黑体"  size=5>Revisionshistorie</font>**
 <font face="宋体"  size=2>In der Revisionshistorie wird eine Beschreibung jeder Dokumentaktualisierung gesammelt. Die neueste Version des Dokuments enthält Updates für alle vorherigen Versionen. </font>

| Die Versionsnummer   | Geändert von     | Datum der Überarbeitung | Revisionshinweise |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.1 | Werbung | 2022-05-10 | nncase_v1.6.1 |
| V1.0.0 | Zhang Yang/Zhang Jizhao/Yang Haoqi | 2022-05-06 | nncase_v1.6.0 |
| V0.9.0 | Werbung | 2022-04-01 | nncase_v1.5.0 |
| V0.8.0 | Zhang Yang/Zhang Jizhao | 2022-03-03 | nncase_v1.4.0 |
| V0.7.0 | Werbung | 2022-01-28 | nncase_v1.3.0 |
| V0.6.0 | Werbung | 2021-12-31 | nncase_v1.2.0 |
| V0.5.0 | Werbung | 2021-12-03 | nncase_v1.1.0 |
| V0.4.0 | Zhang Yang/Haoqi Yang/Zheng Qihang | 2021-10-29 | nncase_v1.0.0 |
| V0.3.0 | Zhang Yang / Yang Haoqi | 2021-09-28 | nncase_v1.0.0_rc1 |
| V0.2.0 | Zhang Yang / Yang Haoqi | 2021-09-02 | nncase_v1.0.0_beta2 |
| V0.1.0 | Zhang Yang / Yang Haoqi | 2021-08-31 | nncase_v1.0.0_beta1 |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Inhalt</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Einführung in die Entwicklungsumgebung

## 1.1 Betriebssystem

- Ubuntu 18.04 / 20.04

## 1.2 Software-Umgebung

Die Anforderungen an die Softwareumgebung sind in der folgenden Tabelle aufgeführt:

| Seriennummer | Software-Ressourcen        | illustrieren                        |
| ---- | --------------- | --------------------------- |
| 1    | Python          | Python 3.6/3.7/3.8/3.9/3.10 |
| 2    | PIP3            | PIP3 Version > = 20.3            |
| 3    | onnx            | Die onnx-Version ist 1.9.0             |
| 4    | onnx-simplify | Die onnx-simplifier Version ist 0.3.6  |
| 5    | onnxoptimizer   | Die onnxoptimizer-Version ist 0.2.6    |

## 1.3 Hardware-Umgebung

Die Anforderungen an die Hardwareumgebung sind in der folgenden Tabelle aufgeführt:

| Seriennummer | Hardware-Ressourcen     | illustrieren |
| ---- | ------------ | ---- |
| 1    | K510 CRB     |      |
| 2    | SD-Karte und Kartenleser |      |

# 2 Einführung in NNCASE

## 2.1 Was ist nncase

nncase ist ein neuronaler Netzwerk-Compiler, der für KI-Beschleuniger entwickelt wurde und derzeit Ziele wie CPU / K210 / K510 unterstützt

Von nncase bereitgestellte Funktionen

- Unterstützt mehrere Eingangs- und mehrere Ausgabenetzwerke, unterstützt die Struktur mit mehreren Zweigen
- Statische Speicherzuweisung, kein Heap-Speicher erforderlich
- Zusammenführung und Optimierung von Betreibern
- Unterstützt float- und uint8/int8-Quantisierungsinferenz
- Unterstützt die Quantisierung nach dem Training unter Verwendung von Gleitkommamodellen und Quantisierungskalibrierungssätzen
- Flaches Modell ohne Kopierunterstützung

Von nncase unterstütztes neuronales Netzwerk-Framework

- tflite
- onnx
- Caffe

## 2.2 Produktvorteile

- **Einfache End-to-End-Bereitstellung**

  Reduzieren Sie die Anzahl der Interaktionen mit Benutzern. Die Bereitstellung auf KPUs kann durch die Verwendung und Bereitstellung derselben Tools und Prozesse für die CPU- und GPU-Modelle erfolgen. Es ist nicht erforderlich, komplexe Parameter festzulegen, die Nutzungsschwelle zu senken und den Iterationszyklus von KI-Algorithmen zu beschleunigen.
- **Nutzen Sie das bestehende KI-Ökosystem voll aus**

  Verbunden mit einem in der Branche weit verbreiteten Rahmen. Auf der einen Seite kann es seine Sichtbarkeit verbessern und die Dividenden einer reifen Ökologie genießen. Auf der anderen Seite können die Entwicklungskosten kleiner und mittlerer Entwickler reduziert und die ausgereiften Modelle und Algorithmen in der Industrie direkt eingesetzt werden.
- **Holen Sie das Beste aus Ihrer Hardware heraus**

  Der Vorteil von NPU ist, dass die Leistung höher ist als die von CPU und GPU, und der DL-Compiler muss in der Lage sein, die Leistung der Hardware voll auszunutzen. Der Compiler muss auch die Leistung für die neue Modellstruktur adaptiv optimieren, daher muss zusätzlich zur manuellen Optimierung eine neue automatische Optimierungstechnik erforscht werden.
- **Skalierbarkeit und Wartbarkeit**

  Möglichkeit zur Unterstützung von KI-Modellbereitstellungen für K210, K510 und zukünftige Chips. Eine gewisse Skalierbarkeit muss auf Architekturebene bereitgestellt werden. Das Hinzufügen eines neuen Ziels ist kostengünstiger und ermöglicht es Ihnen, so viele Module wie möglich wiederzuverwenden. Beschleunigen Sie die Entwicklung neuer Produkte, um die Technologieakkumulation von DL Compiler zu erreichen.

## 2.3 nncase-Architektur

<img src="https://i.loli.net/2021/08/18/IQR12SOJdzxTUZH.png" alt="nncase_arch.png" style="zoom:67%;" />

Der nnncase-Software-Stack besteht derzeit aus zwei Teilen: Compiler und Runtime.

**Compiler:** Wird verwendet, um neuronale Netzwerkmodelle auf einem PC zu kompilieren und schließlich eine kmodel-Datei zu generieren. Es umfasst hauptsächlich Importer, IR, Evaluator, Quantize, Transform Optimization, Tiling, Partition, Schedule, Codegen und andere Module.

- Importer: Importiert Modelle aus anderen neuronalen Netzwerk-Frameworks in nncase
- IR: Mittlere Darstellung, unterteilt in importimportierte Neutral-IR (geräteunabhängig) und Nutral-IR, die durch Absenken der Konvertierungs-Ziel-IR (geräteabhängig) erzeugt wird
- Evaluator: Evaluator bietet interpretative Ausführung von IR und wird häufig in Szenarien wie Constant Folding / PTQ Calibration verwendet
- Transformation: Für IR-Transformation und Graph-Traversal-Optimierung usw.
- Quantisieren: Quantisieren Sie nach dem Training, fügen Sie dem zu quantifizierenden Tensor Quantisierungsmarker hinzu, rufen Sie den Evaluator für die Interpretationsausführung gemäß dem Eingabekorrektursatz auf, sammeln Sie den Tensordatenbereich, fügen Sie Quantisierungs- / Dequantisierungsknoten ein und optimieren Sie schließlich, um unnötige Quantisierungs- / Dequantisierungsknoten usw. zu eliminieren
- Kacheln: Begrenzt durch die geringere Speicherkapazität der NPU, müssen große Teile der Berechnung aufgeteilt werden. Darüber hinaus wirkt sich die Auswahl des Tilling-Parameters bei einer großen Datenmultiplexmenge in der Berechnung auf die Latenz und Bandbreite aus.
- Partition: Teilen Sie den Graphen durch ModuleType, jeder Subgraph nach der Aufteilung entspricht RuntimeModule, verschiedene Typen von RuntimeModule entsprechen verschiedenen Geräten (CPU / K510)
- Zeitplan: Generiert eine Berechnungsreihenfolge und weist Puffer basierend auf den Datenabhängigkeiten im optimierten Diagramm zu
- Codegen: Rufen Sie das Codegen auf, das ModuleType für jeden Subgraphen entspricht, um RuntimeModule zu generieren.

**Laufzeit**: Integriert in die Benutzer-App, bietet es Funktionen wie Laden von kmodel / Einstellen von Eingabedaten, KPU-Ausführung und Abrufen von Ausgabedaten

# 3 Installieren Sie nncase

Der Compiler-Teil der nncase-Toolchain enthält den nncase- und K510-Compiler, die beide das entsprechende Radpaket installieren müssen.

- Das nncase wheel-Paket wurde[auf nncase github veröffentlicht und](https://github.com/kendryte/nncase/releases/tag/v1.6.0)unterstützt Python 3.6 / 3.7 / 3.8 / 3.9 / 3.10, Benutzer können die entsprechende Version zum Herunterladen entsprechend dem Betriebssystem und Python auswählen
- Das K510-Compiler-Radpaket befindet sich im x86_64-Verzeichnis des nncase-SDK, ist nicht von der Python-Version abhängig und kann direkt installiert werden

Wenn Sie keine Ubuntu-Umgebung haben, können Sie[nncase docker](https://github.com/kendryte/nncase/blob/master/docs/build.md#docker)(Ubuntu 20.04 + Python 3.8) verwenden.

```shell
cd /path/to/nncase_sdk
docker pull registry.cn-hangzhou.aliyuncs.com/kendryte/nncase:latest
docker run -it --rm -v `pwd`:/mnt -w /mnt registry.cn-hangzhou.aliyuncs.com/kendryte/nncase:latest /bin/bash -c "/bin/bash"
```

Das Folgende nimmt Ubuntu 20.04 + Python 3.8 Installation von nncase als Beispiel

```shell
wget -P x86_64 https://github.com/kendryte/nncase/releases/download/v1.6.0/nncase-1.6.0.20220505-cp38-cp38-manylinux_2_24_x86_64.whl
pip3 install x86_64/*.whl
```
<!-- markdownlint-disable no-emphasis-as-header -->
# 4 Kompilierungs-/Inferenzmodell

nncase bietet**Python-API**zum Kompilieren/Ableiten von Deep-Learning-Modellen auf einem PC

## 4.1 Unterstützte Betreiber

### 4.1.1 TFLITE-Operator

| Operator                | Wird unterstützt |
| ----------------------- | ------------ |
| ABS                     | ✅            |
| HINZUFÜGEN                     | ✅            |
| ARG_MAX                 | ✅            |
| ARG_MIN                 | ✅            |
| AVERAGE_POOL_2D         | ✅            |
| BATCH_MATMUL            | ✅            |
| WERFEN                    | ✅            |
| CEIL                    | ✅            |
| VERKETTUNG           | ✅            |
| CONV_2D                 | ✅            |
| KÖRPER                     | ✅            |
| GEWOHNHEIT                  | ✅            |
| DEPTHWISE_CONV_2D       | ✅            |
| DIV                     | ✅            |
| GLEICH                   | ✅            |
| EXP                     | ✅            |
| EXPAND_DIMS             | ✅            |
| BODEN                   | ✅            |
| FLOOR_DIV               | ✅            |
| FLOOR_MOD               | ✅            |
| FULLY_CONNECTED         | ✅            |
| GRÖßER                 | ✅            |
| GREATER_EQUAL           | ✅            |
| L2_NORMALIZATION        | ✅            |
| LEAKY_RELU              | ✅            |
| WENIGER                    | ✅            |
| LESS_EQUAL              | ✅            |
| LOG                     | ✅            |
| LOGISTISCH                | ✅            |
| MAX_POOL_2D             | ✅            |
| MAXIMUM                 | ✅            |
| BEDEUTEN                    | ✅            |
| MINIMUM                 | ✅            |
| Ich                     | ✅            |
| NEG                     | ✅            |
| NOT_EQUAL               | ✅            |
| UNTERLAGE                     | ✅            |
| PADV2                   | ✅            |
| MIRROR_PAD              | ✅            |
| PACKEN                    | ✅            |
| KRIEGSGEFANGENER                     | ✅            |
| REDUCE_MAX              | ✅            |
| REDUCE_MIN              | ✅            |
| REDUCE_PROD             | ✅            |
| RELU                    | ✅            |
| PRELU                   | ✅            |
| RELU6                   | ✅            |
| UMFORMEN                 | ✅            |
| RESIZE_BILINEAR         | ✅            |
| RESIZE_NEAREST_NEIGHBOR | ✅            |
| RUND                   | ✅            |
| RSQRT                   | ✅            |
| FORM                   | ✅            |
| OHNE                     | ✅            |
| SCHEIBE                   | ✅            |
| SOFTMAX                 | ✅            |
| SPACE_TO_BATCH_ND       | ✅            |
| DRÜCKEN                 | ✅            |
| BATCH_TO_SPACE_ND       | ✅            |
| STRIDED_SLICE           | ✅            |
| SQRT                    | ✅            |
| QUADRAT                  | ✅            |
| SUB                     | ✅            |
| SUMME                     | ✅            |
| FISCHIG                    | ✅            |
| FLIESE                    | ✅            |
| TRANSPONIEREN               | ✅            |
| TRANSPOSE_CONV          | ✅            |
| QUANTISIEREN                | ✅            |
| FAKE_QUANT              | ✅            |
| DEQUANTISIEREN              | ✅            |
| VERSAMMELN                  | ✅            |
| GATHER_ND               | ✅            |
| ONE_HOT                 | ✅            |
| SQUARED_DIFFERENCE      | ✅            |
| LOG_SOFTMAX             | ✅            |
| TRENNEN                   | ✅            |
| HARD_SWISH              | ✅            |

### 4.1.2 onnx-Operator

| Operator              | Wird unterstützt |
| --------------------- | ------------ |
| Abs                   | ✅            |
| Acos                  | ✅            |
| Acosch                 | ✅            |
| Und                   | ✅            |
| ArgMax                | ✅            |
| ArgMin                | ✅            |
| Salzig                  | ✅            |
| Asinh |                 | ✅            |
| Hinzufügen                   | ✅            |
| Durchschnittlicher Pool           | ✅            |
| BatchNormalisierung    | ✅            |
| Werfen                  | ✅            |
| Ceil |                  | ✅            |
| An                  | ✅            |
| Scheren                  | ✅            |
| Concat                | ✅            |
| Konstante              | ✅            |
| KonstanteOfShape       | ✅            |
| Conv                  | ✅            |
| ConvTranspose         | ✅            |
| Körper                   | ✅            |
| Totschläger                  | ✅            |
| CumSum                | ✅            |
| DepthToSpace          | ✅            |
| DequantizeLinear      | ✅            |
| Div                   | ✅            |
| Dropout               | ✅            |
| Leben                   | ✅            |
| Exp                   | ✅            |
| Erweitern                | ✅            |
| Gleich                 | ✅            |
| Abflachen               | ✅            |
| Boden                 | ✅            |
| Versammeln                | ✅            |
| Sammeln Sie ND              | ✅            |
| Gemm |                  | ✅            |
| GlobalAveragePool     | ✅            |
| GlobalMaxPool         | ✅            |
| Größer               | ✅            |
| GreaterOrEqual        | ✅            |
| Hardmax               | ✅            |
| HardSigmoid           | ✅            |
| HardSwish             | ✅            |
| Identität              | ✅            |
| InstanzNormalisierung | ✅            |
| LpNormalisierung       | ✅            |
| LeakyRelu             | ✅            |
| Weniger                  | ✅            |
| LessOrEqual           | ✅            |
| Log                   | ✅            |
| LogSoftmax            | ✅            |
| LRN                   | ✅            |
| LSTM                  | ✅            |
| MatMul                | ✅            |
| MaxPool               | ✅            |
| Max                   | ✅            |
| Min                   | ✅            |
| Ich                   | ✅            |
| Neg                   | ✅            |
| Nicht                   | ✅            |
| OneHot                | ✅            |
| Unterlage                   | ✅            |
| Kriegsgefangener                   | ✅            |
| PRelu                 | ✅            |
| QuantizeLinear        | ✅            |
| RandomNormal          | ✅            |
| RandomNormalLike      | ✅            |
| RandomUniform         | ✅            |
| RandomUniformLike     | ✅            |
| ReduceL1              | ✅            |
| ReduceL2              | ✅            |
| ReduceLogSum          | ✅            |
| ReduceLogSumExp       | ✅            |
| ReduceMax             | ✅            |
| ReduceMean            | ✅            |
| ReduceMin             | ✅            |
| ReduceProd            | ✅            |
| ReduceSum             | ✅            |
| ReduceSumSquare       | ✅            |
| Relu                  | ✅            |
| Umformen               | ✅            |
| Größe                | ✅            |
| ReverseSequence       | ✅            |
| RoiAlign              | ✅            |
| Rund                 | ✅            |
| Dorf                  | ✅            |
| Form                 | ✅            |
| Zeichen                  | ✅            |
| Ohne                   | ✅            |
| Geburt                  | ✅            |
| S-förmig               | ✅            |
| Größe                  | ✅            |
| Scheibe                 | ✅            |
| Softmax               | ✅            |
| Softplus              | ✅            |
| Softsign              | ✅            |
| SpaceToDepth          | ✅            |
| Trennen                 | ✅            |
| Sqrt                  | ✅            |
| Drücken               | ✅            |
| Sub                   | ✅            |
| Summe                   | ✅            |
| Fischig                  | ✅            |
| Fliese                  | ✅            |
| TopK                  | ✅            |
| Transponieren             | ✅            |
| Trilu                 | ✅            |
| Upsampling              | ✅            |
| Ungequetscht             | ✅            |
| Wo                 | ✅            |

### 4.1.3 Caffe-Operator

| Operator              | Wird unterstützt |
| --------------------- | ------------ |
| Eingabe                 | ✅            |
| Concat                | ✅            |
| Faltung           | ✅            |
| Eltwise               | ✅            |
| Inzahlungnahme               | ✅            |
| relu                  | ✅            |
| Umformen               | ✅            |
| Scheibe                 | ✅            |
| Softmax               | ✅            |
| Trennen                 | ✅            |
| ContinuationIndicator | ✅            |
| Vereinigend               | ✅            |
| BatchNorm             | ✅            |
| Maßstab                 | ✅            |
| Rückwärts               | ✅            |
| LSTM                  | ✅            |
| InnerProdukt          | ✅            |

## 4.2 Modell-APIs kompilieren

Derzeit unterstützt die API des Kompilierungsmodells Deep-Learning-Frameworks wie tflite/onnx/caffe.

### 4.2.1 CompileOptions

**Funktionsbeschreibung**

CompileOptions-Klasse zum Konfigurieren von nncase-Kompilierungsoptionen

**Klassendefinition**

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

Jede Eigenschaft wird im Folgenden beschrieben

| Name der Immobilie         | Art   | Ja oder nein | Beschreibung                                                         |
| ---------------- | ------ | -------- | ------------------------------------------------------------ |
| Ziel           | Schnur | sein       | Geben Sie das Kompilierungsziel an, z. B. 'k210', 'k510'                               |
| quant_type       | Schnur | nicht       | Geben Sie den Datenquantisierungstyp an, z. B. 'uint8', 'int8'                          |
| w_quant_type     | Schnur | nicht       | Geben Sie den Gewichtsquantisierungstyp an, z. B. 'uint8', 'int8', standardmäßig 'uint8'           |
| use_mse_quant_w  | Bool   | nicht       | Gibt an, ob der MSE-Algorithmus (Mean-Square Error) verwendet werden soll, um die Quantisierungsparameter bei der Quantifizierung von Gewichtungen zu optimieren. |
| split_w_to_act   | Bool   | nicht       | Gibt an, ob Teilgewichtungsdaten in aktive Daten überführt werden sollen.                       |
| Vorverarbeiten       | Bool   | nicht       | Unabhängig davon, ob die Vorverarbeitung aktiviert ist oder nicht, ist der Standardwert False                                  |
| swapRB           | Bool   | nicht       | Unabhängig davon, ob RGB-Eingangsdaten zwischen den roten und blauen Kanälen (RGB--> BGR oder BGR->RGB) ausgetauscht werden sollen, ist der Standardwert False |
| bedeuten             | Liste   | nicht       | Die Vorverarbeitung normalisiert den Parametermittelwert, der standardmäßig auf[0, 0, 0]                        |
| std              | Liste   | nicht       | Die Vorverarbeitung normalisiert die Parametervarianz, die standardmäßig auf[1, 1, 1]                        |
| input_range      | Liste   | nicht       | Der Bereich der Gleitkommazahlen nach der Dequantisierung der Eingabedaten, der standardmäßig auf[0，1]               |
| output_range     | Liste   | nicht       | Der Bereich der Gleitkommazahlen vor der Ausgabe der Festkommadaten, der standardmäßig leer ist                     |
| input_shape      | Liste   | nicht       | Geben Sie die Form der Eingabedaten an, das Layout der input_shape muss mit dem Eingabelayout konsistent sein, und die input_shape der Eingabedaten ist nicht konsistent mit der Eingabeform des Modells, und der Bitbox-Vorgang (Größenänderung/Pad usw.) wird ausgeführt. |
| letterbox_value  | schweben  | nicht       | Gibt den Auffüllungswert der vorverarbeiteten Abrufbox an.                                  |
| input_type       | Schnur | nicht       | Gibt den Typ der Eingabedaten an, standardmäßig 'float32'                          |
| output_type      | Schnur | nicht       | Gibt den Typ der Ausgabedaten an, z. B. 'float32', 'uint8' (nur für angegebene Quantisierung), standardmäßig 'float32' |
| input_layout     | Schnur | nicht       | Geben Sie das Layout der Eingabedaten an, z. B. "NCHW", "NHWC". Wenn sich das Layout der Eingabedaten vom Modell selbst unterscheidet, wird nncase zur Konvertierung transponiert |
| output_layout    | Schnur | nicht       | Geben Sie die Ausgabedaten für das Layout an, z. B. 'NCHW', 'NHWC'. Wenn sich das Layout der Ausgabedaten vom Modell selbst unterscheidet, fügt nncase transpose für die Konvertierung ein |
| model_layout     | Schnur | nicht       | Geben Sie das Layout des Modells an, das standardmäßig leer ist und angibt, wann das tflite-Modelllayout 'NCHW' und die Onnx- und Caffe-Modelle 'NHWC' sind |
| is_fpga          | Bool   | nicht       | Gibt an, ob kmodel für FPGAs verwendet wird, wobei standardmäßig False                          |
| dump_ir          | Bool   | nicht       | Gibt an, ob Dump-IR standardmäßig False ist.                                 |
| dump_asm         | Bool   | nicht       | Gibt an, ob die Dump-ASM-Assemblydatei, die standardmäßig False ist.                        |
| dump_quant_error | Bool   | nicht       | Gibt an, ob dump den Modellfehler vorher und nachher quantifiziert.                               |
| dump_dir         | Schnur | nicht       | Nachdem Sie zuvor die Befehlszeilenoptionen dump_ir und andere Optionen angegeben haben, geben Sie hier das Verzeichnis des Speicherabbilds an, das standardmäßig eine leere Zeichenfolge verwendet  |
| benchmark_only   | Bool   | nicht       | Gibt an, ob kmodel nur für den Benchmark verwendet wird, der standardmäßig auf False festgelegt ist.                   |

> 1. Der Eingabebereich ist der Bereich der Gleitkommazahlen, dh wenn der Eingabedatentyp uint8 ist, ist der Eingabebereich der Bereich nach der Dequantisierung zum Gleitkommawert (kann nicht 0 ~ 1 sein), der frei angegeben werden kann.
> 2. input_shape müssen gemäß dem input_layout spezifiziert werden[1，224，224，3], z. B. wenn der input_layout NCHW ist, muss der input_shape wie folgt angegeben werden[1,3,224,224]: input_layout NHWC ist, muss das input_shape wie folgt angegeben werden[1,224,224,3]:
> 3. Mittelwert und STD sind Parameter zur Normalisierung von Gleitkommazahlen, die der Benutzer frei angeben kann;
> 4. Wenn Sie die Letterbox-Funktion verwenden, müssen Sie die Eingabegröße auf 1,5 MB begrenzen, und die Größe eines einzelnen Kanals liegt innerhalb von 0,75 MB.
>
> Zum Beispiel:
>
> 1. Der Eingabedatentyp ist auf uint8 gesetzt, input_range auf gesetzt, die [0,255]Rolle der Dequantisierung besteht nur darin, den Typ zu konvertieren, die Daten von uint8 in float32 zu konvertieren, und die mittleren und std-Parameter können immer noch gemäß den Daten von 0 ~ 255 angegeben werden
> 2. Der Eingabedatentyp wird auf uint8 gesetzt, input_range [0,1]auf festgelegt, die Festkommazahl wird zu einer Gleitkommazahl im Bereich dequantisiert,[0,1] und Mittelwert und std müssen entsprechend dem neuen Gleitkommazahlenbereich angegeben werden.

Der Vorverarbeitungsprozess ist wie folgt (die grünen Knoten in der Abbildung sind optional):

![Vorprozess.png](https://i.loli.net/2021/11/08/fhBLsozUTCbt4dp.png)

**Codebeispiel**

Instanziieren Sie CompileOptions, konfigurieren Sie die Werte jeder Eigenschaft

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

### 4.2.2 ImportOptions

**Funktionsbeschreibung**

ImportOptions-Klasse zum Konfigurieren von nncase-Importoptionen

**Klassendefinition**

```python
py::class_<import_options>(m, "ImportOptions")
    .def(py::init())
    .def_readwrite("output_arrays", &import_options::output_arrays);
```

Jede Eigenschaft wird im Folgenden beschrieben

| Name der Immobilie      | Art   | Ja oder nein | Beschreibung     |
| ------------- | ------ | -------- | -------- |
| output_arrays | Schnur | nicht       | Ausgabename |

**Codebeispiel**

Instanziieren Sie ImageOptions, konfigurieren Sie die Werte jeder Eigenschaft

```python
# import_options
import_options = nncase.ImportOptions()
import_options.output_arrays = 'output' # Your output node name
```

### 4.2.3 PTQTensorOptions

**Funktionsbeschreibung**

PTQTensorOptions-Klasse zum Konfigurieren von nncase PTQ-Optionen

**Klassendefinition**

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

Jede Eigenschaft wird im Folgenden beschrieben

| Der Feldname         | Art   | Ja oder nein | Beschreibung                                                                                  |
| ---------------- | ------ | -------- | ------------------------------------------------------------------------------------- |
| calibrate_method | Schnur | nicht       | Kalibrierungsmethode , unterstützt 'no_clip', 'l2', 'kld_m0', 'kld_m1', 'kld_m2', 'cdf', Standard ist 'no_clip' |
| samples_count    | Int    | nicht       | Die Anzahl der Proben                                                                              |

#### set_tensor_data()

**Funktionsbeschreibung**

Festlegen der Korrekturdaten

**Schnittstellendefinition**

```python
set_tensor_data(calib_data)
```

**Eingabeparameter**

| Parametername   | Art   | Ja oder nein | Beschreibung     |
| ---------- | ------ | -------- | -------- |
| calib_data | Byte[] | sein       | Korrigieren der Daten |

**Der Rückgabewert**

N/A

**Codebeispiel**

```python
# ptq_options
ptq_options = nncase.PTQTensorOptions()
ptq_options.samples_count = cfg.generate_calibs.batch_size
ptq_options.set_tensor_data(np.asarray([sample['data'] for sample in self.calibs]).tobytes())
```

### 4.2.4 Compiler

**Funktionsbeschreibung**

Compilerklasse zum Kompilieren neuronaler Netzwerkmodelle

**Klassendefinition**

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

**Codebeispiel**

```python
compiler = nncase.Compiler(compile_options)
```

#### import_tflite()

**Funktionsbeschreibung**

Importieren des tflite-Modells

**Schnittstellendefinition**

```python
import_tflite(model_content, import_options)
```

**Eingabeparameter**

| Parametername       | Art          | Ja oder nein | Beschreibung           |
| -------------- | ------------- | -------- | -------------- |
| model_content  | Byte[]        | sein       | Lesen Sie den Modellinhalt |
| import_options | ImportOptionen | sein       | Importoptionen       |

**Der Rückgabewert**

N/A

**Codebeispiel**

```python
model_content = read_model_file(model)
compiler.import_tflite(model_content, import_options)
```

#### import_onnx()

**Funktionsbeschreibung**

Importieren des onnx-Modells

**Schnittstellendefinition**

```python
import_onnx(model_content, import_options)
```

**Eingabeparameter**

| Parametername       | Art          | Ja oder nein | Beschreibung           |
| -------------- | ------------- | -------- | -------------- |
| model_content  | Byte[]        | sein       | Lesen Sie den Modellinhalt |
| import_options | ImportOptionen | sein       | Importoptionen       |

**Der Rückgabewert**

N/A

**Codebeispiel**

```python
model_content = read_model_file(model)
compiler.import_onnx(model_content, import_options)
```

#### import_caffe()

**Funktionsbeschreibung**

Importieren des Caffe-Modells

> Benutzer müssen caffe auf dem lokalen Computer kompilieren/installieren.

**Schnittstellendefinition**

```python
import_caffe(caffemodel, prototxt)
```

**Eingabeparameter**

| Parametername   | Art   | Ja oder nein | Beschreibung                 |
| ---------- | ------ | -------- | -------------------- |
| caffemodel | Byte[] | sein       | Lesen Sie den caffemodel-Inhalt |
| Prototxt   | Byte[] | sein       | Lesen Sie den Prototxt-Inhalt   |

**Der Rückgabewert**

N/A

**Codebeispiel**

```python
# import
caffemodel = read_model_file('test.caffemodel')
prototxt = read_model_file('test.prototxt')
compiler.import_caffe(caffemodel, prototxt)
```

#### use_ptq()

**Funktionsbeschreibung**

PTQ-Konfigurationsoptionen festlegen

**Schnittstellendefinition**

```python
use_ptq(ptq_options)
```

**Eingabeparameter**

| Parametername    | Art             | Ja oder nein | Beschreibung        |
| ----------- | ---------------- | -------- | ----------- |
| ptq_options | PTQTensorOptions | sein       | PTQ-Konfigurationsoptionen |

**Der Rückgabewert**

N/A

**Codebeispiel**

```python
compiler.use_ptq(ptq_options)
```

#### kompilieren()

**Funktionsbeschreibung**

Kompilieren des neuronalen Netzwerkmodells

**Schnittstellendefinition**

```python
compile()
```

**Eingabeparameter**

N/A

**Der Rückgabewert**

N/A

**Codebeispiel**

```python
compiler.compile()
```

#### gencode_tobytes()

**Funktionsbeschreibung**

Generiert einen Strom von Codebytes

**Schnittstellendefinition**

```python
gencode_tobytes()
```

**Eingabeparameter**

N/A

**Der Rückgabewert**

Bytes[]

**Codebeispiel**

```python
kmodel = compiler.gencode_tobytes()
with open(os.path.join(infer_dir, 'test.kmodel'), 'wb') as f:
    f.write(kmodel)
```

## 4.3 Kompilieren des Modellbeispiels

Im folgenden Beispiel wird das Modell- und Python-Kompilierungsskript verwendet

- Das Modell befindet sich im Unterverzeichnis /path/to/nncase_sdk/examples/models/
- Das Python-Kompilierungsskript befindet sich im Unterverzeichnis /path/to/nncase_sdk/examples/scripts

### 4.3.1 Kompilieren des float32 tflite-Modells

- Mobilenetv2_tflite_fp32_image.py Skript lautet wie folgt

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

- Führen Sie den folgenden Befehl aus, um das tflite-Modell von mobiletv2, target k510, zu kompilieren

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_tflite_fp32_image.py --target k510 --model models/mobilenet_v2_1.0_224.tflite
```

### 4.3.2 Kompilieren des float32 onnx-Modells

- Für onnx-Modelle wird empfohlen, die Verwendung von[ONNX Simplifier](https://github.com/daquexian/onnx-simplifier)zu vereinfachen, bevor Sie mit nncase kompilieren
- mobilenetv2_onnx_fp32_image.py Skript lautet wie folgt

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

- Führen Sie den folgenden Befehl aus, um das onnx-Modell von mobiletv2, target k510, zu kompilieren

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_onnx_fp32_image.py --target k510 --model models/mobilenetv2-7.onnx
```

### 4.3.3 Kompilieren des float32 Caffe-Modells

- Das Caffe Wheel Paket stammt[von](https://github.com/kendryte/caffe/releases)kendryte caffe
- conv2d_caffe_fp32.py Skript lautet wie folgt

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

- Führen Sie den folgenden Befehl aus, um das Caffe-Modell von conv2d mit dem Ziel k510 zu kompilieren

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/conv2d_caffe_fp32.py --target k510 --caffemodel models/test.caffemodel --prototxt models/test.prototxt
```

### 4.3.4 Kompilieren und Hinzufügen des Vorverarbeitungsmodells float32 onnx

- Für onnx-Modelle wird empfohlen, die Verwendung von[ONNX Simplifier](https://github.com/daquexian/onnx-simplifier)zu vereinfachen, bevor Sie mit nncase kompilieren
- Mobilenetv2_onnx_fp32_preprocess.py Skript lautet wie folgt

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

- Führen Sie den folgenden Befehl aus, um das onnx-Modell von mobiletv2 mit dem Ziel-k510 zu kompilieren

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_onnx_fp32_preprocess.py --target k510 --model models/mobilenetv2-7.onnx
```

### 4.3.5 Kompilieren des uint8-Quantisierungs-tflite-Modells

- Mobilenetv2_tflite_uint8_image.py Skript lautet wie folgt

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

- Führen Sie den folgenden Befehl aus, um das tflite-Modell von uint8 quantized mobiletv2, target k510 zu kompilieren

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_tflite_uint8_image.py --target k510 --model models/mobilenet_v2_1.0_224.tflite
```

## 4.4 Inferenzmodell-APIs

Neben den APs des kompilierten Modells stellt nncase auch die APIs des Inferenzmodells zur Verfügung, die vor der Kompilierung des kmodels auf dem PC abgeleitet werden können, mit dem überprüft wird, ob die nncase-Inferenzergebnisse und die Laufzeitergebnisse des entsprechenden Deep-Learning-Frameworks konsistent sind.

### 4.4.1 Speicherbereich

**Funktionsbeschreibung**

Die MemoryRange-Klasse, die verwendet wird, um einen Speicherbereich darzustellen

**Klassendefinition**

```python
py::class_<memory_range>(m, "MemoryRange")
    .def_readwrite("location", &memory_range::memory_location)
    .def_property(
        "dtype", [](const memory_range &range) { return to_dtype(range.datatype); },
        [](memory_range &range, py::object dtype) { range.datatype = from_dtype(py::dtype::from_args(dtype)); })
    .def_readwrite("start", &memory_range::start)
    .def_readwrite("size", &memory_range::size);
```

Jede Eigenschaft wird im Folgenden beschrieben

| Name der Immobilie | Art           | Ja oder nein | Beschreibung                                                                       |
| -------- | -------------- | -------- | -------------------------------------------------------------------------- |
| Ort | Int            | nicht       | Speicherposition, 0 für Eingang, 1 für Ausgang, 2 für rdata, 3 für Daten, 4 für shared_data |
| dtype    | Python-Datentyp | nicht       | Datentyp                                                                   |
| anfangen    | Int            | nicht       | Speicherstartadresse                                                               |
| Größe     | Int            | nicht       | Speichergröße                                                                   |

**Codebeispiel**

Instanziieren des Speicherbereichs

```python
mr = nncase.MemoryRange()
```

### 4.4.2 RuntimeTensor

**Funktionsbeschreibung**

Die RuntimeTensor-Klasse, die den Laufzeittensor darstellt

**Klassendefinition**

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

Jede Eigenschaft wird im Folgenden beschrieben

| Name der Immobilie | Art | Ja oder nein | Beschreibung             |
| -------- | ---- | -------- | ---------------- |
| dtype    | Int  | nicht       | Datentyp von Tensor |
| Form    | Liste | nicht       | Die Form des Tensors     |

#### from_numpy()

**Funktionsbeschreibung**

Erstellen des RuntimeTensor-Objekts aus numpy.ndarray

**Schnittstellendefinition**

```python
from_numpy(py::array arr)
```

**Eingabeparameter**

| Parametername | Art          | Ja oder nein | Beschreibung              |
| -------- | ------------- | -------- | ----------------- |
| Arr      | numpy.ndarray | sein       | numpy.ndarray-Objekt |

**Der Rückgabewert**

RuntimeTensor

**Codebeispiel**

```python
tensor = nncase.RuntimeTensor.from_numpy(self.inputs[i]['data'])
```

#### copy_to()

**Funktionsbeschreibung**

Laufzeittensor kopieren

**Schnittstellendefinition**

```python
copy_to(RuntimeTensor to)
```

**Eingabeparameter**

| Parametername | Art          | Ja oder nein | Beschreibung              |
| -------- | ------------- | -------- | ----------------- |
| An       | RuntimeTensor | sein       | RuntimeTensor-Objekt |

**Der Rückgabewert**

N/A

**Codebeispiel**

```python
sim.get_output_tensor(i).copy_to(to)
```

#### to_numpy()

**Funktionsbeschreibung**

Konvertieren von RuntimeTensor in ein numpy.ndarray-Objekt

**Schnittstellendefinition**

```python
to_numpy()
```

**Eingabeparameter**

N/A

**Der Rückgabewert**

numpy.ndarray-Objekt

**Codebeispiel**

```python
arr = sim.get_output_tensor(i).to_numpy()
```

### 4.4.3 Simulator

**Funktionsbeschreibung**

Simulatorklasse für Inferenz kmodel auf PC

**Klassendefinition**

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

Jede Eigenschaft wird im Folgenden beschrieben

| Name der Immobilie     | Art | Ja oder nein | Beschreibung     |
| ------------ | ---- | -------- | -------- |
| inputs_size  | Int  | nicht       | Geben Sie die Anzahl der |
| outputs_size | Int  | nicht       | Die Anzahl der Ausgaben |

**Codebeispiel**

Instanziieren des Simulators

```python
sim = nncase.Simulator()
```

#### load_model()

**Funktionsbeschreibung**

Laden Sie das kmodel

**Schnittstellendefinition**

```python
load_model(model_content)
```

**Eingabeparameter**

| Parametername      | Art   | Ja oder nein | Beschreibung         |
| ------------- | ------ | -------- | ------------ |
| model_content | Byte[] | sein       | Kmodel-Bytestream |

**Der Rückgabewert**

N/A

**Codebeispiel**

```python
sim.load_model(kmodel)
```

#### get_input_desc()

**Funktionsbeschreibung**

Ruft die Beschreibung der Eingabe für den angegebenen Index ab.

**Schnittstellendefinition**

```python
get_input_desc(index)
```

**Eingabeparameter**

| Parametername | Art | Ja oder nein | Beschreibung       |
| -------- | ---- | -------- | ---------- |
| Index    | Int  | sein       | Der Index der Eingabe |

**Der Rückgabewert**

Speicherbereich

**Codebeispiel**

```python
input_desc_0 = sim.get_input_desc(0)
```

#### get_output_desc()

**Funktionsbeschreibung**

Ruft die Beschreibung der Ausgabe des angegebenen Indexes ab.

**Schnittstellendefinition**

```python
get_output_desc(index)
```

**Eingabeparameter**

| Parametername | Art | Ja oder nein | Beschreibung       |
| -------- | ---- | -------- | ---------- |
| Index    | Int  | sein       | Der Index der Ausgabe |

**Der Rückgabewert**

Speicherbereich

**Codebeispiel**

```python
output_desc_0 = sim.get_output_desc(0)
```

#### get_input_tensor()

**Funktionsbeschreibung**

Ruft den RuntimeTensor für die Eingabe für den angegebenen Index ab.

**Schnittstellendefinition**

```python
get_input_tensor(index)
```

**Eingabeparameter**

| Parametername | Art | Ja oder nein | Beschreibung             |
| -------- | ---- | -------- | ---------------- |
| Index    | Int  | sein       | Geben Sie den Index des Tensors ein |

**Der Rückgabewert**

RuntimeTensor

**Codebeispiel**

```python
input_tensor_0 = sim.get_input_tensor(0)
```

#### set_input_tensor()

**Funktionsbeschreibung**

Legt den Laufzeittensor für die Eingabe des angegebenen Indexes fest.

**Schnittstellendefinition**

```python
set_input_tensor(index, tensor)
```

**Eingabeparameter**

| Parametername | Art          | Ja oder nein | Beschreibung                    |
| -------- | ------------- | -------- | ----------------------- |
| Index    | Int           | sein       | Geben Sie den Index von RuntimeTensor ein |
| Tensor   | RuntimeTensor | sein       | RuntimeTensor eingeben       |

**Der Rückgabewert**

N/A

**Codebeispiel**

```python
sim.set_input_tensor(0, nncase.RuntimeTensor.from_numpy(self.inputs[0]['data']))
```

#### get_output_tensor()

**Funktionsbeschreibung**

Ruft den Laufzeittensor für die Ausgabe des angegebenen Indexes ab.

**Schnittstellendefinition**

```python
get_output_tensor(index)
```

**Eingabeparameter**

| Parametername | Art | Ja oder nein | Beschreibung                    |
| -------- | ---- | -------- | ----------------------- |
| Index    | Int  | sein       | Gibt den Index des RuntimeTensor aus |

**Der Rückgabewert**

RuntimeTensor

**Codebeispiel**

```python
output_arr_0 = sim.get_output_tensor(0).to_numpy()
```

#### set_output_tensor()

**Funktionsbeschreibung**

Legt den RuntimeTensor für die Ausgabe des angegebenen Indexes fest.

**Schnittstellendefinition**

```python
set_output_tensor(index, tensor)
```

**Eingabeparameter**

| Parametername | Art          | Ja oder nein | Beschreibung                    |
| -------- | ------------- | -------- | ----------------------- |
| Index    | Int           | sein       | Gibt den Index des RuntimeTensor aus |
| Tensor   | RuntimeTensor | sein       | Laufzeittensor für die Ausgabe       |

**Der Rückgabewert**

N/A

**Codebeispiel**

```python
sim.set_output_tensor(0, tensor)
```

#### run()

**Funktionsbeschreibung**

Ausführen von kmodel-Inferenz

**Schnittstellendefinition**

```python
run()
```

**Eingabeparameter**

N/A

**Der Rückgabewert**

N/A

**Codebeispiel**

```python
sim.run()
```

## 4.5 Beispiel eines Inferenzmodells

**Voraussetzung:**mobilenetv2_onnx_fp32_image.py Skript wurde mit dem Modell MobileTV2-7.onnx kompiliert

mobilenetv2_onnx_simu.py befindet sich im Unterverzeichnis /path/to/nncase_sdk/examples/scripts, das wie folgt lautet:

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

Ausführen des Inferenzskripts

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_onnx_simu.py --model_file models/mobilenetv2-7.onnx --kmodel_file tmp/mobilenetv2_onnx_fp32_image/test.kmodel --input_file mobilenetv2_onnx_fp32_image/data/input_0_0.bin
```

Der Vergleich der Ergebnisse des nncase-Simulators und der CPU-Inferenz ist wie folgt

```shell
... ...
output 0 cosine similarity : 0.9992437958717346
```

# 5 nnncase Laufzeitbibliothek

## 5.1 Einführung in die nncase Runtime

Die nncase-Laufzeit wird verwendet, um kmodel auf AI-Geräten zu laden / Eingabedaten einzustellen / KPU-Berechnungen durchzuführen / Ausgabedaten zu erhalten usw.

Derzeit sind nur**die C++-Version**von APIs, zugehörigen Headerdateien und statischen Bibliotheken im nncase sdk/riscv64-Verzeichnis verfügbar.

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

## 5.2 Laufzeit-APIs

### 5.2.1 Klasse runtime_tensor

Tensor zum Speichern von Modelleingabe-/Ausgabedaten

#### hrt::create()

**Funktionsbeschreibung**

Erstellen einer runtime_tensor

**Schnittstellendefinition**

```C++
(1) NNCASE_API result<runtime_tensor> create(datatype_t datatype, runtime_shape_t shape, memory_pool_t pool = pool_cpu_only, uintptr_t physical_address = 0) noexcept;

(2) NNCASE_API result<runtime_tensor> create(datatype_t datatype, runtime_shape_t shape, gsl::span<gsl::byte> data, bool copy, memory_pool_t pool = pool_cpu_only, uintptr_t physical_address = 0) noexcept;
```

**Eingabeparameter**

| Parametername         | Art                  | Ja oder nein | Beschreibung                              |
| ---------------- | --------------------- | -------- | --------------------------------- |
| Datatype         | datatype_t            | sein       | Datentyp, z. B. dt_float32            |
| Form            | runtime_shape_t       | sein       | Die Form des Tensors                      |
| Daten             | gsl::span\<gsl::byte> | sein       | Datenpuffer für den Benutzerstatus                  |
| kopieren             | Bool                  | sein       | Ob kopiert werden soll                          |
| Tümpel             | memory_pool_t         | nicht       | Speicherpooltyp, Standardwert ist pool_cpu_only |
| physical_address | uintptr_t             | nicht       | Physische Adresse, Standardwert ist 0               |

**Der Rückgabewert**

Ergebnis<runtime_tensor>

Codebeispiel

```c++
// create input
auto in_shape = interp.input_shape(0);
auto input_tensor = host_runtime_tensor::create(dt_float32, in_shape,
                                                {(gsl::byte *)mat.data, mat.cols * mat.rows * mat.elemSize()},
                                                true, hrt::pool_shared).expect("cannot create input tensor");
```

### 5.2.2 Klassendolmetscher

Interpreter ist eine laufende Instanz der nncase-Laufzeit, die funktionale Kernfunktionen wie load_model()/run()/input_tensor()/output_tensor() bereitstellt.

#### load_model()

**Funktionsbeschreibung**

Laden des kmodel-Modells

**Schnittstellendefinition**

```C++
 NNCASE_NODISCARD result<void> load_model(gsl::span<const gsl::byte> buffer) noexcept;
```

**Eingabeparameter**

| Parametername | Art                            | Ja oder nein | Beschreibung          |
| -------- | ------------------------------- | -------- | ------------- |
| Puffer   | gsl::span `<const gsl::byte>` | sein       | kmodel-Puffer |

**Der Rückgabewert**

Ergebnis `<void>`

**Codebeispiel**

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

**Funktionsbeschreibung**

Ruft die Anzahl der Modelleingaben ab.

**Schnittstellendefinition**

```C++
size_t inputs_size() const noexcept;
```

**Eingabeparameter**

N/A

**Der Rückgabewert**

size_t

**Codebeispiel**

```c++
auto inputs_size = interp.inputs_size();
```

#### outputs_size()

**Funktionsbeschreibung**

Ruft die Anzahl der Modellausgaben ab.

**Schnittstellendefinition**

```C++
size_t outputs_size() const noexcept;
```

**Eingabeparameter**

N/A

**Der Rückgabewert**

size_t

**Codebeispiel**

```c++
auto outputs_size = interp.outputs_size();
```

#### input_shape()

**Funktionsbeschreibung**

Ruft die Form der angegebenen Modelleingabe ab.

**Schnittstellendefinition**

```C++
const runtime_shape_t &input_shape(size_t index) const noexcept;
```

**Eingabeparameter**

| Parametername | Art   | Ja oder nein | Beschreibung       |
| -------- | ------ | -------- | ---------- |
| Index    | size_t | sein       | Der Index der Eingabe |

**Der Rückgabewert**

runtime_shape_t

**Codebeispiel**

```c++
auto in_shape = interp.input_shape(0);
```

#### output_shape()

**Funktionsbeschreibung**

Ruft die Form der angegebenen Ausgabe des Modells ab.

**Schnittstellendefinition**

```C++
const runtime_shape_t &output_shape(size_t index) const noexcept;
```

**Eingabeparameter**

| Parametername | Art   | Ja oder nein | Beschreibung       |
| -------- | ------ | -------- | ---------- |
| Index    | size_t | sein       | Der Index der Ausgabe |

**Der Rückgabewert**

runtime_shape_t

**Codebeispiel**

```c++
auto out_shape = interp.output_shape(0);
```

#### input_tensor()

**Funktionsbeschreibung**

Ruft den Eingabetensor für den angegebenen Index ab/legt ihn fest.

**Schnittstellendefinition**

```C++
(1) result<runtime_tensor> input_tensor(size_t index) noexcept;
(2) result<void> input_tensor(size_t index, runtime_tensor tensor) noexcept;
```

**Eingabeparameter**

| Parametername | Art           | Ja oder nein | Beschreibung                     |
| -------- | -------------- | -------- | ------------------------ |
| Index    | size_t         | sein       | kmodel-Puffer            |
| Tensor   | runtime_tensor | sein       | Geben Sie den entsprechenden Laufzeittensor ein |

**Der Rückgabewert**

(1) Gibt die Ergebnisse zurück<runtime_tensor>

(2) Gibt die Ergebnisse zurück `<void>`

**Codebeispiel**

```c++
// set input
interp.input_tensor(0, input_tensor).expect("cannot set input tensor");
```

#### output_tensor()

**Funktionsbeschreibung**

Ruft den ausgehenden Tensor für den angegebenen Index ab/legt diesen fest.

**Schnittstellendefinition**

```C++
(1) result<runtime_tensor> output_tensor(size_t index) noexcept;
(2) result<void> output_tensor(size_t index, runtime_tensor tensor) noexcept;
```

**Eingabeparameter**

| Parametername | Art           | Ja oder nein | Beschreibung                     |
| -------- | -------------- | -------- | ------------------------ |
| Index    | size_t         | sein       |                          |
| Tensor   | runtime_tensor | sein       | Geben Sie den entsprechenden Laufzeittensor ein |

**Der Rückgabewert**

(1) Gibt die Ergebnisse zurück<runtime_tensor>

(2) Gibt die Ergebnisse zurück `<void>`

**Codebeispiel**

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

**Funktionsbeschreibung**

Durchführung von kPU-Berechnungen

**Schnittstellendefinition**

```C++
result<void> run() noexcept;
```

**Eingabeparameter**

N/A

**Der Rückgabewert**

Ergebnis `<void>`

**Codebeispiel**

```c++
// run
interp.run().expect("error occurred in running model");
```

## 5.3 Laufzeitbeispiel

Der Beispielcode befindet sich unter /path/to/nncase_sdk/examples/mobilenetv2_onnx_fp32_image

**Präfixbedingung**

- mobilenetv2_onnx_fp32_image.py Skript hat das MobileTV2-7.onnx-Modell kompiliert
- Da das Beispiel auf der OpenCV-Bibliothek basiert, müssen Sie den Pfad zu OpenCV in der CMakeLists-.txt des Beispiels angeben.

**Kompilieren von Apps**

```shell
cd /path/to/nncase_sdk/examples
./build.sh
```

Generieren Sie schließlich die mobilenetv2_onnx_fp32_image im Verzeichnis out/bin

**Der k510 EVB arbeitet auf dem Board**

Kopieren Sie die folgenden Dateien auf das k510 EVB-Board

| Datei                        | Bemerkung                                                         |
| --------------------------- | ------------------------------------------------------------ |
| mobilenetv2_onnx_fp32_image | Kompilierungsübergreifende Beispiele werden generiert                                         |
| test.kmodel                 | Verwenden Sie mobilenetv2_onnx_fp32_image.py Kompilieren Sie den MobileTV2-7.onnx-Build |
| Katze .png und labels_1000.txt    | Befindet sich im Unterverzeichnis /path/to/nncase_sdk/examples/mobilenetv2_onnx_fp32_image/data/ |

```bash
$ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mnt/zhangyang/nncase_check/lib/gomp:/mnt/zhangyang/nncase_check/lib/opencv
$ ./mobilenetv2_onnx_fp32_image test.kmodel cat.png labels_1000.txt
case ./mobilenetv2_onnx_fp32_image build at Mar  1 2022 16:31:29
interp.run() duration: 12.6642 ms
image classification result: tiger cat(9.25)
```

# 6 Funktionale Programmierbibliotheken (Laufzeitunterstützung)

## 6.1 Einführung in Functional

nncase Functional wird verwendet, um die Benutzerfreundlichkeit zu verbessern, wenn Benutzer Modelle vor und nach der Verarbeitung verwenden

Derzeit ist nur die C ++ - Version von APIs verfügbar, und die zugehörigen Headerdateien und Bibliotheken befinden sich im Verzeichnis riscv64 des nncase sdk.

## 6.2 APIS

### 6.2.1 Quadrat

**Funktionsbeschreibung**

Berechnen Sie das Quadrat, unterstützen Sie derzeit Eingabe uint8 / int8, Ausgabe ist auch uint8 / int8, beachten Sie, dass die Eingabe Fixpunkt ist und die Ausgabe Gleitkommazahl ist, müssen Sie die Quantisierungsparameter einstellen.

**Schnittstellendefinition**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`square`](#ops_8h_1adff2f60c7c045a9840519eab2c04d127)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Eingabeparameter**

| Parametername  | Art           | Ja oder nein | Beschreibung                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | sein       | Eingabe                |
| `dtype` | datatype_t     | sein       | Datentyp des Ausgabetensors |

**Der Rückgabewert**

`result<runtime_tensor>`

**Codebeispiel**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto squared = F::square(input, output_type).unwrap_or_throw();
```

### 6.2.2 sqrt

**Funktionsbeschreibung**

Berechnen Sie den Stammzahlenwert, unterstützen Sie derzeit die Eingabe uint8 / int8, die Ausgabe ist auch uint8 / int8, beachten Sie, dass die Eingabe ein Festkommapunkt ist und die Ausgabe Gleitkommazahlen ist, um die Quantisierungsparameter festzulegen.

**Schnittstellendefinition**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`sqrt`](#ops_8h_1a53f8dde3dd4e27058b5dc743eb5dd076)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Eingabeparameter**

| Parametername  | Art           | Ja oder nein | Beschreibung                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | sein       | Eingabe                |
| `dtype` | datatype_t     | sein       | Datentyp des Ausgabetensors |

**Der Rückgabewert**

`result<runtime_tensor>`

**Codebeispiel**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::sqrt(input, output_type).unwrap_or_throw();
```

### 6.2.3 Protokoll

**Funktionsbeschreibung**

Berechnen Sie den Log-Wert, die negative Anzahl der Eingabe wird in Nan konvertiert, unterstützt derzeit Eingabe uint8 / int8, Ausgabe ist auch uint8 / int8, beachten Sie, dass die Eingabe Fixpunkt ist und die Ausgabe Gleitkomma ist, muss den Quantisierungsparameter einstellen.

**Schnittstellendefinition**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`log`](#ops_8h_1a91df53276c3f1511427d4ac1a0140b71)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Eingabeparameter**

| Parametername  | Art           | Ja oder nein | Beschreibung                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | sein       | Eingabe                |
| `dtype` | datatype_t     | sein       | Datentyp des Ausgabetensors |

**Der Rückgabewert**

`result<runtime_tensor>`

**Codebeispiel**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::log(input, output_type).unwrap_or_throw();
```

### 6.2.4 exp

**Funktionsbeschreibung**

Berechnen Sie den exp-Wert, unterstützen Sie derzeit die Eingabe uint8 / int8, die Ausgabe ist auch uint8 / int8, beachten Sie, dass die Eingabe ein Fixpunkt und die Ausgabe ein Gleitkommawert ist, müssen Sie die Quantisierungsparameter einstellen.

**Schnittstellendefinition**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`exp`](#ops_8h_1a2c6ce457805a5ba515fa7454fb4aede0)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Eingabeparameter**

| Parametername  | Art           | Ja oder nein | Beschreibung                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | sein       | Eingabe                |
| `dtype` | datatype_t     | sein       | Datentyp des Ausgabetensors |

**Der Rückgabewert**

`result<runtime_tensor>`

**Codebeispiel**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::exp(input, output_type).unwrap_or_throw();
```

### 6.2.5 ohne

**Funktionsbeschreibung**

Um den Sin-Wert zu berechnen, wird die Eingabe uint8/int8 derzeit unterstützt, und die Ausgabe ist auch uint8/int8, beachten Sie, dass die Quantisierungsparameter gesetzt werden müssen, wenn die Eingabe Festkommazahl und die Ausgabe Gleitkommazahlen ist.

**Schnittstellendefinition**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`sin`](#ops_8h_1a9605b2b0dc9a6892ce878bda14586890)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Eingabeparameter**

| Parametername  | Art           | Ja oder nein | Beschreibung                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | sein       | Eingabe                |
| `dtype` | datatype_t     | sein       | Datentyp des Ausgabetensors |

**Der Rückgabewert**

`result<runtime_tensor>`

**Codebeispiele**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::sin(input, output_type).unwrap_or_throw();
```

### 6.2.6 Körper

**Funktionsbeschreibung**

Berechnen Sie den cos-Wert, unterstützen Sie derzeit die Eingabe uint8 / int8, die Ausgabe ist auch uint8 / int8, beachten Sie, dass die Eingabe ein Festkommapunkt ist und die Ausgabe Gleitkommazahlen ist, um den Quantisierungsparameter festzulegen.

**Schnittstellendefinition**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`cos`](#ops_8h_1a71d36c13c82f4c411f24d030cf333249)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Eingabeparameter**

| Parametername  | Art           | Ja oder nein | Beschreibung                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | sein       | Eingabe                |
| `dtype` | datatype_t     | sein       | Datentyp des Ausgabetensors |

**Der Rückgabewert**

`result<runtime_tensor>`

**Codebeispiele**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::cos(input, output_type).unwrap_or_throw();
```

### 6.2.7 Runde

**Funktionsbeschreibung**

Um den Rundungswert zu berechnen, wird derzeit die Eingabe uint8/int8 unterstützt, und die Ausgabe ist auch uint8/int8, beachten Sie, dass der Quantisierungsparameter gesetzt werden muss, wenn die Eingabe Fixpunkt und die Ausgabe Gleitkomma ist.

**Schnittstellendefinition**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`round`](#ops_8h_1a81db8ac4866004f75fb65db876262785)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Eingabeparameter**

| Parametername  | Art           | Ja oder nein | Beschreibung                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | sein       | Eingabe                |
| `dtype` | datatype_t     | sein       | Datentyp des Ausgabetensors |

**Der Rückgabewert**

`result<runtime_tensor>`

**Codebeispiele**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::round(input, output_type).unwrap_or_throw();
```

### 6.2.8 Etage

**Funktionsbeschreibung**

Berechnen Sie den Frostwert, unterstützen Sie derzeit Eingang uint8 / int8, Ausgabe ist auch uint8 / int8, beachten Sie, dass die Eingabe Fixpunkt ist und die Ausgabe Gleitkommazahl ist, müssen Sie die Quantisierungsparameter einstellen.

**Schnittstellendefinition**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`floor`](#ops_8h_1a1079af8fe9fb6edbb2906d91fac12635)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Eingabeparameter**

| Parametername  | Art           | Ja oder nein | Beschreibung                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | sein       | Eingabe                |
| `dtype` | datatype_t     | sein       | Datentyp des Ausgabetensors |

**Der Rückgabewert**

`result<runtime_tensor>`

**Codebeispiele**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::floor(input, output_type).unwrap_or_throw();
```

### 6.2.9 CEIL

**Funktionsbeschreibung**

Berechnen Sie den ceil-Wert, unterstützen derzeit die Eingabe uint8 / int8, die Ausgabe ist auch uint8 / int8, beachten Sie, dass die Eingabe ein Fixpunkt und die Ausgabe ein Gleitkommafaktor ist, müssen die Quantisierungsparameter festgelegt werden.

**Schnittstellendefinition**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`ceil`](#ops_8h_1ad3b78c97f1e5348a26de7e5ba2396fb7)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Eingabeparameter**

| Parametername  | Art           | Ja oder nein | Beschreibung                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | sein       | Eingabe                |
| `dtype` | datatype_t     | sein       | Datentyp des Ausgabetensors |

**Der Rückgabewert**

`result<runtime_tensor>`

**Codebeispiele**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::ceil(input, output_type).unwrap_or_throw();
```

### 6.2.10 abs

**Funktionsbeschreibung**

Berechnen Sie den ABS-Wert, unterstützen Sie derzeit die Eingabe uint8 / int8, die Ausgabe ist auch uint8 / int8, beachten Sie, dass die Eingabe ein Festkommapunkt ist und die Ausgabe Gleitkommazahlen ist, um die Quantisierungsparameter einzustellen.

**Schnittstellendefinition**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`abs`](#ops_8h_1ad8290dc793bae0dc22b3baf9e0f80c14)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Eingabeparameter**

| Parametername  | Art           | Ja oder nein | Beschreibung                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | sein       | Eingabe                |
| `dtype` | datatype_t     | sein       | Datentyp des Ausgabetensors |

**Der Rückgabewert**

`result<runtime_tensor>`

**Codebeispiele**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::abs(input, output_type).unwrap_or_throw();
```

### 6.2.11 neg

**Funktionsbeschreibung**

Berechnen Sie den Wert von neg, unterstützen Sie derzeit Eingabe uint8 / int8, Ausgabe ist auch uint8 / int8, beachten Sie, dass die Eingabe Fixpunkt ist und die Ausgabe Gleitkomma ist, muss die Quantisierungsparameter einstellen.

**Schnittstellendefinition**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`neg`](#ops_8h_1aa1b7858802e1afce78db72163c5210d8)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Eingabeparameter**

| Parametername  | Art           | Ja oder nein | Beschreibung                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | sein       | Eingabe                |
| `dtype` | datatype_t     | sein       | Datentyp des Ausgabetensors |

**Der Rückgabewert**

`result<runtime_tensor>`

**Codebeispiele**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::neg(input, output_type).unwrap_or_throw();
```

### 6.2.12 quantisieren

**Funktionsbeschreibung**

Eingabe dt_bfloat16, dt_float32 Daten, Ausgabe dt_int8 oder dt_uint8 Ausgabe

**Schnittstellendefinition**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`quantize`](#ops_8h_1ad8ad779083b5c08da520d2f1c2469c3a)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Eingabeparameter**

| Parametername  | Art           | Ja oder nein | Beschreibung                                |
| --------- | -------------- | -------- | ----------------------------------- |
| `input` | runtime_tensor | sein       | Eingang, Typ muss float32 oder bfloat16 sein |
| `dtype` | datatype_t     | sein       | Datentyp des Ausgabetensors                 |

**Der Rückgabewert**

`result<runtime_tensor>`

**Codebeispiele**

```cpp
auto quantized = F::quantize(input, dt_int8).unwrap_or_throw();
```

### 6.2.13 Dequantisieren

**Funktionsbeschreibung**

Geben Sie die Eingabe uint8 oder int8 ein und konvertieren Sie sie in float- oder bfloat-Daten. Beachten Sie, dass der Benutzer die korrekten Quantisierungsparameter für die Daten im Voraus für die Dequantisierung festlegen muss.

**Schnittstellendefinition**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`dequantize`](#ops_8h_1ab91a262349baf393c91abad6f393de24)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Eingabeparameter**

| Parametername  | Art           | Ja oder nein | Beschreibung                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | sein       | Eingabe                |
| `dtype` | datatype_t     | sein       | Datentyp des Ausgabetensors |

**Der Rückgabewert**

`result<runtime_tensor>`

**Codebeispiele**

```cpp
input.quant_param({ 0, 1 });
auto dequantized = F::dequantize(input, output_type).unwrap_or_throw();
```

### 6.2.14 Ernte

**Funktionsbeschreibung**

Gegebene Bboxen, vom ursprünglichen Tensor abgeschnitten und die Größe der Ausgabe in den neuen Tensor geändert. Akzeptieren Sie dt_bfloat16, dt_float32, dt_int8 dt_uint8 Typausgabe, Ausgabe desselben Typs.

**Schnittstellendefinition**

`NNCASE_API inline result<runtime::runtime_tensor> crop(runtime::runtime_tensor &input, runtime::runtime_tensor &bbox, size_t out_h, size_t out_w, image_resize_mode_t resize_mode, bool align_corners, bool half_pixel_centers) noexcept`

**Eingabeparameter**

| Parametername           | Art                | Ja oder nein | Beschreibung                                                                                     |
| ------------------ | ------------------- | -------- | ---------------------------------------------------------------------------------------- |
| Eingabe              | runtime_tensor      | sein       |Geben Sie die Daten  ein, müssen [n,c,h,w] Sie das Layout formatieren, wenn die Daten uint8 oder int8 sind, stellen Sie bitte die Richtigkeit der Datenquantisierungsparameter sicher |
| bbox               | runtime_tensor      | sein       | Geben Sie die bbox-Daten ein, müssen [1,1,m,4] Sie das Layout formatieren, die internen Daten sind,[y0,x0,y1,x1] der Typ ist[float32,bfloat16] |
| out_h              | size_t              | sein       | Höhe der Ausgabedaten                                                                           |
| out_w              | size_t              | sein       | Geben Sie die Datenbreite ein                                                                            |
| resize_mode        | image_resize_mode_t | sein       | Ändern der Größe des Methodenmusters                                                                           |
| align_corners      | Bool                | sein       | Ändern der Größe, ob align_corners                                                    |
| half_pixel_centers | Bool                | sein       | Ändern der Größe, wenn das Pixel zentriert ausgerichtet ist                                                                  |

**Der Rückgabewert**

`result<runtime_tensor>`

**Codebeispiele**

```cpp
auto bbox = get_rand_bbox(input_shape, roi_amount);
auto &&[out_h, out_w] = get_rand_out_hw();
auto output_opt = F::crop(input, bbox, out_h, out_w, resize_mode).unwrap_or_throw();
```

### 6.2.15 Größe ändern

**Funktionsbeschreibung**

Legen Sie angesichts der Breite der Ausgabehöhe die Größe des Eingabetensors auf die neue Größe fest. Akzeptieren Sie dt_bfloat16, dt_float32, dt_int8 dt_uint8 Typausgabe, Ausgabe desselben Typs.

**Schnittstellendefinition**

`NNCASE_API inline result<runtime::runtime_tensor> resize(runtime::runtime_tensor &input, size_t out_h, size_t out_w, image_resize_mode_t resize_mode, bool align_corners, bool half_pixel_centers) noexcept`

**Eingabeparameter**

| Parametername           | Art                | Ja oder nein | Beschreibung                                                                               |
| ------------------ | ------------------- | -------- | ---------------------------------------------------------------------------------- |
| Eingabe              | runtime_tensor      | sein       |Geben Sie die Daten  ein,  die [n,c,h,w] formatiert werden müssen, wenn die Daten uint8 oder int8 sind, stellen Sie bitte die Richtigkeit der Datenquantisierungsparameter sicher |
| out_h              | size_t              | sein       | Höhe der Ausgabedaten                                                                     |
| out_w              | size_t              | sein       | Geben Sie die Datenbreite ein                                                                      |
| resize_mode        | image_resize_mode_t | sein       | Ändern der Größe des Methodenmusters                                                                     |
| align_corners      | Bool                | sein       | Ändern der Größe, ob align_corners                                              |
| half_pixel_centers | Bool                | sein       | Ändern der Größe, wenn das Pixel zentriert ausgerichtet ist                                                            |

**Der Rückgabewert**

`result<runtime_tensor>`

**Codebeispiele**

```cpp
auto &&[out_h, out_w] = get_rand_out_hw();
auto output_opt = F::resize(input, out_h, out_w, resize_mode, false, false).unwrap_or_throw();
```

### 6.2.16 Pad

**Funktionsbeschreibung**

Beim Auffüllen von Daten für jede Dimension werden dt_bfloat16, dt_float32, dt_int8 dt_uint8 Typausgabe und -ausgabe desselben Typs akzeptiert.

**Schnittstellendefinition**

`NNCASE_API inline result<runtime::runtime_tensor> pad(runtime::runtime_tensor &input, runtime_paddings_t &paddings, pad_mode_t pad_mode, float fill_v)`

**Eingabeparameter**

| Parametername | Art               | Ja oder nein | Beschreibung                                                                                                                                       |
| -------- | ------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Eingabe    | runtime_tensor     | sein       | Geben Sie die Daten ein, wenn die Daten uint8 oder int8 sind Stellen Sie sicher, dass die Datenquantisierungsparameter korrekt sind                                                                                  |
| Polsterung  | runtime_paddings_t | sein       | Beispielsweise wird der Auffüllungswert  vor Pad 2 in der letzten Dimension angezeigt, gefolgt von Pad `[ {2,3}, {1,3} ]`3. Der vorletzten Dimension geht Pad 1 voraus, gefolgt von Pad 2 |
| pad_mode | pad_mode_t         | sein       | Derzeit wird nur der const-Modus unterstützt                                                                                                                   |
| fill_v   | schweben              | sein       | Auffüllen der Werte                                                                                                                                     |

**Der Rückgabewert**

`result<runtime_tensor>`

**Codebeispiele**

```cpp
runtime_paddings_t paddings{ { 0, 0 }, { 0, 0 }, { 0, 0 }, { 1, 2 } };
auto output = F::pad(input, paddings, pad_constant, pad_value).unwrap_or_throw();
```
<!-- markdownlint-enable no-emphasis-as-header -->
# 7 Quantitatives Weißbuch

## 7.1 Whitepaper zur Quantifizierung von Klassifikationsmodellen

| Klassifikationsmodell     | CPU-Präzision (Top-1) | Gleitkommagenauigkeit (Top-1) | uint8 Präzision (Top-1) | int8 Präzision (Top-1) |
| ------------ | -------------- | --------------- | ---------------- | --------------- |
| Alexnet      | 0.531          | 0.53            | N/A              | 0.52            |
| densenet 121 | 0.732          | 0.732           | 0.723            | N/A             |
| Inception V3 | 0.766          | 0.765           | 0.773            | 0.77            |
| Gründung V4 | 0.789          | 0.789           | 0.793            | 0.792           |
| MobileNet V1 | 0.731          | 0.73            | 0.723            | 0.718           |
| MobileNet V2 | 0.713          | 0.715           | 0.713            | 0.719           |
| Resnet50 v2  | 0.747          | 0.74            | 0.748            | 0.749           |
| VGG 16       | 0.689          | 0.687           | 0.690            | 0.689           |

> Diese Tabelle dient hauptsächlich dazu, die Leistung der Quantisierung zu vergleichen, die CPU-Genauigkeit ist die vollständige ImageNet-Validierungssatzdaten, und die Gleitkomma- und Quantisierungsgenauigkeit ist das Ergebnis des Datenteilmengentests für das erste Bild der 1000 Klassen im Validierungssatz gemäß der Ordinalzahl.
>
> Die Testergebnisse von Alexnet und SenseNet sind alte Daten, die beide Testergebnisse der ersten 1000 Bilder der Verifikationsmenge als Teilmenge der Daten sind, und N / A ist, dass sich die Testdatenteilmenge zu diesem Zeitpunkt von der CPU unterscheidet, so dass sie nicht als Vergleich verwendet wird.
>
> Da das ausgewählte Netzwerk nicht unbedingt vom offiziellen Netzwerk stammt oder es Unterschiede in der Vorverarbeitung usw. gibt, kann es von der offiziellen Leistung abweichen.

## 7.2 Whitepaper zur Quantifizierung von Erkennungsmodellen

1. YOLOV3

    | COCOAPI                                                      | Offizielle Ergebnisse | CPU-Gleitkommagenauigkeit | GNNE-Gleitkommagenauigkeit | uint8 Präzision | int8 Präzision |
    | ------------------------------------------------------------ | -------- | ----------- | ------------ | --------- | -------- |
    | Durchschnittliche Genauigkeit (AP) @ [IoU = 0,50:0,95\| area = alle \| maxDets = 100] | 0.314    | 0.307       | 0.306        | 0.295     | 0.288    |
    | Durchschnittliche Genauigkeit (AP) @ [IoU = 0,50\| area = alle \| maxDets = 100] | 0.559    | 0.555       | 0.554        | 0.555     | 0.554    |
    | Durchschnittliche Genauigkeit (AP) @ [IoU = 0,75\| area = alle \| maxDets = 100] | 0.318    | 0.308       | 0.307        | 0.287     | 0.275    |
    | Durchschnittliche Genauigkeit (AP) @ [IoU = 0,50:0,95\| Fläche = klein \| maxDets = 100] | 0.142    | 0.150       | 0.149        | 0.147     | 0.144    |
    | Durchschnittliche Genauigkeit (AP) @ [IoU= 0,50:0,95\| Fläche = mittel \| maxDets = 100] | 0.341    | 0.332       | 0.332        | 0.322     | 0.316    |
    | Durchschnittliche Genauigkeit (AP) @ [IoU = 0,50:0,95\| Fläche = groß \| maxDets = 100] | 0.464    | 0.437       | 0.437        | 0.414     | 0.404    |
    | Durchschnittlicher Rückruf (AR) @ [IoU= 0,50:0,95\| area = alle \| maxDets = 1] | 0.278    | 0.270       | 0.271        | 0.262     | 0.256    |
    | Durchschnittlicher Rückruf (AR) @ [IoU= 0,50:0,95\| area = alle \| maxDets = 10] | 0.419    | 0.412       | 0.412        | 0.399     | 0.392    |
    | Durchschnittlicher Rückruf (AR) @ [IoU = 0,50:0,95\| area = alle \| maxDets = 100] | 0.442    | 0.433       | 0.433        | 0.421     | 0.414    |
    | Durchschnittlicher Rückruf (AR) @ [IoU = 0,50:0,95\| Fläche = klein \| maxDets = 100] | 0.239    | 0.251       | 0.251        | 0.248     | 0.246    |
    | Durchschnittlicher Rückruf (AR) @ [IoU= 0,50:0,95\| Fläche = mittel \| maxDets = 100] | 0.482    | 0.462       | 0.463        | 0.451     | 0.443    |
    | Durchschnittlicher Rückruf (AR) @ [IoU = 0,50:0,95\| Fläche = groß \| maxDets = 100] | 0.611    | 0.586       | 0.585        | 0.559     | 0.550    |

2. SSD-MobileNetV1

    | COCOAPI                                                                    | Offizielle Ergebnisse | CPU-Gleitkommagenauigkeit | GNNE-Gleitkommagenauigkeit | uint8 Präzision | int8 Präzision |
    | -------------------------------------------------------------------------- | -------- | ----------- | ------------ | --------- | -------- |
    | Durchschnittliche Genauigkeit (AP) @ [IoU = 0,50:0,95\| area = alle \| maxDets = 100]   | 0.184    | 0.184       | 0.184        | 0.183     | 0.183    |
    | Durchschnittliche Genauigkeit (AP) @ [IoU = 0,50\| area = alle \| maxDets = 100]        | 0.306    | 0.307       | 0.306        | 0.305     | 0.306    |
    | Durchschnittliche Genauigkeit (AP) @ [IoU = 0,75\| area = alle \| maxDets = 100]        | 0.191    | 0.192       | 0.190        | 0.189     | 0.190    |
    | Durchschnittliche Genauigkeit (AP) @ [IoU = 0,50:0,95\| Fläche = klein \| maxDets = 100] | 0.017    | 0.017       | 0.017        | 0.017     | 0.017    |
    | Durchschnittliche Genauigkeit (AP) @ [IoU= 0,50:0,95\| Fläche = mittel \| maxDets = 100] | 0.157    | 0.157       | 0.157        | 0.156     | 0.155    |
    | Durchschnittliche Genauigkeit (AP) @ [IoU = 0,50:0,95\| Fläche = groß \| maxDets = 100] | 0.371    | 0.372       | 0.371        | 0.370     | 0.369    |
    | Durchschnittlicher Rückruf (AR) @ [IoU= 0,50:0,95\| area = alle \| maxDets = 1]         | 0.180    | 0.180       | 0.180        | 0.181     | 0.181    |
    | Durchschnittlicher Rückruf (AR) @ [IoU= 0,50:0,95\| area = alle \| maxDets = 10]        | 0.242    | 0.242       | 0.242        | 0.243     | 0.243    |
    | Durchschnittlicher Rückruf (AR) @ [IoU = 0,50:0,95\| area = alle \| maxDets = 100]      | 0.242    | 0.242       | 0.242        | 0.243     | 0.243    |
    | Durchschnittlicher Rückruf (AR) @ [IoU = 0,50:0,95\| Fläche = klein \| maxDets = 100]    | 0.026    | 0.026       | 0.026        | 0.026     | 0.026    |
    | Durchschnittlicher Rückruf (AR) @ [IoU= 0,50:0,95\| Fläche = mittel \| maxDets = 100]    | 0.206    | 0.206       | 0.206        | 0.206     | 0.205    |
    | Durchschnittlicher Rückruf (AR) @ [IoU = 0,50:0,95\| Fläche = groß \| maxDets = 100]    | 0.489    | 0.491       | 0.490        | 0.490     | 0.491    |

3. YOLOV5S

    | COCOAPI                                                                    | Offizielle Ergebnisse | CPU-Gleitkommagenauigkeit | GNNE-Gleitkommagenauigkeit | uint8 Präzision | int8 Präzision |
    | -------------------------------------------------------------------------- | -------- | ----------- | ------------ | --------- | -------- |
    | Durchschnittliche Genauigkeit (AP) @ [IoU = 0,50:0,95\| area = alle \| maxDets = 100]   | 0.367    | 0.365       | 0.335        | 0.334     | 0.335    |
    | Durchschnittliche Genauigkeit (AP) @ [IoU = 0,50\| area = alle \| maxDets = 100]        | 0.555    | 0.552       | 0.518        | 0.518     | 0.518    |
    | Durchschnittliche Genauigkeit (AP) @ [IoU = 0,75\| area = alle \| maxDets = 100]        | 0.398    | 0.395       | 0.364        | 0.363     | 0.362    |
    | Durchschnittliche Genauigkeit (AP) @ [IoU = 0,50:0,95\| Fläche = klein \| maxDets = 100] | 0.223    | 0.220       | 0.199        | 0.199     | 0.197    |
    | Durchschnittliche Genauigkeit (AP) @ [IoU= 0,50:0,95\| Fläche = mittel \| maxDets = 100] | 0.419    | 0.418       | 0.387        | 0.386     | 0.386    |
    | Durchschnittliche Genauigkeit (AP) @ [IoU = 0,50:0,95\| Fläche = groß \| maxDets = 100] | 0.463    | 0.459       | 0.423        | 0.422     | 0.423    |
    | Durchschnittlicher Rückruf (AR) @ [IoU= 0,50:0,95\| area = alle \| maxDets = 1]         | 0.306    | 0.306       | 0.288        | 0.287     | 0.287    |
    | Durchschnittlicher Rückruf (AR) @ [IoU= 0,50:0,95\| area = alle \| maxDets = 10]        | 0.518    | 0.518       | 0.487        | 0.486     | 0.487    |
    | Durchschnittlicher Rückruf (AR) @ [IoU = 0,50:0,95\| area = alle \| maxDets = 100]      | 0.576    | 0.576       | 0.540        | 0.539     | 0.540    |
    | Durchschnittlicher Rückruf (AR) @ [IoU = 0,50:0,95\| Fläche = klein \| maxDets = 100]    | 0.391    | 0.399       | 0.350        | 0.350     | 0.347    |
    | Durchschnittlicher Rückruf (AR) @ [IoU= 0,50:0,95\| Fläche = mittel \| maxDets = 100]    | 0.641    | 0.640       | 0.606        | 0.605     | 0.607    |
    | Durchschnittlicher Rückruf (AR) @ [IoU = 0,50:0,95\| Fläche = groß \| maxDets = 100]    | 0.716    | 0.710       | 0.680        | 0.683     | 0.685    |

# 8 Häufig gestellte Fragen

1. 安装wheel时报错: "xxx.whl ist kein unterstütztes Rad auf dieser Plattform." **

    Q: 安装nncase wheel包, 出现ERROR: nncase-1.0.0.20210830-cp37-cp37m-manylinux_2_24_x86_64.whl ist kein unterstütztes Rad auf dieser Plattform.

    A: Upgrade-Pip > = 20,3

    ```shell
    sudo pip3 install --upgrade pip
    ```

2. **Wenn das CRB das App-Inferenzprogramm ausführt, meldet es den Fehler "std::bad_alloc"**

    F: Führen Sie das App-Inferenzprogramm auf dem CRB aus, und lösen Sie eine Ausnahme "std::bad_alloc" aus.

    ```shell
    $ ./cpp.sh
    case ./yolov3_bfloat16 build at Sep 16 2021 18:12:03
    terminate called after throwing an instance of 'std::bad_alloc'
    what():  std::bad_alloc
    ```

    A: std::bad_alloc Ausnahmen werden in der Regel durch Fehler bei der Speicherzuweisung verursacht, die wie folgt überprüft werden können.

    - Überprüfen Sie, ob das generierte kmodel den derzeit verfügbaren Systemspeicher überschreitet (z. B. yolov3 bfloat16 kmodel-Größe ist 121MB, der derzeit verfügbare Linux-Speicher ist nur 70MB, die Ausnahme wird ausgelöst).  Wenn dies überschreitet, versuchen Sie, die Quantisierung nach dem Training zu verwenden, um die kmodel-Größe zu reduzieren.
    - Überprüfen Sie die App auf Speicherlecks

3. **Beim Ausführen des App-Inferenzprogramms[.. t_runtime_tensor.cpp:310 (erstellen)] data.size_bytes() == size = false (bool).**

    F: Simulator führt das App-Inferenzprogramm aus und löst eine Ausnahme "[.. t_runtime_tensor.cpp:310 (erstellen)] data.size_bytes() == size = false (bool)" aus

    A: Überprüfen Sie die Eingabetensorinformationen für die Einstellungen und konzentrieren Sie sich dabei auf die Eingabeform und die Anzahl der von jedem Element belegten Bytes (fp32/uint8)

**Haftungsausschluss**für Übersetzungen  
Für die Bequemlichkeit der Kunden verwendet Canaan einen KI-Übersetzer, um Text in mehrere Sprachen zu übersetzen, die Fehler enthalten können. Wir übernehmen keine Gewähr für die Genauigkeit, Zuverlässigkeit oder Aktualität der bereitgestellten Übersetzungen. Canaan haftet nicht für Verluste oder Schäden, die durch das Vertrauen auf die Richtigkeit oder Zuverlässigkeit der übersetzten Informationen verursacht werden. Wenn es einen inhaltlichen Unterschied zwischen den Übersetzungen in verschiedenen Sprachen gibt, ist die vereinfachte chinesische Version maßgebend.

Wenn Sie einen Übersetzungsfehler oder eine Ungenauigkeit melden möchten, können Sie uns gerne per E-Mail kontaktieren.
