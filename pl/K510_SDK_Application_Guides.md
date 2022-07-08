![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 SDK — podręcznik aplikacji</font>**

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
Ten dokument jest dokumentem opisowym przykładowej aplikacji K510 SDK. 

**<font face="黑体"  size=5>Obiekty programu Reader</font>**

Główne osoby, których dotyczy ten dokument (ten przewodnik):

- Programiści
- Personel wsparcia technicznego

**<font face="黑体"  size=5>Historia</font>**
 zmian <font face="宋体"  size=2>Historia zmian gromadzi opis każdej aktualizacji dokumentu. Najnowsza wersja dokumentu zawiera aktualizacje dla wszystkich poprzednich wersji. </font>

| Numer wersji | Zmodyfikowane przez     | Data aktualizacji   | Uwagi do poprawek     |
| :----- | ---------- | ---------- | ------------ |
| Wersja 1.0.0 | Grupy oprogramowania systemowego | 2022-03-09 | SDK V1.5 wydany |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Treść</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Aplikacja demonstracyjna

## 1.1 Program demonstracyjny ai

### 1.1.1 Opis

Kod źródłowy programu demonstracyjnego nncase znajduje się w katalogu w katalogu SDK`package/ai`, a struktura katalogów jest następująca:

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

Możesz odwołać się do kodu źródłowego retinaface_mb_320 i`CMakeLists.txt` dodać nowy program demonstracyjny nncase. 

Aby zapoznać się z kompilacją modelu, zobacz`nncase_demo.mk` POST_INSTALL_TARGET_HOOKS* w nim zdefiniowane*:

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

Kompilacja modelu wymaga środowiska nncase, a dla budowy środowiska nncase patrz k510_nncase_Developer_Guides.md. W przyszłości nncase ma aktualizację, a buildroot sdk zostanie zaktualizowany do nncase synchronicznie.

### 1.1.2 siatkówka twarzy

Funkcja: Wykrywanie twarzy, wykrywanie punktów orientacyjnych twarzy

Ścieżka programu:
`/app/ai/shell`
Biegać:
Wykonywanie modelu `./retinaface_mb_320_bf16.sh`nieilościowego
Wykonać model kwantyzacji uint8,`./retinaface_mb_320_uint8.sh`

W skrypcie znajdują się ustawienia QOS, takie same jak w przypadku kolejnych dwóch wersji demonstracyjnych.

```shell
#devmem phyaddr width value
devmem 0x970E00fc 32 0x0fffff00
devmem 0x970E0100 32 0x000000ff
devmem 0x970E00f4 32 0x00550000
```

Podczas uruchamiania wersji demonstracyjnej konieczne jest ustalenie priorytetów, aby upewnić się, że wyświetlanie ekranu jest normalne, to znaczy dostosować QoS związane z wyświetlaczem do wysokiego priorytetu.
QOS_CTRL0.ax25mp zapis QoS = 5
QOS_CTRL0.ax25mp odczyt QoS = 5
QOS_CTRL2.ispf2k zapisz QoS = 0xf
QOS_CTRL2.ispf2k odczytuje QoS = 0xf
QOS_CTRL2.ispr2k zapisz QoS = 0xf
QOS_CTRL2.ispr2k odczyt QoS = 0xf
QOS_CTRL2.isp3dtof zapisz QoS = 0xf
QOS_CTRL3.display odczyt QoS = 0xf
QOS_CTRL3.display zapisz QoS = 0xf

Przesunięcie rejestru sterowania QOS 0(QOS_CTRL0)[0x00f4]
 ![qos ctrl0](../zh/images/sdk_application/demo_nncase_qos_ctrl0.png)

Przesunięcie 
 [0x00f8]rejestru sterowania QOS 1 (QOS_CTRL1)![ qos ctrl1](../zh/images/sdk_application/demo_nncase_qos_ctrl1.png)

Przesunięcie 
 [0x00fc]rejestru sterowania QOS 2 (QOS_CTRL2)![ qos ctrl2](../zh/images/sdk_application/demo_nncase_qos_ctrl2.png)

Przesunięcie 
 [0x0100]rejestru sterowania QOS 3 (QOS_CTRL3)![ qos ctrl3](../zh/images/sdk_application/demo_nncase_qos_ctrl3.png)

Kompilacja i instalacja modelu jest szczegółowo opisana w pliku package/ai/ai.mk:

Skompiluj ścieżkę skryptu:
pakiet/ai/kod/retinaface_mb_320/rf_onnx.py

### 1.1.3 object_detect

Funkcja: Wykrywanie klasyfikacji obiektów, klasyfikacja 80

Ścieżka programu:`/app/ai/shell`

Biegać:
Wykonywanie modelu `./object_detect_demo_bf16.sh`nieilościowego
Wykonać model kwantyzacji uint8,`./object_detect_demo_uint8.sh`

Kompilacja i instalacja modelu jest szczegółowo opisana w pliku package/ai/ai.mk

Skompiluj ścieżkę skryptu:
pakiet/ai/kod/object_detect_demo/od_onnx.py

## 1.2 ffmpeg

`ffmpeg``ffmpeg-4.4`Przeniesiony na otwarty kod źródłowy, dodany`0001-buildroot-ffmpeg-0.1.patch` dla dodatków Service Pack

- `ff_k510_video_demuxer`: Steruje wejściem ISP, do którego się odwołuje`libvideo.so`
- `ff_libk510_h264_encoder`: Sterowanie kodowaniem sprzętowym h264, odniesienie`libvenc.so`

Konfigurowalne parametry można przeglądać za pomocą dyrektywy pomocy

```shell
ffmpeg -h encoder=libk510_h264 #查看k510编码器的参数
ffmpeg -h demuxer=libk510_video #查看demuxer的配置参数
```

Szczegółowe instrukcje dotyczące uruchamiania można znaleźć w[ K510_Multimedia_Developer_Guides.md](./K510_Multimedia_Developer_Guides.md)

## 1.3 alsa_demo

Program demonstracyjny alsa znajduje się w`/app/alsa_demo` katalogu:

Przygotowanie do biegu:
(1) Podłącz słuchawki

Uruchom demo alsa:

```shell
cd /app/alsa_demo/
./alsa_demo c #录音到文件capture.pcm，demo程序仅作参考，可以参考package/alsa_demo的源码。
./alsa_demo p #播放capture.pcm
```

## 1.4 Demo TWOD

Jak uruchomić obrót:

```shell
cd /app/twod_app
./twod-rotation-app
```

Skopiuj .yuv wejściowy do monitora YUV i ustaw rozmiar 1080 x 1920, format wyświetlania nv12, wynik jest następujący
![wyjście.yuv](../zh/images/sdk_application/driver-twod-output-1080x1920.jpg)

Korzystanie ze skalera

```shell
cd /app/twod_app
./twod-scaler-app
```

Skopiuj .yuv ouput do monitora YUV i ustaw rozmiar 640x480, format wyświetlania nv12, wynik jest następujący
![ouput.yuv](../zh/images/sdk_application/driver-twod-output-640x480.jpg)

Jak uruchomić rgb2yuv:

```shell
cd /app/twod_app
./twod-osd2yuv-app
```

Skopiuj .yuv wyjścia na monitor YUV i ustaw rozmiar 320x240, format wyświetlania nv12, wynik jest następujący
![ouput.yuv](../zh/images/sdk_application/twod-osd2yuv-app.jpg)

Uruchom użycie yuv2rgb:

```shell
cd /app/twod_app
./twod-scaler-output-rgb888-app
```

Skopiuj .yuv wejściowe na monitor rgb888 i ustaw rozmiar 640x480, format wyświetlania rgb24, wynik jest następujący
![ouput.yuv](../zh/images/sdk_application/driver-twod-output-640x480.jpg)

Uruchom wyjście yuv na nakładce osd użycie:

```shell
cd /app/twod_app
./twod-scaler-overlay-osd-app
```

Skopiuj .yuv ouput do monitora, aby ustawić rozmiar 640x480, format wyświetlania nv12, wynik jest następujący
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

Sterownik RTC rejestruje węzeł urządzenia build /dev/rtc0.

Warstwa aplikacji jest zgodna ze standardową metodą programowania RTC w sterowniku wywołania systemowego Linux i zaleca się wyłączenie drukowania informacji o jądrze za pośrednictwem konsoli powłoki przed uruchomieniem procedury referencyjnej.

```shell
echo 0 > /proc/sys/kernel/printk
```

Przejdź do katalogu /app/rtc i wprowadź następujące polecenie, aby uruchomić aplikację rtc.

```shell
cd /app/rtc
./rtc 2021-11-3 21:10:59
```

Wynikiem wykonania programu jest:

![](../zh/images/sdk_application/image-rtc.png)

Główny fragment kodu programu demonstracyjnego RTC jest następujący, zapoznaj się z kodem w folderze package/rtc, aby uzyskać szczegółowe informacje.

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

## 1.6 Wersja demonstracyjna WDT

K510 ma w sumie trzy watchdogi, a sterownik WDT rejestruje węzły urządzeń generate /dev/watchdog0, /dev/watchdog1, /dev/watchdog2.

Warstwa aplikacji jest zgodna ze standardową metodą programowania WDT w sterowniku wywołania systemowego Linux, pierwszy parametr aplikacji wathdog może wynosić odpowiednio 0, 1, reprezentować watchdog0, watchdog1, drugi parametr reprezentuje czas limitu czasu (jednostki sekund), który można ustawić, na przykład następujące polecenie wskazuje początek watchdog0, watchdog0 czas przepełnienia 40 sekund.

```shell
cd /app/watchdog
./watchdog 0 40
```

Po uruchomieniu program będzie karmił watchdoga co 1 sekundę w odstępach czasu, gdy znak stop zostanie wprowadzony w terminalu powłoki, aplikacja przestanie karmić psa, a watchdog zresetuje ponowne uruchomienie urządzenia po przekroczeniu limitu czasu ustawienia, zapoznaj się z kodem pod folderem package/watchdog, aby uzyskać szczegółowe informacje.

Wynikiem wykonania programu jest:

![](../zh/images/sdk_application/image-watchdog.png)

**Uwaga**: Obecny moduł watchdog k510 ma częstotliwość zegara roboczego 757575 Hz, a czas limitu czasu w sekundach musi zostać przekonwertowany na limit czasu rzeczywistej częstotliwości zegara roboczego watchdoga, która jest obliczana jako 2 ^ n / 757575, więc rzeczywisty czas limitu czasu będzie większy lub równy limitowi czasu wejściowego. 

Rzeczywisty limit czasu jest obliczany w następujący sposób:

1) Wprowadź 40, 2^25/757575=44 > 40, 2^24/757575=22 < 40, więc jest ustawiona na 44 sekundy;

2) Wprowadź 155, 2^27/757575=177 > 155, więc jest ustawiona na 177 sekund;

3) Wprowadź 2000, 2^31/757575=2834 > 2000, więc jest ustawiona na 2834 sekundy;

## 1.7 Demo UART

K510 ma w sumie 4 porty szeregowe, bieżący sterownik w portach szeregowych 2, 3 nie jest włączony, sterownik portu szeregowego 0 zarejestruje się w celu wygenerowania węzłów urządzeń /dev/ttyS0.

Warstwa aplikacji jest zgodna ze standardową metodą programowania UART w sterowniku wywołania systemowego Linux. Pierwszym parametrem aplikacji uart mogą być 0 i 1, które reprezentują odpowiednio uart0 i uart1.

Płytka rozwojowa używa sieci przewodowej do łączenia się z routerem, dzięki czemu płytka rozwojowa i debugowanie komputera w sieci, gdy płytka rozwojowa jest włączona, automatycznie uzyska adres IP, wprowadzi polecenie ifconfig w terminalu szeregowym powłoki płytki rozwojowej, aby uzyskać adres IP, a komputer debugujący używa tego adresu IP do otwarcia okna telent, łącząc płytkę rozwojową za pośrednictwem połączenia telent. Na przykład operacja debugowania komputera w celu podłączenia płytki programistycznej za pomocą telent przez MobaXterm jest pokazana na poniższym rysunku.

![](../zh/images/sdk_application/image-uart-mobaxterm.png)

Wprowadź następujące polecenie w oknie terminala telent, aby rozpocząć pracę portu szeregowego 0.

```shell
cd /app/uart
./uart 0
```

Wprowadź zawartość, którą chcesz wysłać w oknie telent, możesz zobaczyć otrzymane dane w oknie terminala szeregowego powłoki, zapoznaj się z kodem w folderze package/crb_demo/uart, aby uzyskać szczegółowe informacje.
Na przykład dane wejściowe dla okna telent:

![](../zh/images/sdk_application/image-uart-telent.png)

Odpowiednie okno terminala szeregowego Shell wyświetla:

![](../zh/images/sdk_application/image-uart-shell.png)

## 1.8 Demo ETH

Warstwa aplikacji jest zgodna ze standardowym sterownikiem wywołań metody programowania ETH w systemach Linux.

### 1.8.1 Klient

Urządzenie jako klient, wprowadź katalog /app/client, wprowadź następujące polecenie, aby uruchomić aplikację kliencką, pierwszy parametr aplikacji ETH wskazuje adres IP serwera w celu ustanowienia łącza TCP, na przykład wprowadź następujące polecenie, aby uruchomić program ETH i serwer 10.20.1.13 w celu nawiązania komunikacji.

```shell
cd /app/client
./client 10.20.1.13
```

Podłącz serwer, aby komunikować się za pośrednictwem protokołu tcp, uruchom program serwera na innym komputerze Ubuntu, zapoznaj się z folderem pakietu / aplikacji / klienta, aby uzyskać szczegółowe informacje.

Wyświetl dzienniki po stronie urządzenia:

![](../zh/images/sdk_application/image-client.png)

### 1.8.2 Serwer

Urządzenie wchodzi do katalogu /app/server jako serwer, na przykład wprowadź następujące polecenie, aby uruchomić program serwera.

```shell
cd /app/server
./server
```

Uruchom program kliencki na innym komputerze Ubuntu, podłącz serwer za pośrednictwem protokołu tcp, aby się komunikować, aby uzyskać szczegółowe informacje, zapoznaj się z folderem pakietu / crb_demo / serwera.

Wyświetl dzienniki po stronie urządzenia:

 ![](../zh/images/sdk_application/image-server.png)

## 1.9 Demo SDMMC

K510 ma w sumie 3 główne kontrolery SDMMC, płytka rozwojowa SDMMC0 służy do podłączenia eMMC, SDMMC1 służy do modułów WIFI, a kontroler SDMMC2 służy do podłączania kart Sdcard.

Sterownik SDMMC rejestruje się w celu wygenerowania /dev/mmcblk0, a sterownik EMMC rejestruje się jako węzeł urządzenia /dev/mmcblk1.

Karta SD zostanie automatycznie zamontowana do /root/data po uruchomieniu systemu, wejdzie do katalogu /app/write_read_file, pierwszy parametr aplikacji SDMMC wskaże plik do odczytu i zapisu, np. karta SD zamontowana w /root/data, można odczytywać i zapisywać pliki w katalogu /root/data/, najpierw zapisywać, a następnie odczytywać, Wprowadź następujące polecenie, aby uruchomić aplikację SDMMC do odczytu i zapisu na karcie SD oraz obliczyć prędkość odczytu i zapisu (jednostka m / s).

```shell
cd /app/write_read_file
./write_read_file /root/data/test.txt
```

Aby włączyć odczyt i zapis danych 1G na karcie SD, zapoznaj się z folderem / aplikacją / write_read_file folderze.

![](../zh/images/sdk_application/image-sdmmc.png)

## 1.10 Demo SHA/AES

Demo SHA/AES używa jądra Linuksa do eksportowania AF_ALG typu interfejsu Netlink i używa interfejsu API szyfrowania jądra w przestrzeni użytkownika. Proszę odnieść się do .<https://www.kernel.org/doc/html/latest/crypto/userspace-if.html> 

Parametr:
-h Drukuje informacje pomocy
-t typ algorytmu: hash, skcipher
-n Nazwy algorytmów: sha256, ecb(aes), cbc(aes)
-x operacja deszyfrowania
-k AES KEY (ciąg szesnastkowy)
-v AES IV (ciąg szesnastkowy)

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

test ecb(aes) 128:

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

Szyfrowanie AES-ECB-128 i aes-cbc-128 wymaga 16-bajtowego wyrównania tekstu jawnego, a niewystarczające zostanie automatycznie wypełnione cyfrą 0.

## 1.11 Demo TRNG

Demo TRNG generuje losową liczbę o określonej długości, odczytując urządzenie znakowe /dev/hwrng, wyprowadzane jako ciąg szesnastkowy.

Znaczenie parametru wejściowego ./trng:

-h Drukuje informacje pomocy

-b Określa długość wyjściowej liczby losowej w bajtach

![](../zh/images/sdk_application/image_trng.png)

## 1.12 Demo DRM

Demo Drm demonstruje wielowarstwowe możliwości sprzętowe vo.

Vo ma w sumie 8 warstw:

1) Warstwa tła, można skonfigurować kolor tła.

2) Layer0 to warstwa wideo, obsługuje YUV422 i YUV420, obsługuje formaty NV12 i NV21, może być dopasowana po stronie rozmiaru i obsługuje skalowanie sprzętowe w górę i w dół.

3) Warstwa 1-warstwa3 to warstwa wideo, obsługująca YUV422 i YUV420, obsługująca formaty NV12 i NV21, a strona rozmiaru może być dopasowana.

4) Warstwa 4-warstwa6 to warstwa OSD, która obsługuje wiele formatów ARGB.

Po uruchomieniu tablicy wprowadź katalog /app/drm_demo i wprowadź polecenie:

```shell
cd /app/drm_demo
./drm_demo
```

Uruchom drm_demo aplikację, drm_demo wyświetlone:

![](../zh/images/sdk_application/image_drm_demo.png)

## 1.13 V4L2_DRM demo

v4l2_drm demonstracyjna demonstruje funkcjonalność wejścia i wyświetlacza kamery.

Po uruchomieniu tablicy wprowadź katalog /app/mediactl_lib i wprowadź polecenie:

```shell
cd /app/mediactl_lib
./v4l2_drm.out -f video_drm_1080x1920.conf -e 1
或者
./v4l2_drm.out -f video_drm_1920x1080.conf
```

Uruchom aplikację v4l2_drm.out i wyświetlacz v4l2_drm.out:

![](../zh/images/sdk_application/image_v4l2_drm_demo.png)

## 1.14 LvGL demo

Przejdź do /app/lvgl i uruchom następujące polecenie:

```shell
cd /app/lvgl
./lvgl
```

Efekt wyświetlania jest następujący:![](../zh/images/sdk_application/image_lvgl.png)

## 1.15 Demo PWM

Sterownik PWM rejestruje węzły urządzeń generate /sys/class/pwm/pwmchip0 i /sys/class/pwm/pwmchip3.

Ten przykład można skonfigurować i włączyć odpowiednio dla pwm0 i pwm1, w katalogu /app/pwm, pierwszy parametr aplikacji pwm wskazuje okres ustawienia pwm, jednostka to ns, drugi parametr ustawia czas "ON" w cyklu pwm, jednostka to ns, trzeci parametr może wynosić 0, 1, reprezentujący pwm0 i pwm1, na przykład wprowadź następujące polecenie, aby włączyć pwm0, cykl to 1s, cykl to 1s, cykl pracy to 100000000/ 500000000 * 100% = 50%, proszę zapoznać się z folderem / app / pwm folder, aby uzyskać szczegółowe kody.

```shell
cd /app/pwm
./pwm 1000000000 500000000 0
```

Wynikiem wykonania programu jest:

![](../zh/images/sdk_application/image-pwm.png)

Po podłączeniu pinu 28 płytki rozwojowej K510 CRB1.2 J15 przez oscyloskop można zaobserwować na oscyloskopie wzór przebiegu z okresem 1 sekundy i cyklem pracy 50%.

## 1.16 Demo WIFI

Po załadowaniu sterownika modułu WiFi generowana jest bezprzewodowa karta sieciowa wlan0, która jest zgodna ze standardowym sterownikiem portu sieciowego i zwykle odnosi się do programowania gniazd TCP /IP.

1) Otwórz "Mobilny hotspot" w notatniku, a następnie ustaw nazwę i hasło hotspotu
2) Uruchom Program NetAssist na notebooku, skonfiguruj typ protokołu, adres IP hosta lokalnego, port hosta lokalnego, ustawienia odbierania, ustawienia wysyłania i dane, które mają zostać wysłane, jak pokazano na poniższym rysunku:

![](../zh/images/sdk_application/image_wifi_1.png)

3) Format parametru programu testowego wifi to:

```shell
./wifi <AP name> <password> <local ip> <server ip>
```

Na przykład wprowadź katalog /app/wifi, wprowadź polecenie, aby uruchomić program testowy Wi-Fi, a wynik wykonania programu jest następujący:

![](../zh/images/sdk_application/image_wifi_2.png)

## 1.17 GPIO_KEYS demo

Sterownik klucza wykorzystuje samo jądro Linuksa zintegrowane z ogólnym sterownikiem kluczy GPU opartym na podsystemie wejściowym, a po załadowaniu sterownika węzeł monitorujący zdarzenia eventX jest generowany w katalogu /dev/input, a X jest numerem sekwencyjnym węzła zdarzenia, który można przeglądać za pomocą cat /proc/bus/input/devices

procedura gpio-keys blokująca odczytywanie zdarzeń raportowania kluczy i drukowanie informacji o zdarzeniach, jej informacje obejmują kodowanie i akcję klucza, kod klucza do identyfikacji tożsamości klucza, akcja klucza jest podzielona na wciśnięta i zwolniona, w wydaniu klucza, gdy procedura obliczy czas trwania naciśnięcia

Wynik wykonania programu pokazano na poniższym rysunku:![](../zh/images/sdk_application/image-gpio-keys.png)

**Zrzeczenie się odpowiedzialności za **tłumaczenie  
Dla wygody klientów Canaan używa tłumacza AI do tłumaczenia tekstu na wiele języków, które mogą zawierać błędy. Nie gwarantujemy dokładności, rzetelności ani terminowości dostarczonych tłumaczeń. Canaan nie ponosi odpowiedzialności za jakiekolwiek straty lub szkody spowodowane poleganiem na dokładności lub wiarygodności przetłumaczonych informacji. W przypadku różnic w treści tłumaczeń w różnych językach, pierwszeństwo ma chińska wersja uproszczona. 

Jeśli chcesz zgłosić błąd lub niedokładność tłumaczenia, skontaktuj się z nami pocztą.