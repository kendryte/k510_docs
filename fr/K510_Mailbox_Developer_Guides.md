![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 Mailbox Guide du développeur</font>**

<font face="黑体"  size=3>Version du document : V1.0.0</font>

<font face="黑体"  size=3>Date de publication : 2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Démenti**</font>
Les produits, services ou fonctionnalités que vous achetez sont soumis aux contrats commerciaux et aux conditions de Beijing Canaan Jiesi Information Technology Co., Ltd. (« la Société », les mêmes ci-après), et tout ou partie des produits, services ou fonctionnalités décrits dans ce document peuvent ne pas être dans le cadre de votre achat ou de votre utilisation. Sauf accord contraire dans le contrat, la Société décline toute représentation ou garantie, expresse ou implicite, quant à l'exactitude, la fiabilité, l'exhaustivité, le marketing, l'objectif spécifique et la non-agression de toute représentation, information ou contenu de ce document. Sauf convention contraire, le présent document est fourni à titre indicatif à titre indicatif d'utilisation seulement.
En raison de mises à niveau de la version du produit ou d'autres raisons, le contenu de ce document peut être mis à jour ou modifié de temps à autre sans préavis. 

**<font face="黑体"  size=3>Avis sur les marques de commerce</font>**

«  »<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, l'icône « Canaan », Canaan et d'autres marques de commerce de Canaan et d'autres marques de commerce de Canaan sont des marques de commerce de Beijing Canaan Jiesi Information Technology Co., Ltd. Toutes les autres marques de commerce ou marques déposées qui peuvent être mentionnées dans ce document sont la propriété de leurs propriétaires respectifs. 

**<font face="黑体"  size=3>Copyright ©2022 Beijing Canaan Jiesi Information Technology Co., Ltd</font>**
Ce document ne s'applique qu'au développement et à la conception de la plate-forme K510, sans l'autorisation écrite de la société, aucune unité ou individu ne peut diffuser une partie ou la totalité du contenu de ce document sous quelque forme que ce soit. 

**<font face="黑体"  size=3>Beijing Canaan Jiesi Information Technology Co., Ltd</font>**
URL: canaan-creative.com
Demandes de renseignements des entreprises : salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# préface
**<font face="黑体"  size=5>Objet </font>**du document
Ce document est un document de développement pour le pilote de boîte aux lettres K510. 

**<font face="黑体"  size=5>Objets de lecture</font>**

Les principales personnes auxquelles ce document (ce guide) s'applique :

- Développeurs de logiciels
- Personnel de soutien technique

**<font face="黑体"  size=5>Historique des révisions</font>**
 <font face="宋体"  size=2>L'historique des révisions accumule une description de chaque mise à jour de document. La dernière version du document contient des mises à jour pour toutes les versions précédentes. </font>

| Le numéro de version   | Modifié par     | Date de révision | Notes de révision |
|  :-----  |-------   |  ------  |  ------  |
| Version 1.0.0 | Groupes de logiciels système | 2022-03-09 | Lancement du SDK V1.5 |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenu</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Analyse du cadre

## 1.1 client、controller 与 framework

&emsp; &emsp; L'infrastructure de boîte aux lettres est utilisée pour gérer la communication entre plusieurs processeurs. Le framework est divisé en contrôleur et client.  
&emsp; &emsp; Le contrôleur est un pilote qui manipule directement la boîte aux lettres matérielle. Il fait fonctionner les registres matériels directement vers le bas, complétant la communication avec la télécommande en envoyant et en recevant des interruptions (si elles sont prises en charge par le matériel); Jusqu'à l'interface fournie par le framework pour compléter la communication avec le pilote client.
&emsp; &emsp; Le client est le consommateur du contrôleur, communiquant avec le contrôleur vers le bas, complétant les applications de canal, la préparation des données et d'autres fonctions; Fournit des interfaces pour la manipulation de l'espace utilisateur.  
&emsp; &emsp; Le framework de boîte aux lettres est responsable de l'interface entre le contrôleur et le client, la documentation du noyau dit: « Le pilote client et contrôleur peut être très dépendant de la plate-forme spécifique, par conséquent, le pilote client ne peut pas être partagé entre plusieurs plates-formes », donc dans`/drivers/mailbox` le répertoire, seul le pilote sur le contrôleur peut être trouvé et ne peut pas trouver le pilote client, un seul test peut être trouvé Pilote `mailbox-test.c`client du contrôleur. La façon dont le pilote client échange des données avec l'espace utilisateur dépend également du développeur du pilote lui-même.  
&emsp; &emsp; Le diagramme suivant est le cadre de base pour deux enregistrements de pilotes : 

<div align=center>
<img src="../zh/images/mailbox/130101_frame_00.svg" width="1400">
</div>  

## 1.2 Structures de données

&emsp; &emsp; La structure de données du contrôleur et du client est illustrée dans la figure suivante :<div align=center>
<img src="../zh/images/mailbox/130102_data_structure.svg" width="1400">
</div>

&emsp; &emsp; L'infrastructure utilise `struct mbox_controller`des contrôleurs de boîte aux lettres abstraits, `struct mbox_chan`des canaux abstraits et des collections de fonctions `struct mbox_chan_ops`pour manipuler les canaux. Les trois structures de données ci-dessus sont destinées aux contrôleurs. Le framework utilise `struct mbox_client`des clients abstraits, qui sont spécifiques au client.  
&emsp; &emsp; En plus de cela, nous devons définir notre propre structure de périphérique pour nos appareils et lecteurs, comme le montre la figure ci-dessus. La connexion entre le client et le contrôleur se`mbox_request_channel` fait dans la fonction lors de la demande d'un canal dans le client, et un canal est lié à une`struct mbox_client` structure. 

## 1.3 Flux d'appels de fonction

&emsp; &emsp; Le flux d'appel de fonction est illustré dans la figure suivante :<div align=center>
<img src="../zh/images/mailbox/130103_frame_callback.svg" width="1400">
</div>  

&emsp; &emsp; L'espace utilisateur et la livraison de données pilotée par le client utilisent ioctl plus des notifications asynchrones, qui sont déterminées par les développeurs de pilotes eux-mêmes et n'appartiennent pas au framework.  
&emsp; &emsp; Nous avons créé un nœud de périphérique dans le pilote client`/dev/mailbox-client` à travers lequel l'espace utilisateur lit et envoie des données. 8 canaux d'émission, 8 canaux de réception. 

### 1.3.1 Envoi de flux de données

&emsp; &emsp; Comme le montre la figure ci-dessus :

1. Le fichier de manipulation de l'espace utilisateur gère l'envoi de données;
2. Entrez dans la fonction ioctl pilotée par le client, qui copie les données de l'espace utilisateur dans l'espace du noyau et appelle éventuellement la`mbox_send_message` fonction ; 
3. Le processus de traitement spécifique de cette fonction peut être vu dans l'analyse de code des chapitres suivants, qui appelle principalement deux fonctions de rappel: l'implémentation pilotée par le client`tx_prepare` et l'implémentation pilotée par le contrôleur`send_data`. Regardez les noms pour savoir ce que font ces deux fonctions. Il convient de noter que certaines boîtes aux lettres matérielles ont des registres de transmission de données matérielles, de sorte qu'à ce stade, la transmission de données peut être`send_data` effectuée au milieu; Certains matériels n'ont pas de registres de transmission de données matérielles, puis la transmission de données réelle peut également y être`tx_prepare` effectuée et `send_data`le rôle devient une simple **notification d'interruption de déclenchement au processeur distant**; 
4. Lorsque le processeur distant reçoit l'interruption et reçoit les données, il doit répondre au contrôleur avec une interruption indiquant que Tx est terminé;
5. Après avoir reçu le Tx ACK, le gestionnaire d'interruptions enregistré par le contrôleur doit être appelé`mbox_chan_txdone` pour informer la couche supérieure que le transfert a été reçu à distance ; 
6. `mbox_chan_txdone`Informez le client que le `tx_done`transfert est effectué par le biais de l'inscription du client. Le client décide du traitement ultérieur et les`tx_done` paramètres enregistrent l'état du transfert de données. 

### 1.3.1 Processus de réception des données

&emsp; &emsp; Comme le montre la figure ci-dessus :

1. Interruptions de l'envoi de données par le processeur distant au responsable du traitement;
2. Après avoir reçu l'interruption, l'appel du gestionnaire d'interruption enregistré par le contrôleur `mbox_chan_received_data`informe la couche supérieure de recevoir des données provenant de l'extrémité et de répondre à l'ACK Rx distant. 
3. `mbox_chan_received_data`Appeler le client enregistré`rx_callback` ; 
4. `rx_callback`lit les données de l'adresse spécifiée dans l'arborescence des périphériques, puis avertit l'espace utilisateur à l'aide de notifications asynchrones ;
5. Le gestionnaire asynchrone de l'espace utilisateur qui appelle ioctl lit les données du canal de réception.

# 2 Analyse du code du framework

## 2.1 mailbox_controller.h

&emsp; &emsp; Défini `mbox_controller`(abstraction du matériel de boîte aux lettres),`mbox_chan` (abstraction du canal) `mbox_chan_ops`(collection de fonctions de rappel qui manipulent les canaux). 

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

&emsp; &emsp; La logique de fonction est la suivante :<div align=center>
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

&emsp; &emsp; La logique de fonction est la suivante :<div align=center>
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

&emsp; &emsp; La logique de fonction est la suivante :<div align=center>
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

&emsp; &emsp; Cette fonction, en passant, `of_parse_phandle_with_args`obtient le canal de l'index demandé à partir de l'arborescence des périphériques. 

- `mboxes`Pointe vers le nom de la propriété de liste phandle dans le nœud ;
- `#mbox-cells`Indique le nombre de cellules contenues dans le nœud pointé par le phandle ;
- `index`Représente l'index de la liste phandle, 0 représentant le premier phandle et 1 représentant le second phandle ;
- `out_args`Stocke les paramètres dans le phandle.

&emsp; &emsp; Par exemple, dans notre arborescence d'appareils

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

&emsp; &emsp; Ceci est suivi par l'initialisation des informations de canal, y compris la mise à zéro du nombre de cache, le cl de chan et la liaison client du client demandant le canal, l'initialisation du tx_complete, etc.  
&emsp; &emsp; La logique de fonction est la suivante :<div align=center>
<img src="../zh/images/mailbox/130203_mbox_request_channel.svg" width="500">
</div>

### 2.3.9 mbox_request_channel_byname

&emsp; &emsp; Cette fonction obtient la liste mboxes correspondante à partir de l'arborescence des périphériques en fonction de l'attribut name(mbox-names), et appelle enfin la fonction mbox_request_channel pour demander un canal.

### 2.3.10 mbox_free_channel

&emsp; &emsp; La fonction de libération de canal implémente une fonction de rappel qui videra les membres du canal spécifié et implémentera la fonction de rappel si le registre matériel correspondant doit être configuré`shutdown`. 

### 2.3.11 mbox_controller_register et mbox_controller_unregister

&emsp; &emsp; Le nom implique.

# 3 Analyse de l'arborescence des périphériques

&emsp; &emsp; Exemple:

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

## 3.1 responsable du traitement

&emsp; &emsp; Il doit y avoir un attribut`#mbox-cells` avec une valeur d'au moins 1. Il indique le`mboxes` nombre de cellules pour l'attribut client. 

## 3.2 Client

&emsp; &emsp; Il doit y avoir une propriété `mboxes`qui fournit des informations au canal du lecteur.  
&emsp; &emsp; Attribut facultatif`mbox-names`, alias yes`mboxes`.  
&emsp; &emsp; Si vous `reg`le souhaitez, le client de boîte aux lettres communique avec la télécommande tout en conservant une partie de la mémoire.  

## 3.3 Comment utiliser la propriété

&emsp; &emsp; `mbox-cells`Les`mboxes` `mbox-names`trois propriétés sont utilisées lors de l'application de canaux. 

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

&emsp; &emsp; Ici, nous l'utilisons comme numéro de canal, ou nous pouvons ajouter d'autres informations spécifiques au matériel, l'explication spécifique dépend du développeur du pilote.

# 4 Mise en œuvre des pilotes

- Configuration DTS
&emsp; &emsp; Voir l'exemple d'arborescence des périphériques ci-dessus.
- contrôleur
&emsp;&emsp;référence`/drivers/mailbox/canaan-mailbox.c`
- client
&emsp;&emsp;référence`/drivers/mailbox/canaan_mbox_client.c`
- Programmes d'espace utilisateur
&emsp; &emsp; Référence`k510_buildroot/package/mailbox_demo/src/mailbox_async.c` et`k510_buildroot/package/mailbox_demo/src/mailbox_poll.c`

# 5 Comment utiliser la démo

## 5.1 Utilisation

1. Charger le programme bare metal dsp
Accédez au répertoire`/app/dsp_app_new` et exécutez la commande `./dsp_app mailbox_demo.bin`pour charger le programme bare metal dans le dsp, comme illustré dans la figure suivante :  
![dsp_load](../zh/images/mailbox/130601_dsp_load.png)  
2. Exécuter l'application de test de l'espace utilisateur Linux
Entrez dans le répertoire`/app/mailbox_demo` et exécutez la commande`./mailbox_async`, comme illustré dans la figure suivante :  
![](../zh/images/mailbox/130602_mailbox_async.png)mailbox_demo  
Cette démo utilise des notifications asynchrones pour recevoir les données envoyées par le dsp. 
3. Dans le répertoire`/app/mailbox_demo`, exécutez la commande`./mailbox_poll`, comme illustré dans la figure suivante :  
![](../zh/images/mailbox/130602_mailbox_poll.png)mailbox_demo
Cette démo utilise le blocage des sondages pendant 500 ms pour recevoir les données envoyées par le dsp. Nous envoyons des données toutes les 4 secondes et lisons les données toutes les 2 secondes, de sorte que nous pouvons voir que toutes les 2 secondes, le succès de la lecture est échelonné avec l'échec de la lecture et la lecture de blocage réussit. 

## 5.2 Mise à l'essai du Code

&emsp; &emsp; Le programme bare metal dsp est situé `k510_buildroot/package/k510_evb_test/src/test/mailbox_demo/main.c`au milieu et le code de test de l'espace utilisateur est situé dans`k510_buildroot/package/mailbox_demo/src/mailbox_async.c` et`k510_buildroot/package/mailbox_demo/src/mailbox_poll.c`. 

# 6 Problèmes connus

&emsp; &emsp; Parfois, le `./dsp_app mailbox_demo.bin`programme dsp n'est pas gravé dans le dsp la première fois que la commande est exécutée. L'exécution de la démo à ce stade entraînera un échec d'envoi. 

**Clause de non-responsabilité en matière de**  
Pour la commodité des clients, Canaan utilise un traducteur IA pour traduire du texte en plusieurs langues, ce qui peut contenir des erreurs. Nous ne garantissons pas l'exactitude, la fiabilité ou l'actualité des traductions fournies. Canaan ne sera pas responsable de toute perte ou dommage causé par la confiance accordée à l'exactitude ou à la fiabilité des informations traduites. S'il existe une différence de contenu entre les traductions dans différentes langues, la version simplifiée en chinois prévaudra. 

Si vous souhaitez signaler une erreur de traduction ou une inexactitude, n'hésitez pas à nous contacter par courrier.