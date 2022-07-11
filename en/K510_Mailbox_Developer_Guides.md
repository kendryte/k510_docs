![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 Mailbox Developer's Guide</font>**

<font face="黑体"  size=3>Document version: V1.0.0</font>

<font face="黑体"  size=3>Published: 2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Disclaimer**</font>
The products, services or features you purchase shall be subject to the commercial contracts and terms of Beijing Canaan Jiesi Information Technology Co., Ltd. ("the Company", the same hereinafter), and all or part of the products, services or features described in this document may not be within the scope of your purchase or use. Except as otherwise agreed in the contract, the Company disclaims all representations or warranties, express or implied, as to the accuracy, reliability, completeness, marketing, specific purpose and non-aggression of any representations, information, or content of this document. Unless otherwise agreed, this document is provided as a guide for use only.
Due to product version upgrades or other reasons, the contents of this document may be updated or modified from time to time without any notice.

**<font face="黑体"  size=3>Trademark Notices</font>**

""<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, "Canaan" icon, Canaan and other trademarks of Canaan and other trademarks of Canaan are trademarks of Beijing Canaan Jiesi Information Technology Co., Ltd. All other trademarks or registered trademarks that may be mentioned in this document are owned by their respective owners.

**<font face="黑体"  size=3>Copyright ©2022 Beijing Canaan Jiesi Information Technology Co., Ltd</font>**
This document is only applicable to the development and design of the K510 platform, without the written permission of the company, no unit or individual may disseminate part or all of the content of this document in any form.

**<font face="黑体"  size=3>Beijing Canaan Jiesi Information Technology Co., Ltd</font>**
URL: canaan-creative.com
Business Enquiries: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# preface
**<font face="黑体"  size=5>Document purpose</font>**
This document is a development document for the K510 mailbox driver.

**<font face="黑体"  size=5>Reader Objects</font>**

The main people to whom this document (this guide) applies:

- Software developers
- Technical support personnel

**<font face="黑体"  size=5>Revision history</font>**
 <font face="宋体"  size=2>The revision history accumulates a description of each document update. The latest version of the document contains updates for all previous versions. </font>

| The version number   | Modified by     | Date of revision | Revision Notes |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | System software groups | 2022-03-09 | SDK V1.5 released |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contents</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Framework analysis

## 1.1 client、controller 与 framework

&emsp; &emsp; The mailbox framework is used to handle communication between multiple processors. The framework is divided into controller and client.  
&emsp; &emsp; Controller is a driver that directly manipulates the hardware mailbox. It operates the hardware registers directly down, completing communication with remote by sending and receiving interrupts (if supported by the hardware); Up to the interface provided by the framework to complete the communication with the client driver.
&emsp; &emsp; The client is the consumer of the controller, communicating with the controller downwards, completing channel applications, data preparation and other functions; Provides interfaces up for user-space manipulation.  
&emsp; &emsp; The mailbox framework is responsible for the interface between the controller and the client, the kernel documentation says: "The client and controller driver may be very dependent on the specific platform, therefore, the client driver can not be shared between multiple platforms", so in`/drivers/mailbox` the directory, only the driver about the controller can be found and can not find the client driver, only one test can be found The `mailbox-test.c`client driver of the controller. How the client driver exchanges data with the user space is also up to the driver developer himself.  
&emsp; &emsp; The following diagram is the basic framework for two driver registrations:

<div align=center>
<img src="../zh/images/mailbox/130101_frame_00.svg" width="1400">
</div>  

## 1.2 Data Structures

&emsp; &emsp; The data structure of controller and client is shown in the following figure:<div align=center>
<img src="../zh/images/mailbox/130102_data_structure.svg" width="1400">
</div>

&emsp; &emsp; The framework uses `struct mbox_controller`abstract mailbox controllers, abstract `struct mbox_chan`channels, and collections of functions `struct mbox_chan_ops`to manipulate channels. The above three data structures are for controllers. The framework uses `struct mbox_client`abstract clients, which are client-specific.  
&emsp; &emsp; In addition to this, we need to define our own device structure for our devices and drives, as shown in the figure above. The connection between the client and the controller is`mbox_request_channel` done in the function when applying for a channel in the client, and one channel is bound to a`struct mbox_client` struct.

## 1.3 Function call flow

&emsp; &emsp; The function call flow is shown in the following figure:<div align=center>
<img src="../zh/images/mailbox/130103_frame_callback.svg" width="1400">
</div>  

&emsp; &emsp; User-space and client-driven data delivery uses ioctl plus asynchronous notifications, which is determined by the driver developers themselves and does not belong to the framework.  
&emsp; &emsp; We created a device node in the client driver`/dev/mailbox-client` through which the user space reads and sends data. 8 transmit channels, 8 receive channels.

### 1.3.1 Sending Data Flow

&emsp; &emsp; As shown in the figure above:

1. User-space manipulation file handles to send data;
2. Enter the client-driven ioctl function, which copies user-space data to kernel space and eventually calls the`mbox_send_message` function;
3. The specific processing process of this function can be seen in the code analysis of the later chapters, which mainly calls two callback functions: client-driven`tx_prepare` implementation and controller-driven implementation`send_data`. Look at the names to know what these two functions do. It should be noted that some hardware mailboxes have hardware data transmission registers, so at this time, the data transmission can be`send_data` completed in the middle; Some hardware does not have hardware data transmission registers, then the actual data transmission can also be`tx_prepare` completed in it, and `send_data`the role becomes a simple **trigger interrupt notification to the remote processor**;
4. When the remote processor receives the interrupt and receives the data, it needs to reply to the controller with an interrupt indicating that Tx has completed;
5. After receiving the Tx ACK, the controller-registered interrupt handler needs to be called `mbox_chan_txdone`to notify the upper layer that the transfer has been received remotely;
6. `mbox_chan_txdone`Inform the client that the `tx_done`transfer is completed through the client registration. The client decides for subsequent processing, and the`tx_done` parameters record the state of the data transfer.

### 1.3.1 Process of Receiving Data

&emsp; &emsp; As shown in the figure above:

1. Interrupts of the remote processor sending data to the controller;
2. After receiving the interrupt, the controller-registered interrupt handler call `mbox_chan_received_data`informs the upper layer to receive data coming from the far end and reply to the remote Rx ACK.
3. `mbox_chan_received_data`Invoke the client registered`rx_callback`;
4. `rx_callback`reads data from the address specified in the device tree, and then notifies the user space using asynchronous notifications;
5. The user-space asynchronous handler that calls ioctl reads the data of the receive channel.

# 2 Framework code analysis

## 2.1 mailbox_controller.h

&emsp; &emsp; Defined `mbox_controller`(abstraction of mailbox hardware),`mbox_chan` (abstraction of channel) `mbox_chan_ops`(collection of callback functions that manipulate channels).

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

&emsp; &emsp; The function logic is as follows:<div align=center>
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

&emsp; &emsp; The function logic is as follows:<div align=center>
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

&emsp; &emsp; The function logic is as follows:<div align=center>
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

&emsp; &emsp; This function, by way, `of_parse_phandle_with_args`obtains the channel of the requested index from the device tree.

- `mboxes`Points to the phandle list property name in the node;
- `#mbox-cells`Indicates the number of cells contained in the node pointed to by the phandle;
- `index`Represents the index of the phandle list, with 0 representing the first phandle and 1 representing the second phandle;
- `out_args`Stores parameters in the phandle.

&emsp; &emsp; For example, in our device tree

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

&emsp; &emsp; This is followed by the initialization of the channel information, including the zeroing of the cache count, the cl of chan and the client binding of the client requesting the channel, the initialization of the tx_complete, and so on.  
&emsp; &emsp; The function logic is as follows:<div align=center>
<img src="../zh/images/mailbox/130203_mbox_request_channel.svg" width="500">
</div>

### 2.3.9 mbox_request_channel_byname

&emsp; &emsp; This function obtains the corresponding mboxes list from the device tree according to name(mbox-names attribute), and finally calls the mbox_request_channel function to apply for a channel.

### 2.3.10 mbox_free_channel

&emsp; &emsp; The channel release function implements a callback function that will empty the members of the specified channel and implement the callback function if the corresponding hardware register needs to be configured`shutdown`.

### 2.3.11 mbox_controller_register and mbox_controller_unregister

&emsp; &emsp; Name implies.

# 3 Device tree analysis

&emsp; &emsp; Example:

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

## 3.1 controller

&emsp; &emsp; There must be an attribute`#mbox-cells` with a value of at least 1. It indicates the`mboxes` number of cells for the client attribute.

## 3.2 client

&emsp; &emsp; There must be a property `mboxes`that provides information to the drive channel.  
&emsp; &emsp; Optional attribute`mbox-names`, yes `mboxes`alias.  
&emsp; &emsp; Optionally`reg`, the mailbox client communicates with the remote while retaining a portion of any memory.  

## 3.3 How to use the property

&emsp; &emsp; `mbox-cells`The`mboxes` `mbox-names`three properties are used when applying for channels.

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

&emsp; &emsp; Here we use it as the channel number, or we can add other hardware-specific information, the specific explanation is up to the driver developer.

# 4 Driver implementation

- DTS configuration
&emsp; &emsp; See the device tree example above.
- controller
&emsp;&emsp;reference`/drivers/mailbox/canaan-mailbox.c`
- client
&emsp;&emsp;reference`/drivers/mailbox/canaan_mbox_client.c`
- User-space programs
&emsp; &emsp; Reference`k510_buildroot/package/mailbox_demo/src/mailbox_async.c` and`k510_buildroot/package/mailbox_demo/src/mailbox_poll.c`

# 5 How to use demo

## 5.1 Use

1. Load the dsp bare metal program
Go to the directory`/app/dsp_app_new` and execute the command `./dsp_app mailbox_demo.bin`to load the bare metal program into the dsp, as shown in the following figure:  
![dsp_load](../zh/images/mailbox/130601_dsp_load.png)  
2. Run the Linux userspace test app
Enter the directory`/app/mailbox_demo` and execute the command`./mailbox_async`, as shown in the following figure:  
![mailbox_demo](../zh/images/mailbox/130602_mailbox_async.png)  
This demo uses asynchronous notifications to receive data sent by the dsp.
3. In the directory`/app/mailbox_demo`, execute the command`./mailbox_poll`, as shown in the following figure:  
![mailbox_demo](../zh/images/mailbox/130602_mailbox_poll.png)
This demo uses poll blocking for 500ms to receive data sent by the dsp. We send data every 4s and read the data every 2s, so we can see that every 2s, the read success is staggered with the read failure, and the blocking read is successful.

## 5.2 Testing the Code

&emsp; &emsp; The dsp bare metal program is located `k510_buildroot/package/k510_evb_test/src/test/mailbox_demo/main.c`in the middle, and the user-space test code is located in`k510_buildroot/package/mailbox_demo/src/mailbox_async.c` and`k510_buildroot/package/mailbox_demo/src/mailbox_poll.c`.

# 6 Known issues

&emsp; &emsp; Occasionally, the `./dsp_app mailbox_demo.bin`dsp program is not burned into the dsp the first time the command is executed. Execution of the demo at this point will result in a send failure.

**Translation Disclaimer**  
For the convenience of customers, Canaan uses an AI translator to translate text into multiple languages, which may contain errors. We do not guarantee the accuracy, reliability or timeliness of the translations provided. Canaan shall not be liable for any loss or damage caused by reliance on the accuracy or reliability of the translated information. If there is a content difference between the translations in different languages, the Chinese Simplified version shall prevail.

If you would like to report a translation error or inaccuracy, please feel free to contact us by mail.
