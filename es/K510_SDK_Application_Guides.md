![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">Guía de aplicación del SDK K510</font>**

<font face="黑体"  size=3>Versión del documento: V1.0.0</font>

<font face="黑体"  size=3>Publicado: 2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Renuncia**</font>
Los productos, servicios o características que compre estarán sujetos a los contratos comerciales y términos de Beijing Canaan Jiesi Information Technology Co., Ltd. ("la Compañía", la misma en adelante), y todos o parte de los productos, servicios o características descritos en este documento pueden no estar dentro del alcance de su compra o uso. Salvo que se acuerde lo contrario en el contrato, la Compañía renuncia a todas las representaciones o garantías, expresas o implícitas, en cuanto a la precisión, confiabilidad, integridad, marketing, propósito específico y no agresión de cualquier representación, información o contenido de este documento. A menos que se acuerde lo contrario, este documento se proporciona como una guía para su uso solamente.
Debido a actualizaciones de la versión del producto u otras razones, el contenido de este documento puede actualizarse o modificarse de vez en cuando sin previo aviso. 

**<font face="黑体"  size=3>Avisos de marcas comerciales</font>**

""<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, el icono de "Canaan", Canaan y otras marcas comerciales de Canaan y otras marcas comerciales de Canaan son marcas comerciales de Beijing Canaan Jiesi Information Technology Co., Ltd. Todas las demás marcas comerciales o marcas registradas que puedan mencionarse en este documento son propiedad de sus respectivos propietarios. 

**<font face="黑体"  size=3>Derechos de autor ©2022 Beijing Canaan Jiesi Information Technology Co., Ltd</font>**
Este documento solo es aplicable al desarrollo y diseño de la plataforma K510, sin el permiso por escrito de la empresa, ninguna unidad o individuo puede difundir parte o la totalidad del contenido de este documento en ninguna forma. 

**<font face="黑体"  size=3>Beijing Canaan Jiesi Información Technology Co., Ltd</font>**
URL: canaan-creative.com
Consultas comerciales: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# prefacio
**<font face="黑体"  size=5>Propósito del documento</font>**
Este documento es un documento de descripción para el ejemplo de aplicación K510 SDK. 

**<font face="黑体"  size=5>Objetos reader</font>**

Las principales personas a las que se aplica este documento (esta guía):

- Desarrolladores de software
- Personal de soporte técnico

**<font face="黑体"  size=5>Historial 
 </font>**de revisiones <font face="宋体"  size=2>El historial de revisiones acumula una descripción de cada actualización del documento. La versión más reciente del documento contiene actualizaciones para todas las versiones anteriores. </font>

| El número de versión | Modificado por     | Fecha de revisión   | Notas de revisión     |
| :----- | ---------- | ---------- | ------------ |
| V1.0.0 | Grupos de software del sistema | 2022-03-09 | Lanzamiento del SDK V1.5 |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenido</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Aplicación de demostración

## 1.1 programa de demostración ai

### 1.1.1 Descripción

El código fuente del programa de demostración de nncase se encuentra en el directorio bajo el directorio SDK`package/ai`, y la estructura de directorios es la siguiente:

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

Puede consultar el código fuente del retinaface_mb_320 y `CMakeLists.txt`agregar un nuevo programa de demostración de nncase. 

Para la compilación del modelo, véase`nncase_demo.mk` el POST_INSTALL_TARGET_HOOKS* definido en el mismo*:

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

La compilación del modelo requiere un entorno nncase, y para la construcción del entorno nncase, consulte k510_nncase_Developer_Guides.md. En el futuro, nncase tiene una actualización y el sdk buildroot se actualizará a nncase de forma sincrónica.

### 1.1.2 retinaface

Función: Detección de rostros, detección de puntos de referencia faciales

Ruta del programa:
`/app/ai/shell`
Correr:
Ejecutar un modelo `./retinaface_mb_320_bf16.sh`no cuantitativo
Realizar el modelo de cuantización uint8,`./retinaface_mb_320_uint8.sh`

Hay configuraciones para QOS en el script, las mismas que para las siguientes dos demostraciones.

```shell
#devmem phyaddr width value
devmem 0x970E00fc 32 0x0fffff00
devmem 0x970E0100 32 0x000000ff
devmem 0x970E00f4 32 0x00550000
```

Al ejecutar una demostración, es necesario priorizar asegurarse de que la visualización de la pantalla sea normal, es decir, ajustar la QoS relacionada con la pantalla a una prioridad alta.
QOS_CTRL0.ax25mp escribir QoS = 5
QOS_CTRL0.ax25mp lectura QoS = 5
QOS_CTRL2.ispf2k escribir QoS = 0xf
QOS_CTRL2.ispf2k leer QoS = 0xf
QOS_CTRL2.ispr2k escribir QoS = 0xf
QOS_CTRL2.ispr2k leer QoS = 0xf
QOS_CTRL2.isp3dtof escribir QoS = 0xf
QOS_CTRL3.display leer QoS = 0xf
QOS_CTRL3.display escribir QoS = 0xf

Desplazamiento 
 [0x00f4]del registro de control QOS 0(QOS_CTRL0)![ qos CTRL0](../zh/images/sdk_application/demo_nncase_qos_ctrl0.png)

Desplazamiento 
 [0x00f8]del registro de control QOS 1 (QOS_CTRL1)![ qos CTRL1](../zh/images/sdk_application/demo_nncase_qos_ctrl1.png)

Desplazamiento 
 [0x00fc]del registro de control QOS 2 (QOS_CTRL2)![ qos CTRL2](../zh/images/sdk_application/demo_nncase_qos_ctrl2.png)

Desplazamiento 
 [0x0100]del registro de control QOS 3 (QOS_CTRL3)![ qos CTRL3](../zh/images/sdk_application/demo_nncase_qos_ctrl3.png)

La compilación e instalación del modelo se detalla en el archivo package/ai/ai.mk:

Ruta de script de compilación:
paquete/ai/código/retinaface_mb_320/rf_onnx.py

### 1.1.3 object_detect

Función: Detección de clasificación de objetos, clasificación 80

Ruta del programa:`/app/ai/shell`

Correr:
Ejecutar un modelo `./object_detect_demo_bf16.sh`no cuantitativo
Realizar el modelo de cuantización uint8,`./object_detect_demo_uint8.sh`

La compilación e instalación del modelo se detalla en el archivo package/ai/ai.mk

Ruta de script de compilación:
paquete/ai/código/object_detect_demo/od_onnx.py

## 1.2 ffmpeg

`ffmpeg``ffmpeg-4.4`Migrado a código fuente abierto, agregado`0001-buildroot-ffmpeg-0.1.patch` para Service Packs

- `ff_k510_video_demuxer`: Controla la entrada del isp, referenciada`libvideo.so`
- `ff_libk510_h264_encoder`: Codificación de hardware h264 de control, referenciada`libvenc.so`

Los parámetros configurables se pueden ver a través de la directiva de ayuda

```shell
ffmpeg -h encoder=libk510_h264 #查看k510编码器的参数
ffmpeg -h demuxer=libk510_video #查看demuxer的配置参数
```

Para obtener instrucciones detalladas de ejecución, consulte[ K510_Multimedia_Developer_Guides.md](./K510_Multimedia_Developer_Guides.md)

## 1.3 alsa_demo

El programa de demostración de alsa se coloca en`/app/alsa_demo` el directorio:

Preparación de la carrera:
(1) Conecte los auriculares

Ejecutar demo de alsa:

```shell
cd /app/alsa_demo/
./alsa_demo c #录音到文件capture.pcm，demo程序仅作参考，可以参考package/alsa_demo的源码。
./alsa_demo p #播放capture.pcm
```

## 1.4 Demostración de TWOD

Cómo ejecutar la rotación:

```shell
cd /app/twod_app
./twod-rotation-app
```

Copie el .yuv de salida en el monitor YUV y establezca el tamaño 1080 x 1920, formato de visualización nv12, el resultado es el siguiente
![salida.yuv](../zh/images/sdk_application/driver-twod-output-1080x1920.jpg)

Uso del escalador

```shell
cd /app/twod_app
./twod-scaler-app
```

Copie el .yuv de salida en el monitor YUV y establezca el tamaño 640x480, formato de visualización nv12, el resultado es el siguiente
![ouput.yuv](../zh/images/sdk_application/driver-twod-output-640x480.jpg)

Cómo ejecutar rgb2yuv:

```shell
cd /app/twod_app
./twod-osd2yuv-app
```

Copie el .yuv de salida en el monitor YUV y establezca el tamaño 320x240, formato de visualización nv12, el resultado es el siguiente
![ouput.yuv](../zh/images/sdk_application/twod-osd2yuv-app.jpg)

Ejecute el uso de yuv2rgb:

```shell
cd /app/twod_app
./twod-scaler-output-rgb888-app
```

Copie el .yuv de salida en el monitor rgb888 y establezca el tamaño 640x480, el formato de visualización rgb24, el resultado es el siguiente
![ouput.yuv](../zh/images/sdk_application/driver-twod-output-640x480.jpg)

Ejecute el yuv de salida en el uso de osd superpuesto:

```shell
cd /app/twod_app
./twod-scaler-overlay-osd-app
```

Copie la salida .yuv al monitor para establecer el tamaño 640x480, formato de visualización nv12, el resultado es el siguiente
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

## 1.5 Demostración de RTC

El controlador RTC registra el nodo de dispositivo build /dev/rtc0.

La capa de aplicación sigue el método de programación RTC estándar en el controlador de llamada del sistema Linux, y se recomienda desactivar la impresión de información del kernel a través de la consola del shell antes de ejecutar la rutina de referencia.

```shell
echo 0 > /proc/sys/kernel/printk
```

Vaya al directorio /app/rtc e introduzca el siguiente comando para iniciar la aplicación rtc.

```shell
cd /app/rtc
./rtc 2021-11-3 21:10:59
```

El resultado de la ejecución del programa es:

![](../zh/images/sdk_application/image-rtc.png)

El fragmento de código principal del programa de demostración rtc es el siguiente, consulte el código en la carpeta package/rtc para obtener más detalles.

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

## 1.6 Demostración de WDT

El K510 tiene un total de tres perros guardianes, y el controlador WDT registra los nodos de dispositivo generar /dev/watchdog0, /dev/watchdog1, /dev/watchdog2.

La capa de aplicación sigue el método de programación WDT estándar en el controlador de llamada del sistema Linux, el primer parámetro de la aplicación wathdog puede ser 0, 1, representar watchdog0, watchdog1, respectivamente, el segundo parámetro representa el tiempo de espera (unidad de segundos) que se puede establecer, por ejemplo, el siguiente comando indica el inicio de watchdog0, watchdog0 tiempo de desbordamiento de 40 segundos.

```shell
cd /app/watchdog
./watchdog 0 40
```

Después de que se inicie el programa, alimentará al perro guardián cada 1 segundo a intervalos, cuando se ingrese el carácter de detención en el terminal del shell, la aplicación deje de alimentar al perro y el perro guardián restablecerá el reinicio del dispositivo después de que se desborde el tiempo de espera de configuración, consulte el código en la carpeta del paquete / perro guardián para obtener más detalles.

El resultado de la ejecución del programa es:

![](../zh/images/sdk_application/image-watchdog.png)

**Nota**: El módulo de vigilancia k510 actual tiene una frecuencia de reloj de trabajo de 757575Hz, y el tiempo de espera en segundos debe convertirse en el tiempo de espera de la frecuencia de reloj de trabajo real del perro guardián, que se calcula como 2^n / 757575, por lo que el tiempo de espera real será mayor o igual que el tiempo de espera de entrada. 

El período de tiempo de espera real se calcula de la siguiente manera:

1) Ingrese 40, 2^25/757575=44 > 40, 2^24/757575=22 < 40, por lo que se establece en 44 segundos;

2) Ingrese 155, 2^27/757575=177 > 155, por lo que se establece en 177 segundos;

3) Ingrese 2000, 2^31/757575=2834 > 2000, por lo que se establece en 2834 segundos;

## 1.7 Demostración de UART

K510 tiene un total de 4 puertos serie, el controlador actual en los puertos serie 2, 3 no está habilitado, el controlador del puerto serie 0 se registrará para generar nodos de dispositivo /dev/ttyS0.

La capa de aplicación sigue el método de programación UART estándar en el controlador de llamada del sistema Linux. El primer parámetro de la aplicación uart puede ser 0 y 1, que representan uart0 y uart1 respectivamente.

La placa de desarrollo utiliza una red cableada para conectarse al router, de modo que la placa de desarrollo y el PC de depuración en una red, cuando la placa de desarrollo está encendida, obtendrá automáticamente la IP, ingresará el comando ifconfig en el terminal serie shell de la placa de desarrollo para obtener la dirección IP, y la PC de depuración usa esta IP para abrir una ventana telent conectando la placa de desarrollo a través de la conexión telent. Por ejemplo, la operación de depuración de un PC para conectar una placa de desarrollo utilizando telent a través de MobaXterm se muestra en la siguiente figura.

![](../zh/images/sdk_application/image-uart-mobaxterm.png)

Introduzca el siguiente comando en la ventana del terminal telent para iniciar el trabajo del puerto serie 0.

```shell
cd /app/uart
./uart 0
```

Ingrese el contenido que desea enviar en la ventana telent, puede ver los datos recibidos en la ventana del terminal serie del shell, consulte el código en la carpeta package / crb_demo / uart para obtener más detalles.
Por ejemplo, la entrada para la ventana telent:

![](../zh/images/sdk_application/image-uart-telent.png)

La ventana del terminal serie Shell correspondiente muestra:

![](../zh/images/sdk_application/image-uart-shell.png)

## 1.8 Demostración de ETH

La capa de aplicación sigue el controlador de llamada al método de programación ETH estándar en sistemas Linux.

### 1.8.1 Cliente

El dispositivo como cliente, ingrese el directorio /app/client, ingrese el siguiente comando para iniciar la aplicación cliente, el primer parámetro de la aplicación ETH indica la dirección IP del servidor para establecer el enlace TCP, por ejemplo, ingrese el siguiente comando para iniciar el programa ETH y el servidor 10.20.1.13 para establecer la comunicación.

```shell
cd /app/client
./client 10.20.1.13
```

Conecte el servidor para comunicarse a través del protocolo tcp, ejecute el programa del servidor en otra máquina ubuntu, consulte la carpeta paquete / aplicación / cliente para obtener más detalles.

Mostrar registros en el lado del dispositivo:

![](../zh/images/sdk_application/image-client.png)

### 1.8.2 Servidor

El dispositivo ingresa al directorio /app/server como el servidor, por ejemplo, ingrese el siguiente comando para iniciar el programa del servidor.

```shell
cd /app/server
./server
```

Ejecute el programa cliente en otra máquina ubuntu, conecte el servidor a través del protocolo tcp para comunicarse, para obtener más detalles, consulte la carpeta paquete / crb_demo / servidor.

Mostrar registros en el lado del dispositivo:

 ![](../zh/images/sdk_application/image-server.png)

## 1.9 Demostración de SDMMC

El K510 tiene un total de 3 controladores principales SDMMC, la placa de desarrollo SDMMC0 se utiliza para conectar eMMC, SDMMC1 se utiliza para módulos WIFI y el controlador SDMMC2 se utiliza para conectar tarjetas SD.

El controlador SDMMC se registra para generar /dev/mmcblk0 y el controlador EMMC se registra como el nodo de dispositivo /dev/mmcblk1.

La tarjeta SD se montará automáticamente en /root/data después del inicio del sistema, ingrese el directorio /app/write_read_file, el primer parámetro de la aplicación SDMMC indica el archivo que se leerá y escribirá, como la tarjeta SD montada en /root/data, puede leer y escribir archivos en el directorio /root/data/, primero escribir y luego leer, Ingrese el siguiente comando para iniciar la aplicación SDMMC para leer y escribir en la tarjeta SD y calcular la velocidad de lectura y escritura (unidad m / s).

```shell
cd /app/write_read_file
./write_read_file /root/data/test.txt
```

Para habilitar la lectura y escritura de datos 1G en la tarjeta SD, consulte la carpeta / aplicación / write_read_file carpeta.

![](../zh/images/sdk_application/image-sdmmc.png)

## 1.10 Demostración de SHA/AES

La demostración de SHA/AES utiliza el kernel de Linux para exportar AF_ALG tipo de interfaz Netlink y utiliza la API de cifrado del kernel en el espacio de usuario. Consulte .<https://www.kernel.org/doc/html/latest/crypto/userspace-if.html> 

Parámetro:
-h Imprime la información de ayuda
-t tipo de algoritmo: hash, skcipher
-n Nombres de algoritmos: sha256, ecb(aes), cbc(aes)
-x operación de descifrado
-k AES KEY (cadena hexadecimal)
-v AES IV (cadena hexadecimal)

![](../zh/images/sdk_application/image_crypto_help.png)

Prueba sha256:

```shell
cd /app/crypto
echo -n "This is a test file, hello world" > plain.txt
./crypto -t hash -n "sha256" plain.txt sha256.txt
xxd -p -c 32 sha256.txt
sha256sum plain.txt
```

![](../zh/images/sdk_application/image_crypto_sha256.png)

Prueba bce(aes) 128:

```shell
cd /app/crypto
echo -n "This is a test file, hello world" > plain.txt
./crypto -t skcipher -n "ecb(aes)" -k 00112233445566778899aabbccddeeff plain.txt ecb_aes_en.bin
./crypto -t skcipher -n "ecb(aes)" -k 00112233445566778899aabbccddeeff  -x ecb_aes_en.bin ecb_aes_de.bin
cmp ecb_aes_de.bin plain.txt
cat ecb_aes_de.bin
```

![](../zh/images/sdk_application/image_crypto_ecb.png)

prueba cbc(aes) 128

```shell
cd /app/crypto
echo -n "This is a test file, hello world" > plain.txt
./crypto -t skcipher -n "cbc(aes)" -k 00112233445566778899aabbccddeeff -v 00112233445566778899aabbccddeeff plain.txt cbc_aes_en.bin
./crypto -t skcipher -n "cbc(aes)" -k 00112233445566778899aabbccddeeff -v 00112233445566778899aabbccddeeff -x cbc_aes_en.bin cbc_aes_de.bin
cmp cbc_aes_de.bin plain.txt
cat cbc_aes_de.bin
```

![](../zh/images/sdk_application/image_crypto_cbc.png)

El cifrado AES-ECB-128 y aes-cbc-128 requieren una alineación de 16 bytes del texto plano, y el insuficiente se rellenará automáticamente con 0.

## 1.11 Demostración de TRNG

La demostración de TRNG produce un número aleatorio de la longitud especificada leyendo el dispositivo de caracteres /dev/hwrng, que se genera como una cadena hexadecimal.

El significado del parámetro de entrada de ./trng:

-h Imprime la información de ayuda

-b Especifica la longitud del número aleatorio de salida, en bytes

![](../zh/images/sdk_application/image_trng.png)

## 1.12 Demostración de DRM

La demostración de Drm muestra las capacidades multicapa de vo hardware.

Vo tiene un total de 8 capas:

1) Capa de fondo, se puede configurar el color de fondo.

2) Layer0 es una capa de video, admite YUV422 y YUV420, admite formatos NV12 y NV21, se puede emparejar en el lado del tamaño y admite el escalado y la reducción de escala de hardware.

3) Layer1-layer3 es una capa de video, compatible con YUV422 y YUV420, compatible con los formatos NV12 y NV21, y el lado del tamaño se puede igualar.

4) Layer4-layer6 es la capa OSD que admite múltiples formatos ARGB.

Después de que se inicie la placa, ingrese el directorio /app/drm_demo e ingrese el comando:

```shell
cd /app/drm_demo
./drm_demo
```

Inicie drm_demo aplicación, drm_demo se muestra:

![](../zh/images/sdk_application/image_drm_demo.png)

## 1.13 demostración V4L2_DRM

v4l2_drm demostración demuestra la funcionalidad de la entrada y visualización de la cámara.

Después de que se inicie la placa, ingrese el directorio /app/mediactl_lib e ingrese el comando:

```shell
cd /app/mediactl_lib
./v4l2_drm.out -f video_drm_1080x1920.conf -e 1
或者
./v4l2_drm.out -f video_drm_1920x1080.conf
```

Inicie la aplicación v4l2_drm.out y v4l2_drm.out:

![](../zh/images/sdk_application/image_v4l2_drm_demo.png)

## 1.14 Demostración de LVGL

Vaya a /app/lvgl y ejecute el siguiente comando:

```shell
cd /app/lvgl
./lvgl
```

El efecto de visualización es el siguiente:![](../zh/images/sdk_application/image_lvgl.png)

## 1.15 Demostración de PWM

El controlador PWM registra los nodos de dispositivo generar /sys/class/pwm/pwmchip0 y /sys/class/pwm/pwmchip3.

Este ejemplo se puede configurar y habilitar para pwm0 y pwm1 respectivamente, en el directorio /app/pwm, el primer parámetro de la aplicación pwm indica el período de configuración de pwm, la unidad es ns, el segundo parámetro establece el tiempo de "ON" en un ciclo de pwm, la unidad es ns, el tercer parámetro puede ser 0, 1, que representa pwm0 y pwm1, por ejemplo, ingrese el siguiente comando para habilitar pwm0, el ciclo es 1s, el ciclo de trabajo es 100000000 / 500000000 * 100% = 50%, consulte la carpeta / aplicación / pwm carpeta para obtener códigos detallados.

```shell
cd /app/pwm
./pwm 1000000000 500000000 0
```

El resultado de la ejecución del programa es:

![](../zh/images/sdk_application/image-pwm.png)

Al conectar el pin 28 de la placa de desarrollo K510 CRB1.2 J15 a través del osciloscopio, se puede observar un patrón de forma de onda con un período de 1 segundo y un ciclo de trabajo del 50% en el osciloscopio.

## 1.16 Demostración de WIFI

Después de cargar el controlador del módulo WiFi, se genera la tarjeta de red inalámbrica wlan0, que sigue el controlador de puerto de red estándar y normalmente se refiere a la programación del zócalo TCP / IP.

1) Abra "Punto de acceso móvil" en el cuaderno y luego establezca el nombre y la contraseña del punto de acceso
2) Inicie NetAssist en el bloc de notas, configure el tipo de protocolo, la IP del host local, el puerto del host local, la configuración de recepción, la configuración de envío y los datos que deben enviarse, como se muestra en la siguiente figura:

![](../zh/images/sdk_application/image_wifi_1.png)

3) El formato de parámetro del programa de prueba wifi es:

```shell
./wifi <AP name> <password> <local ip> <server ip>
```

Por ejemplo, ingrese el directorio /app/wifi, ingrese el comando para iniciar el programa de prueba wifi y el resultado de ejecución del programa es el siguiente:

![](../zh/images/sdk_application/image_wifi_2.png)

## 1.17 GPIO_KEYS demo

El controlador de clave utiliza el propio kernel de Linux integrado con el controlador genérico de claves de gpu basado en el subsistema de entrada, y después de cargar el controlador, el nodo de monitoreo de eventos eventX se genera en el directorio /dev/input, y X es el número de secuencia del nodo de evento, que se puede ver a través de cat /proc/bus/input/devices

gpio-keys rutina bloqueo de lectura de eventos de informes de claves e impresión de información de eventos, su información incluye codificación de claves y acción de claves, código de clave para identificar la identidad de clave, acción de clave se divide en presionada y liberada, en la liberación de clave cuando la rutina calculará la duración de la pulsación de tecla

El resultado de la ejecución del programa se muestra en la siguiente figura:![](../zh/images/sdk_application/image-gpio-keys.png)

**Descargo de responsabilidad de **traducción  
Para la comodidad de los clientes, Canaan utiliza un traductor de IA para traducir texto a varios idiomas, que pueden contener errores. No garantizamos la exactitud, fiabilidad o puntualidad de las traducciones proporcionadas. Canaan no será responsable de ninguna pérdida o daño causado por la confianza en la exactitud o fiabilidad de la información traducida. Si existe una diferencia de contenido entre las traducciones en diferentes idiomas, prevalecerá la versión en chino simplificado. 

Si desea informar de un error o inexactitud de traducción, no dude en ponerse en contacto con nosotros por correo.