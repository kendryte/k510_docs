![](../zh/images/canaan-cover.png)
&nbsp;
&nbsp;
**<font face="黑体" size="6" style="float:right">K510 CRB V1.2 Guías de hardware</font>**

<font face="黑体" size=100>&nbsp;
&nbsp;
&nbsp;</font>

<font face="黑体"  size=3>Versión del documento: V1.0.0</font>

<font face="黑体"  size=3>Publicado: 2022-03-15</font>

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
Este documento es un documento complementario al sdk de K510 y está destinado a ayudar a los ingenieros a comprender la compilación y grabación del sdk de K510. 

**<font face="黑体"  size=5>Objetos reader</font>**

Las principales personas a las que se aplica este documento (esta guía):

- Desarrolladores de software
- Personal de soporte técnico

**<font face="黑体"  size=5>Historial 
 </font>**de revisiones <font face="宋体"  size=2>El historial de revisiones acumula una descripción de cada actualización del documento. La versión más reciente del documento contiene actualizaciones para todas las versiones anteriores. </font>

| El número de versión | Modificado por    | Fecha de revisión   | Notas de revisión           |
| :----- | --------- | ---------- | ------------------ |
| V1.0.0 | División de Productos de IA | 2022-03-15 | |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenido</font>**

[Toc]

<div style="page-break-after:always"></div>

# 1 Visión general

&emsp; &emsp; K510 CRB es una plataforma de desarrollo de hardware para el chip de IA Canaan Kendryte K510 que integra el diseño de referencia, la depuración y las pruebas del chip, y la verificación del desarrollo del producto del usuario, que se utiliza para demostrar la potente potencia de cálculo y las funciones del chip K510. Al mismo tiempo, proporciona a los clientes diseños de referencia de hardware basados en chips K510, de modo que los clientes no necesitan modificar o simplemente modificar el circuito del módulo del diseño de referencia, y pueden completar el trabajo de desarrollo de hardware del producto con chips K510 como núcleo.

&emsp; &emsp; K510 CRB es compatible con el desarrollo de hardware, el diseño de software de aplicación, la depuración y el funcionamiento del chip K510, ya que teniendo en cuenta los diferentes entornos de uso, el chip es una verificación completamente funcional, por lo que las diversas interfaces están completas y el diseño es relativamente completo. El K510 CRB se puede conectar a un PC a través de un cable USB, utilizado como sistema de desarrollo básico, o a un sistema de desarrollo y entorno de demostración más completo, conectando los siguientes dispositivos y componentes:

- fuente de alimentación

- Dispositivo de almacenamiento de la tarjeta TF

- Pantalla LCD MIPI DSI

- Módulo de cámara MIPI CSI

- Módulo de cámara DVP

- Cable de red Ethernet

- Pantalla HDMI

- Auriculares o altavoces

- Ampliar piezas de repuesto

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-K510_Core.png">
</div>

  <center>Figura 1-1 Representación de CRB K510</center>

    **禁止事项**

  1. ¡Está prohibido enchufar y desconectar el módulo central y los módulos periféricos en vivo!
  2. Está prohibido operar este producto directamente sin las medidas de descarga de electricidad estática o sin protección estática.
  3. Está prohibido el uso de disolventes orgánicos o líquidos corrosivos para limpiar este producto.
  4. Está prohibido realizar operaciones como golpeteos y torsiones que puedan causar daños físicos.

    **Precauciones**

  1. Tenga en cuenta que después de la descarga electrostática del cuerpo humano, antes de operar este producto, se recomienda usar un brazalete electrostático.
  2. Antes de la operación, confirme el voltaje de alimentación y el voltaje del adaptador de la placa posterior dentro del rango permitido descrito en este documento.
  3. Asegúrese de leer este documento y las consideraciones en el archivo de ingeniería antes de diseñar.
  4. Tenga en cuenta que el uso de productos en ambientes de alta temperatura, alta humedad y alta corrosión requiere un tratamiento especial como la disipación de calor, el drenaje y el sellado.
  5. Por favor, no se repare y desmonte usted mismo, de lo contrario no podrá disfrutar de un servicio postventa gratuito.

<div style="page-break-after:always"></div>

## 1.1 Diagrama de bloques del sistema

&emsp; &emsp; El diagrama de bloques del sistema se utiliza para describir los principios de diseño del K510 CRB y la relación entre los componentes, de modo que el uso del K510 CRB y los desarrolladores puedan tener una comprensión intuitiva de la arquitectura y los principios de todo el sistema.

&emsp; &emsp; Para obtener más información sobre las características de K510, consulte la hoja de datos completa de K510.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_1_2.png">
</div>

<center>Figura 1-2 Composición de CRB K510</center>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_1_3.png">
</div>

<center>Figura 1-3 Diagrama de bloques del sistema K510 CRB </center>

<div style="page-break-after:always"></div>

&emsp; &emsp; El kit de desarrollo K510 CRB consta principalmente de los siguientes componentes:

| partes | cantidad |
| :-: | :-: |
| Placa base K510 CRB | 1 |
| USB type C线缆 | 2 |
| Cable MICRO USB OTG | 1 |
| Pantalla MIPI DSI con una resolución de 1920x1080 | 1 |
| Subcarga de cámara MIPI CSI, sensor de imagen Sony IMX219 integrado dos | 1 |
| Carcasa protectora acrílica | 1 |

<div style="page-break-after:always"></div>

## 1.2 Descripción general de la función

&emsp; &emsp; El SDK K510 se basa en buildroot como marco básico, con kernel linux K510 (versión linux 4.17.0), u-boot (u-boot versión 2020.01), riscv-pk-k510

&emsp; &emsp; Las principales características de K510 CRB V1.2 (si no hay declaraciones especiales, las versiones de CRB descritas más adelante en este documento son V1.2) son las siguientes:

- PMIC: Administración de energía
- LPDDR3EE de 32 bits, capacidad total 512MByte
- eMMC de 8 bits, capacidad total 4GByte
- QSPI NAND, capacidad total 128MByte
- Tarjeta TF: Admite la expansión externa del almacenamiento de la tarjeta TF.
- USB OTG: Actualización del sistema, soporte de conmutación de host / dispositivo
- SDIO WIFI: Soporta la función de Internet inalámbrico y la conexión Bluetooth
- Audio: Soporte de entrada y salida de voz
- PDM MIC: función de activación VAD
- Uart & JTAG Debug: Placas de desarrollo utilizadas por Debug
- Entrada de vídeo: Entrada de cámara dual MIPI CSI 2lane
- Salida de vídeo: MIPI DSI 4lane, pantalla 1080P
- RGMII: Conexión Gigabit Ethernet
- HDMI: Interfaz multimedia de alta definición
- Interfaces extendidas: fuente de alimentación, GPIO, I2C, SPI
- Claves, indicadores

<div style="page-break-after:always"></div>

# 2 Introducción a los recursos de hardware

## 2.1 Representaciones generales

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_1.png" width=80%>
</div>

<center> Figura 2-1 Frente de la placa base </center>

<div style="page-break-after:always"></div>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_2.png" width=80%>
</div>

<center> Figura 2-1 En la parte posterior de la placa base </center>

<div style="page-break-after:always"></div>

## 2.2 Diagrama esquemático de estructura e interfaz

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_3.png" width=120%>
</div>

<center> Figura 2-3 Posición de cada dispositivo en la parte frontal de la placa base </center>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2-4.png" width=120%>
</div>

<center> Figura 2-4 Parte posterior de la placa base </center>

<div style="page-break-after:always"></div>

## 2.3 Diagrama de bloques de potencia

&emsp; &emsp; El K510 CRB utiliza DC-5V como potencia de entrada de toda la placa, proporcionando DC-5V para el módulo central K510 CORE, y 1.8V y 3.3V para los otros periféricos de la placa posterior a través de dos DC-DC.

## 2.4 Dirección del dispositivo I2C

<center>Tabla 2-1 Tabla de direcciones de dispositivos I2C</center>

| nombre | Pines (SCL, SDA) | dirección | comentario |
| :-: | :-: | :-: | :-: |
| pantalla táctil | IO_103、IO_102 | 0x14 o 0x5D | |
| HDMI | IO_117、IO_116 | 0x3B | |
| Códec de audio | IO_117、IO_116 | 0x1A | |
| Cámara MIPI CSI0 | IO_120、IO_121 | 0x10 | |
| Cámara MIPI CSI1 | IO_47、IO_48   | 0x10 | |

## 2.5 Esquemas

&emsp; &emsp; El esquema de referencia para la placa de desarrollo K510 CRB debe descargarse[ en el lanzamiento](https://github.com/kendryte/k510_docs/releases). 

<div style="page-break-after:always"></div>

# 3 Introducción a cada sección de la placa de desarrollo

## 3.1 Módulos principales

&emsp; &emsp; Antes de usar K510 CRB para el aprendizaje y el desarrollo, se recomienda consultar la arquitectura detallada del chip en el manual K510, para que pueda tener una comprensión más profunda de la fuente de alimentación, el almacenamiento, los recursos informáticos y los periféricos del K510, lo que es propicio para la familiaridad y el desarrollo de la solución de chip. La placa central K510 se muestra en la Figura 3-1.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_1.png">
</div>

<center>Figura 3-1 Módulo central K510</center>

<div style="page-break-after:always"></div>

## 3.2 Fuente de alimentación de entrada

&emsp; &emsp; K510 CRB utiliza una fuente de alimentación externa de 5V, a bordo dos interfaces USB tipo C, se pueden usar para alimentar la placa de desarrollo, de las cuales la interfaz UART se usa para conectarse a la computadora, la interfaz USB de la COMPUTADORA solo puede proporcionar corriente de 500mA, en el caso de una fuente de alimentación insuficiente, use el adaptador al mismo tiempo para suministrar energía a DC: 5V. La interfaz se muestra en la siguiente figura.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_2.png" width=60%>
</div>

<center> Figura 3-2 Conector de entrada de alimentación </center>

**Nota: Limite el uso de la fuente de alimentación de 5V, cuando use el adaptador de carga rápida, intente no conectar otros dispositivos como teléfonos móviles al mismo tiempo, para no hacer que el adaptador de carga rápida emita incorrectamente una fuente de alimentación superior a 5V, lo que resulta en daños en la parte de la fuente de alimentación de la placa de desarrollo. **
&emsp; &emsp; Utilice el interruptor de palanca K2 para el funcionamiento de encendido y apagado, como se muestra en la siguiente figura. 

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-3.jpg" width=50%>
</div>

<center>Figura 3-3 Descripción del interruptor de encendido</center>

<div style="page-break-after:always"></div>

## 3.3 Dispositivos de almacenamiento

&emsp; &emsp; El K510 CRB incluye una variedad de dispositivos de almacenamiento a bordo, incluyendo DDR, eMMC, NAND Flash y TF Card.

### 3.3.1 eMMC

&emsp; &emsp; Una memoria eMMC de 4G Bytes a bordo en el K510 CRB, ubicada en el módulo central, se puede utilizar para almacenar datos como el código de inicio y los archivos de usuario.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-eMMC.png" width=70%>
</div>

<center>Figura 3-4 Memoria eMMC</center>

### 3.3.2 NandFlash

&emsp; &emsp; El K510 CRB incluye 128M Bytes de memoria Flash NAND, que se puede utilizar para almacenar datos como código de inicio y archivos de usuario.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_5.jpg " width=75%>
</div>

<center>Figura 3-5 Memoria flash NAND</center>

### 3.3.2 Tarjeta TF

&emsp; &emsp; El K510 CRB tiene un soporte para tarjeta TF a bordo que se puede conectar externamente a una tarjeta TF para almacenar datos como el código de inicio y los archivos de usuario.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_6.png">
</div>

<center>Figura 3-6 Soporte de tarjeta TF</center>

<div style="page-break-after:always"></div>

## 3.4 Pulsaciones de teclas

&emsp; &emsp; El K510 CRB contiene dos botones táctiles de usuario que permiten a los usuarios personalizar los botones de toque para activarlos como entradas del sistema u otras funciones relacionadas con el software.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_7.jpg" width=50%>
</div>

<center>Figura 3-7 Claves</center>

## 3.5 LEDs

&emsp; &emsp; El K510 CRB tiene un diodo emisor de luz a bordo que está conectado directamente al pin GPIO del chip K510.

&emsp; &emsp; El K510 CRB está a bordo de un LED de color WS2812 que está conectado directamente al pin GPIO del chip K510.

&emsp; &emsp; Los dos LED están programados a medida para iluminar o extinguir y se pueden utilizar como salidas del sistema o indicaciones de estado relacionadas con el software.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_8.jpg" width=60%>
</div>

<center>Figura 3-8 LED</center>

<div style="page-break-after:always"></div>

## 3.6 Modo de arranque y restablecimiento

&emsp; &emsp; El K510 CRB tiene una variedad de dispositivos de almacenamiento a bordo, y el modo de arranque se selecciona configurando los niveles de los pines de arranque, BOOT0 y BOOT1, con 0 y 1 que representan niveles bajos y altos.

&emsp; &emsp; En la PCB, el modo de inicio es seleccionado por el interruptor DIP que se muestra en la siguiente figura, y el módulo central ha sido diseñado para levantar BOOT0 y BOOT1, y el lado de la marca de luz de marcación ON representa el correspondiente bit pull down efectivo, y el otro lado de ON corresponde a OFF representa el pull-up efectivo.

&emsp; &emsp; El K510 determina el modo de arranque del chip por el estado de los pines de hardware boot0 y BOOT1, y la selección del modo de arranque se muestra en la tabla siguiente.

<center>Tabla 2-1 Modos de arranque</center>

| ARRANQUE1   | BOOT0   | Modo de inicio      |
| ------- | ------- | ------------ |
| 0(ENCENDIDO)   | 0(ENCENDIDO)   | Arranque del puerto serie      |
| 0(ENCENDIDO)   | 1 (APAGADO)  | La tarjeta SD arranca      |
| 1 (APAGADO)  | 0(ENCENDIDO)   | Botas NANDFLASH |
| 1 (APAGADO)  | 1 (APAGADO)  | Botas EMMC      |

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_9.jpg" width=60%>
</div>

<center>Figura 3-9 Interruptor DIP de reinicio y modo de inicio</center>

&emsp; &emsp; El botón de reinicio a bordo K510 CRB es K2 en la Figura 3-9, que se puede presionar para realizar una operación de restablecimiento de hardware del sistema.

<div style="page-break-after:always"></div>

## 3.7 Entrada y salida de audio

&emsp; &emsp; El K510 CRB utiliza el chip de códec de audio de Nuvoton, NAU88C22, para implementar funciones de entrada y salida para el habla. Incluye un micrófono integrado, conector para auriculares estándar de 3,5 mm y conector de altavoz 2P.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-10.jpg" width=60%>
</div>

<center>Figura 3-10 Audio</center>

## Toma OTG USB 3.8

&emsp; &emsp; La toma USB OTG integrada K510 CRB se puede utilizar para implementar la funcionalidad de host/dispositivo USB.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_11.jpg">
</div>

<center>Figura 3-11 Asiento USB-OTG</center>

<div style="page-break-after:always"></div>

## 3.9 Interfaz UART

&emsp; &emsp; K510 CRB Con el fin de facilitar el desarrollo y la depuración del usuario, el K510 CRB tiene una interfaz USB-> UART a bordo, que puede ser operada por la comunicación del puerto serie USART y la depuración del K510 a través del cable PC-USB. El uso inicial puede requerir la carga del controlador, como se detalla en la Sección 4.2. La interfaz UART integrada se muestra en la siguiente figura.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_12.jpg" width=50%>
</div>

<center>Figura 3-12 Interfaz USB-UART</center>

## Módulo 3.10 WIFI/BT

&emsp; &emsp; El K510 CRB incluye un módulo WIFI /BT 2 en 1 AP6212 para ampliar la placa de desarrollo para la conectividad de red y las funciones de comunicación Bluetooth, como se muestra en la interfaz integrada a continuación.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-13.jpg" width=40%>
</div>

<center>Figura 3-13 Módulo WIFI/BT</center>

<div style="page-break-after:always"></div>

## 3.11 Ethernet

&emsp; &emsp; El K510 CRB tiene un soporte Gigabit Ethernet incorporado, y el K510 se implementa a través de un chip PHY externo con una interfaz RGMII. La interfaz integrada se muestra en la siguiente figura.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_14.jpg" width=60%>
</div>

<center>Figura 3-14 Interfaz Ethernet</center>

## Salida hdmi 3.12

&emsp; &emsp; La montura hembra HDMI-A integrada K510 CRB se puede conectar a la pantalla externa a través de un cable HDMI estándar, utilizando la conversión de salida de la interfaz mipi dsi del K510. La interfaz integrada se muestra en la siguiente figura.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_15.jpg" width=60%>
</div>

<center>Figura 3-15 Interfaz HDMI</center>

 **Nota**: Debido a que tanto las pantallas HDMI como las TFT 1080P usan controladores mipi dsi, solo pueden elegir una de las dos pantallas, no se pueden usar al mismo tiempo, cambien a través del pin de control GPIO para seleccionar una de las salidas. 

<div style="page-break-after:always"></div>

## 3.13 Entrada de vídeo

&emsp; &emsp; El K510 CRB extrae mipi CSI, DVP, fuente de alimentación y GPIO parcial a través de un conector de placa a placa de paso de 0,8 mm para lograr la entrada de la cámara en diferentes escenarios y diferentes situaciones de demanda. La interfaz integrada se muestra en la siguiente figura. Las definiciones de interfaz se muestran en la tabla siguiente.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-16.jpg">
</div>

<center>Figura 3-16 Interfaz video IN</center>

<center>Tabla 3-2 Definiciones de interfaz video IN</center>

| numeración | definición             | numeración | definición                       |
| ---- | ---------------- | ---- | --------------- |
| 1    | VDD_5V           | 60   | GPIO_1V8_59_DVP_D12      |
| 2    | VDD_5V           | 59   | GPIO_1V8_58_DVP_D11      |
| 3    | VDD_5V           | 58   | GPIO_1V8_50_DVP_D3       |
| 4    | VDD_5V           | 57   | GPIO_1V8_51_DVP_D4       |
| 5    | GND              | 56   | GPIO_1V8_60_DVP_D13      |
| 6    | GND              | 55   | GPIO_1V8_55_DVP_D8       |
| 7    | MIPI_CSI_D0_P    | 54   | GPIO_1V8_61_DVP_D14      |
| 8    | MIPI_CSI_D0_N    | 53   | GPIO_1V8_52_DVP_D5       |
| 9    | GND              | 52   | GPIO_1V8_47_DVP_D0       |
| 10   | MIPI_CSI_CLK0_P  | 51   | GPIO_1V8_56_DVP_D9       |
| 11   | MIPI_CSI_CLK0_N  | 50   | GPIO_1V8_53_DVP_D6       |
| 12   | GND              | 49   | GPIO_1V8_57_DVP_D10      |
| 13   | MIPI_CSI_D1_P    | 48   | GPIO_1V8_48_DVP_D1       |
| 14   | MIPI_CSI_D1_N    | 47   | GPIO_1V8_54_DVP_D7       |
| 15   | GND              | 46   | GPIO_1V8_64_DVP_HREF     |
| 16   | MIPI_CSI_D2_N    | 45   | GPIO_1V8_49_DVP_D2       |
| 17   | MIPI_CSI_D2_P    | 44   | GPIO_1V8_65_DVP_DEN      |
| 18   | GND              | 43   | GPIO_1V8_66_DVP_PCLK     |
| 19   | MIPI_CSI_CLK1_N  | 42   | GPIO_1V8_62_DVP_D15      |
| 20   | MIPI_CSI_CLK1_P  | 41   | GPIO_1V8_63_DVP_VSYNC    |
| 21   | GND              | 40   | GPIO_1V8_82 |
| 22   | MIPI_CSI_D3_N    | 39   | GPIO_1V8_67  |
| 23   | MIPI_CSI_D3_P    | 38   | GPIO_1V8_68  |
| 24   | GND              | 37   | GPIO_1V8_72  |
| 25   | MIPI_CSI_I2C_SCL | 36   | GPIO_1V8_73  |
| 26   | MIPI_CSI_I2C_SCA | 35   | GPIO_1V8_74  |
| 27   | GND              | 34   | GND          |
| 28   | GND              | 33   | GND          |
| 29   | 1V8              | 32   | 3V3          |
| 30   | 1V8              | 31   | 3V3          |

**Nota**: Preste atención al rango de nivel de los pines conectados cuando se conecte externamente para evitar que la entrada de voltaje incorrecta dañe permanentemente el chip K510. 

<div style="page-break-after:always"></div>

## 3.14 Salida de vídeo

&emsp; &emsp; El K510 CRB tiene una solapa 30P de paso de 0,5 mm debajo del conector FPC para conectarse a una pantalla LCD externa, como se muestra en la figura a continuación. Las definiciones de interfaz se muestran en la tabla siguiente.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-17.jpg">
</div>

<center>Figura 3-17 Interfaz de salida de vídeo</center>

<center>Tabla 3-3 Definiciones de interfaz de salida de vídeo</center>

| numeración | definición              | numeración | definición             |
| ---- | ----------------- | ---- | ---------------- |
| 1    | GND               | 16   | MIPI_DSI_D1_N    |
| 2    | GND               | 17   | MIPI_DSI_D1_P    |
| 3    | VDD_5V            | 18   | GND              |
| 4    | VDD_5V            | 19   | MIPI_DSI_CLK_N   |
| 5    | VDD_3V3           | 20   | MIPI_DSI_CLK_P   |
| 6    | VDD_3V3           | 21   | GND              |
| 7    | GND               | 22   | MIPI_DSI_D0_N    |
| 8    | TOUCH_1V8_I2C_SCL | 23   | MIPI_DSI_D0_P    |
| 9    | TOUCH_1V8_I2C_SDA | 24   | GND              |
| 10   | TOUCH_1V8_INT     | 25   | MIPI_DSI_D3_N    |
| 11   | TOUCH_1V8_RST     | 26   | MIPI_DSI_D3_P    |
| 12   | GND               | 27   | GND              |
| 13   | MIPI_DSI_D2_N     | 28   | MIPI_DSI_LCD_RST |
| 14   | MIPI_DSI_D2_P     | 29   | MIPI_DSI_LCD_EN  |
| 15   | GND               | 30   | GND              |

<div style="page-break-after:always"></div>

## 3.15 Ampliación de la interfaz

&emsp; &emsp; Con el fin de facilitar la implementación de funciones de expansión personalizadas para los usuarios, se reserva un pin de expansión 30P 2.54mm en el K510 CRB, que conduce a una fuente de alimentación y parte del GPIO, que el usuario puede operar a través del software iomux para mapear recursos de hardware como I2C, UART, SPI al GPIO correspondiente para lograr la conexión externa y la expansión de las funciones correspondientes. La interfaz integrada se muestra en la siguiente figura. Las definiciones detalladas se muestran en la tabla siguiente.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw-3-18.jpg">
</div>

<center>Figura 3-18 Interfaz de extensión de pin 40P</center>

<center>Tabla 3-4 Definiciones de interfaz extendida</center>

| numeración | definición         | numeración | definición         |
| ---- | ------------ | ---- | ------------ |
| 1    | VDD_1V8      | 2    | GND          |
| 3    | VDD_1V8      | 4    | GND          |
| 5    | VDD_3V3      | 6    | GND          |
| 7    | VDD_3V3      | 8    | GND          |
| 9    | VDD_5V       | 10   | GND          |
| 11   | VDD_5V       | 12   | GPIO_1V8_95  |
| 13   | GPIO_3V3_114 | 14   | GPIO_3V3_115 |
| 15   | GPIO_1V8_92  | 16   | GPIO_1V8_96  |
| 17   | GPIO_1V8_105 | 18   | GPIO_1V8_107 |
| 19   | GPIO_1V8_104 | 20   | GPIO_1V8_106 |
| 21   | GPIO_1V8_118 | 22   | GPIO_1V8_119 |
| 23   | GPIO_1V8_93  | 24   | GPIO_1V8_94  |
| 25   | GPIO_3V3_125 | 26   | GPIO_3V3_124 |
| 27   | GPIO_3V3_127 | 28   | GPIO_3V3_126 |
| 29   | GND          | 30   | GND          |

**Nota**: Preste atención al rango de nivel de los pines conectados cuando se conecte externamente para evitar que la entrada de voltaje incorrecta dañe permanentemente el chip K510. 

<div style="page-break-after:always"></div>

# 4 Uso de la placa de desarrollo

## 4.1 Instalación del controlador

&emsp; &emsp; El K510 CRB tiene ch340E incorporado para implementar la función de comunicación USB-UART, por lo que el controlador correspondiente debe instalarse antes de su uso.

&emsp; &emsp; Utilice el controlador del paquete o descárguelo e instálelo en la siguiente dirección.

&emsp;&emsp;<http://www.wch.cn/product/CH340.html>

## 4.2 Grabación de firmware

&emsp; &emsp; Consulte [la documentación de K510_SDK_Build_and_Burn_Guide](./K510_SDK_Build_and_Burn_Guide.md). 

## 4.3 Encender y apagar

&emsp; &emsp; 1) Instale el cable de alimentación y el cable de depuración USB.

&emsp; &emsp; 2) Interruptor DIP seleccionado para comenzar desde la tarjeta TF.

&emsp; &emsp; 3) Encienda el interruptor alternando el interruptor como se muestra en la Sección 3.2.

## 4.4 Depuración de puertos serie

&emsp; &emsp; Después de instalar el controlador, encienda el K510 CRB, momento en el que el puerto aparece en el Administrador de dispositivos - Puerto de la PC.

&emsp; &emsp; Con la herramienta de depuración de puerto serie, abra el número de puerto del dispositivo, velocidad en baudios 115200.

&emsp; &emsp; Como se muestra en la siguiente figura, el dispositivo es "COM6", que se muestra en el Administrador de dispositivos de PC.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_4_1.jpg">
</div>

<center>Figura 4-1 Administrador de dispositivos una vez completada la instalación del controlador</center>

**Descargo de responsabilidad de **traducción  
Para la comodidad de los clientes, Canaan utiliza un traductor de IA para traducir texto a varios idiomas, que pueden contener errores. No garantizamos la exactitud, fiabilidad o puntualidad de las traducciones proporcionadas. Canaan no será responsable de ninguna pérdida o daño causado por la confianza en la exactitud o fiabilidad de la información traducida. Si existe una diferencia de contenido entre las traducciones en diferentes idiomas, prevalecerá la versión en chino simplificado. 

Si desea informar de un error o inexactitud de traducción, no dude en ponerse en contacto con nosotros por correo.
