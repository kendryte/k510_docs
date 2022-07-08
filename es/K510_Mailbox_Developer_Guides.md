![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">Guía del desarrollador de buzones de correo K510</font>**

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
Este documento es un documento de desarrollo para el controlador de buzón K510.

**<font face="黑体"  size=5>Objetos reader</font>**

Las principales personas a las que se aplica este documento (esta guía):

- Desarrolladores de software
- Personal de soporte técnico

**<font face="黑体"  size=5>Historial
 </font>**de revisiones <font face="宋体"  size=2>El historial de revisiones acumula una descripción de cada actualización del documento. La versión más reciente del documento contiene actualizaciones para todas las versiones anteriores. </font>

| El número de versión   | Modificado por     | Fecha de revisión | Notas de revisión |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | Grupos de software del sistema | 2022-03-09 | Lanzamiento del SDK V1.5 |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenido</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Análisis del marco

## 1.1 cliente、controlador 与 framework

&emsp; &emsp; El marco de buzones se utiliza para controlar la comunicación entre varios procesadores. El marco se divide en controlador y cliente.  
&emsp; &emsp; Controller es un controlador que manipula directamente el buzón de hardware. Opera los registros de hardware directamente hacia abajo, completando la comunicación con el control remoto mediante el envío y la recepción de interrupciones (si es compatible con el hardware); Hasta la interfaz proporcionada por el framework para completar la comunicación con el controlador cliente.
&emsp; &emsp; El cliente es el consumidor del controlador, comunicándose con el controlador hacia abajo, completando aplicaciones de canal, preparación de datos y otras funciones; Proporciona interfaces para la manipulación del espacio de usuario.  
&emsp; &emsp; El marco del buzón es responsable de la interfaz entre el controlador y el cliente, la documentación del kernel dice: "El controlador del cliente y el controlador del controlador pueden ser muy dependientes de la plataforma específica, por lo tanto, el controlador del cliente no se puede compartir entre múltiples plataformas", por lo que en`/drivers/mailbox` el directorio, solo se puede encontrar el controlador sobre el controlador del controlador y no se puede encontrar el controlador del cliente, solo se puede encontrar una prueba. El `mailbox-test.c`controlador cliente del controlador. La forma en que el controlador cliente intercambia datos con el espacio de usuario también depende del propio desarrollador del controlador.  
&emsp; &emsp; El siguiente diagrama es el marco básico para dos registros de conductores:

<div align=center>
<img src="../zh/images/mailbox/130101_frame_00.svg" width="1400">
</div>  

## 1.2 Estructuras de datos

&emsp; &emsp; La estructura de datos del controlador y el cliente se muestra en la siguiente figura:<div align=center>
<img src="../zh/images/mailbox/130102_data_structure.svg" width="1400">
</div>

&emsp; &emsp; El marco utiliza `struct mbox_controller`controladores de buzones abstractos, canales abstractos`struct mbox_chan` y colecciones de funciones `struct mbox_chan_ops`para manipular canales. Las tres estructuras de datos anteriores son para controladores. El marco utiliza `struct mbox_client`clientes abstractos, que son específicos del cliente.  
&emsp; &emsp; Además de esto, necesitamos definir nuestra propia estructura de dispositivos para nuestros dispositivos y unidades, como se muestra en la figura anterior. La conexión entre el cliente y el controlador se`mbox_request_channel` realiza en la función al solicitar un canal en el cliente, y un canal está enlazado a una`struct mbox_client` estructura.

## 1.3 Flujo de llamadas a funciones

&emsp; &emsp; El flujo de llamada a la función se muestra en la siguiente figura:<div align=center>
<img src="../zh/images/mailbox/130103_frame_callback.svg" width="1400">
</div>  

&emsp; &emsp; El espacio de usuario y la entrega de datos basada en el cliente utilizan ioctl más notificaciones asincrónicas, que son determinadas por los propios desarrolladores de controladores y no pertenecen al marco.  
&emsp; &emsp; Creamos un nodo de dispositivo en el controlador cliente`/dev/mailbox-client` a través del cual el espacio de usuario lee y envía datos. 8 canales de transmisión, 8 canales de recepción.

### 1.3.1 Flujo de datos de envío

&emsp; &emsp; Como se muestra en la figura anterior:

1. El archivo de manipulación del espacio de usuario maneja para enviar datos;
2. Introduzca la función ioctl controlada por el cliente, que copia los datos del espacio de usuario en el espacio del kernel y, finalmente, llama a la`mbox_send_message` función;
3. El proceso de procesamiento específico de esta función se puede ver en el análisis de código de los capítulos posteriores, que principalmente llama a dos funciones de devolución de llamada: implementación impulsada por el cliente`tx_prepare` e implementación impulsada por el controlador`send_data`. Mira los nombres para saber qué hacen estas dos funciones. Cabe señalar que algunos buzones de hardware tienen registros de transmisión de datos de hardware, por lo que en este momento, la transmisión de datos se puede`send_data` completar en el medio; Algunos hardware no tienen registros de transmisión de datos de hardware, entonces la transmisión de datos real también se puede`tx_prepare` completar en él, y `send_data`el rol se convierte en una simple **notificación de interrupción de disparo al procesador remoto**;
4. Cuando el procesador remoto recibe la interrupción y recibe los datos, debe responder al controlador con una interrupción que indique que Tx se ha completado;
5. Después de recibir el Tx ACK, se debe llamar al controlador de interrupciones registrado por el controlador `mbox_chan_txdone`para notificar a la capa superior que la transferencia se ha recibido de forma remota;
6. `mbox_chan_txdone`Informar al cliente que la `tx_done`transferencia se completa a través del registro del cliente. El cliente decide para el procesamiento posterior, y los`tx_done` parámetros registran el estado de la transferencia de datos.

### 1.3.1 Proceso de recepción de datos

&emsp; &emsp; Como se muestra en la figura anterior:

1. Interrupciones del procesador remoto que envía datos al controlador;
2. Después de recibir la interrupción, la llamada del controlador de interrupciones registrada por el controlador `mbox_chan_received_data`informa a la capa superior para que reciba los datos procedentes del extremo lejano y responda al Rx ACK remoto.
3. `mbox_chan_received_data`Invocar al cliente registrado`rx_callback`;
4. `rx_callback`lee los datos de la dirección especificada en el árbol de dispositivos y, a continuación, notifica al espacio de usuario mediante notificaciones asincrónicas;
5. El controlador asincrónico de espacio de usuario que llama a ioctl lee los datos del canal de recepción.

# 2 Análisis de código marco

## 2.1 mailbox_controller.h

&emsp; &emsp; Definido `mbox_controller`(abstracción del hardware del buzón),`mbox_chan` (abstracción del canal) `mbox_chan_ops`(colección de funciones de devolución de llamada que manipulan los canales).

```c
struct mbox_controller {
    /* 此 controller 对应的设备，在 probe 时赋值，dev = &pdev->dev */
    struct device *dev;                  
    const struct mbox_chan_ops *ops;    // 对 channel 进行操作的函数集合
    struct mbox_chan *chans;            // channel 的指针数组，channel 的集合
    int num_chans;                      // 支持的 channel 的个数
    /* 是否支持通过中断来检查 remote 消费了一条消息。
        * 例如：硬件上有一些 TX ACK irq（传输完成后收到中断回复表明传输完成了） */
    bool txdone_irq;                  
    /* 是否支持通过 poll 机制来检查 remote 消费了一条消息。
        * 此标志用于硬件没有 TX ACK irq 机制，但是可以通过查询相关寄存器的某些位
        * 来检查是否完成传输。如果设置了 txdone_irq，此标志位会被忽略 */  
    bool txdone_poll;                   
    unsigned txpoll_period;             // POLL 周期，以 ms 计
    /* controller 驱动中通过此函数返回设备树参数中设定的通道 */
    struct mbox_chan *(*of_xlate)(struct mbox_controller *mbox,
                        const struct of_phandle_args *sp);
    /* Internal to API */
    struct hrtimer poll_hrt;
    struct list_head node;
};

struct mbox_chan {
    struct mbox_controller *mbox;           // 此通道所属的 controller
    unsigned txdone_method;                 // 传输完成的通知方式，在 mailbox.h中定义
    /* 指向占有此 channel 的 client 的指针，client 在 client driver 中声明 */
    struct mbox_client *cl;                 
    struct completion tx_complete;          
    void *active_req;                       // 如果不为 NULL，说明还有数据在传输
    unsigned msg_count, msg_free;           // 在代码中会详细分析
    void *msg_data[MBOX_TX_QUEUE_LEN];
    spinlock_t lock; /* Serialise access to the channel */
    void *con_priv;                         // controller 的私有数据，我用作了channel number
};

/**
 * struct mbox_chan_ops - 控制 mailbox channels 的函数
 * @send_data: 此 API 在 MBOX 驱动中使用, 在原子上下文中尝试在总线上
 *      发送消息. 如果发送的消息被远端接受，则返回0；如果远端还没有读取
 *      上一次的数据，会被拒绝并返回 -EBUSY（这个 -EBUSY 怎么使用还没
 *      看懂）。如果有 TX ACK irq 的话，实际的数据传输完成的通知是由 MBOX 
 *      controller 通过 mbox_chan_txdone 来完成的（在中断中）。此函数
 *      禁止睡眠。
 *      实际上，如果硬件没有发送数据的寄存器，那此函数只进行开始传输数据
 *      的通知。例如触发 remote 的中断，告诉远端开始发送数据了。
 * @startup: Called when a client requests the chan. The controller
 *      could ask clients for additional parameters of communication
 *      to be provided via client's chan_data. This call may
 *      block. After this call the Controller must forward any
 *      data received on the chan by calling mbox_chan_received_data.
 *      The controller may do stuff that need to sleep.
 * @shutdown:  Called when a client relinquishes control of a chan.
 *      This call may block too. The controller must not forward
 *      any received data anymore.
 *      The controller may do stuff that need to sleep.
 * @last_tx_done: If the controller sets 'txdone_poll', the API calls
 *        this to poll status of last TX. The controller must
 *        give priority to IRQ method over polling and never
 *        set both txdone_poll and txdone_irq. Only in polling
 *        mode 'send_data' is expected to return -EBUSY.
 *        The controller may do stuff that need to sleep/block.
 *        Used only if txdone_poll:=true && txdone_irq:=false
 * @peek_data: Atomic check for any received data. Return true if controller
 *        has some data to push to the client. False otherwise.
 */
struct mbox_chan_ops {
    int (*send_data)(struct mbox_chan *chan, void *data);
    int (*startup)(struct mbox_chan *chan);
    void (*shutdown)(struct mbox_chan *chan);
    bool (*last_tx_done)(struct mbox_chan *chan);
    bool (*peek_data)(struct mbox_chan *chan);
};

/* 
 * client 要送的消息的 buffer 队列，此队列是循环缓冲区。
 * 'msg_count' 记录缓冲消息的数量；
 * 'msg_free' 是下一条将被缓存的消息的 index。
 * 此缓冲区长度不需要太大，因为每次传输都会触发中断，如果有大量数据需要传输，
 * 终端延迟将会成为瓶颈，而不是缓冲区长度。
 * 此外，mbox_send_message 可以在原子上下文中调用，并且 client 可以在它的
 * 回调函数 tx_done 中发送下一条要发送的数据（tx_done 是传输完成的通知函数）。
 */
#define MBOX_TX_QUEUE_LEN   20
```

## 2.2 mailbox_client.h

```c
/**
 * struct mbox_client - User of a mailbox
 * @dev:            此 client 对应的设备
 * @tx_block:       如果 mbox_send_message 在数据传输完之前应该是阻塞的，那么
 *                  设置为 true。
 * @tx_tout:        最大阻塞时间，如果超过此时间，认为传输失败。
 * @knows_txdone:   在可以知道 TX 状态的机器上使用. 如果已经有了 TX_Done/RTR 
 *                  中断，那就不需要此位，置为 false 即可。
 * @rx_callback:    Atomic callback to provide client the data received
 * @tx_prepare:     原子回调函数，在初始化开始传输的寄存器之前，在此函数中准备
 *                  要传输的数据。
 *                  实际上：如果硬件只负责通知消息已经开始传输（例如触发远端中
 *                  断），而没有实际的数据传输寄存器，那么在此函数中完成实际的
 *                  数据传输（从源地址拷贝到目的地址）。
 * @tx_done:        原子回调函数，通知 client 传输已经完成，可以在此函数中准备
 *                  下一次要发送的数据，见 MBOX_TX_QUEUE_LEN 的注释。
 */
struct mbox_client {
    struct device *dev;
    bool tx_block;
    unsigned long tx_tout;
    bool knows_txdone;

    void (*rx_callback)(struct mbox_client *cl, void *mssg);
    void (*tx_prepare)(struct mbox_client *cl, void *mssg);
    void (*tx_done)(struct mbox_client *cl, void *mssg, int r);
};
```

## 2.3 Mailbox.c

### 2.3.1 add_to_rbuf

```c
/* 
 * 缓存通道传输的消息。
 * 'msg_count' 记录缓冲消息的数量；
 * 'msg_free' 是下一条将被缓存的消息的 index。
 */
static int add_to_rbuf(struct mbox_chan *chan, void *mssg)
```

&emsp; &emsp; La lógica de la función es la siguiente:<div align=center>
<img src="../zh/images/mailbox/130203_add_to_rbuf.svg" width="500">
</div>

### 2.3.2msg_submit

```c
/* 判断存在有效数据以后，调用准备数据和发送数据的回调函数。*/
static void msg_submit(struct mbox_chan *chan)
{
    ......
    /* 
    * index -= count 是为了取出还未传输的最早缓存的 data
    * 缓存区是环形的，当 index < count 时，需要 + MBOX_TX_QUEUE_LEN - count。
    */
    count = chan->msg_count;
    idx = chan->msg_free;
    if (idx >= count)
        idx -= count;
    else
        idx += MBOX_TX_QUEUE_LEN - count;

    data = chan->msg_data[idx];

    ......
}
```

&emsp; &emsp; La lógica de la función es la siguiente:<div align=center>
<img src="../zh/images/mailbox/130203_msg_submit.svg" width="450">
</div>  

### 2.3.3 tx_tick

```c
/* 
 * 此函数的作用应该是更新状态，在 txdone 传输完成函数中调用，或者超时以后
 * 调用此函数。
 * 如果正确传输完成，complete(&chan->tx_complete) 结束此次传输。
 *
 * active_req 在此函数中清空。
 */
static void tx_tick(struct mbox_chan *chan, int r)
{
    ......

    /* 如果缓冲区还有消息，会继续发送下一条，如果没有，
        msg_submit 函数会直接返回 */
    msg_submit(chan);

    /* Notify the client */
    if (chan->cl->tx_done)
        chan->cl->tx_done(chan->cl, mssg, r);

    if (r != -ETIME && chan->cl->tx_block)
        complete(&chan->tx_complete);
}
```

### 2.3.4 mbox_chan_received_data

```c
/* 
 * 此函数的作用是在 controller 驱动接收到远端数据时，调用此函数来通知
 * 上层（client）接收到的数据。通知上层的方式是调用 client 中的回调函
 * 数 rx_callback。
 * @chan: RX chennel
 * @mssg: 数据指针，如果没有传输数据的寄存器，可以为空
 * 
 * 一般在 controller 驱动的中断处理函数中调用，在收到远端传输数据的中断
 * 后调用。
 */
void mbox_chan_received_data(struct mbox_chan *chan, void *mssg)
```

### 2.3.5 mbox_chan_txdone

```c
/* 
 * controller 驱动中通知框架数据传输完成的方式，在 controller 驱动的中
 * 断处理函数中调用，在接收到远端 ACK irq 以后调用。
 * 调用了 tx_tick 来完成状态更新。
 */
void mbox_chan_txdone(struct mbox_chan *chan, int r)
```

### 2.3.6 mbox_client_txdone

```c
/* 
 * 在 client 驱动中完成 tx 状态更新的方式
 * 此函数主要是为了不支持 ACK irq 的芯片服务的。例如，txdone_poll 的方式，
 * 芯片提供 tx 传输完成的标志位，此时，可以在 client 驱动中调用此函数完成
 * tx 状态更新。
 */
void mbox_client_txdone(struct mbox_chan *chan, int r)
```

### 2.3.7 mbox_send_message

```c
/* 
 * 为了 client 驱动准备的向 remote 传输数据的函数。
 * 如果在 client 中设置为 tx_block，此函数会在远端接收数据以后或者超时 
 * tx_out 以后返回。
 */
mbox_send_message(struct mbox_chan *chan, void *mssg)
```

&emsp; &emsp; La lógica de la función es la siguiente:<div align=center>
<img src="../zh/images/mailbox/130203_mbox_send_message.svg" width="700">
</div>  

### 2.3.8 mbox_request_channel

```c
/* 
 * cl：请求通道的 client，在 client 驱动中调用，当客户端驱动声明了一个
 *     struct mbox_client 变量，并为其各个成员赋值以后，调用此函数来
 *     绑定 client 和 chan。
 * index：设备树中的通道的索引，下面会分析。
 * 返回值：如果 client 申请 channel 成功，返回对应 channel 的指针。
 */
struct mbox_chan *mbox_request_channel(struct mbox_client *cl, int index)
{
    ......

    if (of_parse_phandle_with_args(dev->of_node, "mboxes",
                        "#mbox-cells", index, &spec)) {
        dev_dbg(dev, "%s: can't parse \"mboxes\" property\n", __func__);
        mutex_unlock(&con_mutex);
        return ERR_PTR(-ENODEV);
    }

    chan = ERR_PTR(-EPROBE_DEFER);
    list_for_each_entry(mbox, &mbox_cons, node)
        if (mbox->dev->of_node == spec.np) {
            chan = mbox->of_xlate(mbox, &spec);
            break;
        }

    ......

    chan->msg_free = 0;
    chan->msg_count = 0;
    chan->active_req = NULL;
    chan->cl = cl;
    init_completion(&chan->tx_complete);

    ......
}
```

&emsp; &emsp; Esta función, por cierto, `of_parse_phandle_with_args`obtiene el canal del índice solicitado del árbol de dispositivos.

- `mboxes`Apunta al nombre de la propiedad phandle list en el nodo;
- `#mbox-cells`Indica el número de celdas contenidas en el nodo señalado por el phandle;
- `index`Representa el índice de la lista de phandle, con 0 representando el primer phandle y 1 representando el segundo phandle;
- `out_args`Almacena parámetros en el phandle.

&emsp; &emsp; Por ejemplo, en nuestro árbol de dispositivos

```c
/* 
 * #mbox-cells 指明了 mboxes 属性只有一个 cell；
 * mboxes 是对应的通道的参数列表，我们将其用作了通道的索引
 * 此时，在 client 中调用上面申请通道的函数时，index = 1，就得到了
 * <&mailbox 1>，然后在 of_xlate 函数中进行处理并返回对应 channel 
 * 的指针。（of_xlate 函数是controller 驱动中注册的回调，可以参看
 * mbox_controller 结构体。）
 */
&mailbox {
    #mbox-cells = <1>;
};

&manage_subsys {
    mailbox_client: mailbox_client@0 {
        mboxes =    <&mailbox 0>, <&mailbox 1>, <&mailbox 2>, <&mailbox 3>,
                    ......
                    <&mailbox 12>, <&mailbox 13>, <&mailbox 14>, <&mailbox 15>;
        mbox-names = "tx_chan_0", "tx_chan_1", "tx_chan_2", "tx_chan_3", 
                    ......
                    "rx_chan_7";                    
};
```

&emsp; &emsp; Esto es seguido por la inicialización de la información del canal, incluida la puesta a cero del recuento de caché, el cl de chan y el enlace de cliente del cliente que solicita el canal, la inicialización del tx_complete, etc.  
&emsp; &emsp; La lógica de la función es la siguiente:<div align=center>
<img src="../zh/images/mailbox/130203_mbox_request_channel.svg" width="500">
</div>

### 2.3.9 mbox_request_channel_byname

&emsp; &emsp; Esta función obtiene la lista mboxes correspondiente del árbol de dispositivos según el atributo name(mbox-names) y, finalmente, llama a la función mbox_request_channel para solicitar un canal.

### 2.3.10 mbox_free_channel

&emsp; &emsp; La función de liberación de canal implementa una función de devolución de llamada que vaciará los miembros del canal especificado e implementará la función de devolución de llamada si es necesario configurar el registro de hardware correspondiente`shutdown`.

### 2.3.11 mbox_controller_register y mbox_controller_unregister

&emsp; &emsp; El nombre implica.

# 3 Análisis del árbol de dispositivos

&emsp; &emsp; Ejemplo:

```c
/* controller */
mailbox: mailbox@970e0000 {
    ......
    compatible          = ;
    ......
    #mbox-cells = <1>;
};

/* client */
&manage_subsys {
    mailbox_client: mailbox_client@0 {
        compatible = "mailbox-client";
        mboxes =    <&mailbox 0>, <&mailbox 1>, <&mailbox 2>, <&mailbox 3>,
                    ......
                    <&mailbox 12>, <&mailbox 13>, <&mailbox 14>, <&mailbox 15>;
        mbox-names = "tx_chan_0", "tx_chan_1", "tx_chan_2", "tx_chan_3", 
                    ...... 
                    "rx_chan_4", "rx_chan_5", "rx_chan_6", "rx_chan_7";                    
        reg =   <0x1 0x087ffe00 0x0 0x20>, /* cpu2dsp channel 0 */
                <0x1 0x087ffe20 0x0 0x20>, /* cpu2dsp channel 1 */
                ......
                <0x1 0x087fffc0 0x0 0x20>, /* dsp2cpu channel 6 */
                <0x1 0x087fffe0 0x0 0x20>; /* dsp2cpu channel 7 */
    };
};
```

## 3.1 controlador

&emsp; &emsp; Debe haber un atributo`#mbox-cells` con un valor de al menos 1. Indica el`mboxes` número de celdas para el atributo cliente.

## 3.2 cliente

&emsp; &emsp; Debe haber una propiedad `mboxes`que proporcione información al canal de unidad.  
&emsp; &emsp; Atributo opcional`mbox-names`, alias sí`mboxes`.  
&emsp; &emsp; Opcionalmente`reg`, el cliente de buzón se comunica con el mando a distancia mientras conserva una parte de cualquier memoria.  

## 3.3 Cómo usar la propiedad

&emsp; &emsp; `mbox-cells`Las`mboxes` `mbox-names`tres propiedades se utilizan al solicitar canales.

```c

/* mailbox.c */
struct of_phandle_args spec;

if (of_parse_phandle_with_args(dev->of_node, "mboxes",
                    "#mbox-cells", index, &spec)) {
    dev_dbg(dev, "%s: can't parse \"mboxes\" property\n", __func__);
    mutex_unlock(&con_mutex);
    return ERR_PTR(-ENODEV);
}

chan = ERR_PTR(-EPROBE_DEFER);
list_for_each_entry(mbox, &mbox_cons, node)
    if (mbox->dev->of_node == spec.np) {
        chan = mbox->of_xlate(mbox, &spec);
        break;
    }

/* controller driver */
static struct mbox_chan *canaan_mailbox_xlate(struct mbox_controller *controller,
                        const struct of_phandle_args *spec)
{
    unsigned int ch = spec->args[0];
    ......
    return &mbox->chan[ch];
}
```

&emsp; &emsp; Aquí lo usamos como el número de canal, o podemos agregar otra información específica del hardware, la explicación específica depende del desarrollador del controlador.

# 4 Implementación del controlador

- Configuración de DTS
&emsp; &emsp; Consulte el ejemplo del árbol de dispositivos anterior.
- controlador
&emsp;&emsp;referencia`/drivers/mailbox/canaan-mailbox.c`
- cliente
&emsp;&emsp;referencia`/drivers/mailbox/canaan_mbox_client.c`
- Programas de espacio de usuario
&emsp; &emsp; Referencia`k510_buildroot/package/mailbox_demo/src/mailbox_async.c` y`k510_buildroot/package/mailbox_demo/src/mailbox_poll.c`

# 5 Cómo usar la demo

## 5.1 Uso

1. Cargue el programa dsp bare metal
Vaya al directorio`/app/dsp_app_new` y ejecute el comando `./dsp_app mailbox_demo.bin`para cargar el programa bare metal en el dsp, como se muestra en la siguiente figura:  
![dsp_load](../zh/images/mailbox/130601_dsp_load.png)  
2. Ejecutar la aplicación de prueba de espacio de usuario de Linux
Ingrese el directorio`/app/mailbox_demo` y ejecute el comando`./mailbox_async`, como se muestra en la siguiente figura:  
![](../zh/images/mailbox/130602_mailbox_async.png)mailbox_demo  
Esta demostración utiliza notificaciones asincrónicas para recibir los datos enviados por el dsp.
3. En el directorio`/app/mailbox_demo`, ejecute el comando`./mailbox_poll`, como se muestra en la siguiente figura:  
![](../zh/images/mailbox/130602_mailbox_poll.png)mailbox_demo
Esta demostración utiliza el bloqueo de sondeo durante 500 ms para recibir los datos enviados por el dsp. Enviamos datos cada 4s y leemos los datos cada 2s, por lo que podemos ver que cada 2s, el éxito de lectura se escalona con el error de lectura y la lectura de bloqueo es exitosa.

## 5.2 Probar el código

&emsp; &emsp; El programa dsp bare metal se encuentra `k510_buildroot/package/k510_evb_test/src/test/mailbox_demo/main.c`en el medio, y el código de prueba de espacio de usuario se encuentra en`k510_buildroot/package/mailbox_demo/src/mailbox_async.c` y`k510_buildroot/package/mailbox_demo/src/mailbox_poll.c`.

# 6 Problemas conocidos

&emsp; &emsp; Ocasionalmente, el `./dsp_app mailbox_demo.bin`programa dsp no se graba en el dsp la primera vez que se ejecuta el comando. La ejecución de la demostración en este punto dará lugar a un error de envío.

**Descargo de responsabilidad de**traducción  
Para la comodidad de los clientes, Canaan utiliza un traductor de IA para traducir texto a varios idiomas, que pueden contener errores. No garantizamos la exactitud, fiabilidad o puntualidad de las traducciones proporcionadas. Canaan no será responsable de ninguna pérdida o daño causado por la confianza en la exactitud o fiabilidad de la información traducida. Si existe una diferencia de contenido entre las traducciones en diferentes idiomas, prevalecerá la versión en chino simplificado.

Si desea informar de un error o inexactitud de traducción, no dude en ponerse en contacto con nosotros por correo.
