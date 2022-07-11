![canaan-cover.png](http://s2.loli.net/2022/03/30/7UG1IxrOXTo2QKw.png)

**<font face="黑体" size="6" style="float:right">K510 nncase Guía del desarrollador</font>**

<font face="黑体"  size=3>Versión del documento: V1.0.1</font>

<font face="黑体"  size=3>Publicado: 2022-05-10</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Renuncia**</font>
Los productos, servicios o características que compre estarán sujetos a los contratos comerciales y términos de Beijing Canaan Jiesi Information Technology Co., Ltd. ("la Compañía", la misma en adelante), y todos o parte de los productos, servicios o características descritos en este documento pueden no estar dentro del alcance de su compra o uso. Salvo que se acuerde lo contrario en el contrato, la Compañía renuncia a todas las representaciones o garantías, expresas o implícitas, en cuanto a la precisión, confiabilidad, integridad, marketing, propósito específico y no agresión de cualquier representación, información o contenido de este documento. A menos que se acuerde lo contrario, este documento se proporciona como una guía para su uso solamente.
Debido a actualizaciones de la versión del producto u otras razones, el contenido de este documento puede actualizarse o modificarse de vez en cuando sin previo aviso.

**<font face="黑体"  size=3>Avisos de marcas comerciales</font>**

""<img src="http://s2.loli.net/2022/03/30/xN21jbhnwSFyGRD.png" style="zoom:33%;" />, el icono de "Canaan", Canaan y otras marcas comerciales de Canaan y otras marcas comerciales de Canaan son marcas comerciales de Beijing Canaan Jiesi Information Technology Co., Ltd. Todas las demás marcas comerciales o marcas registradas que puedan mencionarse en este documento son propiedad de sus respectivos propietarios.

**<font face="黑体"  size=3>Derechos de autor ©2022 Beijing Canaan Jiesi Information Technology Co., Ltd</font>**
Este documento solo es aplicable al desarrollo y diseño de la plataforma K510, sin el permiso por escrito de la empresa, ninguna unidad o individuo puede difundir parte o la totalidad del contenido de este documento en ninguna forma.

**<font face="黑体"  size=3>Beijing Canaan Jiesi Información Technology Co., Ltd</font>**
URL: canaan-creative.com
Consultas comerciales: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# prefacio
**<font face="黑体"  size=5>Propósito del documento</font>**
Este documento es un documento de descripción para el uso del compilador nncase/K510, que proporciona a los usuarios cómo instalar nncase, cómo llamar a las API del compilador para compilar modelos de redes neuronales y API en tiempo de ejecución para escribir programas de inferencia de IA

**<font face="黑体"  size=5>Objetos reader</font>**

Las principales personas a las que se aplica este documento (esta guía):

- Desarrolladores de software
- Personal de soporte técnico

**<font face="黑体"  size=5>Términos y siglas</font>**

| término | Explicación/nombre completo                              |
| ---- | -------------------------------------- |
| PTQ  | Cuantización posterior a la capacitación, cuantización posterior a la capacitación |
| MSE  | error cuadrático medio, error cuadrático medio            |
|      |                                        |

**<font face="黑体"  size=5>Historial
 </font>**de revisiones <font face="宋体"  size=2>El historial de revisiones acumula una descripción de cada actualización del documento. La versión más reciente del documento contiene actualizaciones para todas las versiones anteriores. </font>

| El número de versión   | Modificado por     | Fecha de revisión | Notas de revisión |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.1 | Publicidad | 2022-05-10 | nncase_v1.6.1 Español |
| V1.0.0 | Zhang Yang/Zhang Jizhao/Yang Haoqi | 2022-05-06 | nncase_v1.6.0 |
| V0.9.0 | Publicidad | 2022-04-01 | nncase_v1.5.0 |
| V0.8.0 | Zhang Yang/Zhang Jizhao | 2022-03-03 | nncase_v1.4.0 |
| V0.7.0 | Publicidad | 2022-01-28 | nncase_v1.3.0 |
| V0.6.0 | Publicidad | 2021-12-31 | nncase_v1.2.0 |
| V0.5.0 | Publicidad | 2021-12-03 | nncase_v1.1.0 |
| V0.4.0 | Zhang Yang/Haoqi Yang/Zheng Qihang | 2021-10-29 | nncase_v1.0.0 |
| V0.3.0 | Zhang Yang / Yang Haoqi | 2021-09-28 | nncase_v1.0.0_rc1 |
| V0.2.0 | Zhang Yang / Yang Haoqi | 2021-09-02 | nncase_v1.0.0_beta2 |
| V0.1.0 | Zhang Yang / Yang Haoqi | 2021-08-31 | nncase_v1.0.0_beta1 |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenido</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Introducción al entorno de desarrollo

## 1.1 Sistema operativo

- Ubuntu 18.04/20.04

## 1.2 Entorno de software

Los requisitos del entorno de software se muestran en la tabla siguiente:

| número de serie | Recursos de software        | ilustrar                        |
| ---- | --------------- | --------------------------- |
| 1    | Pitón          | Python 3.6/3.7/3.8/3.9/3.10 |
| 2    | pip3            | pip3 versión > = 20.3            |
| 3    | onnx            | La versión onnx es 1.9.0             |
| 4    | onnx-simplificar | La versión del simplificador de onxáx es 0.3.6  |
| 5    | onnxoptimizador   | La versión de onnxoptimizer es 0.2.6    |

## 1.3 Entorno de hardware

Los requisitos del entorno de hardware se muestran en la tabla siguiente:

| número de serie | Recursos de hardware     | ilustrar |
| ---- | ------------ | ---- |
| 1    | K510 CRB     |      |
| 2    | Tarjeta SD y lector de tarjetas |      |

# 2 Introducción a nncase

## 2.1 Qué es nncase

nncase es un compilador de redes neuronales diseñado para aceleradores de IA, y actualmente soporta objetivos como CPU/K210/K510

Características proporcionadas por nncase

- Admite múltiples redes de entrada y salida múltiples, admite estructuras de múltiples sucursales
- Asignación de memoria estática, no se requiere memoria de montón
- Fusión y optimización de operadores
- Soporta inferencia de cuantización float y uint8/int8
- Admite la cuantización posterior al entrenamiento, utilizando modelos de coma flotante y conjuntos de calibración de cuantización
- Modelo plano con soporte de carga de copia cero

Marco de red neuronal soportado por nncase

- tflite
- onnx
- café

## 2.2 Ventajas del producto

- **Implementación sencilla de extremo a extremo**

  Reducir el número de interacciones con los usuarios. La implementación en KPU se puede lograr mediante el uso y la implementación de las mismas herramientas y procesos para los modelos de CPU y GPU. No es necesario establecer parámetros complejos, reducir el umbral de uso y acelerar el ciclo de iteración de los algoritmos de IA.
- **Aprovechar al máximo el ecosistema de IA existente**

  Apegado a un marco ampliamente utilizado en la industria. Por un lado, puede mejorar su visibilidad y disfrutar de los dividendos de una ecología madura. Por otro lado, los costos de desarrollo de los desarrolladores pequeños y medianos se pueden reducir, y los modelos y algoritmos maduros en la industria se pueden implementar directamente.
- **Aproveche al máximo su hardware**

  La ventaja de NPU es que el rendimiento es mayor que el de la CPU y la GPU, y el compilador DL debe ser capaz de utilizar completamente el rendimiento del hardware. El compilador también necesita optimizar adaptativamente el rendimiento para la nueva estructura del modelo, por lo que se debe explorar una nueva técnica de optimización automática además de la optimización manual.
- **Escalabilidad y mantenibilidad**

  Capacidad para admitir implementaciones de modelos de IA para K210, K510 y futuros chips. Es necesario proporcionar cierta escalabilidad a nivel arquitectónico. Agregar un nuevo Target es menos costoso y le permite reutilizar tantos módulos como sea posible. Acelerar el desarrollo de nuevos productos para lograr la acumulación tecnológica de DL Compiler.

## 2.3 Arquitectura nncase

<img src="https://i.loli.net/2021/08/18/IQR12SOJdzxTUZH.png" alt="nncase_arch.png" style="zoom:67%;" />

La pila de software nnncase consta actualmente de dos partes: compilador y tiempo de ejecución.

**Compilador:** Se utiliza para compilar modelos de redes neuronales en una PC y, finalmente, generar un archivo kmodel. Incluye principalmente importador, IR, evaluador, quantize, optimización de transformaciones, mosaicos, particiones, programación, codegen y otros módulos.

- Importador: Importa modelos de otros marcos de redes neuronales en nncase
- IR: Representación intermedia, dividida en IR neutro importado por el importador (independiente del dispositivo) e IR nutral generado al reducir el IR objetivo de conversión (dependiente del dispositivo)
- Evaluador: El evaluador proporciona una ejecución interpretativa de IR y se usa a menudo en escenarios como la calibración de plegamiento constante / PTQ
- Transformación: Para la transformación IR y la optimización transversal de gráficos, etc.
- Quantize: Cuantifique después del entrenamiento, agregue marcadores de cuantización al tensor a cuantificar, llame al evaluador para la ejecución de interpretación de acuerdo con el conjunto de corrección de entrada, recopile el rango de datos del tensor, inserte nodos de cuantización / descuantización y, finalmente, optimice para eliminar nodos innecesarios de cuantización / descuantización, etc.
- Mosaico: Limitado por la menor capacidad de memoria de la NPU, es necesario dividir grandes trozos de computación. Además, la selección del parámetro Tilling cuando hay una gran cantidad de multiplexación de datos en el cálculo tendrá un impacto en la latencia y el ancho de banda.
- Partición: Divida el gráfico por ModuleType, cada subgrafo después de la división corresponderá a RuntimeModule, diferentes tipos de RuntimeModule corresponden a diferentes dispositivos (cpu / K510)
- Programación: Genera un orden de cálculo y asigna búferes en función de las dependencias de datos en el gráfico optimizado
- Codegen: Llame al codegen correspondiente a ModuleType para cada subgrafo para generar RuntimeModule

**Tiempo de ejecución**: Integrado en la aplicación del usuario, proporciona funciones como cargar kmodel / configurar datos de entrada, ejecución de KPU y obtener datos de salida

# 3 Instalar nncase

La parte del compilador de la cadena de herramientas de nncase incluye nncase y el compilador K510, los cuales necesitan instalar el paquete de rueda correspondiente.

- El paquete de rueda nncase fue[lanzado en nncase github](https://github.com/kendryte/nncase/releases/tag/v1.6.0), soportando Python 3.6/3.7/3.8/3.9/3.10, los usuarios pueden elegir la versión correspondiente para descargar según el sistema operativo y Python
- El paquete de rueda del compilador K510 se encuentra en el directorio x86_64 del SDK de nncase, no depende de la versión de Python y se puede instalar directamente

Si no tiene un entorno Ubuntu, puede usar[nncase docker](https://github.com/kendryte/nncase/blob/master/docs/build.md#docker)(Ubuntu 20.04 + Python 3.8).

```shell
cd /path/to/nncase_sdk
docker pull registry.cn-hangzhou.aliyuncs.com/kendryte/nncase:latest
docker run -it --rm -v `pwd`:/mnt -w /mnt registry.cn-hangzhou.aliyuncs.com/kendryte/nncase:latest /bin/bash -c "/bin/bash"
```

Lo siguiente toma Ubuntu 20.04 + Python 3.8 instalación de nncase como ejemplo

```shell
wget -P x86_64 https://github.com/kendryte/nncase/releases/download/v1.6.0/nncase-1.6.0.20220505-cp38-cp38-manylinux_2_24_x86_64.whl
pip3 install x86_64/*.whl
```
<!-- markdownlint-disable no-emphasis-as-header -->
# 4 Modelo de compilación/inferencia

nncase proporciona**la API de Python**para compilar/inferir modelos de aprendizaje profundo en un PC

## 4.1 Operadores compatibles

### Operador de 4.1.1 tflite

| Operador                | Es compatible |
| ----------------------- | ------------ |
| ABS                     | ✅            |
| AGREGAR                     | ✅            |
| ARG_MAX                 | ✅            |
| ARG_MIN                 | ✅            |
| AVERAGE_POOL_2D         | ✅            |
| BATCH_MATMUL            | ✅            |
| LANZAR                    | ✅            |
| CEIL                    | ✅            |
| CONCATENACIÓN           | ✅            |
| CONV_2D                 | ✅            |
| COS                     | ✅            |
| COSTUMBRE                  | ✅            |
| DEPTHWISE_CONV_2D       | ✅            |
| DIV                     | ✅            |
| IGUAL                   | ✅            |
| EXP                     | ✅            |
| EXPAND_DIMS             | ✅            |
| PISO                   | ✅            |
| FLOOR_DIV               | ✅            |
| FLOOR_MOD               | ✅            |
| FULLY_CONNECTED         | ✅            |
| MAYOR                 | ✅            |
| GREATER_EQUAL           | ✅            |
| L2_NORMALIZATION        | ✅            |
| LEAKY_RELU              | ✅            |
| MENOS                    | ✅            |
| LESS_EQUAL              | ✅            |
| REGISTRO                     | ✅            |
| LOGÍSTICO                | ✅            |
| MAX_POOL_2D             | ✅            |
| MÁXIMO                 | ✅            |
| SIGNIFICAR                    | ✅            |
| MÍNIMO                 | ✅            |
| Yo                     | ✅            |
| NEG                     | ✅            |
| NOT_EQUAL               | ✅            |
| ALMOHADILLA                     | ✅            |
| PADV2                   | ✅            |
| MIRROR_PAD              | ✅            |
| EMPAQUETAR                    | ✅            |
| PRISIONERO DE GUERRA                     | ✅            |
| REDUCE_MAX              | ✅            |
| REDUCE_MIN              | ✅            |
| REDUCE_PROD             | ✅            |
| RELU                    | ✅            |
| PRELU                   | ✅            |
| RELU6                   | ✅            |
| REFORMAR                 | ✅            |
| RESIZE_BILINEAR         | ✅            |
| RESIZE_NEAREST_NEIGHBOR | ✅            |
| REDONDO                   | ✅            |
| RSQRT                   | ✅            |
| FORMA                   | ✅            |
| SIN                     | ✅            |
| LONCHA                   | ✅            |
| SOFTMAX                 | ✅            |
| SPACE_TO_BATCH_ND       | ✅            |
| EXPRIMIR                 | ✅            |
| BATCH_TO_SPACE_ND       | ✅            |
| STRIDED_SLICE           | ✅            |
| SQRT                    | ✅            |
| CUADRADO                  | ✅            |
| SUB                     | ✅            |
| SUMA                     | ✅            |
| SOSPECHOSO                    | ✅            |
| TEJA                    | ✅            |
| TRANSPONER               | ✅            |
| TRANSPOSE_CONV          | ✅            |
| CUANTIFICAR                | ✅            |
| FAKE_QUANT              | ✅            |
| DESCUANTIZAR              | ✅            |
| REUNIR                  | ✅            |
| GATHER_ND               | ✅            |
| ONE_HOT                 | ✅            |
| SQUARED_DIFFERENCE      | ✅            |
| LOG_SOFTMAX             | ✅            |
| PARTIR                   | ✅            |
| HARD_SWISH              | ✅            |

### Operador de 4.1.2 onnx

| Operador              | Es compatible |
| --------------------- | ------------ |
| Abs                   | ✅            |
| Acos                  | ✅            |
| Acosh                 | ✅            |
| Y                   | ✅            |
| ArgMax                | ✅            |
| ArgMin                | ✅            |
| Salado                  | ✅            |
| Asinh                 | ✅            |
| Agregar                   | ✅            |
| AveragePool           | ✅            |
| BatchNormalización    | ✅            |
| Lanzar                  | ✅            |
| Ceil                  | ✅            |
| Para                  | ✅            |
| Pinza                  | ✅            |
| Concat                | ✅            |
| Constante              | ✅            |
| ConstantOfShape       | ✅            |
| Conv                  | ✅            |
| ConvTranspose         | ✅            |
| Cuerpo                   | ✅            |
| Cosh                  | ✅            |
| Cumsum                | ✅            |
| DepthToSpace          | ✅            |
| DequantizeLinear      | ✅            |
| Div                   | ✅            |
| Abandono escolar               | ✅            |
| Vida                   | ✅            |
| Exp                   | ✅            |
| Expandir                | ✅            |
| Igual                 | ✅            |
| Aplanar               | ✅            |
| Piso                 | ✅            |
| Reunir                | ✅            |
| ReunirSEND              | ✅            |
| Gemm                  | ✅            |
| GlobalAveragePool     | ✅            |
| GlobalMaxPool         | ✅            |
| Mayor               | ✅            |
| GreaterOrEqual        | ✅            |
| Hardmax               | ✅            |
| HardSigmoid           | ✅            |
| HardSwish             | ✅            |
| Identidad              | ✅            |
| InstanceNormalización | ✅            |
| LpNormalización       | ✅            |
| LeakyRelu             | ✅            |
| Menos                  | ✅            |
| LessOrEqual           | ✅            |
| Registro                   | ✅            |
| LogSoftmax            | ✅            |
| LRN                   | ✅            |
| LSTM                  | ✅            |
| MatMul                | ✅            |
| MaxPool               | ✅            |
| Máximo                   | ✅            |
| Min                   | ✅            |
| Yo                   | ✅            |
| Neg                   | ✅            |
| No                   | ✅            |
| OneHot                | ✅            |
| Almohadilla                   | ✅            |
| Prisionero de guerra                   | ✅            |
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
| ReducirMean            | ✅            |
| ReduceMin             | ✅            |
| ReduceProd            | ✅            |
| ReduceSum             | ✅            |
| ReduceSumSquare       | ✅            |
| Relu                  | ✅            |
| Reformar               | ✅            |
| Redimensionar                | ✅            |
| ReverseSequence       | ✅            |
| RoiAlign              | ✅            |
| Redondo                 | ✅            |
| Pueblo                  | ✅            |
| Forma                 | ✅            |
| Firmar                  | ✅            |
| Sin                   | ✅            |
| Nacimiento                  | ✅            |
| Sigmoide               | ✅            |
| Tamaño                  | ✅            |
| Loncha                 | ✅            |
| Softmax               | ✅            |
| Softplus              | ✅            |
| Softsign              | ✅            |
| SpaceToDepth          | ✅            |
| Partir                 | ✅            |
| Sqrt                  | ✅            |
| Exprimir               | ✅            |
| Sub                   | ✅            |
| Suma                   | ✅            |
| Sospechoso                  | ✅            |
| Teja                  | ✅            |
| TopK                  | ✅            |
| Transponer             | ✅            |
| Trilu                 | ✅            |
| Muestra ascendente              | ✅            |
| Despresprimir             | ✅            |
| Dónde                 | ✅            |

### 4.1.3 Operador de café

| Operador              | Es compatible |
| --------------------- | ------------ |
| Entrada                 | ✅            |
| Concat                | ✅            |
| Circunvolución           | ✅            |
| Eltwise               | ✅            |
| Intercambios               | ✅            |
| relu                  | ✅            |
| Reformar               | ✅            |
| Loncha                 | ✅            |
| Softmax               | ✅            |
| Partir                 | ✅            |
| ContinuationIndicator | ✅            |
| Agrupación               | ✅            |
| BatchNorm             | ✅            |
| Escama                 | ✅            |
| Marcha atrás               | ✅            |
| LSTM                  | ✅            |
| Producto Interno          | ✅            |

## 4.2 Compilar API de modelos

En la actualidad, la API del modelo de compilación admite marcos de aprendizaje profundo como tflite / onnx / caffe.

### 4.2.1 CompileOptions

**Descripción de la característica**

Clase CompileOptions para configurar las opciones de compilación de nncase

**Definición de clase**

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

Cada propiedad se describe a continuación

| Nombre de la propiedad         | tipo   | Sí o no | descripción                                                         |
| ---------------- | ------ | -------- | ------------------------------------------------------------ |
| blanco           | cuerda | ser       | Especifique el destino de compilación, como 'k210', 'k510'                               |
| quant_type       | cuerda | no       | Especifique el tipo de cuantización de datos, como 'uint8', 'int8'                          |
| w_quant_type     | cuerda | no       | Especifique el tipo de cuantización de peso, como 'uint8', 'int8', predeterminado en 'uint8'           |
| use_mse_quant_w  | Bool   | no       | Especifica si se debe utilizar el algoritmo de error cuadrático medio (MSE) para optimizar los parámetros de cuantización al cuantificar pesos |
| split_w_to_act   | Bool   | no       | Especifica si se deben equilibrar los datos de peso parcial en datos activos                       |
| Preprocesar       | Bool   | no       | Independientemente de si el preprocesamiento está habilitado o no, el valor predeterminado es False                                  |
| swapRB           | Bool   | no       | Ya sea para intercambiar datos de entrada RGB entre los canales rojo y azul (RGB--> BGR o BGR->RGB), el valor predeterminado es False |
| significar             | lista   | no       | El preprocesamiento normaliza la media del parámetro, que de forma predeterminada es[0, 0, 0]                        |
| ETS              | lista   | no       | El preprocesamiento normaliza la varianza de parámetros, que de forma predeterminada es[1, 1, 1]                        |
| input_range      | lista   | no       | El rango de números de coma flotante después de la descuantización de los datos de entrada, que por defecto es[0, 1]               |
| output_range     | lista   | no       | El rango de números de coma flotante antes de que se generen los datos de punto fijo, que de forma predeterminada es en blanco                     |
| input_shape      | lista   | no       | Especifique la forma de los datos de entrada, el diseño del input_shape debe ser coherente con el diseño de entrada, y la input_shape de los datos de entrada es inconsistente con la forma de entrada del modelo, y se realizará la operación de caja de bits (cambio de tamaño / pad, etc.). |
| letterbox_value  | flotar  | no       | Especifica el valor de relleno del fetchbox de preprocesamiento                                  |
| input_type       | cuerda | no       | Especifica el tipo de datos de entrada, por defecto en 'float32'                          |
| output_type      | cuerda | no       | Especifica el tipo de datos de salida, como 'float32', 'uint8' (solo para la cuantificación especificada), de forma predeterminada 'float32' |
| input_layout     | cuerda | no       | Especifique el diseño de los datos de entrada, como 'NCHW', 'NHWC'. Si el diseño de los datos de entrada es diferente del modelo en sí, los insertos de nncase se transponen para la conversión |
| output_layout    | cuerda | no       | Especifique los datos de salida para el diseño, como 'NCHW', 'NHWC'. Si el diseño de los datos de salida es diferente del modelo en sí, nncase insertará transposición para la conversión |
| model_layout     | cuerda | no       | Especifique el diseño del modelo, que por defecto es en blanco, y especifique cuándo el diseño del modelo tflite es 'NCHW' y los modelos Onnx y Caffe son 'NHWC' |
| is_fpga          | Bool   | no       | Especifica si kmodel se usa para FPGA, que de forma predeterminada es False                          |
| dump_ir          | Bool   | no       | Especifica si el valor predeterminado es False de VOLcado IR                                 |
| dump_asm         | Bool   | no       | Especifica si el archivo de ensamblado asm de volcado, que de forma predeterminada es False                        |
| dump_quant_error | Bool   | no       | Especifica si el volcado cuantifica el error del modelo antes y después                               |
| dump_dir         | cuerda | no       | Después de especificar la dump_ir y otros modificadores anteriormente, aquí se especifica el directorio de volcado, que de forma predeterminada es una cadena vacía  |
| benchmark_only   | Bool   | no       | Especifica si kmodel se usa solo para el punto de referencia, que de forma predeterminada es False                   |

> 1. El rango de entrada es el rango de números de coma flotante, es decir, si el tipo de datos de entrada es uint8, entonces el rango de entrada es el rango después de la descuantización a punto flotante (no puede ser 0 ~ 1), que se puede especificar libremente.
> 2. input_shape deben especificarse de acuerdo con el input_layout, [1，224，224，3]por ejemplo, si el input_layout es NCHW, el input_shape debe especificarse como[1,3,224,224]; input_layout es NHWC, el input_shape debe especificarse como[1,224,224,3];
> 3. media y std son parámetros para normalizar los números de coma flotante, que el usuario es libre de especificar;
> 4. Cuando se utiliza la función de buzón, debe limitar el tamaño de entrada a 1,5 MB, y el tamaño de un solo canal está dentro de 0,75 MB;
>
> Por ejemplo:
>
> 1. El tipo de datos de entrada se establece en uint8, input_range establece en[0,255], el papel de la descuantización es solo convertir el tipo, convertir los datos de uint8 a float32, y los parámetros mean y std aún se pueden especificar de acuerdo con los datos de 0 ~ 255
> 2. El tipo de datos de entrada se establece en uint8, input_range establece en[0,1], el número de punto fijo se descuantiza a un [0,1]número de coma flotante en el rango, y la media y la std deben especificarse de acuerdo con el nuevo rango de números de coma flotante.

El proceso de preprocesamiento es el siguiente (los nodos verdes de la figura son opcionales):

![preproceso.png](https://i.loli.net/2021/11/08/fhBLsozUTCbt4dp.png)

**Ejemplo de código**

Crear una instancia de CompileOptions, configurar los valores de cada propiedad

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

**Descripción de la característica**

Clase ImportOptions para configurar las opciones de importación de nncase

**Definición de clase**

```python
py::class_<import_options>(m, "ImportOptions")
    .def(py::init())
    .def_readwrite("output_arrays", &import_options::output_arrays);
```

Cada propiedad se describe a continuación

| Nombre de la propiedad      | tipo   | Sí o no | descripción     |
| ------------- | ------ | -------- | -------- |
| output_arrays | cuerda | no       | Nombre de salida |

**Ejemplo de código**

Crear una instancia de ImageOptions, configurar los valores de cada propiedad

```python
# import_options
import_options = nncase.ImportOptions()
import_options.output_arrays = 'output' # Your output node name
```

### 4.2.3 PTQTensorOpciones

**Descripción de la característica**

Clase PTQTensorOptions para configurar las opciones de PTQ de nncase

**Definición de clase**

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

Cada propiedad se describe a continuación

| El nombre del campo         | tipo   | Sí o no | descripción                                                                                  |
| ---------------- | ------ | -------- | ------------------------------------------------------------------------------------- |
| calibrate_method | cuerda | no       | Método de calibración, admite 'no_clip', 'l2', 'kld_m0', 'kld_m1', 'kld_m2', 'cdf', el valor predeterminado es 'no_clip' |
| samples_count    | Int    | no       | El número de muestras                                                                              |

#### set_tensor_data()

**Descripción de la característica**

Establecer los datos de corrección

**Definición de la interfaz**

```python
set_tensor_data(calib_data)
```

**Parámetros de entrada**

| Nombre del parámetro   | tipo   | Sí o no | descripción     |
| ---------- | ------ | -------- | -------- |
| calib_data | byte[] | ser       | Corregir los datos |

**El valor devuelto**

N/A

**Ejemplo de código**

```python
# ptq_options
ptq_options = nncase.PTQTensorOptions()
ptq_options.samples_count = cfg.generate_calibs.batch_size
ptq_options.set_tensor_data(np.asarray([sample['data'] for sample in self.calibs]).tobytes())
```

### 4.2.4 Compilador

**Descripción de la característica**

Clase de compilador para compilar modelos de redes neuronales

**Definición de clase**

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

**Ejemplo de código**

```python
compiler = nncase.Compiler(compile_options)
```

#### import_tflite()

**Descripción de la característica**

Importar el modelo tflite

**Definición de la interfaz**

```python
import_tflite(model_content, import_options)
```

**Parámetros de entrada**

| Nombre del parámetro       | tipo          | Sí o no | descripción           |
| -------------- | ------------- | -------- | -------------- |
| model_content  | byte[]        | ser       | Lea el contenido del modelo |
| import_options | ImportOptions | ser       | Opciones de importación       |

**El valor devuelto**

N/A

**Ejemplo de código**

```python
model_content = read_model_file(model)
compiler.import_tflite(model_content, import_options)
```

#### import_onnx()

**Descripción de la característica**

Importar el modelo onnx

**Definición de la interfaz**

```python
import_onnx(model_content, import_options)
```

**Parámetros de entrada**

| Nombre del parámetro       | tipo          | Sí o no | descripción           |
| -------------- | ------------- | -------- | -------------- |
| model_content  | byte[]        | ser       | Lea el contenido del modelo |
| import_options | ImportOptions | ser       | Opciones de importación       |

**El valor devuelto**

N/A

**Ejemplo de código**

```python
model_content = read_model_file(model)
compiler.import_onnx(model_content, import_options)
```

#### import_caffe()

**Descripción de la característica**

Importar el modelo de café

> Los usuarios deben compilar/instalar caffe en la máquina local.

**Definición de la interfaz**

```python
import_caffe(caffemodel, prototxt)
```

**Parámetros de entrada**

| Nombre del parámetro   | tipo   | Sí o no | descripción                 |
| ---------- | ------ | -------- | -------------------- |
| caffemodel | byte[] | ser       | Lea el contenido del modelo de café |
| prototxt   | byte[] | ser       | Lea el contenido de prototxt   |

**El valor devuelto**

N/A

**Ejemplo de código**

```python
# import
caffemodel = read_model_file('test.caffemodel')
prototxt = read_model_file('test.prototxt')
compiler.import_caffe(caffemodel, prototxt)
```

#### use_ptq()

**Descripción de la característica**

Establecer opciones de configuración de PTQ

**Definición de la interfaz**

```python
use_ptq(ptq_options)
```

**Parámetros de entrada**

| Nombre del parámetro    | tipo             | Sí o no | descripción        |
| ----------- | ---------------- | -------- | ----------- |
| ptq_options | PTQTensorOpciones | ser       | Opciones de configuración de PTQ |

**El valor devuelto**

N/A

**Ejemplo de código**

```python
compiler.use_ptq(ptq_options)
```

#### compilar()

**Descripción de la característica**

Compilar el modelo de red neuronal

**Definición de la interfaz**

```python
compile()
```

**Parámetros de entrada**

N/A

**El valor devuelto**

N/A

**Ejemplo de código**

```python
compiler.compile()
```

#### gencode_tobytes()

**Descripción de la característica**

Genera un flujo de bytes de código

**Definición de la interfaz**

```python
gencode_tobytes()
```

**Parámetros de entrada**

N/A

**El valor devuelto**

Bytes[]

**Ejemplo de código**

```python
kmodel = compiler.gencode_tobytes()
with open(os.path.join(infer_dir, 'test.kmodel'), 'wb') as f:
    f.write(kmodel)
```

## 4.3 Compilar el ejemplo del modelo

En el ejemplo siguiente se utiliza el modelo y el script de compilación de Python

- El modelo se encuentra en el subdirectorio /path/to/nncase_sdk/examples/models/
- El script de compilación de Python se encuentra en el subdirectorio /path/to/nncase_sdk/examples/scripts

### 4.3.1 Compilar el modelo float32 tflite

- Mobilenetv2_tflite_fp32_image.py script es el siguiente

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

- Ejecute el siguiente comando para compilar el modelo tflite de mobiletv2, destino k510

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_tflite_fp32_image.py --target k510 --model models/mobilenet_v2_1.0_224.tflite
```

### 4.3.2 Compilar el modelo de onnx float32

- Para los modelos onnx, se recomienda simplificar el uso de[ONNX Simplifier](https://github.com/daquexian/onnx-simplifier)antes de compilar con nncase
- mobilenetv2_onnx_fp32_image.py script es el siguiente

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

- Ejecute el siguiente comando para compilar el modelo onnx de mobiletv2, destino k510

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_onnx_fp32_image.py --target k510 --model models/mobilenetv2-7.onnx
```

### 4.3.3 Compilar el modelo de café float32

- El paquete de rueda de café está[tomado de](https://github.com/kendryte/caffe/releases)kendryte caffe
- conv2d_caffe_fp32.py script es el siguiente

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

- Ejecute el siguiente comando para compilar el modelo de caffe de conv2d, con el destino k510

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/conv2d_caffe_fp32.py --target k510 --caffemodel models/test.caffemodel --prototxt models/test.prototxt
```

### 4.3.4 Compilar y agregar modelo de onnx float32 previo al proceso

- Para los modelos onnx, se recomienda simplificar el uso de[ONNX Simplifier](https://github.com/daquexian/onnx-simplifier)antes de compilar con nncase
- Mobilenetv2_onnx_fp32_preprocess.py script es el siguiente

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

- Ejecute el siguiente comando para compilar el modelo onnx de mobiletv2 con el destino k510

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_onnx_fp32_preprocess.py --target k510 --model models/mobilenetv2-7.onnx
```

### 4.3.5 Compilar el modelo tflite de cuantización uint8

- Mobilenetv2_tflite_uint8_image.py script es el siguiente

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

- Ejecute el siguiente comando para compilar el modelo tflite de uint8 quantized mobiletv2, target k510

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_tflite_uint8_image.py --target k510 --model models/mobilenet_v2_1.0_224.tflite
```

## 4.4 API del modelo de inferencia

Además de los AP del modelo compilado, nncase también proporciona las API del modelo de inferencia, que se pueden inferir en el PC antes de la compilación del kmodel, que se utiliza para verificar si los resultados de la inferencia de nncase y los resultados en tiempo de ejecución del marco de aprendizaje profundo correspondiente son consistentes.

### 4.4.1 Rango de memoria

**Descripción de la característica**

La clase MemoryRange, que se utiliza para representar un rango de memoria

**Definición de clase**

```python
py::class_<memory_range>(m, "MemoryRange")
    .def_readwrite("location", &memory_range::memory_location)
    .def_property(
        "dtype", [](const memory_range &range) { return to_dtype(range.datatype); },
        [](memory_range &range, py::object dtype) { range.datatype = from_dtype(py::dtype::from_args(dtype)); })
    .def_readwrite("start", &memory_range::start)
    .def_readwrite("size", &memory_range::size);
```

Cada propiedad se describe a continuación

| Nombre de la propiedad | tipo           | Sí o no | descripción                                                                       |
| -------- | -------------- | -------- | -------------------------------------------------------------------------- |
| ubicación | Int            | no       | Posición de memoria, 0 para entrada, 1 para salida, 2 para rdata, 3 para datos, 4 para shared_data |
| dtype    | Tipo de datos de Python | no       | tipo de dato                                                                   |
| empezar    | Int            | no       | Dirección de inicio de memoria                                                               |
| tamaño     | Int            | no       | Tamaño de la memoria                                                                   |

**Ejemplo de código**

Instanciar MemoryRange

```python
mr = nncase.MemoryRange()
```

### 4.4.2 RuntimeTensor

**Descripción de la característica**

La clase RuntimeTensor, que representa el tensor de tiempo de ejecución

**Definición de clase**

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

Cada propiedad se describe a continuación

| Nombre de la propiedad | tipo | Sí o no | descripción             |
| -------- | ---- | -------- | ---------------- |
| dtype    | Int  | no       | Tipo de datos de Tensor |
| forma    | lista | no       | La forma del tensor     |

#### from_numpy()

**Descripción de la característica**

Construir el objeto RuntimeTensor a partir de numpy.ndarray

**Definición de la interfaz**

```python
from_numpy(py::array arr)
```

**Parámetros de entrada**

| Nombre del parámetro | tipo          | Sí o no | descripción              |
| -------- | ------------- | -------- | ----------------- |
| Arr      | numpy.ndarray | ser       | Objeto numpy.ndarray |

**El valor devuelto**

RuntimeTensor

**Ejemplo de código**

```python
tensor = nncase.RuntimeTensor.from_numpy(self.inputs[i]['data'])
```

#### copy_to()

**Descripción de la característica**

Copiar tensor de tiempo de ejecución

**Definición de la interfaz**

```python
copy_to(RuntimeTensor to)
```

**Parámetros de entrada**

| Nombre del parámetro | tipo          | Sí o no | descripción              |
| -------- | ------------- | -------- | ----------------- |
| Para       | RuntimeTensor | ser       | Objeto RuntimeTensor |

**El valor devuelto**

N/A

**Ejemplo de código**

```python
sim.get_output_tensor(i).copy_to(to)
```

#### to_numpy()

**Descripción de la característica**

Convertir RuntimeTensor en un objeto numpy.ndarray

**Definición de la interfaz**

```python
to_numpy()
```

**Parámetros de entrada**

N/A

**El valor devuelto**

Objeto numpy.ndarray

**Ejemplo de código**

```python
arr = sim.get_output_tensor(i).to_numpy()
```

### 4.4.3 Simulador

**Descripción de la característica**

Clase de simulador para inferencia kmodel en PC

**Definición de clase**

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

Cada propiedad se describe a continuación

| Nombre de la propiedad     | tipo | Sí o no | descripción     |
| ------------ | ---- | -------- | -------- |
| inputs_size  | Int  | no       | Introduzca el número de |
| outputs_size | Int  | no       | El número de salidas |

**Ejemplo de código**

Instanciar el simulador

```python
sim = nncase.Simulator()
```

#### load_model()

**Descripción de la característica**

Cargar el kmodel

**Definición de la interfaz**

```python
load_model(model_content)
```

**Parámetros de entrada**

| Nombre del parámetro      | tipo   | Sí o no | descripción         |
| ------------- | ------ | -------- | ------------ |
| model_content | byte[] | ser       | Flujo de bytes de Kmodel |

**El valor devuelto**

N/A

**Ejemplo de código**

```python
sim.load_model(kmodel)
```

#### get_input_desc()

**Descripción de la característica**

Obtiene la descripción de la entrada para el índice especificado

**Definición de la interfaz**

```python
get_input_desc(index)
```

**Parámetros de entrada**

| Nombre del parámetro | tipo | Sí o no | descripción       |
| -------- | ---- | -------- | ---------- |
| índice    | Int  | ser       | El índice de la entrada |

**El valor devuelto**

Rango de memoria

**Ejemplo de código**

```python
input_desc_0 = sim.get_input_desc(0)
```

#### get_output_desc()

**Descripción de la característica**

Obtiene la descripción del resultado del índice especificado

**Definición de la interfaz**

```python
get_output_desc(index)
```

**Parámetros de entrada**

| Nombre del parámetro | tipo | Sí o no | descripción       |
| -------- | ---- | -------- | ---------- |
| índice    | Int  | ser       | El índice de la salida |

**El valor devuelto**

Rango de memoria

**Ejemplo de código**

```python
output_desc_0 = sim.get_output_desc(0)
```

#### get_input_tensor()

**Descripción de la característica**

Obtiene el RuntimeTensor para la entrada del índice especificado

**Definición de la interfaz**

```python
get_input_tensor(index)
```

**Parámetros de entrada**

| Nombre del parámetro | tipo | Sí o no | descripción             |
| -------- | ---- | -------- | ---------------- |
| índice    | Int  | ser       | Introduzca el índice del tensor |

**El valor devuelto**

RuntimeTensor

**Ejemplo de código**

```python
input_tensor_0 = sim.get_input_tensor(0)
```

#### set_input_tensor()

**Descripción de la característica**

Establece el tensor en tiempo de ejecución para la entrada del índice especificado

**Definición de la interfaz**

```python
set_input_tensor(index, tensor)
```

**Parámetros de entrada**

| Nombre del parámetro | tipo          | Sí o no | descripción                    |
| -------- | ------------- | -------- | ----------------------- |
| índice    | Int           | ser       | Introduzca el índice de RuntimeTensor |
| tensor   | RuntimeTensor | ser       | Escriba RuntimeTensor       |

**El valor devuelto**

N/A

**Ejemplo de código**

```python
sim.set_input_tensor(0, nncase.RuntimeTensor.from_numpy(self.inputs[0]['data']))
```

#### get_output_tensor()

**Descripción de la característica**

Obtiene el tensor en tiempo de ejecución para la salida del índice especificado

**Definición de la interfaz**

```python
get_output_tensor(index)
```

**Parámetros de entrada**

| Nombre del parámetro | tipo | Sí o no | descripción                    |
| -------- | ---- | -------- | ----------------------- |
| índice    | Int  | ser       | Genera el índice de RuntimeTensor |

**El valor devuelto**

RuntimeTensor

**Ejemplo de código**

```python
output_arr_0 = sim.get_output_tensor(0).to_numpy()
```

#### set_output_tensor()

**Descripción de la característica**

Establece el RuntimeTensor para la salida del índice especificado

**Definición de la interfaz**

```python
set_output_tensor(index, tensor)
```

**Parámetros de entrada**

| Nombre del parámetro | tipo          | Sí o no | descripción                    |
| -------- | ------------- | -------- | ----------------------- |
| índice    | Int           | ser       | Genera el índice de RuntimeTensor |
| tensor   | RuntimeTensor | ser       | Tensor de tiempo de ejecución de salida       |

**El valor devuelto**

N/A

**Ejemplo de código**

```python
sim.set_output_tensor(0, tensor)
```

#### run()

**Descripción de la característica**

Ejecutar inferencia kmodel

**Definición de la interfaz**

```python
run()
```

**Parámetros de entrada**

N/A

**El valor devuelto**

N/A

**Ejemplo de código**

```python
sim.run()
```

## 4.5 Ejemplo de un modelo de inferencia

**Prerrequisito:**mobilenetv2_onnx_fp32_image.py script se ha compilado con el modelo mobiletv2-7.onnx

mobilenetv2_onnx_simu.py se encuentra en el subdirectorio /path/to/nncase_sdk/examples/scripts, que dice lo siguiente:

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

Ejecutar el script de inferencia

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_onnx_simu.py --model_file models/mobilenetv2-7.onnx --kmodel_file tmp/mobilenetv2_onnx_fp32_image/test.kmodel --input_file mobilenetv2_onnx_fp32_image/data/input_0_0.bin
```

La comparación de los resultados del simulador de nncase y la inferencia de la CPU es la siguiente

```shell
... ...
output 0 cosine similarity : 0.9992437958717346
```

# 5 nncase biblioteca de tiempo de ejecución

## 5.1 Introducción al tiempo de ejecución de nncase

nncase runtime se utiliza para cargar kmodel en dispositivos de IA / establecer datos de entrada / realizar cálculos de KPU / obtener datos de salida, etc.

Actualmente, solo **la versión de C++**de las API, los archivos de encabezado relacionados y las bibliotecas estáticas están disponibles en el directorio nncase sdk/riscv64

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

## 5.2 API de tiempo de ejecución

### 5.2.1 runtime_tensor de clase

Tensor utilizado para almacenar datos de entrada/salida del modelo

#### hrt::create()

**Descripción de la característica**

Crear una runtime_tensor

**Definición de la interfaz**

```C++
(1) NNCASE_API result<runtime_tensor> create(datatype_t datatype, runtime_shape_t shape, memory_pool_t pool = pool_cpu_only, uintptr_t physical_address = 0) noexcept;

(2) NNCASE_API result<runtime_tensor> create(datatype_t datatype, runtime_shape_t shape, gsl::span<gsl::byte> data, bool copy, memory_pool_t pool = pool_cpu_only, uintptr_t physical_address = 0) noexcept;
```

**Parámetros de entrada**

| Nombre del parámetro         | tipo                  | Sí o no | descripción                              |
| ---------------- | --------------------- | -------- | --------------------------------- |
| Datatype         | datatype_t            | ser       | Tipo de datos, como dt_float32            |
| forma            | runtime_shape_t       | ser       | La forma del tensor                      |
| datos             | gsl::span\<gsl::byte> | ser       | Búfer de datos de estado de usuario                  |
| copiar             | Bool                  | ser       | Si se debe copiar                          |
| piscina             | memory_pool_t         | no       | Tipo de grupo de memoria, el valor predeterminado es pool_cpu_only |
| physical_address | uintptr_t             | no       | Dirección física, el valor predeterminado es 0               |

**El valor devuelto**

resultado<runtime_tensor>

Ejemplo de código

```c++
// create input
auto in_shape = interp.input_shape(0);
auto input_tensor = host_runtime_tensor::create(dt_float32, in_shape,
                                                {(gsl::byte *)mat.data, mat.cols * mat.rows * mat.elemSize()},
                                                true, hrt::pool_shared).expect("cannot create input tensor");
```

### 5.2.2 Intérprete de clase

Interpreter es una instancia en ejecución del tiempo de ejecución de nncase, que proporciona funciones funcionales básicas como load_model()/run()/input_tensor()/output_tensor().

#### load_model()

**Descripción de la característica**

Cargar el modelo kmodel

**Definición de la interfaz**

```C++
 NNCASE_NODISCARD result<void> load_model(gsl::span<const gsl::byte> buffer) noexcept;
```

**Parámetros de entrada**

| Nombre del parámetro | tipo                            | Sí o no | descripción          |
| -------- | ------------------------------- | -------- | ------------- |
| búfer   | gsl::span `<const gsl::byte>` | ser       | búfer kmodel |

**El valor devuelto**

resultado `<void>`

**Ejemplo de código**

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

**Descripción de la característica**

Obtiene el número de entradas de modelo

**Definición de la interfaz**

```C++
size_t inputs_size() const noexcept;
```

**Parámetros de entrada**

N/A

**El valor devuelto**

size_t

**Ejemplo de código**

```c++
auto inputs_size = interp.inputs_size();
```

#### outputs_size()

**Descripción de la característica**

Obtiene el número de salidas del modelo

**Definición de la interfaz**

```C++
size_t outputs_size() const noexcept;
```

**Parámetros de entrada**

N/A

**El valor devuelto**

size_t

**Ejemplo de código**

```c++
auto outputs_size = interp.outputs_size();
```

#### input_shape()

**Descripción de la característica**

Obtiene la forma de la entrada especificada del modelo

**Definición de la interfaz**

```C++
const runtime_shape_t &input_shape(size_t index) const noexcept;
```

**Parámetros de entrada**

| Nombre del parámetro | tipo   | Sí o no | descripción       |
| -------- | ------ | -------- | ---------- |
| índice    | size_t | ser       | El índice de la entrada |

**El valor devuelto**

runtime_shape_t

**Ejemplo de código**

```c++
auto in_shape = interp.input_shape(0);
```

#### output_shape()

**Descripción de la característica**

Obtiene la forma del resultado especificado del modelo

**Definición de la interfaz**

```C++
const runtime_shape_t &output_shape(size_t index) const noexcept;
```

**Parámetros de entrada**

| Nombre del parámetro | tipo   | Sí o no | descripción       |
| -------- | ------ | -------- | ---------- |
| índice    | size_t | ser       | El índice de la salida |

**El valor devuelto**

runtime_shape_t

**Ejemplo de código**

```c++
auto out_shape = interp.output_shape(0);
```

#### input_tensor()

**Descripción de la característica**

Obtiene/establece el tensor de entrada para el índice especificado

**Definición de la interfaz**

```C++
(1) result<runtime_tensor> input_tensor(size_t index) noexcept;
(2) result<void> input_tensor(size_t index, runtime_tensor tensor) noexcept;
```

**Parámetros de entrada**

| Nombre del parámetro | tipo           | Sí o no | descripción                     |
| -------- | -------------- | -------- | ------------------------ |
| índice    | size_t         | ser       | búfer kmodel            |
| tensor   | runtime_tensor | ser       | Introduzca el tensor de tiempo de ejecución correspondiente |

**El valor devuelto**

(1) Devuelve los resultados<runtime_tensor>

(2) Devuelve los resultados `<void>`

**Ejemplo de código**

```c++
// set input
interp.input_tensor(0, input_tensor).expect("cannot set input tensor");
```

#### output_tensor()

**Descripción de la característica**

Obtiene/establece el tensor saliente para el índice especificado

**Definición de la interfaz**

```C++
(1) result<runtime_tensor> output_tensor(size_t index) noexcept;
(2) result<void> output_tensor(size_t index, runtime_tensor tensor) noexcept;
```

**Parámetros de entrada**

| Nombre del parámetro | tipo           | Sí o no | descripción                     |
| -------- | -------------- | -------- | ------------------------ |
| índice    | size_t         | ser       |                          |
| tensor   | runtime_tensor | ser       | Introduzca el tensor de tiempo de ejecución correspondiente |

**El valor devuelto**

(1) Devuelve los resultados<runtime_tensor>

(2) Devuelve los resultados `<void>`

**Ejemplo de código**

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

**Descripción de la característica**

Realizar cálculos de kPU

**Definición de la interfaz**

```C++
result<void> run() noexcept;
```

**Parámetros de entrada**

N/A

**El valor devuelto**

resultado `<void>`

**Ejemplo de código**

```c++
// run
interp.run().expect("error occurred in running model");
```

## 5.3 Ejemplo de tiempo de ejecución

El código de ejemplo se encuentra en /path/to/nncase_sdk/examples/mobilenetv2_onnx_fp32_image

**Condición de prefijo**

- mobilenetv2_onnx_fp32_image.py script ha compilado el modelo MobileTV2-7.onnx
- Dado que el ejemplo se basa en la biblioteca de OpenCV, debe especificar la ruta de acceso a OpenCV en la .txt CMakeLists del ejemplo.

**Aplicaciones de compilación cruzada**

```shell
cd /path/to/nncase_sdk/examples
./build.sh
```

Finalmente, genere el mobilenetv2_onnx_fp32_image en el directorio out/bin

**El k510 EVB funciona en la placa**

Copie los siguientes archivos en la placa k510 EVB

| archivo                        | comentario                                                         |
| --------------------------- | ------------------------------------------------------------ |
| mobilenetv2_onnx_fp32_image | Se generan ejemplos de compilación cruzada                                         |
| test.kmodel                 | Utilice mobilenetv2_onnx_fp32_image.py compilar la compilación mobiletv2-7.onnx |
| .png y labels_1000.txt de gatos    | Ubicado debajo del subdirectorio /path/to/nncase_sdk/examples/mobilenetv2_onnx_fp32_image/data/ |

```bash
$ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mnt/zhangyang/nncase_check/lib/gomp:/mnt/zhangyang/nncase_check/lib/opencv
$ ./mobilenetv2_onnx_fp32_image test.kmodel cat.png labels_1000.txt
case ./mobilenetv2_onnx_fp32_image build at Mar  1 2022 16:31:29
interp.run() duration: 12.6642 ms
image classification result: tiger cat(9.25)
```

# 6 Bibliotecas de programación funcional (soporte en tiempo de ejecución)

## 6.1 Introducción a la funcionalidad

nncase Functional se utiliza para mejorar la facilidad de uso cuando los usuarios pre y post-proceso modelos

Actualmente, solo está disponible la versión C++ de las API, y los archivos de encabezado y las bibliotecas asociados se encuentran en el directorio riscv64 del sdk de nncase.

## 6.2 API

### 6.2.1 cuadrado

**Descripción de la característica**

Calcule el cuadrado, actualmente admite la entrada uint8 / int8, la salida también es uint8 / int8, tenga en cuenta que la entrada es de punto fijo y la salida es de punto flotante necesario para establecer los parámetros de cuantización.

**Definición de la interfaz**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`square`](#ops_8h_1adff2f60c7c045a9840519eab2c04d127)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parámetros de entrada**

| Nombre del parámetro  | tipo           | Sí o no | descripción                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | ser       | entrada                |
| `dtype` | datatype_t     | ser       | Tipo de datos del tensor de salida |

**El valor devuelto**

`result<runtime_tensor>`

**Ejemplo de código**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto squared = F::square(input, output_type).unwrap_or_throw();
```

### 6.2.2 sqrt

**Descripción de la característica**

Calcule el valor del número raíz, actualmente admite la entrada uint8 / int8, la salida también es uint8 / int8, tenga en cuenta que la entrada es de punto fijo y la salida es de punto flotante necesita establecer los parámetros de cuantización.

**Definición de la interfaz**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`sqrt`](#ops_8h_1a53f8dde3dd4e27058b5dc743eb5dd076)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parámetros de entrada**

| Nombre del parámetro  | tipo           | Sí o no | descripción                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | ser       | entrada                |
| `dtype` | datatype_t     | ser       | Tipo de datos del tensor de salida |

**El valor devuelto**

`result<runtime_tensor>`

**Ejemplo de código**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::sqrt(input, output_type).unwrap_or_throw();
```

### 6.2.3 Registro

**Descripción de la característica**

Calcule el valor de registro, el número negativo de entrada se convertirá a Nan, actualmente admite la entrada uint8 / int8, la salida también es uint8 / int8, tenga en cuenta que la entrada es de punto fijo y la salida es de punto flotante necesita establecer el parámetro de cuantización.

**Definición de la interfaz**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`log`](#ops_8h_1a91df53276c3f1511427d4ac1a0140b71)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parámetros de entrada**

| Nombre del parámetro  | tipo           | Sí o no | descripción                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | ser       | entrada                |
| `dtype` | datatype_t     | ser       | Tipo de datos del tensor de salida |

**El valor devuelto**

`result<runtime_tensor>`

**Ejemplo de código**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::log(input, output_type).unwrap_or_throw();
```

### 6.2.4 exp

**Descripción de la característica**

Calcule el valor exp, actualmente admite la entrada uint8 / int8, la salida también es uint8 / int8, tenga en cuenta que la entrada es de punto fijo y la salida es de punto flotante necesario para establecer los parámetros de cuantización.

**Definición de la interfaz**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`exp`](#ops_8h_1a2c6ce457805a5ba515fa7454fb4aede0)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parámetros de entrada**

| Nombre del parámetro  | tipo           | Sí o no | descripción                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | ser       | entrada                |
| `dtype` | datatype_t     | ser       | Tipo de datos del tensor de salida |

**El valor devuelto**

`result<runtime_tensor>`

**Ejemplo de código**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::exp(input, output_type).unwrap_or_throw();
```

### 6.2.5 sin

**Descripción de la característica**

Para calcular el valor sin, la entrada uint8 / int8 es actualmente compatible, y la salida también es uint8 / int8, tenga en cuenta que los parámetros de cuantización deben establecerse cuando la entrada es de punto fijo y la salida es de punto flotante.

**Definición de la interfaz**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`sin`](#ops_8h_1a9605b2b0dc9a6892ce878bda14586890)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parámetros de entrada**

| Nombre del parámetro  | tipo           | Sí o no | descripción                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | ser       | entrada                |
| `dtype` | datatype_t     | ser       | Tipo de datos del tensor de salida |

**El valor devuelto**

`result<runtime_tensor>`

**Ejemplos de código**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::sin(input, output_type).unwrap_or_throw();
```

### 6.2.6 cuerpo

**Descripción de la característica**

Calcule el valor cos, actualmente admite la entrada uint8 / int8, la salida también es uint8 / int8, tenga en cuenta que la entrada es de punto fijo y la salida es de punto flotante necesita establecer el parámetro de cuantización.

**Definición de la interfaz**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`cos`](#ops_8h_1a71d36c13c82f4c411f24d030cf333249)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parámetros de entrada**

| Nombre del parámetro  | tipo           | Sí o no | descripción                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | ser       | entrada                |
| `dtype` | datatype_t     | ser       | Tipo de datos del tensor de salida |

**El valor devuelto**

`result<runtime_tensor>`

**Ejemplos de código**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::cos(input, output_type).unwrap_or_throw();
```

### 6.2.7 ronda

**Descripción de la característica**

Para calcular el valor redondo, actualmente se admite la entrada uint8/ int8 y la salida también es uint8/ int8, tenga en cuenta que el parámetro de cuantización debe establecerse cuando la entrada es de punto fijo y la salida es de punto flotante.

**Definición de la interfaz**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`round`](#ops_8h_1a81db8ac4866004f75fb65db876262785)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parámetros de entrada**

| Nombre del parámetro  | tipo           | Sí o no | descripción                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | ser       | entrada                |
| `dtype` | datatype_t     | ser       | Tipo de datos del tensor de salida |

**El valor devuelto**

`result<runtime_tensor>`

**Ejemplos de código**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::round(input, output_type).unwrap_or_throw();
```

### Piso 6.2.8

**Descripción de la característica**

Calcule el valor de escarcha, actualmente admite la entrada uint8 / int8, la salida también es uint8 / int8, tenga en cuenta que la entrada es de punto fijo y la salida es de punto flotante necesario para establecer los parámetros de cuantización.

**Definición de la interfaz**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`floor`](#ops_8h_1a1079af8fe9fb6edbb2906d91fac12635)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parámetros de entrada**

| Nombre del parámetro  | tipo           | Sí o no | descripción                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | ser       | entrada                |
| `dtype` | datatype_t     | ser       | Tipo de datos del tensor de salida |

**El valor devuelto**

`result<runtime_tensor>`

**Ejemplos de código**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::floor(input, output_type).unwrap_or_throw();
```

### 6.2.9 Ceil

**Descripción de la característica**

Calcule el valor de ceil, actualmente admite la entrada uint8 / int8, la salida también es uint8 / int8, tenga en cuenta que la entrada es de punto fijo y la salida es de punto flotante necesario para establecer los parámetros de cuantización.

**Definición de la interfaz**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`ceil`](#ops_8h_1ad3b78c97f1e5348a26de7e5ba2396fb7)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parámetros de entrada**

| Nombre del parámetro  | tipo           | Sí o no | descripción                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | ser       | entrada                |
| `dtype` | datatype_t     | ser       | Tipo de datos del tensor de salida |

**El valor devuelto**

`result<runtime_tensor>`

**Ejemplos de código**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::ceil(input, output_type).unwrap_or_throw();
```

### 6.2.10 abdominales

**Descripción de la característica**

Calcule el valor abs, actualmente admite la entrada uint8 / int8, la salida también es uint8 / int8, tenga en cuenta que la entrada es de punto fijo y la salida es de punto flotante necesita establecer los parámetros de cuantización.

**Definición de la interfaz**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`abs`](#ops_8h_1ad8290dc793bae0dc22b3baf9e0f80c14)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parámetros de entrada**

| Nombre del parámetro  | tipo           | Sí o no | descripción                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | ser       | entrada                |
| `dtype` | datatype_t     | ser       | Tipo de datos del tensor de salida |

**El valor devuelto**

`result<runtime_tensor>`

**Ejemplos de código**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::abs(input, output_type).unwrap_or_throw();
```

### 6.2.11 neg

**Descripción de la característica**

Calcule el valor de neg, actualmente admite la entrada uint8 / int8, la salida también es uint8 / int8, tenga en cuenta que la entrada es de punto fijo y la salida es de punto flotante necesita establecer los parámetros de cuantización.

**Definición de la interfaz**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`neg`](#ops_8h_1aa1b7858802e1afce78db72163c5210d8)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parámetros de entrada**

| Nombre del parámetro  | tipo           | Sí o no | descripción                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | ser       | entrada                |
| `dtype` | datatype_t     | ser       | Tipo de datos del tensor de salida |

**El valor devuelto**

`result<runtime_tensor>`

**Ejemplos de código**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::neg(input, output_type).unwrap_or_throw();
```

### 6.2.12 Cuantizar

**Descripción de la característica**

dt_bfloat16 de entrada, datos de dt_float32, dt_int8 de salida o salida de dt_uint8

**Definición de la interfaz**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`quantize`](#ops_8h_1ad8ad779083b5c08da520d2f1c2469c3a)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parámetros de entrada**

| Nombre del parámetro  | tipo           | Sí o no | descripción                                |
| --------- | -------------- | -------- | ----------------------------------- |
| `input` | runtime_tensor | ser       | La entrada, el tipo debe ser float32 o bfloat16 |
| `dtype` | datatype_t     | ser       | Tipo de datos del tensor de salida                 |

**El valor devuelto**

`result<runtime_tensor>`

**Ejemplos de código**

```cpp
auto quantized = F::quantize(input, dt_int8).unwrap_or_throw();
```

### 6.2.13 descuantizar

**Descripción de la característica**

Ingrese la entrada uint8 o int8, convierta en datos flotantes o bfloat. Tenga en cuenta que el usuario debe establecer los parámetros de cuantización correctos para los datos de antemano para la descuantización.

**Definición de la interfaz**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`dequantize`](#ops_8h_1ab91a262349baf393c91abad6f393de24)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Parámetros de entrada**

| Nombre del parámetro  | tipo           | Sí o no | descripción                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | ser       | entrada                |
| `dtype` | datatype_t     | ser       | Tipo de datos del tensor de salida |

**El valor devuelto**

`result<runtime_tensor>`

**Ejemplos de código**

```cpp
input.quant_param({ 0, 1 });
auto dequantized = F::dequantize(input, output_type).unwrap_or_throw();
```

### 6.2.14 cultivo

**Descripción de la característica**

Cajas de bboxes dadas, recortadas del tensor original y redimensionando la salida en el nuevo tensor. Acepte dt_bfloat16, dt_float32, dt_int8, salida de tipo dt_uint8, salida del mismo tipo.

**Definición de la interfaz**

`NNCASE_API inline result<runtime::runtime_tensor> crop(runtime::runtime_tensor &input, runtime::runtime_tensor &bbox, size_t out_h, size_t out_w, image_resize_mode_t resize_mode, bool align_corners, bool half_pixel_centers) noexcept`

**Parámetros de entrada**

| Nombre del parámetro           | tipo                | Sí o no | descripción                                                                                     |
| ------------------ | ------------------- | -------- | ---------------------------------------------------------------------------------------- |
| entrada              | runtime_tensor      | ser       | Ingrese los datos, debe formatear [n, c, h, w] el diseño, si los datos son uint8 o int8, asegúrese de la exactitud de los parámetros de cuantificación de datos       |
| caja de bbox               | runtime_tensor      | ser       | Ingrese los datos de la caja de herramientas, necesita formatear [1,1,m,4] el diseño, los datos internos son[y0,x0,y1,x1], el tipo es[float32,bfloat16] |
| out_h              | size_t              | ser       | Altura de los datos de salida                                                                           |
| out_w              | size_t              | ser       | Introduzca el ancho de datos                                                                            |
| resize_mode        | image_resize_mode_t | ser       | Cambiar el tamaño del patrón de método                                                                           |
| align_corners      | Bool                | ser       | Cambiar el tamaño de si align_corners                                                    |
| half_pixel_centers | Bool                | ser       | Cambiar el tamaño si el píxel está alineado al centro                                                                  |

**El valor devuelto**

`result<runtime_tensor>`

**Ejemplos de código**

```cpp
auto bbox = get_rand_bbox(input_shape, roi_amount);
auto &&[out_h, out_w] = get_rand_out_hw();
auto output_opt = F::crop(input, bbox, out_h, out_w, resize_mode).unwrap_or_throw();
```

### 6.2.15 cambio de tamaño

**Descripción de la característica**

Dado el ancho de altura de salida, coloque el tensor de entrada redimensionado al nuevo tamaño. Acepte dt_bfloat16, dt_float32, dt_int8, salida de tipo dt_uint8, salida del mismo tipo.

**Definición de la interfaz**

`NNCASE_API inline result<runtime::runtime_tensor> resize(runtime::runtime_tensor &input, size_t out_h, size_t out_w, image_resize_mode_t resize_mode, bool align_corners, bool half_pixel_centers) noexcept`

**Parámetros de entrada**

| Nombre del parámetro           | tipo                | Sí o no | descripción                                                                               |
| ------------------ | ------------------- | -------- | ---------------------------------------------------------------------------------- |
| entrada              | runtime_tensor      | ser       | Ingrese los datos, debe ser [n, c, h, w] formateado, si los datos son uint8 o int8, asegúrese de la exactitud de los parámetros de cuantificación de datos |
| out_h              | size_t              | ser       | Altura de los datos de salida                                                                     |
| out_w              | size_t              | ser       | Introduzca el ancho de datos                                                                      |
| resize_mode        | image_resize_mode_t | ser       | Cambiar el tamaño del patrón de método                                                                     |
| align_corners      | Bool                | ser       | Cambiar el tamaño de si align_corners                                              |
| half_pixel_centers | Bool                | ser       | Cambiar el tamaño si el píxel está alineado al centro                                                            |

**El valor devuelto**

`result<runtime_tensor>`

**Ejemplos de código**

```cpp
auto &&[out_h, out_w] = get_rand_out_hw();
auto output_opt = F::resize(input, out_h, out_w, resize_mode, false, false).unwrap_or_throw();
```

### 6.2.16 almohadilla

**Descripción de la característica**

Los datos de relleno de cada dimensión aceptan dt_bfloat16, dt_float32, dt_int8, dt_uint8 tipo de salida y salida del mismo tipo.

**Definición de la interfaz**

`NNCASE_API inline result<runtime::runtime_tensor> pad(runtime::runtime_tensor &input, runtime_paddings_t &paddings, pad_mode_t pad_mode, float fill_v)`

**Parámetros de entrada**

| Nombre del parámetro | tipo               | Sí o no | descripción                                                                                                                                       |
| -------- | ------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| entrada    | runtime_tensor     | ser       | Introduzca los datos, si los datos son uint8 o int8 Asegúrese de la exactitud de los parámetros de cuantificación de datos                                                                                  |
| relleno  | runtime_paddings_t | ser       | Por ejemplo, el valor de relleno se `[ {2,3}, {1,3} ]`indica delante de la almohadilla 2 en la última dimensión, seguida de la almohadilla 3. La penúltima dimensión está precedida por la almohadilla 1, seguida de la almohadilla 2 |
| pad_mode | pad_mode_t         | ser       | Actualmente, solo se admite el modo const                                                                                                                   |
| fill_v   | flotar              | ser       | Rellenar los valores                                                                                                                                     |

**El valor devuelto**

`result<runtime_tensor>`

**Ejemplos de código**

```cpp
runtime_paddings_t paddings{ { 0, 0 }, { 0, 0 }, { 0, 0 }, { 1, 2 } };
auto output = F::pad(input, paddings, pad_constant, pad_value).unwrap_or_throw();
```
<!-- markdownlint-enable no-emphasis-as-header -->
# 7 Libro Blanco Cuantitativo

## 7.1 Libro Blanco de Cuantificación del Modelo de Clasificación

| Modelo de clasificación     | Precisión de la CPU (Top-1) | Precisión de coma flotante (Top-1) | Precisión uint8 (Top-1) | Precisión int8 (Top-1) |
| ------------ | -------------- | --------------- | ---------------- | --------------- |
| alexnet      | 0.531          | 0.53            | N/A              | 0.52            |
| densenet 121 | 0.732          | 0.732           | 0.723            | N/A             |
| inicio v3 | 0.766          | 0.765           | 0.773            | 0.77            |
| inicio v4 | 0.789          | 0.789           | 0.793            | 0.792           |
| mobilenet v1 | 0.731          | 0.73            | 0.723            | 0.718           |
| mobilenet v2 | 0.713          | 0.715           | 0.713            | 0.719           |
| resnet50 v2  | 0.747          | 0.74            | 0.748            | 0.749           |
| vgg 16       | 0.689          | 0.687           | 0.690            | 0.689           |

> Esta tabla es principalmente para comparar el rendimiento de la cuantización, la precisión de la CPU son los datos completos del conjunto de validación de ImageNet, y la precisión de punto flotante y cuantización es el resultado de la prueba de subconjunto de datos para la primera imagen de las 1000 clases en el conjunto de validación de acuerdo con el número ordinal.
>
> Los resultados de las pruebas de Alexnet y SenseNet son datos antiguos, los cuales son resultados de prueba de las primeras 1000 imágenes del conjunto de verificación como un subconjunto de los datos, y N / A es que el subconjunto de datos de prueba en ese momento es diferente de la CPU, por lo que no se utiliza como comparación.
>
> Debido a que la red seleccionada no se origina necesariamente en el oficial o hay diferencias en el preprocesamiento, etc., puede diferir del rendimiento oficial.

## 7.2 Informe técnico sobre cuantificación del modelo de detección

1. YOLOV3

    | COCOAPI                                                      | Resultados oficiales | Precisión de coma flotante de la CPU | gnne precisión de coma flotante | Precisión uint8 | precisión int8 |
    | ------------------------------------------------------------ | -------- | ----------- | ------------ | --------- | -------- |
    | Precisión media (AP) @ [IoU = 0,50:0,95\| área = todos \| maxDets = 100] | 0.314    | 0.307       | 0.306        | 0.295     | 0.288    |
    | Precisión media (AP) @ [IoU = 0,50\| área = todos \| maxDets = 100] | 0.559    | 0.555       | 0.554        | 0.555     | 0.554    |
    | Precisión media (AP) @ [IoU = 0,75\| área = todos \| maxDets = 100] | 0.318    | 0.308       | 0.307        | 0.287     | 0.275    |
    | Precisión media (AP) @ [IoU = 0,50:0,95\| área = pequeño \| maxDets = 100] | 0.142    | 0.150       | 0.149        | 0.147     | 0.144    |
    | Precisión media (AP) @ [IoU= 0.50:0.95\| área = medio \| maxDets = 100] | 0.341    | 0.332       | 0.332        | 0.322     | 0.316    |
    | Precisión media (AP) @ [IoU = 0,50:0,95\| área = grande \| maxDets = 100] | 0.464    | 0.437       | 0.437        | 0.414     | 0.404    |
    | Recuperación promedio (AR) @ [IoU= 0.50:0.95\| área = todos \| maxDets = 1] | 0.278    | 0.270       | 0.271        | 0.262     | 0.256    |
    | Recuperación promedio (AR) @ [IoU= 0.50:0.95\| área = todos \| maxDets = 10] | 0.419    | 0.412       | 0.412        | 0.399     | 0.392    |
    | Recuperación promedio (AR) @ [IoU = 0,50:0,95\| área = todos \| maxDets = 100] | 0.442    | 0.433       | 0.433        | 0.421     | 0.414    |
    | Recuperación promedio (AR) @ [IoU = 0,50:0,95\| área = pequeño \| maxDets = 100] | 0.239    | 0.251       | 0.251        | 0.248     | 0.246    |
    | Recuperación promedio (AR) @ [IoU= 0.50:0.95\| área = medio \| maxDets = 100] | 0.482    | 0.462       | 0.463        | 0.451     | 0.443    |
    | Recuperación promedio (AR) @ [IoU = 0,50:0,95\| área = grande \| maxDets = 100] | 0.611    | 0.586       | 0.585        | 0.559     | 0.550    |

2. ssd-mobilenetv1

    | COCOAPI                                                                    | Resultados oficiales | Precisión de coma flotante de la CPU | gnne precisión de coma flotante | Precisión uint8 | precisión int8 |
    | -------------------------------------------------------------------------- | -------- | ----------- | ------------ | --------- | -------- |
    | Precisión media (AP) @ [IoU = 0,50:0,95\| área = todos \| maxDets = 100]   | 0.184    | 0.184       | 0.184        | 0.183     | 0.183    |
    | Precisión media (AP) @ [IoU = 0,50\| área = todos \| maxDets = 100]        | 0.306    | 0.307       | 0.306        | 0.305     | 0.306    |
    | Precisión media (AP) @ [IoU = 0,75\| área = todos \| maxDets = 100]        | 0.191    | 0.192       | 0.190        | 0.189     | 0.190    |
    | Precisión media (AP) @ [IoU = 0,50:0,95\| área = pequeño \| maxDets = 100] | 0.017    | 0.017       | 0.017        | 0.017     | 0.017    |
    | Precisión media (AP) @ [IoU= 0.50:0.95\| área = medio \| maxDets = 100] | 0.157    | 0.157       | 0.157        | 0.156     | 0.155    |
    | Precisión media (AP) @ [IoU = 0,50:0,95\| área = grande \| maxDets = 100] | 0.371    | 0.372       | 0.371        | 0.370     | 0.369    |
    | Recuperación promedio (AR) @ [IoU= 0.50:0.95\| área = todos \| maxDets = 1]         | 0.180    | 0.180       | 0.180        | 0.181     | 0.181    |
    | Recuperación promedio (AR) @ [IoU= 0.50:0.95\| área = todos \| maxDets = 10]        | 0.242    | 0.242       | 0.242        | 0.243     | 0.243    |
    | Recuperación promedio (AR) @ [IoU = 0,50:0,95\| área = todos \| maxDets = 100]      | 0.242    | 0.242       | 0.242        | 0.243     | 0.243    |
    | Recuperación promedio (AR) @ [IoU = 0,50:0,95\| área = pequeño \| maxDets = 100]    | 0.026    | 0.026       | 0.026        | 0.026     | 0.026    |
    | Recuperación promedio (AR) @ [IoU= 0.50:0.95\| área = medio \| maxDets = 100]    | 0.206    | 0.206       | 0.206        | 0.206     | 0.205    |
    | Recuperación promedio (AR) @ [IoU = 0,50:0,95\| área = grande \| maxDets = 100]    | 0.489    | 0.491       | 0.490        | 0.490     | 0.491    |

3. YOLOV5S

    | COCOAPI                                                                    | Resultados oficiales | Precisión de coma flotante de la CPU | gnne precisión de coma flotante | Precisión uint8 | precisión int8 |
    | -------------------------------------------------------------------------- | -------- | ----------- | ------------ | --------- | -------- |
    | Precisión media (AP) @ [IoU = 0,50:0,95\| área = todos \| maxDets = 100]   | 0.367    | 0.365       | 0.335        | 0.334     | 0.335    |
    | Precisión media (AP) @ [IoU = 0,50\| área = todos \| maxDets = 100]        | 0.555    | 0.552       | 0.518        | 0.518     | 0.518    |
    | Precisión media (AP) @ [IoU = 0,75\| área = todos \| maxDets = 100]        | 0.398    | 0.395       | 0.364        | 0.363     | 0.362    |
    | Precisión media (AP) @ [IoU = 0,50:0,95\| área = pequeño \| maxDets = 100] | 0.223    | 0.220       | 0.199        | 0.199     | 0.197    |
    | Precisión media (AP) @ [IoU= 0.50:0.95\| área = medio \| maxDets = 100] | 0.419    | 0.418       | 0.387        | 0.386     | 0.386    |
    | Precisión media (AP) @ [IoU = 0,50:0,95\| área = grande \| maxDets = 100] | 0.463    | 0.459       | 0.423        | 0.422     | 0.423    |
    | Recuperación promedio (AR) @ [IoU= 0.50:0.95\| área = todos \| maxDets = 1]         | 0.306    | 0.306       | 0.288        | 0.287     | 0.287    |
    | Recuperación promedio (AR) @ [IoU= 0.50:0.95\| área = todos \| maxDets = 10]        | 0.518    | 0.518       | 0.487        | 0.486     | 0.487    |
    | Recuperación promedio (AR) @ [IoU = 0,50:0,95\| área = todos \| maxDets = 100]      | 0.576    | 0.576       | 0.540        | 0.539     | 0.540    |
    | Recuperación promedio (AR) @ [IoU = 0,50:0,95\| área = pequeño \| maxDets = 100]    | 0.391    | 0.399       | 0.350        | 0.350     | 0.347    |
    | Recuperación promedio (AR) @ [IoU= 0.50:0.95\| área = medio \| maxDets = 100]    | 0.641    | 0.640       | 0.606        | 0.605     | 0.607    |
    | Recuperación promedio (AR) @ [IoU = 0,50:0,95\| área = grande \| maxDets = 100]    | 0.716    | 0.710       | 0.680        | 0.683     | 0.685    |

# 8 Preguntas frecuentes

1. 安装wheel时报错: "xxx.whl no es una rueda compatible en esta plataforma". **

    Q: 安装nncase wheel包, 出现ERROR: nncase-1.0.0.20210830-cp37-cp37m-manylinux_2_24_x86_64.whl no es una rueda compatible en esta plataforma.

    A: Pip de actualización > = 20.3

    ```shell
    sudo pip3 install --upgrade pip
    ```

2. **Cuando el CRB ejecuta el programa de inferencia de la aplicación, informa del error "std::bad_alloc"**

    P: Ejecute el programa de inferencia de aplicaciones en el CRB y lance una excepción "std::bad_alloc"

    ```shell
    $ ./cpp.sh
    case ./yolov3_bfloat16 build at Sep 16 2021 18:12:03
    terminate called after throwing an instance of 'std::bad_alloc'
    what():  std::bad_alloc
    ```

    R: std::bad_alloc excepciones suelen deberse a errores de asignación de memoria, que se pueden comprobar de la siguiente manera.

    - Compruebe si el kmodel generado excede la memoria disponible del sistema actual (como el tamaño del kmodel yolov3 bfloat16 es de 121 MB, la memoria disponible actual de Linux es de solo 70 MB, se lanzará la excepción).  Si excede, intente usar la cuantización posterior al entrenamiento para reducir el tamaño del modelo k.
    - Compruebe la aplicación en busca de pérdidas de memoria

3. **Al ejecutar el programa de inferencia de la aplicación[.. t_runtime_tensor.cpp:310 (crear)], data.size_bytes() == size = false (bool).**

    P: El simulador ejecuta el programa de inferencia de la aplicación, lanzando una[.. t_runtime_tensor.cpp:310 (crear)] excepción "data.size_bytes() == size = false (bool)"

    R: Compruebe la información del tensor de entrada para la configuración, centrándose en la forma de entrada y el número de bytes ocupados por cada elemento (fp32/uint8)

**Descargo de responsabilidad de**traducción  
Para la comodidad de los clientes, Canaan utiliza un traductor de IA para traducir texto a varios idiomas, que pueden contener errores. No garantizamos la exactitud, fiabilidad o puntualidad de las traducciones proporcionadas. Canaan no será responsable de ninguna pérdida o daño causado por la confianza en la exactitud o fiabilidad de la información traducida. Si existe una diferencia de contenido entre las traducciones en diferentes idiomas, prevalecerá la versión en chino simplificado.

Si desea informar de un error o inexactitud de traducción, no dude en ponerse en contacto con nosotros por correo.
