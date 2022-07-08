![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 V4L2 Podręcznik programisty</font>**

<font face="黑体"  size=3>Wersja dokumentu: V1.0.0</font>

<font face="黑体"  size=3>Opublikowano: 2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Zrzeczenie się**</font>
Zakupione produkty, usługi lub funkcje podlegają umowom handlowym i warunkom Beijing Canaan Jiesi Information Technology Co., Ltd. ("Spółka", ta sama poniżej), a wszystkie lub część produktów, usług lub funkcji opisanych w niniejszym dokumencie może nie być objęta zakresem zakupu lub użytkowania. O ile nie uzgodniono inaczej w umowie, Firma zrzeka się wszelkich oświadczeń lub gwarancji, wyraźnych lub dorozumianych, co do dokładności, niezawodności, kompletności, marketingu, konkretnego celu i nieagresji jakichkolwiek oświadczeń, informacji lub treści tego dokumentu. O ile nie uzgodniono inaczej, niniejszy dokument jest dostarczany jako wskazówka wyłącznie do użytku.
Ze względu na aktualizacje wersji produktu lub z innych powodów zawartość tego dokumentu może być od czasu do czasu aktualizowana lub modyfikowana bez powiadomienia. 

**<font face="黑体"  size=3>Informacje o znakach towarowych</font>**

""<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, ikona "Canaan", Canaan i inne znaki towarowe Canaan oraz inne znaki towarowe Canaan są znakami towarowymi Beijing Canaan Jiesi Information Technology Co., Ltd. Wszystkie inne znaki towarowe lub zarejestrowane znaki towarowe, które mogą być wymienione w niniejszym dokumencie, są własnością ich odpowiednich właścicieli. 

**<font face="黑体"  size=3>Prawa autorskie ©2022 Beijing Canaan Jiesi Information Technology Co., Ltd</font>**
Niniejszy dokument ma zastosowanie wyłącznie do rozwoju i projektowania platformy K510, bez pisemnej zgody firmy, żadna jednostka ani osoba fizyczna nie może rozpowszechniać części lub całości treści tego dokumentu w jakiejkolwiek formie. 

**<font face="黑体"  size=3>Pekin Canaan Jiesi Information Technology Co Ltd</font>**
Adres internetowy: canaan-creative.com
Zapytania biznesowe: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# przedmowa
**<font face="黑体"  size=5>Przeznaczenie </font>**dokumentu
Niniejszy dokument jest dokumentem wyjaśniającym przykład zastosowania K510 V4L2. 

**<font face="黑体"  size=5>Obiekty programu Reader</font>**

Główne osoby, których dotyczy ten dokument (ten przewodnik):

- Programiści
- Personel wsparcia technicznego

**<font face="黑体"  size=5>Historia</font>**
 zmian <font face="宋体"  size=2>Historia zmian gromadzi opis każdej aktualizacji dokumentu. Najnowsza wersja dokumentu zawiera aktualizacje dla wszystkich poprzednich wersji. </font>

| Numer wersji   | Zmodyfikowane przez     | Data aktualizacji | Uwagi do poprawek |
|  :-----  |-------   |  ------  |  ------  |
| Wersja 1.0.0 | Grupy oprogramowania systemowego | 2022-03-09 | SDK V1.5 wydany |
| Wersja 1.0.1 | Zhu Dalei | 2022-03-11 | SDK V1.5 wydany |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Treść</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 biblioteka multimedialna V4L2

## 1.1 Opis pliku nagłówka

\#include "media_ctl.h"

## 1.2 Opisy funkcji API

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

Inicjowanie multimediów.

#### parametr

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

#### Zwracana wartość

```text
0 成功,  -1 失败.
```

### ◆ mediactl_exit

Wyłącz urządzenie multimedialne i zwolnij żądaną pamięć współdzieloną.

#### parametr

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

Konfigurowanie wartości AE czujnika

#### parametr

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

Pobiera stan włączenia każdego modułu usługodawcy internetowego.

#### parametr

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

#### Zwracana wartość

```text
0 -- 模块没有使能  1 -- 模块使能 
```

# 2 Aplikacja demonstracyjna

## 2.1 v4l2_drm

Program umieszczony jest`/app/mediactl_lib` w katalogu:

- `v4l2_drm.out`:v4l2 i drm linkage case, dodano -f, aby zmodyfikować nazwę wejściowego pliku konfiguracyjnego, -e, aby otworzyć funkcję isp ae. Możesz użyć -h, aby wyświetlić pomoc.

Uruchom v4l2_drm.out

- -e:0 wyłącza wszystkie aes, 1 włącza f-2k ae, 2 włącza r-2k ae, a 3 włącza wszystkie aes. Domyślnie możesz zostawić -e, aby wyłączyć wszystkie aes.
- Demo wymaga, aby plik konfiguracyjny wideo i odpowiadający mu plik konfiguracyjny czujnika znajdowały się w bieżącym katalogu.
- Demo może zademonstrować pojedynczą i podwójną kamerę, zmieniając plik konfiguracyjny.
- Demo z jedną kamerą na pełnym ekranie: ./v4l2_drm.out -e 1 -f video_drm_1080x1920.conf
- Demo podwójnej kamery: ./v4l2_drm.out -f video_drm_1920x1080.conf
- Pokaz musi zapewniać istnienie trzech profili video_drm_1920x1080.conf, imx219_0.conf i imx219_1.conf

**Zrzeczenie się odpowiedzialności za **tłumaczenie  
Dla wygody klientów Canaan używa tłumacza AI do tłumaczenia tekstu na wiele języków, które mogą zawierać błędy. Nie gwarantujemy dokładności, rzetelności ani terminowości dostarczonych tłumaczeń. Canaan nie ponosi odpowiedzialności za jakiekolwiek straty lub szkody spowodowane poleganiem na dokładności lub wiarygodności przetłumaczonych informacji. W przypadku różnic w treści tłumaczeń w różnych językach, pierwszeństwo ma chińska wersja uproszczona. 

Jeśli chcesz zgłosić błąd lub niedokładność tłumaczenia, skontaktuj się z nami pocztą.