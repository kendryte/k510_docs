![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 Mailbox Handleiding voor ontwikkelaars</font>**

<font face="黑体"  size=3>Document versie: V1.0.0</font>

<font face="黑体"  size=3>Publicatiedatum: 2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Disclaimer**</font>
De producten, diensten of functies die u koopt, zijn onderworpen aan de commerciële contracten en voorwaarden van Beijing Canaan Jiesi Information Technology Co., Ltd. ("het Bedrijf", hierna hetzelfde), en alle of een deel van de producten, diensten of functies die in dit document worden beschreven, vallen mogelijk niet binnen het bereik van uw aankoop of gebruik. Tenzij anders overeengekomen in het contract, wijst het bedrijf alle verklaringen of garanties af, expliciet of impliciet, met betrekking tot de nauwkeurigheid, betrouwbaarheid, volledigheid, marketing, specifiek doel en niet-agressie van verklaringen, informatie of inhoud van dit document. Tenzij anders overeengekomen, wordt dit document uitsluitend verstrekt als leidraad voor gebruik.
Vanwege upgrades van de productversie of andere redenen kan de inhoud van dit document van tijd tot tijd zonder enige kennisgeving worden bijgewerkt of gewijzigd. 

**<font face="黑体"  size=3>Handelsmerkkennisgevingen</font>**

""<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, "Canaan" icoon, Kanaän en andere handelsmerken van Kanaän en andere handelsmerken van Kanaän zijn handelsmerken van Beijing Canaan Jiesi Information Technology Co., Ltd. Alle andere handelsmerken of geregistreerde handelsmerken die in dit document kunnen worden genoemd, zijn eigendom van hun respectieve eigenaars. 

**<font face="黑体"  size=3>Copyright ©2022 Beijing Canaan Jiesi Information Technology Co, Ltd</font>**
Dit document is alleen van toepassing op de ontwikkeling en het ontwerp van het K510-platform, zonder de schriftelijke toestemming van het bedrijf mag geen enkele eenheid of persoon een deel of de inhoud van dit document in welke vorm dan ook verspreiden. 

**<font face="黑体"  size=3>Beijing Canaan Jiesi Information Technology Co, Ltd</font>**
URL: canaan-creative.com
Zakelijke vragen: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# inleiding
**<font face="黑体"  size=5>Doel van het document</font>**
Dit document is een ontwikkelingsdocument voor de K510 mailbox driver. 

**<font face="黑体"  size=5>Reader Objecten</font>**

De belangrijkste personen op wie dit document (deze gids) van toepassing is:

- Softwareontwikkelaars
- Technisch ondersteunend personeel

**<font face="黑体"  size=5>Revisiegeschiedenis</font>**
 <font face="宋体"  size=2>De revisiegeschiedenis bevat een beschrijving van elke documentupdate. De nieuwste versie van het document bevat updates voor alle voorgaande versies. </font>

| Het versienummer   | Gewijzigd door     | Datum van herziening | Opmerkingen bij herziening |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | Systeemsoftwaregroepen | 2022-03-09 | SDK V1.5 vrijgegeven |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Inhoud</font>**

[INHOUDSOPGAVE]

<div style="page-break-after:always"></div>

# 1 Kaderanalyse

## 1.1 client、controller 与 framework

&emsp; &emsp; Het postvakframework wordt gebruikt om de communicatie tussen meerdere processors af te handelen. Het framework is onderverdeeld in controller en client.  
&emsp; &emsp; Controller is een stuurprogramma dat de hardwarepostbus rechtstreeks manipuleert. Het bedient de hardwareregisters direct naar beneden en voltooit de communicatie met de afstandsbediening door interrupts te verzenden en te ontvangen (indien ondersteund door de hardware); Tot aan de interface die door het framework wordt geleverd om de communicatie met de clientdriver te voltooien.
&emsp; &emsp; De klant is de consument van de controller, communiceert met de controller naar beneden, voltooit kanaaltoepassingen, gegevensvoorbereiding en andere functies; Biedt interfaces voor manipulatie van gebruikersruimte.  
&emsp; &emsp; Het mailboxframework is verantwoordelijk voor de interface tussen de controller en de client, de kerneldocumentatie zegt: "De client- en controllerdriver kunnen erg afhankelijk zijn van het specifieke platform, daarom kan het clientstuurprogramma niet worden gedeeld tussen meerdere platforms", dus in`/drivers/mailbox` de directory kan alleen het stuurprogramma over de controller worden gevonden en kan het clientstuurprogramma niet worden gevonden, er is slechts één test te vinden De `mailbox-test.c`clientdriver van de controller. Hoe de clientdriver gegevens uitwisselt met de gebruikersruimte is ook aan de driverontwikkelaar zelf.  
&emsp; &emsp; Het volgende diagram is het basiskader voor twee bestuurdersregistraties: 

<div align=center>
<img src="../zh/images/mailbox/130101_frame_00.svg" width="1400">
</div>  

## 1.2 Gegevensstructuren

&emsp; &emsp; De gegevensstructuur van verwerkingsverantwoordelijke en klant wordt weergegeven in de volgende afbeelding:<div align=center>
<img src="../zh/images/mailbox/130102_data_structure.svg" width="1400">
</div>

&emsp; &emsp; Het framework maakt gebruik`struct mbox_controller` van abstracte postvakcontrollers, abstracte`struct mbox_chan` kanalen en verzamelingen functies `struct mbox_chan_ops`om kanalen te manipuleren. De bovenstaande drie gegevensstructuren zijn voor verwerkingsverantwoordelijken. Het framework maakt gebruik `struct mbox_client`van abstracte clients, die klantspecifiek zijn.  
&emsp; &emsp; Daarnaast moeten we onze eigen apparaatstructuur voor onze apparaten en schijven definiëren, zoals weergegeven in de bovenstaande afbeelding. De verbinding tussen de client en de controller wordt`mbox_request_channel` gedaan in de functie bij het aanvragen van een kanaal in de client en één kanaal is gebonden aan een`struct mbox_client` struct. 

## 1.3 Functie call flow

&emsp; &emsp; De functieaanroepstroom wordt weergegeven in de volgende afbeelding:<div align=center>
<img src="../zh/images/mailbox/130103_frame_callback.svg" width="1400">
</div>  

&emsp; &emsp; Gebruikersruimte en clientgestuurde gegevenslevering maakt gebruik van ioctl plus asynchrone meldingen, die door de ontwikkelaars van stuurprogramma's zelf worden bepaald en niet tot het framework behoren.  
&emsp; &emsp; We hebben een apparaatknooppunt in het clientstuurprogramma gemaakt`/dev/mailbox-client` waarmee de gebruikersruimte gegevens leest en verzendt. 8 kanalen, 8 ontvangstkanalen. 

### 1.3.1 Gegevensstroom verzenden

&emsp; &emsp; Zoals te zien is in de bovenstaande figuur:

1. Gebruikersruimte manipulatie bestandshandgrepen om gegevens te verzenden;
2. Voer de clientgestuurde ioctl-functie in, die gebruikersruimtegegevens naar de kernelruimte kopieert en uiteindelijk de functie aanroept`mbox_send_message`; 
3. Het specifieke verwerkingsproces van deze functie is te zien in de code-analyse van de latere hoofdstukken, die voornamelijk twee callback-functies aanroept: clientgestuurde`tx_prepare` implementatie en controllergestuurde implementatie`send_data`. Kijk naar de namen om te weten wat deze twee functies doen. Opgemerkt moet worden dat sommige hardwarepostvakken hardwaregegevensoverdrachtsregisters hebben, dus op dit moment kan de gegevensoverdracht`send_data` in het midden worden voltooid; Sommige hardware heeft geen hardwaregegevensoverdrachtsregisters, dan kan de feitelijke gegevensoverdracht er ook in worden`tx_prepare` voltooid en `send_data`wordt de rol een eenvoudige **trigger interrupt-melding aan de externe processor**; 
4. Wanneer de externe processor de interrupt ontvangt en de gegevens ontvangt, moet deze de controller antwoorden met een interrupt die aangeeft dat Tx is voltooid;
5. Na ontvangst van de Tx ACK moet de controller-geregistreerde interrupt-handler worden aangeroepen `mbox_chan_txdone`om de bovenste laag te laten weten dat de overdracht op afstand is ontvangen; 
6. `mbox_chan_txdone`Informeer de klant dat de `tx_done`overdracht is voltooid via de klantregistratie. De klant beslist voor de daaropvolgende verwerking en de`tx_done` parameters registreren de status van de gegevensoverdracht. 

### 1.3.1 Proces van het ontvangen van gegevens

&emsp; &emsp; Zoals te zien is in de bovenstaande figuur:

1. Onderbrekingen van de externe processor die gegevens naar de controller verzendt;
2. Na ontvangst van de interrupt informeert de door de controller geregistreerde interrupt handler-oproep `mbox_chan_received_data`de bovenste laag om gegevens te ontvangen die van het uiteinde komen en te antwoorden op de externe Rx ACK. 
3. `mbox_chan_received_data`Beroep doen op de geregistreerde klant`rx_callback`; 
4. `rx_callback`leest gegevens van het adres dat is opgegeven in de apparaatstructuur en waarschuwt vervolgens de gebruikersruimte met behulp van asynchrone meldingen;
5. De asynchrone handler voor gebruikersruimte die ioctl aanroept, leest de gegevens van het ontvangstkanaal.

# 2 Framework code analyse

## 2.1 mailbox_controller.h

&emsp; &emsp; Gedefinieerd `mbox_controller`(abstractie van postvakhardware),`mbox_chan` (abstractie van kanaal) `mbox_chan_ops`(verzameling callbackfuncties die kanalen manipuleren). 

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

## 2,2 mailbox_client,h

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

## 2.3 mailbox.c

### 2.3.1 add_to_rbuf

```c
/* 
 * 缓存通道传输的消息。
 * 'msg_count' 记录缓冲消息的数量；
 * 'msg_free' 是下一条将被缓存的消息的 index。
 */
static int add_to_rbuf(struct mbox_chan *chan, void *mssg)
```

&emsp; &emsp; De functielogica is als volgt:<div align=center>
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

&emsp; &emsp; De functielogica is als volgt:<div align=center>
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

&emsp; &emsp; De functielogica is als volgt:<div align=center>
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

&emsp; &emsp; Deze functie verkrijgt trouwens `of_parse_phandle_with_args`het kanaal van de gevraagde index uit de apparaatstructuur. 

- `mboxes`Wijst naar de naam van de eigenschap phandle list in het knooppunt;
- `#mbox-cells`Geeft het aantal cellen aan in het knooppunt waarnaar de phandle wijst;
- `index`Vertegenwoordigt de index van de phandle-lijst, waarbij 0 de eerste phandle vertegenwoordigt en 1 de tweede phandle;
- `out_args`Slaat parameters op in de phandle.

&emsp; &emsp; Bijvoorbeeld in onze apparatenstructuur

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

&emsp; &emsp; Dit wordt gevolgd door de initialisatie van de kanaalinformatie, inclusief het op nul zetten van het aantal caches, de cl of chan en de clientbinding van de client die het kanaal aanvraagt, de initialisatie van de tx_complete, enzovoort.  
&emsp; &emsp; De functielogica is als volgt:<div align=center>
<img src="../zh/images/mailbox/130203_mbox_request_channel.svg" width="500">
</div>

### 2.3.9 mbox_request_channel_byname

&emsp; &emsp; Deze functie verkrijgt de bijbehorende mboxes-lijst uit de apparaatstructuur op basis van name (mbox-names attribuut) en roept ten slotte de mbox_request_channel functie aan om een kanaal aan te vragen.

### 2.3.10 mbox_free_channel

&emsp; &emsp; De kanaalreleasefunctie implementeert een callbackfunctie die de leden van het opgegeven kanaal leegmaakt en de callback-functie implementeert als het bijbehorende hardwareregister moet worden geconfigureerd`shutdown`. 

### 2.3.11 mbox_controller_register en mbox_controller_unregister

&emsp; &emsp; Naam impliceert.

# 3 Analyse van de apparaatstructuur

&emsp; &emsp; Voorbeeld:

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

## 3.1 verantwoordelijke

&emsp; &emsp; Er moet een attribuut zijn `#mbox-cells`met een waarde van ten minste 1. Het geeft het`mboxes` aantal cellen voor het kenmerk client aan. 

## 3.2 Klant

&emsp; &emsp; Er moet een eigenschap zijn `mboxes`die informatie verstrekt aan het aandrijfkanaal.  
&emsp; &emsp; Optioneel attribuut`mbox-names`, ja `mboxes`alias.  
&emsp; &emsp; Optioneel `reg`communiceert de postvakclient met de afstandsbediening terwijl een deel van het geheugen behouden blijft.  

## 3.3 Hoe de woning te gebruiken

&emsp; &emsp; `mbox-cells`De`mboxes` `mbox-names`drie eigenschappen worden gebruikt bij het aanvragen van kanalen. 

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

&emsp; &emsp; Hier gebruiken we het als het kanaalnummer, of we kunnen andere hardware-specifieke informatie toevoegen, de specifieke uitleg is aan de ontwikkelaar van het stuurprogramma.

# 4 Driver implementatie

- DTS configuratie
&emsp; &emsp; Zie het voorbeeld van de apparaatstructuur hierboven.
- controleur
&emsp;&emsp;referentie`/drivers/mailbox/canaan-mailbox.c`
- klant
&emsp;&emsp;referentie`/drivers/mailbox/canaan_mbox_client.c`
- Programma's voor gebruikersruimte
&emsp; &emsp; Referentie`k510_buildroot/package/mailbox_demo/src/mailbox_async.c` en`k510_buildroot/package/mailbox_demo/src/mailbox_poll.c`

# 5 Hoe demo te gebruiken

## 5.1 Gebruik

1. Laad het dsp bare metal programma
Ga naar de map`/app/dsp_app_new` en voer de opdracht uit `./dsp_app mailbox_demo.bin`om het bare metal-programma in de dsp te laden, zoals weergegeven in de volgende afbeelding:  
![dsp_load](../zh/images/mailbox/130601_dsp_load.png)  
2. De Linux userspace-testapp uitvoeren
Voer de map in`/app/mailbox_demo` en voer de opdracht uit`./mailbox_async`, zoals weergegeven in de volgende afbeelding:  
![](../zh/images/mailbox/130602_mailbox_async.png)mailbox_demo  
Deze demo maakt gebruik van asynchrone meldingen om gegevens te ontvangen die door de dsp zijn verzonden. 
3. Voer in de map`/app/mailbox_demo` de opdracht uit`./mailbox_poll`, zoals weergegeven in de volgende afbeelding:  
![](../zh/images/mailbox/130602_mailbox_poll.png)mailbox_demo
Deze demo maakt gebruik van poll-blokkering voor 500ms om gegevens te ontvangen die door de dsp zijn verzonden. We verzenden gegevens om de 4s en lezen de gegevens elke 2s, zodat we kunnen zien dat elke 2s, het leessucces wordt gespreid met de leesfout en het blokkeren van lezen succesvol is. 

## 5.2 De Code testen

&emsp; &emsp; Het dsp bare metal-programma bevindt zich `k510_buildroot/package/k510_evb_test/src/test/mailbox_demo/main.c`in het midden en de testcode voor gebruikersruimte bevindt zich in`k510_buildroot/package/mailbox_demo/src/mailbox_async.c` en`k510_buildroot/package/mailbox_demo/src/mailbox_poll.c`. 

# 6 Bekende problemen

&emsp; &emsp; Af en toe wordt het `./dsp_app mailbox_demo.bin`dsp-programma niet in de dsp gebrand wanneer de opdracht voor het eerst wordt uitgevoerd. Uitvoering van de demo op dit punt zal resulteren in een verzendfout. 

**Vertaling Disclaimer**  
Voor het gemak van klanten gebruikt Canaan een AI-vertaler om tekst in meerdere talen te vertalen, wat fouten kan bevatten. Wij garanderen niet de nauwkeurigheid, betrouwbaarheid of tijdigheid van de geleverde vertalingen. Canaan is niet aansprakelijk voor enig verlies of schade veroorzaakt door het vertrouwen op de nauwkeurigheid of betrouwbaarheid van de vertaalde informatie. Als er een inhoudelijk verschil is tussen de vertalingen in verschillende talen, prevaleert de vereenvoudigd Chinese versie. 

Als u een vertaalfout of onnauwkeurigheid wilt melden, neem dan gerust contact met ons op via e-mail.