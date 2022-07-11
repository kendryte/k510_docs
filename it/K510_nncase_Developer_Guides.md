![canaan-cover.png](http://s2.loli.net/2022/03/30/7UG1IxrOXTo2QKw.png)

**<font face="黑体" size="6" style="float:right">K510 nncase Guida per lo sviluppatore</font>**

<font face="黑体"  size=3>Versione del documento: V1.0.1</font>

<font face="黑体"  size=3>Data di pubblicazione: 2022-05-10</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Disconoscimento**</font>
I prodotti, i servizi o le funzionalità acquistati saranno soggetti ai contratti e ai termini commerciali di Beijing Canaan Jiesi Information Technology Co., Ltd. ("la Società", la stessa di seguito), e tutti o parte dei prodotti, servizi o funzionalità descritti in questo documento potrebbero non rientrare nell'ambito dell'acquisto o dell'utilizzo. Salvo quanto diversamente concordato nel contratto, la Società declina ogni dichiarazione o garanzia, espressa o implicita, in merito all'accuratezza, affidabilità, completezza, marketing, scopo specifico e non aggressione di qualsiasi dichiarazione, informazione o contenuto di questo documento. Salvo diverso accordo, questo documento è fornito solo come guida per l'uso.
A causa di aggiornamenti della versione del prodotto o altri motivi, il contenuto di questo documento può essere aggiornato o modificato di volta in volta senza alcun preavviso.

**<font face="黑体"  size=3>Avvisi sui marchi</font>**

""<img src="http://s2.loli.net/2022/03/30/xN21jbhnwSFyGRD.png" style="zoom:33%;" />, l'icona "Canaan", Canaan e altri marchi di Canaan e altri marchi di Canaan sono marchi di Beijing Canaan Jiesi Information Technology Co., Ltd. Tutti gli altri marchi o marchi registrati che possono essere menzionati in questo documento sono di proprietà dei rispettivi proprietari.

**<font face="黑体"  size=3>Copyright ©2022 Pechino Canaan Jiesi Information Technology Co., Ltd</font>**
Questo documento è applicabile solo allo sviluppo e alla progettazione della piattaforma K510, senza il permesso scritto della società, nessuna unità o individuo può diffondere parte o tutto il contenuto di questo documento in qualsiasi forma.

**<font face="黑体"  size=3>Pechino Canaan Jiesi Information Technology Co., Ltd</font>**
URL: canaan-creative.com
Richieste commerciali: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# prefazione
**<font face="黑体"  size=5>Scopo </font>**del documento
Questo documento è un documento di descrizione per l'uso del compilatore nncase/K510, che fornisce agli utenti come installare nncase, come chiamare le API del compilatore per compilare modelli di rete neurale e le API di runtime per scrivere programmi di inferenza AI

**<font face="黑体"  size=5>Oggetti lettore</font>**

Le principali persone a cui si applica questo documento (questa guida):

- Sviluppatori di software
- Personale di supporto tecnico

**<font face="黑体"  size=5>Termini e acronimi</font>**

| termine | Spiegazione/nome completo                              |
| ---- | -------------------------------------- |
| PTQ ·  | Quantizzazione post-allenamento, quantizzazione post-allenamento |
| MSE  | errore medio-quadrato, errore medio quadrato            |
|      |                                        |

**<font face="黑体"  size=5>Cronologia delle revisioni</font>**
 <font face="宋体"  size=2>La cronologia delle revisioni accumula una descrizione di ogni aggiornamento del documento. La versione più recente del documento contiene gli aggiornamenti per tutte le versioni precedenti. </font>

| Il numero di versione   | Modificato da     | Data della revisione | Note di revisione |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.1 | Pubblicità | 2022-05-10 | nncase_v1.6.1 |
| V1.0.0 · | Zhang Yang/Zhang Jizhao/Yang Haoqi | 2022-05-06 | nncase_v1.6.0 |
| V0.9.0 | Pubblicità | 2022-04-01 | nncase_v1.5.0 |
| V0.8,0 | Zhang Yang/Zhang Jizhao | 2022-03-03 | nncase_v1.4.0 |
| V0.7,0 | Pubblicità | 2022-01-28 | nncase_v1.3.0 |
| V0.6.0 | Pubblicità | 2021-12-31 | nncase_v1.2.0 |
| V0.5,0 | Pubblicità | 2021-12-03 | nncase_v1.1.0 |
| V0.4.0 | Zhang Yang/Haoqi Yang/Zheng Qihang | 2021-10-29 | nncase_v1.0.0 |
| V0.3.0 | Zhang Yang / Yang Haoqi | 2021-09-28 | nncase_v1.0.0_rc1 |
| V0.2.0 | Zhang Yang / Yang Haoqi | 2021-09-02 | nncase_v1.0.0_beta2 |
| V0.1.0 | Zhang Yang / Yang Haoqi | 2021-08-31 | nncase_v1.0.0_beta1 |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenuto</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Introduzione all'ambiente di sviluppo

## 1.1 Sistema operativo

- Ubuntu 18.04/20.04

## 1.2 Ambiente software

I requisiti dell'ambiente software sono illustrati nella tabella seguente:

| numero di serie | Risorse software        | illustrare                        |
| ---- | --------------- | --------------------------- |
| 1    | Pitone          | Python 3.6/3.7/3.8/3.9/3.10 |
| 2    | pip3 ·            | > versione pip3 = 20.3            |
| 3    | onnx            | La versione onnx è 1.9.0             |
| 4    | onnx-semplificare | La versione onnx-simplifier è 0.3.6  |
| 5    | onnxoptimizer   | La versione di onnxoptimizer è 0.2.6    |

## 1.3 Ambiente hardware

I requisiti dell'ambiente hardware sono illustrati nella tabella seguente:

| numero di serie | Risorse hardware     | illustrare |
| ---- | ------------ | ---- |
| 1    | K510 CRB     |      |
| 2    | Scheda SD e lettore di schede |      |

# 2 introduzione a nncase

## 2.1 Cos'è nncase

nncase è un compilatore di reti neurali progettato per acceleratori AI e attualmente supporta target come CPU / K210 / K510

Caratteristiche fornite da nncase

- Supporta più reti di input e più output, supporta la struttura multi-ramo
- Allocazione di memoria statica, non è richiesta memoria heap
- Fusione e ottimizzazione degli operatori
- Supporta l'inferenza di quantizzazione float e uint8/int8
- Supporta la quantizzazione post-addestramento, utilizzando modelli a virgola mobile e set di calibrazione della quantizzazione
- Modello piatto con supporto per il caricamento della copia zero

Framework di rete neurale supportato da nncase

- tflite
- onnx
- caffè

## 2.2 Vantaggi del prodotto

- **Distribuzione end-to-end semplice**

  Riduci il numero di interazioni con gli utenti. La distribuzione su KPU può essere eseguita utilizzando e distribuendo gli stessi strumenti e processi per i modelli CPU e GPU. Non è necessario impostare parametri complessi, abbassare la soglia di utilizzo e accelerare il ciclo di iterazione degli algoritmi di intelligenza artificiale.
- **Sfrutta appieno l'ecosistema AI esistente**

  Collegato a un quadro ampiamente utilizzato nel settore. Da un lato, può migliorare la sua visibilità e godere dei dividendi di un'ecologia matura. D'altra parte, i costi di sviluppo degli sviluppatori di piccole e medie dimensioni possono essere ridotti e i modelli e gli algoritmi maturi nel settore possono essere distribuiti direttamente.
- **Ottieni il massimo dal tuo hardware**

  Il vantaggio di NPU è che le prestazioni sono superiori a quelle di CPU e GPU e il compilatore DL deve essere in grado di utilizzare appieno le prestazioni dell'hardware. Il compilatore deve anche ottimizzare in modo adattivo le prestazioni per la nuova struttura del modello, quindi è necessario esplorare una nuova tecnica di ottimizzazione automatica oltre all'ottimizzazione manuale.
- **Scalabilità e manutenibilità**

  Capacità di supportare le implementazioni di modelli di intelligenza artificiale per K210, K510 e chip futuri. È necessario fornire una certa scalabilità a livello di architettura. L'aggiunta di un nuovo Target è meno costosa e consente di riutilizzare il maggior numero possibile di moduli. Accelerare lo sviluppo di nuovi prodotti per ottenere l'accumulo tecnologico di DL Compiler.

## 2.3 Architettura nncase

<img src="https://i.loli.net/2021/08/18/IQR12SOJdzxTUZH.png" alt="nncase_arch.png" style="zoom:67%;" />

Lo stack software nnncase è attualmente costituito da due parti: compilatore e runtime.

**Compilatore:** utilizzato per compilare modelli di reti neurali su un PC ed eventualmente generare un file kmodel. Include principalmente importatore, IR, valutatore, quantizzare, trasformare l'ottimizzazione, tiling, partizione, pianificazione, Codegen e altri moduli.

- Importatore: importa modelli da altri framework di reti neurali in nncase
- IR: rappresentazione centrale, suddivisa in IR neutro importato dall'importatore (indipendente dal dispositivo) e IR Nutral generato abbassando l'IR target di conversione (dipendente dal dispositivo)
- Valutatore: il valutatore fornisce l'esecuzione interpretativa dell'IR ed è spesso utilizzato in scenari come la piegatura costante / calibrazione PTQ
- Trasformazione: per la trasformazione IR e l'ottimizzazione dell'attraversamento del grafo, ecc.
- Quantizzare: quantizzare dopo l'addestramento, aggiungere marcatori di quantizzazione al tensore da quantizzare, chiamare Evaluator per l'esecuzione dell'interpretazione in base al set di correzione dell'input, raccogliere l'intervallo di dati tensoriali, inserire nodi di quantizzazione / dequantizzazione e infine ottimizzare per eliminare i nodi di quantizzazione / dequantizzazione non necessari, ecc.
- Tiling: Limitato dalla minore capacità di memoria della NPU, è necessario dividere grandi blocchi di calcolo. Inoltre, la selezione del parametro Tilling quando nel calcolo è presente una grande quantità di multiplexing dei dati avrà un impatto sulla latenza e sulla larghezza di banda
- Partizione: Dividi il grafico per ModuleType, ogni sottografo dopo la suddivisione corrisponderà a RuntimeModule, diversi tipi di RuntimeModule corrispondono a diversi dispositivi (cpu / K510)
- Pianificazione: genera un ordine di calcolo e alloca i buffer in base alle dipendenze dei dati nel grafico ottimizzato
- Codegen: chiamare il codegen corrispondente a ModuleType per ogni sottografo per generare RuntimeModule

**Runtime**: integrato nell'app utente, fornisce funzioni come il caricamento di kmodel / l'impostazione dei dati di input, l'esecuzione KPU e l'ottenimento di dati di output

# 3 Installare nncase

La parte del compilatore della toolchain nncase include il compilatore nncase e K510, entrambi i quali devono installare il pacchetto wheel corrispondente.

- Il pacchetto nncase wheel è stato[rilasciato su nncase github](https://github.com/kendryte/nncase/releases/tag/v1.6.0), supportando Python 3.6/3.7/3.8/3.9/3.10, gli utenti possono scegliere la versione corrispondente da scaricare in base al sistema operativo e Python
- Il pacchetto ruota del compilatore K510 si trova nella directory x86_64 dell'SDK nncase, non dipende dalla versione python e può essere installato direttamente

Se non si dispone di un ambiente Ubuntu, è possibile utilizzare[nncase docker](https://github.com/kendryte/nncase/blob/master/docs/build.md#docker)(Ubuntu 20.04 + Python 3.8).

```shell
cd /path/to/nncase_sdk
docker pull registry.cn-hangzhou.aliyuncs.com/kendryte/nncase:latest
docker run -it --rm -v `pwd`:/mnt -w /mnt registry.cn-hangzhou.aliyuncs.com/kendryte/nncase:latest /bin/bash -c "/bin/bash"
```

Quanto segue prende Ubuntu 20.04 + Python 3.8 installazione di nncase come esempio

```shell
wget -P x86_64 https://github.com/kendryte/nncase/releases/download/v1.6.0/nncase-1.6.0.20220505-cp38-cp38-manylinux_2_24_x86_64.whl
pip3 install x86_64/*.whl
```
<!-- markdownlint-disable no-emphasis-as-header -->
# 4 Modello di compilazione/inferenza

nncase fornisce**l'API Python**per la compilazione/inferenza di modelli di deep learning su un PC

## 4.1 Operatori supportati

### 4.1.1 Operatore tflite

| Operatore                | È supportato |
| ----------------------- | ------------ |
| ABS                     | ✅            |
| AGGIUNGERE                     | ✅            |
| ARG_MAX                 | ✅            |
| ARG_MIN                 | ✅            |
| AVERAGE_POOL_2D         | ✅            |
| BATCH_MATMUL            | ✅            |
| GETTARE                    | ✅            |
| CEIL                    | ✅            |
| CONCATENAZIONE           | ✅            |
| CONV_2D                 | ✅            |
| CORPO                     | ✅            |
| COSTUME                  | ✅            |
| DEPTHWISE_CONV_2D       | ✅            |
| DIV                     | ✅            |
| UGUALE                   | ✅            |
| EXP                     | ✅            |
| EXPAND_DIMS             | ✅            |
| PAVIMENTO                   | ✅            |
| FLOOR_DIV               | ✅            |
| FLOOR_MOD               | ✅            |
| FULLY_CONNECTED         | ✅            |
| MAGGIORE                 | ✅            |
| GREATER_EQUAL           | ✅            |
| L2_NORMALIZATION        | ✅            |
| LEAKY_RELU              | ✅            |
| MENO                    | ✅            |
| LESS_EQUAL              | ✅            |
| REGISTRO                     | ✅            |
| LOGISTICO                | ✅            |
| MAX_POOL_2D             | ✅            |
| MASSIMO                 | ✅            |
| SIGNIFICARE                    | ✅            |
| MINIMO                 | ✅            |
| Io                     | ✅            |
| NEG                     | ✅            |
| NOT_EQUAL               | ✅            |
| BLOCCO                     | ✅            |
| PADV2 ·                   | ✅            |
| MIRROR_PAD              | ✅            |
| BRANCO                    | ✅            |
| PRIGIONIERO DI GUERRA                     | ✅            |
| REDUCE_MAX              | ✅            |
| REDUCE_MIN              | ✅            |
| REDUCE_PROD             | ✅            |
| RELU ·                    | ✅            |
| PRELU ·                   | ✅            |
| RELU6 ·                   | ✅            |
| RISTRUTTURARE                 | ✅            |
| RESIZE_BILINEAR         | ✅            |
| RESIZE_NEAREST_NEIGHBOR | ✅            |
| ROTONDO                   | ✅            |
| RSQRT                   | ✅            |
| FORMA                   | ✅            |
| SENZA                     | ✅            |
| FETTA                   | ✅            |
| SOFTMAX ·                 | ✅            |
| SPACE_TO_BATCH_ND       | ✅            |
| SPREMERE                 | ✅            |
| BATCH_TO_SPACE_ND       | ✅            |
| STRIDED_SLICE           | ✅            |
| SQRT                    | ✅            |
| QUADRATO                  | ✅            |
| SUB                     | ✅            |
| SOMMA                     | ✅            |
| SOSPETTO                    | ✅            |
| TEGOLA                    | ✅            |
| TRASPORRE               | ✅            |
| TRANSPOSE_CONV          | ✅            |
| QUANTIZZARE                | ✅            |
| FAKE_QUANT              | ✅            |
| DEQUANTIZE              | ✅            |
| RACCOGLIERE                  | ✅            |
| GATHER_ND               | ✅            |
| ONE_HOT                 | ✅            |
| SQUARED_DIFFERENCE      | ✅            |
| LOG_SOFTMAX             | ✅            |
| DIVISO                   | ✅            |
| HARD_SWISH              | ✅            |

### 4.1.2 Operatore onnx

| Operatore              | È supportato |
| --------------------- | ------------ |
| Abs                   | ✅            |
| Acos ·                  | ✅            |
| Acosh ·                 | ✅            |
| E                   | ✅            |
| ArgMax ·                | ✅            |
| ArgMin ·                | ✅            |
| Salato                  | ✅            |
| Asinh ·                 | ✅            |
| Aggiungere                   | ✅            |
| Piscina Media           | ✅            |
| BatchNormalizzazione    | ✅            |
| Gettare                  | ✅            |
| Ceil                  | ✅            |
| A                  | ✅            |
| Morsetto                  | ✅            |
| Concat ·                | ✅            |
| Costante              | ✅            |
| ConstantOfShape       | ✅            |
| Conv                  | ✅            |
| ConvTrasposizione         | ✅            |
| Corpo                   | ✅            |
| Manganello                  | ✅            |
| CumSum                | ✅            |
| DepthToSpace          | ✅            |
| DequantizeLinear      | ✅            |
| Div                   | ✅            |
| Abbandono degli studi               | ✅            |
| Vita                   | ✅            |
| Exp                   | ✅            |
| Espandere                | ✅            |
| Uguale                 | ✅            |
| Appiattire               | ✅            |
| Pavimento                 | ✅            |
| Raccogliere                | ✅            |
| GatherND              | ✅            |
| Gemm ·                  | ✅            |
| GlobalAveragePool     | ✅            |
| GlobalMaxPool         | ✅            |
| Maggiore               | ✅            |
| GreaterOrEqual        | ✅            |
| Hardmax ·               | ✅            |
| HardSigmoid           | ✅            |
| HardSwish             | ✅            |
| Identità              | ✅            |
| Metodo InstanceNormalization | ✅            |
| LpNormalizzazione       | ✅            |
| LeakyRelu             | ✅            |
| Meno                  | ✅            |
| LessOrEqual           | ✅            |
| Registro                   | ✅            |
| LogSoftmax            | ✅            |
| LRN ·                   | ✅            |
| LSTM ·                  | ✅            |
| MatMul                | ✅            |
| Piscina Max               | ✅            |
| Max                   | ✅            |
| Min                   | ✅            |
| Io                   | ✅            |
| Neg                   | ✅            |
| Non                   | ✅            |
| OneHot                | ✅            |
| Blocco                   | ✅            |
| Prigioniero di guerra                   | ✅            |
| PRelu ·                 | ✅            |
| QuantizeLinear        | ✅            |
| RandomNormal          | ✅            |
| RandomNormalMi piace      | ✅            |
| RandomUniform         | ✅            |
| RandomUniformLike     | ✅            |
| RiduciL1              | ✅            |
| RiduciL2              | ✅            |
| ReduceLogSum          | ✅            |
| ReduceLogSumExp       | ✅            |
| ReduceMax             | ✅            |
| RiduciMi            | ✅            |
| ReduceMin             | ✅            |
| ReduceProd            | ✅            |
| ReduceSum             | ✅            |
| ReduceSumSquare       | ✅            |
| Relu ·                  | ✅            |
| Ristrutturare               | ✅            |
| Ridimensionare                | ✅            |
| ReverseSequence       | ✅            |
| RoiAlign              | ✅            |
| Rotondo                 | ✅            |
| Villaggio                  | ✅            |
| Forma                 | ✅            |
| Segno                  | ✅            |
| Senza                   | ✅            |
| Nascita                  | ✅            |
| Sigmoideo               | ✅            |
| Grandezza                  | ✅            |
| Fetta                 | ✅            |
| Softmax ·               | ✅            |
| Softplus ·              | ✅            |
| Softsign ·              | ✅            |
| SpaceToDepth          | ✅            |
| Diviso                 | ✅            |
| Sqrt                  | ✅            |
| Spremere               | ✅            |
| Sub                   | ✅            |
| Somma                   | ✅            |
| Sospetto                  | ✅            |
| Tegola                  | ✅            |
| TopK ·                  | ✅            |
| Trasporre             | ✅            |
| Trilu ·                 | ✅            |
| Upsample              | ✅            |
| Spremere             | ✅            |
| Dove                 | ✅            |

### 4.1.3 Operatore caffe

| Operatore              | È supportato |
| --------------------- | ------------ |
| Immissione                 | ✅            |
| Concat ·                | ✅            |
| Convoluzione           | ✅            |
| Eltwise               | ✅            |
| Permute               | ✅            |
| relu                  | ✅            |
| Ristrutturare               | ✅            |
| Fetta                 | ✅            |
| Softmax ·               | ✅            |
| Diviso                 | ✅            |
| ContinuazioneIndicatore | ✅            |
| Pool               | ✅            |
| BatchNorm             | ✅            |
| Scala                 | ✅            |
| Inverso               | ✅            |
| LSTM ·                  | ✅            |
| Prodotto interno          | ✅            |

## 4.2 Compilare le API del modello

Allo stato attuale, l'API del modello di compilazione supporta framework di deep learning come tflite / onnx / caffe.

### 4.2.1 CompileOptions

**Descrizione della caratteristica**

Classe CompileOptions per la configurazione delle opzioni di compilazione nncase

**Definizione della classe**

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

Ogni proprietà è descritta di seguito

| Nome della proprietà         | digitare   | Sì o No | descrizione                                                         |
| ---------------- | ------ | -------- | ------------------------------------------------------------ |
| bersaglio           | corda | essere       | Specificare la destinazione di compilazione, ad esempio 'k210', 'k510'                               |
| quant_type       | corda | non       | Specificare il tipo di quantizzazione dei dati, ad esempio 'uint8', 'int8'                          |
| w_quant_type     | corda | non       | Specificare il tipo di quantizzazione del peso, ad esempio 'uint8', 'int8', per impostazione predefinita su 'uint8'           |
| use_mse_quant_w  | Bool   | non       | Specifica se utilizzare l'algoritmo MSE (Mean Square Error) per ottimizzare i parametri di quantizzazione durante la quantizzazione dei pesi |
| split_w_to_act   | Bool   | non       | Specifica se bilanciare i dati di peso parziale in dati attivi                       |
| pre-elaborazione       | Bool   | non       | Indipendentemente dal fatto che la pre-elaborazione sia abilitata o meno, l'impostazione predefinita è False                                  |
| swapRB           | Bool   | non       | Se scambiare dati di input RGB tra i canali rosso e blu (RGB--> BGR o BGR->RGB), l'impostazione predefinita è False |
| Significare             | lista   | non       | La pre-elaborazione normalizza la media del parametro, che per impostazione predefinita è[0, 0, 0]                        |
| Std              | lista   | non       | La pre-elaborazione normalizza la varianza dei parametri, che per impostazione predefinita è[1, 1, 1]                        |
| input_range      | lista   | non       | Intervallo di numeri a virgola mobile dopo la dequantizzazione dei dati di input, che per impostazione predefinita è[0，1]               |
| output_range     | lista   | non       | Intervallo di numeri a virgola mobile prima dell'output dei dati a virgola fissa, che per impostazione predefinita è vuoto                     |
| input_shape      | lista   | non       | Specificare la forma dei dati di input, il layout del input_shape deve essere coerente con il layout di input e la input_shape dei dati di input è incoerente con la forma di input del modello e verrà eseguita l'operazione bitbox (ridimensionamento/pad, ecc.). |
| letterbox_value  | galleggiare  | non       | Specifica il valore di riempimento della fetchbox di pre-elaborazione                                  |
| input_type       | corda | non       | Specifica il tipo di dati di input, il valore predefinito è 'float32'                          |
| output_type      | corda | non       | Specifica il tipo di dati di output, ad esempio 'float32', 'uint8' (solo per la quantizzazione specificata), per impostazione predefinita su 'float32' |
| input_layout     | corda | non       | Specificare il layout dei dati di input, ad esempio 'NCHW', 'NHWC'. Se il layout dei dati di input è diverso dal modello stesso, gli inserti nncase traspongono per la conversione |
| output_layout    | corda | non       | Specificare i dati di output per il layout, ad esempio 'NCHW', 'NHWC'. Se il layout dei dati di output è diverso dal modello stesso, nncase inserirà transpose per la conversione |
| model_layout     | corda | non       | Specificare il layout del modello, che per impostazione predefinita è vuoto, e specifica quando il layout del modello tflite è 'NCHW' e i modelli Onnx e Caffe sono 'NHWC' |
| is_fpga          | Bool   | non       | Specifica se kmodel viene utilizzato per gli FPGA, che per impostazione predefinita è False                          |
| dump_ir          | Bool   | non       | Specifica se dump IR, impostazione predefinita su False                                 |
| dump_asm         | Bool   | non       | Specifica se il file di assieme asm di dump, che per impostazione predefinita è False                        |
| dump_quant_error | Bool   | non       | Specifica se il dump quantizza l'errore del modello prima e dopo                               |
| dump_dir         | corda | non       | Dopo aver specificato in precedenza il dump_ir e altre opzioni, qui si specifica la directory di dump, che per impostazione predefinita è una stringa vuota  |
| benchmark_only   | Bool   | non       | Specifica se kmodel viene utilizzato solo per il benchmark, che per impostazione predefinita è False                   |

> 1. L'intervallo di input è l'intervallo di numeri a virgola mobile, cioè se il tipo di dati di input è uint8, l'intervallo di input è l'intervallo dopo la dequantizzazione in virgola mobile (non può essere 0 ~ 1), che può essere specificato liberamente.
> 2. input_shape devono essere specificati in base alla input_layout, [1，224，224，3]ad esempio, se il input_layout è NCHW, il input_shape deve essere specificato come[1,3,224,224]; input_layout è NHWC, il input_shape deve essere specificato come[1,224,224,3];
> 3. mean e std sono parametri per normalizzare i numeri a virgola mobile, che l'utente è libero di specificare;
> 4. Quando si utilizza la funzione letterbox, è necessario limitare la dimensione dell'input a 1,5 MB e la dimensione di un singolo canale è compresa tra 0,75 MB;
>
> Per esempio:
>
> 1. Il tipo di dati di input è impostato su uint8, input_range impostato su[0,255], il ruolo della dequantizzazione è solo quello di convertire il tipo, convertire i dati di uint8 in float32 e i parametri media e std possono ancora essere specificati in base ai dati di 0 ~ 255
> 2. Il tipo di dati di input è impostato su uint8, input_range impostato [0,1]su, il numero a virgola fissa viene dequantizzato in un numero a [0,1]virgola mobile nell'intervallo e la media e std devono essere specificati in base al nuovo intervallo di numeri a virgola mobile.

Il processo di pre-elaborazione è il seguente (i nodi verdi nella figura sono facoltativi):

![pre-elaborazione.png](https://i.loli.net/2021/11/08/fhBLsozUTCbt4dp.png)

**Esempio di codice**

Crea un'istanza di CompileOptions, configura i valori di ogni proprietà

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

**Descrizione della caratteristica**

Classe ImportOptions per la configurazione delle opzioni di importazione nncase

**Definizione della classe**

```python
py::class_<import_options>(m, "ImportOptions")
    .def(py::init())
    .def_readwrite("output_arrays", &import_options::output_arrays);
```

Ogni proprietà è descritta di seguito

| Nome della proprietà      | digitare   | Sì o No | descrizione     |
| ------------- | ------ | -------- | -------- |
| output_arrays | corda | non       | Nome di output |

**Esempio di codice**

Crea un'istanza di ImageOptions, configura i valori di ogni proprietà

```python
# import_options
import_options = nncase.ImportOptions()
import_options.output_arrays = 'output' # Your output node name
```

### 4.2.3 PTQTensorOptions

**Descrizione della caratteristica**

Classe PTQTensorOptions per la configurazione delle opzioni PTQ nncase

**Definizione della classe**

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

Ogni proprietà è descritta di seguito

| Il nome del campo         | digitare   | Sì o No | descrizione                                                                                  |
| ---------------- | ------ | -------- | ------------------------------------------------------------------------------------- |
| calibrate_method | corda | non       | Metodo di calibrazione , supporta 'no_clip', 'l2', 'kld_m0', 'kld_m1', 'kld_m2', 'cdf', il valore predefinito è 'no_clip' |
| samples_count    | Int    | non       | Il numero di campioni                                                                              |

#### set_tensor_data()

**Descrizione della caratteristica**

Impostare i dati di correzione

**Definizione dell'interfaccia**

```python
set_tensor_data(calib_data)
```

**Parametri di input**

| Nome parametro   | digitare   | Sì o No | descrizione     |
| ---------- | ------ | -------- | -------- |
| calib_data | byte[] | essere       | Correggere i dati |

**Il valore restituito**

N/D

**Esempio di codice**

```python
# ptq_options
ptq_options = nncase.PTQTensorOptions()
ptq_options.samples_count = cfg.generate_calibs.batch_size
ptq_options.set_tensor_data(np.asarray([sample['data'] for sample in self.calibs]).tobytes())
```

### 4.2.4 Compilatore

**Descrizione della caratteristica**

Classe del compilatore per la compilazione di modelli di reti neurali

**Definizione della classe**

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

**Esempio di codice**

```python
compiler = nncase.Compiler(compile_options)
```

#### import_tflite()

**Descrizione della caratteristica**

Importare il modello tflite

**Definizione dell'interfaccia**

```python
import_tflite(model_content, import_options)
```

**Parametri di input**

| Nome parametro       | digitare          | Sì o No | descrizione           |
| -------------- | ------------- | -------- | -------------- |
| model_content  | byte[]        | essere       | Leggi il contenuto del modello |
| import_options | ImportOptions | essere       | Opzioni di importazione       |

**Il valore restituito**

N/D

**Esempio di codice**

```python
model_content = read_model_file(model)
compiler.import_tflite(model_content, import_options)
```

#### import_onnx()

**Descrizione della caratteristica**

Importare il modello onnx

**Definizione dell'interfaccia**

```python
import_onnx(model_content, import_options)
```

**Parametri di input**

| Nome parametro       | digitare          | Sì o No | descrizione           |
| -------------- | ------------- | -------- | -------------- |
| model_content  | byte[]        | essere       | Leggi il contenuto del modello |
| import_options | ImportOptions | essere       | Opzioni di importazione       |

**Il valore restituito**

N/D

**Esempio di codice**

```python
model_content = read_model_file(model)
compiler.import_onnx(model_content, import_options)
```

#### import_caffe()

**Descrizione della caratteristica**

Importare il modello caffe

> Gli utenti devono compilare / installare caffe sul computer locale.

**Definizione dell'interfaccia**

```python
import_caffe(caffemodel, prototxt)
```

**Parametri di input**

| Nome parametro   | digitare   | Sì o No | descrizione                 |
| ---------- | ------ | -------- | -------------------- |
| caffemodel | byte[] | essere       | Leggi il contenuto del caffemodel |
| prototxt   | byte[] | essere       | Leggi il contenuto di prototxt   |

**Il valore restituito**

N/D

**Esempio di codice**

```python
# import
caffemodel = read_model_file('test.caffemodel')
prototxt = read_model_file('test.prototxt')
compiler.import_caffe(caffemodel, prototxt)
```

#### use_ptq()

**Descrizione della caratteristica**

Impostare le opzioni di configurazione PTQ

**Definizione dell'interfaccia**

```python
use_ptq(ptq_options)
```

**Parametri di input**

| Nome parametro    | digitare             | Sì o No | descrizione        |
| ----------- | ---------------- | -------- | ----------- |
| ptq_options | PTQTensorOptions | essere       | Opzioni di configurazione PTQ |

**Il valore restituito**

N/D

**Esempio di codice**

```python
compiler.use_ptq(ptq_options)
```

#### compile()

**Descrizione della caratteristica**

Compilare il modello di rete neurale

**Definizione dell'interfaccia**

```python
compile()
```

**Parametri di input**

N/D

**Il valore restituito**

N/D

**Esempio di codice**

```python
compiler.compile()
```

#### gencode_tobytes()

**Descrizione della caratteristica**

Genera un flusso di byte di codice

**Definizione dell'interfaccia**

```python
gencode_tobytes()
```

**Parametri di input**

N/D

**Il valore restituito**

Byte[]

**Esempio di codice**

```python
kmodel = compiler.gencode_tobytes()
with open(os.path.join(infer_dir, 'test.kmodel'), 'wb') as f:
    f.write(kmodel)
```

## 4.3 Compilare l'esempio di modello

Nell'esempio seguente viene utilizzato lo script di compilazione model e python

- Il modello si trova nella sottodirectory /path/to/nncase_sdk/examples/models/subdirectory
- Lo script di compilazione python si trova nella sottodirectory /path/to/nncase_sdk/examples/scripts

### 4.3.1 Compilare il modello float32 tflite

- Mobilenetv2_tflite_fp32_image.py script è il seguente

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

- Eseguire il comando seguente per compilare il modello tflite di mobiletv2, target k510

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_tflite_fp32_image.py --target k510 --model models/mobilenet_v2_1.0_224.tflite
```

### 4.3.2 Compilare il modello float32 onnx

- Per i modelli onnx, si consiglia di semplificare l'utilizzo di[ONNX Simplifier](https://github.com/daquexian/onnx-simplifier)prima di compilare con nncase
- mobilenetv2_onnx_fp32_image.py script è il seguente

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

- Eseguire il comando seguente per compilare il modello onnx di mobiletv2, target k510

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_onnx_fp32_image.py --target k510 --model models/mobilenetv2-7.onnx
```

### 4.3.3 Compilare il modello di caffe float32

- Il pacchetto della ruota del caffè è[preso dal](https://github.com/kendryte/caffe/releases)caffè kendryte
- conv2d_caffe_fp32.py script è il seguente

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

- Eseguire il comando seguente per compilare il modello caffe di conv2d, con la destinazione k510

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/conv2d_caffe_fp32.py --target k510 --caffemodel models/test.caffemodel --prototxt models/test.prototxt
```

### 4.3.4 Compilare e aggiungere il modello float32 onnx pre-processo

- Per i modelli onnx, si consiglia di semplificare l'utilizzo di[ONNX Simplifier](https://github.com/daquexian/onnx-simplifier)prima di compilare con nncase
- Mobilenetv2_onnx_fp32_preprocess.py script è il seguente

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

- Eseguire il seguente comando per compilare il modello onnx di mobiletv2 con la destinazione k510

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_onnx_fp32_preprocess.py --target k510 --model models/mobilenetv2-7.onnx
```

### 4.3.5 Compilare il modello tflite di quantizzazione uint8

- Mobilenetv2_tflite_uint8_image.py script è il seguente

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

- Eseguire il comando seguente per compilare il modello tflite di uint8 quantized mobiletv2, target k510

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_tflite_uint8_image.py --target k510 --model models/mobilenet_v2_1.0_224.tflite
```

## 4.4 API del modello di inferenza

Oltre agli AP del modello compilato, nncase fornisce anche le API del modello di inferenza, che possono essere dedotte sul PC prima della compilazione del kmodel, che viene utilizzato per verificare se i risultati dell'inferenza nncase e i risultati di runtime del framework di deep learning corrispondente sono coerenti.

### 4.4.1 MemoryRange

**Descrizione della caratteristica**

Classe MemoryRange, utilizzata per rappresentare un intervallo di memoria

**Definizione della classe**

```python
py::class_<memory_range>(m, "MemoryRange")
    .def_readwrite("location", &memory_range::memory_location)
    .def_property(
        "dtype", [](const memory_range &range) { return to_dtype(range.datatype); },
        [](memory_range &range, py::object dtype) { range.datatype = from_dtype(py::dtype::from_args(dtype)); })
    .def_readwrite("start", &memory_range::start)
    .def_readwrite("size", &memory_range::size);
```

Ogni proprietà è descritta di seguito

| Nome della proprietà | digitare           | Sì o No | descrizione                                                                       |
| -------- | -------------- | -------- | -------------------------------------------------------------------------- |
| ubicazione | Int            | non       | Posizione della memoria, 0 per l'ingresso, 1 per l'uscita, 2 per i dati, 3 per i dati, 4 per shared_data |
| dtype    | Tipo di dati Python | non       | tipo di dati                                                                   |
| inizio    | Int            | non       | Indirizzo di avvio della memoria                                                               |
| grandezza     | Int            | non       | Dimensione della memoria                                                                   |

**Esempio di codice**

Creazione di un'istanza di MemoryRange

```python
mr = nncase.MemoryRange()
```

### 4.4.2 RuntimeTensor

**Descrizione della caratteristica**

La classe RuntimeTensor, che rappresenta il tensore di runtime

**Definizione della classe**

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

Ogni proprietà è descritta di seguito

| Nome della proprietà | digitare | Sì o No | descrizione             |
| -------- | ---- | -------- | ---------------- |
| dtype    | Int  | non       | Tipo di dati di Tensor |
| forma    | lista | non       | La forma del tensore     |

#### from_numpy()

**Descrizione della caratteristica**

Costruire l'oggetto RuntimeTensor da numpy.ndarray

**Definizione dell'interfaccia**

```python
from_numpy(py::array arr)
```

**Parametri di input**

| Nome parametro | digitare          | Sì o No | descrizione              |
| -------- | ------------- | -------- | ----------------- |
| Arr      | numpy.ndarray | essere       | oggetto numpy.ndarray |

**Il valore restituito**

Metodo runtimeTensor

**Esempio di codice**

```python
tensor = nncase.RuntimeTensor.from_numpy(self.inputs[i]['data'])
```

#### copy_to()

**Descrizione della caratteristica**

Copia tensore di runtime

**Definizione dell'interfaccia**

```python
copy_to(RuntimeTensor to)
```

**Parametri di input**

| Nome parametro | digitare          | Sì o No | descrizione              |
| -------- | ------------- | -------- | ----------------- |
| A       | Metodo runtimeTensor | essere       | Oggetto RuntimeTensor |

**Il valore restituito**

N/D

**Esempio di codice**

```python
sim.get_output_tensor(i).copy_to(to)
```

#### to_numpy()

**Descrizione della caratteristica**

Convertire RuntimeTensor in un oggetto numpy.ndarray

**Definizione dell'interfaccia**

```python
to_numpy()
```

**Parametri di input**

N/D

**Il valore restituito**

oggetto numpy.ndarray

**Esempio di codice**

```python
arr = sim.get_output_tensor(i).to_numpy()
```

### 4.4.3 Simulatore

**Descrizione della caratteristica**

Classe simulatore per inferenza kmodel su PC

**Definizione della classe**

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

Ogni proprietà è descritta di seguito

| Nome della proprietà     | digitare | Sì o No | descrizione     |
| ------------ | ---- | -------- | -------- |
| inputs_size  | Int  | non       | Inserisci il numero di |
| outputs_size | Int  | non       | Il numero di uscite |

**Esempio di codice**

Crea un'istanza del simulatore

```python
sim = nncase.Simulator()
```

#### load_model()

**Descrizione della caratteristica**

Carica il kmodel

**Definizione dell'interfaccia**

```python
load_model(model_content)
```

**Parametri di input**

| Nome parametro      | digitare   | Sì o No | descrizione         |
| ------------- | ------ | -------- | ------------ |
| model_content | byte[] | essere       | Flusso di byte Kmodel |

**Il valore restituito**

N/D

**Esempio di codice**

```python
sim.load_model(kmodel)
```

#### get_input_desc()

**Descrizione della caratteristica**

Ottiene la descrizione dell'input per l'indice specificato

**Definizione dell'interfaccia**

```python
get_input_desc(index)
```

**Parametri di input**

| Nome parametro | digitare | Sì o No | descrizione       |
| -------- | ---- | -------- | ---------- |
| indice    | Int  | essere       | L'indice dell'input |

**Il valore restituito**

Metodo MemoryRange

**Esempio di codice**

```python
input_desc_0 = sim.get_input_desc(0)
```

#### get_output_desc()

**Descrizione della caratteristica**

Ottiene la descrizione dell'output dell'indice specificato

**Definizione dell'interfaccia**

```python
get_output_desc(index)
```

**Parametri di input**

| Nome parametro | digitare | Sì o No | descrizione       |
| -------- | ---- | -------- | ---------- |
| indice    | Int  | essere       | L'indice dell'output |

**Il valore restituito**

Metodo MemoryRange

**Esempio di codice**

```python
output_desc_0 = sim.get_output_desc(0)
```

#### get_input_tensor()

**Descrizione della caratteristica**

Ottiene il Metodo RuntimeTensor per l'input per l'indice specificato

**Definizione dell'interfaccia**

```python
get_input_tensor(index)
```

**Parametri di input**

| Nome parametro | digitare | Sì o No | descrizione             |
| -------- | ---- | -------- | ---------------- |
| indice    | Int  | essere       | Inserisci l'indice del tensore |

**Il valore restituito**

Metodo runtimeTensor

**Esempio di codice**

```python
input_tensor_0 = sim.get_input_tensor(0)
```

#### set_input_tensor()

**Descrizione della caratteristica**

Imposta il tensore di runtime per l'input dell'indice specificato

**Definizione dell'interfaccia**

```python
set_input_tensor(index, tensor)
```

**Parametri di input**

| Nome parametro | digitare          | Sì o No | descrizione                    |
| -------- | ------------- | -------- | ----------------------- |
| indice    | Int           | essere       | Inserisci l'indice di RuntimeTensor |
| tensore   | Metodo runtimeTensor | essere       | Entra in RuntimeTensor       |

**Il valore restituito**

N/D

**Esempio di codice**

```python
sim.set_input_tensor(0, nncase.RuntimeTensor.from_numpy(self.inputs[0]['data']))
```

#### get_output_tensor()

**Descrizione della caratteristica**

Ottiene il tensore di runtime per l'output dell'indice specificato

**Definizione dell'interfaccia**

```python
get_output_tensor(index)
```

**Parametri di input**

| Nome parametro | digitare | Sì o No | descrizione                    |
| -------- | ---- | -------- | ----------------------- |
| indice    | Int  | essere       | Restituisce l'indice di RuntimeTensor |

**Il valore restituito**

Metodo runtimeTensor

**Esempio di codice**

```python
output_arr_0 = sim.get_output_tensor(0).to_numpy()
```

#### set_output_tensor()

**Descrizione della caratteristica**

Imposta RuntimeTensor per l'output dell'indice specificato

**Definizione dell'interfaccia**

```python
set_output_tensor(index, tensor)
```

**Parametri di input**

| Nome parametro | digitare          | Sì o No | descrizione                    |
| -------- | ------------- | -------- | ----------------------- |
| indice    | Int           | essere       | Restituisce l'indice di RuntimeTensor |
| tensore   | Metodo runtimeTensor | essere       | Tensore di runtime di output       |

**Il valore restituito**

N/D

**Esempio di codice**

```python
sim.set_output_tensor(0, tensor)
```

#### run()

**Descrizione della caratteristica**

Eseguire l'inferenza kmodel

**Definizione dell'interfaccia**

```python
run()
```

**Parametri di input**

N/D

**Il valore restituito**

N/D

**Esempio di codice**

```python
sim.run()
```

## 4.5 Esempio di modello di inferenza

**Prerequisito:**mobilenetv2_onnx_fp32_image.py script è stato compilato con il modello mobiletv2-7.onnx

mobilenetv2_onnx_simu.py si trova nella sottodirectory /path/to/nncase_sdk/examples/scripts, che recita come segue

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

Eseguire lo script di inferenza

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_onnx_simu.py --model_file models/mobilenetv2-7.onnx --kmodel_file tmp/mobilenetv2_onnx_fp32_image/test.kmodel --input_file mobilenetv2_onnx_fp32_image/data/input_0_0.bin
```

Il confronto tra i risultati del simulatore nncase e dell'inferenza della CPU è il seguente

```shell
... ...
output 0 cosine similarity : 0.9992437958717346
```

# Libreria di runtime nncase 5

## 5.1 Introduzione al nncase Runtime

Il runtime nncase viene utilizzato per caricare kmodel su dispositivi AI / impostare dati di input / eseguire calcoli KPU / ottenere dati di output, ecc.

Attualmente, solo**la versione C++**delle API, i relativi file di intestazione e le librerie statiche sono disponibili nella directory nncase sdk/riscv64

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

## 5.2 API di runtime

### 5.2.1 classe runtime_tensor

Tensore utilizzato per memorizzare i dati di input/output del modello

#### hrt::create()

**Descrizione della caratteristica**

Creare un runtime_tensor

**Definizione dell'interfaccia**

```C++
(1) NNCASE_API result<runtime_tensor> create(datatype_t datatype, runtime_shape_t shape, memory_pool_t pool = pool_cpu_only, uintptr_t physical_address = 0) noexcept;

(2) NNCASE_API result<runtime_tensor> create(datatype_t datatype, runtime_shape_t shape, gsl::span<gsl::byte> data, bool copy, memory_pool_t pool = pool_cpu_only, uintptr_t physical_address = 0) noexcept;
```

**Parametri di input**

| Nome parametro         | digitare                  | Sì o No | descrizione                              |
| ---------------- | --------------------- | -------- | --------------------------------- |
| Datatype         | datatype_t            | essere       | Tipo di dati, ad esempio dt_float32            |
| forma            | runtime_shape_t       | essere       | La forma del tensore                      |
| dati             | gsl::span\<gsl::byte> | essere       | Buffer di dati dello stato utente                  |
| copiare             | Bool                  | essere       | Se copiare                          |
| pozza             | memory_pool_t         | non       | Tipo di pool di memoria, il valore predefinito è pool_cpu_only |
| physical_address | uintptr_t             | non       | Indirizzo fisico, il valore predefinito è 0               |

**Il valore restituito**

risultato<runtime_tensor>

Esempio di codice

```c++
// create input
auto in_shape = interp.input_shape(0);
auto input_tensor = host_runtime_tensor::create(dt_float32, in_shape,
                                                {(gsl::byte *)mat.data, mat.cols * mat.rows * mat.elemSize()},
                                                true, hrt::pool_shared).expect("cannot create input tensor");
```

### 5.2.2 Interprete di classe

Interpreter è un'istanza in esecuzione del runtime nncase, che fornisce funzioni funzionali di base come load_model()/run()/input_tensor()/output_tensor().

#### load_model()

**Descrizione della caratteristica**

Caricare il modello kmodel

**Definizione dell'interfaccia**

```C++
 NNCASE_NODISCARD result<void> load_model(gsl::span<const gsl::byte> buffer) noexcept;
```

**Parametri di input**

| Nome parametro | digitare                            | Sì o No | descrizione          |
| -------- | ------------------------------- | -------- | ------------- |
| buffer   | gsl::span `<const gsl::byte>` | essere       | buffer kmodel |

**Il valore restituito**

risultato `<void>`

**Esempio di codice**

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

**Descrizione della caratteristica**

Ottiene il numero di input del modello

**Definizione dell'interfaccia**

```C++
size_t inputs_size() const noexcept;
```

**Parametri di input**

N/D

**Il valore restituito**

size_t

**Esempio di codice**

```c++
auto inputs_size = interp.inputs_size();
```

#### outputs_size()

**Descrizione della caratteristica**

Ottiene il numero di output del modello

**Definizione dell'interfaccia**

```C++
size_t outputs_size() const noexcept;
```

**Parametri di input**

N/D

**Il valore restituito**

size_t

**Esempio di codice**

```c++
auto outputs_size = interp.outputs_size();
```

#### input_shape()

**Descrizione della caratteristica**

Ottiene la forma dell'input specificato dal modello

**Definizione dell'interfaccia**

```C++
const runtime_shape_t &input_shape(size_t index) const noexcept;
```

**Parametri di input**

| Nome parametro | digitare   | Sì o No | descrizione       |
| -------- | ------ | -------- | ---------- |
| indice    | size_t | essere       | L'indice dell'input |

**Il valore restituito**

runtime_shape_t

**Esempio di codice**

```c++
auto in_shape = interp.input_shape(0);
```

#### output_shape()

**Descrizione della caratteristica**

Ottiene la forma dell'output specificato del modello

**Definizione dell'interfaccia**

```C++
const runtime_shape_t &output_shape(size_t index) const noexcept;
```

**Parametri di input**

| Nome parametro | digitare   | Sì o No | descrizione       |
| -------- | ------ | -------- | ---------- |
| indice    | size_t | essere       | L'indice dell'output |

**Il valore restituito**

runtime_shape_t

**Esempio di codice**

```c++
auto out_shape = interp.output_shape(0);
```

#### input_tensor()

**Descrizione della caratteristica**

Ottiene/imposta il tensore di input per l'indice specificato

**Definizione dell'interfaccia**

```C++
(1) result<runtime_tensor> input_tensor(size_t index) noexcept;
(2) result<void> input_tensor(size_t index, runtime_tensor tensor) noexcept;
```

**Parametri di input**

| Nome parametro | digitare           | Sì o No | descrizione                     |
| -------- | -------------- | -------- | ------------------------ |
| indice    | size_t         | essere       | buffer kmodel            |
| tensore   | runtime_tensor | essere       | Immettere il tensore di runtime corrispondente |

**Il valore restituito**

(1) Restituisce i risultati<runtime_tensor>

(2) Restituisce i risultati `<void>`

**Esempio di codice**

```c++
// set input
interp.input_tensor(0, input_tensor).expect("cannot set input tensor");
```

#### output_tensor()

**Descrizione della caratteristica**

Ottiene/imposta il tensore in uscita per l'indice specificato

**Definizione dell'interfaccia**

```C++
(1) result<runtime_tensor> output_tensor(size_t index) noexcept;
(2) result<void> output_tensor(size_t index, runtime_tensor tensor) noexcept;
```

**Parametri di input**

| Nome parametro | digitare           | Sì o No | descrizione                     |
| -------- | -------------- | -------- | ------------------------ |
| indice    | size_t         | essere       |                          |
| tensore   | runtime_tensor | essere       | Immettere il tensore di runtime corrispondente |

**Il valore restituito**

(1) Restituisce i risultati<runtime_tensor>

(2) Restituisce i risultati `<void>`

**Esempio di codice**

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

**Descrizione della caratteristica**

Eseguire calcoli kPU

**Definizione dell'interfaccia**

```C++
result<void> run() noexcept;
```

**Parametri di input**

N/D

**Il valore restituito**

risultato `<void>`

**Esempio di codice**

```c++
// run
interp.run().expect("error occurred in running model");
```

## 5.3 Esempio di runtime

Il codice di esempio si trova in /path/to/nncase_sdk/examples/mobilenetv2_onnx_fp32_image

**Condizione prefisso**

- mobilenetv2_onnx_fp32_image.py script ha compilato il modello mobiletv2-7.onnx
- Poiché l'esempio si basa sulla libreria OpenCV, è necessario specificare il percorso di OpenCV nella .txt CMakeLists dell'esempio.

**Compilazione incrociata di app**

```shell
cd /path/to/nncase_sdk/examples
./build.sh
```

Infine, generare il mobilenetv2_onnx_fp32_image nella directory out/bin

**Il k510 EVB opera sulla scheda**

Copiare i seguenti file sulla scheda EVB k510

| file                        | osservazione                                                         |
| --------------------------- | ------------------------------------------------------------ |
| mobilenetv2_onnx_fp32_image | Vengono generati esempi di compilazione incrociata                                         |
| test.kmodel                 | Utilizzare mobilenetv2_onnx_fp32_image.py compilare la build mobiletv2-7.onnx |
| .png e labels_1000.txt    | Situato sotto la sottodirectory /path/to/nncase_sdk/examples/mobilenetv2_onnx_fp32_image/data/ |

```bash
$ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mnt/zhangyang/nncase_check/lib/gomp:/mnt/zhangyang/nncase_check/lib/opencv
$ ./mobilenetv2_onnx_fp32_image test.kmodel cat.png labels_1000.txt
case ./mobilenetv2_onnx_fp32_image build at Mar  1 2022 16:31:29
interp.run() duration: 12.6642 ms
image classification result: tiger cat(9.25)
```

# 6 Librerie di programmazione funzionale (supporto runtime)

## 6.1 Introduzione al funzionale

nncase Functional viene utilizzato per migliorare la facilità d'uso quando gli utenti pre e post-elaborazione modelli

Attualmente, è disponibile solo la versione C++ delle API e i file di intestazione e le librerie associati si trovano nella directory riscv64 di nncase sdk.

## 6.2 API

### 6.2.1 quadrato

**Descrizione della caratteristica**

Calcola il quadrato, attualmente supporta l'input uint8 / int8, l'output è anche uint8 / int8, nota che l'input è a punto fisso e l'output è in virgola mobile necessità di impostare i parametri di quantizzazione.

**Definizione dell'interfaccia**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`square`](#ops_8h_1adff2f60c7c045a9840519eab2c04d127)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parametri di input**

| Nome parametro  | digitare           | Sì o No | descrizione                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | essere       | immissione                |
| `dtype` | datatype_t     | essere       | Tipo di dati del tensore di output |

**Il valore restituito**

`result<runtime_tensor>`

**Esempio di codice**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto squared = F::square(input, output_type).unwrap_or_throw();
```

### 6.2.2 mq

**Descrizione della caratteristica**

Calcola il valore del numero radice, attualmente supporta l'input uint8 / int8, l'output è anche uint8 / int8, nota che l'input è a punto fisso e l'output è in virgola mobile deve impostare i parametri di quantizzazione.

**Definizione dell'interfaccia**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`sqrt`](#ops_8h_1a53f8dde3dd4e27058b5dc743eb5dd076)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parametri di input**

| Nome parametro  | digitare           | Sì o No | descrizione                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | essere       | immissione                |
| `dtype` | datatype_t     | essere       | Tipo di dati del tensore di output |

**Il valore restituito**

`result<runtime_tensor>`

**Esempio di codice**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::sqrt(input, output_type).unwrap_or_throw();
```

### 6.2.3 Registro

**Descrizione della caratteristica**

Calcola il valore del registro, il numero negativo di input verrà convertito in Nan, attualmente supporta l'input uint8 / int8, l'output è anche uint8 / int8, nota che l'input è a punto fisso e l'output è in virgola mobile deve impostare il parametro di quantizzazione.

**Definizione dell'interfaccia**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`log`](#ops_8h_1a91df53276c3f1511427d4ac1a0140b71)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parametri di input**

| Nome parametro  | digitare           | Sì o No | descrizione                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | essere       | immissione                |
| `dtype` | datatype_t     | essere       | Tipo di dati del tensore di output |

**Il valore restituito**

`result<runtime_tensor>`

**Esempio di codice**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::log(input, output_type).unwrap_or_throw();
```

### 6.2.4 exp

**Descrizione della caratteristica**

Calcola il valore exp, attualmente supporta l'input uint8 / int8, l'output è anche uint8 / int8, nota che l'input è a punto fisso e l'output è in virgola mobile necessità di impostare i parametri di quantizzazione.

**Definizione dell'interfaccia**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`exp`](#ops_8h_1a2c6ce457805a5ba515fa7454fb4aede0)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parametri di input**

| Nome parametro  | digitare           | Sì o No | descrizione                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | essere       | immissione                |
| `dtype` | datatype_t     | essere       | Tipo di dati del tensore di output |

**Il valore restituito**

`result<runtime_tensor>`

**Esempio di codice**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::exp(input, output_type).unwrap_or_throw();
```

### 6.2.5 senza

**Descrizione della caratteristica**

Per calcolare il valore di sin, l'input uint8/int8 è attualmente supportato e anche l'output è uint8/int8, si noti che i parametri di quantizzazione devono essere impostati quando l'input è a punto fisso e l'output è a virgola mobile.

**Definizione dell'interfaccia**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`sin`](#ops_8h_1a9605b2b0dc9a6892ce878bda14586890)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parametri di input**

| Nome parametro  | digitare           | Sì o No | descrizione                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | essere       | immissione                |
| `dtype` | datatype_t     | essere       | Tipo di dati del tensore di output |

**Il valore restituito**

`result<runtime_tensor>`

**Esempi di codice**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::sin(input, output_type).unwrap_or_throw();
```

### 6.2.6 corpo

**Descrizione della caratteristica**

Calcola il valore cos, attualmente supporta l'input uint8 / int8, l'output è anche uint8 / int8, nota che l'input è a punto fisso e l'output è in virgola mobile deve impostare il parametro di quantizzazione.

**Definizione dell'interfaccia**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`cos`](#ops_8h_1a71d36c13c82f4c411f24d030cf333249)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parametri di input**

| Nome parametro  | digitare           | Sì o No | descrizione                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | essere       | immissione                |
| `dtype` | datatype_t     | essere       | Tipo di dati del tensore di output |

**Il valore restituito**

`result<runtime_tensor>`

**Esempi di codice**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::cos(input, output_type).unwrap_or_throw();
```

### 6.2.7 Turno

**Descrizione della caratteristica**

Per calcolare il valore di arrotondamento, l'input uint8/int8 è attualmente supportato e anche l'output è uint8/int8, si noti che il parametro di quantizzazione deve essere impostato quando l'input è a punto fisso e l'output è a virgola mobile.

**Definizione dell'interfaccia**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`round`](#ops_8h_1a81db8ac4866004f75fb65db876262785)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parametri di input**

| Nome parametro  | digitare           | Sì o No | descrizione                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | essere       | immissione                |
| `dtype` | datatype_t     | essere       | Tipo di dati del tensore di output |

**Il valore restituito**

`result<runtime_tensor>`

**Esempi di codice**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::round(input, output_type).unwrap_or_throw();
```

### 6.2.8 piano

**Descrizione della caratteristica**

Calcola il valore di gelo, attualmente supporta l'input uint8 / int8, l'output è anche uint8 / int8, nota che l'input è a punto fisso e l'output è in virgola mobile necessità di impostare i parametri di quantizzazione.

**Definizione dell'interfaccia**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`floor`](#ops_8h_1a1079af8fe9fb6edbb2906d91fac12635)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parametri di input**

| Nome parametro  | digitare           | Sì o No | descrizione                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | essere       | immissione                |
| `dtype` | datatype_t     | essere       | Tipo di dati del tensore di output |

**Il valore restituito**

`result<runtime_tensor>`

**Esempi di codice**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::floor(input, output_type).unwrap_or_throw();
```

### 6.2.9 ceil

**Descrizione della caratteristica**

Calcolare il valore ceil, attualmente supporta l'input uint8 / int8, l'output è anche uint8 / int8, si noti che l'input è a punto fisso e l'output è in virgola mobile necessità di impostare i parametri di quantizzazione.

**Definizione dell'interfaccia**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`ceil`](#ops_8h_1ad3b78c97f1e5348a26de7e5ba2396fb7)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parametri di input**

| Nome parametro  | digitare           | Sì o No | descrizione                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | essere       | immissione                |
| `dtype` | datatype_t     | essere       | Tipo di dati del tensore di output |

**Il valore restituito**

`result<runtime_tensor>`

**Esempi di codice**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::ceil(input, output_type).unwrap_or_throw();
```

### 6.2.10 addominali

**Descrizione della caratteristica**

Calcola il valore abs, attualmente supporta l'input uint8 / int8, l'output è anche uint8 / int8, nota che l'input è a punto fisso e l'output è in virgola mobile deve impostare i parametri di quantizzazione.

**Definizione dell'interfaccia**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`abs`](#ops_8h_1ad8290dc793bae0dc22b3baf9e0f80c14)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parametri di input**

| Nome parametro  | digitare           | Sì o No | descrizione                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | essere       | immissione                |
| `dtype` | datatype_t     | essere       | Tipo di dati del tensore di output |

**Il valore restituito**

`result<runtime_tensor>`

**Esempi di codice**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::abs(input, output_type).unwrap_or_throw();
```

### 6.2.11 neg

**Descrizione della caratteristica**

Calcola il valore di neg, attualmente supporta l'input uint8 / int8, l'output è anche uint8 / int8, nota che l'input è a punto fisso e l'output è in virgola mobile deve impostare i parametri di quantizzazione.

**Definizione dell'interfaccia**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`neg`](#ops_8h_1aa1b7858802e1afce78db72163c5210d8)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parametri di input**

| Nome parametro  | digitare           | Sì o No | descrizione                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | essere       | immissione                |
| `dtype` | datatype_t     | essere       | Tipo di dati del tensore di output |

**Il valore restituito**

`result<runtime_tensor>`

**Esempi di codice**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::neg(input, output_type).unwrap_or_throw();
```

### 6.2.12 quantizzare

**Descrizione della caratteristica**

dt_bfloat16 di input, dati di dt_float32, dt_int8 di output o output dt_uint8

**Definizione dell'interfaccia**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`quantize`](#ops_8h_1ad8ad779083b5c08da520d2f1c2469c3a)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parametri di input**

| Nome parametro  | digitare           | Sì o No | descrizione                                |
| --------- | -------------- | -------- | ----------------------------------- |
| `input` | runtime_tensor | essere       | Ingresso, il tipo deve essere float32 o bfloat16 |
| `dtype` | datatype_t     | essere       | Tipo di dati del tensore di output                 |

**Il valore restituito**

`result<runtime_tensor>`

**Esempi di codice**

```cpp
auto quantized = F::quantize(input, dt_int8).unwrap_or_throw();
```

### 6.2.13 dequantizzare

**Descrizione della caratteristica**

Inserisci l'input uint8 o int8, converti in dati float o bfloat. Si noti che l'utente deve impostare in anticipo i parametri di quantizzazione corretti per i dati per la dequantizzazione.

**Definizione dell'interfaccia**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`dequantize`](#ops_8h_1ab91a262349baf393c91abad6f393de24)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parametri di input**

| Nome parametro  | digitare           | Sì o No | descrizione                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | essere       | immissione                |
| `dtype` | datatype_t     | essere       | Tipo di dati del tensore di output |

**Il valore restituito**

`result<runtime_tensor>`

**Esempi di codice**

```cpp
input.quant_param({ 0, 1 });
auto dequantized = F::dequantize(input, output_type).unwrap_or_throw();
```

### 6.2.14 raccolto

**Descrizione della caratteristica**

Date le bbox, ritagliate dal tensore originale e ridimensionate l'output nel nuovo tensore. Accetta dt_bfloat16, dt_float32, dt_int8, dt_uint8 tipo output, output dello stesso tipo.

**Definizione dell'interfaccia**

`NNCASE_API inline result<runtime::runtime_tensor> crop(runtime::runtime_tensor &input, runtime::runtime_tensor &bbox, size_t out_h, size_t out_w, image_resize_mode_t resize_mode, bool align_corners, bool half_pixel_centers) noexcept`

**Parametri di input**

| Nome parametro           | digitare                | Sì o No | descrizione                                                                                     |
| ------------------ | ------------------- | -------- | ---------------------------------------------------------------------------------------- |
| immissione              | runtime_tensor      | essere       | Inserire i dati, è necessario formattare [n,c,h,w] il layout, se i dati sono uint8 o int8 si prega di garantire la correttezza dei parametri di quantizzazione dei dati       |
| bbox               | runtime_tensor      | essere       | Inserisci i dati bbox, devi formattare [1,1,m,4] il layout, i dati interni sono[y0,x0,y1,x1], il tipo è[float32, bfloat16] |
| out_h              | size_t              | essere       | Altezza dei dati di output                                                                           |
| out_w              | size_t              | essere       | Inserisci la larghezza dei dati                                                                            |
| resize_mode        | image_resize_mode_t | essere       | Modello del metodo di ridimensionamento                                                                           |
| align_corners      | Bool                | essere       | Ridimensionare se align_corners                                                    |
| half_pixel_centers | Bool                | essere       | Ridimensionare se il pixel è allineato al centro                                                                  |

**Il valore restituito**

`result<runtime_tensor>`

**Esempi di codice**

```cpp
auto bbox = get_rand_bbox(input_shape, roi_amount);
auto &&[out_h, out_w] = get_rand_out_hw();
auto output_opt = F::crop(input, bbox, out_h, out_w, resize_mode).unwrap_or_throw();
```

### 6.2.15 ridimensionare

**Descrizione della caratteristica**

Data la larghezza dell'altezza di uscita, metti il tensore di ingresso ridimensionato alla nuova dimensione. Accetta dt_bfloat16, dt_float32, dt_int8, dt_uint8 tipo output, output dello stesso tipo.

**Definizione dell'interfaccia**

`NNCASE_API inline result<runtime::runtime_tensor> resize(runtime::runtime_tensor &input, size_t out_h, size_t out_w, image_resize_mode_t resize_mode, bool align_corners, bool half_pixel_centers) noexcept`

**Parametri di input**

| Nome parametro           | digitare                | Sì o No | descrizione                                                                               |
| ------------------ | ------------------- | -------- | ---------------------------------------------------------------------------------- |
| immissione              | runtime_tensor      | essere       | Inserisci i dati, devono essere [n,c,h,w] formattati, se i dati sono uint8 o int8 assicurati la correttezza dei parametri di quantizzazione dei dati |
| out_h              | size_t              | essere       | Altezza dei dati di output                                                                     |
| out_w              | size_t              | essere       | Inserisci la larghezza dei dati                                                                      |
| resize_mode        | image_resize_mode_t | essere       | Modello del metodo di ridimensionamento                                                                     |
| align_corners      | Bool                | essere       | Ridimensionare se align_corners                                              |
| half_pixel_centers | Bool                | essere       | Ridimensionare se il pixel è allineato al centro                                                            |

**Il valore restituito**

`result<runtime_tensor>`

**Esempi di codice**

```cpp
auto &&[out_h, out_w] = get_rand_out_hw();
auto output_opt = F::resize(input, out_h, out_w, resize_mode, false, false).unwrap_or_throw();
```

### 6.2.16 pad

**Descrizione della caratteristica**

I dati di riempimento su ogni dimensione accettano dt_bfloat16, dt_float32, dt_int8, dt_uint8 tipo output e output dello stesso tipo.

**Definizione dell'interfaccia**

`NNCASE_API inline result<runtime::runtime_tensor> pad(runtime::runtime_tensor &input, runtime_paddings_t &paddings, pad_mode_t pad_mode, float fill_v)`

**Parametri di input**

| Nome parametro | digitare               | Sì o No | descrizione                                                                                                                                       |
| -------- | ------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| immissione    | runtime_tensor     | essere       | Inserire i dati, se i dati sono uint8 o int8 Garantire la correttezza dei parametri di quantizzazione dei dati                                                                                  |
| imbottitura  | runtime_paddings_t | essere       | Ad esempio, il valore di imbottitura è `[ {2,3}, {1,3} ]`indicato davanti al pad 2 nell'ultima dimensione, seguito dal pad 3. La penultima dimensione è preceduta dal pad 1, seguito dal pad 2 |
| pad_mode | pad_mode_t         | essere       | Attualmente, è supportata solo la modalità const                                                                                                                   |
| fill_v   | galleggiare              | essere       | Popolare i valori                                                                                                                                     |

**Il valore restituito**

`result<runtime_tensor>`

**Esempi di codice**

```cpp
runtime_paddings_t paddings{ { 0, 0 }, { 0, 0 }, { 0, 0 }, { 1, 2 } };
auto output = F::pad(input, paddings, pad_constant, pad_value).unwrap_or_throw();
```
<!-- markdownlint-enable no-emphasis-as-header -->
# 7 Libro bianco quantitativo

## 7.1 White paper sulla quantificazione del modello di classificazione

| Modello di classificazione     | Precisione cpu (Top-1) | Precisione in virgola mobile (Top-1) | precisione uint8 (Top-1) | Precisione int8 (Top-1) |
| ------------ | -------------- | --------------- | ---------------- | --------------- |
| alexnet      | 0.531          | 0.53            | N/D              | 0.52            |
| densenet 121 · | 0.732          | 0.732           | 0.723            | N/D             |
| Inception v3 | 0.766          | 0.765           | 0.773            | 0.77            |
| Inception v4 | 0.789          | 0.789           | 0.793            | 0.792           |
| rete mobile v1 | 0.731          | 0.73            | 0.723            | 0.718           |
| rete mobile v2 | 0.713          | 0.715           | 0.713            | 0.719           |
| Resnet50 v2  | 0.747          | 0.74            | 0.748            | 0.749           |
| VGG 16       | 0.689          | 0.687           | 0.690            | 0.689           |

> Questa tabella serve principalmente a confrontare le prestazioni della quantizzazione, la precisione della CPU è l'intero set di convalida ImageNet e l'accuratezza a virgola mobile e quantizzazione è il risultato del test del sottoinsieme di dati per la prima immagine delle 1000 classi nel set di convalida in base al numero ordinale.
>
> I risultati dei test di Alexnet e SenseNet sono vecchi dati, entrambi i quali sono i risultati dei test delle prime 1000 immagini del set di verifica come sottoinsieme dei dati, e N / A è che il sottoinsieme di dati di test in quel momento è diverso dalla CPU, quindi non viene utilizzato come confronto.
>
> Poiché la rete selezionata non proviene necessariamente dal funzionario o ci sono differenze nella pre-elaborazione, ecc., Può differire dalle prestazioni ufficiali.

## 7.2 White paper sulla quantificazione del modello di rilevamento

1. YOLOV3 ·

    | COCOAPI                                                      | Risultati ufficiali | Precisione in virgola mobile della CPU | gnne precisione a virgola mobile | precisione uint8 | precisione int8 |
    | ------------------------------------------------------------ | -------- | ----------- | ------------ | --------- | -------- |
    | Precisione media (AP) @ [IoU = 0,50:0,95 \| area = tutti \| maxDets = 100] | 0.314    | 0.307       | 0.306        | 0.295     | 0.288    |
    | Precisione media (AP) @ [UI = 0,50\| area = tutti \| maxDets = 100] | 0.559    | 0.555       | 0.554        | 0.555     | 0.554    |
    | Precisione media (AP) @ [UI = 0,75\| area = tutti \| maxDets = 100] | 0.318    | 0.308       | 0.307        | 0.287     | 0.275    |
    | Precisione media (AP) @ [IoU = 0,50:0,95 \| area = piccolo \| maxDets = 100] | 0.142    | 0.150       | 0.149        | 0.147     | 0.144    |
    | Precisione media (AP) @ [IoU= 0.50:0.95\| area = media \| maxDets = 100] | 0.341    | 0.332       | 0.332        | 0.322     | 0.316    |
    | Precisione media (AP) @ [IoU = 0,50:0,95 \| area = grande \| maxDets = 100] | 0.464    | 0.437       | 0.437        | 0.414     | 0.404    |
    | Richiamo medio (AR) @ [IoU= 0.50:0.95\| area = tutti \| maxDets = 1] | 0.278    | 0.270       | 0.271        | 0.262     | 0.256    |
    | Richiamo medio (AR) @ [IoU= 0.50:0.95\| area = tutti \| maxDets = 10] | 0.419    | 0.412       | 0.412        | 0.399     | 0.392    |
    | Richiamo medio (AR) @ [IoU = 0,50:0,95 \| area = tutti \| maxDets = 100] | 0.442    | 0.433       | 0.433        | 0.421     | 0.414    |
    | Richiamo medio (AR) @ [IoU = 0,50:0,95 \| area = piccolo \| maxDets = 100] | 0.239    | 0.251       | 0.251        | 0.248     | 0.246    |
    | Richiamo medio (AR) @ [IoU= 0.50:0.95\| area = media \| maxDets = 100] | 0.482    | 0.462       | 0.463        | 0.451     | 0.443    |
    | Richiamo medio (AR) @ [IoU = 0,50:0,95 \| area = grande \| maxDets = 100] | 0.611    | 0.586       | 0.585        | 0.559     | 0.550    |

2. ssd-mobilenetv1

    | COCOAPI                                                                    | Risultati ufficiali | Precisione in virgola mobile della CPU | gnne precisione a virgola mobile | precisione uint8 | precisione int8 |
    | -------------------------------------------------------------------------- | -------- | ----------- | ------------ | --------- | -------- |
    | Precisione media (AP) @ [IoU = 0,50:0,95 \| area = tutti \| maxDets = 100]   | 0.184    | 0.184       | 0.184        | 0.183     | 0.183    |
    | Precisione media (AP) @ [UI = 0,50\| area = tutti \| maxDets = 100]        | 0.306    | 0.307       | 0.306        | 0.305     | 0.306    |
    | Precisione media (AP) @ [UI = 0,75\| area = tutti \| maxDets = 100]        | 0.191    | 0.192       | 0.190        | 0.189     | 0.190    |
    | Precisione media (AP) @ [IoU = 0,50:0,95 \| area = piccolo \| maxDets = 100] | 0.017    | 0.017       | 0.017        | 0.017     | 0.017    |
    | Precisione media (AP) @ [IoU= 0.50:0.95\| area = media \| maxDets = 100] | 0.157    | 0.157       | 0.157        | 0.156     | 0.155    |
    | Precisione media (AP) @ [IoU = 0,50:0,95 \| area = grande \| maxDets = 100] | 0.371    | 0.372       | 0.371        | 0.370     | 0.369    |
    | Richiamo medio (AR) @ [IoU= 0.50:0.95\| area = tutti \| maxDets = 1]         | 0.180    | 0.180       | 0.180        | 0.181     | 0.181    |
    | Richiamo medio (AR) @ [IoU= 0.50:0.95\| area = tutti \| maxDets = 10]        | 0.242    | 0.242       | 0.242        | 0.243     | 0.243    |
    | Richiamo medio (AR) @ [IoU = 0,50:0,95 \| area = tutti \| maxDets = 100]      | 0.242    | 0.242       | 0.242        | 0.243     | 0.243    |
    | Richiamo medio (AR) @ [IoU = 0,50:0,95 \| area = piccolo \| maxDets = 100]    | 0.026    | 0.026       | 0.026        | 0.026     | 0.026    |
    | Richiamo medio (AR) @ [IoU= 0.50:0.95\| area = media \| maxDets = 100]    | 0.206    | 0.206       | 0.206        | 0.206     | 0.205    |
    | Richiamo medio (AR) @ [IoU = 0,50:0,95 \| area = grande \| maxDets = 100]    | 0.489    | 0.491       | 0.490        | 0.490     | 0.491    |

3. YOLOV5S

    | COCOAPI                                                                    | Risultati ufficiali | Precisione in virgola mobile della CPU | gnne precisione a virgola mobile | precisione uint8 | precisione int8 |
    | -------------------------------------------------------------------------- | -------- | ----------- | ------------ | --------- | -------- |
    | Precisione media (AP) @ [IoU = 0,50:0,95 \| area = tutti \| maxDets = 100]   | 0.367    | 0.365       | 0.335        | 0.334     | 0.335    |
    | Precisione media (AP) @ [UI = 0,50\| area = tutti \| maxDets = 100]        | 0.555    | 0.552       | 0.518        | 0.518     | 0.518    |
    | Precisione media (AP) @ [UI = 0,75\| area = tutti \| maxDets = 100]        | 0.398    | 0.395       | 0.364        | 0.363     | 0.362    |
    | Precisione media (AP) @ [IoU = 0,50:0,95 \| area = piccolo \| maxDets = 100] | 0.223    | 0.220       | 0.199        | 0.199     | 0.197    |
    | Precisione media (AP) @ [IoU= 0.50:0.95\| area = media \| maxDets = 100] | 0.419    | 0.418       | 0.387        | 0.386     | 0.386    |
    | Precisione media (AP) @ [IoU = 0,50:0,95 \| area = grande \| maxDets = 100] | 0.463    | 0.459       | 0.423        | 0.422     | 0.423    |
    | Richiamo medio (AR) @ [IoU= 0.50:0.95\| area = tutti \| maxDets = 1]         | 0.306    | 0.306       | 0.288        | 0.287     | 0.287    |
    | Richiamo medio (AR) @ [IoU= 0.50:0.95\| area = tutti \| maxDets = 10]        | 0.518    | 0.518       | 0.487        | 0.486     | 0.487    |
    | Richiamo medio (AR) @ [IoU = 0,50:0,95 \| area = tutti \| maxDets = 100]      | 0.576    | 0.576       | 0.540        | 0.539     | 0.540    |
    | Richiamo medio (AR) @ [IoU = 0,50:0,95 \| area = piccolo \| maxDets = 100]    | 0.391    | 0.399       | 0.350        | 0.350     | 0.347    |
    | Richiamo medio (AR) @ [IoU= 0.50:0.95\| area = media \| maxDets = 100]    | 0.641    | 0.640       | 0.606        | 0.605     | 0.607    |
    | Richiamo medio (AR) @ [IoU = 0,50:0,95 \| area = grande \| maxDets = 100]    | 0.716    | 0.710       | 0.680        | 0.683     | 0.685    |

# 8 Domande frequenti

1. 安装wheel时报错: "xxx.whl non è una ruota supportata su questa piattaforma." **

    D: 安装nncase wheel包, 出现ERROR: nncase-1.0.0.20210830-cp37-cp37m-manylinux_2_24_x86_64.whl non è una ruota supportata su questa piattaforma.

    A: > pip di aggiornamento = 20,3

    ```shell
    sudo pip3 install --upgrade pip
    ```

2. **Quando il CRB esegue il programma di inferenza app, segnala l'errore "std::bad_alloc"**

    D: Eseguire il programma di inferenza dell'app sul CRB e generare un'eccezione "std::bad_alloc"

    ```shell
    $ ./cpp.sh
    case ./yolov3_bfloat16 build at Sep 16 2021 18:12:03
    terminate called after throwing an instance of 'std::bad_alloc'
    what():  std::bad_alloc
    ```

    R: le eccezioni std::bad_alloc sono in genere causate da errori di allocazione della memoria, che possono essere controllati come segue.

    - Controlla se il kmodel generato supera la memoria corrente disponibile nel sistema (ad esempio yolov3 bfloat16 kmodel size è 121MB, l'attuale memoria disponibile Linux è solo 70MB, l'eccezione verrà generata).  Se supera, prova a utilizzare la quantizzazione post-allenamento per ridurre le dimensioni del kmodel.
    - Controlla l'app per perdite di memoria

3. **Quando si esegue il programma di inferenza dell'app[.. t_runtime_tensor.cpp:310 (creare)] data.size_bytes() == size = false (bool).**

    D: Il simulatore esegue il programma di inferenza dell'app, generando un[.. t_runtime_tensor.cpp:310 (creare)] 'eccezione "data.size_bytes() == size = false (bool)"

    A: Controllare le informazioni del tensore di ingresso per le impostazioni, concentrandosi sulla forma di input e sul numero di byte occupati da ciascun elemento (fp32/uint8)

**Traduzione Disclaimer**  
Per la comodità dei clienti, Canaan utilizza un traduttore AI per tradurre il testo in più lingue, che possono contenere errori. Non garantiamo l'accuratezza, l'affidabilità o la tempestività delle traduzioni fornite. Canaan non sarà responsabile per eventuali perdite o danni causati dall'affidamento sull'accuratezza o sull'affidabilità delle informazioni tradotte. Se c'è una differenza di contenuto tra le traduzioni in lingue diverse, prevarrà la versione cinese semplificata.

Se desideri segnalare un errore di traduzione o un'inesattezza, non esitare a contattarci via mail.
