![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">Руководство разработчика почтовых ящиков K510</font>**

<font face="黑体"  size=3>Версия документа: V1.0.0</font>

<font face="黑体"  size=3>Опубликовано: 2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Отказ**</font>
Продукты, услуги или функции, которые вы покупаете, регулируются коммерческими контрактами и условиями Beijing Canaan Jiesi Information Technology Co., Ltd. («Компания», то же самое далее), и все или часть продуктов, услуг или функций, описанных в этом документе, могут не входить в сферу вашей покупки или использования. Если иное не оговорено в договоре, Компания отказывается от всех заявлений или гарантий, явных или подразумеваемых, в отношении точности, надежности, полноты, маркетинга, конкретной цели и ненападения любых заявлений, информации или содержания этого документа. Если не согласовано иное, настоящий документ предоставляется только в качестве руководства для использования.
В связи с обновлением версии продукта или по другим причинам содержимое этого документа может время от времени обновляться или изменяться без какого-либо уведомления.

**<font face="黑体"  size=3>Уведомления о товарных знаках</font>**

""<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, значок "Canaan", Canaan и другие товарные знаки Canaan и другие товарные знаки Canaan являются товарными знаками Beijing Canaan Jiesi Information Technology Co., Ltd. Все другие товарные знаки или зарегистрированные товарные знаки, которые могут быть упомянуты в этом документе, принадлежат их соответствующим владельцам.

**<font face="黑体"  size=3>Copyright ©2022 Пекин Ханаан Цзеси Информационные технологии Co., Ltd</font>**
Настоящий документ применим только к разработке и проектированию платформы K510, без письменного разрешения компании, ни одно подразделение или частное лицо не может распространять часть или все содержание этого документа в любой форме.

**<font face="黑体"  size=3>Пекин Ханаан Цзеси Информационные Технологии Co., Ltd</font>**
URL: canaan-creative.com
Бизнес-запросы: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# предисловие
**<font face="黑体"  size=5>Назначение </font>**документа
Этот документ является документом по разработке драйвера почтового ящика K510.

**<font face="黑体"  size=5>Объекты чтения</font>**

Основные люди, к которым относится этот документ (это руководство):

- Разработчики программного обеспечения
- Персонал технической поддержки

**<font face="黑体"  size=5>История изменений</font>**
 <font face="宋体"  size=2>Журнал изменений накапливает описание каждого обновления документа. Последняя версия документа содержит обновления для всех предыдущих версий. </font>

| Номер версии   | Изменено     | Дата пересмотра | Примечания к пересмотру |
|  :-----  |-------   |  ------  |  ------  |
| Версия 1.0.0 | Группы системного программного обеспечения | 2022-03-09 | Выпущен пакет SDK версии 1.5 |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Содержание</font>**

[ОГЛАВЛЕНИЯ]

<div style="page-break-after:always"></div>

# 1 Анализ фреймворка

## 1.1 client、controller 与 framework

&emsp; &emsp; Платформа почтовых ящиков используется для обработки обмена данными между несколькими процессорами. Фреймворк делится на контроллер и клиент.  
&emsp; &emsp; Контроллер — это драйвер, который непосредственно управляет аппаратным почтовым ящиком. Он управляет аппаратными регистрами непосредственно вниз, завершая связь с удаленным путем отправки и приема прерываний (если поддерживается оборудованием); Вплоть до интерфейса, предоставляемого фреймворком для завершения связи с клиентским драйвером.
&emsp; &emsp; Клиент является потребителем контроллера, общаясь с контроллером вниз, выполняя приложения канала, подготовку данных и другие функции; Предоставляет интерфейсы для манипулирования пользовательским пространством.  
&emsp; &emsp; За интерфейс между контроллером и клиентом отвечает инфраструктура почтовых ящиков, в документации по ядру написано: «Драйвер клиента и контроллера может сильно зависеть от конкретной платформы, поэтому драйвер клиента не может быть разделен между несколькими платформами», поэтому в`/drivers/mailbox` каталоге можно найти только драйвер о контроллере и не удается найти драйвер клиента, можно найти только один тест Клиентский `mailbox-test.c`драйвер контроллера. То, как клиентский драйвер обменивается данными с пользовательским пространством, также зависит от самого разработчика драйвера.  
&emsp; &emsp; Следующая схема является базовой структурой для двух регистраций драйверов:

<div align=center>
<img src="../zh/images/mailbox/130101_frame_00.svg" width="1400">
</div>  

## 1.2 Структуры данных

&emsp; &emsp; Структура данных контроллера и клиента показана на следующем рисунке:<div align=center>
<img src="../zh/images/mailbox/130102_data_structure.svg" width="1400">
</div>

&emsp; &emsp; Платформа использует `struct mbox_controller`абстрактные контроллеры почтовых ящиков, абстрактные`struct mbox_chan` каналы и наборы функций `struct mbox_chan_ops`для управления каналами. Вышеуказанные три структуры данных предназначены для контроллеров. Фреймворк использует `struct mbox_client`абстрактные клиенты, которые специфичны для клиента.  
&emsp; &emsp; В дополнение к этому, нам нужно определить нашу собственную структуру устройств для наших устройств и дисков, как показано на рисунке выше. Соединение между клиентом и контроллером осуществляется`mbox_request_channel` в функции при подаче заявки на канал в клиенте, и один канал привязан к структуре`struct mbox_client`.

## 1.3 Поток вызовов функций

&emsp; &emsp; Поток вызова функции показан на следующем рисунке:<div align=center>
<img src="../zh/images/mailbox/130103_frame_callback.svg" width="1400">
</div>  

&emsp; &emsp; Пользовательское пространство и клиентская доставка данных использует ioctl плюс асинхронные уведомления, которые определяются самими разработчиками драйверов и не относятся к фреймворку.  
&emsp; &emsp; Мы создали узел устройства в драйвере клиента`/dev/mailbox-client`, через который пользовательское пространство считывает и отправляет данные. 8 каналов передачи, 8 приемных каналов.

### 1.3.1 Отправка потока данных

&emsp; &emsp; Как показано на рисунке выше:

1. Дескрипторы файлов манипулирования пользовательским пространством для отправки данных;
2. Введите управляемую клиентом функцию ioctl, которая копирует данные пользовательского пространства в пространство ядра и в конечном итоге вызывает`mbox_send_message` функцию;
3. Специфический процесс обработки этой функции можно увидеть в анализе кода более поздних глав, который в основном вызывает две функции обратного вызова: клиент-управляемую`tx_prepare` реализацию и реализацию, управляемую контроллером`send_data`. Посмотрите на имена, чтобы узнать, что делают эти две функции. Следует отметить, что некоторые аппаратные почтовые ящики имеют аппаратные регистры передачи данных, поэтому в это время передача данных может быть`send_data` завершена посередине; Некоторые аппаратные средства не имеют аппаратных регистров передачи данных, тогда в нем также может быть завершена фактическая передача данных`tx_prepare`, а `send_data`роль становится простым триггером **прерывания уведомления удаленного процессора**;
4. Когда удаленный процессор получает прерывание и получает данные, он должен ответить контроллеру прерыванием, указывающим, что Tx завершен;
5. После получения Tx ACK необходимо вызвать зарегистрированный контроллером обработчик прерываний,`mbox_chan_txdone` чтобы уведомить верхний слой о том, что передача была получена удаленно;
6. `mbox_chan_txdone`Сообщите клиенту, что `tx_done`перевод завершен через регистрацию клиента. Клиент принимает решение о последующей обработке, а`tx_done` параметры фиксируют состояние передачи данных.

### 1.3.1 Процесс получения данных

&emsp; &emsp; Как показано на рисунке выше:

1. Прерывания удаленного процессора, отправляющего данные на контроллер;
2. После получения прерывания зарегистрированный контроллером вызов обработчика прерываний `mbox_chan_received_data`информирует верхний уровень о получении данных, поступающих с дальнего конца, и ответе на удаленный Rx ACK.
3. `mbox_chan_received_data`Вызовите зарегистрированного клиента`rx_callback`;
4. `rx_callback`считывает данные с адреса, указанного в дереве устройств, а затем уведомляет пространство пользователя с помощью асинхронных уведомлений;
5. Асинхронный обработчик пользовательского пространства, вызывающий ioctl, считывает данные канала приема.

# 2 Анализ кода фреймворка

## 2.1 mailbox_controller.ч

&emsp; &emsp; Определено `mbox_controller`(абстракция аппаратного обеспечения почтового ящика),`mbox_chan` (абстракция канала) `mbox_chan_ops`(коллекция функций обратного вызова, которые манипулируют каналами).

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

## 2.2 mailbox_client.ч

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

## 2.3 почтовый ящик.c

### 2.3.1 add_to_rbuf

```c
/* 
 * 缓存通道传输的消息。
 * 'msg_count' 记录缓冲消息的数量；
 * 'msg_free' 是下一条将被缓存的消息的 index。
 */
static int add_to_rbuf(struct mbox_chan *chan, void *mssg)
```

&emsp; &emsp; Логика функции выглядит следующим образом:<div align=center>
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

&emsp; &emsp; Логика функции выглядит следующим образом:<div align=center>
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

&emsp; &emsp; Логика функции выглядит следующим образом:<div align=center>
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

&emsp; &emsp; Эта функция, кстати, `of_parse_phandle_with_args`получает канал запрошенного индекса из дерева устройств.

- `mboxes`Указывает на имя свойства списка phandle в узле;
- `#mbox-cells`Указывает количество ячеек, содержащихся в узле, на который указывает ручка;
- `index`Представляет индекс списка phandle, где 0 представляет первую ручку, а 1 представляет вторую ручку;
- `out_args`Сохраняет параметры в панели.

&emsp; &emsp; Например, в нашем дереве устройств

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

&emsp; &emsp; За этим следует инициализация информации о канале, включая обнуление количества кэша, cl chan и привязки клиента, запрашивающего канал, инициализацию tx_complete и так далее.  
&emsp; &emsp; Логика функции выглядит следующим образом:<div align=center>
<img src="../zh/images/mailbox/130203_mbox_request_channel.svg" width="500">
</div>

### 2.3.9 mbox_request_channel_byname

&emsp; &emsp; Эта функция получает соответствующий список mboxes из дерева устройств в соответствии с атрибутом name(mbox-names) и, наконец, вызывает функцию mbox_request_channel для применения к каналу.

### 2.3.10 mbox_free_channel

&emsp; &emsp; Функция освобождения канала реализует функцию обратного вызова, которая будет очищать члены указанного канала и реализовывать функцию обратного вызова, если необходимо настроить соответствующий аппаратный регистр`shutdown`.

### 2.3.11 mbox_controller_register и mbox_controller_unregister

&emsp; &emsp; Названия.

# 3 Анализ дерева устройств

&emsp; &emsp; Пример:

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

## 3.1 контроллер

&emsp; &emsp; Должен быть атрибут`#mbox-cells` со значением не менее 1. Он указывает`mboxes` количество ячеек для атрибута client.

## 3.2 клиент

&emsp; &emsp; Должно быть свойство`mboxes`, предоставляющее информацию каналу диска.  
&emsp; &emsp; Необязательный атрибут`mbox-names`, да `mboxes`псевдоним.  
&emsp; &emsp; При `reg`необходимости клиент почтового ящика взаимодействует с удаленным пользователем, сохраняя при этом часть любой памяти.  

## 3.3 Как пользоваться недвижимостью

&emsp; &emsp; `mbox-cells`Эти`mboxes` `mbox-names`три свойства используются при подаче заявки на каналы.

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

&emsp; &emsp; Здесь мы используем его в качестве номера канала, или мы можем добавить другую информацию, специфичную для оборудования, конкретное объяснение зависит от разработчика драйвера.

# 4 Реализация драйвера

- Конфигурация служб DTS
&emsp; &emsp; См. пример дерева устройств выше.
- контроллер
&emsp;&emsp;ссылка`/drivers/mailbox/canaan-mailbox.c`
- клиент
&emsp;&emsp;ссылка`/drivers/mailbox/canaan_mbox_client.c`
- Программы пользовательского пространства
&emsp; &emsp; Справка`k510_buildroot/package/mailbox_demo/src/mailbox_async.c` и`k510_buildroot/package/mailbox_demo/src/mailbox_poll.c`

# 5 Как использовать демо

## 5.1 Использование

1. Загрузка программы DSP без операционной системы
Перейдите в каталог`/app/dsp_app_new` и выполните команду`./dsp_app mailbox_demo.bin`, чтобы загрузить программу без операционной системы в dsp, как показано на следующем рисунке:  
![dsp_load](../zh/images/mailbox/130601_dsp_load.png)  
2. Запуск тестового приложения пользовательского пространства Linux
Введите каталог`/app/mailbox_demo` и выполните команду`./mailbox_async`, как показано на следующем рисунке:  
![](../zh/images/mailbox/130602_mailbox_async.png)mailbox_demo  
Эта демонстрация использует асинхронные уведомления для получения данных, отправляемых dsp.
3. В каталоге `/app/mailbox_demo`выполните команду`./mailbox_poll`, как показано на следующем рисунке:  
![](../zh/images/mailbox/130602_mailbox_poll.png)mailbox_demo
Эта демонстрация использует блокировку опроса в течение 500 мс для получения данных, отправленных dsp. Мы отправляем данные каждые 4 секунды и считываем данные каждые 2 секунды, поэтому мы можем видеть, что каждые 2 секунды успешное чтение происходит в шахматном порядке с ошибкой чтения, а блокировка чтения успешна.

## 5.2 Тестирование кода

&emsp; &emsp; Программа dsp bare metal расположена `k510_buildroot/package/k510_evb_test/src/test/mailbox_demo/main.c`посередине, а тестовый код пользовательского пространства расположен в`k510_buildroot/package/mailbox_demo/src/mailbox_async.c` и`k510_buildroot/package/mailbox_demo/src/mailbox_poll.c`.

# 6 Известные проблемы

&emsp; &emsp; Иногда `./dsp_app mailbox_demo.bin`программа dsp не записывается в dsp при первом выполнении команды. Выполнение демонстрации на этом этапе приведет к сбою отправки.

**Отказ от ответственности за**перевод  
Для удобства клиентов Canaan использует переводчик AI для перевода текста на несколько языков, которые могут содержать ошибки. Мы не гарантируем точность, надежность или своевременность предоставленных переводов. Компания Canaan не несет ответственности за любые убытки или ущерб, вызванные доверием к точности или надежности переведенной информации. При наличии разницы в содержании переводов на разные языки преимущественную силу имеет упрощенная версия на китайском языке.

Если вы хотите сообщить об ошибке или неточности перевода, пожалуйста, не стесняйтесь обращаться к нам по почте.
