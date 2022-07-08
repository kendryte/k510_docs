![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">Guía K510 DSP CORE</font>**

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
Este documento es una guía para usar el núcleo DSP K510.

**<font face="黑体"  size=5>Objetos reader</font>**

Las principales personas a las que se aplica este documento (esta guía):

- Desarrolladores de software
- Personal de soporte técnico

**<font face="黑体"  size=5>Historial
 </font>**de revisiones <font face="宋体"  size=2>El historial de revisiones acumula una descripción de cada actualización del documento. La versión más reciente del documento contiene actualizaciones para todas las versiones anteriores. </font>

| El número de versión   | Modificado por     | Fecha de revisión | Notas de revisión |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | Grupos de software del sistema | 2022-03-09 |         |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenido</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Visión general

Hay tres procesadores en el chip K510, de los cuales la CPU dual cores ejecuta Linux, y el núcleo DSP está inactivo para que los usuarios lo desarrollen y usen, y este documento proporciona el núcleo DSP como una rutina de referencia para que el coprocesador ejecute programas bare metal.

![](../zh/images/doc_dsp/image-dsp_1.png)

<center> Figura 1 diagrama de bloques k510 </center>

# 1 programa DSP cargado

 k510_buildroot/package/dsp_app_new directorio, es el código que carga el DSP y lo ejecuta en el espacio de usuario de Linux. dsp_app_new código implementa principalmente la carga del firmware DSP en la ubicación especificada e inicia el DSP para iniciar la ejecución, su código principal es el siguiente:

```c
/*将DSP固件从pDspBinmPath路径下加载到DspRestVector位置。*/
if (kendryte_dsp_load_bin(DspRestVector, pDspBinmPath)) {
    printf("ERR: Load dsp bin file err\n");
    return -1;
} else {
    printf("Load dsp success\n");
}

/*启动DspRestVector位置处的DSP固件运行。*/
if (kendryte_dsp_boot(DspRestVector)) {
    printf("ERR: Boot dsp err\n");
    return -1;
}
```

dsp_app_new programa ejecutable compilado se almacena en el directorio root file system/app/dsp_app_new.

# 2 Impresión de información DSP

 k510_buildroot/package/dsp_log directorio, es el código que consulta si el núcleo DSP tiene salida log, que se ejecuta en el espacio de usuario de Linux. dsp_log El programa ejecutable compilado se almacena en el directorio root file system/app/dsp_log.

Después de encenderse, el dsp_log se ejecutará en segundo plano de forma predeterminada, y su archivo de configuración es: k510_buildroot/board/canaan/k510/k510_rootfs_skeleton/etc/init.d/rc.sysinit

![](../zh/images/doc_dsp/image-dsp_log.png)

# 3 DSP demo bare metal

## 3.1 fft

Se encuentra el programa de demostración fft`/app/dsp_app_new/fft.bin`.
El código fuente del programa de demostración fft se coloca en`k510_buildroot/package/k510_evb_test/src/test/fft` el directorio.

Vaya al directorio /app/dsp_app_new':

- `dsp_app`: Programas que cargan el DSP y hacen que el DSP se ejecute (se ejecutan en el espacio de usuario de Linux)
- `fft.bin`: Programa DSP bare metal

Inicie el programa fft y ejecute:

```shell
cd /app/dsp_app_new
./dsp_app fft.bin
```

Puedes ver la siguiente impresión:

![Demostración de DSP](../zh/images/doc_dsp/demo_dsp.png)

Ahora el firmware que se ejecuta en DSP es un programa de demostración para fct.

## 3.2 simd_umul8

Simd_umul8 encuentra el programa de demostración`/app/dsp_app_new/simd_umul8_demo.bin`.
simd_umul8 el código fuente del programa de demostración se coloca `k510_buildroot/package/k510_evb_test/src/test/simd_umul8_demo`en el directorio, el trabajo principal realizado es el siguiente:

- En la demostración, deje que dos datos de 32 bits se "multipliquen", es decir, divida cada dato de 32 bits en 4 datos de 8 bits y luego multiplíquelos respectivamente para obtener 4 resultados de 16 bits, y verifique si los resultados del cálculo son los esperados. Por ejemplo, 0x05050505 multiplica por 0x02020202 da como resultado 0x000a000a000a000a.
- Si es como se esperaba, imprima `DSP SIMD UMUL8 TEST PASS`la información, de lo contrario imprima`DSP SIMD UMUL8 TEST FAIL` la información

Método para ejecutar la demostración:

```shell
cd /app/dsp_app_new
./dsp_app simd_umul8_demo.bin
```

Puede encontrar instrucciones específicas en [la Documentación del producto - Andes Technology](http://www.andestech.com/en/products-solutions/product-documentation/) para descargar la Especificación de extensión AndeStar V5 DSP ISA .PDF (v1.0, 2019-03-25), consulte la Sección 3.172.

## 3.3 API del programador DSP

Cuando el rendimiento de la CPU no puede satisfacer algunas aplicaciones, puede dividir una parte de la función para ejecutarla en el DSP para reducir la carga de la CPU. No hay ningún sistema operativo en el DSP, por lo que se implementa un administrador de programación de tareas y el código está en el directorio de k510_buildroot/package/dsp_scheduler. Las tareas que se ejecutan en el DSP se compilan en bibliotecas estáticas, previnculadas con el programador DSP, y la CPU en tiempo de ejecución envía un mensaje al dsp a través del buzón para iniciar la ejecución de tareas correspondiente.

Los usuarios pueden definir prioridades al registrar tareas, y el programador DSP programa las tareas de acuerdo con las prioridades. El valor devuelto de la función run de la interfaz de ejecución de tareas determina si es RUN_ONCE o CONTINUE_RUN, de modo que el usuario pueda decidir por sí mismo cuántas veces se ejecuta la tarea.

Cómo enviar mensajes a dsps a través del marco de buzones de linux, consulte la introducción correspondiente en el documento K510_Mailbox_Developer_Guides. La implementación de referencia está en k510_buildroot/package/k510_evb_test/src/test/mailbox_demo/cpu2dsp_task_demo.c

### 3.3.1 Descripciones de archivos de encabezado

1. k510_buildroot/package/dsp_scheduler/src/dsp_tasks.h

    El programa que se ejecuta en la CPU debe incluir este archivo de encabezado, que define el tipo de mensaje y la estructura entre la CPU y el dsp, y la comunicación del mensaje del sistema adopta un método de pregunta y respuesta, y la CPU debe esperar hasta el mismo mensaje enviado por el dsp después de enviar el mensaje para indicar que el dsp está procesado. Los mensajes de usuario pueden definir sus propios mecanismos según sea necesario. El mensaje significa lo siguiente:

    - DSP_TASK_ENABLE

    Cuando la tarea correspondiente comienza a ejecutarse, este mensaje puede ir seguido de una dirección de memoria para la información de depuración de impresión de la tarea en el dsp

    - DSP_TASK_DISABLE

    La tarea correspondiente deja de ejecutarse

    - DSP_TASK_PRINT_INFO

    Imprime toda la información de la tarea registrada

    - DSP_TASK_USER_MSG

    Los mensajes de tareas definidos por el usuario, que siguen una dirección de memoria, permiten a los usuarios diseñar sus propios mecanismos de cola de mensajes y comunicación de mensajes según sea necesario.

    ```c
    typedef enum
    {
        DSP_TASK_ENABLE = 0x10000000,
        DSP_TASK_DISABLE,
        DSP_TASK_PRINT_INFO,
        DSP_TASK_USER_MSG,
        MAX_NUM_DSP_TASK_MSG
    } DspTaskMsg;

    typedef struct tDSP_MESSAGE
    {
        DspTaskMsg      msgId;         /**<Message ID*/
        unsigned int    msg_phyAddr;   /**<Message content, shared memory physical address
                                        when msgId is DSP_TASK_ENABLE, it is
                                        buffer address for print log
                                    */
        unsigned int    len;           /**<Length of message*/
    } DSP_MESSAGE;
    ```

2. k510_buildroot/package/dsp_scheduler/src/scheduler.h
    Los programas que se ejecutan en dsp requieren incluir este archivo de encabezado

### 3.3.2 Descripción de la función API

#### 3.3.2.1 SCHE_TaskRegister

【Descripción】

Registrar una tarea. Se pueden registrar hasta 8 tareas en el DSP, cada una de las cuales se comunica a través de un canal de buzón y una CPU. La tarea 0 corresponde al número de canal del buzón de correo de 0, DSP_TASK_0_CH corresponde al MBOX_CHAN_0_TX del buzón de cpu, etc.

Implementar la siguiente estructura de tareas

```c
DSP_TASK dsp_sample_task = {
    .name             = "sample task",
    .priority         = 2,
    .init             = sample_task_init,
    .deinit           = sample_task_deinit,
    .run              = sample_task_run,
    .rev_callback     = sample_task_callback,
    .ack_callback     = sample_ack_callback,
};
```

En k510_buildroot/package/dsp_scheduler/alltasks.c, registre la tarea con el código siguiente:

```c
{
    extern DSP_TASK dsp_sample_task;
    SCHE_TaskRegister(&dsp_sample_task, DSP_TASK_0_CH);
}
```

【Gramática】

```c
ScheStatus SCHE_TaskRegister(DSP_TASK *task, DspTaskChannel ch)
```

【Parámetros】

```c
typedef enum
{
    DSP_TASK_0_CH = 0,
    DSP_TASK_1_CH,
    DSP_TASK_2_CH,
    DSP_TASK_3_CH,
    DSP_TASK_4_CH,
    DSP_TASK_5_CH,
    DSP_TASK_6_CH,
    DSP_TASK_7_CH,
    MAX_NUM_DSP_TASKS
} DspTaskChannel;

typedef enum
{
    SCHE_RUN_ONCE = 0,
    SCHE_CONTINUE_RUN = 1,
}ScheRunType;

typedef struct DSP_TASK
{
    /**task name*/
    char *name;

    /**priority 0 to 255, 0 is the highest*/
    int priority;

    /**init function
       return task context pointer
    */
    void *(*init)();

    /**deinit function*/
    void (*deinit)(void *arg);

    /**task process function
       return 0 means run once
       return 1 means conitune run
    */
    ScheRunType (*run)(void *arg);

    /**ISR callback
       for receiving msg from cpu
    */
    void (*rev_callback)(void *arg);

    /**ISR callback
       for ack msg from cpu after dsp send msg to cpu
    */
    void (*ack_callback)(void *arg);
} DSP_TASK;
```

#### 3.2.2 SCHE_SendMessage

【Descripción】

Las tareas en el dsp envían mensajes a la CPU a través de esta interfaz

```c
ScheStatus SCHE_SendMessage(DSP_MESSAGE *pMsg, DspTaskChannel ch)
```

【Parámetros】

Consulte la Sección 3.3.1 para obtener instrucciones.

#### 3.2.3 SCHE_GetMessage

【Descripción】

Las tareas en el dsp reciben mensajes de la CPU a través de esta interfaz

```c
ScheStatus SCHE_GetMessage(DSP_MESSAGE *pMsg, DspTaskChannel ch)
```

【Parámetros】

Consulte la Sección 3.3.1 para obtener instrucciones.

### 3.3.3 DSP Scheduler aplica columnas reales

Ejecute el siguiente comando para cargar el programador dsp del programa bare metal:

```shell
cd /app/dsp_app_new
./dsp_app ../dsp_scheduler/scheduler.bin
```

En la ventana del shell, puede ver el siguiente registro, lo que indica que el programador dsp se ha cargado correctamente.

```text
dsp schduler start
dsp schduler: register sample task successful, ch 0
dsp schduler: register audio3a task successful, ch 1
```

Ingrese el directorio /app/mailbox_demo, ingrese el siguiente comando, la cpu enviará un comando a dsp para iniciar una tarea y enviará una solicitud para procesar los datos, el procesamiento dsp enviará un mensaje para notificar a la cpu, de modo que el bucle.

```shell
cd /app/mailbox_demo
/app/mailbox_demo/cpu2dsp_task_demo
```

Consulte el siguiente registro, que indica que la tarea especificada por la cpu especificada por dsp se realizó correctamente.

```shell
[root@canaan ~/data ]$ ./cpu2dsp_task_demo
task 0 message buffer: vaddr 0x18000, phyAddr 0x1fdff000, size 4096
task 0 print buffer: vaddr 0x18000, phyAddr 0x1fdfd000, size 4096
task 0 src buffer: vaddr 0x14d000, phyAddr 0x1fdfb000, size 4096
task 0 dst buffer: vaddr 0x14e000, phyAddr 0x1fdf9000, size 4096
printc_init>log_id 0, cur_addr 0x1fdfd000, log_len 4096
dsp process_command>task 0: init done
task 0 is enabled
cpu send PROCESS_START
cpu receive PROCESS_END
cpu send PROCESS_START
cpu receive PROCESS_END
cpu send PROCESS_START
cpu receive PROCESS_END
cpu send PROCESS_START
cpu receive PROCESS_END
cpu send PROCESS_START
cpu receive PROCESS_END
cpu send PROCESS_START
cpu receive PROCESS_END
cpu send PROCESS_START
cpu receive PROCESS_END
^C //按下ctrl+c后
cpu send PROCESS_START
cpu receive PROCESS_END
dsp process_command>task 0: deinit done
task 0 is disabled
exit: task0 is disabled
cpu2dsp_task_demo: exit successful
```

**Descargo de responsabilidad de**traducción  
Para la comodidad de los clientes, Canaan utiliza un traductor de IA para traducir texto a varios idiomas, que pueden contener errores. No garantizamos la exactitud, fiabilidad o puntualidad de las traducciones proporcionadas. Canaan no será responsable de ninguna pérdida o daño causado por la confianza en la exactitud o fiabilidad de la información traducida. Si existe una diferencia de contenido entre las traducciones en diferentes idiomas, prevalecerá la versión en chino simplificado.

Si desea informar de un error o inexactitud de traducción, no dude en ponerse en contacto con nosotros por correo.
