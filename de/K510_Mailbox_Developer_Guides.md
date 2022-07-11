![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 Mailbox Entwicklerhandbuch</font>**

<font face="黑体"  size=3>Dokumentversion: V1.0.0</font>

<font face="黑体"  size=3>Veröffentlicht: 2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Verzichtserklärung**</font>
Die Produkte, Dienstleistungen oder Funktionen, die Sie erwerben, unterliegen den kommerziellen Verträgen und Bedingungen von Beijing Canaan Jiesi Information Technology Co., Ltd. ("das Unternehmen", dasselbe im Folgenden), und alle oder ein Teil der in diesem Dokument beschriebenen Produkte, Dienstleistungen oder Funktionen fallen möglicherweise nicht in den Rahmen Ihres Kaufs oder Ihrer Nutzung. Sofern im Vertrag nicht anders vereinbart, lehnt das Unternehmen alle ausdrücklichen oder stillschweigenden Zusicherungen oder Gewährleistungen hinsichtlich der Genauigkeit, Zuverlässigkeit, Vollständigkeit, des Marketings, des spezifischen Zwecks und der Nichtverletzung von Zusicherungen, Informationen oder Inhalten dieses Dokuments ab. Sofern nicht anders vereinbart, wird dieses Dokument nur als Leitfaden für die Verwendung zur Verfügung gestellt.
Aufgrund von Produktversions-Upgrades oder anderen Gründen kann der Inhalt dieses Dokuments von Zeit zu Zeit ohne vorherige Ankündigung aktualisiert oder geändert werden.

**<font face="黑体"  size=3>Markenhinweise</font>**

"", "Canaan"-Symbol, Canaan und andere Marken von Canaan und andere Marken von Canaan <img src="../zh/images/canaan-logo.png" style="zoom:33%;" />sind Marken von Beijing Canaan Jiesi Information Technology Co., Ltd. Alle anderen Marken oder eingetragenen Warenzeichen, die in diesem Dokument erwähnt werden können, sind Eigentum ihrer jeweiligen Inhaber.

**<font face="黑体"  size=3>Copyright ©2022 Peking Canaan Jiesi Information Technology Co., Ltd</font>**
Dieses Dokument gilt nur für die Entwicklung und das Design der K510-Plattform, ohne die schriftliche Genehmigung des Unternehmens darf keine Einheit oder Einzelperson einen Teil oder den gesamten Inhalt dieses Dokuments in irgendeiner Form verbreiten.

**<font face="黑体"  size=3>Peking Canaan Jiesi Informationstechnologie Co., Ltd</font>**
URL: canaan-creative.com
Geschäftliche Anfragen: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# Vorwort
**<font face="黑体"  size=5>Zweck des Dokuments</font>**
Dieses Dokument ist ein Entwicklungsdokument für den K510-Postfachtreiber.

**<font face="黑体"  size=5>Reader-Objekte</font>**

Die wichtigsten Personen, für die sich dieses Dokument (dieser Leitfaden) richtet:

- Softwareentwickler
- Mitarbeiter des technischen Supports

**<font face="黑体"  size=5>Revisionshistorie</font>**
 <font face="宋体"  size=2>In der Revisionshistorie wird eine Beschreibung jeder Dokumentaktualisierung gesammelt. Die neueste Version des Dokuments enthält Updates für alle vorherigen Versionen. </font>

| Die Versionsnummer   | Geändert von     | Datum der Überarbeitung | Revisionshinweise |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | Systemsoftwaregruppen | 2022-03-09 | SDK V1.5 veröffentlicht |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Inhalt</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Rahmenanalyse

## 1.1 client、controller 与 framework

&emsp; &emsp; Das Postfachframework wird verwendet, um die Kommunikation zwischen mehreren Prozessoren zu verwalten. Das Framework ist in Controller und Client unterteilt.  
&emsp; &emsp; Controller ist ein Treiber, der das Hardwarepostfach direkt manipuliert. Es betreibt die Hardware-Register direkt nach unten und schließt die Kommunikation mit der Fernbedienung durch Senden und Empfangen von Interrupts ab (sofern von der Hardware unterstützt); Bis zur Schnittstelle, die vom Framework bereitgestellt wird, um die Kommunikation mit dem Client-Treiber abzuschließen.
&emsp; &emsp; Der Kunde ist der Verbraucher des Controllers, der mit dem Controller nach unten kommuniziert und Kanalanwendungen, Datenaufbereitung und andere Funktionen ausführt; Bietet Schnittstellen für die Manipulation des Benutzerbereichs.  
&emsp; &emsp; Das Mailbox-Framework ist für die Schnittstelle zwischen dem Controller und dem Client verantwortlich, die Kernel-Dokumentation sagt: "Der Client und der Controller-Treiber können sehr von der spezifischen Plattform abhängig sein, daher kann der Client-Treiber nicht zwischen mehreren Plattformen gemeinsam genutzt werden", so dass im`/drivers/mailbox` Verzeichnis nur der Treiber über den Controller gefunden werden kann und der Client-Treiber nicht gefunden werden kann, nur ein Test kann gefunden werden Der `mailbox-test.c`Clienttreiber des Controllers. Wie der Clienttreiber Daten mit dem Benutzerraum austauscht, bleibt auch dem Treiberentwickler selbst überlassen.  
&emsp; &emsp; Das folgende Diagramm bildet das Grundgerüst für zwei Treiberregistrierungen:

<div align=center>
<img src="../zh/images/mailbox/130101_frame_00.svg" width="1400">
</div>  

## 1.2 Datenstrukturen

&emsp; &emsp; Die Datenstruktur von Controller und Client ist in der folgenden Abbildung dargestellt:<div align=center>
<img src="../zh/images/mailbox/130102_data_structure.svg" width="1400">
</div>

&emsp; &emsp; Das Framework verwendet`struct mbox_controller` abstrakte Postfachcontroller, abstrakte`struct mbox_chan` Kanäle und Auflistungen von Funktionen, `struct mbox_chan_ops`um Kanäle zu bearbeiten. Die oben genannten drei Datenstrukturen sind für Controller bestimmt. Das Framework verwendet `struct mbox_client`abstrakte Clients, die clientspezifisch sind.  
&emsp; &emsp; Darüber hinaus müssen wir unsere eigene Gerätestruktur für unsere Geräte und Laufwerke definieren, wie in der obigen Abbildung gezeigt. Die Verbindung zwischen dem`mbox_request_channel` Client und der Steuerung erfolgt in der Funktion bei der Beantragung eines Kanals im Client, und ein Kanal ist an eine Struktur gebunden`struct mbox_client`.

## 1.3 Ablauf von Funktionsaufrufen

&emsp; &emsp; Der Funktionsaufruffluss ist in der folgenden Abbildung dargestellt:<div align=center>
<img src="../zh/images/mailbox/130103_frame_callback.svg" width="1400">
</div>  

&emsp; &emsp; User-Space und clientgesteuerte Datenbereitstellung verwenden ioctl plus asynchrone Benachrichtigungen, die von den Treiberentwicklern selbst festgelegt werden und nicht zum Framework gehören.  
&emsp; &emsp; Wir haben einen Geräteknoten im Clienttreiber erstellt`/dev/mailbox-client`, über den der Benutzerbereich Daten liest und sendet. 8 Sendekanäle, 8 Empfangskanäle.

### 1.3.1 Senden von Datenfluss

&emsp; &emsp; Wie in der Abbildung oben gezeigt:

1. Dateihandles zur Manipulation des Benutzerbereichs zum Senden von Daten;
2. Geben Sie die clientgesteuerte ioctl-Funktion ein, die User-Space-Daten in den Kernel-Space kopiert und schließlich die Funktion aufruft`mbox_send_message`.
3. Der spezifische Verarbeitungsprozess dieser Funktion zeigt sich in der Codeanalyse der späteren Kapitel, die hauptsächlich zwei Callback-Funktionen aufruft: die clientgesteuerte`tx_prepare` Implementierung und die controllergesteuerte Implementierung.`send_data` Schauen Sie sich die Namen an, um zu wissen, was diese beiden Funktionen tun. Es sollte beachtet werden, dass einige Hardwarepostfächer Hardware-Datenübertragungsregister haben, so dass zu diesem Zeitpunkt die Datenübertragung`send_data` in der Mitte abgeschlossen werden kann; Einige Hardware verfügt nicht über Hardware-Datenübertragungsregister, dann kann die eigentliche Datenübertragung auch`tx_prepare` darin abgeschlossen werden, und `send_data`die Rolle wird zu einer einfachen **Trigger-Interrupt-Benachrichtigung an den Remoteprozessor**.
4. Wenn der Remote-Prozessor den Interrupt empfängt und die Daten empfängt, muss er dem Controller mit einem Interrupt antworten, der anzeigt, dass Tx abgeschlossen ist.
5. Nach dem Empfang des Tx ACK muss der Controller registrierte Interrupt-Handler aufgerufen werden, `mbox_chan_txdone`um die obere Schicht darüber zu informieren, dass die Übertragung remote empfangen wurde.
6. `mbox_chan_txdone`Informieren Sie den Kunden, dass die `tx_done`Übertragung durch die Kundenregistrierung abgeschlossen ist. Der Kunde entscheidet sich für die weitere Verarbeitung, und die`tx_done` Parameter erfassen den Status der Datenübertragung.

### 1.3.1 Prozess des Empfangens von Daten

&emsp; &emsp; Wie in der Abbildung oben gezeigt:

1. Interrupts des Remote-Prozessors, die Daten an die Steuerung senden;
2. Nach dem Empfang des Interrupts informiert der vom Controller registrierte Interrupt-Handler-Aufruf `mbox_chan_received_data`die obere Schicht, um Daten vom anderen Ende zu empfangen und an den entfernten Rx ACK zu antworten.
3. `mbox_chan_received_data`Rufen Sie den registrierten Client auf`rx_callback`.
4. `rx_callback`liest Daten von der in der Gerätestruktur angegebenen Adresse und benachrichtigt dann den Benutzerbereich mithilfe asynchroner Benachrichtigungen.
5. Der asynchrone Userspace-Handler, der ioctl aufruft, liest die Daten des Empfangskanals.

# 2 Framework-Code-Analyse

## 2,1 mailbox_controller.h

&emsp; &emsp; Definiert (`mbox_controller`Abstraktion der Postfachhardware),`mbox_chan` (Abstraktion des Kanals) (`mbox_chan_ops`Sammlung von Callback-Funktionen, die Kanäle manipulieren).

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

## 2,2 mailbox_client.h

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

&emsp; &emsp; Die Funktionslogik sieht wie folgt aus:<div align=center>
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

&emsp; &emsp; Die Funktionslogik sieht wie folgt aus:<div align=center>
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

&emsp; &emsp; Die Funktionslogik sieht wie folgt aus:<div align=center>
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

&emsp; &emsp; Diese Funktion `of_parse_phandle_with_args`ruft übrigens den Kanal des angeforderten Index aus dem Gerätebaum ab.

- `mboxes`Verweist auf den Eigenschaftsnamen der Griffliste im Knoten.
- `#mbox-cells`Gibt die Anzahl der Zellen an, die in dem Knoten enthalten sind, auf die der Knoten verweist;
- `index`Stellt den Index der Handleliste dar, wobei 0 für den ersten Handle und 1 für den zweiten Phandle steht.
- `out_args`Speichert Parameter im phandle.

&emsp; &emsp; Zum Beispiel in unserem Gerätebaum

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

&emsp; &emsp; Es folgt die Initialisierung der Kanalinformationen, einschließlich der Nullstellung der Cache-Anzahl, der cl von chan und der Clientbindung des Clients, der den Kanal anfordert, der Initialisierung des tx_complete und so weiter.  
&emsp; &emsp; Die Funktionslogik sieht wie folgt aus:<div align=center>
<img src="../zh/images/mailbox/130203_mbox_request_channel.svg" width="500">
</div>

### 2.3.9 mbox_request_channel_byname

&emsp; &emsp; Diese Funktion ruft die entsprechende mboxes-Liste aus dem Gerätebaum nach name(mbox-names Attribut) ab und ruft schließlich die mbox_request_channel-Funktion auf, um einen Kanal anzuwenden.

### 2.3.10 mbox_free_channel

&emsp; &emsp; Die Kanalfreigabefunktion implementiert eine Rückruffunktion, die die Mitglieder des angegebenen Kanals leert und die Rückruffunktion implementiert, wenn das entsprechende Hardwareregister konfiguriert werden muss`shutdown`.

### 2.3.11 mbox_controller_register und mbox_controller_unregister

&emsp; &emsp; Name impliziert.

# 3 Gerätebaumanalyse

&emsp; &emsp; Beispiel:

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

## 3.1 Verantwortlicher

&emsp; &emsp; Es muss ein Attribut `#mbox-cells`mit einem Wert von mindestens 1 vorhanden sein. Es gibt die`mboxes` Anzahl der Zellen für das Clientattribut an.

## 3.2 Kunde

&emsp; &emsp; Es muss eine Eigenschaft vorhanden sein`mboxes`, die Informationen für den Laufwerkkanal bereitstellt.  
&emsp; &emsp; Optionales Attribut`mbox-names`, ja Alias`mboxes`.  
&emsp; &emsp; Optional `reg`kommuniziert der Postfachclient mit dem Remoteclient, während er einen Teil des Arbeitsspeichers beibehält.  

## 3.3 Nutzung der Immobilie

&emsp; &emsp; `mbox-cells`Die`mboxes` `mbox-names`drei Eigenschaften werden bei der Anwendung von Kanälen verwendet.

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

&emsp; &emsp; Hier verwenden wir es als Kanalnummer, oder wir können andere hardwarespezifische Informationen hinzufügen, die spezifische Erklärung liegt beim Treiberentwickler.

# 4 Treiber-Implementierung

- DTS-Konfiguration
&emsp; &emsp; Siehe das Beispiel für den Gerätebaum oben.
- Controller
&emsp;&emsp;Referenz`/drivers/mailbox/canaan-mailbox.c`
- Kunde
&emsp;&emsp;Referenz`/drivers/mailbox/canaan_mbox_client.c`
- User-Space-Programme
&emsp; &emsp; Referenz`k510_buildroot/package/mailbox_demo/src/mailbox_async.c` und`k510_buildroot/package/mailbox_demo/src/mailbox_poll.c`

# 5 Wie benutzt man die Demo?

## 5.1 Nutzung

1. Laden des dsp-Bare-Metal-Programms
Gehen Sie in das Verzeichnis `/app/dsp_app_new`und führen Sie den Befehl aus`./dsp_app mailbox_demo.bin`, um das Bare-Metal-Programm in den DSP zu laden, wie in der folgenden Abbildung dargestellt:  
![dsp_load](../zh/images/mailbox/130601_dsp_load.png)  
2. Ausführen der Linux-Userspace-Test-App
Geben Sie das Verzeichnis ein`/app/mailbox_demo`, und führen Sie den Befehl aus`./mailbox_async`, wie in der folgenden Abbildung dargestellt:  
![](../zh/images/mailbox/130602_mailbox_async.png)mailbox_demo  
Diese Demo verwendet asynchrone Benachrichtigungen, um Daten zu empfangen, die vom DSP gesendet werden.
3. Führen Sie im Verzeichnis`/app/mailbox_demo` den Befehl aus`./mailbox_poll`, wie in der folgenden Abbildung dargestellt:  
![](../zh/images/mailbox/130602_mailbox_poll.png)mailbox_demo
Diese Demo verwendet die Polling-Blockierung für 500ms, um Daten zu empfangen, die vom DSP gesendet werden. Wir senden Daten alle 4s und lesen die Daten alle 2s, so dass wir sehen können, dass alle 2s der Leseerfolg mit dem Lesefehler gestaffelt wird und der blockierende Lesevorgang erfolgreich ist.

## 5.2 Testen des Codes

&emsp; &emsp; Das dsp-Bare-Metal-Programm befindet sich `k510_buildroot/package/k510_evb_test/src/test/mailbox_demo/main.c`in der Mitte, und der User-Space-Testcode befindet sich in und`k510_buildroot/package/mailbox_demo/src/mailbox_async.c``k510_buildroot/package/mailbox_demo/src/mailbox_poll.c`.

# 6 Bekannte Probleme

&emsp; &emsp; Gelegentlich wird das `./dsp_app mailbox_demo.bin`dsp-Programm nicht in den dsp gebrannt, wenn der Befehl zum ersten Mal ausgeführt wird. Die Ausführung der Demo an dieser Stelle führt zu einem Sendefehler.

**Haftungsausschluss**für Übersetzungen  
Für die Bequemlichkeit der Kunden verwendet Canaan einen KI-Übersetzer, um Text in mehrere Sprachen zu übersetzen, die Fehler enthalten können. Wir übernehmen keine Gewähr für die Genauigkeit, Zuverlässigkeit oder Aktualität der bereitgestellten Übersetzungen. Canaan haftet nicht für Verluste oder Schäden, die durch das Vertrauen auf die Richtigkeit oder Zuverlässigkeit der übersetzten Informationen verursacht werden. Wenn es einen inhaltlichen Unterschied zwischen den Übersetzungen in verschiedenen Sprachen gibt, ist die vereinfachte chinesische Version maßgebend.

Wenn Sie einen Übersetzungsfehler oder eine Ungenauigkeit melden möchten, können Sie uns gerne per E-Mail kontaktieren.
