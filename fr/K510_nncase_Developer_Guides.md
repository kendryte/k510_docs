![couverture de canaan.png](http://s2.loli.net/2022/03/30/7UG1IxrOXTo2QKw.png)

**<font face="黑体" size="6" style="float:right">K510 nncase Guide du développeur</font>**

<font face="黑体"  size=3>Version du document : V1.0.1</font>

<font face="黑体"  size=3>Date de publication : 2022-05-10</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Démenti**</font>
Les produits, services ou fonctionnalités que vous achetez sont soumis aux contrats commerciaux et aux conditions de Beijing Canaan Jiesi Information Technology Co., Ltd. (« la Société », les mêmes ci-après), et tout ou partie des produits, services ou fonctionnalités décrits dans ce document peuvent ne pas être dans le cadre de votre achat ou de votre utilisation. Sauf accord contraire dans le contrat, la Société décline toute représentation ou garantie, expresse ou implicite, quant à l'exactitude, la fiabilité, l'exhaustivité, le marketing, l'objectif spécifique et la non-agression de toute représentation, information ou contenu de ce document. Sauf convention contraire, le présent document est fourni à titre indicatif à titre indicatif d'utilisation seulement.
En raison de mises à niveau de la version du produit ou d'autres raisons, le contenu de ce document peut être mis à jour ou modifié de temps à autre sans préavis.

**<font face="黑体"  size=3>Avis sur les marques de commerce</font>**

«  »<img src="http://s2.loli.net/2022/03/30/xN21jbhnwSFyGRD.png" style="zoom:33%;" />, l'icône « Canaan », Canaan et d'autres marques de commerce de Canaan et d'autres marques de commerce de Canaan sont des marques de commerce de Beijing Canaan Jiesi Information Technology Co., Ltd. Toutes les autres marques de commerce ou marques déposées qui peuvent être mentionnées dans ce document sont la propriété de leurs propriétaires respectifs.

**<font face="黑体"  size=3>Copyright ©2022 Beijing Canaan Jiesi Information Technology Co., Ltd</font>**
Ce document ne s'applique qu'au développement et à la conception de la plate-forme K510, sans l'autorisation écrite de la société, aucune unité ou individu ne peut diffuser une partie ou la totalité du contenu de ce document sous quelque forme que ce soit.

**<font face="黑体"  size=3>Beijing Canaan Jiesi Information Technology Co., Ltd</font>**
URL: canaan-creative.com
Demandes de renseignements des entreprises : salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# préface
**<font face="黑体"  size=5>Objet </font>**du document
Ce document est un document de description pour l'utilisation du compilateur nncase/K510, fournissant aux utilisateurs comment installer nncase, comment appeler les API du compilateur pour compiler des modèles de réseau neuronal et des API d'exécution pour écrire des programmes d'inférence AI

**<font face="黑体"  size=5>Objets de lecture</font>**

Les principales personnes auxquelles ce document (ce guide) s'applique :

- Développeurs de logiciels
- Personnel de soutien technique

**<font face="黑体"  size=5>Termes et acronymes</font>**

| terme | Explication/nom complet                              |
| ---- | -------------------------------------- |
| PtQ  | Quantification post-formation, quantification post-formation |
| MSE  | erreur quadratique moyenne, erreur quadratique moyenne            |
|      |                                        |

**<font face="黑体"  size=5>Historique des révisions</font>**
 <font face="宋体"  size=2>L'historique des révisions accumule une description de chaque mise à jour de document. La dernière version du document contient des mises à jour pour toutes les versions précédentes. </font>

| Le numéro de version   | Modifié par     | Date de révision | Notes de révision |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.1 | Publicité | 2022-05-10 | nncase_v1.6.1 |
| Version 1.0.0 | Zhang Yang/Zhang Jizhao/Yang Haoqi | 2022-05-06 | nncase_v1.6.0 |
| V0.9.0 | Publicité | 2022-04-01 | nncase_v1.5.0 |
| V0.8.0 | Zhang Yang/Zhang Jizhao | 2022-03-03 | nncase_v1.4.0 |
| Version 0.7.0 | Publicité | 2022-01-28 | nncase_v1.3.0 |
| V0.6.0 | Publicité | 2021-12-31 | nncase_v1.2.0 |
| V0.5.0 | Publicité | 2021-12-03 | nncase_v1.1.0 |
| V0.4.0 | Zhang Yang/Haoqi Yang/Zheng Qihang | 2021-10-29 | nncase_v1.0.0 |
| V0.3.0 | Zhang Yang / Yang Haoqi | 2021-09-28 | nncase_v1.0.0_rc1 |
| V0.2.0 | Zhang Yang / Yang Haoqi | 2021-09-02 | nncase_v1.0.0_beta2 |
| V0.1.0 | Zhang Yang / Yang Haoqi | 2021-08-31 | nncase_v1.0.0_beta1 |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenu</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Introduction à l'environnement de développement

## 1.1 Système d'exploitation

- Ubuntu 18.04/20.04

## 1.2 Environnement logiciel

La configuration requise pour l'environnement logiciel est indiquée dans le tableau suivant :

| matricule | Ressources logicielles        | illustrer                        |
| ---- | --------------- | --------------------------- |
| 1    | Python          | Python 3.6/3.7/3.8/3.9/3.10 |
| 2    | pip3            | pip3 version > = 20,3            |
| 3    | onnx            | La version onnx est 1.9.0             |
| 4    | onnx-simplifier | La version onnx-simplifier est 0.3.6  |
| 5    | onnxoptimizer   | La version onnxoptimizer est 0.2.6    |

## 1.3 Environnement matériel

La configuration matérielle requise pour l'environnement est indiquée dans le tableau suivant :

| matricule | Ressources matérielles     | illustrer |
| ---- | ------------ | ---- |
| 1    | K510 CRB     |      |
| 2    | Carte SD et lecteur de carte |      |

# 2 introduction à nncase

## 2.1 Qu'est-ce que nncase

nncase est un compilateur de réseau neuronal conçu pour les accélérateurs d'IA et prend actuellement en charge des cibles telles que CPU / K210 / K510

Fonctionnalités fournies par nncase

- Prise en charge de plusieurs réseaux d'entrée et de sortie, prise en charge de la structure multi-branches
- Allocation de mémoire statique, aucune mémoire de tas requise
- Fusion et optimisation des opérateurs
- Prend en charge l'inférence de quantification float et uint8/int8
- Prend en charge la quantification post-entraînement, à l'aide de modèles à virgule flottante et d'ensembles d'étalonnage de quantification
- Modèle plat avec prise en charge du chargement de copie nulle

Framework de réseau neuronal pris en charge par nncase

- tflite
- onnx
- café

## 2.2 Avantages du produit

- **Déploiement simple de bout en bout**

  Réduisez le nombre d'interactions avec les utilisateurs. Le déploiement sur les KPU peut être réalisé en utilisant et en déployant les mêmes outils et processus pour les modèles CPU et GPU. Il n'est pas nécessaire de définir des paramètres complexes, d'abaisser le seuil d'utilisation et d'accélérer le cycle d'itération des algorithmes d'IA.
- **Tirer pleinement parti de l'écosystème d'IA existant**

  Attaché à un cadre largement utilisé dans l'industrie. D'une part, il peut améliorer sa visibilité et profiter des dividendes d'une écologie mature. D'autre part, les coûts de développement des développeurs de petite et moyenne taille peuvent être réduits et les modèles et algorithmes matures de l'industrie peuvent être directement déployés.
- **Tirez le meilleur parti de votre matériel**

  L'avantage de NPU est que les performances sont supérieures à celles du CPU et du GPU, et le compilateur DL doit être en mesure d'utiliser pleinement les performances du matériel. Le compilateur doit également optimiser de manière adaptative les performances de la nouvelle structure de modèle, de sorte qu'une nouvelle technique d'optimisation automatique doit être explorée en plus de l'optimisation manuelle.
- **Évolutivité et maintenabilité**

  Possibilité de prendre en charge les déploiements de modèles d'IA pour K210, K510 et les futures puces. Une certaine évolutivité doit être fournie au niveau architectural. L'ajout d'une nouvelle cible est moins coûteux et vous permet de réutiliser autant de modules que possible. Accélérer le développement de nouveaux produits pour réaliser l'accumulation de technologie de DL Compiler.

## 2.3 Architecture nncase

<img src="https://i.loli.net/2021/08/18/IQR12SOJdzxTUZH.png" alt="nncase_arch.png" style="zoom:67%;" />

La pile logicielle nnncase se compose actuellement de deux parties : le compilateur et le runtime.

**Compilateur :** Utilisé pour compiler des modèles de réseau neuronal sur un PC et éventuellement générer un fichier kmodel. Il comprend principalement importateur, IR, Evaluator, Quantize, Transform optimization, Tiling, Partition, Schedule, Codegen et d'autres modules.

- Importateur : importe des modèles à partir d'autres infrastructures de réseaux neuronaux dans nncase
- IR : Représentation intermédiaire, divisée en IR neutre importé par l'importateur (indépendant du périphérique) et IR nutral généré par l'abaissement de la conversion IR cible (dépendant du périphérique)
- Évaluateur : L'évaluateur fournit une exécution interprétative de l'IR et est souvent utilisé dans des scénarios tels que le pliage constant / étalonnage PTQ
- Transformation: Pour la transformation IR et l'optimisation de la traversée du graphe, etc.
- Quantifier : Quantifier après la formation, ajouter des marqueurs de quantification au tenseur à quantifier, appeler Evaluator pour l'exécution de l'interprétation en fonction du jeu de correction d'entrée, collecter la plage de données tensorielles, insérer des nœuds de quantification/déquantisation, et enfin optimiser pour éliminer les nœuds de quantification/déquantisation inutiles, etc.
- Carrelage: Limité par la capacité de mémoire inférieure du NPU, de gros morceaux de calcul doivent être divisés. De plus, la sélection du paramètre Tilling lorsqu'il y a une grande quantité de multiplexage de données dans le calcul aura un impact sur la latence et la bande passante.
- Partition: Divisez le graphique par ModuleType, chaque sous-graphe après fractionnement correspondra à RuntimeModule, différents types de RuntimeModule correspondent à différents périphériques (cpu / K510)
- Planification : génère un ordre de calcul et alloue des tampons en fonction des dépendances de données dans le graphique optimisé
- Codegen : Appelez le codegen correspondant à ModuleType pour chaque sous-graphe afin de générer RuntimeModule

**Runtime**: Intégré à l'application utilisateur, il fournit des fonctions telles que le chargement de kmodel / réglage des données d'entrée, l'exécution KPU et l'obtention de données de sortie

# 3 Installer nncase

La partie compilateur de la chaîne d'outils nncase inclut le compilateur nncase et K510, qui doivent tous deux installer le package de roue correspondant.

- Le paquet nncase wheel a été[publié sur nncase github](https://github.com/kendryte/nncase/releases/tag/v1.6.0), prenant en charge Python 3.6 / 3.7 / 3.8 / 3.9 / 3.10, les utilisateurs peuvent choisir la version correspondante à télécharger en fonction du système d'exploitation et de Python
- Le package de roue du compilateur K510 se trouve dans le répertoire x86_64 du SDK nncase, ne dépend pas de la version Python et peut être installé directement

Si vous n'avez pas d'environnement Ubuntu, vous pouvez utiliser[nncase docker](https://github.com/kendryte/nncase/blob/master/docs/build.md#docker)(Ubuntu 20.04 + Python 3.8).

```shell
cd /path/to/nncase_sdk
docker pull registry.cn-hangzhou.aliyuncs.com/kendryte/nncase:latest
docker run -it --rm -v `pwd`:/mnt -w /mnt registry.cn-hangzhou.aliyuncs.com/kendryte/nncase:latest /bin/bash -c "/bin/bash"
```

Ce qui suit prend Ubuntu 20.04 + Python 3.8 installation de nncase comme exemple

```shell
wget -P x86_64 https://github.com/kendryte/nncase/releases/download/v1.6.0/nncase-1.6.0.20220505-cp38-cp38-manylinux_2_24_x86_64.whl
pip3 install x86_64/*.whl
```
<!-- markdownlint-disable no-emphasis-as-header -->
# 4 Modèle de compilation/inférence

nncase fournit une**API Python**pour compiler/déduire des modèles de deep learning sur un PC

## 4.1 Opérateurs pris en charge

### 4.1.1 Opérateur tflite

| Opérateur                | Est pris en charge |
| ----------------------- | ------------ |
| ABS                     | ✅            |
| AJOUTER                     | ✅            |
| ARG_MAX                 | ✅            |
| ARG_MIN                 | ✅            |
| AVERAGE_POOL_2D         | ✅            |
| BATCH_MATMUL            | ✅            |
| JETER                    | ✅            |
| CEIL                    | ✅            |
| CONCATÉNATION           | ✅            |
| CONV_2D                 | ✅            |
| CORPS                     | ✅            |
| COUTUME                  | ✅            |
| DEPTHWISE_CONV_2D       | ✅            |
| DIV                     | ✅            |
| ÉGAL                   | ✅            |
| EXP                     | ✅            |
| EXPAND_DIMS             | ✅            |
| SOL                   | ✅            |
| FLOOR_DIV               | ✅            |
| FLOOR_MOD               | ✅            |
| FULLY_CONNECTED         | ✅            |
| PLUS                 | ✅            |
| GREATER_EQUAL           | ✅            |
| L2_NORMALIZATION        | ✅            |
| LEAKY_RELU              | ✅            |
| MOINS                    | ✅            |
| LESS_EQUAL              | ✅            |
| RAPPORT                     | ✅            |
| LOGISTIQUE                | ✅            |
| MAX_POOL_2D             | ✅            |
| MAXIMUM                 | ✅            |
| MÉCHANT                    | ✅            |
| MINIMUM                 | ✅            |
| Je                     | ✅            |
| NEG                     | ✅            |
| NOT_EQUAL               | ✅            |
| COUSSINET                     | ✅            |
| PADV2                   | ✅            |
| MIRROR_PAD              | ✅            |
| EMBALLER                    | ✅            |
| PRISONNIER DE GUERRE                     | ✅            |
| REDUCE_MAX              | ✅            |
| REDUCE_MIN              | ✅            |
| REDUCE_PROD             | ✅            |
| RELU                    | ✅            |
| PRELU                   | ✅            |
| RELU6                   | ✅            |
| REFAÇONNER                 | ✅            |
| RESIZE_BILINEAR         | ✅            |
| RESIZE_NEAREST_NEIGHBOR | ✅            |
| ROND                   | ✅            |
| RsQRT                   | ✅            |
| FORME                   | ✅            |
| SANS                     | ✅            |
| TRANCHE                   | ✅            |
| SOFTMAX                 | ✅            |
| SPACE_TO_BATCH_ND       | ✅            |
| PRESSER                 | ✅            |
| BATCH_TO_SPACE_ND       | ✅            |
| STRIDED_SLICE           | ✅            |
| SQRT                    | ✅            |
| CARRÉ                  | ✅            |
| SUB                     | ✅            |
| SOMME                     | ✅            |
| LOUCHE                    | ✅            |
| CARREAU                    | ✅            |
| TRANSPOSER               | ✅            |
| TRANSPOSE_CONV          | ✅            |
| QUANTIFICATION                | ✅            |
| FAKE_QUANT              | ✅            |
| DÉQUANTISER              | ✅            |
| RASSEMBLER                  | ✅            |
| GATHER_ND               | ✅            |
| ONE_HOT                 | ✅            |
| SQUARED_DIFFERENCE      | ✅            |
| LOG_SOFTMAX             | ✅            |
| FENDRE                   | ✅            |
| HARD_SWISH              | ✅            |

### 4.1.2 Opérateur onnx

| Opérateur              | Est pris en charge |
| --------------------- | ------------ |
| ABS                   | ✅            |
| Acos                  | ✅            |
| Acosh                 | ✅            |
| Et                   | ✅            |
| ArgMax                | ✅            |
| ArgMin                | ✅            |
| Salé                  | ✅            |
| Asinh                 | ✅            |
| Ajouter                   | ✅            |
| AveragePool (en anglais seulement)           | ✅            |
| BatchNormalisation    | ✅            |
| Jeter                  | ✅            |
| Ceil                  | ✅            |
| À                  | ✅            |
| Capture                  | ✅            |
| Concat                | ✅            |
| Constant              | ✅            |
| ConstantOfShape       | ✅            |
| Conv                  | ✅            |
| ConvTranspose         | ✅            |
| Corps                   | ✅            |
| Matraque                  | ✅            |
| Cumsum                | ✅            |
| ProfondeurToSpace          | ✅            |
| DequantizeLinear      | ✅            |
| Div                   | ✅            |
| Marginal               | ✅            |
| Vie                   | ✅            |
| Exp                   | ✅            |
| Développer                | ✅            |
| Égal                 | ✅            |
| Aplatir               | ✅            |
| Sol                 | ✅            |
| Rassembler                | ✅            |
| RassemblerND              | ✅            |
| Gemm                  | ✅            |
| GlobalAveragePool     | ✅            |
| GlobalMaxPool         | ✅            |
| Plus               | ✅            |
| GreaterOrEqual        | ✅            |
| Hardmax               | ✅            |
| HardSigmoid           | ✅            |
| HardSwish             | ✅            |
| Identité              | ✅            |
| InstanceNormalisation | ✅            |
| LpNormalisation       | ✅            |
| LeakyRelu             | ✅            |
| Moins                  | ✅            |
| LessOrEqual           | ✅            |
| Rapport                   | ✅            |
| LogSoftmax            | ✅            |
| LRN                   | ✅            |
| LSTM                  | ✅            |
| MatMul                | ✅            |
| MaxPool               | ✅            |
| Max                   | ✅            |
| Min                   | ✅            |
| Je                   | ✅            |
| Neg                   | ✅            |
| Non                   | ✅            |
| OneHot                | ✅            |
| Coussinet                   | ✅            |
| Prisonnier de guerre                   | ✅            |
| PRelu                 | ✅            |
| QuantizeLinear        | ✅            |
| RandomNormal          | ✅            |
| RandomNormalLike      | ✅            |
| RandomUniform         | ✅            |
| RandomUniformLike     | ✅            |
| RéduireL1              | ✅            |
| RéduireL2              | ✅            |
| ReduceLogSum          | ✅            |
| ReduceLogSumExp       | ✅            |
| ReduceMax             | ✅            |
| RéduireMoisan            | ✅            |
| Réduiremin             | ✅            |
| ReduceProd            | ✅            |
| RéduireSoum             | ✅            |
| ReduceSumSquare       | ✅            |
| Relu                  | ✅            |
| Refaçonner               | ✅            |
| Redimensionner                | ✅            |
| ReverseSéquence       | ✅            |
| RoiAlign              | ✅            |
| Rond                 | ✅            |
| Village                  | ✅            |
| Forme                 | ✅            |
| Signe                  | ✅            |
| Sans                   | ✅            |
| Naissance                  | ✅            |
| Sigmoïde               | ✅            |
| Taille                  | ✅            |
| Tranche                 | ✅            |
| Softmax               | ✅            |
| Softplus              | ✅            |
| Softsign (enseigne logicielle)              | ✅            |
| SpaceToDepth          | ✅            |
| Fendre                 | ✅            |
| Sqrt                  | ✅            |
| Presser               | ✅            |
| Sub                   | ✅            |
| Somme                   | ✅            |
| Louche                  | ✅            |
| Carreau                  | ✅            |
| TopK                  | ✅            |
| Transposer             | ✅            |
| Trilu                 | ✅            |
| Suréchantillonnage              | ✅            |
| Annuler la compression             | ✅            |
| Où                 | ✅            |

### 4.1.3 Opérateur de café

| Opérateur              | Est pris en charge |
| --------------------- | ------------ |
| Entrée                 | ✅            |
| Concat                | ✅            |
| Convolution           | ✅            |
| Eltwise               | ✅            |
| Reprises               | ✅            |
| relu                  | ✅            |
| Refaçonner               | ✅            |
| Tranche                 | ✅            |
| Softmax               | ✅            |
| Fendre                 | ✅            |
| ContinuationIndicateur | ✅            |
| Mutualisation               | ✅            |
| BatchNorm             | ✅            |
| Écaille                 | ✅            |
| Inverse               | ✅            |
| LSTM                  | ✅            |
| InnerProduct (produit intérieur)          | ✅            |

## 4.2 Compiler les API du modèle

À l'heure actuelle, l'API du modèle de compilation prend en charge les frameworks de deep learning tels que tflite/onnx/caffe.

### 4.2.1 CompileOptions

**Description de la fonctionnalité**

CompileOptions, classe pour la configuration des options de compilation nncase

**Définition de classe**

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

Chaque propriété est décrite ci-dessous

| Nom de la propriété         | type   | Oui ou Non | description                                                         |
| ---------------- | ------ | -------- | ------------------------------------------------------------ |
| cible           | corde | être       | Spécifiez la cible de compilation, telle que 'k210', 'k510'                               |
| quant_type       | corde | non       | Spécifiez le type de quantification des données, tel que 'uint8', 'int8'                          |
| w_quant_type     | corde | non       | Spécifiez le type de quantification de poids, tel que 'uint8', 'int8', par défaut 'uint8'           |
| use_mse_quant_w  | Bool   | non       | Spécifie s'il faut utiliser l'algorithme d'erreur moyenne-carrée (MSE) pour optimiser les paramètres de quantification lors de la quantification des pondérations |
| split_w_to_act   | Bool   | non       | Spécifie s'il faut équilibrer les données de poids partiel dans les données actives                       |
| prétraitement       | Bool   | non       | Que le prétraitement soit activé ou non, la valeur par défaut est False                                  |
| swapRB           | Bool   | non       | S'il faut échanger des données d'entrée RVB entre les canaux rouge et bleu (RVB - > BGR ou BGR->RGB), la valeur par défaut est False |
| méchant             | liste   | non       | Le prétraitement normalise la moyenne des paramètres, qui est par défaut la suivante :[0, 0, 0]                        |
| MST              | liste   | non       | Le prétraitement normalise la variance du paramètre, qui est définie par défaut sur[1, 1, 1]                        |
| input_range      | liste   | non       | Plage de nombres à virgule flottante après déquantisation des données d'entrée, qui est par défaut la suivante :[0, 1]               |
| output_range     | liste   | non       | Plage de nombres à virgule flottante avant la sortie des données à virgule fixe, qui est par défaut vide                     |
| input_shape      | liste   | non       | Spécifiez la forme des données d'entrée, la disposition du input_shape doit être cohérente avec la disposition d'entrée, et la input_shape des données d'entrée est incompatible avec la forme d'entrée du modèle, et l'opération bitbox (redimensionnement/pad, etc.) sera effectuée. |
| letterbox_value  | flotter  | non       | Spécifie la valeur de remplissage de la zone de prétraitement fetchbox                                  |
| input_type       | corde | non       | Spécifie le type de données d'entrée, par défaut 'float32'                          |
| output_type      | corde | non       | Spécifie le type de données de sortie, telles que 'float32', 'uint8' (uniquement pour la quantification spécifiée), par défaut 'float32' |
| input_layout     | corde | non       | Spécifiez la disposition des données d'entrée, telles que 'NCHW', 'NHWC'. Si la disposition des données d'entrée est différente du modèle lui-même, nncase insère la transposition pour la conversion |
| output_layout    | corde | non       | Spécifiez les données de sortie pour la mise en page, telles que 'NCHW', 'NHWC'. Si la disposition des données de sortie est différente du modèle lui-même, nncase insérera transpose pour la conversion |
| model_layout     | corde | non       | Spécifiez la disposition du modèle, qui est vide par défaut, et spécifie quand la disposition du modèle tflite est 'NCHW' et les modèles Onnx et Caffe sont 'NHWC' |
| is_fpga          | Bool   | non       | Spécifie si kmodel est utilisé pour les FPGA, qui a la valeur par défaut False                          |
| dump_ir          | Bool   | non       | Spécifie si l'IR de vidage, par défaut, est False                                 |
| dump_asm         | Bool   | non       | Spécifie si le fichier d'assembly asm de vidage, qui a par défaut la valeur False                        |
| dump_quant_error | Bool   | non       | Spécifie si le vidage quantifie l'erreur de modèle avant et après                               |
| dump_dir         | corde | non       | Après avoir spécifié le dump_ir et d'autres commutateurs précédemment, vous spécifiez ici le répertoire de vidage, qui par défaut est une chaîne vide  |
| benchmark_only   | Bool   | non       | Spécifie si kmodel est utilisé uniquement pour le benchmark, dont la valeur par défaut est False                   |

> 1. La plage d'entrée est la plage de nombres à virgule flottante, c'est-à-dire que si le type de données d'entrée est uint8, la plage d'entrée est la plage après déquantisation en virgule flottante (ne peut pas être 0 ~ 1), qui peut être spécifiée librement.
> 2. input_shape doivent être spécifiés conformément à la input_layout, [1，224，224，3]par exemple, si le input_layout est NCHW, le input_shape doit être spécifié comme[1,3,224,224] suit: input_layout'est NHWC, le input_shape doit être spécifié comme[1,224,224,3] suit:
> 3. mean et std sont des paramètres permettant de normaliser les nombres à virgule flottante, que l'utilisateur est libre de spécifier ;
> 4. Lorsque vous utilisez la fonction boîte aux lettres, vous devez limiter la taille d'entrée à 1,5 Mo et la taille d'un seul canal est inférieure à 0,75 Mo;
>
> Par exemple:
>
> 1. Le type de données d'entrée est défini sur uint8, input_range défini sur[0,255], le rôle de la déquantisation est uniquement de convertir le type, convertir les données de uint8 en float32, et les paramètres moyen et std peuvent toujours être spécifiés en fonction des données de 0 ~ 255
> 2. Le type de données d'entrée est défini sur uint8, input_range défini sur[0,1], le nombre à virgule fixe est déquantisé en un nombre à [0,1]virgule flottante dans la plage, et la moyenne et la MST doivent être spécifiées en fonction de la nouvelle plage de nombres à virgule flottante.

Le processus de prétraitement est le suivant (les nœuds verts de la figure sont facultatifs) :

![prétraitement.png](https://i.loli.net/2021/11/08/fhBLsozUTCbt4dp.png)

**Exemple de code**

Instancier CompileOptions, configurer les valeurs de chaque propriété

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

**Description de la fonctionnalité**

ImportOptions, classe pour configurer les options d'importation nncase

**Définition de classe**

```python
py::class_<import_options>(m, "ImportOptions")
    .def(py::init())
    .def_readwrite("output_arrays", &import_options::output_arrays);
```

Chaque propriété est décrite ci-dessous

| Nom de la propriété      | type   | Oui ou Non | description     |
| ------------- | ------ | -------- | -------- |
| output_arrays | corde | non       | Nom de sortie |

**Exemple de code**

Instancier ImageOptions, configurer les valeurs de chaque propriété

```python
# import_options
import_options = nncase.ImportOptions()
import_options.output_arrays = 'output' # Your output node name
```

### 4.2.3 PTQTensorOptions

**Description de la fonctionnalité**

Classe PTQTensorOptions pour la configuration des options PTQ nncase

**Définition de classe**

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

Chaque propriété est décrite ci-dessous

| Nom du champ         | type   | Oui ou Non | description                                                                                  |
| ---------------- | ------ | -------- | ------------------------------------------------------------------------------------- |
| calibrate_method | corde | non       | Méthode d'étalonnage , prend en charge 'no_clip', 'l2', 'kld_m0', 'kld_m1', 'kld_m2', 'cdf', la valeur par défaut est 'no_clip' |
| samples_count    | Int    | non       | Le nombre d'échantillons                                                                              |

#### set_tensor_data()

**Description de la fonctionnalité**

Définir les données de correction

**Définition de l'interface**

```python
set_tensor_data(calib_data)
```

**Paramètres d'entrée**

| Nom du paramètre   | type   | Oui ou Non | description     |
| ---------- | ------ | -------- | -------- |
| calib_data | octet[] | être       | Corriger les données |

**La valeur renvoyée**

N/A

**Exemple de code**

```python
# ptq_options
ptq_options = nncase.PTQTensorOptions()
ptq_options.samples_count = cfg.generate_calibs.batch_size
ptq_options.set_tensor_data(np.asarray([sample['data'] for sample in self.calibs]).tobytes())
```

### 4.2.4 Compilateur

**Description de la fonctionnalité**

Classe de compilateur pour la compilation de modèles de réseau neuronal

**Définition de classe**

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

**Exemple de code**

```python
compiler = nncase.Compiler(compile_options)
```

#### import_tflite()

**Description de la fonctionnalité**

Importer le modèle tflite

**Définition de l'interface**

```python
import_tflite(model_content, import_options)
```

**Paramètres d'entrée**

| Nom du paramètre       | type          | Oui ou Non | description           |
| -------------- | ------------- | -------- | -------------- |
| model_content  | octet[]        | être       | Lire le contenu du modèle |
| import_options | ImportOptions | être       | Options d'importation       |

**La valeur renvoyée**

N/A

**Exemple de code**

```python
model_content = read_model_file(model)
compiler.import_tflite(model_content, import_options)
```

#### import_onnx()

**Description de la fonctionnalité**

Importer le modèle onnx

**Définition de l'interface**

```python
import_onnx(model_content, import_options)
```

**Paramètres d'entrée**

| Nom du paramètre       | type          | Oui ou Non | description           |
| -------------- | ------------- | -------- | -------------- |
| model_content  | octet[]        | être       | Lire le contenu du modèle |
| import_options | ImportOptions | être       | Options d'importation       |

**La valeur renvoyée**

N/A

**Exemple de code**

```python
model_content = read_model_file(model)
compiler.import_onnx(model_content, import_options)
```

#### import_caffe()

**Description de la fonctionnalité**

Importer le modèle de café

> Les utilisateurs doivent compiler/installer caffe sur la machine locale.

**Définition de l'interface**

```python
import_caffe(caffemodel, prototxt)
```

**Paramètres d'entrée**

| Nom du paramètre   | type   | Oui ou Non | description                 |
| ---------- | ------ | -------- | -------------------- |
| caffemodel | octet[] | être       | Lire le contenu du caffemodel |
| prototxt   | octet[] | être       | Lire le contenu prototxt   |

**La valeur renvoyée**

N/A

**Exemple de code**

```python
# import
caffemodel = read_model_file('test.caffemodel')
prototxt = read_model_file('test.prototxt')
compiler.import_caffe(caffemodel, prototxt)
```

#### use_ptq()

**Description de la fonctionnalité**

Définir les options de configuration PTQ

**Définition de l'interface**

```python
use_ptq(ptq_options)
```

**Paramètres d'entrée**

| Nom du paramètre    | type             | Oui ou Non | description        |
| ----------- | ---------------- | -------- | ----------- |
| ptq_options | PTQTensorOptions | être       | Options de configuration PTQ |

**La valeur renvoyée**

N/A

**Exemple de code**

```python
compiler.use_ptq(ptq_options)
```

#### compile()

**Description de la fonctionnalité**

Compiler le modèle de réseau neuronal

**Définition de l'interface**

```python
compile()
```

**Paramètres d'entrée**

N/A

**La valeur renvoyée**

N/A

**Exemple de code**

```python
compiler.compile()
```

#### gencode_tobytes()

**Description de la fonctionnalité**

Génère un flux d'octets de code

**Définition de l'interface**

```python
gencode_tobytes()
```

**Paramètres d'entrée**

N/A

**La valeur renvoyée**

Octets[]

**Exemple de code**

```python
kmodel = compiler.gencode_tobytes()
with open(os.path.join(infer_dir, 'test.kmodel'), 'wb') as f:
    f.write(kmodel)
```

## 4.3 Compiler l'exemple de modèle

L'exemple suivant utilise le modèle et le script de compilation python

- Le modèle se trouve dans le sous-répertoire /path/to/nncase_sdk/examples/models/subdirectory
- Le script de compilation python se trouve dans le sous-répertoire /path/to/nncase_sdk/examples/scripts

### 4.3.1 Compiler le modèle float32 tflite

- Mobilenetv2_tflite_fp32_image.py script est le suivant

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

- Exécutez la commande suivante pour compiler le modèle tflite de mobiletv2, cible k510

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_tflite_fp32_image.py --target k510 --model models/mobilenet_v2_1.0_224.tflite
```

### 4.3.2 Compiler le modèle onnx float32

- Pour les modèles onnx, il est recommandé de simplifier l'utilisation d'[ONNX Simplifier](https://github.com/daquexian/onnx-simplifier)avant de compiler avec nncase
- mobilenetv2_onnx_fp32_image.py script est le suivant

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

- Exécutez la commande suivante pour compiler le modèle onnx de mobiletv2, cible k510

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_onnx_fp32_image.py --target k510 --model models/mobilenetv2-7.onnx
```

### 4.3.3 Compiler le modèle de café float32

- L'ensemble de roues de café est[tiré de](https://github.com/kendryte/caffe/releases)kendryte caffe
- conv2d_caffe_fp32.py script est le suivant

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

- Exécutez la commande suivante pour compiler le modèle caffe de conv2d, avec la cible k510

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/conv2d_caffe_fp32.py --target k510 --caffemodel models/test.caffemodel --prototxt models/test.prototxt
```

### 4.3.4 Compiler et ajouter un modèle onnx float32 pré-processus

- Pour les modèles onnx, il est recommandé de simplifier l'utilisation d'[ONNX Simplifier](https://github.com/daquexian/onnx-simplifier)avant de compiler avec nncase
- Mobilenetv2_onnx_fp32_preprocess.py script est le suivant

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

- Exécutez la commande suivante pour compiler le modèle onnx de mobiletv2 avec la cible k510

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_onnx_fp32_preprocess.py --target k510 --model models/mobilenetv2-7.onnx
```

### 4.3.5 Compiler le modèle tflite de quantification uint8

- Mobilenetv2_tflite_uint8_image.py script est le suivant

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

- Exécutez la commande suivante pour compiler le modèle tflite de uint8 quantized mobiletv2, target k510

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_tflite_uint8_image.py --target k510 --model models/mobilenet_v2_1.0_224.tflite
```

## 4.4 API du modèle d'inférence

En plus des points d'accès du modèle compilé, nncase fournit également les API du modèle d'inférence, qui peuvent être déduites sur le PC avant la compilation du kmodel, qui est utilisé pour vérifier si les résultats d'inférence nncase et les résultats d'exécution de l'infrastructure de deep learning correspondante sont cohérents.

### 4.4.1 MemoryRange

**Description de la fonctionnalité**

Classe MemoryRange, utilisée pour représenter une plage de mémoire

**Définition de classe**

```python
py::class_<memory_range>(m, "MemoryRange")
    .def_readwrite("location", &memory_range::memory_location)
    .def_property(
        "dtype", [](const memory_range &range) { return to_dtype(range.datatype); },
        [](memory_range &range, py::object dtype) { range.datatype = from_dtype(py::dtype::from_args(dtype)); })
    .def_readwrite("start", &memory_range::start)
    .def_readwrite("size", &memory_range::size);
```

Chaque propriété est décrite ci-dessous

| Nom de la propriété | type           | Oui ou Non | description                                                                       |
| -------- | -------------- | -------- | -------------------------------------------------------------------------- |
| emplacement | Int            | non       | Position de la mémoire, 0 pour l'entrée, 1 pour la sortie, 2 pour rdata, 3 pour les données, 4 pour shared_data |
| dtype    | Type de données Python | non       | type de données                                                                   |
| commencer    | Int            | non       | Adresse de démarrage de la mémoire                                                               |
| taille     | Int            | non       | Taille de la mémoire                                                                   |

**Exemple de code**

Instancier MemoryRange

```python
mr = nncase.MemoryRange()
```

### 4.4.2 RuntimeTensor

**Description de la fonctionnalité**

La classe RuntimeTensor, qui représente le tenseur d'exécution

**Définition de classe**

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

Chaque propriété est décrite ci-dessous

| Nom de la propriété | type | Oui ou Non | description             |
| -------- | ---- | -------- | ---------------- |
| dtype    | Int  | non       | Type de données du tenseur |
| forme    | liste | non       | La forme du tenseur     |

#### from_numpy()

**Description de la fonctionnalité**

Construire l'objet RuntimeTensor à partir de numpy.ndarray

**Définition de l'interface**

```python
from_numpy(py::array arr)
```

**Paramètres d'entrée**

| Nom du paramètre | type          | Oui ou Non | description              |
| -------- | ------------- | -------- | ----------------- |
| Arr      | numpy.ndarray | être       | Objet numpy.ndarray |

**La valeur renvoyée**

RuntimeTensor

**Exemple de code**

```python
tensor = nncase.RuntimeTensor.from_numpy(self.inputs[i]['data'])
```

#### copy_to()

**Description de la fonctionnalité**

Copier le tenseur d'exécution

**Définition de l'interface**

```python
copy_to(RuntimeTensor to)
```

**Paramètres d'entrée**

| Nom du paramètre | type          | Oui ou Non | description              |
| -------- | ------------- | -------- | ----------------- |
| À       | RuntimeTensor | être       | Objet RuntimeTensor |

**La valeur renvoyée**

N/A

**Exemple de code**

```python
sim.get_output_tensor(i).copy_to(to)
```

#### to_numpy()

**Description de la fonctionnalité**

Convertir RuntimeTensor en objet numpy.ndarray

**Définition de l'interface**

```python
to_numpy()
```

**Paramètres d'entrée**

N/A

**La valeur renvoyée**

Objet numpy.ndarray

**Exemple de code**

```python
arr = sim.get_output_tensor(i).to_numpy()
```

### 4.4.3 Simulateur

**Description de la fonctionnalité**

Classe de simulateur pour inférence kmodel sur PC

**Définition de classe**

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

Chaque propriété est décrite ci-dessous

| Nom de la propriété     | type | Oui ou Non | description     |
| ------------ | ---- | -------- | -------- |
| inputs_size  | Int  | non       | Entrez le nombre de |
| outputs_size | Int  | non       | Le nombre de sorties |

**Exemple de code**

Instancier le simulateur

```python
sim = nncase.Simulator()
```

#### load_model()

**Description de la fonctionnalité**

Charger le kmodel

**Définition de l'interface**

```python
load_model(model_content)
```

**Paramètres d'entrée**

| Nom du paramètre      | type   | Oui ou Non | description         |
| ------------- | ------ | -------- | ------------ |
| model_content | octet[] | être       | Flux d'octets Kmodel |

**La valeur renvoyée**

N/A

**Exemple de code**

```python
sim.load_model(kmodel)
```

#### get_input_desc()

**Description de la fonctionnalité**

Obtient la description de l'entrée pour l'index spécifié

**Définition de l'interface**

```python
get_input_desc(index)
```

**Paramètres d'entrée**

| Nom du paramètre | type | Oui ou Non | description       |
| -------- | ---- | -------- | ---------- |
| index    | Int  | être       | L'index de l'entrée |

**La valeur renvoyée**

MemoryRange (Plage de mémoire)

**Exemple de code**

```python
input_desc_0 = sim.get_input_desc(0)
```

#### get_output_desc()

**Description de la fonctionnalité**

Obtient la description de la sortie de l'index spécifié

**Définition de l'interface**

```python
get_output_desc(index)
```

**Paramètres d'entrée**

| Nom du paramètre | type | Oui ou Non | description       |
| -------- | ---- | -------- | ---------- |
| index    | Int  | être       | L'indice de la sortie |

**La valeur renvoyée**

MemoryRange (Plage de mémoire)

**Exemple de code**

```python
output_desc_0 = sim.get_output_desc(0)
```

#### get_input_tensor()

**Description de la fonctionnalité**

Obtient le RuntimeTensor pour l'entrée de l'index spécifié

**Définition de l'interface**

```python
get_input_tensor(index)
```

**Paramètres d'entrée**

| Nom du paramètre | type | Oui ou Non | description             |
| -------- | ---- | -------- | ---------------- |
| index    | Int  | être       | Entrez l'index du tenseur |

**La valeur renvoyée**

RuntimeTensor

**Exemple de code**

```python
input_tensor_0 = sim.get_input_tensor(0)
```

#### set_input_tensor()

**Description de la fonctionnalité**

Définit le tenseur d'exécution pour l'entrée de l'index spécifié

**Définition de l'interface**

```python
set_input_tensor(index, tensor)
```

**Paramètres d'entrée**

| Nom du paramètre | type          | Oui ou Non | description                    |
| -------- | ------------- | -------- | ----------------------- |
| index    | Int           | être       | Entrez l'index de RuntimeTensor |
| tenseur   | RuntimeTensor | être       | Entrez RuntimeTensor       |

**La valeur renvoyée**

N/A

**Exemple de code**

```python
sim.set_input_tensor(0, nncase.RuntimeTensor.from_numpy(self.inputs[0]['data']))
```

#### get_output_tensor()

**Description de la fonctionnalité**

Obtient le tenseur d'exécution pour la sortie de l'index spécifié

**Définition de l'interface**

```python
get_output_tensor(index)
```

**Paramètres d'entrée**

| Nom du paramètre | type | Oui ou Non | description                    |
| -------- | ---- | -------- | ----------------------- |
| index    | Int  | être       | Génère l'index du RuntimeTensor |

**La valeur renvoyée**

RuntimeTensor

**Exemple de code**

```python
output_arr_0 = sim.get_output_tensor(0).to_numpy()
```

#### set_output_tensor()

**Description de la fonctionnalité**

Définit le RuntimeTensor pour la sortie de l'index spécifié

**Définition de l'interface**

```python
set_output_tensor(index, tensor)
```

**Paramètres d'entrée**

| Nom du paramètre | type          | Oui ou Non | description                    |
| -------- | ------------- | -------- | ----------------------- |
| index    | Int           | être       | Génère l'index du RuntimeTensor |
| tenseur   | RuntimeTensor | être       | Tenseur d'exécution de sortie       |

**La valeur renvoyée**

N/A

**Exemple de code**

```python
sim.set_output_tensor(0, tensor)
```

#### exécuter()

**Description de la fonctionnalité**

Exécuter l'inférence kmodel

**Définition de l'interface**

```python
run()
```

**Paramètres d'entrée**

N/A

**La valeur renvoyée**

N/A

**Exemple de code**

```python
sim.run()
```

## 4.5 Exemple de modèle d'inférence

**Prérequis :**mobilenetv2_onnx_fp32_image.py script a été compilé avec le modèle mobiletv2-7.onnx

mobilenetv2_onnx_simu.py se trouve dans le sous-répertoire /path/to/nncase_sdk/examples/scripts, qui se lit comme suit :

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

Exécuter le script d'inférence

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_onnx_simu.py --model_file models/mobilenetv2-7.onnx --kmodel_file tmp/mobilenetv2_onnx_fp32_image/test.kmodel --input_file mobilenetv2_onnx_fp32_image/data/input_0_0.bin
```

La comparaison des résultats du simulateur nncase et de l'inférence du processeur est la suivante

```shell
... ...
output 0 cosine similarity : 0.9992437958717346
```

# Bibliothèque d'exécution 5 nncase

## 5.1 Introduction au runtime nncase

nncase runtime est utilisé pour charger kmodel sur des périphériques d'IA / définir des données d'entrée / effectuer des calculs KPU / obtenir des données de sortie, etc.

Actuellement, seule**la version C++**des API, les fichiers d'en-tête associés et les bibliothèques statiques sont disponibles dans le répertoire nncase sdk/riscv64

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

## 5.2 API d'exécution

### 5.2.1 classe runtime_tensor

Tenseur utilisé pour stocker les données d'entrée/sortie du modèle

#### hrt::create()

**Description de la fonctionnalité**

Créer un runtime_tensor

**Définition de l'interface**

```C++
(1) NNCASE_API result<runtime_tensor> create(datatype_t datatype, runtime_shape_t shape, memory_pool_t pool = pool_cpu_only, uintptr_t physical_address = 0) noexcept;

(2) NNCASE_API result<runtime_tensor> create(datatype_t datatype, runtime_shape_t shape, gsl::span<gsl::byte> data, bool copy, memory_pool_t pool = pool_cpu_only, uintptr_t physical_address = 0) noexcept;
```

**Paramètres d'entrée**

| Nom du paramètre         | type                  | Oui ou Non | description                              |
| ---------------- | --------------------- | -------- | --------------------------------- |
| Datatype         | datatype_t            | être       | Type de données, tel que dt_float32            |
| forme            | runtime_shape_t       | être       | La forme du tenseur                      |
| données             | gsl::span\<gsl::byte> | être       | Tampon de données d'état utilisateur                  |
| copier             | Bool                  | être       | S'il faut copier                          |
| mare             | memory_pool_t         | non       | Type de pool de mémoire, la valeur par défaut est pool_cpu_only |
| physical_address | uintptr_t             | non       | Adresse physique, la valeur par défaut est 0               |

**La valeur renvoyée**

résultat<runtime_tensor>

Exemple de code

```c++
// create input
auto in_shape = interp.input_shape(0);
auto input_tensor = host_runtime_tensor::create(dt_float32, in_shape,
                                                {(gsl::byte *)mat.data, mat.cols * mat.rows * mat.elemSize()},
                                                true, hrt::pool_shared).expect("cannot create input tensor");
```

### 5.2.2 Interprète de classe

L'interpréteur est une instance en cours d'exécution du runtime nncase, qui fournit des fonctions fonctionnelles de base telles que load_model()/run()/input_tensor()/output_tensor().

#### load_model()

**Description de la fonctionnalité**

Charger le modèle kmodel

**Définition de l'interface**

```C++
 NNCASE_NODISCARD result<void> load_model(gsl::span<const gsl::byte> buffer) noexcept;
```

**Paramètres d'entrée**

| Nom du paramètre | type                            | Oui ou Non | description          |
| -------- | ------------------------------- | -------- | ------------- |
| tampon   | gsl::span `<const gsl::byte>` | être       | Tampon kmodel |

**La valeur renvoyée**

résultat `<void>`

**Exemple de code**

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

**Description de la fonctionnalité**

Obtient le nombre d'entrées de modèle

**Définition de l'interface**

```C++
size_t inputs_size() const noexcept;
```

**Paramètres d'entrée**

N/A

**La valeur renvoyée**

size_t

**Exemple de code**

```c++
auto inputs_size = interp.inputs_size();
```

#### outputs_size()

**Description de la fonctionnalité**

Obtient le nombre de sorties de modèle

**Définition de l'interface**

```C++
size_t outputs_size() const noexcept;
```

**Paramètres d'entrée**

N/A

**La valeur renvoyée**

size_t

**Exemple de code**

```c++
auto outputs_size = interp.outputs_size();
```

#### input_shape()

**Description de la fonctionnalité**

Obtient la forme de l'entrée spécifiée dans le modèle

**Définition de l'interface**

```C++
const runtime_shape_t &input_shape(size_t index) const noexcept;
```

**Paramètres d'entrée**

| Nom du paramètre | type   | Oui ou Non | description       |
| -------- | ------ | -------- | ---------- |
| index    | size_t | être       | L'index de l'entrée |

**La valeur renvoyée**

runtime_shape_t

**Exemple de code**

```c++
auto in_shape = interp.input_shape(0);
```

#### output_shape()

**Description de la fonctionnalité**

Obtient la forme de la sortie spécifiée du modèle

**Définition de l'interface**

```C++
const runtime_shape_t &output_shape(size_t index) const noexcept;
```

**Paramètres d'entrée**

| Nom du paramètre | type   | Oui ou Non | description       |
| -------- | ------ | -------- | ---------- |
| index    | size_t | être       | L'indice de la sortie |

**La valeur renvoyée**

runtime_shape_t

**Exemple de code**

```c++
auto out_shape = interp.output_shape(0);
```

#### input_tensor()

**Description de la fonctionnalité**

Obtient/définit le tenseur d'entrée pour l'index spécifié

**Définition de l'interface**

```C++
(1) result<runtime_tensor> input_tensor(size_t index) noexcept;
(2) result<void> input_tensor(size_t index, runtime_tensor tensor) noexcept;
```

**Paramètres d'entrée**

| Nom du paramètre | type           | Oui ou Non | description                     |
| -------- | -------------- | -------- | ------------------------ |
| index    | size_t         | être       | Tampon kmodel            |
| tenseur   | runtime_tensor | être       | Entrez le tenseur d'exécution correspondant |

**La valeur renvoyée**

(1) Renvoie les résultats<runtime_tensor>

(2) Renvoie les résultats `<void>`

**Exemple de code**

```c++
// set input
interp.input_tensor(0, input_tensor).expect("cannot set input tensor");
```

#### output_tensor()

**Description de la fonctionnalité**

Obtient/définit le tenseur sortant pour l'index spécifié

**Définition de l'interface**

```C++
(1) result<runtime_tensor> output_tensor(size_t index) noexcept;
(2) result<void> output_tensor(size_t index, runtime_tensor tensor) noexcept;
```

**Paramètres d'entrée**

| Nom du paramètre | type           | Oui ou Non | description                     |
| -------- | -------------- | -------- | ------------------------ |
| index    | size_t         | être       |                          |
| tenseur   | runtime_tensor | être       | Entrez le tenseur d'exécution correspondant |

**La valeur renvoyée**

(1) Renvoie les résultats<runtime_tensor>

(2) Renvoie les résultats `<void>`

**Exemple de code**

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

#### exécuter()

**Description de la fonctionnalité**

Effectuer des calculs kPU

**Définition de l'interface**

```C++
result<void> run() noexcept;
```

**Paramètres d'entrée**

N/A

**La valeur renvoyée**

résultat `<void>`

**Exemple de code**

```c++
// run
interp.run().expect("error occurred in running model");
```

## 5.3 Exemple d'exécution

L'exemple de code se trouve dans /path/to/nncase_sdk/examples/mobilenetv2_onnx_fp32_image

**Condition de préfixe**

- mobilenetv2_onnx_fp32_image.py script a compilé le modèle mobiletv2-7.onnx
- Étant donné que l'exemple repose sur la bibliothèque OpenCV, vous devez spécifier le chemin d'accès à OpenCV dans la .txt CMakeLists de l'exemple.

**Applications de compilation croisée**

```shell
cd /path/to/nncase_sdk/examples
./build.sh
```

Enfin, générez le mobilenetv2_onnx_fp32_image dans le répertoire out/bin

**Le k510 EVB fonctionne sur la carte**

Copiez les fichiers suivants sur la carte k510 EVB

| lime                        | remarque                                                         |
| --------------------------- | ------------------------------------------------------------ |
| mobilenetv2_onnx_fp32_image | Des exemples de compilation croisée sont générés                                         |
| test.kmodel                 | Utiliser mobilenetv2_onnx_fp32_image.py compiler la version mobiletv2-7.onnx |
| .png et labels_1000.txt pour chats    | Situé sous le sous-répertoire /path/to/nncase_sdk/examples/mobilenetv2_onnx_fp32_image/data/ |

```bash
$ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mnt/zhangyang/nncase_check/lib/gomp:/mnt/zhangyang/nncase_check/lib/opencv
$ ./mobilenetv2_onnx_fp32_image test.kmodel cat.png labels_1000.txt
case ./mobilenetv2_onnx_fp32_image build at Mar  1 2022 16:31:29
interp.run() duration: 12.6642 ms
image classification result: tiger cat(9.25)
```

# 6 Bibliothèques de programmation fonctionnelles (prise en charge du runtime)

## 6.1 Introduction à Functional

nncase Functional est utilisé pour améliorer la facilité d'utilisation lorsque les utilisateurs utilisent des modèles pré- et post-processus

Actuellement, seule la version C++ des API est disponible et les fichiers d'en-tête et les bibliothèques associés se trouvent dans le répertoire riscv64 du sdk nncase.

## 6.2 API

### 6.2.1 carré

**Description de la fonctionnalité**

Calculer le carré, actuellement support d'entrée uint8 / int8, la sortie est également uint8 / int8, notez que l'entrée est à virgule fixe et la sortie est à virgule flottante besoin de définir les paramètres de quantification.

**Définition de l'interface**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`square`](#ops_8h_1adff2f60c7c045a9840519eab2c04d127)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Paramètres d'entrée**

| Nom du paramètre  | type           | Oui ou Non | description                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | être       | entrée                |
| `dtype` | datatype_t     | être       | Type de données du tenseur de sortie |

**La valeur renvoyée**

`result<runtime_tensor>`

**Exemple de code**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto squared = F::square(input, output_type).unwrap_or_throw();
```

### 6.2.2 sqrt

**Description de la fonctionnalité**

Calculer la valeur du nombre racine, actuellement prendre en charge l'entrée uint8 / int8, la sortie est également uint8 / int8, notez que l'entrée est à point fixe et la sortie est à virgule flottante doit définir les paramètres de quantification.

**Définition de l'interface**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`sqrt`](#ops_8h_1a53f8dde3dd4e27058b5dc743eb5dd076)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Paramètres d'entrée**

| Nom du paramètre  | type           | Oui ou Non | description                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | être       | entrée                |
| `dtype` | datatype_t     | être       | Type de données du tenseur de sortie |

**La valeur renvoyée**

`result<runtime_tensor>`

**Exemple de code**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::sqrt(input, output_type).unwrap_or_throw();
```

### 6.2.3 journal

**Description de la fonctionnalité**

Calculez la valeur du journal, le nombre négatif d'entrée sera converti en Nan, actuellement le support d'entrée uint8 / int8, la sortie est également uint8 / int8, notez que l'entrée est à point fixe et la sortie est à virgule flottante doit définir le paramètre de quantification.

**Définition de l'interface**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`log`](#ops_8h_1a91df53276c3f1511427d4ac1a0140b71)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Paramètres d'entrée**

| Nom du paramètre  | type           | Oui ou Non | description                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | être       | entrée                |
| `dtype` | datatype_t     | être       | Type de données du tenseur de sortie |

**La valeur renvoyée**

`result<runtime_tensor>`

**Exemple de code**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::log(input, output_type).unwrap_or_throw();
```

### 6.2.4 exp

**Description de la fonctionnalité**

Calculer la valeur exp, actuellement supporte l'entrée uint8 / int8, la sortie est également uint8 / int8, notez que l'entrée est à point fixe et la sortie est à virgule flottante besoin de définir les paramètres de quantification.

**Définition de l'interface**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`exp`](#ops_8h_1a2c6ce457805a5ba515fa7454fb4aede0)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Paramètres d'entrée**

| Nom du paramètre  | type           | Oui ou Non | description                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | être       | entrée                |
| `dtype` | datatype_t     | être       | Type de données du tenseur de sortie |

**La valeur renvoyée**

`result<runtime_tensor>`

**Exemple de code**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::exp(input, output_type).unwrap_or_throw();
```

### 6.2.5 sans

**Description de la fonctionnalité**

Pour calculer la valeur sin, l'entrée uint8/int8 est actuellement prise en charge et la sortie est également uint8/int8, notez que les paramètres de quantification doivent être définis lorsque l'entrée est à virgule fixe et que la sortie est à virgule flottante.

**Définition de l'interface**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`sin`](#ops_8h_1a9605b2b0dc9a6892ce878bda14586890)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Paramètres d'entrée**

| Nom du paramètre  | type           | Oui ou Non | description                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | être       | entrée                |
| `dtype` | datatype_t     | être       | Type de données du tenseur de sortie |

**La valeur renvoyée**

`result<runtime_tensor>`

**Exemples de code**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::sin(input, output_type).unwrap_or_throw();
```

### 6.2.6 Organisme

**Description de la fonctionnalité**

Calculer la valeur cos, actuellement supporte l'entrée uint8 / int8, la sortie est également uint8 / int8, notez que l'entrée est à point fixe et la sortie est à virgule flottante doit définir le paramètre de quantification.

**Définition de l'interface**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`cos`](#ops_8h_1a71d36c13c82f4c411f24d030cf333249)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Paramètres d'entrée**

| Nom du paramètre  | type           | Oui ou Non | description                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | être       | entrée                |
| `dtype` | datatype_t     | être       | Type de données du tenseur de sortie |

**La valeur renvoyée**

`result<runtime_tensor>`

**Exemples de code**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::cos(input, output_type).unwrap_or_throw();
```

### 6.2.7 ronde

**Description de la fonctionnalité**

Pour calculer la valeur d'arrondi, l'entrée uint8/int8 est actuellement prise en charge et la sortie est également uint8/int8, notez que le paramètre de quantification doit être défini lorsque l'entrée est à virgule fixe et que la sortie est en virgule flottante.

**Définition de l'interface**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`round`](#ops_8h_1a81db8ac4866004f75fb65db876262785)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Paramètres d'entrée**

| Nom du paramètre  | type           | Oui ou Non | description                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | être       | entrée                |
| `dtype` | datatype_t     | être       | Type de données du tenseur de sortie |

**La valeur renvoyée**

`result<runtime_tensor>`

**Exemples de code**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::round(input, output_type).unwrap_or_throw();
```

### 6.2.8 étage

**Description de la fonctionnalité**

Calculer la valeur de gel, actuellement soutenir l'entrée uint8 / int8, la sortie est également uint8 / int8, notez que l'entrée est à point fixe et la sortie est à virgule flottante besoin de définir les paramètres de quantification.

**Définition de l'interface**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`floor`](#ops_8h_1a1079af8fe9fb6edbb2906d91fac12635)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Paramètres d'entrée**

| Nom du paramètre  | type           | Oui ou Non | description                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | être       | entrée                |
| `dtype` | datatype_t     | être       | Type de données du tenseur de sortie |

**La valeur renvoyée**

`result<runtime_tensor>`

**Exemples de code**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::floor(input, output_type).unwrap_or_throw();
```

### 6.2.9 ceil

**Description de la fonctionnalité**

Calculer la valeur ceil, actuellement supporte l'entrée uint8 / int8, la sortie est également uint8 / int8, notez que l'entrée est à virgule fixe et la sortie est à virgule flottante besoin de définir les paramètres de quantification.

**Définition de l'interface**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`ceil`](#ops_8h_1ad3b78c97f1e5348a26de7e5ba2396fb7)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Paramètres d'entrée**

| Nom du paramètre  | type           | Oui ou Non | description                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | être       | entrée                |
| `dtype` | datatype_t     | être       | Type de données du tenseur de sortie |

**La valeur renvoyée**

`result<runtime_tensor>`

**Exemples de code**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::ceil(input, output_type).unwrap_or_throw();
```

### 6.2.10 abs

**Description de la fonctionnalité**

Calculer la valeur abs, actuellement support d'entrée uint8 / int8, sortie est également uint8 / int8, notez que l'entrée est à point fixe et la sortie est à virgule flottante doit définir les paramètres de quantification.

**Définition de l'interface**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`abs`](#ops_8h_1ad8290dc793bae0dc22b3baf9e0f80c14)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Paramètres d'entrée**

| Nom du paramètre  | type           | Oui ou Non | description                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | être       | entrée                |
| `dtype` | datatype_t     | être       | Type de données du tenseur de sortie |

**La valeur renvoyée**

`result<runtime_tensor>`

**Exemples de code**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::abs(input, output_type).unwrap_or_throw();
```

### 6.2.11 neg

**Description de la fonctionnalité**

Calculer la valeur de neg, actuellement support d'entrée uint8 / int8, sortie est également uint8 / int8, notez que l'entrée est à point fixe et la sortie est à virgule flottante doit définir les paramètres de quantification.

**Définition de l'interface**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`neg`](#ops_8h_1aa1b7858802e1afce78db72163c5210d8)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Paramètres d'entrée**

| Nom du paramètre  | type           | Oui ou Non | description                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | être       | entrée                |
| `dtype` | datatype_t     | être       | Type de données du tenseur de sortie |

**La valeur renvoyée**

`result<runtime_tensor>`

**Exemples de code**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::neg(input, output_type).unwrap_or_throw();
```

### 6.2.12 quantifier

**Description de la fonctionnalité**

Dt_bfloat16 d'entrée, données dt_float32, dt_int8 de sortie ou sortie dt_uint8

**Définition de l'interface**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`quantize`](#ops_8h_1ad8ad779083b5c08da520d2f1c2469c3a)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Paramètres d'entrée**

| Nom du paramètre  | type           | Oui ou Non | description                                |
| --------- | -------------- | -------- | ----------------------------------- |
| `input` | runtime_tensor | être       | Entrée, le type doit être float32 ou bfloat16 |
| `dtype` | datatype_t     | être       | Type de données du tenseur de sortie                 |

**La valeur renvoyée**

`result<runtime_tensor>`

**Exemples de code**

```cpp
auto quantized = F::quantize(input, dt_int8).unwrap_or_throw();
```

### 6.2.13 Déquantiser

**Description de la fonctionnalité**

Entrez l'entrée uint8 ou int8, convertissez-la en données float ou bfloat. Notez que l'utilisateur doit définir à l'avance les paramètres de quantification corrects pour les données pour la déquantisation.

**Définition de l'interface**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`dequantize`](#ops_8h_1ab91a262349baf393c91abad6f393de24)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Paramètres d'entrée**

| Nom du paramètre  | type           | Oui ou Non | description                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | être       | entrée                |
| `dtype` | datatype_t     | être       | Type de données du tenseur de sortie |

**La valeur renvoyée**

`result<runtime_tensor>`

**Exemples de code**

```cpp
input.quant_param({ 0, 1 });
auto dequantized = F::dequantize(input, output_type).unwrap_or_throw();
```

### 6.2.14 culture

**Description de la fonctionnalité**

Étant donné les bbox, recadrées à partir du tenseur d'origine et redimensionnées la sortie dans le nouveau tenseur. Acceptez dt_bfloat16, dt_float32, dt_int8, sortie de type dt_uint8, sortie du même type.

**Définition de l'interface**

`NNCASE_API inline result<runtime::runtime_tensor> crop(runtime::runtime_tensor &input, runtime::runtime_tensor &bbox, size_t out_h, size_t out_w, image_resize_mode_t resize_mode, bool align_corners, bool half_pixel_centers) noexcept`

**Paramètres d'entrée**

| Nom du paramètre           | type                | Oui ou Non | description                                                                                     |
| ------------------ | ------------------- | -------- | ---------------------------------------------------------------------------------------- |
| entrée              | runtime_tensor      | être       | Entrez les données, besoin de formater [n,c,h,w] la mise en page, si les données sont uint8 ou int8 s'il vous plaît assurer l'exactitude des paramètres de quantification des données       |
| bbox               | runtime_tensor      | être       | Entrez les données bbox, besoin de [1,1,m,4] formater la mise en page, les données internes sont[y0,x0,y1,x1], le type est[float32,bfloat16] |
| out_h              | size_t              | être       | Hauteur des données de sortie                                                                           |
| out_w              | size_t              | être       | Entrez la largeur des données                                                                            |
| resize_mode        | image_resize_mode_t | être       | Redimensionner le modèle de méthode                                                                           |
| align_corners      | Bool                | être       | Redimensionner si align_corners                                                    |
| half_pixel_centers | Bool                | être       | Redimensionner si le pixel est aligné au centre                                                                  |

**La valeur renvoyée**

`result<runtime_tensor>`

**Exemples de code**

```cpp
auto bbox = get_rand_bbox(input_shape, roi_amount);
auto &&[out_h, out_w] = get_rand_out_hw();
auto output_opt = F::crop(input, bbox, out_h, out_w, resize_mode).unwrap_or_throw();
```

### 6.2.15 redimensionnement

**Description de la fonctionnalité**

Compte tenu de la largeur de la hauteur de sortie, redimensionnez le tenseur d'entrée à la nouvelle taille. Acceptez dt_bfloat16, dt_float32, dt_int8, sortie de type dt_uint8, sortie du même type.

**Définition de l'interface**

`NNCASE_API inline result<runtime::runtime_tensor> resize(runtime::runtime_tensor &input, size_t out_h, size_t out_w, image_resize_mode_t resize_mode, bool align_corners, bool half_pixel_centers) noexcept`

**Paramètres d'entrée**

| Nom du paramètre           | type                | Oui ou Non | description                                                                               |
| ------------------ | ------------------- | -------- | ---------------------------------------------------------------------------------- |
| entrée              | runtime_tensor      | être       | Entrez les données, doivent être [n,c,h,w] formatées, si les données sont uint8 ou int8 s'il vous plaît assurer l'exactitude des paramètres de quantification des données |
| out_h              | size_t              | être       | Hauteur des données de sortie                                                                     |
| out_w              | size_t              | être       | Entrez la largeur des données                                                                      |
| resize_mode        | image_resize_mode_t | être       | Redimensionner le modèle de méthode                                                                     |
| align_corners      | Bool                | être       | Redimensionner si align_corners                                              |
| half_pixel_centers | Bool                | être       | Redimensionner si le pixel est aligné au centre                                                            |

**La valeur renvoyée**

`result<runtime_tensor>`

**Exemples de code**

```cpp
auto &&[out_h, out_w] = get_rand_out_hw();
auto output_opt = F::resize(input, out_h, out_w, resize_mode, false, false).unwrap_or_throw();
```

### 6.2.16 tampon

**Description de la fonctionnalité**

Les données de remplissage sur chaque dimension acceptent la sortie de dt_bfloat16, dt_float32, dt_int8, dt_uint8 type et sortie du même type.

**Définition de l'interface**

`NNCASE_API inline result<runtime::runtime_tensor> pad(runtime::runtime_tensor &input, runtime_paddings_t &paddings, pad_mode_t pad_mode, float fill_v)`

**Paramètres d'entrée**

| Nom du paramètre | type               | Oui ou Non | description                                                                                                                                       |
| -------- | ------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| entrée    | runtime_tensor     | être       | Entrez les données, si les données sont uint8 ou int8 Assurez-vous de l'exactitude des paramètres de quantification des données                                                                                  |
| rembourrage  | runtime_paddings_t | être       | Par exemple, la valeur de remplissage est `[ {2,3}, {1,3} ]`indiquée devant le pad 2 dans la dernière dimension, suivie du pad 3. L'avant-dernière dimension est précédée du pad 1, suivi du pad 2 |
| pad_mode | pad_mode_t         | être       | Actuellement, seul le mode const est pris en charge                                                                                                                   |
| fill_v   | flotter              | être       | Remplir les valeurs                                                                                                                                     |

**La valeur renvoyée**

`result<runtime_tensor>`

**Exemples de code**

```cpp
runtime_paddings_t paddings{ { 0, 0 }, { 0, 0 }, { 0, 0 }, { 1, 2 } };
auto output = F::pad(input, paddings, pad_constant, pad_value).unwrap_or_throw();
```
<!-- markdownlint-enable no-emphasis-as-header -->
# 7 Livre blanc quantitatif

## 7.1 Livre blanc sur la quantification du modèle de classification

| Modèle de classification     | Précision du processeur (Top-1) | Précision en virgule flottante (Top-1) | Précision uint8 (Top-1) | int8 Précision (Top-1) |
| ------------ | -------------- | --------------- | ---------------- | --------------- |
| alexnet      | 0.531          | 0.53            | N/A              | 0.52            |
| densenet 121 | 0.732          | 0.732           | 0.723            | N/A             |
| inception v3 | 0.766          | 0.765           | 0.773            | 0.77            |
| inception v4 | 0.789          | 0.789           | 0.793            | 0.792           |
| mobilenet v1 | 0.731          | 0.73            | 0.723            | 0.718           |
| mobilenet v2 | 0.713          | 0.715           | 0.713            | 0.719           |
| resnet50 v2  | 0.747          | 0.74            | 0.748            | 0.749           |
| vgg 16       | 0.689          | 0.687           | 0.690            | 0.689           |

> Ce tableau sert principalement à comparer les performances de la quantification, la précision du processeur est l'ensemble complet des données de l'ensemble de validation ImageNet, et la précision de la virgule flottante et de la quantification est le résultat du test du sous-ensemble de données pour la première image des 1000 classes de l'ensemble de validation en fonction du nombre ordinal.
>
> Les résultats des tests d'Alexnet et de SenseNet sont des données anciennes, qui sont tous deux des résultats de test des 1000 premières images de l'ensemble de vérification en tant que sous-ensemble des données, et N/A est que le sous-ensemble de données de test à ce moment-là est différent du processeur, il n'est donc pas utilisé comme comparaison.
>
> Étant donné que le réseau sélectionné ne provient pas nécessairement de l'officiel ou qu'il existe des différences dans le prétraitement, etc., il peut différer de la performance officielle.

## 7.2 Livre blanc sur la quantification du modèle de détection

1. YOLOV3

    | COCOAPI                                                      | Résultats officiels | Précision en virgule flottante du processeur | gnne précision en virgule flottante | précision uint8 | int8 précision |
    | ------------------------------------------------------------ | -------- | ----------- | ------------ | --------- | -------- |
    | Précision moyenne (AP) @ [IoU = 0,50:0,95\| surface = tous \| maxDets = 100] | 0.314    | 0.307       | 0.306        | 0.295     | 0.288    |
    | Précision moyenne (AP) @ [IoU = 0,50\| surface = tous \| maxDets = 100] | 0.559    | 0.555       | 0.554        | 0.555     | 0.554    |
    | Précision moyenne (AP) @ [IoU = 0,75\| surface = tous \| maxDets = 100] | 0.318    | 0.308       | 0.307        | 0.287     | 0.275    |
    | Précision moyenne (AP) @ [IoU = 0,50:0,95\| superficie = petite \| maxDets = 100] | 0.142    | 0.150       | 0.149        | 0.147     | 0.144    |
    | Précision moyenne (AP) @ [IoU= 0,50:0,95\| surface = moyenne \| maxDets = 100] | 0.341    | 0.332       | 0.332        | 0.322     | 0.316    |
    | Précision moyenne (AP) @ [IoU = 0,50:0,95\| surface = grande \| maxDets = 100] | 0.464    | 0.437       | 0.437        | 0.414     | 0.404    |
    | Rappel moyen (RA) @ [IoU= 0,50:0,95\| surface = tous \| maxDets = 1] | 0.278    | 0.270       | 0.271        | 0.262     | 0.256    |
    | Rappel moyen (RA) @ [IoU= 0,50:0,95\| surface = tous \| maxDets = 10] | 0.419    | 0.412       | 0.412        | 0.399     | 0.392    |
    | Rappel moyen (RA) @ [IoU = 0,50:0,95\| surface = tous \| maxDets = 100] | 0.442    | 0.433       | 0.433        | 0.421     | 0.414    |
    | Rappel moyen (RA) @ [IoU = 0,50:0,95\| superficie = petite \| maxDets = 100] | 0.239    | 0.251       | 0.251        | 0.248     | 0.246    |
    | Rappel moyen (RA) @ [IoU= 0,50:0,95\| surface = moyenne \| maxDets = 100] | 0.482    | 0.462       | 0.463        | 0.451     | 0.443    |
    | Rappel moyen (RA) @ [IoU = 0,50:0,95\| surface = grande \| maxDets = 100] | 0.611    | 0.586       | 0.585        | 0.559     | 0.550    |

2. ssd-mobilenetv1

    | COCOAPI                                                                    | Résultats officiels | Précision en virgule flottante du processeur | gnne précision en virgule flottante | précision uint8 | int8 précision |
    | -------------------------------------------------------------------------- | -------- | ----------- | ------------ | --------- | -------- |
    | Précision moyenne (AP) @ [IoU = 0,50:0,95\| surface = tous \| maxDets = 100]   | 0.184    | 0.184       | 0.184        | 0.183     | 0.183    |
    | Précision moyenne (AP) @ [IoU = 0,50\| surface = tous \| maxDets = 100]        | 0.306    | 0.307       | 0.306        | 0.305     | 0.306    |
    | Précision moyenne (AP) @ [IoU = 0,75\| surface = tous \| maxDets = 100]        | 0.191    | 0.192       | 0.190        | 0.189     | 0.190    |
    | Précision moyenne (AP) @ [IoU = 0,50:0,95\| superficie = petite \| maxDets = 100] | 0.017    | 0.017       | 0.017        | 0.017     | 0.017    |
    | Précision moyenne (AP) @ [IoU= 0,50:0,95\| surface = moyenne \| maxDets = 100] | 0.157    | 0.157       | 0.157        | 0.156     | 0.155    |
    | Précision moyenne (AP) @ [IoU = 0,50:0,95\| surface = grande \| maxDets = 100] | 0.371    | 0.372       | 0.371        | 0.370     | 0.369    |
    | Rappel moyen (RA) @ [IoU= 0,50:0,95\| surface = tous \| maxDets = 1]         | 0.180    | 0.180       | 0.180        | 0.181     | 0.181    |
    | Rappel moyen (RA) @ [IoU= 0,50:0,95\| surface = tous \| maxDets = 10]        | 0.242    | 0.242       | 0.242        | 0.243     | 0.243    |
    | Rappel moyen (RA) @ [IoU = 0,50:0,95\| surface = tous \| maxDets = 100]      | 0.242    | 0.242       | 0.242        | 0.243     | 0.243    |
    | Rappel moyen (RA) @ [IoU = 0,50:0,95\| superficie = petite \| maxDets = 100]    | 0.026    | 0.026       | 0.026        | 0.026     | 0.026    |
    | Rappel moyen (RA) @ [IoU= 0,50:0,95\| surface = moyenne \| maxDets = 100]    | 0.206    | 0.206       | 0.206        | 0.206     | 0.205    |
    | Rappel moyen (RA) @ [IoU = 0,50:0,95\| surface = grande \| maxDets = 100]    | 0.489    | 0.491       | 0.490        | 0.490     | 0.491    |

3. YOLOV5S

    | COCOAPI                                                                    | Résultats officiels | Précision en virgule flottante du processeur | gnne précision en virgule flottante | précision uint8 | int8 précision |
    | -------------------------------------------------------------------------- | -------- | ----------- | ------------ | --------- | -------- |
    | Précision moyenne (AP) @ [IoU = 0,50:0,95\| surface = tous \| maxDets = 100]   | 0.367    | 0.365       | 0.335        | 0.334     | 0.335    |
    | Précision moyenne (AP) @ [IoU = 0,50\| surface = tous \| maxDets = 100]        | 0.555    | 0.552       | 0.518        | 0.518     | 0.518    |
    | Précision moyenne (AP) @ [IoU = 0,75\| surface = tous \| maxDets = 100]        | 0.398    | 0.395       | 0.364        | 0.363     | 0.362    |
    | Précision moyenne (AP) @ [IoU = 0,50:0,95\| superficie = petite \| maxDets = 100] | 0.223    | 0.220       | 0.199        | 0.199     | 0.197    |
    | Précision moyenne (AP) @ [IoU= 0,50:0,95\| surface = moyenne \| maxDets = 100] | 0.419    | 0.418       | 0.387        | 0.386     | 0.386    |
    | Précision moyenne (AP) @ [IoU = 0,50:0,95\| surface = grande \| maxDets = 100] | 0.463    | 0.459       | 0.423        | 0.422     | 0.423    |
    | Rappel moyen (RA) @ [IoU= 0,50:0,95\| surface = tous \| maxDets = 1]         | 0.306    | 0.306       | 0.288        | 0.287     | 0.287    |
    | Rappel moyen (RA) @ [IoU= 0,50:0,95\| surface = tous \| maxDets = 10]        | 0.518    | 0.518       | 0.487        | 0.486     | 0.487    |
    | Rappel moyen (RA) @ [IoU = 0,50:0,95\| surface = tous \| maxDets = 100]      | 0.576    | 0.576       | 0.540        | 0.539     | 0.540    |
    | Rappel moyen (RA) @ [IoU = 0,50:0,95\| superficie = petite \| maxDets = 100]    | 0.391    | 0.399       | 0.350        | 0.350     | 0.347    |
    | Rappel moyen (RA) @ [IoU= 0,50:0,95\| surface = moyenne \| maxDets = 100]    | 0.641    | 0.640       | 0.606        | 0.605     | 0.607    |
    | Rappel moyen (RA) @ [IoU = 0,50:0,95\| surface = grande \| maxDets = 100]    | 0.716    | 0.710       | 0.680        | 0.683     | 0.685    |

# 8 Foire aux questions (FAQ)

1. 安装wheel时报错: « xxx.whl n'est pas une roue supportée sur cette plate-forme. » **

    Q: 安装nncase wheel包, 出现ERROR: nncase-1.0.0.20210830-cp37-cp37m-manylinux_2_24_x86_64.whl n'est pas une roue prise en charge sur cette plate-forme.

    R : Mise à niveau pip > = 20,3

    ```shell
    sudo pip3 install --upgrade pip
    ```

2. **Lorsque le CRB exécute le programme d'inférence d'application, il signale l'erreur « std::bad_alloc »**

    Q : Exécutez le programme d'inférence d'application sur le CRB et lancez une exception « std::bad_alloc »

    ```shell
    $ ./cpp.sh
    case ./yolov3_bfloat16 build at Sep 16 2021 18:12:03
    terminate called after throwing an instance of 'std::bad_alloc'
    what():  std::bad_alloc
    ```

    R : std::bad_alloc exceptions sont généralement causées par des échecs d'allocation de mémoire, qui peuvent être vérifiés comme suit.

    - Vérifiez si le kmodel généré dépasse la mémoire disponible actuelle du système (par exemple, la taille du modèle yolov3 bfloat16 est de 121 Mo, la mémoire disponible actuelle de Linux n'est que de 70 Mo, l'exception sera levée).  S'il dépasse, essayez d'utiliser la quantification post-formation pour réduire la taille du kmodel.
    - Vérifiez l'application pour les fuites de mémoire

3. **Lors de l'exécution du programme d'inférence d'application[.. t_runtime_tensor.cpp:310 (créer)] data.size_bytes() == size = false (bool).**

    Q : Simulator exécute le programme d'inférence de l'application, en lançant une exception «[.. t_runtime_tensor.cpp:310 (créer)] data.size_bytes() == size = false (bool) »

    R : Vérifiez les informations du tenseur d'entrée pour les paramètres, en vous concentrant sur la forme d'entrée et le nombre d'octets occupés par chaque élément (fp32/uint8)

**Clause de non-responsabilité en matière de**  
Pour la commodité des clients, Canaan utilise un traducteur IA pour traduire du texte en plusieurs langues, ce qui peut contenir des erreurs. Nous ne garantissons pas l'exactitude, la fiabilité ou l'actualité des traductions fournies. Canaan ne sera pas responsable de toute perte ou dommage causé par la confiance accordée à l'exactitude ou à la fiabilité des informations traduites. S'il existe une différence de contenu entre les traductions dans différentes langues, la version simplifiée en chinois prévaudra.

Si vous souhaitez signaler une erreur de traduction ou une inexactitude, n'hésitez pas à nous contacter par courrier.
