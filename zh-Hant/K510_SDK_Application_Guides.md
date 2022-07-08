![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 SDK 應用指南</font>**

<font face="黑体"  size=3>文件版本：V1.0.0</font>

<font face="黑体"  size=3>發佈日期：2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**免責聲明**</font>
您購買的產品、服務或特性等應受北京嘉楠捷思資訊技術有限公司（“本公司”，下同）商業合同和條款的約束，本文檔中描述的全部或部分產品、服務或特性可能不在您的購買或使用範圍之內。 除非合同另有約定，本公司不對本文檔的任何陳述、資訊、內容的準確性、可靠性、完整性、行銷型、特定目的性和非侵略性提供任何明示或默示的聲明或保證。 除非另有約定，本文檔僅作為使用指導的參考。
由於產品版本升級或其他原因，本文檔內容將可能在未經任何通知的情況下，不定期進行更新或修改。 

**<font face="黑体"  size=3>商標聲明</font>**

“<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />”、“Canaan”圖示、嘉楠和嘉楠其他商標均為北京嘉楠捷思資訊技術有限公司的商標。 本文檔可能提及的其他所有商標或註冊商標，由各自的所有人擁有。 

**<font face="黑体"  size=3>版權所有©2022北京嘉楠捷思資訊技術有限公司</font>**
本文檔僅適用K510平台開發設計，非經本公司書面許可，任何單位和個人不得以任何形式對本文檔的部分或全部內容傳播。 

**<font face="黑体"  size=3>北京嘉楠捷思資訊技術有限公司</font>**
網址：canaan-creative.com
商務垂詢：salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# 前言
**<font face="黑体"  size=5>文件目的</font>**
本文檔為K510 SDK 應用實例的說明文檔。 

**<font face="黑体"  size=5>讀者物件</font>**

本文檔（本指南）主要適用的人員：

- 軟體開發人員
- 技術支持人員

**<font face="黑体"  size=5>修訂記錄</font>**
 <font face="宋体"  size=2>修訂記錄累積了每次文檔更新的說明。 最新版本的文件包含以前所有版本的更新內容。 </font>

| 版本號 | 修改者     | 修訂日期   | 修訂說明     |
| :----- | ---------- | ---------- | ------------ |
| 1.0.0 版 | 系統軟體組 | 2022-03-09 | SDK V1.5發佈 |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>目 錄</font>**

[目錄]

<div style="page-break-after:always"></div>

# 1 Demo應用

## 1.1 ai demo程式

### 1.1.1 說明

nncase 的demo程式源碼位於SDK目錄下的`package/ai`目錄，目錄結構如下：

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

可以參考retinaface_mb_320的源碼和`CMakeLists.txt`添加新的nncase 的demo程式。 

模型的編譯參見`nncase_demo.mk`裡面定義的*POST_INSTALL_TARGET_HOOKS*：

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

模型的編譯需要nncase環境，關於nncase環境的搭建，參考k510_nncase_Developer_Guides.md。 以後nncase有更新，buildroot sdk會同步更新到nncase。

### 1.1.2 視網膜面

功能：人臉檢測，人臉特徵點檢測

程式路徑：
`/app/ai/shell`
執行：
執行非量化模型，`./retinaface_mb_320_bf16.sh`
執行uint8量化模型，`./retinaface_mb_320_uint8.sh`

腳本裡面有關於QOS的設置，下面的兩個demo的設置一樣。

```shell
#devmem phyaddr width value
devmem 0x970E00fc 32 0x0fffff00
devmem 0x970E0100 32 0x000000ff
devmem 0x970E00f4 32 0x00550000
```

跑demo時，需要優先保證屏幕顯示正常，即調整顯示相關的QoS為高優先順序。
QOS_CTRL0.ax25mp write QoS = 5
QOS_CTRL0.ax25mp read QoS = 5
QOS_CTRL2.ispf2k write QoS = 0xf
QOS_CTRL2.ispf2k read QoS = 0xf
QOS_CTRL2.ispr2k write QoS = 0xf
QOS_CTRL2.ispr2k read QoS = 0xf
QOS_CTRL2.isp3dtof write QoS = 0xf
QOS_CTRL3.display read QoS = 0xf
QOS_CTRL3.display write QoS = 0xf

QOS 控制寄存器0（QOS_CTRL0） offset[0x00f4]
 ![qos ctrl0](../zh/images/sdk_application/demo_nncase_qos_ctrl0.png)

QOS 控制寄存器1（QOS_CTRL1） offset[0x00f8]
 ![qos ctrl1](../zh/images/sdk_application/demo_nncase_qos_ctrl1.png)

QOS 控制寄存器2（QOS_CTRL2） offset[0x00fc]
 ![qos ctrl2](../zh/images/sdk_application/demo_nncase_qos_ctrl2.png)

QOS 控制寄存器3（QOS_CTRL3） offset[0x0100]
 ![qos ctrl3](../zh/images/sdk_application/demo_nncase_qos_ctrl3.png)

模型的編譯安裝詳見檔package/ai/ai.mk：

編譯文稿路徑：
package/ai/code/retinaface_mb_320/rf_onnx.py

### 1.1.3 object_detect

功能：物體分類檢測，80分類

程式路徑：`/app/ai/shell`

執行：
執行非量化模型，`./object_detect_demo_bf16.sh`
執行uint8量化模型，`./object_detect_demo_uint8.sh`

模型的編譯安裝詳見檔package/ai/ai.mk

編譯文稿路徑：
package/ai/code/object_detect_demo/od_onnx.py

## 1.2 ffmpeg

`ffmpeg`在`ffmpeg-4.4`開原始程式碼上進行移植，`0001-buildroot-ffmpeg-0.1.patch`為補丁包，增加了

- `ff_k510_video_demuxer`：控制isp輸入，引用了`libvideo.so`
- `ff_libk510_h264_encoder`：控制h264硬體編碼，引用了`libvenc.so`

可以通過help指令查看可配置參數

```shell
ffmpeg -h encoder=libk510_h264 #查看k510编码器的参数
ffmpeg -h demuxer=libk510_video #查看demuxer的配置参数
```

詳細運行說明參考[K510_Multimedia_Developer_Guides.md](./K510_Multimedia_Developer_Guides.md)

## 1.3 alsa_demo

alsa demo程式放在`/app/alsa_demo`目錄下：

執行準備：
（1）插上耳機

執行alsa demo：

```shell
cd /app/alsa_demo/
./alsa_demo c #录音到文件capture.pcm，demo程序仅作参考，可以参考package/alsa_demo的源码。
./alsa_demo p #播放capture.pcm
```

## 1.4 二維演示

運行 rotation 使用方法：

```shell
cd /app/twod_app
./twod-rotation-app
```

將ouput.yuv 拷到yuv顯示器上設置尺寸1080 x 1920，顯示格式nv12，結果如下
![output.yuv](../zh/images/sdk_application/driver-twod-output-1080x1920.jpg)

scaler 使用方法

```shell
cd /app/twod_app
./twod-scaler-app
```

將ouput.yuv 拷到yuv顯示器上設置尺寸640x480，顯示格式nv12，結果如下
![ouput.yuv](../zh/images/sdk_application/driver-twod-output-640x480.jpg)

運行 rgb2yuv 使用方法：

```shell
cd /app/twod_app
./twod-osd2yuv-app
```

將ouput.yuv 拷到yuv 顯示器上設置尺寸320x240，顯示格式nv12，結果如下
![ouput.yuv](../zh/images/sdk_application/twod-osd2yuv-app.jpg)

運行 yuv2rgb 使用方法：

```shell
cd /app/twod_app
./twod-scaler-output-rgb888-app
```

將ouput.yuv 拷到rgb888顯示器上設置尺寸640x480，顯示格式rgb24，結果如下
![ouput.yuv](../zh/images/sdk_application/driver-twod-output-640x480.jpg)

執行 輸出yuv上疊加osd 使用方法：

```shell
cd /app/twod_app
./twod-scaler-overlay-osd-app
```

將ouput.yuv 拷到顯示器上設置尺寸640x480，顯示格式nv12，結果如下
![ouput.yuv](../zh/images/sdk_application/twod-scaler-overlay-osd-app.jpg)

應用程式介面：

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

## 1.5 RTC 演示

RTC驅動會註冊生成/dev/rtc0設備節點。

應用層遵循Linux系統中的標準RTC程式設計方法調用驅動，在運行參考例程之前，建議通過shell控制台關閉內核資訊列印。

```shell
echo 0 > /proc/sys/kernel/printk
```

進入/app/rtc目錄，輸入如下命令啟動rtc應用程式。

```shell
cd /app/rtc
./rtc 2021-11-3 21:10:59
```

程式的執行結果為：

![](../zh/images/sdk_application/image-rtc.png)

RTC demo程式的主要代碼片段如下，詳細請參考package/rtc 資料夾下的代碼。

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

## 1.6 WDT 演示

K510一共有三個看門狗，WDT驅動會註冊生成/dev/watchdog0、/dev/watchdog1、/dev/watchdog2 設備節點。

應用層遵循Linux系統中的標準WDT程式設計方法調用驅動，wathdog應用程式第一個參數可為0、1，分別代表watchdog0、watchdog1，第二個參數表示可設置的超時時間（單位秒），例如如下命令表示啟動watchdog0，watchdog0溢出時間40秒。

```shell
cd /app/watchdog
./watchdog 0 40
```

程序啟動后將每間隔1秒喂一次看門狗，當shell終端中輸入stop字元后，應用程式停止喂狗，看門狗將在設置超時時間溢出后複位設備重啟，詳細請參考package/watchdog資料夾下的代碼。

程式的執行結果為：

![](../zh/images/sdk_application/image-watchdog.png)

**注意**：當前k510看門狗模組的工作時鐘頻率為757575Hz，以秒為單位的超時時間需要轉換成看門狗實際的工作時鐘頻率的超時時間，計算公式是2^n/757575，因此實際的超時時間會大於等於輸入的超時時間。 

實際超時時間的計算過程是：

1）輸入40，2^25/757575=44 > 40，2^24/757575=22 < 40，因此設置為44秒;

2）輸入155，2^27/757575=177 > 155，因此設置為177秒;

3）輸入2000，2^31/757575=2834 > 2000，因此設置為2834秒;

## 1.7 UART 演示

K510一共有4個串口，當前驅動中串口2、3沒有使能，串口0驅動會註冊生成/dev/ttyS0設備節點。

應用層遵循Linux系統中的標準UART程式設計方法調用驅動。 uart應用程式第一個參數可為0、1，分別代表uart0、uart1。

將開發板使用有線網連接到路由器，使得開發板和調試PC在一個網路中，當開發板上電后將自動獲取IP，在開發板的shell串口終端中輸入ifconfig命令獲取IP位址，調試PC利用此IP通過telent連接開發板打開一個telent視窗。 例如調試PC通過MobaXterm使用telent連接開發板的操作如下圖。

![](../zh/images/sdk_application/image-uart-mobaxterm.png)

telent終端視窗中輸入如下命令啟動串口0工作。

```shell
cd /app/uart
./uart 0
```

在telent視窗中輸入要發送的內容，可以在shell串口終端視窗看到接收到的數據，詳細請參考package/crb_demo/uart資料夾下的代碼。
例如，telent視窗的輸入：

![](../zh/images/sdk_application/image-uart-telent.png)

對應的Shell串口終端視窗顯示：

![](../zh/images/sdk_application/image-uart-shell.png)

## 1.8 乙太幣演示

應用層遵循Linux系統中的標準ETH程式設計方法調用驅動。

### 1.8.1 用戶端

設備作為client端，進入/app/client目錄，輸入如下命令啟動client應用程式，ETH應用程式第一個參數表示要建立TCP連結的伺服器ip位址，例如輸入如下命令表示啟動ETH程式與10.20.1.13的server建立通信。

```shell
cd /app/client
./client 10.20.1.13
```

通過tcp協議連接server進行通信，在另一台ubuntu機器上運行server程式，詳細代碼請參考package/app/client資料夾下內容。

裝置端顯示紀錄：

![](../zh/images/sdk_application/image-client.png)

### 1.8.2 伺服器

設備作為server端，進入/app/server目錄，例如輸入如下命令表示啟動server程式。

```shell
cd /app/server
./server
```

在另一台ubuntu機器上運行client程式，通過tcp協議連接server進行通信，詳細代碼請參考package/crb_demo/server資料夾下內容。

裝置端顯示紀錄：

 ![](../zh/images/sdk_application/image-server.png)

## 1.9 SDMMC 演示

K510一共有3個SDMMC主控制器，開發板上SDMMC0用於接eMMC，SDMMC1用於WIFI模組，SDMMC2控制器用於接sdcard。

SDMMC驅動會註冊生成/dev/mmcblk0，EMMC驅動會註冊成/dev/mmcblk1設備節點。

SD卡在系統啟動後會自動掛載到/root/data ，進入/app/write_read_file目錄，SDMMC應用程式第一個參數表示要進行讀寫操作的檔，如SD卡掛載到/root/data，可對/root/data/目錄下的檔進行讀寫操作，先寫后讀， 輸入如下命令啟動SDMMC應用程式對SD卡進行讀和寫的操作並計算讀寫速度（單位m/s）。

```shell
cd /app/write_read_file
./write_read_file /root/data/test.txt
```

開啟對SD卡進行1G數據的讀寫，代碼請參考package/app/write_read_file資料夾下的內容。

![](../zh/images/sdk_application/image-sdmmc.png)

## 1.10 SHA/AES 演示

SHA/AES demo 使用Linux 內核匯出 AF_ALG 類型的 Netlink 介面，在用戶空間使用內核加密 API。 詳細資訊請參考<https://www.kernel.org/doc/html/latest/crypto/userspace-if.html>。 

參數：
-h 列印幫助資訊
-t 演算法類型：hash、skcipher
-n 演算法名稱：sha256、ecb（aes）、cbc（aes）
-x 解密操作
-k AES KEY（16進位字串）
-v AES IV（16進位字串）

![](../zh/images/sdk_application/image_crypto_help.png)

sha256 測試：

```shell
cd /app/crypto
echo -n "This is a test file, hello world" > plain.txt
./crypto -t hash -n "sha256" plain.txt sha256.txt
xxd -p -c 32 sha256.txt
sha256sum plain.txt
```

![](../zh/images/sdk_application/image_crypto_sha256.png)

ecb（aes） 128 測試：

```shell
cd /app/crypto
echo -n "This is a test file, hello world" > plain.txt
./crypto -t skcipher -n "ecb(aes)" -k 00112233445566778899aabbccddeeff plain.txt ecb_aes_en.bin
./crypto -t skcipher -n "ecb(aes)" -k 00112233445566778899aabbccddeeff  -x ecb_aes_en.bin ecb_aes_de.bin
cmp ecb_aes_de.bin plain.txt
cat ecb_aes_de.bin
```

![](../zh/images/sdk_application/image_crypto_ecb.png)

全血細胞計數 128 次測試

```shell
cd /app/crypto
echo -n "This is a test file, hello world" > plain.txt
./crypto -t skcipher -n "cbc(aes)" -k 00112233445566778899aabbccddeeff -v 00112233445566778899aabbccddeeff plain.txt cbc_aes_en.bin
./crypto -t skcipher -n "cbc(aes)" -k 00112233445566778899aabbccddeeff -v 00112233445566778899aabbccddeeff -x cbc_aes_en.bin cbc_aes_de.bin
cmp cbc_aes_de.bin plain.txt
cat cbc_aes_de.bin
```

![](../zh/images/sdk_application/image_crypto_cbc.png)

aes-ecb-128和aes-cbc-128加密時要求明文要16位元組對齊，不足會自動補0。

## 1.11 TRNG 演示

TRNG demo通過讀取/dev/hwrng字元設備產生指定長度的隨機數，按16進位字元串輸出。

./trng的輸入參數含義：

-h 列印幫助資訊

-b 指定輸出隨機數長度，單位byte

![](../zh/images/sdk_application/image_trng.png)

## 1.12 數字版權管理演示

drm demo展示了VO硬體多圖層功能。

VO共有8個layer：

1）背景層，可配置背景色。

2）layer0是video層，支援YUV422和YUV420，支援NV12和NV21格式，大小端可配，支持硬體scaling up和scaling down。

3）layer1-layer3是video層，支援YUV422和YUV420，支援NV12和NV21格式，大小端可配。

4）layer4-layer6是OSD層，支持多種ARGB格式。

開發板啟動後進入/app/drm_demo目錄，輸入命令：

```shell
cd /app/drm_demo
./drm_demo
```

啟動drm_demo應用程式， drm_demo顯示效果：

![](../zh/images/sdk_application/image_drm_demo.png)

## 1.13 V4L2_DRM演示

v4l2_drm demo展示了攝像頭輸入和顯示的功能。

開發板啟動後進入/app/mediactl_lib目錄，輸入命令：

```shell
cd /app/mediactl_lib
./v4l2_drm.out -f video_drm_1080x1920.conf -e 1
或者
./v4l2_drm.out -f video_drm_1920x1080.conf
```

啟動v4l2_drm.out應用程式，v4l2_drm.out顯示效果：

![](../zh/images/sdk_application/image_v4l2_drm_demo.png)

## 1.14 LVGL 演示

進入/app/lvgl，運行以下命令：

```shell
cd /app/lvgl
./lvgl
```

顯示效果如下：![](../zh/images/sdk_application/image_lvgl.png)

## 1.15 PWM 演示

PWM驅動會註冊生成/sys/class/pwm/pwmchip0和/sys/class/pwm/pwmchip3設備節點。

本例程可分別對pwm0和pwm1進行配置和使能，進入/app/pwm目錄，pwm應用程式第一個參數表示設置pwm的週期，單位為ns，第二個參數設置pwm一個週期中“ON”的時間，單位為ns，第三個參數可以為0、1，分別代表pwm0和pwm1，例如輸入如下命令表示使能pwm0，週期為1s，佔空比為1000000000/ 500000000*100% = 50%，詳細代碼請參考package/app/pwm資料夾下的內容。

```shell
cd /app/pwm
./pwm 1000000000 500000000 0
```

程式的執行結果為：

![](../zh/images/sdk_application/image-pwm.png)

通過示波器連接K510 CRB1.2開發板J15的28號引腳，可以示波器上觀察到一個週期為1秒，佔空比為50%的波形圖。

## 1.16 無線網路演示

WiFi模組驅動載入後會生成無線網卡wlan0，遵循標準網口驅動，正常參考TCP/IP socket程式設計。

1）在筆記本打開「移動熱點」，然後設置熱點的名稱和密碼
2）在筆記本上啟動NetAssist，配置協定類型、本地主機IP、本地主機埠、接收設置、發送設置及需要發送的數據，如下圖：

![](../zh/images/sdk_application/image_wifi_1.png)

3）wifi測試程式的參數格式為：

```shell
./wifi <AP name> <password> <local ip> <server ip>
```

例如進入/app/wifi目錄，輸入啟動wifi測試程式命令，程式的執行結果如下圖：

![](../zh/images/sdk_application/image_wifi_2.png)

## 1.17 GPIO_KEYS演示

按鍵驅動使用linux kernel自身集成的基於input子系統的通用gpio-keys驅動，驅動載入后在/dev/input目錄下生成事件監控節點eventX，X為事件節點序號，可以通過cat /proc/bus/input/devices查看

gpio-keys例程阻塞式讀取按鍵上報事件並列印事件資訊，其資訊包括按鍵編碼和按鍵動作，按鍵編碼標識按鍵身份，按鍵動作分為pressed和released，在按鍵release時例程會計算按鍵按下的持續時間

程式執行結果如下圖所示：![](../zh/images/sdk_application/image-gpio-keys.png)

**翻譯免責聲明**  
為方便客戶，Canaan 使用 AI 翻譯程式將文字翻譯為多種語言，它可能包含錯誤。 我們不保證提供的譯文的準確性、可靠性或時效性。 對於因依賴已翻譯信息的準確性或可靠性而造成的任何損失或損害，Canaan 概不負責。 如果不同語言翻譯之間存在內容差異，以簡體中文版本為準。 

如果您要報告翻譯錯誤或不準確的問題，歡迎通過郵件與我們聯繫。