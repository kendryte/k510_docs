![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 SDK-toepassingshandleiding</font>**

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
Dit document is een beschrijvingsdocument voor het voorbeeld van de K510 SDK-toepassing.

**<font face="黑体"  size=5>Reader Objecten</font>**

De belangrijkste personen op wie dit document (deze gids) van toepassing is:

- Softwareontwikkelaars
- Technisch ondersteunend personeel

**<font face="黑体"  size=5>Revisiegeschiedenis</font>**
 <font face="宋体"  size=2>De revisiegeschiedenis bevat een beschrijving van elke documentupdate. De nieuwste versie van het document bevat updates voor alle voorgaande versies. </font>

| Het versienummer | Gewijzigd door     | Datum van herziening   | Opmerkingen bij herziening     |
| :----- | ---------- | ---------- | ------------ |
| V1.0.0 | Systeemsoftwaregroepen | 2022-03-09 | SDK V1.5 vrijgegeven |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Inhoud</font>**

[INHOUDSOPGAVE]

<div style="page-break-after:always"></div>

# 1 Demo-app

## 1.1 ai demo programma

### 1.1.1 Beschrijving

De broncode van het demoprogramma van nncase bevindt zich in de map onder de SDK-map`package/ai` en de mapstructuur is als volgt:

```shell
$ tree -L 2 ai
ai
├── ai.hash
├── ai.mk
├── code
│   ├── build.sh
│   ├── cmake
│   ├── CMakeLists.txt
│   ├── common
│   ├── face_alignment
│   ├── face_detect
│   ├── face_expression
│   ├── face_landmarks
│   ├── face_recog
│   ├── hand_image_classify
│   ├── head_pose_estimation
│   ├── imx219_0.conf
│   ├── imx219_1.conf
│   ├── license_plate_recog
│   ├── object_detect
│   ├── object_detect_demo
│   ├── openpose
│   ├── person_detect
│   ├── retinaface_mb_320
│   ├── self_learning
│   ├── shell
│   ├── simple_pose
│   ├── video_192x320.conf
│   ├── video_object_detect_320.conf
│   ├── video_object_detect_320x320.conf
│   ├── video_object_detect_432x368.conf
│   ├── video_object_detect_512.conf
│   ├── video_object_detect_640.conf
│   └── video_object_detect_640x480.conf
└── Config.in
```

U kunt de broncode van de retinaface_mb_320 raadplegen en`CMakeLists.txt` een nieuw nncase-demoprogramma toevoegen.

Voor de samenstelling van het model, zie`nncase_demo.mk` de daarin *gedefinieerde POST_INSTALL_TARGET_HOOKS*:

```text
NNCASE_DEMO_DEPENDENCIES += mediactl_lib nncase_linux_runtime opencv4 libdrm
define NNCASE_DEMO_COMPILE_MODEL
    mkdir -p $(TARGET_DIR)/app/ai/kmodel/kmodel_compile/retinaface_mb_320
    cd $(@D) && /usr/bin/python3 retinaface_mb_320/rf_onnx.py --quant_type uint8 --model ai_kmodel_data/model_file/retinaface/retinaface_mobile0.25_320.onnx
    cp $(@D)/rf.kmodel $(TARGET_DIR)/app/ai/kmodel/kmodel_compile/retinaface_mb_320/rf_uint8.kmodel
    cd $(@D) && /usr/bin/python3 retinaface_mb_320/rf_onnx.py --quant_type bf16 --model ai_kmodel_data/model_file/retinaface/retinaface_mobile0.25_320.onnx
    cp $(@D)/rf.kmodel $(TARGET_DIR)/app/ai/kmodel/kmodel_compile/retinaface_mb_320/rf_bf16.kmodel

NNCASE_DEMO_POST_INSTALL_TARGET_HOOKS += NNCASE_DEMO_COMPILE_MODEL
```

De compilatie van het model vereist een nncase-omgeving en voor de constructie van de nncase-omgeving, raadpleeg k510_nncase_Developer_Guides.md. In de toekomst heeft de nncase een update en wordt de buildroot sdk synchroon bijgewerkt naar de nncase.

### 1.1.2 netvlies

Functie: Gezichtsherkenning, gezichtsherkenning

Programma Pad:
`/app/ai/shell`
Rennen:
Een niet-kwantitatief model `./retinaface_mb_320_bf16.sh`uitvoeren
Voer het uint8-kwantisatiemodel uit,`./retinaface_mb_320_uint8.sh`

Er zijn instellingen voor QOS in het script, hetzelfde als voor de volgende twee demo's.

```shell
#devmem phyaddr width value
devmem 0x970E00fc 32 0x0fffff00
devmem 0x970E0100 32 0x000000ff
devmem 0x970E00f4 32 0x00550000
```

Bij het uitvoeren van een demo is het noodzakelijk om ervoor te zorgen dat de schermweergave normaal is, dat wil zeggen, de QoS met betrekking tot het scherm aanpassen aan een hoge prioriteit.
QOS_CTRL0.ax25mp QoS schrijven = 5
QOS_CTRL0.ax25mp lezen QoS = 5
QOS_CTRL2.ispf2k QoS schrijven = 0xf
QOS_CTRL2.ispf2k lezen QoS = 0xf
QOS_CTRL2.ispr2k QoS schrijven = 0xf
QOS_CTRL2.ispr2k lezen QoS = 0xf
QOS_CTRL2.isp3dtof QoS = 0xf schrijven
QOS_CTRL3.display QoS lezen = 0xf
QOS_CTRL3.display QoS schrijven = 0xf

QOS-controleregister 0(QOS_CTRL0)offset[0x00f4]
 ![QOS Ctrl0](../zh/images/sdk_application/demo_nncase_qos_ctrl0.png)

QOS-besturingsregister 1 (QOS_CTRL1) offset[0x00f8]
 ![QOS Ctrl1](../zh/images/sdk_application/demo_nncase_qos_ctrl1.png)

QOS-besturingsregister 2 (QOS_CTRL2) offset[0x00fc]
 ![QOS Ctrl2](../zh/images/sdk_application/demo_nncase_qos_ctrl2.png)

QOS-controleregister 3 (QOS_CTRL3) offset[0x0100]
 ![QOS Ctrl3](../zh/images/sdk_application/demo_nncase_qos_ctrl3.png)

De compilatie en installatie van het model wordt gedetailleerd beschreven in het bestandspakket/ai/ai.mk:

Scriptpad compileren:
pakket/ai/code/retinaface_mb_320/rf_onnx.py

### 1.1.3 object_detect

Functie: Objectclassificatiedetectie, 80-classificatie

Programma Pad:`/app/ai/shell`

Rennen:
Een niet-kwantitatief model `./object_detect_demo_bf16.sh`uitvoeren
Voer het uint8-kwantisatiemodel uit,`./object_detect_demo_uint8.sh`

De compilatie en installatie van het model wordt gedetailleerd beschreven in het bestandspakket/ai/ai.mk

Scriptpad compileren:
pakket/ai/code/object_detect_demo/od_onnx.py

## 1,2 ffmpeg

`ffmpeg``ffmpeg-4.4`Geporteerd op open source code, toegevoegd`0001-buildroot-ffmpeg-0.1.patch` voor servicepacks

- `ff_k510_video_demuxer`: Regelt de internetprovider waarnaar wordt verwezen`libvideo.so`
- `ff_libk510_h264_encoder`: Controle h264 hardware codering, waarnaar wordt verwezen`libvenc.so`

Configureerbare parameters kunnen worden bekeken via de help-instructie

```shell
ffmpeg -h encoder=libk510_h264 #查看k510编码器的参数
ffmpeg -h demuxer=libk510_video #查看demuxer的配置参数
```

Voor gedetailleerde uitvoeringsinstructies raadpleegt u[K510_Multimedia_Developer_Guides.md](./K510_Multimedia_Developer_Guides.md)

## 1.3 alsa_demo

Het alsa demo programma wordt in `/app/alsa_demo`de directory geplaatst :

Run voorbereiding:
(1) Sluit de hoofdtelefoon aan

Voer alsa demo uit:

```shell
cd /app/alsa_demo/
./alsa_demo c #录音到文件capture.pcm，demo程序仅作参考，可以参考package/alsa_demo的源码。
./alsa_demo p #播放capture.pcm
```

## 1.4 TWOD-demo

Hoe rotatie uit te voeren:

```shell
cd /app/twod_app
./twod-rotation-app
```

Kopieer de uitvoer .yuv naar de YUV-monitor en stel de grootte 1080 x 1920 in, weergaveformaat nv12, het resultaat is als volgt
![uitgang.yuv](../zh/images/sdk_application/driver-twod-output-1080x1920.jpg)

Scaler gebruiken

```shell
cd /app/twod_app
./twod-scaler-app
```

Kopieer de uitvoer .yuv naar de YUV-monitor en stel de grootte 640x480 in, weergaveformaat nv12, het resultaat is als volgt
![ouput.yuv](../zh/images/sdk_application/driver-twod-output-640x480.jpg)

Hoe rgb2yuv uit te voeren:

```shell
cd /app/twod_app
./twod-osd2yuv-app
```

Kopieer de uitvoer .yuv naar de YUV-monitor en stel de grootte 320x240 in, weergaveformaat nv12, het resultaat is als volgt
![ouput.yuv](../zh/images/sdk_application/twod-osd2yuv-app.jpg)

Voer yuv2rgb gebruik uit:

```shell
cd /app/twod_app
./twod-scaler-output-rgb888-app
```

Kopieer de uitvoer .yuv naar de rgb888-monitor en stel de grootte 640x480 in, het weergaveformaat rgb24, het resultaat is als volgt
![ouput.yuv](../zh/images/sdk_application/driver-twod-output-640x480.jpg)

Voer output yuv uit op overlay osd gebruik:

```shell
cd /app/twod_app
./twod-scaler-overlay-osd-app
```

Kopieer de uitvoer .yuv naar de monitor om de grootte 640x480 in te stellen, weergaveformaat nv12, het resultaat is als volgt
![ouput.yuv](../zh/images/sdk_application/twod-scaler-overlay-osd-app.jpg)

API:

```c
/* 创建内存 */
twod_create_fb()
/* 配置原图片参数 */   
twod_set_src_picture()
/* 配置输出图片参数 */ 
twod_set_des_picture()
/* 设置 scaler */     
twod_set_scaler()
/* 等待操作完成 */     
twod_wait_vsync()
/* Invali cache */   
twod_InvalidateCache()
/* flash cache */     
twod_flashdateCache()
/* 释放内存*/     
twod_free_mem()
/* 设置旋转 */  
twod_set_rot()
```

## 1.5 RTC-demo

Het RTC-stuurprogramma registreert het apparaatknooppunt build /dev/rtc0.

De toepassingslaag volgt de standaard RTC-programmeermethode in het Linux-systeemaanroepstuurprogramma en het wordt aanbevolen om het afdrukken van kernelinformatie via de shellconsole uit te schakelen voordat u de referentieroutine uitvoert.

```shell
echo 0 > /proc/sys/kernel/printk
```

Ga naar de map /app/rtc en voer de volgende opdracht in om de rtc-toepassing te starten.

```shell
cd /app/rtc
./rtc 2021-11-3 21:10:59
```

Het resultaat van de uitvoering van het programma is:

![](../zh/images/sdk_application/image-rtc.png)

Het belangrijkste codefragment van het RTC-demoprogramma is als volgt, raadpleeg de code onder de map package / rtc voor meer informatie.

```c
/*解析参数，获取当前年月日、时分秒*/
if(argc !=3) {
    fprintf(stdout, "useage:\t ./rtc year-month-day hour:minute:second\n");
    fprintf(stdout, "example: ./rtc 2021-10-11 19:54:30\n");
    return -1;
}

sscanf(argv[1], "%d-%d-%d",  &year, &month, &day);
sscanf(argv[2], "%d:%d:%d",  &hour, &minute, &second);

/*打开RTC设备，设备节点是：/dev/rtc0 */
fd = open("/dev/rtc0", O_RDONLY);
if (fd == -1) {
    perror("/dev/rtc0");
    exit(errno);
}

/* 设置RTC时间。*/
retval = ioctl(fd, RTC_SET_TIME, &rtc_tm);
if (retval == -1) {
    perror("ioctl");
    exit(errno);
}

/* 休眠 2秒。 */
sleep(2);

/* 读取RTC当前时间。*/
retval = ioctl(fd, RTC_RD_TIME, &rtc_tm);
if (retval == -1) {
    perror("ioctl");
    exit(errno);
}

/* 打印 RTC当前时间。*/
fprintf(stdout, "\nRTC date/time: %d/%d/%d %02d:%02d:%02d\n",
        rtc_tm.tm_mday, rtc_tm.tm_mon + 1, rtc_tm.tm_year + 1900,
        rtc_tm.tm_hour, rtc_tm.tm_min, rtc_tm.tm_sec);
```

## 1.6 WDT-demo

De K510 heeft in totaal drie waakhonden en de WDT-driver registreert de apparaatknooppunten generate /dev/watchdog0, /dev/watchdog1, /dev/watchdog2.

De toepassingslaag volgt de standaard WDT-programmeermethode in het Linux-systeemaanroepstuurprogramma, de eerste parameter van de wathdog-toepassing kan respectievelijk 0, 1, waakhond0, waakhond1 vertegenwoordigen, de tweede parameter vertegenwoordigt de time-outtijd (eenheidsseconden) die kan worden ingesteld, bijvoorbeeld het volgende commando geeft het begin van waakhond0 aan, waakhond0 overlooptijd van 40 seconden.

```shell
cd /app/watchdog
./watchdog 0 40
```

Nadat het programma is gestart, zal het de waakhond elke 1 seconde met tussenpozen voeden, wanneer het stopteken in de shell-terminal wordt ingevoerd, de applicatie stopt met het voeren van de hond en de waakhond het apparaat opnieuw opstart nadat de time-out van de instelling overloopt, raadpleegt u de code onder de map pakket / waakhond voor meer informatie.

Het resultaat van de uitvoering van het programma is:

![](../zh/images/sdk_application/image-watchdog.png)

**Opmerking**: De huidige k510-waakhondmodule heeft een werkende klokfrequentie van 757575Hz en de time-outtijd in seconden moet worden geconverteerd naar de time-out time-out van de werkelijke werkklokfrequentie van de waakhond, die wordt berekend als 2 ^ n / 757575, dus de werkelijke time-outtijd is groter dan of gelijk aan de time-out time-out voor invoer.

De werkelijke time-outperiode wordt als volgt berekend:

1) Voer 40, 2 ^ 25 / 757575 = 44 > 40, 2 ^ 24 / 757575 = 22 < 40 in, dus het is ingesteld op 44 seconden;

2) Voer 155, 2 ^ 27 / 757575 = 177 > 155 in, dus het is ingesteld op 177 seconden;

3) Voer 2000, 2 ^ 31/757575 = 2834 > 2000 in, dus het is ingesteld op 2834 seconden;

## 1.7 UART-demo

K510 heeft in totaal 4 seriële poorten, de huidige driver in de seriële poorten 2, 3 is niet ingeschakeld, seriële poort 0 driver zal registreren om /dev/ttyS0 apparaatknooppunten te genereren.

De toepassingslaag volgt de standaard UART-programmeermethode in het Linux-systeemaanroepstuurprogramma. De eerste parameter van de uart-toepassing kan 0 en 1 zijn, die respectievelijk uart0 en uart1 vertegenwoordigen.

De ontwikkelkaart maakt gebruik van een bekabeld netwerk om verbinding te maken met de router, zodat de ontwikkelingskaart en de foutopsporings-pc in een netwerk, wanneer de ontwikkelingskaart is ingeschakeld, automatisch het IP-adres verkrijgt, de ifconfig-opdracht invoert in de shell seriële terminal van de ontwikkelingskaart om het IP-adres te verkrijgen, en de foutopsporings-pc gebruikt dit IP-adres om een telentvenster te openen door het ontwikkelingsbord via de telentverbinding aan te sluiten. De bewerking van het debuggen van een pc om een ontwikkelbord aan te sluiten met behulp van telent via MobaXterm wordt bijvoorbeeld weergegeven in de volgende afbeelding.

![](../zh/images/sdk_application/image-uart-mobaxterm.png)

Voer de volgende opdracht in het telentterminalvenster in om seriële poort 0-werk te starten.

```shell
cd /app/uart
./uart 0
```

Voer de inhoud in die u wilt verzenden in het telentvenster, u kunt de ontvangen gegevens zien in het shell seriële terminalvenster, raadpleeg de code onder de map package / crb_demo / uart voor meer informatie.
Bijvoorbeeld de ingang voor het telentvenster:

![](../zh/images/sdk_application/image-uart-telent.png)

Het bijbehorende Shell seriële terminalvenster toont:

![](../zh/images/sdk_application/image-uart-shell.png)

## 1.8 ETH-demo

De toepassingslaag volgt het standaard ETH-aanroepstuurprogramma voor programmeermethoden in Linux-systemen.

### 1.8.1 Klant

Het apparaat als de client, voer de map /app/client in, voer de volgende opdracht in om de clienttoepassing te starten, de eerste parameter van de ETH-toepassing geeft het IP-adres van de server aan om de TCP-koppeling tot stand te brengen, voer bijvoorbeeld de volgende opdracht in om het ETH-programma te starten en 10.20.1.13-server om communicatie tot stand te brengen.

```shell
cd /app/client
./client 10.20.1.13
```

Verbind de server om te communiceren via het TCP-protocol, voer het serverprogramma uit op een andere Ubuntu-machine, raadpleeg de map package / app / client voor meer informatie.

Logboeken aan de kant van het apparaat weergeven:

![](../zh/images/sdk_application/image-client.png)

### 1.8.2. Server

Het apparaat voert de map /app/server in als de server, bijvoorbeeld de volgende opdracht invoert om het serverprogramma te starten.

```shell
cd /app/server
./server
```

Voer het clientprogramma uit op een andere Ubuntu-machine, verbind de server via het tcp-protocol om te communiceren, raadpleeg voor meer informatie de map package / crb_demo / server.

Logboeken aan de kant van het apparaat weergeven:

 ![](../zh/images/sdk_application/image-server.png)

## 1.9 SDMMC demo

De K510 heeft in totaal 3 SDMMC-hoofdcontrollers, de ontwikkelingskaart SDMMC0 wordt gebruikt om eMMC aan te sluiten, SDMMC1 wordt gebruikt voor WIFI-modules en de SDMMC2-controller wordt gebruikt om sdcards aan te sluiten.

Het SDMMC-stuurprogramma registreert om /dev/mmcblk0 te genereren en het EMMC-stuurprogramma registreert als het apparaatknooppunt /dev/mmcblk1.

SD-kaart wordt automatisch gekoppeld aan / root / data na het opstarten van het systeem, voer de map /app/write_read_file in, de eerste parameter van de SDMMC-toepassing geeft aan welk bestand moet worden gelezen en geschreven, zoals sd-kaart gekoppeld aan /root/data, u kunt bestanden lezen en schrijven onder de map /root/data/, eerst schrijven en dan lezen, Voer de volgende opdracht in om de SDMMC-toepassing te starten om naar de SD-kaart te lezen en te schrijven en de lees- en schrijfsnelheid (eenheid m/s) te berekenen.

```shell
cd /app/write_read_file
./write_read_file /root/data/test.txt
```

Om het lezen en schrijven van 1G-gegevens naar de SD-kaart mogelijk te maken, raadpleegt u de map / app / write_read_file map.

![](../zh/images/sdk_application/image-sdmmc.png)

## 1.10 SHA/AES-demo

SHA/AES demo gebruikt de Linux kernel om AF_ALG type Netlink interface te exporteren en gebruikt de kernel encryptie API in de gebruikersruimte. Zie .<https://www.kernel.org/doc/html/latest/crypto/userspace-if.html>

Parameter:
-h Drukt de helpinformatie af
-t algoritme type: hash, skcipher
-n Algoritme namen: sha256, ecb(aes), cbc(aes)
-x decoderingsbewerking
-k AES KEY (hexadecimale string)
-v AES IV (hexadecimale string)

![](../zh/images/sdk_application/image_crypto_help.png)

sha256 test:

```shell
cd /app/crypto
echo -n "This is a test file, hello world" > plain.txt
./crypto -t hash -n "sha256" plain.txt sha256.txt
xxd -p -c 32 sha256.txt
sha256sum plain.txt
```

![](../zh/images/sdk_application/image_crypto_sha256.png)

ECB(aes) 128-test:

```shell
cd /app/crypto
echo -n "This is a test file, hello world" > plain.txt
./crypto -t skcipher -n "ecb(aes)" -k 00112233445566778899aabbccddeeff plain.txt ecb_aes_en.bin
./crypto -t skcipher -n "ecb(aes)" -k 00112233445566778899aabbccddeeff  -x ecb_aes_en.bin ecb_aes_de.bin
cmp ecb_aes_de.bin plain.txt
cat ecb_aes_de.bin
```

![](../zh/images/sdk_application/image_crypto_ecb.png)

cbc(aes) 128-test

```shell
cd /app/crypto
echo -n "This is a test file, hello world" > plain.txt
./crypto -t skcipher -n "cbc(aes)" -k 00112233445566778899aabbccddeeff -v 00112233445566778899aabbccddeeff plain.txt cbc_aes_en.bin
./crypto -t skcipher -n "cbc(aes)" -k 00112233445566778899aabbccddeeff -v 00112233445566778899aabbccddeeff -x cbc_aes_en.bin cbc_aes_de.bin
cmp cbc_aes_de.bin plain.txt
cat cbc_aes_de.bin
```

![](../zh/images/sdk_application/image_crypto_cbc.png)

AES-ECB-128 en aes-cbc-128 encryptie vereisen 16-byte uitlijning van de platte tekst, en de onvoldoende wordt automatisch gevuld met 0.

## 1.11 TRNG-demo

De TRNG-demo produceert een willekeurig getal van de opgegeven lengte door het /dev/hwrng-tekenapparaat te lezen, uitgevoerd als een hexadecimale tekenreeks.

De ingangsparameter betekenis van ./trng:

-h Drukt de helpinformatie af

-b Hiermee geeft u de lengte van het willekeurige getal van de uitvoer op, in bytes

![](../zh/images/sdk_application/image_trng.png)

## 1.12 DRM-demo

Drm-demo demonstreert de vo hardware multi-layer mogelijkheden.

Vo heeft in totaal 8 lagen:

1) Achtergrondlaag, kan worden geconfigureerd achtergrondkleur.

2) Layer0 is een videolaag, ondersteunt YUV422 en YUV420, ondersteunt NV12- en NV21-formaten, kan aan de groottekant worden afgestemd en ondersteunt hardware die op- en afschaalt.

3) Layer1-layer3 is een videolaag, die YUV422 en YUV420 ondersteunt, NV12- en NV21-formaten ondersteunt en de groottezijde kan worden afgestemd.

4) Layer4-layer6 is de OSD-laag die meerdere ARGB-formaten ondersteunt.

Nadat het bord is gestart, voert u de map /app/drm_demo in en voert u de opdracht in:

```shell
cd /app/drm_demo
./drm_demo
```

Start drm_demo applicatie drm_demo weergegeven:

![](../zh/images/sdk_application/image_drm_demo.png)

## 1.13 V4L2_DRM demo

v4l2_drm demo demonstreert de functionaliteit van camera-invoer en weergave.

Nadat het bord is gestart, voert u de map /app/mediactl_lib in en voert u de opdracht in:

```shell
cd /app/mediactl_lib
./v4l2_drm.out -f video_drm_1080x1920.conf -e 1
或者
./v4l2_drm.out -f video_drm_1920x1080.conf
```

Start de v4l2_drm.out applicatie en v4l2_drm.out display:

![](../zh/images/sdk_application/image_v4l2_drm_demo.png)

## 1,14 LVGL-demo

Ga naar /app/lvgl en voer de volgende opdracht uit:

```shell
cd /app/lvgl
./lvgl
```

Het weergave-effect is als volgt:![](../zh/images/sdk_application/image_lvgl.png)

## 1,15 PWM-demo

Het PWM-stuurprogramma registreert de apparaatknooppunten generate /sys/class/pwm/pwmchip0 en /sys/class/pwm/pwmchip3.

Dit voorbeeld kan worden geconfigureerd en ingeschakeld voor respectievelijk pwm0 en pwm1, in de map /app/pwm, de eerste parameter van de pwm-toepassing geeft de periode aan van het instellen van pwm, de eenheid is ns, de tweede parameter stelt de tijd van "ON" in een cyclus van pwm in, de eenheid is ns, de derde parameter kan 0, 1 zijn, die pwm0 en pwm1 vertegenwoordigt, voer bijvoorbeeld het volgende commando in om pwm0 in te schakelen, de cyclus is 1s, de duty cycle is 100000000/ 500000000* 100% = 50%, raadpleeg de map / app / pwm-map voor gedetailleerde codes.

```shell
cd /app/pwm
./pwm 1000000000 500000000 0
```

Het resultaat van de uitvoering van het programma is:

![](../zh/images/sdk_application/image-pwm.png)

Door pin 28 van de K510 CRB1.2 development board J15 door de oscilloscoop te verbinden, kan een golfvormpatroon met een periode van 1 seconde en een duty cycle van 50% worden waargenomen op de oscilloscoop.

## 1,16 WIFI demo

Nadat het stuurprogramma van de WiFi-module is geladen, wordt de draadloze netwerkkaart wlan0 gegenereerd, die het standaard netwerkpoortstuurprogramma volgt en normaal gesproken verwijst naar TCP / IP-socketprogrammering.

1) Open "Mobile Hotspot" in het notitieblok en stel vervolgens de naam en het wachtwoord van de hotspot in
2) Start NetAssist op de notebook, configureer het protocoltype, het lokale host-IP-adres, de lokale hostpoort, de ontvangstinstellingen, de verzendinstellingen en de gegevens die moeten worden verzonden, zoals weergegeven in de volgende afbeelding:

    ![](../zh/images/sdk_application/image_wifi_1.png)

3) Het parameterformaat van het wifi-testprogramma is:

    ```shell
    ./wifi <AP name> <password> <local ip> <server ip>
    ```

    Voer bijvoorbeeld de map /app/wifi in, voer de opdracht in om het wifi-testprogramma te starten en het uitvoeringsresultaat van het programma is als volgt:

    ![](../zh/images/sdk_application/image_wifi_2.png)

## 1,17 GPIO_KEYS demo

Het belangrijkste stuurprogramma gebruikt de Linux-kernel zelf geïntegreerd met de generieke gpu-keys driver op basis van het invoersubsysteem, en nadat het stuurprogramma is geladen, wordt het gebeurtenisbewakingsknooppunt eventX gegenereerd in de map /dev/input en X is het volgnummer van het gebeurtenisknooppunt, dat kan worden bekeken via cat /proc/bus/input/devices

gpio-keys routine blokkeert het lezen van belangrijke rapportagegebeurtenissen en het afdrukken van gebeurtenisinformatie, de informatie omvat sleutelcodering en toetsactie, sleutelcode om de sleutelidentiteit te identificeren, toetsactie is verdeeld in ingedrukt en vrijgegeven, in de sleutelrelease wanneer de routine de duur van het indrukken van de toets berekent

Het resultaat van de uitvoering van het programma wordt weergegeven in de volgende afbeelding:![](../zh/images/sdk_application/image-gpio-keys.png)

**Vertaling Disclaimer**  
Voor het gemak van klanten gebruikt Canaan een AI-vertaler om tekst in meerdere talen te vertalen, wat fouten kan bevatten. Wij garanderen niet de nauwkeurigheid, betrouwbaarheid of tijdigheid van de geleverde vertalingen. Canaan is niet aansprakelijk voor enig verlies of schade veroorzaakt door het vertrouwen op de nauwkeurigheid of betrouwbaarheid van de vertaalde informatie. Als er een inhoudelijk verschil is tussen de vertalingen in verschillende talen, prevaleert de vereenvoudigd Chinese versie.

Als u een vertaalfout of onnauwkeurigheid wilt melden, neem dan gerust contact met ons op via e-mail.
