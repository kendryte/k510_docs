![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510メールボックス開発者ガイド</font>**

<font face="黑体"  size=3>ドキュメントのバージョン: V1.0.0</font>

<font face="黑体"  size=3>発売日:2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**免責事項**</font>
お客様が購入した製品、サービス、または機能は、北京Jiayuan Jetts情報技術有限公司(以下「当社」、以下同じ)の商業契約および条件の対象となり、本書に記載されている製品、サービス、または機能の全部または一部がお客様の購入または使用の範囲外となる場合があります。 契約に別段の定めがない限り、当社は、本書の記述、情報、内容の正確性、信頼性、完全性、マーケティング、特定目的、非攻撃性について、明示または黙示を問わず、いかなる表明または保証も行いません。 特に断りのない限り、このドキュメントは使用ガイダンスの参照としてのみ使用してください。
このドキュメントの内容は、製品バージョンのアップグレードまたはその他の理由により、予告なく随時更新または変更されることがあります。

**<font face="黑体"  size=3>商標表示</font>**

「<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />」アイコン、カナン、その他の商標は、北京Jiayuan Jets情報技術有限公司の商標です。 本書で言及されるその他すべての商標または登録商標は、それぞれの所有者が所有しています。

**<font face="黑体"  size=3>©著作権2022北京Jiayuan Jetth情報技術有限公司</font>**
このドキュメントは、K510プラットフォーム開発設計にのみ適用され、当社の書面による許可なく、いかなるユニットまたは個人も、このドキュメントの一部または全部をいかなる形式でも配布することはできません。

**<font face="黑体"  size=3>北京Jiayuan Jetth情報技術有限公司</font>**
URL: canaan-creative.com
ビジネスお問い合わせ:salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# 序文
**<font face="黑体"  size=5>ドキュメントの目的</font>**
このドキュメントは、K510 mailbox ドライバ用のドキュメントを開発しています。

**<font face="黑体"  size=5>リーダー オブジェクト</font>**

このドキュメント (このガイド) は、主に次の担当者に適用されます。

- ソフトウェア開発者
- テクニカル サポート スタッフ

**<font face="黑体"  size=5>レコードを改訂します</font>**
 <font face="宋体"  size=2>リビジョン レコードには、ドキュメントが更新されるたびに説明が蓄積されます。 ドキュメントの最新バージョンには、以前のすべてのバージョンの更新が含まれています。 </font>

| バージョン番号   | 変更者     | 改訂日 | 修正の説明 |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | システム ソフトウェア グループ | 2022-03-09 | SDK V1.5 リリース |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>目録</font>**

[目次]

<div style="page-break-after:always"></div>

# 1 フレームワーク分析

## 1.1 クライアント、コントローラ与フレームワーク

&emsp; &emsp; mailbox フレームワークは、マルチプロセッサ間の通信を処理するために使用されます。 フレームワークは、controller と client に分割されます。  
&emsp; &emsp; controller は、ハードウェア mailbox を直接操作するドライバです。 ハードウェア レジスタを直接操作し、送信と受信の割り込み (ハードウェアがサポートしている場合) を介して remote との通信を完了します。 client 駆動型との通信は、フレームワークによって提供されるインターフェイスを介して上向きに行われます。
&emsp; &emsp; client は controller の消費者であり、controller とのダウンコミュニケーション、チャネルアプリケーションの完了、データの準備などの機能を備えています。 ユーザー空間で操作できるインターフェイスを上に提供します。  
&emsp; &emsp; mailbox フレームワークは controller と client の間のインターフェイスを担当しており、カーネル ドキュメントでは"client ドライバと controller ドライバは特定のプラットフォームに大きく依存する可能性があるため、client ドライバは複数のプラットフォーム間で共有できない可能性があります" ため、`/drivers/mailbox`ディレクトリの下には controller のドライバのみが見つかり、client ドライバは見つからず、1 つのテストしか見つかりませんでした controller の `mailbox-test.c`client ドライブ。 client ドライバがユーザー空間とデータを交換する方法は、ドライバ開発者自身によって決定されます。  
&emsp; &emsp; 次の図は、登録を駆動する 2 つの基本的なフレームワークです

<div align=center>
<img src="../zh/images/mailbox/130101_frame_00.svg" width="1400">
</div>  

## 1.2 データ構造

&emsp; &emsp; controller と client のデータ構造を次の図に示します。<div align=center>
<img src="../zh/images/mailbox/130102_data_structure.svg" width="1400">
</div>

&emsp; &emsp; フレームワークでは`struct mbox_controller`抽象 mailbox コントローラーを使用し、`struct mbox_chan`抽象チャネルを使用し、関数コレクションを使用`struct mbox_chan_ops`してチャネルを操作します。 上記の 3 つのデータ構造は controller 用です。 フレームワーク`struct mbox_client`は抽象クライアントを使用し、client 用です。  
&emsp; &emsp; さらに、上の図に示すように、デバイスとドライバに対して独自のデバイス構造を定義する必要があります。 client と controller の関係は、client でチャネルを要求するときに関数`mbox_request_channel`内で行われ、チャネルは構造体をバインド`struct mbox_client`します。

## 1.3 関数呼び出しプロセス

&emsp; &emsp; 関数呼び出しのフローを次の図に示します。<div align=center>
<img src="../zh/images/mailbox/130103_frame_callback.svg" width="1400">
</div>  

&emsp; &emsp; ユーザー空間と client 駆動型データ配信は、ioctl と非同期通知を使用して、フレームワークの一部ではないコンテンツを駆動する開発者自身によって決定されます。  
&emsp; &emsp; client ドライバにデバイス ノードを作成し`/dev/mailbox-client`、ユーザー空間がこのファイルを介してデータの読み取りと送信を行います。 8 つの送信チャネルと 8 つの受信チャネル。

### 1.3.1 データ送信プロセス

&emsp; &emsp; 上の図に示すように:

1. ユーザー空間操作ファイル ハンドルはデータを送信します。
2. ユーザー空間データをカーネル空間にコピーし、最終的に関数を呼び出す client 駆動型 ioctl 関数に入ります`mbox_send_message`。
3. この関数の具体的な処理フローは、主に client 駆動型実装と controller 駆動型実装の 2 つのコールバック関数の呼び出しで、後の章のコード分析を参照できます`tx_prepare``send_data`。 名前を見ると、これらの 2 つの関数の動作がわかります。 一部のハードウェアの mailbox にはハードウェア データ転送レジスタがあり、この時点でデータ転送を完了できます`send_data`。 一部のハードウェアにはハードウェア データ転送レジスタがないため、`tx_prepare`実際のデータ転送を完了でき、`send_data`単なる**トリガ割り込み通知遠端プロセッサ**になります。
4. リモートプロセッサが割り込みを受信し、データを受信すると、Tx が完了したことを示す割り込みで controller に返信する必要があります。
5. Tx ACK を受信すると、controller によって登録された割り込み処理関数は、`mbox_chan_txdone`このトランスポートがリモートで受信されたことを上位層に通知するために呼び出す必要があります。
6. `mbox_chan_txdone`client によって登録され`tx_done`、この転送が完了したことを client に通知します。 後続の処理は client によって決定され、`tx_done`パラメータはデータ転送の状態を記録します。

### 1.3.1 データの受信プロセス

&emsp; &emsp; 上の図に示すように:

1. 遠端プロセッサが controller に送信するデータの割り込み。
2. 割り込みが受信されると、controller によって登録された割り込み処理関数呼び出`mbox_chan_received_data`しは、上位レベルが遠端からデータを受信し、遠端 Rx ACK に応答することを通知します。
3. `mbox_chan_received_data`クライアント登録を呼び出します`rx_callback`。
4. `rx_callback`からデバイス ツリーで指定されたアドレスからデータを読み取り、非同期通知を使用してユーザー空間に通知します。
5. ユーザー・スペースの非同期処理関数で ioctl が呼び出され、受信チャネルのデータが読み取られます。

# 2 フレームワーク コード分析

## 2.1 mailbox_controller.h

&emsp; &emsp; 定義されている`mbox_controller` (mailbox ハードウェアの抽象化)、`mbox_chan`(channel の抽象化)`mbox_chan_ops`(channel を操作するコールバック関数のコレクション)。

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

## 2.3 メールボックス.c

### 2.3.1 add_to_rbuf

```c
/* 
 * 缓存通道传输的消息。
 * 'msg_count' 记录缓冲消息的数量；
 * 'msg_free' 是下一条将被缓存的消息的 index。
 */
static int add_to_rbuf(struct mbox_chan *chan, void *mssg)
```

&emsp; &emsp; この関数のロジックは次のとおりです。<div align=center>
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

&emsp; &emsp; この関数のロジックは次のとおりです。<div align=center>
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

&emsp; &emsp; この関数のロジックは次のとおりです。<div align=center>
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

&emsp; &emsp; この関数は、`of_parse_phandle_with_args`デバイス ツリーから index 対応要求の channel を取得します。

- `mboxes`ノード内の phandle リスト プロパティ名をポイントします。
- `#mbox-cells`phandle が指すノードに含まれるセルの数を示します。
- `index`phandle リストのインデックスを表し、0 は最初の phandle を表し、1 は 2 番目の phandle を表します。
- `out_args`phandle の引数を格納します。

&emsp; &emsp; たとえば、デバイス ツリーなどです

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

&emsp; &emsp; 次に、キャッシュ カウントのゼロ化、chan の cl、クライアントが channel の client バインディングを要求する、tx_completeの初期化など、チャネル情報の初期化が続きます。  
&emsp; &emsp; この関数のロジックは次のとおりです。<div align=center>
<img src="../zh/images/mailbox/130203_mbox_request_channel.svg" width="500">
</div>

### 2.3.9 mbox_request_channel_byname

&emsp; &emsp; この関数は、name (mbox-names プロパティ) に基づいてデバイス ツリーから対応する mboxes リストを取得し、最後に mbox_request_channel 関数要求チャネルを呼び出します。

### 2.3.10 mbox_free_channel

&emsp; &emsp; チャネル解放関数は、指定されたチャネルのメンバーを空にし、対応するハードウェア レジスタを構成する必要がある場合は、`shutdown`コールバック関数を実装します。

### 2.3.11 mbox_controller_register および mbox_controller_unregister

&emsp; &emsp; 名前が示すように。

# 3 デバイスツリー分析

&emsp; &emsp; 例:

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

## 3.1 コントローラ

&emsp; &emsp; 少`#mbox-cells`なくとも 1 の値を持つプロパティが必要です。 これは、client プロパティ`mboxes` cell の数を示します。

## 3.2 クライアント

&emsp; &emsp; ドライブ `mboxes`チャネルに情報を提供するプロパティが必要です。  
&emsp; &emsp; 省略可能なプロパティ`mbox-names` (はい) の`mboxes`エイリアス。  
&emsp; &emsp; オプションのプロパティ`reg`である mailbox client は、remote と通信するために予約されているメモリの一部です。  

## 3.3 プロパティの使用方法

&emsp; &emsp; `mbox-cells`、`mboxes`、`mbox-names`3つの属性は、チャネルを適用するときに使用されます。

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

&emsp; &emsp; ここでは、チャネル番号として使用するか、ドライバ開発者の裁量で、ハードウェア固有の情報を追加できます。

# 4 ドライバの実装

- dts 構成
&emsp; &emsp; 上記のデバイス ツリーの例を参照してください。
- controller
&emsp;&emsp;参考`/drivers/mailbox/canaan-mailbox.c`
- client
&emsp;&emsp;参考`/drivers/mailbox/canaan_mbox_client.c`
- ユーザー空間プログラム
&emsp; &emsp; 参照`k510_buildroot/package/mailbox_demo/src/mailbox_async.c`と`k510_buildroot/package/mailbox_demo/src/mailbox_poll.c`

# 5 demo 使用方法

## 5.1 使用

1. dsp ベア メタル プログラムを読み込みます
ディレクトリに移動`/app/dsp_app_new`し、次`./dsp_app mailbox_demo.bin`の図に示すように、実行コマンドはベア メタル プログラムを dsp にロードします。  
![dsp_load](../zh/images/mailbox/130601_dsp_load.png)  
2. Linux ユーザー空間のテストアプリを実行します
ディレクトリに移動`/app/mailbox_demo`し、`./mailbox_async`次の図に示すようにコマンドを実行します。  
![mailbox_demo](../zh/images/mailbox/130602_mailbox_async.png)  
この demo は、非同期通知を使用して dsp によって送信されたデータを受信します。
3. ディレクトリで`/app/mailbox_demo`、次の図に`./mailbox_poll`示すようにコマンドを実行します。  
![mailbox_demo](../zh/images/mailbox/130602_mailbox_poll.png)
この demo は、poll を使用して 500 ms をブロックして、dsp によって送信されたデータを受信します。 データは 4 秒ごとに送信され、2 秒ごとに読み取られるため、2 秒ごとに、読み取りの成功と読み取りの失敗がインターリーブされ、ブロックされた読み取りが成功します。

## 5.2 コードをテストします

&emsp; &emsp; dsp ベア メタル プログラムは`k510_buildroot/package/k510_evb_test/src/test/mailbox_demo/main.c`、ユーザー空間テスト コードが合計にある場所にあります`k510_buildroot/package/mailbox_demo/src/mailbox_async.c``k510_buildroot/package/mailbox_demo/src/mailbox_poll.c`。

# 6 既知の問題

&emsp; &emsp; コマンドを初めて実行`./dsp_app mailbox_demo.bin`したときに、dsp プログラムが dsp に焼き込まれなかった場合があります。 この時点で demo を実行すると、送信に失敗する状況が発生します。

**免責事項を翻訳します**  
お客様の便宜のために、カナアンはAI翻訳プログラムを使用してテキストを複数の言語に翻訳し、エラーが含まれている可能性があります。 当社は、提供される翻訳の正確性、信頼性、または適時性を保証するものではありません。 カナアンは、翻訳された情報の正確性または信頼性への依存に起因するいかなる損失または損害についても責任を負いません。 異なる言語翻訳間でコンテンツの違いがある場合は、簡体字中国語版が優先されます。

翻訳エラーや不正確な問題を報告する場合は、メールでお問い合わせください。
