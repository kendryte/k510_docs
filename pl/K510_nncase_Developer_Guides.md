![okładka kanaanu.png](http://s2.loli.net/2022/03/30/7UG1IxrOXTo2QKw.png)

**<font face="黑体" size="6" style="float:right">K510 nncase Podręcznik programisty</font>**

<font face="黑体"  size=3>Wersja dokumentu: V1.0.1</font>

<font face="黑体"  size=3>Opublikowano: 2022-05-10</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Zrzeczenie się**</font>
Zakupione produkty, usługi lub funkcje podlegają umowom handlowym i warunkom Beijing Canaan Jiesi Information Technology Co., Ltd. ("Spółka", ta sama poniżej), a wszystkie lub część produktów, usług lub funkcji opisanych w niniejszym dokumencie może nie być objęta zakresem zakupu lub użytkowania. O ile nie uzgodniono inaczej w umowie, Firma zrzeka się wszelkich oświadczeń lub gwarancji, wyraźnych lub dorozumianych, co do dokładności, niezawodności, kompletności, marketingu, konkretnego celu i nieagresji jakichkolwiek oświadczeń, informacji lub treści tego dokumentu. O ile nie uzgodniono inaczej, niniejszy dokument jest dostarczany jako wskazówka wyłącznie do użytku.
Ze względu na aktualizacje wersji produktu lub z innych powodów zawartość tego dokumentu może być od czasu do czasu aktualizowana lub modyfikowana bez powiadomienia. 

**<font face="黑体"  size=3>Informacje o znakach towarowych</font>**

""<img src="http://s2.loli.net/2022/03/30/xN21jbhnwSFyGRD.png" style="zoom:33%;" />, ikona "Canaan", Canaan i inne znaki towarowe Canaan oraz inne znaki towarowe Canaan są znakami towarowymi Beijing Canaan Jiesi Information Technology Co., Ltd. Wszystkie inne znaki towarowe lub zarejestrowane znaki towarowe, które mogą być wymienione w niniejszym dokumencie, są własnością ich odpowiednich właścicieli. 

**<font face="黑体"  size=3>Prawa autorskie ©2022 Beijing Canaan Jiesi Information Technology Co., Ltd</font>**
Niniejszy dokument ma zastosowanie wyłącznie do rozwoju i projektowania platformy K510, bez pisemnej zgody firmy, żadna jednostka ani osoba fizyczna nie może rozpowszechniać części lub całości treści tego dokumentu w jakiejkolwiek formie. 

**<font face="黑体"  size=3>Pekin Canaan Jiesi Information Technology Co Ltd</font>**
Adres internetowy: canaan-creative.com
Zapytania biznesowe: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# przedmowa
**<font face="黑体"  size=5>Przeznaczenie </font>**dokumentu
Ten dokument jest dokumentem opisowym dotyczącym korzystania z kompilatora nncase/K510, zapewniającym użytkownikom sposób instalowania nncase, wywoływanie interfejsów API kompilatora w celu kompilacji modeli sieci neuronowych oraz interfejsy API środowiska uruchomieniowego do pisania programów inferencji AI

**<font face="黑体"  size=5>Obiekty programu Reader</font>**

Główne osoby, których dotyczy ten dokument (ten przewodnik):

- Programiści
- Personel wsparcia technicznego

**<font face="黑体"  size=5>Terminy i akronimy</font>**

| termin | Wyjaśnienie/imię i nazwisko                              |
| ---- | -------------------------------------- |
| PTQ  | Kwantyzacja potreningowa, kwantyzacja potreningowa |
| MSE  | błąd średniego kwadratu, błąd średniego kwadratu            |
|      |                                        |

**<font face="黑体"  size=5>Historia</font>**
 zmian <font face="宋体"  size=2>Historia zmian gromadzi opis każdej aktualizacji dokumentu. Najnowsza wersja dokumentu zawiera aktualizacje dla wszystkich poprzednich wersji. </font>

| Numer wersji   | Zmodyfikowane przez     | Data aktualizacji | Uwagi do poprawek |
|  :-----  |-------   |  ------  |  ------  |
| Wersja 1.0.1 | Reklama | 2022-05-10 | nncase_v1.6.1 |
| Wersja 1.0.0 | Zhang Yang/Zhang Jizhao/Yang Haoqi | 2022-05-06 | nncase_v1.6.0 |
| Wersja 0.9.0 | Reklama | 2022-04-01 | nncase_v1.5.0 |
| Wersja 0.8.0 | Zhang Yang/Zhang Jizhao | 2022-03-03 | nncase_v1.4.0 |
| Wersja 0.7.0 | Reklama | 2022-01-28 | nncase_v1.3.0 |
| Wersja 0.6.0 | Reklama | 2021-12-31 | nncase_v1.2.0 |
| Wersja 0.5.0 | Reklama | 2021-12-03 | nncase_v1.1.0 |
| Wersja 0.4.0 | Zhang Yang/Haoqi Yang/Zheng Qihang | 2021-10-29 | nncase_v1.0.0 |
| Wersja 0.3.0 | Zhang Yang / Yang Haoqi | 2021-09-28 | nncase_v1.0.0_rc1 |
| Wersja 0.2.0 | Zhang Yang / Yang Haoqi | 2021-09-02 | nncase_v1.0.0_beta2 |
| Wersja 0.1.0 | Zhang Yang / Yang Haoqi | 2021-08-31 | nncase_v1.0.0_beta1 |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Treść</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Wprowadzenie do środowiska programistycznego

## 1.1 System operacyjny

- Ubuntu 18.04 / 20.04

## 1.2 Środowisko oprogramowania

Wymagania dotyczące środowiska oprogramowania przedstawiono w poniższej tabeli:

| numer seryjny | Zasoby dotyczące oprogramowania        | Ilustrują                        |
| ---- | --------------- | --------------------------- |
| 1    | Pyton          | Python 3.6/3.7/3.8/3.9/3.10 |
| 2    | pip3            | pip3 wersja > = 20.3            |
| 3    | onnx            | Wersja onnx to 1.9.0             |
| 4    | onnx-simplify | Wersja onnx-simplifier to 0.3.6  |
| 5    | onnxoptimizer   | Wersja onnxoptimizer to 0.2.6    |

## 1.3 Środowisko sprzętowe

Wymagania dotyczące środowiska sprzętowego przedstawiono w poniższej tabeli:

| numer seryjny | Zasoby sprzętowe     | Ilustrują |
| ---- | ------------ | ---- |
| 1    | K510 CRB     |      |
| 2    | Karta SD i czytnik kart |      |

# 2 wprowadzenie do nncase

## 2.1 Co to jest nncase

nncase to kompilator sieci neuronowych przeznaczony dla akceleratorów AI, który obecnie obsługuje cele, takie jak CPU / K210 / K510

Funkcje dostarczane przez nncase

- Obsługa wielu sieci wejściowych i wyjściowych, obsługa struktury wielobranżowej
- Alokacja pamięci statycznej, nie jest wymagana pamięć sterty
- Scalanie i optymalizacja operatora
- Obsługuje wnioskowanie kwantyzacji float i uint8/int8
- Obsługuje kwantyzację po szkoleniu, wykorzystując modele zmiennoprzecinkowe i zestawy kalibracji kwantyzacji
- Model płaski z obsługą ładowania bez kopiowania

Struktura sieci neuronowych obsługiwana przez nncase

- tflite
- onnx
- kawiarnia

## 2.2 Zalety produktu

- **Proste, kompleksowe wdrożenie**

  Zmniejsz liczbę interakcji z użytkownikami. Wdrożenie na wskaźnikach KPU można osiągnąć, używając i wdrażając te same narzędzia i procesy dla modeli CPU i GPU. Nie ma potrzeby ustawiania złożonych parametrów, obniżania progu użytkowania i przyspieszania cyklu iteracji algorytmów AI.
- **Pełne wykorzystanie istniejącego ekosystemu sztucznej inteligencji**

  Dołączony do ram szeroko stosowanych w branży. Z jednej strony może poprawić swoją widoczność i cieszyć się dywidendami dojrzałej ekologii. Z drugiej strony można zmniejszyć koszty rozwoju małych i średnich programistów, a dojrzałe modele i algorytmy w branży mogą być bezpośrednio wdrażane.
- **Wykorzystaj w pełni swój sprzęt**

  Zaletą NPU jest to, że wydajność jest wyższa niż CPU i GPU, a kompilator DL musi być w stanie w pełni wykorzystać wydajność sprzętu. Kompilator musi również adaptacyjnie optymalizować wydajność dla nowej struktury modelu, więc oprócz optymalizacji ręcznej należy zbadać nową technikę automatycznej optymalizacji.
- **Skalowalność i łatwość konserwacji**

  Możliwość obsługi wdrożeń modeli AI dla K210, K510 i przyszłych układów. Pewna skalowalność musi być zapewniona na poziomie architektonicznym. Dodanie nowego obiektu docelowego jest tańsze i pozwala na ponowne użycie jak największej liczby modułów. Przyspiesz rozwój nowych produktów, aby osiągnąć akumulację technologii kompilatora DL.

## 2.3 Architektura nncase

<img src="https://i.loli.net/2021/08/18/IQR12SOJdzxTUZH.png" alt="nncase_arch.png" style="zoom:67%;" />

Stos oprogramowania nnncase składa się obecnie z dwóch części: kompilatora i środowiska wykonawczego.

**Kompilator:** Służy do kompilowania modeli sieci neuronowych na komputerze i ostatecznie generowania pliku kmodel. Obejmuje głównie importera, IR, Evaluator, Quantize, Transform optimization, Tiling, Partition, Schedule, Codegen i inne moduły. 

- Importer: Importuje modele z innych struktur sieci neuronowych do nncase
- IR: Środkowa reprezentacja, podzielona na importowaną przez importera neutralną IR (niezależną od urządzenia) i Nutral IR generowaną przez obniżenie konwersji Target IR (zależna od urządzenia)
- Ewaluator: Ewaluator zapewnia interpretacyjne wykonanie IR i jest często używany w scenariuszach takich jak Constant Folding/PTQ Calibration
- Transformacja: do transformacji IR i optymalizacji przechodzenia wykresu itp
- Kwantyzacja: Kwantyzacja po treningu, dodawanie znaczników kwantyzacji do tensora, który ma być kwantyzowany, wywoływanie Ewaluatora w celu wykonania interpretacji zgodnie z zestawem korekcji wejściowej, zbieranie zakresu danych tensorowych, wstawianie węzłów kwantyzacji / dekwantyzacji, a na koniec optymalizacja w celu wyeliminowania niepotrzebnych węzłów kwantyzacji / dekwantyzacji itp.
- Kafelki: Ograniczone przez mniejszą pojemność pamięci NPU, duże fragmenty obliczeń muszą zostać podzielone. Ponadto wybranie parametru Tilling, gdy w obliczeniach występuje duża ilość multipleksowania danych, będzie miało wpływ na opóźnienie i przepustowość.
- Partycja: Podziel wykres według ModuleType, każdy podgraf po podzieleniu będzie odpowiadał RuntimeModule, różne typy RuntimeModule odpowiadają różnym urządzeniom (cpu / K510)
- Harmonogram: generuje kolejność obliczeń i przydziela na podstawie zależności danych na zoptymalizowanym wykresie.
- Codegen: Wywołaj codegen odpowiadający ModuleType dla każdego podgrafu, aby wygenerować RuntimeModule

**Środowisko wykonawcze**: Zintegrowane z aplikacją użytkownika, zapewnia takie funkcje, jak ładowanie kmodel / ustawianie danych wejściowych, wykonywanie KPU i uzyskiwanie danych wyjściowych

# 3 Zainstaluj nncase

Część kompilatora łańcucha narzędzi nncase zawiera nncase i kompilator K510, z których oba muszą zainstalować odpowiedni pakiet kół.

- Pakiet nncase wheel został[ wydany na github nncase](https://github.com/kendryte/nncase/releases/tag/v1.6.0), obsługując Python 3.6 / 3.7 / 3.8 / 3.9 / 3.10, użytkownicy mogą wybrać odpowiednią wersję do pobrania zgodnie z systemem operacyjnym i Pythonem
- Pakiet koła kompilatora K510 znajduje się w katalogu x86_64 zestawu SDK nncase, nie zależy od wersji Pythona i można go zainstalować bezpośrednio

Jeśli nie masz środowiska Ubuntu, możesz użyć[ dockera nncase](https://github.com/kendryte/nncase/blob/master/docs/build.md#docker) (Ubuntu 20.04 + Python 3.8).

```shell
cd /path/to/nncase_sdk
docker pull registry.cn-hangzhou.aliyuncs.com/kendryte/nncase:latest
docker run -it --rm -v `pwd`:/mnt -w /mnt registry.cn-hangzhou.aliyuncs.com/kendryte/nncase:latest /bin/bash -c "/bin/bash"
```

Poniżej przedstawiono Ubuntu 20.04 + Python 3.8 instalacja nncase jako przykład

```shell
wget -P x86_64 https://github.com/kendryte/nncase/releases/download/v1.6.0/nncase-1.6.0.20220505-cp38-cp38-manylinux_2_24_x86_64.whl
pip3 install x86_64/*.whl
```
<!-- markdownlint-disable no-emphasis-as-header -->
# 4 Model kompilacji/wnioskowania

nncase zapewnia** interfejs API języka Python **do kompilowania/wnioskowania modeli głębokiego uczenia na komputerze PC

## 4.1 Obsługiwane podmioty

### 4.1.1 operator tflite

| Operator                | Jest obsługiwany |
| ----------------------- | ------------ |
| ABS                     | ✅            |
| DODAWAĆ                     | ✅            |
| ARG_MAX                 | ✅            |
| ARG_MIN                 | ✅            |
| AVERAGE_POOL_2D         | ✅            |
| BATCH_MATMUL            | ✅            |
| OBSADA                    | ✅            |
| CEIL                    | ✅            |
| ŁĄCZENIE           | ✅            |
| CONV_2D                 | ✅            |
| CIAŁO                     | ✅            |
| ZWYCZAJ                  | ✅            |
| DEPTHWISE_CONV_2D       | ✅            |
| DIV                     | ✅            |
| RÓWNY                   | ✅            |
| EXP                     | ✅            |
| EXPAND_DIMS             | ✅            |
| PIĘTRO                   | ✅            |
| FLOOR_DIV               | ✅            |
| FLOOR_MOD               | ✅            |
| FULLY_CONNECTED         | ✅            |
| WIĘKSZA                 | ✅            |
| GREATER_EQUAL           | ✅            |
| L2_NORMALIZATION        | ✅            |
| LEAKY_RELU              | ✅            |
| MNIEJ                    | ✅            |
| LESS_EQUAL              | ✅            |
| DZIENNIK                     | ✅            |
| LOGISTYCZNE                | ✅            |
| MAX_POOL_2D             | ✅            |
| MAKSIMUM                 | ✅            |
| ZNACZYĆ                    | ✅            |
| MINIMUM                 | ✅            |
| Ja                     | ✅            |
| NEG                     | ✅            |
| NOT_EQUAL               | ✅            |
| PAD                     | ✅            |
| PADV2                   | ✅            |
| MIRROR_PAD              | ✅            |
| PACZKA                    | ✅            |
| POW                     | ✅            |
| REDUCE_MAX              | ✅            |
| REDUCE_MIN              | ✅            |
| REDUCE_PROD             | ✅            |
| RELU •                    | ✅            |
| PRELU                   | ✅            |
| RELU6                   | ✅            |
| PRZEKSZTAŁCIĆ                 | ✅            |
| RESIZE_BILINEAR         | ✅            |
| RESIZE_NEAREST_NEIGHBOR | ✅            |
| OKRĄGŁY                   | ✅            |
| RSQRT                   | ✅            |
| KSZTAŁT                   | ✅            |
| BEZ                     | ✅            |
| KAWAŁEK                   | ✅            |
| SOFTMAX                 | ✅            |
| SPACE_TO_BATCH_ND       | ✅            |
| ŚCISKAĆ                 | ✅            |
| BATCH_TO_SPACE_ND       | ✅            |
| STRIDED_SLICE           | ✅            |
| SQRT                    | ✅            |
| KWADRATOWY                  | ✅            |
| SUB                     | ✅            |
| SUMA                     | ✅            |
| PODEJRZANY                    | ✅            |
| KAFELEK                    | ✅            |
| TRANSPOZYCJI               | ✅            |
| TRANSPOSE_CONV          | ✅            |
| KWANTYZACJA                | ✅            |
| FAKE_QUANT              | ✅            |
| DEQUANTIZE              | ✅            |
| ZBIERAĆ                  | ✅            |
| GATHER_ND               | ✅            |
| ONE_HOT                 | ✅            |
| SQUARED_DIFFERENCE      | ✅            |
| LOG_SOFTMAX             | ✅            |
| ROZSZCZEPIAĆ                   | ✅            |
| HARD_SWISH              | ✅            |

### 4.1.2 Operator onnx

| Operator              | Jest obsługiwany |
| --------------------- | ------------ |
| Abs                   | ✅            |
| Acos •                  | ✅            |
| Acosh •                 | ✅            |
| I                   | ✅            |
| ArgMax                | ✅            |
| ArgMin                | ✅            |
| Słony                  | ✅            |
| Asinh •                 | ✅            |
| Dodawać                   | ✅            |
| AveragePool           | ✅            |
| BatchNormalizacja    | ✅            |
| Obsada                  | ✅            |
| Ceil                  | ✅            |
| Celu                  | ✅            |
| Klips                  | ✅            |
| Concat                | ✅            |
| Stały              | ✅            |
| ConstantOfShape       | ✅            |
| Conv                  | ✅            |
| ConvTranspose         | ✅            |
| Ciało                   | ✅            |
| Cosh                  | ✅            |
| Cumsum •                | ✅            |
| DepthToSpace          | ✅            |
| DequantizeLinear      | ✅            |
| Div                   | ✅            |
| Odpad szkolny               | ✅            |
| Życie                   | ✅            |
| Exp                   | ✅            |
| Rozszerzać                | ✅            |
| Równy                 | ✅            |
| Spłaszczyć               | ✅            |
| Piętro                 | ✅            |
| Zbierać                | ✅            |
| ZbierzND              | ✅            |
| Gemm •                  | ✅            |
| GlobalAveragePool     | ✅            |
| GlobalMaxPool         | ✅            |
| Większa               | ✅            |
| WiększyRówna równość        | ✅            |
| Hardmax               | ✅            |
| HardSigmoid           | ✅            |
| HardSwish             | ✅            |
| Tożsamość              | ✅            |
| InstancjaNormalizacja | ✅            |
| LpNormalizacja       | ✅            |
| LeakyRelu             | ✅            |
| Mniej                  | ✅            |
| LessOrEqual           | ✅            |
| Dziennik                   | ✅            |
| LogSoftmax            | ✅            |
| LRN                   | ✅            |
| LSTM                  | ✅            |
| Matmul •                | ✅            |
| MaxPool               | ✅            |
| Max                   | ✅            |
| Min                   | ✅            |
| Ja                   | ✅            |
| Neg                   | ✅            |
| Nie                   | ✅            |
| OneHot                | ✅            |
| Pad                   | ✅            |
| Pow                   | ✅            |
| PRelu                 | ✅            |
| QuantizeLinear        | ✅            |
| LosowyNormalny          | ✅            |
| RandomNormalLike      | ✅            |
| RandomUniform         | ✅            |
| RandomUniformLike     | ✅            |
| RedukcjaL1              | ✅            |
| RedukcjaL2              | ✅            |
| ReduceLogSum          | ✅            |
| ReduceLogSumExp       | ✅            |
| ReduceMax             | ✅            |
| ReduceŚredni            | ✅            |
| ReduceMin             | ✅            |
| ReduceProd            | ✅            |
| ReduceSum             | ✅            |
| ReduceSumSquare       | ✅            |
| Żal                  | ✅            |
| Przekształcić               | ✅            |
| Zmienić rozmiar                | ✅            |
| Sekwencja odwrotna       | ✅            |
| RoiAlign              | ✅            |
| Okrągły                 | ✅            |
| Wieś                  | ✅            |
| Kształt                 | ✅            |
| Znak                  | ✅            |
| Bez                   | ✅            |
| Narodziny                  | ✅            |
| Sigmoid               | ✅            |
| Rozmiar                  | ✅            |
| Kawałek                 | ✅            |
| Softmax               | ✅            |
| Softplus              | ✅            |
| Miękki znak              | ✅            |
| SpaceToDepth          | ✅            |
| Rozszczepiać                 | ✅            |
| Sqrt                  | ✅            |
| Ściskać               | ✅            |
| Sub                   | ✅            |
| Suma                   | ✅            |
| Podejrzany                  | ✅            |
| Kafelek                  | ✅            |
| TopK                  | ✅            |
| Transpozycji             | ✅            |
| Trilu •                 | ✅            |
| Próbkowanie w górę              | ✅            |
| Unsqueeze             | ✅            |
| Gdzie                 | ✅            |

### 4.1.3 Operator kawiarni

| Operator              | Jest obsługiwany |
| --------------------- | ------------ |
| Wkład                 | ✅            |
| Concat                | ✅            |
| Splot           | ✅            |
| Eltwise •               | ✅            |
| Wymiany               | ✅            |
| relu                  | ✅            |
| Przekształcić               | ✅            |
| Kawałek                 | ✅            |
| Softmax               | ✅            |
| Rozszczepiać                 | ✅            |
| KontynuacjaIndektor | ✅            |
| Buforowanie               | ✅            |
| BatchNorm             | ✅            |
| Skala                 | ✅            |
| Rewers               | ✅            |
| LSTM                  | ✅            |
| Produkt wewnętrzny          | ✅            |

## 4.2 Kompilowanie interfejsów API modelu

Obecnie interfejs API modelu kompilacji obsługuje struktury głębokiego uczenia, takie jak tflite / onnx / caffe.

### 4.2.1 CompileOptions

**Opis funkcji**

Klasa CompileOptions do konfigurowania opcji kompilacji nncase

**Definicja klasy**

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

Każda właściwość jest opisana poniżej

| Nazwa nieruchomości         | typ   | Tak lub nie | opis                                                         |
| ---------------- | ------ | -------- | ------------------------------------------------------------ |
| cel           | struna | być       | Określ cel kompilacji, taki jak "k210", "k510"                               |
| quant_type       | struna | nie       | Określ typ kwantyzacji danych, na przykład "uint8", "int8"                          |
| w_quant_type     | struna | nie       | Określ typ kwantyzacji wagi, na przykład "uint8", "int8", domyślnie "uint8"           |
| use_mse_quant_w  | Bool   | nie       | Określa, czy algorytm błędu średniego kwadratu (MSE) ma być używany do optymalizacji parametrów kwantyzacji podczas kwantyzacji wag |
| split_w_to_act   | Bool   | nie       | Określa, czy dane o częściowej wadze mają być równoważone w dane aktywne.                       |
| przetwarzanie wstępne       | Bool   | nie       | Niezależnie od tego, czy przetwarzanie wstępne jest włączone, czy nie, wartością domyślną jest Fałsz                                  |
| swapRB           | Bool   | nie       | Niezależnie od tego, czy dane wejściowe RGB mają być wymieniane między kanałami czerwonym i niebieskim (RGB--> BGR lub BGR->RGB), domyślnie jest to False |
| znaczyć             | lista   | nie       | Wstępne przetwarzanie normalizuje parametr mean, który domyślnie jest ustawiony na[0, 0, 0]                        |
| Std              | lista   | nie       | Wstępne przetwarzanie normalizuje wariancję parametru, która domyślnie wynosi[1, 1, 1]                        |
| input_range      | lista   | nie       | Zakres liczb zmiennoprzecinkowych po kwantyzacji danych wejściowych, który domyślnie wynosi[0，1]               |
| output_range     | lista   | nie       | Zakres liczb zmiennoprzecinkowych przed wyjściem danych stałoprzecinkowych, który domyślnie jest pusty                     |
| input_shape      | lista   | nie       | Określ kształt danych wejściowych, układ input_shape musi być spójny z układem wejściowym, a input_shape danych wejściowych jest niespójna z kształtem wejściowym modelu, a operacja bitbox (zmiana rozmiaru / pad itp.) zostanie wykonana. |
| letterbox_value  | spławik  | nie       | Określa wartość wypełnienia wstępnie przetwarzanego pola pobierania                                  |
| input_type       | struna | nie       | Określa typ danych wejściowych, domyślnie "float32"                          |
| output_type      | struna | nie       | Określa typ danych wyjściowych, takich jak "float32", "uint8" (tylko dla określonej kwantyzacji), domyślnie jest to "float32" |
| input_layout     | struna | nie       | Określ układ danych wejściowych, takich jak "NCHW", "NHWC". Jeśli układ danych wejściowych różni się od samego modelu, wstawki nncase transponują do konwersji |
| output_layout    | struna | nie       | Określ dane wyjściowe dla układu, takie jak "NCHW", "NHWC". Jeśli układ danych wyjściowych różni się od samego modelu, nncase wstawi transpozycję do konwersji |
| model_layout     | struna | nie       | Określ układ modelu, który domyślnie jest pusty, i określ, kiedy układ modelu tflite to "NCHW", a modele Onnx i Caffe to "NHWC" |
| is_fpga          | Bool   | nie       | Określa, czy kmodel jest używany dla układów FPGA, co domyślnie ma wartość False                          |
| dump_ir          | Bool   | nie       | Określa, czy wartość domyślna zrzutu podczerwieni ma wartość False                                 |
| dump_asm         | Bool   | nie       | Określa, czy plik zestawu zrzutu asm, który domyślnie ma wartość False                        |
| dump_quant_error | Bool   | nie       | Określa, czy zrzut kwantyfikuje błąd modelu przed i po                               |
| dump_dir         | struna | nie       | Po wcześniejszym określeniu dump_ir i innych przełączników, tutaj określasz katalog zrzutu, który domyślnie jest pustym ciągiem  |
| benchmark_only   | Bool   | nie       | Określa, czy kmodel jest używany tylko do testu porównawczego, który domyślnie ma wartość False                   |

> 1. Zakres wejściowy to zakres liczb zmiennoprzecinkowych, to znaczy, jeśli typem danych wejściowych jest uint8, to zakres wejściowy jest zakresem po dekwantacji do zmiennoprzecinkowego (nie może być 0 ~ 1), który można dowolnie określić.
> 2. input_shape muszą być określone zgodnie z input_layout, [1，224，224，3]na przykład, jeśli input_layout jest NCHW, input_shape musi być określony jako[1,3,224,224]; input_layout jest NHWC, input_shape należy określić jako[1,224,224,3]; 
> 3. średnia i std są parametrami normalizującymi liczby zmiennoprzecinkowe, które użytkownik może dowolnie określić;
> 4. Podczas korzystania z funkcji skrzynki na listy należy ograniczyć rozmiar wejściowy do 1,5 MB, a rozmiar pojedynczego kanału mieści się w granicach 0,75 MB;
>
> Na przykład:
>
> 1. Typ danych wejściowych jest ustawiony na uint8, input_range ustawiony na[0,255], rolą dekwantyzacji jest tylko konwersja typu, konwersja danych uint8 na float32, a parametry średniej i std można nadal określić zgodnie z danymi 0 ~ 255
> 2. Typ danych wejściowych jest ustawiony na uint8, input_range ustawiony[0,1] na, liczba stała jest dekwantowana na liczbę [0,1]zmiennoprzecinkową w zakresie, a średnia i std muszą być określone zgodnie z nowym zakresem liczb zmiennoprzecinkowych. 

Proces wstępnego przetwarzania jest następujący (zielone węzły na rysunku są opcjonalne):

![przetwarzanie wstępne.png](https://i.loli.net/2021/11/08/fhBLsozUTCbt4dp.png)

**Przykład kodu**

Utwórz wystąpienie CompileOptions, skonfiguruj wartości każdej właściwości

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

**Opis funkcji**

Klasa ImportOptions do konfigurowania opcji importu nncase

**Definicja klasy**

```python
py::class_<import_options>(m, "ImportOptions")
    .def(py::init())
    .def_readwrite("output_arrays", &import_options::output_arrays);
```

Każda właściwość jest opisana poniżej

| Nazwa nieruchomości      | typ   | Tak lub nie | opis     |
| ------------- | ------ | -------- | -------- |
| output_arrays | struna | nie       | Nazwa wyjściowa |

**Przykład kodu**

Utwórz instancję ImageOptions, skonfiguruj wartości każdej właściwości

```python
# import_options
import_options = nncase.ImportOptions()
import_options.output_arrays = 'output' # Your output node name
```

### 4.2.3 PTQTensorOptions

**Opis funkcji**

Klasa PTQTensorOptions do konfigurowania opcji PTQ nncase

**Definicja klasy**

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

Każda właściwość jest opisana poniżej

| Nazwa pola         | typ   | Tak lub nie | opis                                                                                  |
| ---------------- | ------ | -------- | ------------------------------------------------------------------------------------- |
| calibrate_method | struna | nie       | Metoda kalibracji, obsługuje "no_clip", "l2", "kld_m0", "kld_m1", "kld_m2", "cdf", domyślnie jest to "no_clip" |
| samples_count    | Int    | nie       | Liczba próbek                                                                              |

#### set_tensor_data()

**Opis funkcji**

Ustawianie danych korekty

**Definicja interfejsu**

```python
set_tensor_data(calib_data)
```

**Parametry wejściowe**

| Nazwa parametru   | typ   | Tak lub nie | opis     |
| ---------- | ------ | -------- | -------- |
| calib_data | bajt[] | być       | Popraw dane |

**Zwracana wartość**

N/A

**Przykład kodu**

```python
# ptq_options
ptq_options = nncase.PTQTensorOptions()
ptq_options.samples_count = cfg.generate_calibs.batch_size
ptq_options.set_tensor_data(np.asarray([sample['data'] for sample in self.calibs]).tobytes())
```

### 4.2.4 Kompilator

**Opis funkcji**

Klasa kompilatora do kompilacji modeli sieci neuronowych

**Definicja klasy**

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

**Przykład kodu**

```python
compiler = nncase.Compiler(compile_options)
```

#### import_tflite()

**Opis funkcji**

Importowanie modelu tflite

**Definicja interfejsu**

```python
import_tflite(model_content, import_options)
```

**Parametry wejściowe**

| Nazwa parametru       | typ          | Tak lub nie | opis           |
| -------------- | ------------- | -------- | -------------- |
| model_content  | bajt[]        | być       | Przeczytaj zawartość modelu |
| import_options | ImportOptions | być       | Opcje importu       |

**Zwracana wartość**

N/A

**Przykład kodu**

```python
model_content = read_model_file(model)
compiler.import_tflite(model_content, import_options)
```

#### import_onnx()

**Opis funkcji**

Importowanie modelu onnx

**Definicja interfejsu**

```python
import_onnx(model_content, import_options)
```

**Parametry wejściowe**

| Nazwa parametru       | typ          | Tak lub nie | opis           |
| -------------- | ------------- | -------- | -------------- |
| model_content  | bajt[]        | być       | Przeczytaj zawartość modelu |
| import_options | ImportOptions | być       | Opcje importu       |

**Zwracana wartość**

N/A

**Przykład kodu**

```python
model_content = read_model_file(model)
compiler.import_onnx(model_content, import_options)
```

#### import_caffe()

**Opis funkcji**

Importowanie modelu kawiarni

> Użytkownicy muszą skompilować/zainstalować caffe na komputerze lokalnym.

**Definicja interfejsu**

```python
import_caffe(caffemodel, prototxt)
```

**Parametry wejściowe**

| Nazwa parametru   | typ   | Tak lub nie | opis                 |
| ---------- | ------ | -------- | -------------------- |
| caffemodel | bajt[] | być       | Przeczytaj zawartość caffemodel |
| prototxt   | bajt[] | być       | Przeczytaj zawartość prototxt   |

**Zwracana wartość**

N/A

**Przykład kodu**

```python
# import
caffemodel = read_model_file('test.caffemodel')
prototxt = read_model_file('test.prototxt')
compiler.import_caffe(caffemodel, prototxt)
```

#### use_ptq()

**Opis funkcji**

Ustawianie opcji konfiguracji PTQ

**Definicja interfejsu**

```python
use_ptq(ptq_options)
```

**Parametry wejściowe**

| Nazwa parametru    | typ             | Tak lub nie | opis        |
| ----------- | ---------------- | -------- | ----------- |
| ptq_options | PTQTensorOptions | być       | Opcje konfiguracji PTQ |

**Zwracana wartość**

N/A

**Przykład kodu**

```python
compiler.use_ptq(ptq_options)
```

#### compile()

**Opis funkcji**

Skompiluj model sieci neuronowej

**Definicja interfejsu**

```python
compile()
```

**Parametry wejściowe**

N/A

**Zwracana wartość**

N/A

**Przykład kodu**

```python
compiler.compile()
```

#### gencode_tobytes()

**Opis funkcji**

Generuje strumień bajtów kodu

**Definicja interfejsu**

```python
gencode_tobytes()
```

**Parametry wejściowe**

N/A

**Zwracana wartość**

Bajtów[]

**Przykład kodu**

```python
kmodel = compiler.gencode_tobytes()
with open(os.path.join(infer_dir, 'test.kmodel'), 'wb') as f:
    f.write(kmodel)
```

## 4.3 Skompiluj przykład modelu

W poniższym przykładzie użyto modelu i skryptu kompilacji pythona

- Model znajduje się w podkatalogu /path/to/nncase_sdk/examples/models/
- Skrypt kompilacji Pythona znajduje się w podkatalogu /path/to/nncase_sdk/examples/scripts

### 4.3.1 Skompiluj model tflite float32

- Mobilenetv2_tflite_fp32_image.py skrypt jest następujący:

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

- Uruchom następujące polecenie, aby skompilować model tflite mobiletv2, target k510

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_tflite_fp32_image.py --target k510 --model models/mobilenet_v2_1.0_224.tflite
```

### 4.3.2 Skompiluj model float32 onnx

- W przypadku modeli onnx zaleca się uproszczenie korzystania z[ ONNX Simplifier ](https://github.com/daquexian/onnx-simplifier)przed skompilowaniem z nncase
- mobilenetv2_onnx_fp32_image.py skrypt jest następujący:

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

- Uruchom następujące polecenie, aby skompilować model onnx mobiletv2, target k510

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_onnx_fp32_image.py --target k510 --model models/mobilenetv2-7.onnx
```

### 4.3.3 Skompiluj model caffe float32

- Pakiet kół caffe pochodzi[  z ](https://github.com/kendryte/caffe/releases)kendryte caffe
- conv2d_caffe_fp32.py skrypt jest następujący:

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

- Uruchom następujące polecenie, aby skompilować model caffe conv2d z docelowym k510

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/conv2d_caffe_fp32.py --target k510 --caffemodel models/test.caffemodel --prototxt models/test.prototxt
```

### 4.3.4 Skompiluj i dodaj wstępny model float32 onnx

- W przypadku modeli onnx zaleca się uproszczenie korzystania z[ ONNX Simplifier ](https://github.com/daquexian/onnx-simplifier)przed skompilowaniem z nncase
- Mobilenetv2_onnx_fp32_preprocess.py skrypt jest następujący:

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

- Uruchom następujące polecenie, aby skompilować model onnx mobiletv2 z docelowym k510

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_onnx_fp32_preprocess.py --target k510 --model models/mobilenetv2-7.onnx
```

### 4.3.5 Skompiluj model tflite kwantyzacji uint8

- Mobilenetv2_tflite_uint8_image.py skrypt jest następujący

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

- Uruchom następujące polecenie, aby skompilować model tflite skwantyzowanego mobiletv2 uint8, docelowego k510

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_tflite_uint8_image.py --target k510 --model models/mobilenet_v2_1.0_224.tflite
```

## 4.4 Interfejsy API modelu wnioskowania

Oprócz punktów dostępowych skompilowanego modelu, nncase zapewnia również interfejsy API modelu wnioskowania, które można wywnioskować na komputerze przed kompilacją kmodel, który służy do weryfikacji, czy wyniki wnioskowania nncase i wyniki środowiska uruchomieniowego odpowiedniej struktury głębokiego uczenia są spójne.

### 4.4.1 MemoryRange

**Opis funkcji**

Klasa MemoryRange, która jest używana do reprezentowania zakresu pamięci

**Definicja klasy**

```python
py::class_<memory_range>(m, "MemoryRange")
    .def_readwrite("location", &memory_range::memory_location)
    .def_property(
        "dtype", [](const memory_range &range) { return to_dtype(range.datatype); },
        [](memory_range &range, py::object dtype) { range.datatype = from_dtype(py::dtype::from_args(dtype)); })
    .def_readwrite("start", &memory_range::start)
    .def_readwrite("size", &memory_range::size);
```

Każda właściwość jest opisana poniżej

| Nazwa nieruchomości | typ           | Tak lub nie | opis                                                                       |
| -------- | -------------- | -------- | -------------------------------------------------------------------------- |
| lokalizacja | Int            | nie       | Pozycja pamięci, 0 dla wejścia, 1 dla wyjścia, 2 dla rdata, 3 dla danych, 4 dla shared_data |
| dtype    | Typ danych języka Python | nie       | typ danych                                                                   |
| początek    | Int            | nie       | Adres początkowy pamięci                                                               |
| rozmiar     | Int            | nie       | Rozmiar pamięci                                                                   |

**Przykład kodu**

Tworzenie wystąpienia MemoryRange

```python
mr = nncase.MemoryRange()
```

### 4.4.2 RuntimeTensor

**Opis funkcji**

Klasa RuntimeTensor, która reprezentuje tensor środowiska wykonawczego

**Definicja klasy**

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

Każda właściwość jest opisana poniżej

| Nazwa nieruchomości | typ | Tak lub nie | opis             |
| -------- | ---- | -------- | ---------------- |
| dtype    | Int  | nie       | Typ danych Tensora |
| kształt    | lista | nie       | Kształt tensora     |

#### from_numpy()

**Opis funkcji**

Skonstruuj obiekt RuntimeTensor z numpy.ndarray

**Definicja interfejsu**

```python
from_numpy(py::array arr)
```

**Parametry wejściowe**

| Nazwa parametru | typ          | Tak lub nie | opis              |
| -------- | ------------- | -------- | ----------------- |
| Arr      | numpy.ndarray | być       | Obiekt numpy.ndarray |

**Zwracana wartość**

RuntimeTensor

**Przykład kodu**

```python
tensor = nncase.RuntimeTensor.from_numpy(self.inputs[i]['data'])
```

#### copy_to()

**Opis funkcji**

Kopiuj tensor runtime

**Definicja interfejsu**

```python
copy_to(RuntimeTensor to)
```

**Parametry wejściowe**

| Nazwa parametru | typ          | Tak lub nie | opis              |
| -------- | ------------- | -------- | ----------------- |
| do       | RuntimeTensor | być       | Obiekt RuntimeTensor |

**Zwracana wartość**

N/A

**Przykład kodu**

```python
sim.get_output_tensor(i).copy_to(to)
```

#### to_numpy()

**Opis funkcji**

Konwertowanie RuntimeTensor na obiekt numpy.ndarray

**Definicja interfejsu**

```python
to_numpy()
```

**Parametry wejściowe**

N/A

**Zwracana wartość**

Obiekt numpy.ndarray

**Przykład kodu**

```python
arr = sim.get_output_tensor(i).to_numpy()
```

### 4.4.3 Symulator

**Opis funkcji**

Klasa symulatora wnioskowania kmodel na PC

**Definicja klasy**

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

Każda właściwość jest opisana poniżej

| Nazwa nieruchomości     | typ | Tak lub nie | opis     |
| ------------ | ---- | -------- | -------- |
| inputs_size  | Int  | nie       | Wprowadź numer |
| outputs_size | Int  | nie       | Liczba wyjść |

**Przykład kodu**

Tworzenie wystąpienia symulatora

```python
sim = nncase.Simulator()
```

#### load_model()

**Opis funkcji**

Załaduj kmodel

**Definicja interfejsu**

```python
load_model(model_content)
```

**Parametry wejściowe**

| Nazwa parametru      | typ   | Tak lub nie | opis         |
| ------------- | ------ | -------- | ------------ |
| model_content | bajt[] | być       | Strumień bajtów Kmodel |

**Zwracana wartość**

N/A

**Przykład kodu**

```python
sim.load_model(kmodel)
```

#### get_input_desc()

**Opis funkcji**

Pobiera opis danych wejściowych dla określonego indeksu

**Definicja interfejsu**

```python
get_input_desc(index)
```

**Parametry wejściowe**

| Nazwa parametru | typ | Tak lub nie | opis       |
| -------- | ---- | -------- | ---------- |
| indeks    | Int  | być       | Indeks danych wejściowych |

**Zwracana wartość**

MemoryRange

**Przykład kodu**

```python
input_desc_0 = sim.get_input_desc(0)
```

#### get_output_desc()

**Opis funkcji**

Pobiera opis danych wyjściowych określonego indeksu

**Definicja interfejsu**

```python
get_output_desc(index)
```

**Parametry wejściowe**

| Nazwa parametru | typ | Tak lub nie | opis       |
| -------- | ---- | -------- | ---------- |
| indeks    | Int  | być       | Indeks wyniku |

**Zwracana wartość**

MemoryRange

**Przykład kodu**

```python
output_desc_0 = sim.get_output_desc(0)
```

#### get_input_tensor()

**Opis funkcji**

Pobiera RuntimeTensor dla danych wejściowych dla określonego indeksu

**Definicja interfejsu**

```python
get_input_tensor(index)
```

**Parametry wejściowe**

| Nazwa parametru | typ | Tak lub nie | opis             |
| -------- | ---- | -------- | ---------------- |
| indeks    | Int  | być       | Wprowadź indeks tensora |

**Zwracana wartość**

RuntimeTensor

**Przykład kodu**

```python
input_tensor_0 = sim.get_input_tensor(0)
```

#### set_input_tensor()

**Opis funkcji**

Ustawia tensor czasu wykonawczego dla wprowadzania określonego indeksu

**Definicja interfejsu**

```python
set_input_tensor(index, tensor)
```

**Parametry wejściowe**

| Nazwa parametru | typ          | Tak lub nie | opis                    |
| -------- | ------------- | -------- | ----------------------- |
| indeks    | Int           | być       | Wprowadź indeks RuntimeTensor |
| tensor   | RuntimeTensor | być       | Wejdź do RuntimeTensor       |

**Zwracana wartość**

N/A

**Przykład kodu**

```python
sim.set_input_tensor(0, nncase.RuntimeTensor.from_numpy(self.inputs[0]['data']))
```

#### get_output_tensor()

**Opis funkcji**

Pobiera tensor runtime dla danych wyjściowych określonego indeksu

**Definicja interfejsu**

```python
get_output_tensor(index)
```

**Parametry wejściowe**

| Nazwa parametru | typ | Tak lub nie | opis                    |
| -------- | ---- | -------- | ----------------------- |
| indeks    | Int  | być       | Wyprowadza indeks RuntimeTensor |

**Zwracana wartość**

RuntimeTensor

**Przykład kodu**

```python
output_arr_0 = sim.get_output_tensor(0).to_numpy()
```

#### set_output_tensor()

**Opis funkcji**

Ustawia Napięcie wykonawcze dla danych wyjściowych określonego indeksu

**Definicja interfejsu**

```python
set_output_tensor(index, tensor)
```

**Parametry wejściowe**

| Nazwa parametru | typ          | Tak lub nie | opis                    |
| -------- | ------------- | -------- | ----------------------- |
| indeks    | Int           | być       | Wyprowadza indeks RuntimeTensor |
| tensor   | RuntimeTensor | być       | Wyjściowy tensor czasu wykonawczego       |

**Zwracana wartość**

N/A

**Przykład kodu**

```python
sim.set_output_tensor(0, tensor)
```

#### run()

**Opis funkcji**

Uruchamianie wnioskowania kmodel

**Definicja interfejsu**

```python
run()
```

**Parametry wejściowe**

N/A

**Zwracana wartość**

N/A

**Przykład kodu**

```python
sim.run()
```

## 4.5 Przykład modelu wnioskowania

**Wymagane umiejętności: **mobilenetv2_onnx_fp32_image.py skrypt został skompilowany z modelem mobiletv2-7.onnx

mobilenetv2_onnx_simu.py znajduje się w podkatalogu /path/to/nncase_sdk/examples/scripts, który brzmi następująco:

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

Wykonywanie skryptu wnioskowania

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_onnx_simu.py --model_file models/mobilenetv2-7.onnx --kmodel_file tmp/mobilenetv2_onnx_fp32_image/test.kmodel --input_file mobilenetv2_onnx_fp32_image/data/input_0_0.bin
```

Porównanie wyników symulatora nncase i wnioskowania procesora jest następujące:

```shell
... ...
output 0 cosine similarity : 0.9992437958717346
```

# Biblioteka uruchomieniowa 5 nncase

## 5.1 Wprowadzenie do środowiska uruchomieniowego nncase

Środowisko uruchomieniowe nncase służy do ładowania kmodel na urządzeniach AI / ustawiania danych wejściowych / wykonywania obliczeń KPU / uzyskiwania danych wyjściowych itp.

Obecnie tylko** wersja C++ **interfejsów API, powiązane pliki nagłówkowe i biblioteki statyczne są dostępne w katalogu nncase sdk/riscv64

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

## 5.2 Interfejsy API środowiska wykonawczego

### 5.2.1 runtime_tensor klasy

Tensor używany do przechowywania danych wejściowych/wyjściowych modelu

#### hrt::create()

**Opis funkcji**

Tworzenie runtime_tensor

**Definicja interfejsu**

```C++
(1) NNCASE_API result<runtime_tensor> create(datatype_t datatype, runtime_shape_t shape, memory_pool_t pool = pool_cpu_only, uintptr_t physical_address = 0) noexcept;

(2) NNCASE_API result<runtime_tensor> create(datatype_t datatype, runtime_shape_t shape, gsl::span<gsl::byte> data, bool copy, memory_pool_t pool = pool_cpu_only, uintptr_t physical_address = 0) noexcept;
```

**Parametry wejściowe**

| Nazwa parametru         | typ                  | Tak lub nie | opis                              |
| ---------------- | --------------------- | -------- | --------------------------------- |
| Datatype         | datatype_t            | być       | Typ danych, na przykład dt_float32            |
| kształt            | runtime_shape_t       | być       | Kształt tensora                      |
| dane             | gsl::span\<gsl::byte> | być       | Bufor danych stanu użytkownika                  |
| kopiować             | Bool                  | być       | Czy kopiować                          |
| basen             | memory_pool_t         | nie       | Typ puli pamięci, wartość domyślna to pool_cpu_only |
| physical_address | uintptr_t             | nie       | Adres fizyczny, wartość domyślna to 0               |

**Zwracana wartość**

wynik<runtime_tensor>

Przykład kodu

```c++
// create input
auto in_shape = interp.input_shape(0);
auto input_tensor = host_runtime_tensor::create(dt_float32, in_shape,
                                                {(gsl::byte *)mat.data, mat.cols * mat.rows * mat.elemSize()},
                                                true, hrt::pool_shared).expect("cannot create input tensor");
```

### 5.2.2 tłumacz klasowy

Interpreter jest uruchomioną instancją środowiska wykonawczego nncase, która udostępnia podstawowe funkcje funkcjonalne, takie jak load_model()/run()/input_tensor()/output_tensor().

#### load_model()

**Opis funkcji**

Załaduj model kmodel

**Definicja interfejsu**

```C++
 NNCASE_NODISCARD result<void> load_model(gsl::span<const gsl::byte> buffer) noexcept;
```

**Parametry wejściowe**

| Nazwa parametru | typ                            | Tak lub nie | opis          |
| -------- | ------------------------------- | -------- | ------------- |
| bufor   | gsl::span `<const gsl::byte>` | być       | bufor kmodel |

**Zwracana wartość**

wynik `<void>`

**Przykład kodu**

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

**Opis funkcji**

Pobiera liczbę wejść modelu

**Definicja interfejsu**

```C++
size_t inputs_size() const noexcept;
```

**Parametry wejściowe**

N/A

**Zwracana wartość**

size_t

**Przykład kodu**

```c++
auto inputs_size = interp.inputs_size();
```

#### outputs_size()

**Opis funkcji**

Pobiera liczbę danych wyjściowych modelu

**Definicja interfejsu**

```C++
size_t outputs_size() const noexcept;
```

**Parametry wejściowe**

N/A

**Zwracana wartość**

size_t

**Przykład kodu**

```c++
auto outputs_size = interp.outputs_size();
```

#### input_shape()

**Opis funkcji**

Pobiera kształt określonego modelu wejściowego

**Definicja interfejsu**

```C++
const runtime_shape_t &input_shape(size_t index) const noexcept;
```

**Parametry wejściowe**

| Nazwa parametru | typ   | Tak lub nie | opis       |
| -------- | ------ | -------- | ---------- |
| indeks    | size_t | być       | Indeks danych wejściowych |

**Zwracana wartość**

runtime_shape_t

**Przykład kodu**

```c++
auto in_shape = interp.input_shape(0);
```

#### output_shape()

**Opis funkcji**

Pobiera kształt określonego wyjścia modelu

**Definicja interfejsu**

```C++
const runtime_shape_t &output_shape(size_t index) const noexcept;
```

**Parametry wejściowe**

| Nazwa parametru | typ   | Tak lub nie | opis       |
| -------- | ------ | -------- | ---------- |
| indeks    | size_t | być       | Indeks wyniku |

**Zwracana wartość**

runtime_shape_t

**Przykład kodu**

```c++
auto out_shape = interp.output_shape(0);
```

#### input_tensor()

**Opis funkcji**

Pobiera/ustawia tensor wejściowy dla określonego indeksu

**Definicja interfejsu**

```C++
(1) result<runtime_tensor> input_tensor(size_t index) noexcept;
(2) result<void> input_tensor(size_t index, runtime_tensor tensor) noexcept;
```

**Parametry wejściowe**

| Nazwa parametru | typ           | Tak lub nie | opis                     |
| -------- | -------------- | -------- | ------------------------ |
| indeks    | size_t         | być       | bufor kmodel            |
| tensor   | runtime_tensor | być       | Wprowadź odpowiedni tensor czasu wykonania |

**Zwracana wartość**

(1) Zwraca wyniki.<runtime_tensor>

(2) Zwraca wyniki. `<void>`

**Przykład kodu**

```c++
// set input
interp.input_tensor(0, input_tensor).expect("cannot set input tensor");
```

#### output_tensor()

**Opis funkcji**

Pobiera/ustawia tensor wychodzący dla określonego indeksu

**Definicja interfejsu**

```C++
(1) result<runtime_tensor> output_tensor(size_t index) noexcept;
(2) result<void> output_tensor(size_t index, runtime_tensor tensor) noexcept;
```

**Parametry wejściowe**

| Nazwa parametru | typ           | Tak lub nie | opis                     |
| -------- | -------------- | -------- | ------------------------ |
| indeks    | size_t         | być       |                          |
| tensor   | runtime_tensor | być       | Wprowadź odpowiedni tensor czasu wykonania |

**Zwracana wartość**

(1) Zwraca wyniki.<runtime_tensor>

(2) Zwraca wyniki. `<void>`

**Przykład kodu**

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

**Opis funkcji**

Wykonywanie obliczeń kPU

**Definicja interfejsu**

```C++
result<void> run() noexcept;
```

**Parametry wejściowe**

N/A

**Zwracana wartość**

wynik `<void>`

**Przykład kodu**

```c++
// run
interp.run().expect("error occurred in running model");
```

## 5.3 Przykład środowiska wykonawczego

Przykładowy kod znajduje się w /ścieżka/do/nncase_sdk/przykłady/mobilenetv2_onnx_fp32_image

**Warunek prefiksu**

- mobilenetv2_onnx_fp32_image.py skrypt skompilował model mobiletv2-7.onnx
- Ponieważ przykład opiera się na bibliotece OpenCV, należy określić ścieżkę do OpenCV w .txt CMakeLists przykładu.

**Kompilowanie aplikacji krzyżowych**

```shell
cd /path/to/nncase_sdk/examples
./build.sh
```

Na koniec wygeneruj mobilenetv2_onnx_fp32_image w katalogu out/bin

**K510 EVB działa na płycie**

Skopiuj następujące pliki na płytkę k510 EVB

| plik                        | uwaga                                                         |
| --------------------------- | ------------------------------------------------------------ |
| mobilenetv2_onnx_fp32_image | Generowane są przykłady kompilacji krzyżowych                                         |
| test.kmodel                 | Użyj mobilenetv2_onnx_fp32_image.py skompilować kompilację mobiletv2-7.onnx |
| .png i labels_1000.txt cat    | Znajduje się w podkatalogu /path/to/nncase_sdk/examples/mobilenetv2_onnx_fp32_image/data/ |

```bash
$ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mnt/zhangyang/nncase_check/lib/gomp:/mnt/zhangyang/nncase_check/lib/opencv
$ ./mobilenetv2_onnx_fp32_image test.kmodel cat.png labels_1000.txt
case ./mobilenetv2_onnx_fp32_image build at Mar  1 2022 16:31:29
interp.run() duration: 12.6642 ms
image classification result: tiger cat(9.25)
```

# 6 Funkcjonalne biblioteki programistyczne (obsługa środowiska uruchomieniowego)

## 6.1 Wprowadzenie do funkcjonalnego

nncase Functional służy do poprawy łatwości użytkowania, gdy użytkownicy modeli przed i po procesie

Obecnie dostępna jest tylko wersja interfejsów API w języku C++, a skojarzone pliki nagłówkowe i biblioteki znajdują się w katalogu riscv64 zestawu sdk nncase.

## 6.2 Interfejsy API

### 6.2.1 kwadrat

**Opis funkcji**

Oblicz kwadrat, obecnie obsługuje wejście uint8 / int8, wyjście jest również uint8 / int8, zauważ, że wejście jest stałym punktem, a wyjście jest zmiennoprzecinkowe, aby ustawić parametry kwantyzacji.

**Definicja interfejsu**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`square`](#ops_8h_1adff2f60c7c045a9840519eab2c04d127)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parametry wejściowe**

| Nazwa parametru  | typ           | Tak lub nie | opis                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | być       | wkład                |
| `dtype` | datatype_t     | być       | Typ danych tensora wyjściowego |

**Zwracana wartość**

`result<runtime_tensor>`

**Przykład kodu**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto squared = F::square(input, output_type).unwrap_or_throw();
```

### 6.2.2 sqrt

**Opis funkcji**

Oblicz wartość liczby głównej, obecnie obsługuje wejście uint8 / int8, wyjście to również uint8 / int8, zauważ, że wejście jest stałym punktem, a wyjście jest zmiennoprzecinkowe musi ustawić parametry kwantyzacji.

**Definicja interfejsu**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`sqrt`](#ops_8h_1a53f8dde3dd4e27058b5dc743eb5dd076)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parametry wejściowe**

| Nazwa parametru  | typ           | Tak lub nie | opis                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | być       | wkład                |
| `dtype` | datatype_t     | być       | Typ danych tensora wyjściowego |

**Zwracana wartość**

`result<runtime_tensor>`

**Przykład kodu**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::sqrt(input, output_type).unwrap_or_throw();
```

### 6.2.3 dziennik

**Opis funkcji**

Oblicz wartość dziennika, ujemna liczba danych wejściowych zostanie przekonwertowana na Nan, obecnie obsługuje wejście uint8 / int8, wyjście to również uint8 / int8, zauważ, że wejście jest stałym punktem, a wyjście jest zmiennoprzecinkowe musi ustawić parametr kwantyzacji.

**Definicja interfejsu**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`log`](#ops_8h_1a91df53276c3f1511427d4ac1a0140b71)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parametry wejściowe**

| Nazwa parametru  | typ           | Tak lub nie | opis                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | być       | wkład                |
| `dtype` | datatype_t     | być       | Typ danych tensora wyjściowego |

**Zwracana wartość**

`result<runtime_tensor>`

**Przykład kodu**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::log(input, output_type).unwrap_or_throw();
```

### 6.2.4 wersja exp

**Opis funkcji**

Oblicz wartość exp, obecnie obsługuje wejście uint8 / int8, wyjście to również uint8 / int8, zauważ, że wejście jest stałym punktem, a wyjście jest zmiennoprzecinkowe, aby ustawić parametry kwantyzacji.

**Definicja interfejsu**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`exp`](#ops_8h_1a2c6ce457805a5ba515fa7454fb4aede0)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parametry wejściowe**

| Nazwa parametru  | typ           | Tak lub nie | opis                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | być       | wkład                |
| `dtype` | datatype_t     | być       | Typ danych tensora wyjściowego |

**Zwracana wartość**

`result<runtime_tensor>`

**Przykład kodu**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::exp(input, output_type).unwrap_or_throw();
```

### 6.2.5 bez

**Opis funkcji**

Aby obliczyć wartość sin, wejście uint8 / int8 jest obecnie obsługiwane, a wyjście jest również uint8 / int8, zauważ, że parametry kwantyzacji muszą być ustawione, gdy wejście jest stałoprzecinkowe, a wyjście jest zmiennoprzecinkowe.

**Definicja interfejsu**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`sin`](#ops_8h_1a9605b2b0dc9a6892ce878bda14586890)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parametry wejściowe**

| Nazwa parametru  | typ           | Tak lub nie | opis                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | być       | wkład                |
| `dtype` | datatype_t     | być       | Typ danych tensora wyjściowego |

**Zwracana wartość**

`result<runtime_tensor>`

**Przykłady kodu**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::sin(input, output_type).unwrap_or_throw();
```

### 6.2.6 nadwozie

**Opis funkcji**

Oblicz wartość cos, obecnie obsługuje wejście uint8 / int8, wyjście to również uint8 / int8, zauważ, że wejście jest stałym punktem, a wyjście jest zmiennoprzecinkowe musi ustawić parametr kwantyzacji.

**Definicja interfejsu**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`cos`](#ops_8h_1a71d36c13c82f4c411f24d030cf333249)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parametry wejściowe**

| Nazwa parametru  | typ           | Tak lub nie | opis                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | być       | wkład                |
| `dtype` | datatype_t     | być       | Typ danych tensora wyjściowego |

**Zwracana wartość**

`result<runtime_tensor>`

**Przykłady kodu**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::cos(input, output_type).unwrap_or_throw();
```

### 6.2.7 runda

**Opis funkcji**

Aby obliczyć okrągłą wartość, wejście uint8 / int8 jest obecnie obsługiwane, a wyjście jest również uint8 / int8, zauważ, że parametr kwantyzacji musi być ustawiony, gdy wejście jest stałe, a wyjście jest zmiennoprzecinkowe.

**Definicja interfejsu**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`round`](#ops_8h_1a81db8ac4866004f75fb65db876262785)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parametry wejściowe**

| Nazwa parametru  | typ           | Tak lub nie | opis                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | być       | wkład                |
| `dtype` | datatype_t     | być       | Typ danych tensora wyjściowego |

**Zwracana wartość**

`result<runtime_tensor>`

**Przykłady kodu**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::round(input, output_type).unwrap_or_throw();
```

### 6.2.8 piętro

**Opis funkcji**

Oblicz wartość mrozu, obecnie obsługuje wejście uint8 / int8, wyjście to również uint8 / int8, zauważ, że wejście jest stałym punktem, a wyjście jest zmiennoprzecinkowe, aby ustawić parametry kwantyzacji.

**Definicja interfejsu**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`floor`](#ops_8h_1a1079af8fe9fb6edbb2906d91fac12635)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parametry wejściowe**

| Nazwa parametru  | typ           | Tak lub nie | opis                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | być       | wkład                |
| `dtype` | datatype_t     | być       | Typ danych tensora wyjściowego |

**Zwracana wartość**

`result<runtime_tensor>`

**Przykłady kodu**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::floor(input, output_type).unwrap_or_throw();
```

### 6.2.9 ceil

**Opis funkcji**

Oblicz wartość ceil, obecnie obsługuje wejście uint8 / int8, wyjście to również uint8 / int8, zauważ, że wejście jest stałym punktem, a wyjście jest zmiennoprzecinkowe, aby ustawić parametry kwantyzacji.

**Definicja interfejsu**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`ceil`](#ops_8h_1ad3b78c97f1e5348a26de7e5ba2396fb7)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parametry wejściowe**

| Nazwa parametru  | typ           | Tak lub nie | opis                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | być       | wkład                |
| `dtype` | datatype_t     | być       | Typ danych tensora wyjściowego |

**Zwracana wartość**

`result<runtime_tensor>`

**Przykłady kodu**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::ceil(input, output_type).unwrap_or_throw();
```

### 6.2.10 abs

**Opis funkcji**

Oblicz wartość abs, obecnie obsługuje wejście uint8 / int8, wyjście to również uint8 / int8, zauważ, że wejście jest stałym punktem, a wyjście jest zmiennoprzecinkowe musi ustawić parametry kwantyzacji.

**Definicja interfejsu**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`abs`](#ops_8h_1ad8290dc793bae0dc22b3baf9e0f80c14)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parametry wejściowe**

| Nazwa parametru  | typ           | Tak lub nie | opis                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | być       | wkład                |
| `dtype` | datatype_t     | być       | Typ danych tensora wyjściowego |

**Zwracana wartość**

`result<runtime_tensor>`

**Przykłady kodu**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::abs(input, output_type).unwrap_or_throw();
```

### 6.2.11 neg

**Opis funkcji**

Oblicz wartość neg, obecnie obsługuje wejście uint8 / int8, wyjście jest również uint8 / int8, zauważ, że wejście jest stałym punktem, a wyjście jest zmiennoprzecinkowe musi ustawić parametry kwantyzacji.

**Definicja interfejsu**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`neg`](#ops_8h_1aa1b7858802e1afce78db72163c5210d8)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parametry wejściowe**

| Nazwa parametru  | typ           | Tak lub nie | opis                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | być       | wkład                |
| `dtype` | datatype_t     | być       | Typ danych tensora wyjściowego |

**Zwracana wartość**

`result<runtime_tensor>`

**Przykłady kodu**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::neg(input, output_type).unwrap_or_throw();
```

### 6.2.12 kwantyfikować

**Opis funkcji**

dt_bfloat16 wejściowe, dane dt_float32, dt_int8 wyjściowe lub dt_uint8 wyjściowe

**Definicja interfejsu**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`quantize`](#ops_8h_1ad8ad779083b5c08da520d2f1c2469c3a)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parametry wejściowe**

| Nazwa parametru  | typ           | Tak lub nie | opis                                |
| --------- | -------------- | -------- | ----------------------------------- |
| `input` | runtime_tensor | być       | Wejście, typ musi być float32 lub bfloat16 |
| `dtype` | datatype_t     | być       | Typ danych tensora wyjściowego                 |

**Zwracana wartość**

`result<runtime_tensor>`

**Przykłady kodu**

```cpp
auto quantized = F::quantize(input, dt_int8).unwrap_or_throw();
```

### 6.2.13 dekwantyzacja

**Opis funkcji**

Wprowadź dane wejściowe uint8 lub int8, przekonwertuj na dane float lub bfloat. Należy pamiętać, że użytkownik musi wcześniej ustawić poprawne parametry kwantyzacji dla danych w celu dekwantyzacji.

**Definicja interfejsu**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`dequantize`](#ops_8h_1ab91a262349baf393c91abad6f393de24)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parametry wejściowe**

| Nazwa parametru  | typ           | Tak lub nie | opis                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | być       | wkład                |
| `dtype` | datatype_t     | być       | Typ danych tensora wyjściowego |

**Zwracana wartość**

`result<runtime_tensor>`

**Przykłady kodu**

```cpp
input.quant_param({ 0, 1 });
auto dequantized = F::dequantize(input, output_type).unwrap_or_throw();
```

### 6.2.14 uprawa

**Opis funkcji**

Podane bboxy, przycięte z oryginalnego tensora i zmienione rozmiary wyjściowe na nowy tensor. Akceptuj dt_bfloat16, dt_float32, dt_int8, dt_uint8 typ wyjściowy, dane wyjściowe tego samego typu.

**Definicja interfejsu**

`NNCASE_API inline result<runtime::runtime_tensor> crop(runtime::runtime_tensor &input, runtime::runtime_tensor &bbox, size_t out_h, size_t out_w, image_resize_mode_t resize_mode, bool align_corners, bool half_pixel_centers) noexcept`

**Parametry wejściowe**

| Nazwa parametru           | typ                | Tak lub nie | opis                                                                                     |
| ------------------ | ------------------- | -------- | ---------------------------------------------------------------------------------------- |
| wkład              | runtime_tensor      | być       | Wprowadź dane, trzeba [n,c,h,w] sformatować układ, jeśli dane są uint8 lub int8 proszę o zapewnienie poprawności parametrów kwantyzacji danych       |
| bbox               | runtime_tensor      | być       | Wprowadź dane bbox, musisz [1,1,m,4] sformatować układ, dane wewnętrzne są[y0,x0,y1,x1], typ jest[float32,bfloat16] |
| out_h              | size_t              | być       | Wysokość danych wyjściowych                                                                           |
| out_w              | size_t              | być       | Wprowadź szerokość danych                                                                            |
| resize_mode        | image_resize_mode_t | być       | Wzorzec metody Zmiany rozmiaru                                                                           |
| align_corners      | Bool                | być       | Zmień rozmiar, czy align_corners                                                    |
| half_pixel_centers | Bool                | być       | Zmień rozmiar, jeśli piksel jest wyrównany do środka                                                                  |

**Zwracana wartość**

`result<runtime_tensor>`

**Przykłady kodu**

```cpp
auto bbox = get_rand_bbox(input_shape, roi_amount);
auto &&[out_h, out_w] = get_rand_out_hw();
auto output_opt = F::crop(input, bbox, out_h, out_w, resize_mode).unwrap_or_throw();
```

### 6.2.15 zmiana rozmiaru

**Opis funkcji**

Biorąc pod uwagę szerokość wysokości wyjściowej, zmień rozmiar tensora wejściowego na nowy rozmiar. Akceptuj dt_bfloat16, dt_float32, dt_int8, dt_uint8 typ wyjściowy, dane wyjściowe tego samego typu.

**Definicja interfejsu**

`NNCASE_API inline result<runtime::runtime_tensor> resize(runtime::runtime_tensor &input, size_t out_h, size_t out_w, image_resize_mode_t resize_mode, bool align_corners, bool half_pixel_centers) noexcept`

**Parametry wejściowe**

| Nazwa parametru           | typ                | Tak lub nie | opis                                                                               |
| ------------------ | ------------------- | -------- | ---------------------------------------------------------------------------------- |
| wkład              | runtime_tensor      | być       | Wprowadź dane, które należy [n,c,h,w] sformatować, jeśli dane są uint8 lub int8 proszę o zapewnienie poprawności parametrów kwantyzacji danych |
| out_h              | size_t              | być       | Wysokość danych wyjściowych                                                                     |
| out_w              | size_t              | być       | Wprowadź szerokość danych                                                                      |
| resize_mode        | image_resize_mode_t | być       | Wzorzec metody Zmiany rozmiaru                                                                     |
| align_corners      | Bool                | być       | Zmień rozmiar, czy align_corners                                              |
| half_pixel_centers | Bool                | być       | Zmień rozmiar, jeśli piksel jest wyrównany do środka                                                            |

**Zwracana wartość**

`result<runtime_tensor>`

**Przykłady kodu**

```cpp
auto &&[out_h, out_w] = get_rand_out_hw();
auto output_opt = F::resize(input, out_h, out_w, resize_mode, false, false).unwrap_or_throw();
```

### 6.2.16 podkładka

**Opis funkcji**

Dane wypełnienia w każdym wymiarze akceptują dane wyjściowe dt_bfloat16, dt_float32, dt_int8, dt_uint8 typu i dane wyjściowe tego samego typu.

**Definicja interfejsu**

`NNCASE_API inline result<runtime::runtime_tensor> pad(runtime::runtime_tensor &input, runtime_paddings_t &paddings, pad_mode_t pad_mode, float fill_v)`

**Parametry wejściowe**

| Nazwa parametru | typ               | Tak lub nie | opis                                                                                                                                       |
| -------- | ------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| wkład    | runtime_tensor     | być       | Wprowadź dane, jeśli dane są uint8 lub int8 Zapewnij poprawność parametrów kwantyzacji danych                                                                                  |
| Dopełnienie  | runtime_paddings_t | być       | Na przykład wartość wypełnienia jest `[ {2,3}, {1,3} ]`wskazywana przed padem 2 w ostatnim wymiarze, a następnie pad 3. Przedostatni wymiar jest poprzedzony padem 1, a następnie pad 2 |
| pad_mode | pad_mode_t         | być       | Obecnie obsługiwany jest tylko tryb const                                                                                                                   |
| fill_v   | spławik              | być       | Wypełnianie wartości                                                                                                                                     |

**Zwracana wartość**

`result<runtime_tensor>`

**Przykłady kodu**

```cpp
runtime_paddings_t paddings{ { 0, 0 }, { 0, 0 }, { 0, 0 }, { 1, 2 } };
auto output = F::pad(input, paddings, pad_constant, pad_value).unwrap_or_throw();
```
<!-- markdownlint-enable no-emphasis-as-header -->
# 7 Biała księga ilościowa

## 7.1 Biała księga dotycząca kwantyfikacji modelu klasyfikacji

| Model klasyfikacji     | Precyzja procesora (Top-1) | Dokładność zmiennoprzecinkowa (Top-1) | Precyzja uint8 (Top-1) | int8 Precision (Top-1) |
| ------------ | -------------- | --------------- | ---------------- | --------------- |
| alexnet      | 0.531          | 0.53            | N/A              | 0.52            |
| densenet 121 | 0.732          | 0.732           | 0.723            | N/A             |
| incepcja v3 | 0.766          | 0.765           | 0.773            | 0.77            |
| incepcja v4 | 0.789          | 0.789           | 0.793            | 0.792           |
| mobilenet v1 | 0.731          | 0.73            | 0.723            | 0.718           |
| mobilenet v2 | 0.713          | 0.715           | 0.713            | 0.719           |
| resnet50 v2  | 0.747          | 0.74            | 0.748            | 0.749           |
| vgg 16       | 0.689          | 0.687           | 0.690            | 0.689           |

> Ta tabela służy głównie do porównywania wydajności kwantyzacji, precyzja procesora jest pełnym zestawem walidacji ImageNet, a dokładność zmiennoprzecinkowa i kwantyzacji jest wynikiem testu podzbioru danych dla pierwszego obrazu 1000 klas w zestawie walidacji zgodnie z liczbą porządkową.
>
> Wyniki testów Alexnet i SenseNet są starymi danymi, z których oba są wynikami testów pierwszych 1000 obrazów zestawu weryfikacyjnego jako podzbioru danych, a N/A polega na tym, że podzbiór danych testowych w tym czasie różni się od procesora, więc nie jest używany jako porównanie.
>
> Ponieważ wybrana sieć niekoniecznie pochodzi od urzędnika lub istnieją różnice w wstępnym przetwarzaniu itp., Może różnić się od oficjalnej wydajności.

## 7.2 Biała księga dotycząca kwantyfikacji modelu wykrywania

1. JOŁOW3

    | COCOAPI                                                      | Oficjalne wyniki | Dokładność zmiennoprzecinkowa procesora | gnne zmiennoprzecinkowa precyzja | Precyzja uint8 | precyzja int8 |
    | ------------------------------------------------------------ | -------- | ----------- | ------------ | --------- | -------- |
    | Średnia precyzja (AP) @ [IoU = 0,50:0,95\| area = wszystkie \| maxDets = 100] | 0.314    | 0.307       | 0.306        | 0.295     | 0.288    |
    | Średnia precyzja (AP) @ [IoU = 0,50\| area = wszystkie \| maxDets = 100] | 0.559    | 0.555       | 0.554        | 0.555     | 0.554    |
    | Średnia precyzja (AP) @ [IoU = 0,75\| area = wszystkie \| maxDets = 100] | 0.318    | 0.308       | 0.307        | 0.287     | 0.275    |
    | Średnia precyzja (AP) @ [IoU = 0,50:0,95\| powierzchnia = mała \| maxDets = 100] | 0.142    | 0.150       | 0.149        | 0.147     | 0.144    |
    | Średnia precyzja (AP) @ [IoU = 0,50:0,95\| powierzchnia = medium \| maxDets = 100] | 0.341    | 0.332       | 0.332        | 0.322     | 0.316    |
    | Średnia precyzja (AP) @ [IoU = 0,50:0,95\| powierzchnia = duży \| maxDets = 100] | 0.464    | 0.437       | 0.437        | 0.414     | 0.404    |
    | Średnie przywołanie (AR) @ [IoU = 0,50:0,95\| area = wszystkie \| maxDets = 1] | 0.278    | 0.270       | 0.271        | 0.262     | 0.256    |
    | Średnie przywołanie (AR) @ [IoU = 0,50:0,95\| area = wszystkie \| maxDets = 10] | 0.419    | 0.412       | 0.412        | 0.399     | 0.392    |
    | Średnie przywołanie (AR) @ [IoU = 0,50:0,95\| area = wszystkie \| maxDets = 100] | 0.442    | 0.433       | 0.433        | 0.421     | 0.414    |
    | Średnie przywołanie (AR) @ [IoU = 0,50:0,95\| powierzchnia = mała \| maxDets = 100] | 0.239    | 0.251       | 0.251        | 0.248     | 0.246    |
    | Średnie przywołanie (AR) @ [IoU = 0,50:0,95\| powierzchnia = medium \| maxDets = 100] | 0.482    | 0.462       | 0.463        | 0.451     | 0.443    |
    | Średnie przywołanie (AR) @ [IoU = 0,50:0,95\| powierzchnia = duży \| maxDets = 100] | 0.611    | 0.586       | 0.585        | 0.559     | 0.550    |

2. ssd-mobilenetv1

    | COCOAPI                                                                    | Oficjalne wyniki | Dokładność zmiennoprzecinkowa procesora | gnne zmiennoprzecinkowa precyzja | Precyzja uint8 | precyzja int8 |
    | -------------------------------------------------------------------------- | -------- | ----------- | ------------ | --------- | -------- |
    | Średnia precyzja (AP) @ [IoU = 0,50:0,95\| area = wszystkie \| maxDets = 100]   | 0.184    | 0.184       | 0.184        | 0.183     | 0.183    |
    | Średnia precyzja (AP) @ [IoU = 0,50\| area = wszystkie \| maxDets = 100]        | 0.306    | 0.307       | 0.306        | 0.305     | 0.306    |
    | Średnia precyzja (AP) @ [IoU = 0,75\| area = wszystkie \| maxDets = 100]        | 0.191    | 0.192       | 0.190        | 0.189     | 0.190    |
    | Średnia precyzja (AP) @ [IoU = 0,50:0,95\| powierzchnia = mała \| maxDets = 100] | 0.017    | 0.017       | 0.017        | 0.017     | 0.017    |
    | Średnia precyzja (AP) @ [IoU = 0,50:0,95\| powierzchnia = medium \| maxDets = 100] | 0.157    | 0.157       | 0.157        | 0.156     | 0.155    |
    | Średnia precyzja (AP) @ [IoU = 0,50:0,95\| powierzchnia = duży \| maxDets = 100] | 0.371    | 0.372       | 0.371        | 0.370     | 0.369    |
    | Średnie wycofanie (AR) @ [IoU = 0,50:0,95\| area = wszystkie \| maxDets = 1]         | 0.180    | 0.180       | 0.180        | 0.181     | 0.181    |
    | Średnie wycofanie (AR) @ [IoU = 0,50:0,95\| area = wszystkie \| maxDets = 10]        | 0.242    | 0.242       | 0.242        | 0.243     | 0.243    |
    | Średnie wycofanie (AR) @ [IoU = 0,50:0,95\| area = wszystkie \| maxDets = 100]      | 0.242    | 0.242       | 0.242        | 0.243     | 0.243    |
    | Średnie wycofanie (AR) @ [IoU = 0,50:0,95\| powierzchnia = mała \| maxDets = 100]    | 0.026    | 0.026       | 0.026        | 0.026     | 0.026    |
    | Średnie wycofanie (AR) @ [IoU = 0,50:0,95\| powierzchnia = medium \| maxDets = 100]    | 0.206    | 0.206       | 0.206        | 0.206     | 0.205    |
    | Średnie wycofanie (AR) @ [IoU = 0,50:0,95\| powierzchnia = duży \| maxDets = 100]    | 0.489    | 0.491       | 0.490        | 0.490     | 0.491    |

3. YOLOV5S

    | COCOAPI                                                                    | Oficjalne wyniki | Dokładność zmiennoprzecinkowa procesora | gnne zmiennoprzecinkowa precyzja | Precyzja uint8 | precyzja int8 |
    | -------------------------------------------------------------------------- | -------- | ----------- | ------------ | --------- | -------- |
    | Średnia precyzja (AP) @ [IoU = 0,50:0,95\| area = wszystkie \| maxDets = 100]   | 0.367    | 0.365       | 0.335        | 0.334     | 0.335    |
    | Średnia precyzja (AP) @ [IoU = 0,50\| area = wszystkie \| maxDets = 100]        | 0.555    | 0.552       | 0.518        | 0.518     | 0.518    |
    | Średnia precyzja (AP) @ [IoU = 0,75\| area = wszystkie \| maxDets = 100]        | 0.398    | 0.395       | 0.364        | 0.363     | 0.362    |
    | Średnia precyzja (AP) @ [IoU = 0,50:0,95\| powierzchnia = mała \| maxDets = 100] | 0.223    | 0.220       | 0.199        | 0.199     | 0.197    |
    | Średnia precyzja (AP) @ [IoU = 0,50:0,95\| powierzchnia = medium \| maxDets = 100] | 0.419    | 0.418       | 0.387        | 0.386     | 0.386    |
    | Średnia precyzja (AP) @ [IoU = 0,50:0,95\| powierzchnia = duży \| maxDets = 100] | 0.463    | 0.459       | 0.423        | 0.422     | 0.423    |
    | Średnie wycofanie (AR) @ [IoU = 0,50:0,95\| area = wszystkie \| maxDets = 1]         | 0.306    | 0.306       | 0.288        | 0.287     | 0.287    |
    | Średnie wycofanie (AR) @ [IoU = 0,50:0,95\| area = wszystkie \| maxDets = 10]        | 0.518    | 0.518       | 0.487        | 0.486     | 0.487    |
    | Średnie wycofanie (AR) @ [IoU = 0,50:0,95\| area = wszystkie \| maxDets = 100]      | 0.576    | 0.576       | 0.540        | 0.539     | 0.540    |
    | Średnie wycofanie (AR) @ [IoU = 0,50:0,95\| powierzchnia = mała \| maxDets = 100]    | 0.391    | 0.399       | 0.350        | 0.350     | 0.347    |
    | Średnie wycofanie (AR) @ [IoU = 0,50:0,95\| powierzchnia = medium \| maxDets = 100]    | 0.641    | 0.640       | 0.606        | 0.605     | 0.607    |
    | Średnie wycofanie (AR) @ [IoU = 0,50:0,95\| powierzchnia = duży \| maxDets = 100]    | 0.716    | 0.710       | 0.680        | 0.683     | 0.685    |

# 8 FAQ - najczęściej zadawane pytania

1.安装wheel时报错: "xxx.whl nie jest obsługiwanym kołem na tej platformie." **

P: 安装nncase wheel包, 出现ERROR: nncase-1.0.0.20210830-cp37-cp37m-manylinux_2_24_x86_64.whl nie jest obsługiwanym kołem na tej platformie.

Odp .: > pipsa aktualizacji = 20,3

```shell
sudo pip3 install --upgrade pip
```

2. **Gdy CRB uruchamia program do wnioskowania aplikacji, zgłasza błąd "std::bad_alloc"**

P: Uruchom program wnioskowania aplikacji na CRB i zgłoś wyjątek "std::bad_alloc"

```shell
$ ./cpp.sh
case ./yolov3_bfloat16 build at Sep 16 2021 18:12:03
terminate called after throwing an instance of 'std::bad_alloc'
  what():  std::bad_alloc
```

Odp .: std::bad_alloc wyjątki są zwykle spowodowane błędami alokacji pamięci, które można sprawdzić w następujący sposób.

- Sprawdź, czy wygenerowany kmodel nie przekracza aktualnej dostępnej pamięci systemu (np. yolov3 bfloat16 kmodel rozmiar to 121MB, obecna dostępna pamięć Linuksa to tylko 70MB, wyjątek zostanie zgłoszony).  Jeśli przekroczy, spróbuj użyć kwantyzacji potreningowej, aby zmniejszyć rozmiar kmodel.
- Sprawdź aplikację pod kątem wycieków pamięci

3. **Podczas uruchamiania programu do wnioskowania aplikacji[.. t_runtime_tensor.cpp:310 (utwórz)] data.size_bytes() == size = false (bool).**

P: Symulator uruchamia program do wnioskowania aplikacji, rzucając[.. t_runtime_tensor.cpp:310 (utwórz)] wyjątek "data.size_bytes() == size = false (bool)"

Odp .: Sprawdź informacje o tensorze wejściowym dla ustawień, koncentrując się na kształcie wejściowym i liczbie bajtów zajętych przez każdy element (fp32/uint8)

**Zrzeczenie się odpowiedzialności za **tłumaczenie  
Dla wygody klientów Canaan używa tłumacza AI do tłumaczenia tekstu na wiele języków, które mogą zawierać błędy. Nie gwarantujemy dokładności, rzetelności ani terminowości dostarczonych tłumaczeń. Canaan nie ponosi odpowiedzialności za jakiekolwiek straty lub szkody spowodowane poleganiem na dokładności lub wiarygodności przetłumaczonych informacji. W przypadku różnic w treści tłumaczeń w różnych językach, pierwszeństwo ma chińska wersja uproszczona. 

Jeśli chcesz zgłosić błąd lub niedokładność tłumaczenia, skontaktuj się z nami pocztą.