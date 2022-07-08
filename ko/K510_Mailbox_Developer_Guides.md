![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 사서함 개발자 안내서</font>**

<font face="黑体"  size=3>문서 버전: V1.0.0</font>

<font face="黑体"  size=3>게시 날짜: 2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**면책 조항**</font>
귀하가 구매한 제품, 서비스 또는 기능은 베이징 Jiananges 정보 기술 유한 회사(이하 "회사")의 상업 계약 및 약관의 적용을 받으며, 이 문서에 설명된 제품, 서비스 또는 기능의 전부 또는 일부는 구매 또는 사용의 범위를 벗어납니다. 계약에 달리 합의하지 않는 한, 회사는 본 문서의 진술, 정보, 내용의 정확성, 신뢰성, 완전성, 마케팅, 특정 목적 및 비침략성에 대해 명시적 또는 묵시적으로 어떠한 진술이나 보증도 하지 않습니다. 달리 합의하지 않는 한, 이 문서는 사용 지침의 참조로만 사용됩니다.
이 문서의 내용은 제품 버전 업그레이드 또는 기타 이유로 인해 예고 없이 수시로 업데이트되거나 수정될 수 있습니다. 

**<font face="黑体"  size=3>상표 고지</font>**

베이징 <img src="../zh/images/canaan-logo.png" style="zoom:33%;" />Jianan Jets 정보 기술 유한 공사의 상표는 Jianan, Jianan 및 Jianan의 다른 상표입니다. 이 문서에 언급될 수 있는 기타 모든 상표 또는 등록 상표는 해당 소유자가 소유합니다. 

**<font face="黑体"  size=3>저작권 ©2022 베이징 Jiananjets 정보 기술 유한 회사</font>**
이 문서는 K510 플랫폼 개발 및 설계에만 적용되며, 어떠한 단위나 개인도 회사의 서면 허가 없이 이 문서의 일부 또는 전부를 어떤 형태로든 배포할 수 없습니다. 

**<font face="黑体"  size=3>베이징 Jiananjets 정보 기술 유한 회사</font>**
웹 사이트: canaan-creative.com
비즈니스 문의: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# 서문
**<font face="黑体"  size=5>문서의 목적</font>**
이 문서는 K510 mailbox 기반 개발 문서입니다. 

**<font face="黑体"  size=5>독자 개체입니다</font>**

이 문서(이 가이드)가 주로 적용되는 사람:

- 소프트웨어 개발자
- 기술 지원 담당자

**<font face="黑体"  size=5>레코드를 수정합니다</font>**
 <font face="宋体"  size=2>개정 레코드에는 각 문서 업데이트에 대한 설명이 누적됩니다. 문서의 최신 버전에는 이전 버전의 모든 업데이트가 포함되어 있습니다. </font>

| 버전 번호입니다   | 수정자     | 개정일입니다 | 개정 지침 |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | 시스템 소프트웨어 그룹입니다 | 2022-03-09 | SDK V1.5 릴리스 |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>카탈로그</font>**

[목차]

<div style="page-break-after:always"></div>

# 1 프레임워크 분석

## 1.1 클라이언트、컨트롤러 与 프레임 워크

&emsp; &emsp; mailbox 프레임워크는 다중 프로세서 간의 통신을 처리하는 데 사용됩니다. 프레임워크는 controller와 client로 나뉩니다.  
&emsp; &emsp; controller는 하드웨어 mailbox를 직접 조작하는 드라이버입니다. 하드웨어 레지스터를 직접 작동시키고 하드웨어가 지원하는 경우 전송 및 수신 인터럽트를 통해 remote와의 통신을 완료합니다. 프레임워크에서 제공하는 인터페이스를 통해 client 기반 통신을 수행합니다.
&emsp; &emsp; client는 controller의 소비자이며, 컨트롤러와 통신하고 채널 응용 프로그램, 데이터 준비 등을 완료합니다. 사용자 공간에서 작동할 수 있는 인터페이스를 위쪽으로 제공합니다.  
&emsp; &emsp; mailbox 프레임워크는 controller와 client 간의 인터페이스를 담당하며 커널 설명서는 "client 및 controller 드라이버는 특정 플랫폼에 크게 의존할 수 있으므로 client 드라이버의 큰 확률은 여러 플랫폼 간에 공유할 수 없으므로 디렉터리에서`/drivers/mailbox` 컨트롤러 드라이버만 찾을 수 있지만 client 드라이버는 찾을 수 없으며 하나의 테스트만 찾을 수 있습니다." controller의 `mailbox-test.c`client 드라이버입니다. 클라이언트 드라이버가 사용자 공간과 데이터를 교환하는 방법도 드라이버 개발자의 재량에 따라 결정됩니다.  
&emsp; &emsp; 다음 그림은 등록을 구동하는 두 가지 기본 프레임워크입니다 

<div align=center>
<img src="../zh/images/mailbox/130101_frame_00.svg" width="1400">
</div>  

## 1.2 데이터 구조

&emsp; &emsp; controller 및 client의 데이터 구조는 다음 그림과 같습니다.<div align=center>
<img src="../zh/images/mailbox/130102_data_structure.svg" width="1400">
</div>

&emsp; &emsp; 프레임워크는 `struct mbox_controller`추상 mailbox 컨트롤러를 사용하고, `struct mbox_chan`추상 채널을 사용하고, 함수 컬렉션을 사용하여 `struct mbox_chan_ops`채널에서 작동합니다. 위의 세 가지 데이터 구조는 controller에 대한 것입니다. 프레임워크`struct mbox_client`는 client용 추상 클라이언트를 사용합니다.  
&emsp; &emsp; 또한 위의 그림과 같이 장치 및 드라이버에 대한 자체 장치 구조를 정의해야 합니다. 클런트-컨트롤러 연결은 client에서 채널을 요청할 때 `mbox_request_channel`함수에서 수행되며 채널은 구조를 바인딩`struct mbox_client`합니다. 

## 1.3 함수는 프로세스를 호출합니다

&emsp; &emsp; 함수 호출 흐름은 다음 그림과 같습니다.<div align=center>
<img src="../zh/images/mailbox/130103_frame_callback.svg" width="1400">
</div>  

&emsp; &emsp; 사용자 공간 및 client 기반 데이터 전송은 ioctl 플러스 비동기 알림을 사용하며, 이 부분은 드라이버 개발자가 결정하며 프레임워크의 일부가 아닙니다.  
&emsp; &emsp; 클라이언트 드라이버에서 `/dev/mailbox-client`사용자 공간이 데이터를 읽고 전송하는 장치 노드를 만들었습니다. 8개의 송신 채널과 8개의 수신 채널. 

### 1.3.1 데이터 전송 프로세스

&emsp; &emsp; 위의 그림에서 볼 수 있듯이:

1. 사용자 공간 작업 파일 핸들은 데이터를 보냅니다.
2. 사용자 공간 데이터를 커널 공간에 복사하고 결국 함수를 호출하는 client 기반 ioctl 함수로 이동합니다`mbox_send_message`. 
3. 이 함수의 특정 처리는 다음 장의 코드 분석을 볼 수 있으며, 주로 client 기반 구현과 controller 기반 구현이라는 두 개의 콜백 함수를 호출`tx_prepare`합니다`send_data`. 이름을 보면 두 함수가 무엇을 하는지 알 수 있습니다. 일부 하드웨어의 mailbox에는 하드웨어 데이터 전송 레지스터가 있으므로 데이터 전송을 수행할 수 있습니다`send_data`. 일부 하드웨어에는 하드웨어 데이터 전송 레지스터가 없으므로 `tx_prepare`실제 데이터 전송을 완료할 수 있으며,`send_data` 그 역할은 단순히 **인터럽트 알림 원격 프로세서를 트리거**하는 것입니다. 
4. 원격 프로세서가 인터럽트를 수신하고 데이터를 수신하면 Tx가 완료되었음을 나타내는 인터럽트가 controller에 반환되어야 합니다.
5. Tx ACK를 받은 후 controller에 등록된 인터럽트 처리기는 `mbox_chan_txdone`이 전송이 원격으로 수신되었음을 상위 계층에 알리기 위해 호출되어야 합니다. 
6. `mbox_chan_txdone`client를 통해 등록`tx_done`하여 이 전송이 완료되었음을 client에 알립니다. 후속 처리는 client에 의해 결정되며`tx_done` 매개 변수는 데이터 전송 상태를 기록합니다. 

### 1.3.1 데이터 수신 프로세스

&emsp; &emsp; 위의 그림에서 볼 수 있듯이:

1. 원격 프로세서에서 controller로 전송된 데이터 전송의 중단;
2. 인터럽트를 받은 후 controller에 등록된 인터럽트 처리기 호출`mbox_chan_received_data`은 상위 계층이 원격에서 데이터를 수신하고 원격 Rx ACK로 다시 응답하도록 알립니다. 
3. `mbox_chan_received_data`클라이언트 등록을 호출`rx_callback`합니다. 
4. `rx_callback`에서 장치 트리에 지정된 주소에서 데이터를 읽은 다음 비동기 알림을 사용하여 사용자에게 공간을 알립니다.
5. 사용자 공간의 비동기 처리기에서 ioctl을 호출하여 수신 채널의 데이터를 읽습니다.

# 2 프레임워크 코드 분석

## 2.1 mailbox_controller.h

&emsp; &emsp; 정의`mbox_controller`(mailbox 하드웨어에 대한 추상화),`mbox_chan` (channel에 대한 추상화)`mbox_chan_ops`(channel을 조작하는 콜백 함수의 컬렉션). 

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

## 2.3 사서함.c

### 2.3.1 add_to_rbuf

```c
/* 
 * 缓存通道传输的消息。
 * 'msg_count' 记录缓冲消息的数量；
 * 'msg_free' 是下一条将被缓存的消息的 index。
 */
static int add_to_rbuf(struct mbox_chan *chan, void *mssg)
```

&emsp; &emsp; 함수 논리는 다음과 같습니다.<div align=center>
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

&emsp; &emsp; 함수 논리는 다음과 같습니다.<div align=center>
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

&emsp; &emsp; 함수 논리는 다음과 같습니다.<div align=center>
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

&emsp; &emsp; 이 함수는 `of_parse_phandle_with_args`장치 트리에서 index 해당 요청에 대한 channel을 가져옵니다. 

- `mboxes`노드의 phandle 목록 속성 이름을 가리킵니다.
- `#mbox-cells`phandle이 가리키는 노드 수를 나타냅니다.
- `index`첫 번째 phandle을 나타내는 인덱스와 두 번째 phandle을 나타내는 0을 나타냅니다.
- `out_args`phandle의 매개 변수를 저장합니다.

&emsp; &emsp; 예를 들어 장치 트리에서

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

&emsp; &emsp; 그런 다음 캐시 수의 0, chan의 cl 및 클라이언트가 channel의 클라이언트 바인딩을 요청하고 tx_complete 초기화 등을 포함하여 채널 정보를 초기화합니다.  
&emsp; &emsp; 함수 논리는 다음과 같습니다.<div align=center>
<img src="../zh/images/mailbox/130203_mbox_request_channel.svg" width="500">
</div>

### 2.3.9 mbox_request_channel_byname

&emsp; &emsp; 이 함수는 name(mbox-names 속성)을 기반으로 장치 트리에서 해당 mboxes 목록을 가져오고 마지막으로 mbox_request_channel 함수 응용 프로그램 채널을 호출합니다.

### 2.3.10 mbox_free_channel

&emsp; &emsp; 채널 해제 함수는 해당 하드웨어 레지스터를 구성해야 하는 경우 콜백 함수를 구현하기 위해 채널의 멤버를 비웁니다`shutdown`. 

### 2.3.11 mbox_controller_register 및 mbox_controller_unregister

&emsp; &emsp; 이름에서 알 수 있듯이.

# 3 장치 트리 분석

&emsp; &emsp; 예:

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

## 3.1 컨트롤러

&emsp; &emsp; 속성이 있어야 `#mbox-cells`하며 값은 1 이상이어야 합니다. client 속성`mboxes` 셀 수를 나타냅니다. 

## 3.2 클라이언트

&emsp; &emsp; `mboxes`드라이버 채널에 대한 정보를 제공하는 속성이 있어야 합니다.  
&emsp; &emsp; 선택적 속성`mbox-names`, 예 `mboxes`별칭입니다.  
&emsp; &emsp; 선택적 속성`reg`인 mailbox client는 remote와 통신하면서 예약된 모든 메모리의 일부입니다.  

## 3.3 이 속성을 사용하는 방법입니다

&emsp; &emsp; `mbox-cells`, `mboxes`, `mbox-names`세 가지 속성은 채널을 신청할 때 사용됩니다. 

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

&emsp; &emsp; 여기에서 채널 번호로 사용하거나 드라이버 개발자의 재량에 따라 다른 하드웨어 관련 정보를 추가할 수 있습니다.

# 4 드라이브 구현

- dts 구성
&emsp; &emsp; 위의 장치 트리 예제를 참조하십시오.
- 컨트롤러
&emsp;&emsp;참조`/drivers/mailbox/canaan-mailbox.c`
- 클라이언트
&emsp;&emsp;참조`/drivers/mailbox/canaan_mbox_client.c`
- 사용자 공간 프로그램입니다
&emsp; &emsp; 참조`k510_buildroot/package/mailbox_demo/src/mailbox_async.c` 및`k510_buildroot/package/mailbox_demo/src/mailbox_poll.c`

# 5 데모 사용 방법

## 5.1 사용

1. dsp 베어 메탈 프로그램을 로드합니다
디렉토리로 이동하여`/app/dsp_app_new` `./dsp_app mailbox_demo.bin`다음 그림과 같이 베어 메탈 프로그램을 dsp에 로드하는 명령을 실행합니다.  
![dsp_load](../zh/images/mailbox/130601_dsp_load.png)  
2. Linux 사용자 공간에 대한 테스트 앱을 실행합니다
디렉토리로 이동하여`/app/mailbox_demo` `./mailbox_async`다음 그림과 같이 명령을 실행합니다.  
![mailbox_demo](../zh/images/mailbox/130602_mailbox_async.png)  
이 데모는 비동기 알림을 사용하여 dsp에서 전송된 데이터를 수신합니다. 
3. 카탈로그에서`/app/mailbox_demo` 다음 `./mailbox_poll`그림과 같이 명령을 실행합니다.  
![mailbox_demo](../zh/images/mailbox/130602_mailbox_poll.png)
이 데모는 poll 차단 500ms를 사용하여 dsp에서 전송된 데이터를 수신합니다. 4s마다 데이터를 보내고 2s마다 데이터를 읽으므로 2s마다 읽기가 성공하고 읽기가 실패한 인터리브 인쇄가 성공하고 차단 읽기가 성공하는 것을 볼 수 있습니다. 

## 5.2 코드를 테스트합니다

&emsp; &emsp; dsp 베어 메탈 프로그램은 사용자`k510_buildroot/package/k510_evb_test/src/test/mailbox_demo/main.c` 공간 테스트 코드가 있는 위치에 있습니다`k510_buildroot/package/mailbox_demo/src/mailbox_async.c``k510_buildroot/package/mailbox_demo/src/mailbox_poll.c`. 

# 6 알려진 문제

&emsp; &emsp; 명령을 처음 실행할 `./dsp_app mailbox_demo.bin`때 dsp 프로그램이 dsp에 굽지 않는 경우가 있습니다. 이 시점에서 demo를 실행하면 전송이 실패합니다. 

**번역 면책 조항**  
고객의 편의를 위해 Canan은 AI 번역 프로그램을 사용하여 오류를 포함할 수 있는 여러 언어로 텍스트를 번역합니다. 당사는 제공된 번역의 정확성, 신뢰성 또는 적시성을 보장하지 않습니다. Canan은 번역된 정보의 정확성이나 신뢰성에 의존하여 발생하는 손실이나 손해에 대해 책임을 지지 않습니다. 언어 번역 간에 콘텐츠 차이가 있는 경우 중국어 간체 버전이 우선합니다. 

번역 오류 또는 부정확한 문제를 신고하려면 이메일로 문의하시기 바랍니다.