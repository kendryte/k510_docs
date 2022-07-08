![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">Mapa de memoria del sistema K510</font>**

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

| El número de versión   | Modificado por     | Fecha de revisión | Notas de revisión |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | Grupos de software del sistema | 2022-03-09 |   |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenido</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Planificación de la memoria del sistema K510

El plan de memoria del K510 se muestra en la siguiente figura:

![](../zh/images/system_memory_map/k510-system-memory-map.png)

Hay un DDR de 512MB en la placa de referencia K510 crb, con un total de cuatro áreas planificadas:

- Planificación de 0 ~ 240M para el kernel de Linux
- 240M ~ 496MB está planeado para la memoria compartida, utilizando el método de reservar el grupo de memoria CMA, de modo que el subsistema de administración de memoria del kernel de Linux también pueda asignar memoria del grupo CMA en ausencia de uso de memoria compartida
- 496M ~ 510M está planeado para el uso de DSP
- 510M ~ 512M está planeado para el uso del logotipo

# 2 Descripción del árbol de dispositivos

La planificación de la memoria del K510 se describe de una manera reservada-meory, a través de los nodos de memoria reservada del árbol de dispositivos. La información relevante del nodo del árbol de dispositivos es la siguiente:

```text
ddr_memory: memory@0 {
    status              = "okay";
    device_type         = "memory";
    reg                 = <0x0 0x00000000 0x0 0x20000000>;
};

sharem_cma:sharem_cma@8000000 {
    compatible          = "k510-share-memory-cma";
    reg                 = <0x0 0xf000000 0x0 0x10000000>;  /*240M~496M*/
};

reserved-memory {
    #address-cells = <2>;
    #size-cells = <2>;
    ranges;

    cma_buffer: buffer@f000000 {
        compatible = "shared-dma-pool";
        reusable;
        linux,cma-default;
        reg = <0x0 0xf000000 0x0 0x10000000>;
    };

    dsp_buffer: buffer@1f000000 {
        no-map;
        reg = <0x0 0x1f000000 0x0 0xe00000>;
    };

    logo_buffer: buffer@1fe00000 {
        no-map;
        reg = <0x0 0x1fe00000 0x0 0x200000>;
    };
};
```

# 3 Configuración relacionada con Buildroot

El plan de memoria del sistema se describe en dts del kernel de Linux, pero la dirección de carga del firmware dsp debe configurarse en buildroot:

configs/k510_crb_lp3_v0_1_defconfig:

configs/k510_crb_lp3_v1_2_defconfig:

BR2_TARGET_EVB_FIRMWARE_LOAD_ADD=0x1f000000

**Descargo de responsabilidad de **traducción  
Para la comodidad de los clientes, Canaan utiliza un traductor de IA para traducir texto a varios idiomas, que pueden contener errores. No garantizamos la exactitud, fiabilidad o puntualidad de las traducciones proporcionadas. Canaan no será responsable de ninguna pérdida o daño causado por la confianza en la exactitud o fiabilidad de la información traducida. Si existe una diferencia de contenido entre las traducciones en diferentes idiomas, prevalecerá la versión en chino simplificado. 

Si desea informar de un error o inexactitud de traducción, no dude en ponerse en contacto con nosotros por correo.