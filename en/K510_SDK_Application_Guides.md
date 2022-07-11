![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 SDK Application Guide</font>**

<font face="黑体"  size=3>Document version: V1.0.0</font>

<font face="黑体"  size=3>Published: 2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Disclaimer**</font>
The products, services or features you purchase shall be subject to the commercial contracts and terms of Beijing Canaan Jiesi Information Technology Co., Ltd. ("the Company", the same hereinafter), and all or part of the products, services or features described in this document may not be within the scope of your purchase or use. Except as otherwise agreed in the contract, the Company disclaims all representations or warranties, express or implied, as to the accuracy, reliability, completeness, marketing, specific purpose and non-aggression of any representations, information, or content of this document. Unless otherwise agreed, this document is provided as a guide for use only.
Due to product version upgrades or other reasons, the contents of this document may be updated or modified from time to time without any notice.

**<font face="黑体"  size=3>Trademark Notices</font>**

""<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, "Canaan" icon, Canaan and other trademarks of Canaan and other trademarks of Canaan are trademarks of Beijing Canaan Jiesi Information Technology Co., Ltd. All other trademarks or registered trademarks that may be mentioned in this document are owned by their respective owners.

**<font face="黑体"  size=3>Copyright ©2022 Beijing Canaan Jiesi Information Technology Co., Ltd</font>**
This document is only applicable to the development and design of the K510 platform, without the written permission of the company, no unit or individual may disseminate part or all of the content of this document in any form.

**<font face="黑体"  size=3>Beijing Canaan Jiesi Information Technology Co., Ltd</font>**
URL: canaan-creative.com
Business Enquiries: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# preface
**<font face="黑体"  size=5>Document purpose</font>**
This document is a description document for the K510 SDK application example.

**<font face="黑体"  size=5>Reader Objects</font>**

The main people to whom this document (this guide) applies:

- Software developers
- Technical support personnel

**<font face="黑体"  size=5>Revision history</font>**
 <font face="宋体"  size=2>The revision history accumulates a description of each document update. The latest version of the document contains updates for all previous versions. </font>

| The version number | Modified by     | Date of revision   | Revision Notes     |
| :----- | ---------- | ---------- | ------------ |
| V1.0.0 | System software groups | 2022-03-09 | SDK V1.5 released |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contents</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Demo app

## 1.1 ai demo program

### 1.1.1 Description

The source code of the demo program of nncase is located in the directory under the SDK directory`package/ai`, and the directory structure is as follows:

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

You can refer to the source code of the retinaface_mb_320 and`CMakeLists.txt` add a new nncase demo program.

For the compilation of the model, see`nncase_demo.mk` the POST_INSTALL_TARGET_HOOKS*defined therein*:

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

The compilation of the model requires an nncase environment, and for the construction of the nncase environment, refer to k510_nncase_Developer_Guides.md. In the future, the nncase has an update, and the buildroot sdk will be updated to the nncase synchronously.

### 1.1.2 retinaface

Function: Face detection, face landmark detection

Program Path:
`/app/ai/shell`
Run:
Execute a non-quantitative model`./retinaface_mb_320_bf16.sh`
Perform the uint8 quantization model,`./retinaface_mb_320_uint8.sh`

There are settings for QOS in the script, the same as for the following two demos.

```shell
#devmem phyaddr width value
devmem 0x970E00fc 32 0x0fffff00
devmem 0x970E0100 32 0x000000ff
devmem 0x970E00f4 32 0x00550000
```

When running a demo, it is necessary to prioritize ensuring that the screen display is normal, that is, adjust the QoS related to the display to a high priority.
QOS_CTRL0.ax25mp write QoS = 5
QOS_CTRL0.ax25mp read QoS = 5
QOS_CTRL2.ispf2k write QoS = 0xf
QOS_CTRL2.ispf2k read QoS = 0xf
QOS_CTRL2.ispr2k write QoS = 0xf
QOS_CTRL2.ispr2k read QoS = 0xf
QOS_CTRL2.isp3dtof write QoS = 0xf
QOS_CTRL3.display read QoS = 0xf
QOS_CTRL3.display write QoS = 0xf

QOS control register 0(QOS_CTRL0) offset[0x00f4]
 ![qos ctrl0](../zh/images/sdk_application/demo_nncase_qos_ctrl0.png)

QOS control register 1 (QOS_CTRL1) offset[0x00f8]
 ![qos ctrl1](../zh/images/sdk_application/demo_nncase_qos_ctrl1.png)

QOS control register 2 (QOS_CTRL2) offset[0x00fc]
 ![qos ctrl2](../zh/images/sdk_application/demo_nncase_qos_ctrl2.png)

QOS control register 3 (QOS_CTRL3) offset[0x0100]
 ![qos ctrl3](../zh/images/sdk_application/demo_nncase_qos_ctrl3.png)

The compilation and installation of the model is detailed in the file package/ai/ai.mk:

Compile script path:
package/ai/code/retinaface_mb_320/rf_onnx.py

### 1.1.3 object_detect

Function: Object classification detection, 80 classification

Program Path:`/app/ai/shell`

Run:
Execute a non-quantitative model`./object_detect_demo_bf16.sh`
Perform the uint8 quantization model,`./object_detect_demo_uint8.sh`

The compilation and installation of the model is detailed in the file package/ai/ai.mk

Compile script path:
package/ai/code/object_detect_demo/od_onnx.py

## 1.2 ffmpeg

`ffmpeg``ffmpeg-4.4`Ported on open source code, added`0001-buildroot-ffmpeg-0.1.patch` for service packs

- `ff_k510_video_demuxer`: Controls the isp input, referenced`libvideo.so`
- `ff_libk510_h264_encoder`: Control h264 hardware encoding, referenced`libvenc.so`

Configurable parameters can be viewed via the help directive

```shell
ffmpeg -h encoder=libk510_h264 #查看k510编码器的参数
ffmpeg -h demuxer=libk510_video #查看demuxer的配置参数
```

For detailed run instructions, refer to[K510_Multimedia_Developer_Guides.md](./K510_Multimedia_Developer_Guides.md)

## 1.3 alsa_demo

The alsa demo program is placed in`/app/alsa_demo` the directory :

Run preparation:
(1) Plug in the headphones

Run alsa demo:

```shell
cd /app/alsa_demo/
./alsa_demo c #录音到文件capture.pcm，demo程序仅作参考，可以参考package/alsa_demo的源码。
./alsa_demo p #播放capture.pcm
```

## 1.4 TWOD demo

How to run rotation:

```shell
cd /app/twod_app
./twod-rotation-app
```

Copy the ouput .yuv to the YUV monitor and set the size 1080 x 1920, display format nv12, the result is as follows
![output.yuv](../zh/images/sdk_application/driver-twod-output-1080x1920.jpg)

Using scaler

```shell
cd /app/twod_app
./twod-scaler-app
```

Copy the ouput .yuv to the YUV monitor and set the size 640x480, display format nv12, the result is as follows
![ouput.yuv](../zh/images/sdk_application/driver-twod-output-640x480.jpg)

How to run rgb2yuv:

```shell
cd /app/twod_app
./twod-osd2yuv-app
```

Copy the ouput .yuv to the YUV monitor and set the size 320x240, display format nv12, the result is as follows
![ouput.yuv](../zh/images/sdk_application/twod-osd2yuv-app.jpg)

Run yuv2rgb usage:

```shell
cd /app/twod_app
./twod-scaler-output-rgb888-app
```

Copy the ouput .yuv to the rgb888 monitor and set the size 640x480, the display format rgb24, the result is as follows
![ouput.yuv](../zh/images/sdk_application/driver-twod-output-640x480.jpg)

Run output yuv on overlay osd usage:

```shell
cd /app/twod_app
./twod-scaler-overlay-osd-app
```

Copy the ouput .yuv to the monitor to set the size 640x480, display format nv12, the result is as follows
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

## 1.5 RTC demo

The RTC driver registers the build /dev/rtc0 device node.

The application layer follows the standard RTC programming method in the Linux system call driver, and it is recommended to turn off kernel information printing through the shell console before running the reference routine.

```shell
echo 0 > /proc/sys/kernel/printk
```

Go to the /app/rtc directory and enter the following command to start the rtc application.

```shell
cd /app/rtc
./rtc 2021-11-3 21:10:59
```

The result of the execution of the program is:

![](../zh/images/sdk_application/image-rtc.png)

The main code snippet of the RTC demo program is as follows, please refer to the code under the package/rtc folder for details.

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

## 1.6 WDT demo

The K510 has a total of three watchdogs, and the WDT driver registers the generate /dev/watchdog0, /dev/watchdog1, /dev/watchdog2 device nodes.

The application layer follows the standard WDT programming method in the Linux system call driver, the first parameter of the wathdog application can be 0, 1, represent watchdog0, watchdog1, respectively, the second parameter represents the timeout time (unit seconds) that can be set, for example, the following command indicates the start of watchdog0, watchdog0 overflow time of 40 seconds.

```shell
cd /app/watchdog
./watchdog 0 40
```

After the program starts, it will feed the watchdog every 1 second at intervals, when the stop character is entered in the shell terminal, the application stops feeding the dog, and the watchdog will reset the device restart after the setting timeout overflows, please refer to the code under the package/watchdog folder for details.

The result of the execution of the program is:

![](../zh/images/sdk_application/image-watchdog.png)

**Note**: The current k510 watchdog module has a working clock frequency of 757575Hz, and the timeout time in seconds needs to be converted to the timeout timeout of the actual working clock frequency of the watchdog, which is calculated as 2^n/757575, so the actual timeout time will be greater than or equal to the input timeout timeout.

The actual timeout period is calculated as follows:

1) Enter 40, 2^25/757575=44 > 40, 2^24/757575=22 < 40, so it is set to 44 seconds;

2) Enter 155, 2^27/757575=177 > 155, so it is set to 177 seconds;

3) Enter 2000, 2^31/757575=2834 > 2000, so it is set to 2834 seconds;

## 1.7 UART demo

K510 has a total of 4 serial ports, the current driver in the serial ports 2, 3 is not enabled, serial port 0 driver will register to generate /dev/ttyS0 device nodes.

The application layer follows the standard UART programming method in Linux system call driver. The first parameter of the uart application can be 0 and 1, which represent uart0 and uart1 respectively.

The development board uses a wired network to connect to the router, so that the development board and debugging PC in a network, when the development board is powered on, it will automatically obtain the IP, enter the ifconfig command in the shell serial terminal of the development board to obtain the IP address, and the debugging PC uses this IP to open a telent window by connecting the development board through the telent connection. For example, the operation of debugging a PC to connect a development board using telent through MobaXterm is shown in the following figure.

![](../zh/images/sdk_application/image-uart-mobaxterm.png)

Enter the following command in the telent terminal window to start serial port 0 work.

```shell
cd /app/uart
./uart 0
```

Enter the content you want to send in the telent window, you can see the received data in the shell serial terminal window, please refer to the code under the package/crb_demo/uart folder for details.
For example, the input for the telent window:

![](../zh/images/sdk_application/image-uart-telent.png)

The corresponding Shell serial terminal window displays:

![](../zh/images/sdk_application/image-uart-shell.png)

## 1.8 ETH demo

The application layer follows the standard ETH programming method call driver in Linux systems.

### 1.8.1 Client

The device as the client, enter the /app/client directory, enter the following command to start the client application, the first parameter of the ETH application indicates the server IP address to establish the TCP link, for example, enter the following command to start the ETH program and 10.20.1.13 server to establish communication.

```shell
cd /app/client
./client 10.20.1.13
```

Connect the server to communicate via tcp protocol, run the server program on another ubuntu machine, please refer to the package/app/client folder for details.

Display logs on the device side:

![](../zh/images/sdk_application/image-client.png)

### 1.8.2 Server

The device enters the /app/server directory as the server, for example, enter the following command to start the server program.

```shell
cd /app/server
./server
```

Run the client program on another ubuntu machine, connect the server through the tcp protocol to communicate, for details, please refer to the package/crb_demo/server folder.

Display logs on the device side:

 ![](../zh/images/sdk_application/image-server.png)

## 1.9 SDMMC demo

The K510 has a total of 3 SDMMC main controllers, the development board SDMMC0 is used to connect eMMC, SDMMC1 is used for WIFI modules, and the SDMMC2 controller is used to connect sdcards.

The SDMMC driver registers to generate /dev/mmcblk0 and the EMMC driver registers as the /dev/mmcblk1 device node.

SD card will be automatically mounted to /root/data after system startup, enter the /app/write_read_file directory, the first parameter of the SDMMC application indicates the file to be read and write, such as SD card mounted to /root/data, you can read and write files under the /root/data/ directory, first write and then read, Enter the following command to start the SDMMC application to read and write to the SD card and calculate the read and write speed (unit m/s).

```shell
cd /app/write_read_file
./write_read_file /root/data/test.txt
```

To enable the reading and writing of 1G data to the SD card, please refer to the folder/app/write_read_file folder.

![](../zh/images/sdk_application/image-sdmmc.png)

## 1.10 SHA/AES demo

SHA/AES demo uses the Linux kernel to export AF_ALG type of Netlink interface and uses the kernel encryption API in user space. Please refer to .<https://www.kernel.org/doc/html/latest/crypto/userspace-if.html>

Parameter:
-h Prints the help information
-t algorithm type: hash, skcipher
-n Algorithm names: sha256, ecb(aes), cbc(aes)
-x decryption operation
-k AES KEY (hexadecimal string)
-v AES IV (hexadecimal string)

![](../zh/images/sdk_application/image_crypto_help.png)

sha256 test：

```shell
cd /app/crypto
echo -n "This is a test file, hello world" > plain.txt
./crypto -t hash -n "sha256" plain.txt sha256.txt
xxd -p -c 32 sha256.txt
sha256sum plain.txt
```

![](../zh/images/sdk_application/image_crypto_sha256.png)

ecb(aes) 128 test：

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

AES-ECB-128 and aes-cbc-128 encryption require 16-byte alignment of the plaintext, and the insufficient will automatically be filled with 0.

## 1.11 TRNG demo

The TRNG demo produces a random number of the specified length by reading the /dev/hwrng character device, output as a hexadecimal string.

The input parameter meaning of ./trng:

-h Prints the help information

-b Specifies the output random number length, in bytes

![](../zh/images/sdk_application/image_trng.png)

## 1.12 DRM demo

Drm demo demonstrates the vo hardware multi-layer capabilities.

Vo has a total of 8 layers:

1) Background layer, can be configured background color.

2) Layer0 is a video layer, supports YUV422 and YUV420, supports NV12 and NV21 formats, can be matched on the size side, and supports hardware scaling up and scaling down.

3) Layer1-layer3 is a video layer, supporting YUV422 and YUV420, supporting NV12 and NV21 formats, and the size side can be matched.

4) Layer4-layer6 is the OSD layer that supports multiple ARGB formats.

After the board starts, enter the /app/drm_demo directory and enter the command:

```shell
cd /app/drm_demo
./drm_demo
```

Launch drm_demo application, drm_demo displayed:

![](../zh/images/sdk_application/image_drm_demo.png)

## 1.13 V4L2_DRM demo

v4l2_drm demo demonstrates the functionality of camera input and display.

After the board starts, enter the /app/mediactl_lib directory and enter the command:

```shell
cd /app/mediactl_lib
./v4l2_drm.out -f video_drm_1080x1920.conf -e 1
或者
./v4l2_drm.out -f video_drm_1920x1080.conf
```

Launch the v4l2_drm.out application and v4l2_drm.out display:

![](../zh/images/sdk_application/image_v4l2_drm_demo.png)

## 1.14 LVGL demo

Go to /app/lvgl and run the following command:

```shell
cd /app/lvgl
./lvgl
```

The display effect is as follows:![](../zh/images/sdk_application/image_lvgl.png)

## 1.15 PWM demo

The PWM driver registers the generate /sys/class/pwm/pwmchip0 and /sys/class/pwm/pwmchip3 device nodes.

This example can be configured and enabled for pwm0 and pwm1 respectively, into the /app/pwm directory, the first parameter of the pwm application indicates the period of setting pwm, the unit is ns, the second parameter sets the time of "ON" in a cycle of pwm, the unit is ns, the third parameter can be 0, 1, representing pwm0 and pwm1, for example, enter the following command to enable pwm0, the cycle is 1s, the duty cycle is 100000000/ 500000000*100% = 50%, please refer to the folder/app/pwm folder for detailed codes.

```shell
cd /app/pwm
./pwm 1000000000 500000000 0
```

The result of the execution of the program is:

![](../zh/images/sdk_application/image-pwm.png)

By connecting pin 28 of the K510 CRB1.2 development board J15 through the oscilloscope, a waveform pattern with a period of 1 second and a duty cycle of 50% can be observed on the oscilloscope.

## 1.16 WIFI demo

After the WiFi module driver is loaded, the wireless network card wlan0 is generated, which follows the standard network port driver and normally refers to TCP/IP socket programming.

1) Open "Mobile Hotspot" in the notebook, and then set the name and password of the hotspot
2) Start NetAssist on the notebook, configure the protocol type, local host IP, local host port, receive settings, send settings, and the data that needs to be sent, as shown in the following figure:

    ![](../zh/images/sdk_application/image_wifi_1.png)

3) The parameter format of the wifi test program is:

    ```shell
    ./wifi <AP name> <password> <local ip> <server ip>
    ```

    For example, enter the /app/wifi directory, enter the command to start the wifi test program, and the execution result of the program is as follows:

    ![](../zh/images/sdk_application/image_wifi_2.png)

## 1.17 GPIO_KEYS demo

The key driver uses the linux kernel itself integrated with the generic gpu-keys driver based on the input subsystem, and after the driver is loaded, the event monitoring node eventX is generated in the /dev/input directory, and X is the event node sequence number, which can be viewed through cat /proc/bus/input/devices

gpio-keys routine blocking reading key reporting events and printing event information, its information includes key encoding and key action, key code to identify key identity, key action is divided into pressed and released, in the key release when the routine will calculate the duration of key press

The program execution result is shown in the following figure:![](../zh/images/sdk_application/image-gpio-keys.png)

**Translation Disclaimer**  
For the convenience of customers, Canaan uses an AI translator to translate text into multiple languages, which may contain errors. We do not guarantee the accuracy, reliability or timeliness of the translations provided. Canaan shall not be liable for any loss or damage caused by reliance on the accuracy or reliability of the translated information. If there is a content difference between the translations in different languages, the Chinese Simplified version shall prevail.

If you would like to report a translation error or inaccuracy, please feel free to contact us by mail.
