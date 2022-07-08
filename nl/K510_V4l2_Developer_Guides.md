![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 V4L2 Handleiding voor ontwikkelaars</font>**

<font face="黑体"  size=3>Document versie: V1.0.0</font>

<font face="黑体"  size=3>Publicatiedatum: 2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Disclaimer**</font>
De producten, diensten of functies die u koopt, zijn onderworpen aan de commerciële contracten en voorwaarden van Beijing Canaan Jiesi Information Technology Co., Ltd. ("het Bedrijf", hierna hetzelfde), en alle of een deel van de producten, diensten of functies die in dit document worden beschreven, vallen mogelijk niet binnen het bereik van uw aankoop of gebruik. Tenzij anders overeengekomen in het contract, wijst het bedrijf alle verklaringen of garanties af, expliciet of impliciet, met betrekking tot de nauwkeurigheid, betrouwbaarheid, volledigheid, marketing, specifiek doel en niet-agressie van verklaringen, informatie of inhoud van dit document. Tenzij anders overeengekomen, wordt dit document uitsluitend verstrekt als leidraad voor gebruik.
Vanwege upgrades van de productversie of andere redenen kan de inhoud van dit document van tijd tot tijd zonder enige kennisgeving worden bijgewerkt of gewijzigd. 

**<font face="黑体"  size=3>Handelsmerkkennisgevingen</font>**

""<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, "Canaan" icoon, Kanaän en andere handelsmerken van Kanaän en andere handelsmerken van Kanaän zijn handelsmerken van Beijing Canaan Jiesi Information Technology Co., Ltd. Alle andere handelsmerken of geregistreerde handelsmerken die in dit document kunnen worden genoemd, zijn eigendom van hun respectieve eigenaars. 

**<font face="黑体"  size=3>Copyright ©2022 Beijing Canaan Jiesi Information Technology Co, Ltd</font>**
Dit document is alleen van toepassing op de ontwikkeling en het ontwerp van het K510-platform, zonder de schriftelijke toestemming van het bedrijf mag geen enkele eenheid of persoon een deel of de inhoud van dit document in welke vorm dan ook verspreiden. 

**<font face="黑体"  size=3>Beijing Canaan Jiesi Information Technology Co, Ltd</font>**
URL: canaan-creative.com
Zakelijke vragen: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# inleiding
**<font face="黑体"  size=5>Doel van het document</font>**
Dit document is een toelichtend document voor het K510 V4L2 toepassingsvoorbeeld. 

**<font face="黑体"  size=5>Reader Objecten</font>**

De belangrijkste personen op wie dit document (deze gids) van toepassing is:

- Softwareontwikkelaars
- Technisch ondersteunend personeel

**<font face="黑体"  size=5>Revisiegeschiedenis</font>**
 <font face="宋体"  size=2>De revisiegeschiedenis bevat een beschrijving van elke documentupdate. De nieuwste versie van het document bevat updates voor alle voorgaande versies. </font>

| Het versienummer   | Gewijzigd door     | Datum van herziening | Opmerkingen bij herziening |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | Systeemsoftwaregroepen | 2022-03-09 | SDK V1.5 vrijgegeven |
| v1.0.1 | Zhu Dalei | 2022-03-11 | SDK V1.5 vrijgegeven |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Inhoud</font>**

[INHOUDSOPGAVE]

<div style="page-break-after:always"></div>

# 1 V4L2 mediactl bibliotheek

## 1.1 Beschrijving van headerbestand

\#include "media_ctl.h"

## 1.2 API-functiebeschrijvingen

### ◆ mediactl_init

```c
struct video_info {
    unsigned int video_used;
    char *video_name[4];
    unsigned int enable[4];
    unsigned int video_width[4];
    unsigned int video_height[4];
    unsigned int video_out_format[4];
};

int mediactl_init(char *video_cfg_file,struct video_info *dev_info);
```

Media initialiseren.

#### parameter

```text
参数:
[in]    video_cfg_file: video的配置文件，这个文件的内容只需关心下面解释的内容，具体解释如下。
sensor0_name:只在V4L2驱动中设置的sensor驱动名字。
sensor0_cfg_file:sensor对应的isp参数配置文件名字，如imx219_0.conf。
sensor0_total_width:sensor输出的水平方向的总像素，用来产生VSYNC信号，如3476
sensor0_total_height:sensor输出的总行数，用来产生HSYNC信号，如1166
sensor0_active_width:sensor输出的水平方向的有效像素，如1920,
sensor0_active_height:sensor输出的有效行数，如1080
video2_used:1 -- 使能，0 -- 没有使用。
video2_width:video输出的宽度，如1920。
video2_height:video输出的高度，如1080。
video2_out_format:1--指YUV420,NV21。
video3_used:1 -- 使能，0 -- 没有使用。
video3_width:video输出的宽度，如1080。
video3_height:video输出的高度，如720。
video3_out_format:1--指YUV420,NV21。
video4_used:1 -- 使能，0 -- 没有使用。
video4_width:video输出的宽度，如640。
video4_height:video输出的高度，如480。
video4_out_format:1--指YUV420,NV21。
video5_used:1 -- 使能，0 -- 没有使用。
video5_width:video输出的宽度，如320。
video5_height":video存储的高度，如320。
video5_height_r:video输出的高度，如240。
video5_out_format:0--指分离RGB，1--指ARGB。
sensor1_name:只在V4L2驱动中设置的sensor驱动名字。
sensor1_cfg_file:sensor对应的isp参数配置文件名字，如imx219_0.conf。
sensor1_total_width:sensor输出的水平方向的总像素，用来产生VSYNC信号，如3476
sensor1_total_height:sensor输出的总行数，用来产生HSYNC信号，如1166
sensor1_active_width:sensor输出的水平方向的有效像素，如1920,
sensor1_active_height:sensor输出的有效行数，如1080
video6_used:1 -- 使能，0 -- 没有使用。
video6_width:video输出的宽度，如1920。
video6_height:video输出的高度，如1080。
video6_out_format:1--指YUV420,NV21。
video7_used:1 -- 使能，0 -- 没有使用。
video7_width:video输出的宽度，如1080。
video7_height:video输出的高度，如720.
video7_out_format:1--指YUV420,NV21。
video8_used:1 -- 使能，0 -- 没有使用。
video8_width:video输出的宽度，如640。
video8_height:video输出的高度，如480。
video8_out_format:1--指YUV420,NV21。
video9_used:1 -- 使能，0 -- 没有使用。
video9_width:video输出的宽度，如320。
video9_height:video存储的宽度，如320。
video9_height_r:video输出的高度，如240。
video9_out_format:0--指分离RGB，1--指ARGB。
[out]   dev_info: mediactl_lib返回从video的配置文件得到的video信息，具体的解释如下。
video_used:这里是指ISP的pipeline，如果使用就会返回1，否则0。K510支持ISP_F2K/ISP_R2K这两个pipeline，每个pipeline最多支持4个video输出。
video_name[4]:返回的video的名字。f2k的四个video是video2/video3/video4/video5;r2k的四个video是 video6/video7/video8/video9
enable[4]:返回的每个video是否使能，1 -- 使能，0 -- 没有使用。
video_width[4]:返回的每个video的宽度。
video_height[4]:返回的每个video的高度。
video_out_format[4]:返回的每个video的输出图像格式，具体见《video的配置文件》的解释。
具体使用方法如下:
char *video_cfg_file = "video_cfg";
struct video_info dev_info[2]
mediactl_init(video_cfg_file,&dev_info)
```

#### De retourwaarde

```text
0 成功,  -1 失败.
```

### ◆ mediactl_exit

Sluit het media-apparaat af en maak het gevraagde geheugen voor delen vrij.

#### parameter

```text
参数:
无
```

### ◆ mediactl_set_ae

```c
enum isp_pipeline_e {
    ISP_F2K_PIPELINE,
    ISP_R2K_PIPELINE,
    ISP_TOF_PIPELINE
};
int mediactl_set_ae(enum isp_pipeline_e pipeline);
```

Configureer de AE-waarde van de sensor

#### parameter

```text
参数:
ISP_F2K_PIPELINE:配置f2k pipeline的AE。
ISP_R2K_PIPELINE:配置r2k pipeline的AE。
ISP_TOF_PIPELINE:没有使用。
```

### ◆ mediactl_get_isp_modules

```c
enum isp_modules {
    ISP_TPG,
    ISP_BLC,
    ISP_LSC,
    ISP_AE,
    ISP_AWB,
    ISP_AWB_D65,
    ISP_AWB_CCM,
    ISP_WDR,
    ISP_RGB_GAMMA,
    ISP_YUV_GAMMA,
    ISP_ADA,
    ISP_ADA_SBZ,
    ISP_ADA_CCR,
    ISP_RGBIR,
    ISP_RAW_2DNR,
    ISP_YUV_Y_2DNR,
    ISP_YUV_UV_2DNR,
    ISP_3DNR,
    ISP_LTM,
    ISP_SHARP,
    ISP_CC,
    ISP_CTRST,
    ISP_LUMA,
    ISP_SATURATION,
    ISP_LDC,
    ISP_AF,
};

unsigned int mediactl_get_isp_modules(enum isp_pipeline_e pipeline,enum isp_modules module);
```

Hiermee wordt de inschakelstatus van elke module van de internetprovider opgehaald.

#### parameter

```text
参数:
isp_pipeline_e:具体见mediactl_set_ae中的解释。
isp_modules:
  ISP_TPG --  Test Pattern Control模块
  ISP_BLC --  Black Level Correction模块
  ISP_LSC --  Lens Shading Correction模块
  ISP_AE --  AUTO Exposure Gain模块
  ISP_AWB -- AUTO white balance模块
  ISP_AWB_D65 -- AUTO white balance d65模块 
  ISP_AWB_CCM -- AUTO white balance ccm模块 
  ISP_WDR --  wide dynamic range模块
  ISP_RGB_GAMMA -- rgb gamma模块 
  ISP_YUV_GAMMA -- yuv gamma模块 
  ISP_ADA --  Adaptive dynamic range adjust模块
  ISP_ADA_SBZ -- Image stabilization模块 
  ISP_ADA_CCR -- Color correction模块 
  ISP_RGBIR -- rgbir rectify模块 
  ISP_RAW_2DNR -- raw域2D降噪模块 
  ISP_YUV_Y_2DNR -- yuv域2D Y方向降噪模块 
  ISP_YUV_UV_2DNR -- yuv域2D uv方向降噪模块 
  ISP_3DNR --  yuv域3D降噪模块
  ISP_LTM --  local tone mapping模块
  ISP_SHARP -- sharpness模块  
  ISP_CC --  color correction模块
  ISP_CTRST -- contrast adjust模块 
  ISP_LUMA --  luma adjust模块
  ISP_SATURATION -- saturation adjust 模块 
  ISP_LDC -- lens Distortion Correction模块 
  ISP_AF -- ATUO FOCUS模块 
```

#### De retourwaarde

```text
0 -- 模块没有使能  1 -- 模块使能 
```

# 2 Demo-app

## 2.1 v4l2_drm

Het programma wordt `/app/mediactl_lib`in de directory geplaatst:

- `v4l2_drm.out`:v4l2 en drm linkage case, toegevoegd -f om de naam van het invoerconfiguratiebestand te wijzigen, -e om de isp ae functie te openen. U kunt -h gebruiken om help te bekijken.

V4l2_drm.out uitvoeren

- -e:0 schakelt alle aes uit, 1 zet f-2k ae aan, 2 zet r-2k ae aan en 3 zet alle aes aan. Standaard kunt u -e verlaten om alle aes uit te schakelen.
- De demo vereist dat het videoconfiguratiebestand en het bijbehorende sensorconfiguratiebestand zich in de huidige map bevinden.
- De demo kan enkele en dubbele camera's demonstreren door het configuratiebestand te wijzigen.
- De demo demo single-camera full screen: ./v4l2_drm.out -e 1 -f video_drm_1080x1920.conf
- De demo demo dual camera: ./v4l2_drm.out -f video_drm_1920x1080.conf
- De demo moet ervoor zorgen dat er drie profielen video_drm_1920x1080.conf, imx219_0.conf en imx219_1.conf bestaan.

**Vertaling Disclaimer**  
Voor het gemak van klanten gebruikt Canaan een AI-vertaler om tekst in meerdere talen te vertalen, wat fouten kan bevatten. Wij garanderen niet de nauwkeurigheid, betrouwbaarheid of tijdigheid van de geleverde vertalingen. Canaan is niet aansprakelijk voor enig verlies of schade veroorzaakt door het vertrouwen op de nauwkeurigheid of betrouwbaarheid van de vertaalde informatie. Als er een inhoudelijk verschil is tussen de vertalingen in verschillende talen, prevaleert de vereenvoudigd Chinese versie. 

Als u een vertaalfout of onnauwkeurigheid wilt melden, neem dan gerust contact met ons op via e-mail.