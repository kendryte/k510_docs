![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 V4L2 Entwicklerhandbuch</font>**

<font face="黑体"  size=3>Dokumentversion: V1.0.0</font>

<font face="黑体"  size=3>Veröffentlicht: 2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Verzichtserklärung**</font>
Die Produkte, Dienstleistungen oder Funktionen, die Sie erwerben, unterliegen den kommerziellen Verträgen und Bedingungen von Beijing Canaan Jiesi Information Technology Co., Ltd. ("das Unternehmen", dasselbe im Folgenden), und alle oder ein Teil der in diesem Dokument beschriebenen Produkte, Dienstleistungen oder Funktionen fallen möglicherweise nicht in den Rahmen Ihres Kaufs oder Ihrer Nutzung. Sofern im Vertrag nicht anders vereinbart, lehnt das Unternehmen alle ausdrücklichen oder stillschweigenden Zusicherungen oder Gewährleistungen hinsichtlich der Genauigkeit, Zuverlässigkeit, Vollständigkeit, des Marketings, des spezifischen Zwecks und der Nichtverletzung von Zusicherungen, Informationen oder Inhalten dieses Dokuments ab. Sofern nicht anders vereinbart, wird dieses Dokument nur als Leitfaden für die Verwendung zur Verfügung gestellt.
Aufgrund von Produktversions-Upgrades oder anderen Gründen kann der Inhalt dieses Dokuments von Zeit zu Zeit ohne vorherige Ankündigung aktualisiert oder geändert werden.

**<font face="黑体"  size=3>Markenhinweise</font>**

"", "Canaan"-Symbol, Canaan und andere Marken von Canaan und andere Marken von Canaan <img src="../zh/images/canaan-logo.png" style="zoom:33%;" />sind Marken von Beijing Canaan Jiesi Information Technology Co., Ltd. Alle anderen Marken oder eingetragenen Warenzeichen, die in diesem Dokument erwähnt werden können, sind Eigentum ihrer jeweiligen Inhaber.

**<font face="黑体"  size=3>Copyright ©2022 Peking Canaan Jiesi Information Technology Co., Ltd</font>**
Dieses Dokument gilt nur für die Entwicklung und das Design der K510-Plattform, ohne die schriftliche Genehmigung des Unternehmens darf keine Einheit oder Einzelperson einen Teil oder den gesamten Inhalt dieses Dokuments in irgendeiner Form verbreiten.

**<font face="黑体"  size=3>Peking Canaan Jiesi Informationstechnologie Co., Ltd</font>**
URL: canaan-creative.com
Geschäftliche Anfragen: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# Vorwort
**<font face="黑体"  size=5>Zweck des Dokuments</font>**
Dieses Dokument ist ein erläuterndes Dokument für das Anwendungsbeispiel K510 V4L2.

**<font face="黑体"  size=5>Reader-Objekte</font>**

Die wichtigsten Personen, für die sich dieses Dokument (dieser Leitfaden) richtet:

- Softwareentwickler
- Mitarbeiter des technischen Supports

**<font face="黑体"  size=5>Revisionshistorie</font>**
 <font face="宋体"  size=2>In der Revisionshistorie wird eine Beschreibung jeder Dokumentaktualisierung gesammelt. Die neueste Version des Dokuments enthält Updates für alle vorherigen Versionen. </font>

| Die Versionsnummer   | Geändert von     | Datum der Überarbeitung | Revisionshinweise |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | Systemsoftwaregruppen | 2022-03-09 | SDK V1.5 veröffentlicht |
| v1.0.1 | Zhu Dalei | 2022-03-11 | SDK V1.5 veröffentlicht |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Inhalt</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 V4L2 Mediaktl-Bibliothek

## 1.1 Beschreibung der Header-Datei

\#include "media_ctl.h"

## 1.2 API-Funktionsbeschreibungen

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

Initialisieren Sie Medien.

#### Parameter

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

#### Der Rückgabewert

```text
0 成功,  -1 失败.
```

### ◆ mediactl_exit

Fahren Sie das Mediengerät herunter und geben Sie den angeforderten Speicher für die gemeinsame Nutzung frei.

#### Parameter

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

Konfigurieren des AE-Werts des Sensors

#### Parameter

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

Ruft den Aktivierungsstatus jedes Moduls des ISP ab.

#### Parameter

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

#### Der Rückgabewert

```text
0 -- 模块没有使能  1 -- 模块使能 
```

# 2 Demo-App

## 2.1 v4l2_drm

Das Programm befindet sich`/app/mediactl_lib` im Verzeichnis:

- `v4l2_drm.out`:v4l2 und DRM-Verknüpfungsfall, Hinzufügen von -f, um den Namen der Eingabekonfigurationsdatei zu ändern, -e, um die ISP AE-Funktion zu öffnen. Sie können -h verwenden, um die Hilfe anzuzeigen.

Ausführen von v4l2_drm.out

- -E: 0 schaltet alle AEs, 1 Umdrehungen auf F-2K AE, 2 Umdrehungen auf R-2K AE und 3 Umdrehungen auf alle AEs aus. Standardmäßig können Sie -e belassen, um alle AES zu deaktivieren.
- Die Demo setzt voraus, dass sich die Videokonfigurationsdatei und die entsprechende Sensorkonfigurationsdatei im aktuellen Verzeichnis befinden.
- Die Demo kann Einzel- und Doppelkameras demonstrieren, indem die Konfigurationsdatei geändert wird.
- Die Demo Demo Einzelkamera Vollbild: ./v4l2_drm.out -e 1 -f video_drm_1080x1920.conf
- Die Demo Demo Dual-Kamera: ./v4l2_drm.out -f video_drm_1920x1080.conf
- Die Demo muss sicherstellen, dass drei Profile video_drm_1920x1080.conf, imx219_0.conf und imx219_1.conf vorhanden sind

**Haftungsausschluss**für Übersetzungen  
Für die Bequemlichkeit der Kunden verwendet Canaan einen KI-Übersetzer, um Text in mehrere Sprachen zu übersetzen, die Fehler enthalten können. Wir übernehmen keine Gewähr für die Genauigkeit, Zuverlässigkeit oder Aktualität der bereitgestellten Übersetzungen. Canaan haftet nicht für Verluste oder Schäden, die durch das Vertrauen auf die Richtigkeit oder Zuverlässigkeit der übersetzten Informationen verursacht werden. Wenn es einen inhaltlichen Unterschied zwischen den Übersetzungen in verschiedenen Sprachen gibt, ist die vereinfachte chinesische Version maßgebend.

Wenn Sie einen Übersetzungsfehler oder eine Ungenauigkeit melden möchten, können Sie uns gerne per E-Mail kontaktieren.
