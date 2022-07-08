![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">Guía del desarrollador de K510 U-boot</font>**

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
Este documento es un documento de soporte del sdk de la placa de demostración K510, que presenta principalmente contenido relacionado con uboot, como el archivo de configuración de la placa de demostración k510, el árbol de dispositivos, la ubicación del controlador y otra información en uboot. 

**<font face="黑体"  size=5>Objetos reader</font>**

Las principales personas a las que se aplica este documento (esta guía):

- Desarrolladores de software
- Personal de soporte técnico

**<font face="黑体"  size=5>Historial 
 </font>**de revisiones <font face="宋体"  size=2>El historial de revisiones acumula una descripción de cada actualización del documento. La versión más reciente del documento contiene actualizaciones para todas las versiones anteriores. </font>

| El número de versión   | Modificado por     | Fecha de revisión | Notas de revisión |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | Grupos de software del sistema | 2022-03-09 |          |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenido</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Introducción a U-Boot

U-boot es parte del sdk, y la versión de u-boot utilizada actualmente por el SDK es 2020.01. Uboot es un programa de gestor de arranque desarrollado por el grupo alemán DENX para una variedad de CPU integradas, UBoot no solo admite el arranque de sistemas Linux integrados, actualmente, también es compatible con netBSD, VxWorks, QNX, RTEMS, ARTOS, sistema operativo integrado LynxOS. Además de admitir la serie de procesadores PowerPC, UBoot también puede admitir MIPS, x86, ARM, NIOS, RISICV, etc., las funciones principales son inicializar memoria, arrancar sistemas Linux, más introducción de u-boot, consulte<https://www.denx.de/wiki/U-Boot>

# 2 Introducción al entorno de desarrollo

- Sistema operativo

| numeración | Recursos de software | ilustrar        |
| ---- | -------- | ----------- |
| 1    | Ubuntu   | 18.04/20.04 |

- Entorno de software

Los requisitos del entorno de software se muestran en la tabla siguiente:

| numeración | Recursos de software | ilustrar |
| ---- | -------- | ---- |
| 1    | K510 SDK |      |

# 3 Cómo conseguirlo

Descargue y compile el sdk, el sdk descargará el código uboot al compilar y compilará el código uboot. Para obtener más información acerca de cómo descargar y compilar el SDK, consulte[ K510_SDK_Build_and_Burn_Guide.md](./K510_SDK_Build_and_Burn_Guide.md)

# 4 Directorios importantes y descripciones de archivos

En este capítulo se utiliza k510_evb_lp3_v1_1_defconfig compilados como ejemplo. El método de compilación del sdk correspondiente es make CONF=k510_evb_lp3_v1_1_defconfig, y el directorio después de la compilación es el siguiente:

![imagen-20210930135634105](../zh/images/uboot_guides/build_out.png)

k510_evb_lp3_v1_1_defconfig/build/uboot-custom --- el código y el directorio de compilación de uboot;

board/canaan/k510/uboot-sdcard.esv--- archivo de configuración de variable de entorno predeterminado de uboot

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/configs/k510_evb_lp3_v1_1_defconfig --uboot archivo de configuración;

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/arch/riscv/dts/k510_evb_lp3_v1_1.dts---- archivo de árbol de dispositivos;

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/include/configs/k510_evb_lp3_v1_1.h--- archivo de encabezado;

k510_evb_lp3_v1_1_defconfig/images/u-boot_burn.bin ---uboot parpadea el firmware

buildroot-2020.02.11/boot/uboot ----buildroot en el script de compilación sobre uboot, generalmente no necesita ser modificado;

Archivo de configuración Configs/k510_evb_lp3_v1_1_defconfig---sdk, BR2_TARGET_UBOOT_BOARD_DEFCONFIG especificar el archivo de configuración de uboot;

# 5 uboot inicia el proceso

_start(arch/riscv/cpu/start. S, línea 43)

board_init_f(common/board_f.c, línea 1013)

board_init_r(common/board_r.c, línea 845)

run_main_loop(common/board_r.c, línea 637)

# 6 uboot en la descripción del controlador

## Controlador 6.1 ddr

tablero/Canaán/k510_evb_lp3/ddr_init.c

## 6.2 Unidad eth

drivers/net/macb.c

Árbol de dispositivos:

```text
ethernet@93030000 {
    compatible = "cdns,macb";
    reg = <0x0 0x93030000 0x0 0x10000>;
    phy-mode = "rmii";
    interrupts = <0x36 0x4>;
    interrupt-parent = <0x4>;
    clocks = <0x5 0x5>;
    clock-names = "hclk", "pclk";
};
```

## 6.3 Unidad de puerto serie

controladores/serie/ns16550.c

Árbol de dispositivos:

```text
serial@96000000 {
    compatible = "andestech,uart16550", "ns16550a";
    reg = <0x0 0x96000000 0x0 0x1000>;
    interrupts = <0x19 0x4>;
    clock-frequency = <0x17d7840>;
    reg-shift = <0x2>;
    reg-io-width = <0x4>;
    no-loopback-test = <0x1>;
    interrupt-parent = <0x4>;
};
```

## 6.4 iomux

drivers/pinctrl/pinctrl-single.c

Árbol de dispositivos:

```text
iomux@97040000 {
    compatible = "pinctrl-single";
    reg = <0x0 0x97040000 0x0 0x10000>;
    #address-cells = <0x1>;
    #size-cells = <0x0>;
    #pinctrl-cells = <0x1>;
    pinctrl-single,register-width = <0x20>;
    pinctrl-single,function-mask = <0xffffffff>;
    pinctrl-names = "default";
    pinctrl-0 = <0x6 0x7 0x8 0x9 0xa>;

    iomux_uart0_pins {
        pinctrl-single,pins = <0x1c0 0x540ca8 0x1c4 0x5a0c69>;
        phandle = <0x6>;
    };

    iomux_emac_pins {
        pinctrl-single,pins = <0x8c 0x4e 0x90 0xce 0x88 0x8e 0x98 0x4e 0x80 0x8e 0xb8 0x4e 0xb4 0x4e 0xa8 0x8e 0xa4 0x8e 0x74 0x8e>;
        phandle = <0x7>;
    };

    iomux_spi0_pins {
        pinctrl-single,pins = <0x158 0x4e 0x15c 0x4e 0x160 0xce 0x164 0xce 0x168 0xce 0x16c 0xce 0x170 0xce 0x174 0xce 0x178 0xce 0x17c 0xce 0x180 0x8e>;
        phandle = <0x8>;
    };

    iomux_mmc0_pins {
        pinctrl-single,pins = <0x1c 0x4e 0x20 0xce 0x24 0xce 0x28 0xce 0x2c 0xce 0x30 0xce 0x34 0xce 0x38 0xce 0x3c 0xce 0x40 0xce>;
        phandle = <0x9>;
    };

    iomux_mmc2_pins {
        pinctrl-single,pins = <0x5c 0x4e 0x60 0xce 0x64 0xce 0x68 0xce 0x6c 0xce 0x70 0xce>;
        phandle = <0xa>;
    };
};
```

## Unidad de 6,5 mmc y tarjeta SD

drivers/mmc/sdhci-cadence.c

Árbol de dispositivos

```text
mmc0@93000000 {
    compatible = "socionext,uniphier-sd4hc", "cdns,sd4hc";
    reg = <0x0 0x93000000 0x0 0x400>;
    interrupts = <0x30 0x4>;
    interrupt-parent = <0x4>;
    clocks = <0xb 0x4>;
    max-frequency = <0xbebc200>;
    cap-mmc-highspeed;
    bus-width = <0x8>;
};

mmc2@93020000 {
    compatible = "socionext,uniphier-sd4hc", "cdns,sd4hc";
    reg = <0x0 0x93020000 0x0 0x400>;
    interrupts = <0x32 0x4>;
    interrupt-parent = <0x4>;
    clocks = <0xb 0x4>;
    max-frequency = <0xbebc200>;
    cap-sd-highspeed;
    bus-width = <0x1>;
};
```

# 7 Variable de entorno predeterminada de Uboot

La variable de entorno predeterminada para uboot se encuentra en el directorio board/canaan/k510 del SDK, predefinida como un archivo de texto:

uboot-emmc.esv

uboot-nfs.esv

uboot-sdcard.esv

El script POST del SDK llamará a mkenvimage en tiempo de compilación para compilar la definición de la variable de entorno de texto en una imagen binaria que uboot puede cargar y colocar en la partición de arranque.

Estos son algunos ejemplos:

uboot-sdcard.esv

```text
bootm_size=0x2000000
bootdelay=3

stderr=serial@96000000
stdin=serial@96000000
stdout=serial@96000000
arch=riscv
baudrate=115200

ipaddr=10.100.226.221
netmask=255.255.255.0
gatewayip=10.100.226.254
serverip=10.100.226.63
bootargs=root=/dev/mmcblk1p2 rw console=ttyS0,115200n8 debug loglevel=7

bootcmd=fatload mmc 1:1 0x600000 bootm-bbl.img;fatload mmc 1:1 0x2000000 k510.dtb;bootm 0x600000 - 0x2000000
bootcmd_nfs=tftp 0x600000 bootm-bbl.img;tftp 0x2000000 k510_nfsroot.dtb;bootm 0x600000 - 0x2000000
```

Nota: Los bootargs del parámetro de arranque del kernel se establecen mediante la variable de entorno predeterminada de uboot, y los bootargs en dts se sobrescribirán. Ver FAQ - ¿Dónde llegaron los bootargs y pasaron al kernel?

# 8 Actualizaciones del programa Uboot

## 8.1 Método de duplicación del sdk parpadeante

La imagen del sdk ya contiene un programa uboot, que muestra directamente la imagen del sdk, como: archivo k510_evb_lp3_v1_1_defconfig/images/sysimage-sdcard.img

## 8.2 Linux actualiza el programa uboot dentro de la tarjeta SD

Coloque el archivo u-boot_burn.bin en el directorio tftp, configure la dirección IP del puerto de red del dispositivo e ingrese el directorio /root/sd/p1; Ejecute el comando tftp -gr u-boot_burn.bin xxx.xxx.xxx.xxx.xx;

## 8.3 Linux actualiza el programa uboot dentro de emmc

Coloque el archivo u-boot_burn.bin en el directorio tftp, configure la dirección IP del puerto de red del dispositivo y descargue el archivo en el dispositivo a través de tftp -gr u-boot_burn.bin xxx.xxx.xxx.xxx.xxx.xx;

Ejecute el comando dd if=u-boot_burn.bin of=/dev/mmcblk0p1 para escribir el archivo en la tarjeta mmc.

# 9 Preguntas Frecuentes

## 9.1 ¿Cómo se configura la frecuencia DDR?

R: En la actualidad, el EVB solo puede ejecutar 800, y el CRB puede establecer 800 o 1600. Método de configuración de frecuencia ddr de la placa CrB consulte el archivo uboot board\Canaan\k510_crb_lp3\ddr_param.h, 800M corresponde a #define DDR_800 1, 1600M corresponde a #define DDR_1600 1.

## 9.2 ¿Dónde llegaron los bootargs y pasaron al núcleo?

R: Obtenido de la variable de entorno uboot bootargs, uboot modificará los parámetros bootargs en el árbol de dispositivos de memoria de acuerdo con el valor de la variable de entorno bootargs al arrancar el kernel. El código pertinente es el siguiente:

```c
int fdt_chosen(void *fdt)
{
    int   nodeoffset;
    int   err;
    char  *str; /* used to set string properties */

    err = fdt_check_header(fdt);
    if (err < 0) {
        printf("fdt_chosen: %s\n", fdt_strerror(err));
        return err;
    }

    /* find or create "/chosen" node. */
    nodeoffset = fdt_find_or_add_subnode(fdt, 0, "chosen");
    if (nodeoffset < 0)
        return nodeoffset;

    str = env_get("bootargs");
    if (str) {
        err = fdt_setprop(fdt, nodeoffset, "bootargs", str,
                    strlen(str) + 1);
        if (err < 0) {
            printf("WARNING: could not set bootargs %s.\n",
                    fdt_strerror(err));
            return err;
        }
    }

    return fdt_fixup_stdout(fdt, nodeoffset);
}
```

## 9.3 ¿Los parámetros de inicio son inconsistentes con el archivo de árbol de dispositivos compilado?

R: uboot obtiene dinámicamente las variables de entorno según el modo de arranque y actualiza el árbol de dispositivos en la memoria de acuerdo con las variables de entorno de bootargs al arrancar el kernel. Después de los parámetros de arranque modificados, consulte el nodo /sys/firmware/devicetree/base/chosen.

## 9.4 ¿Dónde se guardan las variables de entorno de uboot?

Respuesta:

| Modo de inicio | Ubicación de lectura y guardado de UBoot | Archivos correspondientes en tiempo de compilación |
| :-: | :-: | :-: |
| Botas EMMC | Emmc el archivo uboot-emmc.env para la segunda partición | placa\canaan\k510\uboot-emmc.esv |
| Arranque de la tarjeta SD | El archivo uboot-sd.env de la primera partición de la tarjeta SD | placa\canaan\k510\uboot-sd.esv |

## 9.5 ¿Cómo configurar qos?

R: Los registros relacionados con QOS son QOS_CTRL0 QOS_CTRL1 QOS_CTRL2 QOS_CTRL3 QOS_CTRL4. Ejemplo:
Después de configurar qos, el rendimiento de la demostración de nncase ha mejorado

```c
*(uint32_t *)0x970E00FC = (0x2 << 8) | (0x2 << 12) | (0x2 << 16) | (0x2 << 20) | (0x2 << 24);
*(uint32_t *)0x970E0100 = (0x3 << 4) | 0x3;
*(uint32_t *)0x970E00F4 = (0x5 << 16) | (0x5 << 20);
```

**Descargo de responsabilidad de **traducción  
Para la comodidad de los clientes, Canaan utiliza un traductor de IA para traducir texto a varios idiomas, que pueden contener errores. No garantizamos la exactitud, fiabilidad o puntualidad de las traducciones proporcionadas. Canaan no será responsable de ninguna pérdida o daño causado por la confianza en la exactitud o fiabilidad de la información traducida. Si existe una diferencia de contenido entre las traducciones en diferentes idiomas, prevalecerá la versión en chino simplificado. 

Si desea informar de un error o inexactitud de traducción, no dude en ponerse en contacto con nosotros por correo.