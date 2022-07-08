![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 Guías de herramientas de ajuste de ISP</font>**

<font face="黑体"  size=3>Versión del documento: V1.0.0</font>

<font face="黑体"  size=3>Publicado: 2022-03-31</font>

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
Este documento es una documentación de ISP Tuning Tool. 

**<font face="黑体"  size=5>Objetos reader</font>**

La audiencia principal de este documento son ingenieros de software experimentados, ingenieros de algoritmos de imagen, diseñadores de sistemas e integradores de sistemas que desean implementar aplicaciones y controladores propietarios.

**<font face="黑体"  size=5>Historial 
 </font>**de revisiones <font face="宋体"  size=2>El historial de revisiones acumula una descripción de cada actualización del documento. La versión más reciente del documento contiene actualizaciones para todas las versiones anteriores. </font>

| El número de versión   | Modificado por     | Fecha de revisión | Notas de revisión |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | Grupos de software del sistema | 2022-03-31 | Lanzamiento del SDK V1.6 |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenido</font>**

[TOC]

<div style="page-break-after:always"></div>

# Introducción al marco de herramientas de ajuste de ISP

En esta sección se describen las herramientas de ajuste de ISP y las descripciones de los flujos de datos que se proporcionan a los procesadores de nivel superior para controlar la optimización general de la imagen del ISP.

```text
+----------------------------------------------------+
|                                                    |
|                      K510                          |
|                                                    |
|    +-------+        +--------------------------+   |
|    |       |        |                          |   |
|    |  ISP  +------> |   v4l2_drm_isptool.out   |   |
|    |       |        |                          |   |
|    +-------+        +-------------+------------+   |
|                                   |                |
|                                   |                |
|    +-----------------+            |                |
|    |                 |            |                |
|    |   isp-tuningd   | <----------+                |
|    |                 |                             |
|    +^-+--------------+                             |
|     | |                                            |
|     | |                                            |
+----------------------------------------------------+
      | |
      | |
+-------------------------------+
|     | |                       |
|     | |       PC              |
|     | |                       |
|    ++-v------------------+    |
|    |                     |    |
|    |  ISP Tuning Tool    |    |
|    |                     |    |
|    +---------------------+    |
|                               |
+-------------------------------+
```

## Ajustar el tráfico de la herramienta

El protocolo de comunicación se puede encontrar en la documentación en el repositorio de código de cliente, y la herramienta consta de dos partes, una es el cliente isp-tuningd que se ejecuta en la PC, el programa se encuentra en el /app/mediactl_lib/isp-tuningd, y la otra parte es el servidor que se ejecuta en el K510. De forma predeterminada, el puerto 9982 de TCP se utiliza para la comunicación.

### cliente

ISP Tuning Tool es una aplicación que se ejecuta en un PC. Además de poder establecer registros, también se admiten la calibración AWB y la calibración CCM.

### Del lado del servidor

isp-tuningd recibe una imagen yuv (NV12) en tamaño de 3133440 bytes de la entrada estándar y la transmite a todos los clientes, podemos usar v4l2_drm_isptool, iniciará automáticamente isp-tuningd y enviará los datos de la imagen, el uso específico es consistente con el v4l2_drm. Podemos ejecutarlo con el siguiente comando

```shell
cd /app/mediactl_lib
./v4l2_drm_isptool -f video_drm_1080x1920.conf
```

# Opciones de ajuste de ISP

Muchos registros y tablas se proporcionan en el ISP K510 para el control y la sintonización. La configuración de los registros de hardware del ISP es muy importante para la calidad de la imagen. En la actualidad, en la plataforma K510, el proceso de ajuste de imágenes solo se implementa a través de TCP Socket.

## Ventana principal de la herramienta de ajuste

En esta sección se describen las características de estos paneles en la ventana de ajuste.

La Figura 3-1 muestra todo el panel del operador en la ventana de ajuste

- El panel 1 es el** menú **que puede cargar opcionalmente el archivo ISP configurado o realizar la calibración. 
- El panel 2 es el **panel de control de conexión**, complete la dirección IP y el número de puerto de la placa de desarrollo (puerto predeterminado 9982) y haga clic en el botón verde de conexión para conectarse. 
- El panel 3 es el **panel de registro**, si necesita configurar o leer el registro no está en este, puede usar este panel para configurar y leer. 
- El panel 4 es un **panel de selección de **parámetros de ajuste, el usuario puede seleccionar varios parámetros o grupos de parámetros de acuerdo con el texto del mensaje del panel, los registros de estas selecciones se mostrarán en el panel 5. 
- El panel 5 es el **panel Configuración de parámetros de ajuste**, que se utiliza para establecer u obtener valores de parámetros del servidor de ajuste. 
- El panel 6 es un **panel de visualización de imágenes**, que muestra la salida de la imagen por parte del ISP y puede hacer clic en el botón de pausa en el medio cuando no es necesario reproducir todo el tiempo. 

![Figura 3-1 Ventana principal de la herramienta de ajuste](../zh/images/sdk_application/clip_image033.png)

LA herramienta de ajuste de ISP** no **adquiere automáticamente todos los valores de registro después de conectarse, y si necesita obtener todos los valores de registro, puede hacer clic en el** botón Leer en el lado derecho del panel de control de conexión** para extraer todos los valores de registro actuales. 

# Calibración y calibración

En esta sección se describen las instrucciones para la calibración y la calibración mediante herramientas de ajuste de ISP, como el balance de blancos automático (AWB), la matriz de corrección de color (CCM), la gamma y las sombras de lente (LSC).

## AWB

### Preparativos

1. Caja de luz estándar con fuente de luz D65 estándar
2. Tarjeta de color estándar de 24, actualmente solo se admite la tarjeta de color X-RITE
3. Una cámara lista para la calibración puede emitir una imagen original del sensor o una imagen procesada
4. ISP también solo abre el módulo de algoritmo de corrección de nivel de negro y des-mosaico, CSC y otros módulos de conversión de formato deben prestar atención a la simetría (la matriz es matriz inversa), además de la reducción de ruido, la nitidez y otros módulos tienen poco impacto, pero también intentan cerrarse, los módulos no lineales y los módulos de procesamiento de color (GAMMA, dinámica amplia, AWB, CCM, ajuste de saturación, etc.) deben apagarse

### Obtiene la imagen

1. La cámara está dirigida a la tarjeta de 24 colores, asegúrese de que la tarjeta de 24 colores llene toda la imagen y luego tome la imagen, en la que se puede hacer clic para pausar la reproducción sin garantizar la precisión, como se muestra en la siguiente figura

    ![Figura 4-1 Se toman 24 tarjetas de color](../zh/images/sdk_application/clip_image014.jpg)

2. La imagen capturada debe prestar atención al brillo moderado y la oscuridad, y demasiado brillante y demasiado oscuro afectará la calibración

### demarcar

Haga clic en "Calibración" en la barra de menú, seleccione "AWB" para realizar la calibración y el programa seleccionará automáticamente la tarjeta de color

![Figura 4-2 Selector de color de cuadro automático](../zh/images/sdk_application/clip_image016.jpg)

Presione cualquier tecla para continuar, apareciendo la imagen después de que se complete el balance de blancos

![Figura 4-3 Calibración AWB completa](../zh/images/sdk_application/clip_image018.jpg)

Si no hay ningún problema, continúe presionando cualquier tecla, la herramienta abrirá un cuadro de diálogo preguntando si el parámetro es razonable, sí lo llenará en los registros relacionados con la interfaz principal, de lo contrario abandonará el resultado de calibración, si es así, la herramienta continuará preguntando si escribir en el registro del dispositivo.

## CC

De acuerdo con la calibración AWB, no se repetirá.

## Gamma

La fórmula para la curva gamma estándar es
$$
Y=aX^b
$$
Donde $b$ es el coeficiente Gamma, que generalmente es menor que 1 en el extremo de la imagen y mayor que 1 en el extremo de la pantalla. El valor de $a$ se puede calcular en base al valor de $b$

$$
a=\frac{256}{256^b}
$$
El principio de la fórmula es que la entrada es 256, que sigue siendo 256 después de la corrección Gamma.

Cuando el coeficiente gamma b es 0,5, la curva se muestra en la siguiente figura

![](../zh/images/sdk_application/clip_image025.png)

## LSC

### Preparativos

- Una toma captura una fotografía en formato RAW

### principio

Debido a que el centro de la lente es inconsistente con la transmisión de luz circundante, el brillo de la imagen es desigual, por lo que el ajuste de la curva genera una superficie correctiva para compensar este problema.

La corrección se muestra en la siguiente figura

![Antes de la corrección](../zh/images/sdk_application/clip_image029.png)

Después de la corrección, se muestra en la siguiente figura

![Después de la corrección](../zh/images/sdk_application/clip_image031.png)

**Descargo de responsabilidad de **traducción  
Para la comodidad de los clientes, Canaan utiliza un traductor de IA para traducir texto a varios idiomas, que pueden contener errores. No garantizamos la exactitud, fiabilidad o puntualidad de las traducciones proporcionadas. Canaan no será responsable de ninguna pérdida o daño causado por la confianza en la exactitud o fiabilidad de la información traducida. Si existe una diferencia de contenido entre las traducciones en diferentes idiomas, prevalecerá la versión en chino simplificado. 

Si desea informar de un error o inexactitud de traducción, no dude en ponerse en contacto con nosotros por correo.