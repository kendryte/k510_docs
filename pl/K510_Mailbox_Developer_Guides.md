![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 Mailbox — podręcznik programisty</font>**

<font face="黑体"  size=3>Wersja dokumentu: V1.0.0</font>

<font face="黑体"  size=3>Opublikowano: 2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Zrzeczenie się**</font>
Zakupione produkty, usługi lub funkcje podlegają umowom handlowym i warunkom Beijing Canaan Jiesi Information Technology Co., Ltd. ("Spółka", ta sama poniżej), a wszystkie lub część produktów, usług lub funkcji opisanych w niniejszym dokumencie może nie być objęta zakresem zakupu lub użytkowania. O ile nie uzgodniono inaczej w umowie, Firma zrzeka się wszelkich oświadczeń lub gwarancji, wyraźnych lub dorozumianych, co do dokładności, niezawodności, kompletności, marketingu, konkretnego celu i nieagresji jakichkolwiek oświadczeń, informacji lub treści tego dokumentu. O ile nie uzgodniono inaczej, niniejszy dokument jest dostarczany jako wskazówka wyłącznie do użytku.
Ze względu na aktualizacje wersji produktu lub z innych powodów zawartość tego dokumentu może być od czasu do czasu aktualizowana lub modyfikowana bez powiadomienia. 

**<font face="黑体"  size=3>Informacje o znakach towarowych</font>**

""<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, ikona "Canaan", Canaan i inne znaki towarowe Canaan oraz inne znaki towarowe Canaan są znakami towarowymi Beijing Canaan Jiesi Information Technology Co., Ltd. Wszystkie inne znaki towarowe lub zarejestrowane znaki towarowe, które mogą być wymienione w niniejszym dokumencie, są własnością ich odpowiednich właścicieli. 

**<font face="黑体"  size=3>Prawa autorskie ©2022 Beijing Canaan Jiesi Information Technology Co., Ltd</font>**
Niniejszy dokument ma zastosowanie wyłącznie do rozwoju i projektowania platformy K510, bez pisemnej zgody firmy, żadna jednostka ani osoba fizyczna nie może rozpowszechniać części lub całości treści tego dokumentu w jakiejkolwiek formie. 

**<font face="黑体"  size=3>Pekin Canaan Jiesi Information Technology Co Ltd</font>**
Adres internetowy: canaan-creative.com
Zapytania biznesowe: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# przedmowa
**<font face="黑体"  size=5>Przeznaczenie </font>**dokumentu
Ten dokument jest dokumentem rozwojowym sterownika skrzynki pocztowej K510. 

**<font face="黑体"  size=5>Obiekty programu Reader</font>**

Główne osoby, których dotyczy ten dokument (ten przewodnik):

- Programiści
- Personel wsparcia technicznego

**<font face="黑体"  size=5>Historia</font>**
 zmian <font face="宋体"  size=2>Historia zmian gromadzi opis każdej aktualizacji dokumentu. Najnowsza wersja dokumentu zawiera aktualizacje dla wszystkich poprzednich wersji. </font>

| Numer wersji   | Zmodyfikowane przez     | Data aktualizacji | Uwagi do poprawek |
|  :-----  |-------   |  ------  |  ------  |
| Wersja 1.0.0 | Grupy oprogramowania systemowego | 2022-03-09 | SDK V1.5 wydany |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Treść</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Analiza ram

## 1.1 client、controller 与 framework

&emsp; &emsp; Struktura skrzynki pocztowej służy do obsługi komunikacji między wieloma procesorami. Framework jest podzielony na kontroler i klienta.  
&emsp; &emsp; Kontroler to sterownik, który bezpośrednio manipuluje sprzętową skrzynką pocztową. Obsługuje rejestry sprzętowe bezpośrednio w dół, kończąc komunikację ze zdalnym poprzez wysyłanie i odbieranie przerwań (jeśli są obsługiwane przez sprzęt); Aż do interfejsu dostarczonego przez framework, aby zakończyć komunikację ze sterownikiem klienta.
&emsp; &emsp; Klient jest konsumentem administratora, komunikującym się z administratorem w dół, wypełniającym aplikacje kanałowe, przygotowującym dane i innymi funkcjami; Zapewnia interfejsy do manipulowania przestrzenią użytkownika.  
&emsp; &emsp; Struktura skrzynki pocztowej jest odpowiedzialna za interfejs między kontrolerem a klientem, dokumentacja jądra mówi: "Sterownik klienta i kontrolera może być bardzo zależny od konkretnej platformy, dlatego sterownik klienta nie może być współdzielony między wieloma platformami", więc w`/drivers/mailbox` katalogu można znaleźć tylko sterownik dotyczący kontrolera i nie można znaleźć sterownika klienta, można znaleźć tylko jeden test Sterownik `mailbox-test.c`klienta kontrolera. To, w jaki sposób sterownik klienta wymienia dane z przestrzenią użytkownika, zależy również od samego programisty sterownika.  
&emsp; &emsp; Poniższy diagram przedstawia podstawową strukturę dla dwóch rejestracji sterowników: 

<div align=center>
<img src="../zh/images/mailbox/130101_frame_00.svg" width="1400">
</div>  

## 1.2 Struktury danych

&emsp; &emsp; Strukturę danych administratora i klienta przedstawiono na poniższym rysunku:<div align=center>
<img src="../zh/images/mailbox/130102_data_structure.svg" width="1400">
</div>

&emsp; &emsp; Struktura wykorzystuje `struct mbox_controller`abstrakcyjne kontrolery skrzynek pocztowych, abstrakcyjne`struct mbox_chan` kanały i kolekcje funkcji `struct mbox_chan_ops`do manipulowania kanałami. Powyższe trzy struktury danych są przeznaczone dla kontrolerów. Struktura używa `struct mbox_client`abstrakcyjnych klientów, które są specyficzne dla klienta.  
&emsp; &emsp; Oprócz tego musimy zdefiniować własną strukturę urządzeń dla naszych urządzeń i dysków, jak pokazano na powyższym rysunku. Połączenie między klientem a kontrolerem odbywa`mbox_request_channel` się w funkcji podczas ubiegania się o kanał w kliencie, a jeden kanał jest powiązany ze strukturą`struct mbox_client`. 

## 1.3 Przepływ wywołań funkcji

&emsp; &emsp; Przepływ wywołań funkcji pokazano na poniższym rysunku:<div align=center>
<img src="../zh/images/mailbox/130103_frame_callback.svg" width="1400">
</div>  

&emsp; &emsp; Dostarczanie danych w przestrzeni użytkownika i na kliencie korzysta z ioctl plus powiadomienia asynchroniczne, które są określane przez samych programistów sterowników i nie należą do struktury.  
&emsp; &emsp; Stworzyliśmy węzeł urządzenia w sterowniku klienta`/dev/mailbox-client`, przez który przestrzeń użytkownika odczytuje i wysyła dane. 8 kanałów nadawczych, 8 kanałów odbiorczych. 

### 1.3.1 Wysyłanie przepływu danych

&emsp; &emsp; Jak pokazano na powyższym rysunku:

1. Uchwyty plików manipulacji przestrzenią użytkownika w celu wysyłania danych;
2. Wprowadź sterowaną przez klienta funkcję ioctl, która kopiuje dane przestrzeni użytkownika do przestrzeni jądra i ostatecznie wywołuje funkcję`mbox_send_message`; 
3. Specyficzny proces przetwarzania tej funkcji można zobaczyć w analizie kodu późniejszych rozdziałów, która wywołuje głównie dwie funkcje wywołania zwrotnego: implementację opartą na kliencie`tx_prepare` i implementację opartą na kontrolerze`send_data`. Spójrz na nazwy, aby dowiedzieć się, co robią te dwie funkcje. Należy zauważyć, że niektóre skrzynki pocztowe sprzętu mają sprzętowe rejestry transmisji danych, więc w tej chwili transmisja danych może zostać`send_data` zakończona w środku; Niektóre urządzenia nie mają rejestrów transmisji danych sprzętowych, a następnie można w nim również zakończyć rzeczywistą transmisję danych`tx_prepare`, a `send_data`rola staje się prostym powiadomieniem **o przerwaniu wyzwalacza dla zdalnego procesora**; 
4. Gdy zdalny procesor otrzyma przerwanie i otrzyma dane, musi odpowiedzieć kontrolerowi przerwaniem wskazującym, że Tx zostało zakończone;
5. Po otrzymaniu Tx ACK należy wywołać program obsługi przerwań zarejestrowany przez kontroler,`mbox_chan_txdone` aby powiadomić górną warstwę, że transfer został odebrany zdalnie; 
6. `mbox_chan_txdone`Poinformuj klienta, że `tx_done`przelew jest realizowany poprzez rejestrację klienta. Klient decyduje się na późniejsze przetwarzanie, a`tx_done` parametry rejestrują stan przesyłania danych. 

### 1.3.1 Proces otrzymywania danych

&emsp; &emsp; Jak pokazano na powyższym rysunku:

1. Przerwania zdalnego przetwarzania wysyłania danych do administratora;
2. Po odebraniu przerwania zarejestrowane przez kontroler wywołanie obsługi przerwań `mbox_chan_received_data`informuje górną warstwę, aby odebrała dane pochodzące z dalekiego końca i odpowiedziała na zdalny Rx ACK. 
3. `mbox_chan_received_data`Wywołaj zarejestrowanego klienta`rx_callback`; 
4. `rx_callback`odczytuje dane z adresu określonego w drzewie urządzeń, a następnie powiadamia przestrzeń użytkownika za pomocą powiadomień asynchronicznych;
5. Asynchroniczny program obsługi przestrzeni użytkownika, który wywołuje ioctl, odczytuje dane kanału odbiorczego.

# 2 Analiza kodu ramowego

## 2.1 mailbox_controller.h

&emsp; &emsp; Zdefiniowane `mbox_controller`(abstrakcja sprzętu skrzynki pocztowej),`mbox_chan` (abstrakcja kanału) `mbox_chan_ops`(zbiór funkcji wywołania zwrotnego, które manipulują kanałami). 

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

&emsp; &emsp; Logika funkcji jest następująca:<div align=center>
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

&emsp; &emsp; Logika funkcji jest następująca:<div align=center>
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

&emsp; &emsp; Logika funkcji jest następująca:<div align=center>
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

&emsp; &emsp; Ta funkcja w ten sposób `of_parse_phandle_with_args`uzyskuje kanał żądanego indeksu z drzewa urządzeń. 

- `mboxes`Wskazuje nazwę właściwości listy obsługi w węźle;
- `#mbox-cells`Wskazuje liczbę komórek zawartych w węźle wskazanym przez phandle;
- `index`Reprezentuje indeks listy rąk, przy czym 0 oznacza pierwszą phandle, a 1 reprezentuje drugą phandle;
- `out_args`Przechowuje parametry w phandle.

&emsp; &emsp; Na przykład w naszym drzewie urządzeń

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

&emsp; &emsp; Następnie następuje zainicjowanie informacji o kanale, w tym zerowanie liczby pamięci podręcznej, cl chan i powiązania klienta klienta żądającego kanału, zainicjowanie tx_complete i tak dalej.  
&emsp; &emsp; Logika funkcji jest następująca:<div align=center>
<img src="../zh/images/mailbox/130203_mbox_request_channel.svg" width="500">
</div>

### 2.3.9 mbox_request_channel_byname

&emsp; &emsp; Ta funkcja uzyskuje odpowiednią listę mboxów z drzewa urządzeń zgodnie z atrybutem name(mbox-names), a na koniec wywołuje funkcję mbox_request_channel, aby zastosować ją do kanału.

### 2.3.10 mbox_free_channel

&emsp; &emsp; Funkcja zwalniania kanału implementuje funkcję wywołania zwrotnego, która opróżni elementy członkowskie określonego kanału i zaimplementuje funkcję wywołania zwrotnego, jeśli trzeba skonfigurować odpowiedni rejestr sprzętu`shutdown`. 

### 2.3.11 mbox_controller_register i mbox_controller_unregister

&emsp; &emsp; Nazwa sugeruje.

# 3 Analiza drzewa urządzeń

&emsp; &emsp; Przykład:

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

## 3.1 kontroler

&emsp; &emsp; Musi istnieć atrybut `#mbox-cells`o wartości co najmniej 1. Wskazuje liczbę`mboxes` komórek atrybutu client. 

## 3.2 klient

&emsp; &emsp; Musi istnieć właściwość`mboxes`, która dostarcza informacje do kanału dysku.  
&emsp; &emsp; Atrybut opcjonalny`mbox-names`, `mboxes`alias yes.  
&emsp; &emsp; Opcjonalnie `reg`klient skrzynki pocztowej komunikuje się ze zdalnym, zachowując część dowolnej pamięci.  

## 3.3 Jak korzystać z właściwości

&emsp; &emsp; `mbox-cells`Te`mboxes` `mbox-names`trzy właściwości są używane podczas ubiegania się o kanały. 

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

&emsp; &emsp; Tutaj używamy go jako numeru kanału lub możemy dodać inne informacje specyficzne dla sprzętu, konkretne wyjaśnienie zależy od twórcy sterownika.

# 4 Implementacja sterownika

- Konfiguracja DTS
&emsp; &emsp; Zobacz przykład drzewa urządzeń powyżej.
- kontroler
&emsp;&emsp;odniesienie`/drivers/mailbox/canaan-mailbox.c`
- klient
&emsp;&emsp;odniesienie`/drivers/mailbox/canaan_mbox_client.c`
- Programy przestrzeni użytkownika
&emsp; &emsp; Odniesienie`k510_buildroot/package/mailbox_demo/src/mailbox_async.c` i`k510_buildroot/package/mailbox_demo/src/mailbox_poll.c`

# 5 Jak korzystać z wersji demonstracyjnej

## 5.1 Użytkowanie

1. Załaduj program dsp bare metal
Przejdź do katalogu`/app/dsp_app_new` i wykonaj polecenie, `./dsp_app mailbox_demo.bin`aby załadować program bare metal do dsp, jak pokazano na poniższym rysunku:  
![dsp_load](../zh/images/mailbox/130601_dsp_load.png)  
2. Uruchamianie aplikacji testowej przestrzeni użytkownika systemu Linux
Wprowadź katalog`/app/mailbox_demo` i wykonaj polecenie`./mailbox_async`, jak pokazano na poniższym rysunku:  
![](../zh/images/mailbox/130602_mailbox_async.png)mailbox_demo  
Ten pokaz wykorzystuje asynchroniczne powiadomienia do odbierania danych wysyłanych przez dsp. 
3. W katalogu `/app/mailbox_demo`wykonaj polecenie`./mailbox_poll`, jak pokazano na poniższym rysunku:  
![](../zh/images/mailbox/130602_mailbox_poll.png)mailbox_demo
Ta demonstracja wykorzystuje blokowanie ankiet dla 500ms do odbierania danych wysyłanych przez dsp. Wysyłamy dane co 4s i odczytujemy dane co 2s, dzięki czemu widzimy, że co 2s sukces odczytu jest rozłożony w czasie z niepowodzeniem odczytu, a odczyt blokujący jest udany. 

## 5.2 Testowanie Kodu

&emsp; &emsp; Program dsp bare metal znajduje się `k510_buildroot/package/k510_evb_test/src/test/mailbox_demo/main.c`pośrodku, a kod testowy przestrzeni użytkownika znajduje się w`k510_buildroot/package/mailbox_demo/src/mailbox_async.c` i`k510_buildroot/package/mailbox_demo/src/mailbox_poll.c`. 

# 6 Znane problemy

&emsp; &emsp; Czasami `./dsp_app mailbox_demo.bin`program dsp nie jest nagrywany do dsp przy pierwszym wykonaniu polecenia. Wykonanie wersji demonstracyjnej w tym momencie spowoduje niepowodzenie wysyłania. 

**Zrzeczenie się odpowiedzialności za **tłumaczenie  
Dla wygody klientów Canaan używa tłumacza AI do tłumaczenia tekstu na wiele języków, które mogą zawierać błędy. Nie gwarantujemy dokładności, rzetelności ani terminowości dostarczonych tłumaczeń. Canaan nie ponosi odpowiedzialności za jakiekolwiek straty lub szkody spowodowane poleganiem na dokładności lub wiarygodności przetłumaczonych informacji. W przypadku różnic w treści tłumaczeń w różnych językach, pierwszeństwo ma chińska wersja uproszczona. 

Jeśli chcesz zgłosić błąd lub niedokładność tłumaczenia, skontaktuj się z nami pocztą.