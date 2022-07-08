![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 AI Application Guide</font>**

<font face="黑体"  size=3>Version du document : V1.0.0</font>

<font face="黑体"  size=3>Date de publication : 2022-03-07</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Démenti**</font>
Les produits, services ou fonctionnalités que vous achetez sont soumis aux contrats commerciaux et aux conditions de Beijing Canaan Jiesi Information Technology Co., Ltd. (« la Société », les mêmes ci-après), et tout ou partie des produits, services ou fonctionnalités décrits dans ce document peuvent ne pas être dans le cadre de votre achat ou de votre utilisation. Sauf accord contraire dans le contrat, la Société décline toute représentation ou garantie, expresse ou implicite, quant à l'exactitude, la fiabilité, l'exhaustivité, le marketing, l'objectif spécifique et la non-agression de toute représentation, information ou contenu de ce document. Sauf convention contraire, le présent document est fourni uniquement à titre indicatif de raisonnement.
En raison de mises à niveau de la version du produit ou d'autres raisons, le contenu de ce document peut être mis à jour ou modifié de temps à autre sans préavis. 

**<font face="黑体"  size=3>Avis sur les marques de commerce</font>**

«  »<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, l'icône « Canaan », Canaan et d'autres marques de commerce de Canaan et d'autres marques de commerce de Canaan sont des marques de commerce de Beijing Canaan Jiesi Information Technology Co., Ltd. Toutes les autres marques de commerce ou marques déposées qui peuvent être mentionnées dans ce document sont la propriété de leurs propriétaires respectifs. 

**<font face="黑体"  size=3>Copyright ©2022 Beijing Canaan Jiesi Information Technology Co., Ltd</font>**
Ce document ne s'applique qu'au développement et à la conception de la plate-forme K510, sans l'autorisation écrite de la société, aucune unité ou individu ne peut diffuser une partie ou la totalité du contenu de ce document sous quelque forme que ce soit. 

**<font face="黑体"  size=3>Beijing Canaan Jiesi Information Technology Co., Ltd</font>**
URL: canaan-creative.com
Demandes de renseignements des entreprises : salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# préface
**<font face="黑体"  size=5>Objet </font>**du document
Ce document est un document d'accompagnement pour l'application K510 AI et est conçu pour aider les ingénieurs à comprendre l'écriture et l'application des applications k510 AI. 

**<font face="黑体"  size=5>Objets de lecture</font>**

Les principales personnes auxquelles ce document (ce guide) s'applique :

- Développeurs de logiciels
- Personnel de soutien technique

**<font face="黑体"  size=5>Historique des révisions</font>**
 <font face="宋体"  size=2>L'historique des révisions accumule une description de chaque mise à jour de document. La dernière version du document contient des mises à jour pour toutes les versions précédentes. </font>

| Le numéro de version   | Modifié par     | Date de révision | Notes de révision |
| :-----  |-------    |  ------ | ------  |
| Version 1.0.0  | Division des produits d'IA  | 2022-03-07 |      |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |
|        |        |            |            |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenu</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Introduction

Ce document décrit l'écriture et l'application des applications K510 AI. Basé sur la puce K510 AI, le développement d'applications d'IA comporte les étapes suivantes:

Préparation du modèle : Le modèle entraîné est validé côté PC (l'inférence d'image statique peut être utilisée) pour s'assurer de l'exactitude du modèle

Génération de modèle : le modèle entraîné est compilé à l'aide du compilateur nncase pour générer un kmodel

Validation du modèle : le kmodel généré est validé avec précision à l'aide du simulateur nncase

Écrire des applications d'IA: lecture complète de vidéos / images, prétraitement d'entrée, inférence de modèle, post-traitement de modèle

Compiler des applications d'IA : utilisez la chaîne d'outils de compilation croisée pour compiler des applications d'IA K510

Déploiement et co-mise en service : l'application d'IA compilée est déployée sur le produit matériel K510 et le co-débogage fonctionnel est effectué dans le scénario réel

L'architecture globale du développement d'applications d'IA sur la puce K510 AI est illustrée dans la figure suivante :

![](../zh/images/ai_demo/image-ai-demo.png)

Ce document prendra le modèle onnx des YOLOV5 de résolution 320x320 comme exemple pour présenter l'ensemble du processus d'écriture et d'application des applications d'IA K510.

# 2 Préparation du modèle

Le modèle onnx pour YOLOV5s pour l'inférence se trouve dans le sous-répertoire /docs/utils/AI_Application/aidemo_sdk/models/onnx (télécharger les modèles si aucun fichier n'est disponible[](https://github.com/kendryte/k510_docs/releases/download/v1.5/models.tar.gz)).  et décompressez), l'image statique se trouve dans le sous-répertoire /docs/utils/AI_Application/aidemo_sdk/examples/python_inference_on_PC/data, et le script se trouve dans le sous-répertoire /docs/utils/AI_Application/aidemo_sdk/examples/python_inference_on_PC. 

Suivez l'invite de commande script pour exécuter le script yolov5_image.py afin d'obtenir le résultat d'inférence de l'image statique. Détectez l'exactitude du modèle en vérifiant que la zone de détection de l'image de sortie est correcte ou non.

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

# 3 Génération de modèles

La génération de modèle dépend du compilateur nncase et les règles spécifiques d'utilisation du compilateur nncase se trouvent[ K510_nncase_Developer_Guides.md](./K510_nncase_Developer_Guides.md). Le script qui génère le kmodel pour YOLOV5s se trouve dans le sous-répertoire /docs/utils/AI_Application/aidemo_sdk/scripts. 

À l'invite de commandes du script, exécutez la gen_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py pour générer le kmodel correspondant.

```shell
usage: gen_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py [-h] [--target TARGET] [--dump_dir DUMP_DIR] [--onnx ONNX] [--kmodel KMODEL]

optional arguments:
  -h, --help           show this help message and exit
  --target TARGET      target to run
  --dump_dir DUMP_DIR  temp folder to dump
  --onnx ONNX          onnx model path
  --kmodel KMODEL      kendryte model path
```

Il convient de noter que pour minimiser le prétraitement sur le processeur, les options de compilation dans le script sont configurées comme suit :

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

# 4 Validation du modèle

La validation du modèle dépend du simulateur nncase, et les règles spécifiques pour l'utilisation du simulateur nncase se trouvent[ dans K510_nncase_Developer_Guides.md](./K510_nncase_Developer_Guides.md). Vérifiez que le script kmodel de yolov5s se trouve dans le sous-répertoire /docs/utils/AI_Application/aidemo_sdk/scripts. 

À l'invite de commandes de script, exécutez simu_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py pour vérifier que le kmodel correspondant est généré correctement.

```shell
usage: sim_yolov5s_320_with_sigmoid_bf16_with_preprocess_output_nhwc.py [-h] [--onnx ONNX] [--kmodel KMODEL]

optional arguments:
  -h, --help       show this help message and exit
  --onnx ONNX      original model file
  --kmodel KMODEL  kmodel file
```

Si la similitude du cosinus est proche de 1 ou égale à 1, l'exactitude du kmodel généré est assurée.

```text
output 0 cosine similarity : 0.9999450445175171
output 1 cosine similarity : 0.9999403953552246
output 2 cosine similarity : 0.9999019503593445
```

# 5 Écrire des applications d'IA

La validation du modèle dépend du runtime nncase et les règles spécifiques d'utilisation du runtime nncase se trouvent[ K510_nncase_Developer_Guides.md](./K510_nncase_Developer_Guides.md). Référence de l'application d'IA`k510_buildroot/package/ai/code/object_detect`. Tout d'abord, vous devez créer une instance de détection d'objet et allouer de l'espace pour l'entrée et la sortie kmodel. 

```c++
objectDetect od(obj_thresh, nms_thresh, net_len, {valid_width, valid_height});
od.load_model(kmodel_path);  // load kmodel
od.prepare_memory();  // memory allocation
```

Pour implémenter une copie mémoire nulle, associez l'adresse de sortie isp à l'adresse d'entrée kmodel

```c++
// define cv::Mat for ai input
// padding offset is (valid_width - valid_height) / 2 * valid_width
cv::Mat rgb24_img_for_ai(net_len, net_len, CV_8UC3, od.virtual_addr_input[0] + (valid_width - valid_height) / 2 * valid_width);
```

Configure la largeur et la hauteur de la sortie ISP

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

Configurez le fichier de configuration vidéo approprié, video_height_r la hauteur de sortie réelle du FAI et le video_height le décalage de hauteur entre les différents canaux du FAI.

```json
"/dev/video5":{
    "video5_used":1,
    "video5_width":320,
    "video5_height":320,
    "video5_height_r":240,
    "video5_out_format":0
}
```

Associer les adresses d'entrée et de sortie aux input_tensor et output_tensor du kmodel

```c++
od.set_input(0);
od.set_output();
```

Exécutez le kmodel, obtenez le résultat de sortie et effectuez le post-traitement

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

Enfin, dessinez la boîte de détection sur l'OSD pour afficher la sortie

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

# 6 Compiler des applications d'IA

À l'aide de la chaîne d'outils de compilation croisée, les règles spécifiques pour la compilation des applications d'IA peuvent être référencées[ K510_SDK_Build_and_Burn_Guide](./K510_SDK_Build_and_Burn_Guide.md). 

**Clause de non-responsabilité en matière de**  
Pour la commodité des clients, Canaan utilise un traducteur IA pour traduire du texte en plusieurs langues, ce qui peut contenir des erreurs. Nous ne garantissons pas l'exactitude, la fiabilité ou l'actualité des traductions fournies. Canaan ne sera pas responsable de toute perte ou dommage causé par la confiance accordée à l'exactitude ou à la fiabilité des informations traduites. S'il existe une différence de contenu entre les traductions dans différentes langues, la version simplifiée en chinois prévaudra. 

Si vous souhaitez signaler une erreur de traduction ou une inexactitude, n'hésitez pas à nous contacter par courrier.