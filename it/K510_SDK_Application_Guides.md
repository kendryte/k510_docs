![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">Guida all'applicazione K510 SDK</font>**

<font face="黑体"  size=3>Versione del documento: V1.0.0</font>

<font face="黑体"  size=3>Data di pubblicazione: 2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Disconoscimento**</font>
I prodotti, i servizi o le funzionalità acquistati saranno soggetti ai contratti e ai termini commerciali di Beijing Canaan Jiesi Information Technology Co., Ltd. ("la Società", la stessa di seguito), e tutti o parte dei prodotti, servizi o funzionalità descritti in questo documento potrebbero non rientrare nell'ambito dell'acquisto o dell'utilizzo. Salvo quanto diversamente concordato nel contratto, la Società declina ogni dichiarazione o garanzia, espressa o implicita, in merito all'accuratezza, affidabilità, completezza, marketing, scopo specifico e non aggressione di qualsiasi dichiarazione, informazione o contenuto di questo documento. Salvo diverso accordo, questo documento è fornito solo come guida per l'uso.
A causa di aggiornamenti della versione del prodotto o altri motivi, il contenuto di questo documento può essere aggiornato o modificato di volta in volta senza alcun preavviso.

**<font face="黑体"  size=3>Avvisi sui marchi</font>**

""<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, l'icona "Canaan", Canaan e altri marchi di Canaan e altri marchi di Canaan sono marchi di Beijing Canaan Jiesi Information Technology Co., Ltd. Tutti gli altri marchi o marchi registrati che possono essere menzionati in questo documento sono di proprietà dei rispettivi proprietari.

**<font face="黑体"  size=3>Copyright ©2022 Pechino Canaan Jiesi Information Technology Co., Ltd</font>**
Questo documento è applicabile solo allo sviluppo e alla progettazione della piattaforma K510, senza il permesso scritto della società, nessuna unità o individuo può diffondere parte o tutto il contenuto di questo documento in qualsiasi forma.

**<font face="黑体"  size=3>Pechino Canaan Jiesi Information Technology Co., Ltd</font>**
URL: canaan-creative.com
Richieste commerciali: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# prefazione
**<font face="黑体"  size=5>Scopo </font>**del documento
Questo documento è un documento di descrizione per l'esempio di applicazione K510 SDK.

**<font face="黑体"  size=5>Oggetti lettore</font>**

Le principali persone a cui si applica questo documento (questa guida):

- Sviluppatori di software
- Personale di supporto tecnico

**<font face="黑体"  size=5>Cronologia delle revisioni</font>**
 <font face="宋体"  size=2>La cronologia delle revisioni accumula una descrizione di ogni aggiornamento del documento. La versione più recente del documento contiene gli aggiornamenti per tutte le versioni precedenti. </font>

| Il numero di versione | Modificato da     | Data della revisione   | Note di revisione     |
| :----- | ---------- | ---------- | ------------ |
| V1.0.0 · | Gruppi di software di sistema | 2022-03-09 | Rilasciato SDK V1.5 |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenuto</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 App demo

## 1.1 ai demo program

### 1.1.1 Descrizione

Il codice sorgente del programma demo di nncase si trova nella directory sotto la directory SDK`package/ai` e la struttura della directory è la seguente:

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

Puoi fare riferimento al codice sorgente del retinaface_mb_320 e`CMakeLists.txt` aggiungere un nuovo programma demo nncase.

Per la compilazione del modello, vedere`nncase_demo.mk` il POST_INSTALL_TARGET_HOOKS*ivi definito*:

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

La compilazione del modello richiede un ambiente nncase, e per la costruzione dell'ambiente nncase, fare riferimento a k510_nncase_Developer_Guides.md. In futuro, il nncase ha un aggiornamento e l'sdk buildroot verrà aggiornato al nncase in modo sincrono.

### 1.1.2 retinaface

Funzione: rilevamento del volto, rilevamento del punto di riferimento del viso

Percorso del programma:
`/app/ai/shell`
Correre:
Eseguire un modello `./retinaface_mb_320_bf16.sh`non quantitativo
Eseguire il modello di quantizzazione uint8,`./retinaface_mb_320_uint8.sh`

Nello script sono presenti impostazioni per QOS, le stesse delle due demo seguenti.

```shell
#devmem phyaddr width value
devmem 0x970E00fc 32 0x0fffff00
devmem 0x970E0100 32 0x000000ff
devmem 0x970E00f4 32 0x00550000
```

Quando si esegue una demo, è necessario dare la priorità assicurandosi che la visualizzazione dello schermo sia normale, ovvero regolare il QoS relativo al display su un'alta priorità.
QOS_CTRL0.ax25mp scrivi QoS = 5
QOS_CTRL0.ax25mp lettura QoS = 5
QOS_CTRL2.ispf2k write QoS = 0xf
QOS_CTRL2.ispf2k leggere QoS = 0xf
QOS_CTRL2.ispr2k scrivere QoS = 0xf
QOS_CTRL2.ispr2k leggere QoS = 0xf
QOS_CTRL2.isp3dtof write QoS = 0xf
QOS_CTRL3.display leggi QoS = 0xf
QOS_CTRL3.display write QoS = 0xf

Registro di controllo QOS 0(QOS_CTRL0) offset[0x00f4]
 ![QOS CTRL0](../zh/images/sdk_application/demo_nncase_qos_ctrl0.png)

Offset del registro di controllo QOS 1 [QOS_CTRL1](0x00f8)
 ![QOS CTRL1](../zh/images/sdk_application/demo_nncase_qos_ctrl1.png)

Offset del registro di controllo QOS 2 [QOS_CTRL2](0x00fc)
 ![QOS CTRL2](../zh/images/sdk_application/demo_nncase_qos_ctrl2.png)

Offset del registro di controllo QOS 3 [QOS_CTRL3](0x0100)
 ![QOS CTRL3](../zh/images/sdk_application/demo_nncase_qos_ctrl3.png)

La compilazione e l'installazione del modello è dettagliata nel pacchetto di file/ai/ai.mk:

Compilare il percorso dello script:
pacchetto/ai/codice/retinaface_mb_320/rf_onnx.py

### 1.1.3 object_detect

Funzione: rilevamento della classificazione degli oggetti, classificazione 80

Percorso del programma:`/app/ai/shell`

Correre:
Eseguire un modello `./object_detect_demo_bf16.sh`non quantitativo
Eseguire il modello di quantizzazione uint8,`./object_detect_demo_uint8.sh`

La compilazione e l'installazione del modello è dettagliata nel pacchetto di file/ai/ai.mk

Compilare il percorso dello script:
pacchetto/ai/codice/object_detect_demo/od_onnx.py

## 1,2 ffmpeg

`ffmpeg``ffmpeg-4.4`Portato su codice open source, aggiunto`0001-buildroot-ffmpeg-0.1.patch` per i service pack

- `ff_k510_video_demuxer`: controlla l'input isp, a cui si fa riferimento`libvideo.so`
- `ff_libk510_h264_encoder`: Controllo della codifica hardware h264, a cui si fa riferimento`libvenc.so`

I parametri configurabili possono essere visualizzati tramite la direttiva help

```shell
ffmpeg -h encoder=libk510_h264 #查看k510编码器的参数
ffmpeg -h demuxer=libk510_video #查看demuxer的配置参数
```

Per istruzioni dettagliate sull'esecuzione, fare riferimento a[K510_Multimedia_Developer_Guides.md](./K510_Multimedia_Developer_Guides.md)

## 1.3 alsa_demo

Il programma demo alsa è inserito nella`/app/alsa_demo` directory :

Esegui la preparazione:
(1) Collegare le cuffie

Esegui la demo di alsa:

```shell
cd /app/alsa_demo/
./alsa_demo c #录音到文件capture.pcm，demo程序仅作参考，可以参考package/alsa_demo的源码。
./alsa_demo p #播放capture.pcm
```

## 1.4 Demo TWOD

Come eseguire la rotazione:

```shell
cd /app/twod_app
./twod-rotation-app
```

Copiare l'output .yuv sul monitor YUV e impostare la dimensione 1080 x 1920, formato di visualizzazione nv12, il risultato è il seguente
![output.yuv](../zh/images/sdk_application/driver-twod-output-1080x1920.jpg)

Utilizzo dello scaler

```shell
cd /app/twod_app
./twod-scaler-app
```

Copiare l'output .yuv sul monitor YUV e impostare le dimensioni 640x480, formato di visualizzazione nv12, il risultato è il seguente
![ouput.yuv](../zh/images/sdk_application/driver-twod-output-640x480.jpg)

Come eseguire rgb2yuv:

```shell
cd /app/twod_app
./twod-osd2yuv-app
```

Copiare l'output .yuv sul monitor YUV e impostare la dimensione 320x240, formato di visualizzazione nv12, il risultato è il seguente
![ouput.yuv](../zh/images/sdk_application/twod-osd2yuv-app.jpg)

Esegui l'utilizzo di yuv2rgb:

```shell
cd /app/twod_app
./twod-scaler-output-rgb888-app
```

Copia l'output .yuv sul monitor rgb888 e imposta la dimensione 640x480, il formato di visualizzazione rgb24, il risultato è il seguente
![ouput.yuv](../zh/images/sdk_application/driver-twod-output-640x480.jpg)

Esegui l'output yuv sull'utilizzo di osd di sovrapposizione:

```shell
cd /app/twod_app
./twod-scaler-overlay-osd-app
```

Copiare l'output .yuv sul monitor per impostare la dimensione 640x480, formato di visualizzazione nv12, il risultato è il seguente
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

## 1.5 Demo RTC

Il driver RTC registra il nodo del dispositivo build /dev/rtc0.

Il livello dell'applicazione segue il metodo di programmazione RTC standard nel driver di chiamata di sistema Linux e si consiglia di disattivare la stampa delle informazioni del kernel attraverso la console della shell prima di eseguire la routine di riferimento.

```shell
echo 0 > /proc/sys/kernel/printk
```

Vai alla directory /app/rtc e inserisci il seguente comando per avviare l'applicazione rtc.

```shell
cd /app/rtc
./rtc 2021-11-3 21:10:59
```

Il risultato dell'esecuzione del programma è:

![](../zh/images/sdk_application/image-rtc.png)

Lo snippet di codice principale del programma demo RTC è il seguente, fare riferimento al codice nella cartella package/rtc per i dettagli.

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

## 1.6 Demo WDT

Il K510 ha un totale di tre watchdog e il driver WDT registra i nodi di dispositivo generate /dev/watchdog0, /dev/watchdog1, /dev/watchdog2.

Il livello dell'applicazione segue il metodo di programmazione WDT standard nel driver di chiamata di sistema Linux, il primo parametro dell'applicazione wathdog può essere 0, 1, rappresentare watchdog0, watchdog1, rispettivamente, il secondo parametro rappresenta il tempo di timeout (secondi unitari) che può essere impostato, ad esempio, il seguente comando indica l'inizio di watchdog0, tempo di overflow watchdog0 di 40 secondi.

```shell
cd /app/watchdog
./watchdog 0 40
```

Dopo l'avvio del programma, alimenterà il watchdog ogni 1 secondo a intervalli, quando il carattere di arresto viene inserito nel terminale della shell, l'applicazione smette di nutrire il cane e il watchdog ripristinerà il riavvio del dispositivo dopo che il timeout delle impostazioni trabocca, fare riferimento al codice nella cartella package / watchdog per i dettagli.

Il risultato dell'esecuzione del programma è:

![](../zh/images/sdk_application/image-watchdog.png)

**Nota**: l'attuale modulo watchdog k510 ha una frequenza di clock funzionante di 757575Hz e il tempo di timeout in secondi deve essere convertito nel timeout timeout della frequenza di clock di lavoro effettiva del watchdog, che viene calcolata come 2^n/757575, quindi il timeout di timeout effettivo sarà maggiore o uguale al timeout del timeout di input.

Il periodo di timeout effettivo viene calcolato come segue:

1) Inserisci 40, 2^25/757575=44 > 40, 2^24/757575=22 < 40, quindi è impostato su 44 secondi;

2) Inserisci 155, 2^27/757575=177 > 155, quindi è impostato su 177 secondi;

3) Inserisci 2000, 2^31/757575=2834 > 2000, quindi è impostato su 2834 secondi;

## 1.7 Demo UART

K510 ha un totale di 4 porte seriali, il driver corrente nelle porte seriali 2, 3 non è abilitato, il driver della porta seriale 0 verrà registrato per generare nodi di dispositivo / dev / ttyS0.

Il livello dell'applicazione segue il metodo di programmazione UART standard nel driver di chiamata di sistema Linux. Il primo parametro dell'applicazione uart può essere 0 e 1, che rappresentano rispettivamente uart0 e uart1.

La scheda di sviluppo utilizza una rete cablata per connettersi al router, in modo che la scheda di sviluppo e il PC di debug in una rete, quando la scheda di sviluppo è accesa, otterrà automaticamente l'IP, inserirà il comando ifconfig nel terminale seriale della shell della scheda di sviluppo per ottenere l'indirizzo IP e il PC di debug utilizza questo IP per aprire una finestra telent collegando la scheda di sviluppo tramite la connessione telent. Ad esempio, l'operazione di debug di un PC per connettere una scheda di sviluppo utilizzando telent tramite MobaXterm è illustrata nella figura seguente.

![](../zh/images/sdk_application/image-uart-mobaxterm.png)

Immettere il seguente comando nella finestra del terminale telent per avviare il lavoro della porta seriale 0.

```shell
cd /app/uart
./uart 0
```

Inserisci il contenuto che desideri inviare nella finestra telent, puoi vedere i dati ricevuti nella finestra del terminale seriale della shell, fai riferimento al codice nella cartella package / crb_demo / uart per i dettagli.
Ad esempio, l'input per la finestra telent:

![](../zh/images/sdk_application/image-uart-telent.png)

La finestra del terminale seriale Shell corrispondente visualizza:

![](../zh/images/sdk_application/image-uart-shell.png)

## 1.8 Demo ETH

Il livello dell'applicazione segue il driver di chiamata del metodo di programmazione ETH standard nei sistemi Linux.

### 1.8.1 Cliente

Il dispositivo come client, immettere la directory /app/client, immettere il seguente comando per avviare l'applicazione client, il primo parametro dell'applicazione ETH indica l'indirizzo IP del server per stabilire il collegamento TCP, ad esempio, immettere il seguente comando per avviare il programma ETH e il server 10.20.1.13 per stabilire la comunicazione.

```shell
cd /app/client
./client 10.20.1.13
```

Collegare il server per comunicare tramite protocollo tcp, eseguire il programma server su un'altra macchina ubuntu, fare riferimento alla cartella pacchetto / app / client per i dettagli.

Visualizza i registri sul lato dispositivo:

![](../zh/images/sdk_application/image-client.png)

### 1.8.2 Server

Il dispositivo entra nella directory /app/server come server, ad esempio, immettere il seguente comando per avviare il programma server.

```shell
cd /app/server
./server
```

Eseguire il programma client su un'altra macchina ubuntu, collegare il server tramite il protocollo tcp per comunicare, per i dettagli, fare riferimento alla cartella package/crb_demo/server.

Visualizza i registri sul lato dispositivo:

 ![](../zh/images/sdk_application/image-server.png)

## 1.9 Demo SDMMC

Il K510 ha un totale di 3 controller principali SDMMC, la scheda di sviluppo SDMMC0 viene utilizzata per collegare eMMC, SDMMC1 viene utilizzato per i moduli WIFI e il controller SDMMC2 viene utilizzato per collegare le schede SDCARD.

Il driver SDMMC viene registrato per generare /dev/mmcblk0 e il driver EMMC viene registrato come nodo dispositivo /dev/mmcblk1.

La scheda SD verrà automaticamente montata su /root/data dopo l'avvio del sistema, inserisci la directory /app/write_read_file, il primo parametro dell'applicazione SDMMC indica il file da leggere e scrivere, come la scheda SD montata su /root/data, puoi leggere e scrivere file nella directory /root/data/, prima scrivi e poi leggi, Immettere il seguente comando per avviare l'applicazione SDMMC per leggere e scrivere sulla scheda SD e calcolare la velocità di lettura e scrittura (unità m/s).

```shell
cd /app/write_read_file
./write_read_file /root/data/test.txt
```

Per abilitare la lettura e la scrittura dei dati 1G sulla scheda SD, fare riferimento alla cartella/app/cartella write_read_file.

![](../zh/images/sdk_application/image-sdmmc.png)

## 1.10 Demo SHA/AES

La demo SHA/AES utilizza il kernel Linux per esportare AF_ALG tipo di interfaccia Netlink e utilizza l'API di crittografia del kernel nello spazio utente. Si prega di fare riferimento a .<https://www.kernel.org/doc/html/latest/crypto/userspace-if.html>

Parametro:
-h Stampa le informazioni di aiuto
Tipo di algoritmo -t: hash, skcipher
-n Nomi degli algoritmi: sha256, ecb(aes), cbc(aes)
-x operazione di decrittografia
-k CHIAVE AES (stringa esadecimale)
-v AES IV (stringa esadecimale)

![](../zh/images/sdk_application/image_crypto_help.png)

test sha256:

```shell
cd /app/crypto
echo -n "This is a test file, hello world" > plain.txt
./crypto -t hash -n "sha256" plain.txt sha256.txt
xxd -p -c 32 sha256.txt
sha256sum plain.txt
```

![](../zh/images/sdk_application/image_crypto_sha256.png)

bce(aes) 128 test:

```shell
cd /app/crypto
echo -n "This is a test file, hello world" > plain.txt
./crypto -t skcipher -n "ecb(aes)" -k 00112233445566778899aabbccddeeff plain.txt ecb_aes_en.bin
./crypto -t skcipher -n "ecb(aes)" -k 00112233445566778899aabbccddeeff  -x ecb_aes_en.bin ecb_aes_de.bin
cmp ecb_aes_de.bin plain.txt
cat ecb_aes_de.bin
```

![](../zh/images/sdk_application/image_crypto_ecb.png)

cbc(aes) 128 test

```shell
cd /app/crypto
echo -n "This is a test file, hello world" > plain.txt
./crypto -t skcipher -n "cbc(aes)" -k 00112233445566778899aabbccddeeff -v 00112233445566778899aabbccddeeff plain.txt cbc_aes_en.bin
./crypto -t skcipher -n "cbc(aes)" -k 00112233445566778899aabbccddeeff -v 00112233445566778899aabbccddeeff -x cbc_aes_en.bin cbc_aes_de.bin
cmp cbc_aes_de.bin plain.txt
cat cbc_aes_de.bin
```

![](../zh/images/sdk_application/image_crypto_cbc.png)

La crittografia AES-ECB-128 e aes-cbc-128 richiede l'allineamento a 16 byte del testo in chiaro e l'insufficiente verrà automaticamente riempito con 0.

## 1.11 Demo TRNG

La demo TRNG produce un numero casuale della lunghezza specificata leggendo il dispositivo di caratteri /dev/hwrng, output come stringa esadecimale.

Significato del parametro di input di ./trng:

-h Stampa le informazioni di aiuto

-b Specifica la lunghezza del numero casuale di output, in byte

![](../zh/images/sdk_application/image_trng.png)

## 1.12 Demo DRM

La demo drm dimostra le funzionalità multilivello dell'hardware vo.

Vo ha un totale di 8 strati:

1) Livello di sfondo, può essere configurato il colore di sfondo.

2) Layer0 è un livello video, supporta YUV422 e YUV420, supporta i formati NV12 e NV21, può essere abbinato sul lato delle dimensioni e supporta il ridimensionamento e il ridimensionamento dell'hardware.

3) Layer1-layer3 è un livello video, che supporta YUV422 e YUV420, supporta i formati NV12 e NV21 e il lato delle dimensioni può essere abbinato.

4) Layer4-layer6 è il livello OSD che supporta più formati ARGB.

Dopo l'avvio della scheda, immettere la directory /app/drm_demo e immettere il comando:

```shell
cd /app/drm_demo
./drm_demo
```

Avvia drm_demo applicazione, drm_demo visualizzata:

![](../zh/images/sdk_application/image_drm_demo.png)

## 1.13 Demo V4L2_DRM

v4l2_drm demo dimostra la funzionalità dell'input e del display della telecamera.

Dopo l'avvio della scheda, immettere la directory /app/mediactl_lib e immettere il comando:

```shell
cd /app/mediactl_lib
./v4l2_drm.out -f video_drm_1080x1920.conf -e 1
或者
./v4l2_drm.out -f video_drm_1920x1080.conf
```

Avviare l'applicazione v4l2_drm.out e v4l2_drm.out:

![](../zh/images/sdk_application/image_v4l2_drm_demo.png)

## 1.14 Demo LVGL

Vai su /app/lvgl ed esegui il seguente comando:

```shell
cd /app/lvgl
./lvgl
```

L'effetto di visualizzazione è il seguente:![](../zh/images/sdk_application/image_lvgl.png)

## 1.15 Demo PWM

Il driver PWM registra i nodi di periferica generate /sys/class/pwm/pwmchip0 e /sys/class/pwm/pwmchip3.

Questo esempio può essere configurato e abilitato rispettivamente per pwm0 e pwm1, nella directory /app/pwm, il primo parametro dell'applicazione pwm indica il periodo di impostazione pwm, l'unità è ns, il secondo parametro imposta il tempo di "ON" in un ciclo di pwm, l'unità è ns, il terzo parametro può essere 0, 1, che rappresenta pwm0 e pwm1, ad esempio, immettere il seguente comando per abilitare pwm0, il ciclo è 1s, il ciclo di lavoro è 100000000/ 500000000 * 100% = 50%, fare riferimento alla cartella cartella / app / pwm per i codici dettagliati.

```shell
cd /app/pwm
./pwm 1000000000 500000000 0
```

Il risultato dell'esecuzione del programma è:

![](../zh/images/sdk_application/image-pwm.png)

Collegando il pin 28 della scheda di sviluppo K510 CRB1.2 J15 attraverso l'oscilloscopio, è possibile osservare un modello di forma d'onda con un periodo di 1 secondo e un ciclo di lavoro del 50% sull'oscilloscopio.

## 1.16 Demo WIFI

Dopo aver caricato il driver del modulo WiFi, viene generata la scheda di rete wireless wlan0, che segue il driver della porta di rete standard e normalmente si riferisce alla programmazione del socket TCP / IP.

1) Aprire "Mobile Hotspot" nel notebook, quindi impostare il nome e la password dell'hotspot
2) Avviare NetAssist sul notebook, configurare il tipo di protocollo, l'IP dell'host locale, la porta host locale, le impostazioni di ricezione, le impostazioni di invio e i dati che devono essere inviati, come mostrato nella figura seguente:

    ![](../zh/images/sdk_application/image_wifi_1.png)

3) Il formato dei parametri del programma di test wifi è:

    ```shell
    ./wifi <AP name> <password> <local ip> <server ip>
    ```

    Ad esempio, immettere la directory /app/wifi, immettere il comando per avviare il programma di test wifi e il risultato dell'esecuzione del programma è il seguente:

    ![](../zh/images/sdk_application/image_wifi_2.png)

## 1.17 demo GPIO_KEYS

Il driver chiave utilizza il kernel linux stesso integrato con il driver generico gpu-keys basato sul sottosistema di input, e dopo che il driver è stato caricato, il nodo di monitoraggio degli eventi eventX viene generato nella directory /dev/input e X è il numero di sequenza del nodo evento, che può essere visualizzato tramite cat /proc/bus/input/devices

gpio-keys routine blocking reading key reporting events and printing event information, its information includes key encoding and key action, key code to identify key identity, key action is split into pressed and released, in the key release when the routine will calculate the duration of key press

Il risultato dell'esecuzione del programma è illustrato nella figura seguente:![](../zh/images/sdk_application/image-gpio-keys.png)

**Traduzione Disclaimer**  
Per la comodità dei clienti, Canaan utilizza un traduttore AI per tradurre il testo in più lingue, che possono contenere errori. Non garantiamo l'accuratezza, l'affidabilità o la tempestività delle traduzioni fornite. Canaan non sarà responsabile per eventuali perdite o danni causati dall'affidamento sull'accuratezza o sull'affidabilità delle informazioni tradotte. Se c'è una differenza di contenuto tra le traduzioni in lingue diverse, prevarrà la versione cinese semplificata.

Se desideri segnalare un errore di traduzione o un'inesattezza, non esitare a contattarci via mail.
