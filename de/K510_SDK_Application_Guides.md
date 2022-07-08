![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 SDK-Anwendungshandbuch</font>**

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
Dieses Dokument ist ein Beschreibungsdokument für das Anwendungsbeispiel K510 SDK. 

**<font face="黑体"  size=5>Reader-Objekte</font>**

Die wichtigsten Personen, für die sich dieses Dokument (dieser Leitfaden) richtet:

- Softwareentwickler
- Mitarbeiter des technischen Supports

**<font face="黑体"  size=5>Revisionshistorie</font>**
 <font face="宋体"  size=2>In der Revisionshistorie wird eine Beschreibung jeder Dokumentaktualisierung gesammelt. Die neueste Version des Dokuments enthält Updates für alle vorherigen Versionen. </font>

| Die Versionsnummer | Geändert von     | Datum der Überarbeitung   | Revisionshinweise     |
| :----- | ---------- | ---------- | ------------ |
| V1.0.0 | Systemsoftwaregruppen | 2022-03-09 | SDK V1.5 veröffentlicht |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Inhalt</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Demo-App

## 1.1 KI-Demoprogramm

### 1.1.1 Beschreibung

Der Quellcode des Demo-Programms von nncase befindet sich im Verzeichnis unter dem SDK-Verzeichnis`package/ai`, und die Verzeichnisstruktur ist wie folgt:

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

Sie können sich auf den Quellcode der retinaface_mb_320 beziehen und`CMakeLists.txt` ein neues nncase-Demoprogramm hinzufügen. 

Für die Zusammenstellung des Modells siehe`nncase_demo.mk` die *darin definierten *POST_INSTALL_TARGET_HOOKS:

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

Für die Zusammenstellung des Modells ist eine nncase-Umgebung erforderlich, und Informationen zum Erstellen der nncase-Umgebung finden Sie in k510_nncase_Developer_Guides.md. In Zukunft hat das nncase ein Update, und das buildroot sdk wird synchron auf das nncase aktualisiert.

### 1.1.2 Retinaface

Funktion: Gesichtserkennung, Gesichtserkennung

Programmpfad:
`/app/ai/shell`
Laufen:
Ausführen eines nicht-quantitativen Modells`./retinaface_mb_320_bf16.sh`
Führen Sie das uint8-Quantisierungsmodell durch,`./retinaface_mb_320_uint8.sh`

Es gibt Einstellungen für QOS im Skript, die gleichen wie für die folgenden beiden Demos.

```shell
#devmem phyaddr width value
devmem 0x970E00fc 32 0x0fffff00
devmem 0x970E0100 32 0x000000ff
devmem 0x970E00f4 32 0x00550000
```

Beim Ausführen einer Demo ist es notwendig, sicherzustellen, dass die Bildschirmanzeige normal ist, dh die QoS in Bezug auf die Anzeige auf eine hohe Priorität einzustellen.
QOS_CTRL0.ax25mp Schreiben QoS = 5
QOS_CTRL0.ax25mp lesen QoS = 5
QOS_CTRL2.ispf2k schreiben QoS = 0xf
QOS_CTRL2.ispf2k lesen QoS = 0xf
QOS_CTRL2.ispr2k schreiben QoS = 0xf
QOS_CTRL2.ispr2k lesen QoS = 0xf
QOS_CTRL2.isp3dtof schreiben QoS = 0xf
QOS_CTRL3.display lesen QoS = 0xf
QOS_CTRL3.display write QoS = 0xf

QOS-Steuerregister 0(QOS_CTRL0) Offset[0x00f4]
 ![Qos Strg0](../zh/images/sdk_application/demo_nncase_qos_ctrl0.png)

QOS-Steuerregister 1 (QOS_CTRL1) Offset[0x00f8]
 ![Qos Strg1](../zh/images/sdk_application/demo_nncase_qos_ctrl1.png)

QOS-Steuerregister 2 (QOS_CTRL2) Offset[0x00fc]
 ![Qos Strg2](../zh/images/sdk_application/demo_nncase_qos_ctrl2.png)

QOS-Steuerregister 3 (QOS_CTRL3) Offset[0x0100]
 ![Qos Strg3](../zh/images/sdk_application/demo_nncase_qos_ctrl3.png)

Die Kompilierung und Installation des Modells ist im Dateipaket / ai / ai.mk detailliert beschrieben:

Skriptpfad kompilieren:
Paket/ai/code/retinaface_mb_320/rf_onnx.py

### 1.1.3 object_detect

Funktion: Objektklassifizierungserkennung, 80-Klassifikation

Programmpfad:`/app/ai/shell`

Laufen:
Ausführen eines nicht-quantitativen Modells`./object_detect_demo_bf16.sh`
Führen Sie das uint8-Quantisierungsmodell durch,`./object_detect_demo_uint8.sh`

Die Kompilierung und Installation des Modells wird im Dateipaket ai/ai.mk beschrieben.

Skriptpfad kompilieren:
Paket/ai/code/object_detect_demo/od_onnx.py

## 1,2 ffmpeg

`ffmpeg``ffmpeg-4.4`Portiert auf Open Source Code, hinzugefügt`0001-buildroot-ffmpeg-0.1.patch` für Service Packs

- `ff_k510_video_demuxer`: Steuert den ISP-Eingang, referenziert`libvideo.so`
- `ff_libk510_h264_encoder`: Steuerung der h264-Hardwarecodierung, referenziert`libvenc.so`

Konfigurierbare Parameter können über die Hilfedirektive eingesehen werden

```shell
ffmpeg -h encoder=libk510_h264 #查看k510编码器的参数
ffmpeg -h demuxer=libk510_video #查看demuxer的配置参数
```

Ausführliche Anweisungen zum Ausführen finden Sie in[ K510_Multimedia_Developer_Guides.md](./K510_Multimedia_Developer_Guides.md)

## 1.3 alsa_demo

Das alsa Demoprogramm befindet sich im`/app/alsa_demo` Verzeichnis :

Vorbereitung ausführen:
(1) Kopfhörer anschließen

Führen Sie die alsa-Demo aus:

```shell
cd /app/alsa_demo/
./alsa_demo c #录音到文件capture.pcm，demo程序仅作参考，可以参考package/alsa_demo的源码。
./alsa_demo p #播放capture.pcm
```

## 1.4 TWOD Demo

So führen Sie die Rotation aus:

```shell
cd /app/twod_app
./twod-rotation-app
```

Kopieren Sie die .yuv auf den YUV-Monitor und stellen Sie die Größe 1080 x 1920, das Anzeigeformat nv12 ein, das Ergebnis ist wie folgt
![Ausgang.yuv](../zh/images/sdk_application/driver-twod-output-1080x1920.jpg)

Verwenden des Scalers

```shell
cd /app/twod_app
./twod-scaler-app
```

Kopieren Sie die .yuv auf den YUV-Monitor und stellen Sie die Größe 640x480, Anzeigeformat nv12 ein, das Ergebnis ist wie folgt
![ouput.yuv](../zh/images/sdk_application/driver-twod-output-640x480.jpg)

So führen Sie rgb2yuv aus:

```shell
cd /app/twod_app
./twod-osd2yuv-app
```

Kopieren Sie die .yuv auf den YUV-Monitor und stellen Sie die Größe 320x240, Anzeigeformat nv12 ein, das Ergebnis ist wie folgt
![ouput.yuv](../zh/images/sdk_application/twod-osd2yuv-app.jpg)

Führen Sie die yuv2rgb-Nutzung aus:

```shell
cd /app/twod_app
./twod-scaler-output-rgb888-app
```

Kopieren Sie den .yuv auf den rgb888-Monitor und stellen Sie die Größe 640x480 ein, das Anzeigeformat rgb24, das Ergebnis ist wie folgt
![ouput.yuv](../zh/images/sdk_application/driver-twod-output-640x480.jpg)

Führen Sie die Ausgabe yuv bei der Verwendung von Overlay-OSD aus:

```shell
cd /app/twod_app
./twod-scaler-overlay-osd-app
```

Kopieren Sie die Ausgabe.yuv auf den Monitor, um die Größe 640x480, Anzeigeformat nv12 einzustellen, das Ergebnis ist wie folgt
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

## 1.5 RTC-Demo

Der RTC-Treiber registriert den Geräteknoten build /dev/rtc0.

Die Anwendungsschicht folgt der Standard-RTC-Programmiermethode im Linux-Systemaufruftreiber, und es wird empfohlen, das Drucken von Kernelinformationen über die Shell-Konsole zu deaktivieren, bevor die Referenzroutine ausgeführt wird.

```shell
echo 0 > /proc/sys/kernel/printk
```

Wechseln Sie in das Verzeichnis /app/rtc und geben Sie den folgenden Befehl ein, um die rtc-Anwendung zu starten.

```shell
cd /app/rtc
./rtc 2021-11-3 21:10:59
```

Das Ergebnis der Ausführung des Programms ist:

![](../zh/images/sdk_application/image-rtc.png)

Das Hauptcode-Snippet des RTC-Demo-Programms ist wie folgt, bitte beachten Sie den Code unter dem Ordner package / rtc für Details.

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

## 1.6 WDT-Demo

Der K510 verfügt über insgesamt drei Watchdogs, und der WDT-Treiber registriert die Geräteknoten generate /dev/watchdog0, /dev/watchdog1, /dev/watchdog2.

Die Anwendungsschicht folgt der Standard-WDT-Programmiermethode im Linux-Systemaufruftreiber, der erste Parameter der wathdog-Anwendung kann 0, 1 sein, watchdog0, watchdog1 bzw. der zweite Parameter stellt die Timeoutzeit (Sekundeneinheit) dar, die eingestellt werden kann, z. B. der folgende Befehl zeigt den Start von watchdog0 an, watchdog0 Überlaufzeit von 40 Sekunden.

```shell
cd /app/watchdog
./watchdog 0 40
```

Nachdem das Programm gestartet wurde, füttert es den Watchdog alle 1 Sekunde in Intervallen, wenn das Stoppzeichen in das Shell-Terminal eingegeben wird, die Anwendung stoppt die Fütterung des Hundes, und der Watchdog setzt den Geräteneustart zurück, nachdem das Einstellungstimeout überläuft, siehe den Code unter dem Paket/Watchdog-Ordner für Details.

Das Ergebnis der Ausführung des Programms ist:

![](../zh/images/sdk_application/image-watchdog.png)

**Hinweis**: Das aktuelle k510-Watchdog-Modul hat eine funktionierende Taktfrequenz von 757575Hz, und die Timeout-Zeit in Sekunden muss in das Timeout-Timeout der tatsächlichen Arbeitstaktfrequenz des Watchdogs umgewandelt werden, das als 2 ^ n / 757575 berechnet wird, so dass die tatsächliche Timeout-Zeit größer oder gleich dem Timeout-Timeout für die Eingabe ist. 

Der tatsächliche Timeout-Zeitraum wird wie folgt berechnet:

1) Geben Sie 40, 2 ^ 25 / 757575 = 44 > 40, 2 ^ 24 / 757575 = 22 < 40 ein, so dass es auf 44 Sekunden eingestellt ist;

2) Geben Sie 155, 2 ^ 27 / 757575 = 177 > 155 ein, so dass es auf 177 Sekunden eingestellt ist;

3) Geben Sie 2000, 2 ^ 31 / 757575 = 2834 > 2000 ein, so dass es auf 2834 Sekunden eingestellt ist;

## 1.7 UART-Demo

K510 hat insgesamt 4 serielle Ports, der aktuelle Treiber in den seriellen Ports 2, 3 ist nicht aktiviert, Serial Port 0 Treiber registriert, um /dev/ttyS0 Geräteknoten zu generieren.

Die Anwendungsschicht folgt der Standard-UART-Programmiermethode im Linux-Systemaufruftreiber. Der erste Parameter der uart-Anwendung kann 0 und 1 sein, die uart0 bzw. uart1 darstellen.

Das Entwicklungsboard verwendet ein kabelgebundenes Netzwerk, um sich mit dem Router zu verbinden, so dass das Entwicklungsboard und der debuggende PC in einem Netzwerk, wenn das Entwicklungsboard eingeschaltet ist, automatisch die IP erhält, den Befehl ifconfig im seriellen Shell-Terminal des Entwicklungsboards eingibt, um die IP-Adresse zu erhalten, und der debuggende PC verwendet diese IP, um ein telelent Fenster zu öffnen, indem er das Entwicklungsboard über die telelent Verbindung verbindet. In der folgenden Abbildung ist beispielsweise der Vorgang des Debuggens eines PCs zum Verbinden einer Entwicklungsplatine mit telent über MobaXterm dargestellt.

![](../zh/images/sdk_application/image-uart-mobaxterm.png)

Geben Sie den folgenden Befehl in das telent Terminalfenster ein, um die serielle Schnittstelle 0 zu starten.

```shell
cd /app/uart
./uart 0
```

Geben Sie den Inhalt, den Sie senden möchten, in das telent Fenster ein, Sie können die empfangenen Daten im seriellen Shell-Terminalfenster sehen, bitte beachten Sie den Code unter dem Ordner package / crb_demo / uart für Details.
Zum Beispiel die Eingabe für das telent Fenster:

![](../zh/images/sdk_application/image-uart-telent.png)

Das entsprechende Fenster des seriellen Shell-Terminals zeigt Folgendes an:

![](../zh/images/sdk_application/image-uart-shell.png)

## 1.8 ETH-Demo

Die Anwendungsschicht folgt dem Standard-ETH-Programmiermethodenaufruftreiber in Linux-Systemen.

### 1.8.1 Kunde

Geben Sie als Client das Verzeichnis /app/client ein, geben Sie den folgenden Befehl ein, um die Clientanwendung zu starten, der erste Parameter der ETH-Anwendung gibt die IP-Adresse des Servers an, um die TCP-Verbindung herzustellen, geben Sie beispielsweise den folgenden Befehl ein, um das ETH-Programm zu starten, und den Server 10.20.1.13, um die Kommunikation herzustellen.

```shell
cd /app/client
./client 10.20.1.13
```

Verbinden Sie den Server, um über das TCP-Protokoll zu kommunizieren, führen Sie das Serverprogramm auf einem anderen Ubuntu-Computer aus, weitere Informationen finden Sie im Ordner package / app / client.

Protokolle auf der Geräteseite anzeigen:

![](../zh/images/sdk_application/image-client.png)

### 1.8.2 Server

Das Gerät tritt als Server in das Verzeichnis /app/server ein, z. B. geben Sie den folgenden Befehl ein, um das Serverprogramm zu starten.

```shell
cd /app/server
./server
```

Führen Sie das Client-Programm auf einem anderen Ubuntu-Computer aus, verbinden Sie den Server über das TCP-Protokoll, um zu kommunizieren, weitere Informationen finden Sie im Ordner package / crb_demo / server.

Protokolle auf der Geräteseite anzeigen:

 ![](../zh/images/sdk_application/image-server.png)

## 1.9 SDMMC-Demo

Der K510 verfügt über insgesamt 3 SDMMC-Hauptcontroller, das Entwicklungsboard SDMMC0 wird zum Anschluss von eMMC verwendet, SDMMC1 wird für WIFI-Module verwendet und der SDMMC2-Controller wird zum Anschließen von SD-Karten verwendet.

Der SDMMC-Treiber registriert sich, um /dev/mmcblk0 zu generieren, und der EMMC-Treiber wird als /dev/mmcblk1-Geräteknoten registriert.

Die SD-Karte wird nach dem Systemstart automatisch in /root/data eingehängt, Geben Sie das Verzeichnis /app/write_read_file ein, der erste Parameter der SDMMC-Anwendung gibt die zu lesende und zu schreibende Datei an, z. B. die in /root/data eingehängte SD-Karte, Sie können Dateien im Verzeichnis /root/data/ lesen und schreiben, zuerst schreiben und dann lesen, Geben Sie den folgenden Befehl ein, um die SDMMC-Anwendung zum Lesen und Schreiben auf der SD-Karte zu starten und die Lese- und Schreibgeschwindigkeit (Einheit m/s) zu berechnen.

```shell
cd /app/write_read_file
./write_read_file /root/data/test.txt
```

Um das Lesen und Schreiben von 1G-Daten auf die SD-Karte zu ermöglichen, lesen Sie bitte den Ordner / App / write_read_file Ordner.

![](../zh/images/sdk_application/image-sdmmc.png)

## 1.10 SHA/AES-Demo

Die SHA/AES-Demo verwendet den Linux-Kernel, um AF_ALG Art von Netlink-Schnittstelle zu exportieren, und verwendet die Kernel-Verschlüsselungs-API im Benutzerbereich. Weitere Informationen finden Sie unter .<https://www.kernel.org/doc/html/latest/crypto/userspace-if.html> 

Parameter:
-h Druckt die Hilfeinformationen
-t Algorithmustyp: hash, skcipher
-n Algorithmusnamen: sha256, ecb(aes), cbc(aes)
-x-Entschlüsselungsvorgang
-k AES KEY (hexadezimale Zeichenfolge)
-v AES IV (hexadezimale Zeichenfolge)

![](../zh/images/sdk_application/image_crypto_help.png)

SHA256-Test:

```shell
cd /app/crypto
echo -n "This is a test file, hello world" > plain.txt
./crypto -t hash -n "sha256" plain.txt sha256.txt
xxd -p -c 32 sha256.txt
sha256sum plain.txt
```

![](../zh/images/sdk_application/image_crypto_sha256.png)

EZB(AES) 128 Test:

```shell
cd /app/crypto
echo -n "This is a test file, hello world" > plain.txt
./crypto -t skcipher -n "ecb(aes)" -k 00112233445566778899aabbccddeeff plain.txt ecb_aes_en.bin
./crypto -t skcipher -n "ecb(aes)" -k 00112233445566778899aabbccddeeff  -x ecb_aes_en.bin ecb_aes_de.bin
cmp ecb_aes_de.bin plain.txt
cat ecb_aes_de.bin
```

![](../zh/images/sdk_application/image_crypto_ecb.png)

CBC(AES) 128-Test

```shell
cd /app/crypto
echo -n "This is a test file, hello world" > plain.txt
./crypto -t skcipher -n "cbc(aes)" -k 00112233445566778899aabbccddeeff -v 00112233445566778899aabbccddeeff plain.txt cbc_aes_en.bin
./crypto -t skcipher -n "cbc(aes)" -k 00112233445566778899aabbccddeeff -v 00112233445566778899aabbccddeeff -x cbc_aes_en.bin cbc_aes_de.bin
cmp cbc_aes_de.bin plain.txt
cat cbc_aes_de.bin
```

![](../zh/images/sdk_application/image_crypto_cbc.png)

Die AES-ECB-128- und AES-CBC-128-Verschlüsselung erfordert eine 16-Byte-Ausrichtung des Klartexts, und die unzureichende Verschlüsselung wird automatisch mit 0 gefüllt.

## 1.11 TRNG-Demo

Die TRNG-Demo erzeugt eine Zufallszahl der angegebenen Länge durch Lesen des Zeichengeräts /dev/hwrng, das als hexadezimale Zeichenfolge ausgegeben wird.

Die Bedeutung des Eingabeparameters von ./trng:

-h Druckt die Hilfeinformationen

-b Gibt die Länge der Ausgabezufallszahl in Byte an.

![](../zh/images/sdk_application/image_trng.png)

## 1.12 DRM-Demo

Die Drm-Demo demonstriert die Multi-Layer-Funktionen der vo-Hardware.

Vo hat insgesamt 8 Schichten:

1) Hintergrundebene, kann Hintergrundfarbe konfiguriert werden.

2) Layer0 ist eine Videoschicht, unterstützt YUV422 und YUV420, unterstützt NV12- und NV21-Formate, kann auf der Größenseite angepasst werden und unterstützt Hardware-Skalierung nach oben und unten.

3) Layer1-layer3 ist eine Videoschicht, die YUV422 und YUV420 unterstützt, NV12- und NV21-Formate unterstützt, und die Größenseite kann angepasst werden.

4) Layer4-layer6 ist die OSD-Schicht, die mehrere ARGB-Formate unterstützt.

Nachdem das Board gestartet wurde, geben Sie das Verzeichnis /app/drm_demo ein und geben Sie den folgenden Befehl ein:

```shell
cd /app/drm_demo
./drm_demo
```

Starten Sie drm_demo Anwendung, drm_demo angezeigt:

![](../zh/images/sdk_application/image_drm_demo.png)

## 1.13 V4L2_DRM Demo

v4l2_drm Demo demonstriert die Funktionalität von Kameraeingabe und -anzeige.

Nachdem das Board gestartet wurde, geben Sie das Verzeichnis /app/mediactl_lib ein und geben Sie den folgenden Befehl ein:

```shell
cd /app/mediactl_lib
./v4l2_drm.out -f video_drm_1080x1920.conf -e 1
或者
./v4l2_drm.out -f video_drm_1920x1080.conf
```

Starten Sie die v4l2_drm.out-Anwendung und v4l2_drm.out-Anzeige:

![](../zh/images/sdk_application/image_v4l2_drm_demo.png)

## 1.14 LVGL-Demo

Wechseln Sie zu /app/lvgl, und führen Sie den folgenden Befehl aus:

```shell
cd /app/lvgl
./lvgl
```

Der Darstellungseffekt ist wie folgt:![](../zh/images/sdk_application/image_lvgl.png)

## 1.15 PWM-Demo

Der PWM-Treiber registriert die Geräteknoten generate /sys/class/pwm/pwmchip0 und /sys/class/pwm/pwmchip3.

Dieses Beispiel kann für pwm0 bzw. pwm1 im Verzeichnis /app/pwm konfiguriert und aktiviert werden, der erste Parameter der pwm-Anwendung gibt den Zeitraum der Einstellung von pwm an, die Einheit ist ns, der zweite Parameter legt die Zeit von "ON" in einem Zyklus von pwm fest, die Einheit ist ns, der dritte Parameter kann 0, 1 sein und pwm0 und pwm1 darstellen, geben Sie beispielsweise den folgenden Befehl ein, um pwm0 zu aktivieren, der Zyklus ist 1s, der Tastzyklus ist 1000000000/ 500000000*100% = 50%, detaillierte Codes finden Sie im Ordner Ordner/App/PWM.

```shell
cd /app/pwm
./pwm 1000000000 500000000 0
```

Das Ergebnis der Ausführung des Programms ist:

![](../zh/images/sdk_application/image-pwm.png)

Durch den Anschluss von Pin 28 des K510 CRB1.2 Entwicklungsboards J15 durch das Oszilloskop kann ein Wellenformmuster mit einer Periode von 1 Sekunde und einem Tastverhältnis von 50% auf dem Oszilloskop beobachtet werden.

## 1.16 WIFI-Demo

Nachdem der WiFi-Modultreiber geladen wurde, wird die Wireless-Netzwerkkarte wlan0 generiert, die dem Standard-Netzwerkporttreiber folgt und sich normalerweise auf die TCP/IP-Socket-Programmierung bezieht.

1) Öffnen Sie "Mobile Hotspot" im Notizbuch und legen Sie dann den Namen und das Passwort des Hotspots fest
2) Starten Sie NetAssist auf dem Notebook, konfigurieren Sie den Protokolltyp, die lokale Host-IP, den lokalen Host-Port, die Empfangseinstellungen, die Sendeeinstellungen und die zu sendenden Daten, wie in der folgenden Abbildung dargestellt:

![](../zh/images/sdk_application/image_wifi_1.png)

3) Das Parameterformat des WLAN-Testprogramms ist:

```shell
./wifi <AP name> <password> <local ip> <server ip>
```

Geben Sie beispielsweise das Verzeichnis /app/wifi ein, geben Sie den Befehl zum Starten des WLAN-Testprogramms ein, und das Ausführungsergebnis des Programms lautet wie folgt:

![](../zh/images/sdk_application/image_wifi_2.png)

## 1.17 GPIO_KEYS Demo

Der Schlüsseltreiber verwendet den Linux-Kernel selbst, der in den generischen gpu-keys-Treiber integriert ist, der auf dem Eingabesubsystem basiert, und nachdem der Treiber geladen wurde, wird der Ereignisüberwachungsknoten eventX im Verzeichnis /dev/input generiert, und X ist die Sequenznummer des Ereignisknotens, die über cat /proc/bus/input/devices angezeigt werden kann.

gpio-keys-Routine, die das Lesen von Schlüsselberichtsereignissen und das Drucken von Ereignisinformationen blockiert, seine Informationen umfassen Schlüsselcodierung und Schlüsselaktion, Schlüsselcode zur Identifizierung der Schlüsselidentität, Schlüsselaktion ist unterteilt in gedrückt und freigegeben, in der Schlüsselfreigabe, wenn die Routine die Dauer des Tastendrucks berechnet

Das Ergebnis der Programmausführung ist in der folgenden Abbildung dargestellt:![](../zh/images/sdk_application/image-gpio-keys.png)

**Haftungsausschluss **für Übersetzungen  
Für die Bequemlichkeit der Kunden verwendet Canaan einen KI-Übersetzer, um Text in mehrere Sprachen zu übersetzen, die Fehler enthalten können. Wir übernehmen keine Gewähr für die Genauigkeit, Zuverlässigkeit oder Aktualität der bereitgestellten Übersetzungen. Canaan haftet nicht für Verluste oder Schäden, die durch das Vertrauen auf die Richtigkeit oder Zuverlässigkeit der übersetzten Informationen verursacht werden. Wenn es einen inhaltlichen Unterschied zwischen den Übersetzungen in verschiedenen Sprachen gibt, ist die vereinfachte chinesische Version maßgebend. 

Wenn Sie einen Übersetzungsfehler oder eine Ungenauigkeit melden möchten, können Sie uns gerne per E-Mail kontaktieren.