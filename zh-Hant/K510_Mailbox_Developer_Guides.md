![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 郵箱開發人員指南</font>**

<font face="黑体"  size=3>文件版本：V1.0.0</font>

<font face="黑体"  size=3>發佈日期：2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**免責聲明**</font>
您購買的產品、服務或特性等應受北京嘉楠捷思資訊技術有限公司（“本公司”，下同）商業合同和條款的約束，本文檔中描述的全部或部分產品、服務或特性可能不在您的購買或使用範圍之內。 除非合同另有約定，本公司不對本文檔的任何陳述、資訊、內容的準確性、可靠性、完整性、行銷型、特定目的性和非侵略性提供任何明示或默示的聲明或保證。 除非另有約定，本文檔僅作為使用指導的參考。
由於產品版本升級或其他原因，本文檔內容將可能在未經任何通知的情況下，不定期進行更新或修改。

**<font face="黑体"  size=3>商標聲明</font>**

“<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />”、“Canaan”圖示、嘉楠和嘉楠其他商標均為北京嘉楠捷思資訊技術有限公司的商標。 本文檔可能提及的其他所有商標或註冊商標，由各自的所有人擁有。

**<font face="黑体"  size=3>版權所有©2022北京嘉楠捷思資訊技術有限公司</font>**
本文檔僅適用K510平台開發設計，非經本公司書面許可，任何單位和個人不得以任何形式對本文檔的部分或全部內容傳播。

**<font face="黑体"  size=3>北京嘉楠捷思資訊技術有限公司</font>**
網址：canaan-creative.com
商務垂詢：salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# 前言
**<font face="黑体"  size=5>文件目的</font>**
本文檔為K510 mailbox 驅動開發文檔。

**<font face="黑体"  size=5>讀者物件</font>**

本文檔（本指南）主要適用的人員：

- 軟體開發人員
- 技術支持人員

**<font face="黑体"  size=5>修訂記錄</font>**
 <font face="宋体"  size=2>修訂記錄累積了每次文檔更新的說明。 最新版本的文件包含以前所有版本的更新內容。 </font>

| 版本號   | 修改者     | 修訂日期 | 修訂說明 |
|  :-----  |-------   |  ------  |  ------  |
| 1.0.0 版 | 系統軟體組 | 2022-03-09 | SDK V1.5發佈 |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>目 錄</font>**

[目錄]

<div style="page-break-after:always"></div>

# 1 框架分析

## 1.1 用戶端、控制器與框架

&emsp; &emsp; mailbox 框架用於處理多處理器之間的通信。 框架分為controller與 client。  
&emsp; &emsp; controller 是直接操作硬體 mailbox 的驅動。 它向下直接操作硬體寄存器，通過發送與接收中斷（如果硬體支援）完成與 remote 的通信; 向上通過框架提供的介面完成與 client 驅動的交流。
&emsp; &emsp; client 是 controller 的消費者，向下與 controller 溝通，完成通道申請，數據準備等功能; 向上提供可供用戶空間操作的介面。  
&emsp; &emsp; mailbox 框架所負責的就是 controller 與 client 之間的介面，內核文檔中說：“client 和 controller 驅動程式可能是會非常依賴於特定平臺的，因此，client 驅動大概率不能在多個平臺之間共用”，所以在`/drivers/mailbox`目錄下，只能找到有關 controller 的驅動而找不到 client 的驅動，只能找到一個測試 controller 的`mailbox-test.c`的 client 驅動。 client 驅動如何與使用者空間交換數據也就由驅動開發者自己決定。  
&emsp; &emsp; 下圖是兩個驅動註冊的基本框架：  

<div align=center>
<img src="../zh/images/mailbox/130101_frame_00.svg" width="1400">
</div>  

## 1.2 數據結構

&emsp; &emsp; controller 與 client 的數據結構如下圖所示：<div align=center>
<img src="../zh/images/mailbox/130102_data_structure.svg" width="1400">
</div>

&emsp; &emsp; 框架中使用`struct mbox_controller`抽象 mailbox 控制器，使用`struct mbox_chan`抽象通道，使用函數集合`struct mbox_chan_ops`來對通道進行操作。 上面三個數據結構是針對controller的。 框架使用`struct mbox_client`抽象用戶端，是針對 client 的。  
&emsp; &emsp; 除此之外，我們需要針對我們的設備與驅動定義一個我們自己的設備結構體，如上圖所示。 client 與 controller 的聯繫是通過在 client 中申請通道時，在`mbox_request_channel`函數中完成的，一個通道綁定一個`struct mbox_client`結構體。

## 1.3 函數調用流程

&emsp; &emsp; 函數調用流程如下圖所示：<div align=center>
<img src="../zh/images/mailbox/130103_frame_callback.svg" width="1400">
</div>  

&emsp; &emsp; 用戶空間與 client 驅動的數據傳遞使用 ioctl 加異步通知的方式，這一部分內容由驅動開發者自己決定，不屬於框架的內容。  
&emsp; &emsp; 我們在 client 驅動中創建了設備節點`/dev/mailbox-client`，用戶空間通過此文件進行數據讀取與發送。 8 個發送通道，8 個接收通道。

### 1.3.1 發送數據流程

&emsp; &emsp; 如上圖所示：

1. 用戶空間操作檔句柄發送數據;
2. 進入 client 驅動的 ioctl 函數，此函數將使用者空間數據複製到內核空間，最終調用了`mbox_send_message`函數;
3. 此函數的具體處理流程可以看後面章節的代碼分析，主要就是調用了兩個回調函數：client 驅動實現的`tx_prepare`，controller 驅動實現的`send_data`。 看名字就可以知道這兩個函數的作用。 需要注意的是，有些硬體的 mailbox 是有硬體數據傳輸寄存器的，那麼此時，數據傳輸就可以在`send_data`中完成; 有些硬體沒有硬體數據傳輸寄存器，那麼也可以在`tx_prepare`中完成實際的數據傳輸，`send_data`的作用就變成了單純的**觸發中斷通知遠端處理器**;
4. 當遠端處理器收到中斷，並接收數據以後，需要回復給controller一個中斷表明 Tx 已經完成;
5. 收到 Tx ACK 以後，controller 註冊的中斷處理函數需要調用`mbox_chan_txdone`來通知上層本次傳輸已被遠端接收;
6. `mbox_chan_txdone`通過 client 註冊的`tx_done`來告知 client 本次傳輸已完成。 由 client 決定後續處理，`tx_done`的參數記錄了數據傳輸的狀態。

### 1.3.1 接收數據流程

&emsp; &emsp; 如上圖所示：

1. 遠端處理器發送給 controller 傳輸數據的中斷;
2. 收到中斷以後，controller 註冊的中斷處理函數調用`mbox_chan_received_data`通知上層收到遠端傳來的數據，並回復給遠端 Rx ACK。
3. `mbox_chan_received_data`調用客戶端註冊的`rx_callback`;
4. `rx_callback`中從設備樹指定的位址讀取數據，然後使用異步通知的方式通知用戶空間;
5. 用戶空間的異步處理函數中調用ioctl讀取接收通道的數據。

# 2 框架代碼分析

## 2.1 mailbox_controller.h

&emsp; &emsp; 定義了`mbox_controller`（對 mailbox 硬體的抽象）、`mbox_chan`（對 channel 的抽象）`mbox_chan_ops`（操作 channel 的回調函數的集合）。

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

## 2.3 郵箱

### 2.3.1 add_to_rbuf

```c
/* 
 * 缓存通道传输的消息。
 * 'msg_count' 记录缓冲消息的数量；
 * 'msg_free' 是下一条将被缓存的消息的 index。
 */
static int add_to_rbuf(struct mbox_chan *chan, void *mssg)
```

&emsp; &emsp; 該函數邏輯如下：<div align=center>
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

&emsp; &emsp; 該函數邏輯如下：<div align=center>
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

&emsp; &emsp; 該函數邏輯如下：<div align=center>
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

&emsp; &emsp; 此函數，通過`of_parse_phandle_with_args`來從設備樹中獲得 index 對應請求的 channel。

- `mboxes`指向節點中 phandle 列表屬性名;
- `#mbox-cells`指明 phandle 指向的節點所含的 cell 個數;
- `index`表示 phandle 列表的索引，0 代表第一個 phandle，1 代表第二個 phandle;
- `out_args`存儲 phandle 中的參數。

&emsp; &emsp; 例如，在我們的設備樹中

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

&emsp; &emsp; 後面是對通道資訊的初始化，包括緩存計數的清零，chan 的 cl 和客戶端申請 channel 的 client 綁定，tx_complete 的初始化等。  
&emsp; &emsp; 該函數邏輯如下：<div align=center>
<img src="../zh/images/mailbox/130203_mbox_request_channel.svg" width="500">
</div>

### 2.3.9 mbox_request_channel_byname

&emsp; &emsp; 此函數就是根據 name（mbox-names 屬性） 從設備樹中獲取對應的 mboxes 清單，最後還是調用了 mbox_request_channel 函數申請通道。

### 2.3.10 mbox_free_channel

&emsp; &emsp; 通道釋放函數，將指定通道的成員清空，如果對應的硬體寄存器需要配置的，實現`shutdown`回調函數。

### 2.3.11 mbox_controller_register 和 mbox_controller_unregister

&emsp; &emsp; 顧名思義。

# 3 設備樹分析

&emsp; &emsp; 範例：

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

## 3.1 控制器

&emsp; &emsp; 必須有屬性`#mbox-cells`，值至少為 1。 它指明瞭 client 屬性`mboxes` cell 的個數。

## 3.2 用戶端

&emsp; &emsp; 必須有屬性`mboxes`，它會提供給驅動通道的資訊。  
&emsp; &emsp; 可選屬性`mbox-names`，是`mboxes`的別名。  
&emsp; &emsp; 可選屬性`reg`，mailbox client 與 remote 通信而保留的任何記憶體的一部分。  

## 3.3 該屬性的使用方法

&emsp; &emsp; `mbox-cells`、`mboxes`、`mbox-names`三個屬性是在申請通道時用到的。

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

&emsp; &emsp; 在這裡我們將其用作了通道號，也可以添加別的特定於硬體的信息，具體解釋由驅動開發者自行決定。

# 4 驅動實現

- dts 配置
&emsp; &emsp; 參見上面設備樹示例。
- controller
&emsp;&emsp;參考`/drivers/mailbox/canaan-mailbox.c`
- client
&emsp;&emsp;參考`/drivers/mailbox/canaan_mbox_client.c`
- 用戶空間程式
&emsp; &emsp; 參考`k510_buildroot/package/mailbox_demo/src/mailbox_async.c`和`k510_buildroot/package/mailbox_demo/src/mailbox_poll.c`

# 5 demo 使用方法

## 5.1 使用

1. 載入 dsp 裸機程式
進入目錄`/app/dsp_app_new`，執行命令`./dsp_app mailbox_demo.bin`將裸機程式載入 dsp 中，如下圖所示：  
![dsp_load](../zh/images/mailbox/130601_dsp_load.png)  
2. 運行 Linux 使用者空間的測試 app
進入目錄`/app/mailbox_demo`，執行命令`./mailbox_async`，如下圖所示：  
![mailbox_demo](../zh/images/mailbox/130602_mailbox_async.png)  
此 demo 使用異步通知的方式接收 dsp 發送來的數據。
3. 在目錄`/app/mailbox_demo`中，執行命令`./mailbox_poll`，如下圖所示：  
![mailbox_demo](../zh/images/mailbox/130602_mailbox_poll.png)
此 demo 使用 poll 阻塞 500ms 的方式接收 dsp 發送來的數據。 我們每隔 4s 發送一次數據，每 2s 讀一次數據，因此可以看到每隔 2s，讀取成功與讀取失敗交錯列印，阻塞讀取是成功的。

## 5.2 測試代碼

&emsp; &emsp; dsp 裸機程式位於`k510_buildroot/package/k510_evb_test/src/test/mailbox_demo/main.c`中，用戶空間測試代碼位於`k510_buildroot/package/mailbox_demo/src/mailbox_async.c`和`k510_buildroot/package/mailbox_demo/src/mailbox_poll.c`。

# 6 已知問題

&emsp; &emsp; 偶爾會出現第一次執行命令`./dsp_app mailbox_demo.bin`時沒有將 dsp 程式燒進 dsp 中的情況出現。 此時執行 demo 會出現發送失敗的情況。

**翻譯免責聲明**  
為方便客戶，Canaan 使用 AI 翻譯程式將文字翻譯為多種語言，它可能包含錯誤。 我們不保證提供的譯文的準確性、可靠性或時效性。 對於因依賴已翻譯信息的準確性或可靠性而造成的任何損失或損害，Canaan 概不負責。 如果不同語言翻譯之間存在內容差異，以簡體中文版本為準。

如果您要報告翻譯錯誤或不準確的問題，歡迎通過郵件與我們聯繫。
