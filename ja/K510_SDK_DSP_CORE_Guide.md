![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 DSP コア ガイド</font>**

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
このドキュメントは、K510 DSP コアの使用に関するガイダンスです。

**<font face="黑体"  size=5>リーダー オブジェクト</font>**

このドキュメント (このガイド) は、主に次の担当者に適用されます。

- ソフトウェア開発者
- テクニカル サポート スタッフ

**<font face="黑体"  size=5>レコードを改訂します</font>**
 <font face="宋体"  size=2>リビジョン レコードには、ドキュメントが更新されるたびに説明が蓄積されます。 ドキュメントの最新バージョンには、以前のすべてのバージョンの更新が含まれています。 </font>

| バージョン番号   | 変更者     | 改訂日 | 修正の説明 |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | システム ソフトウェア グループ | 2022-03-09 |         |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>目録</font>**

[目次]

<div style="page-break-after:always"></div>

# 1 概要

K510チップには3つのプロセッサがあり、そのうちCPU Dual coresはLinuxを実行し、DSPコアはユーザー開発のためにアイドル状態であり、このドキュメントはDSPコアをコプロセッサとしてベアメタルプログラムを実行するためのリファレンスルーチンを提供します。

![](../zh/images/doc_dsp/image-dsp_1.png)

<center> 図 1 k510 ブロック図 </center>

# 1 DSP プログラムがロードされます

 k510_buildroot/package/dsp_app_new ディレクトリの下には、DSP をロードして実行するコードが含まれており、Linux ユーザー空間で実行されます。 dsp_app_newコードは、主に DSP ファームウェアを指定した場所にロードし、DSP の実行を開始するために実装されます。

```c
/*将DSP固件从pDspBinmPath路径下加载到DspRestVector位置。*/
if (kendryte_dsp_load_bin(DspRestVector, pDspBinmPath)) {
    printf("ERR: Load dsp bin file err\n");
    return -1;
} else {
    printf("Load dsp success\n");
}

/*启动DspRestVector位置处的DSP固件运行。*/
if (kendryte_dsp_boot(DspRestVector)) {
    printf("ERR: Boot dsp err\n");
    return -1;
}
```

コンパイルされた実行可能プログラムdsp_app_new、ルート ファイル システム/app/dsp_app_new ディレクトリに格納されます。

# 2 DSP 情報印刷

 k510_buildroot/package/dsp_log ディレクトリの下には、DSP コアに Linux ユーザー空間で実行されている Log 出力があるかどうかを照会するコードがあります。 dsp_log コンパイルされた実行可能プログラムは、ルート ファイル システム/app/dsp_log ディレクトリに格納されます。

dsp_logはデフォルトでバックグラウンドで実行され、そのプロファイルはk510_buildroot/board/canaan/k510/k510_rootfs_skeleton/etc/init.d/rc.sysinit で実行されます

![](../zh/images/doc_dsp/image-dsp_log.png)

# 3 DSPベアメタルデモ

## 3.1 FFT

fft demo プログラムが配置されます`/app/dsp_app_new/fft.bin`。
fft demo プログラムのソースはディレクトリの下に配置`k510_buildroot/package/k510_evb_test/src/test/fft`されます。

/app/dsp_app_new' ディレクトリの下に移動します。

- `dsp_app`: DSP をロードし、dsp を実行するプログラム (Linux ユーザー空間で実行)
- `fft.bin`: DSPベアメタルプログラム

fft プログラムの実行を開始します。

```shell
cd /app/dsp_app_new
./dsp_app fft.bin
```

次のように印刷できます。

![DSP デモ](../zh/images/doc_dsp/demo_dsp.png)

今dsp上で実行されているfirmwareはfftのdemoプログラムです。

## 3.2 simd_umul8

simd_umul8 demo プログラムが表示されます`/app/dsp_app_new/simd_umul8_demo.bin`。
simd_umul8 demo プログラム ソースを`k510_buildroot/package/k510_evb_test/src/test/simd_umul8_demo`ディレクトリの下に配置すると、主な作業は次のようになります

- demo では、2 つの 32 ビットのデータを "乗算" し、各 32 ビットのデータを 4 つの 8 ビット データに分割し、それぞれに乗算して 4 つの 16 ビットの結果を取得し、計算結果が期待どおりであることを確認します。 たとえば、0x05050505 と 0x02020202 を乗算すると、結果は 0x000a000a000a000a になります。
- 期待どおりであれば、情報を印刷`DSP SIMD UMUL8 TEST PASS`します`DSP SIMD UMUL8 TEST FAIL`

demo を実行するメソッド:

```shell
cd /app/dsp_app_new
./dsp_app simd_umul8_demo.bin
```

特定の命令の可来 [Product Documentation - Andes Technology](http://www.andestech.com/en/products-solutions/product-documentation/) ダウンロード AndeStar V5 DSP ISA Extension Specification.PDF (v1.0,2019-03-25),3.172節を参照してください。

## 3.3 DSP スケジューラ API

CPU のパフォーマンスが一部のアプリケーションを満たしていない場合は、DSP に実行される機能の一部を分割して、CPU の負荷を軽減できます。 DSP にはオペレーティング システムがないため、k510_buildroot/package/dsp_scheduler ディレクトリの下にコードを持つタスク スケジューリング マネージャーが実装されています。 DSP で実行されているタスクは静的ライブラリにコンパイルされ、DSP scheduler と事前に静的にリンクされ、ランタイム cpu は mailbox 経由で dsp にメッセージを送信して適切なタスク実行を開始します。

ユーザーはタスクを登録するときに優先順位を定義でき、DSP scheduler は優先順位に基づいてタスクをスケジュールします。 タスク実行インターフェイス run 関数の戻り値は、ユーザーがタスクの実行回数を自分で決定できるように、RUN_ONCEかCONTINUE_RUNかを決定します。

cpu が Linux mailbox フレームワークを介して dsp にメッセージを送信する方法については、ドキュメントK510_Mailbox_Developer_Guidesの該当する説明を参照してください。 参照は、k510_buildroot/package/k510_evb_test/src/test/mailbox_demo/cpu2dsp_task_demo.c で実装されます

### 3.3.1 ヘッダー ファイルの説明

1. k510_buildroot/パッケージ/dsp_scheduler/src/dsp_tasks.h

    cpu上で実行されるプログラムは、cpuとdsp間のメッセージの種類と構造を定義するincludeヘッダーファイルを必要とし、システムメッセージ通信はQ&A方式を採用し、CPUはdspがメッセージを送信した後、dspが処理されたことを示す同じメッセージを送信するまで待つ必要があります。 ユーザー メッセージは、必要に応じてメカニズムを自分で定義できます。 メッセージの意味は次のとおりです。

    - DSP_TASK_ENABLE

    対応するタスクが実行され始め、このメッセージは dsp のタスク印刷デバッグ情報のメモリ アドレスに従うことができます

    - DSP_TASK_DISABLE

    対応するタスクの実行が停止します

    - DSP_TASK_PRINT_INFO

    登録されているすべてのタスク情報を印刷します

    - DSP_TASK_USER_MSG

    ユーザーが必要に応じてメッセージ キューとメッセージ通信メカニズムを自分で設計できるメモリ アドレスに続く、カスタマイズされたタスク メッセージ

    ```c
    typedef enum
    {
        DSP_TASK_ENABLE = 0x10000000,
        DSP_TASK_DISABLE,
        DSP_TASK_PRINT_INFO,
        DSP_TASK_USER_MSG,
        MAX_NUM_DSP_TASK_MSG
    } DspTaskMsg;

    typedef struct tDSP_MESSAGE
    {
        DspTaskMsg      msgId;         /**<Message ID*/
        unsigned int    msg_phyAddr;   /**<Message content, shared memory physical address
                                        when msgId is DSP_TASK_ENABLE, it is
                                        buffer address for print log
                                    */
        unsigned int    len;           /**<Length of message*/
    } DSP_MESSAGE;
    ```

2. k510_buildroot/package/dsp_scheduler/src/scheduler.h
    dsp で実行されているプログラムには、include このヘッダー ファイルが必要です

### 3.3.2 API 関数の説明

#### 3.3.2.1 SCHE_TaskRegister

【説明】

タスクを登録します。 DSP には最大 8 つのタスクが登録され、各タスクは mailbox チャネルと CPU を介して通信します。 Task 0 に対応する mailbox チャネル番号は 0 で、cpu mailbox のMBOX_CHAN_0_TXに対応DSP_TASK_0_CH。

以下のようなtask構造体を実現した

```c
DSP_TASK dsp_sample_task = {
    .name             = "sample task",
    .priority         = 2,
    .init             = sample_task_init,
    .deinit           = sample_task_deinit,
    .run              = sample_task_run,
    .rev_callback     = sample_task_callback,
    .ack_callback     = sample_ack_callback,
};
```

k510_buildroot/package/dsp_scheduler/alltasks.c で、次のコードでタスク登録を行います。

```c
{
    extern DSP_TASK dsp_sample_task;
    SCHE_TaskRegister(&dsp_sample_task, DSP_TASK_0_CH);
}
```

【文法】

```c
ScheStatus SCHE_TaskRegister(DSP_TASK *task, DspTaskChannel ch)
```

【パラメータ】

```c
typedef enum
{
    DSP_TASK_0_CH = 0,
    DSP_TASK_1_CH,
    DSP_TASK_2_CH,
    DSP_TASK_3_CH,
    DSP_TASK_4_CH,
    DSP_TASK_5_CH,
    DSP_TASK_6_CH,
    DSP_TASK_7_CH,
    MAX_NUM_DSP_TASKS
} DspTaskChannel;

typedef enum
{
    SCHE_RUN_ONCE = 0,
    SCHE_CONTINUE_RUN = 1,
}ScheRunType;

typedef struct DSP_TASK
{
    /**task name*/
    char *name;

    /**priority 0 to 255, 0 is the highest*/
    int priority;

    /**init function
       return task context pointer
    */
    void *(*init)();

    /**deinit function*/
    void (*deinit)(void *arg);

    /**task process function
       return 0 means run once
       return 1 means conitune run
    */
    ScheRunType (*run)(void *arg);

    /**ISR callback
       for receiving msg from cpu
    */
    void (*rev_callback)(void *arg);

    /**ISR callback
       for ack msg from cpu after dsp send msg to cpu
    */
    void (*ack_callback)(void *arg);
} DSP_TASK;
```

#### 3.2.2 SCHE_SendMessage

【説明】

dsp のタスクは、このインターフェイスを介して CPU にメッセージを送信します

```c
ScheStatus SCHE_SendMessage(DSP_MESSAGE *pMsg, DspTaskChannel ch)
```

【パラメータ】

セクション 3.3.1 の説明を参照してください

#### 3.2.3 SCHE_GetMessage

【説明】

dsp のタスクは、このインターフェイスを介して CPU からメッセージを受信します

```c
ScheStatus SCHE_GetMessage(DSP_MESSAGE *pMsg, DspTaskChannel ch)
```

【パラメータ】

セクション 3.3.1 の説明を参照してください

### 3.3.3 DSP Scheduler アプリケーションの実列

次のようなコマンドを実行して、タスク ディスパッチ ベア メタル プログラム dsp scheduler をロードします。

```shell
cd /app/dsp_app_new
./dsp_app ../dsp_scheduler/scheduler.bin
```

シェル ウィンドウには、dsp scheduler の読み込みが成功したことを示す次のようなログが表示されます。

```text
dsp schduler start
dsp schduler: register sample task successful, ch 0
dsp schduler: register audio3a task successful, ch 1
```

/app/mailbox_demoディレクトリに入り、次のようなコマンドを入力すると、cpuはdspにタスクを開始するコマンドを送信し、データを処理する要求を送信し、dsp処理の完了はCPUにメッセージを送信し、ループし続けます。

```shell
cd /app/mailbox_demo
/app/mailbox_demo/cpu2dsp_task_demo
```

dsp が cpu によって指定されたタスクを正常に実行したことを示す log が表示されます。

```shell
[root@canaan ~/data ]$ ./cpu2dsp_task_demo
task 0 message buffer: vaddr 0x18000, phyAddr 0x1fdff000, size 4096
task 0 print buffer: vaddr 0x18000, phyAddr 0x1fdfd000, size 4096
task 0 src buffer: vaddr 0x14d000, phyAddr 0x1fdfb000, size 4096
task 0 dst buffer: vaddr 0x14e000, phyAddr 0x1fdf9000, size 4096
printc_init>log_id 0, cur_addr 0x1fdfd000, log_len 4096
dsp process_command>task 0: init done
task 0 is enabled
cpu send PROCESS_START
cpu receive PROCESS_END
cpu send PROCESS_START
cpu receive PROCESS_END
cpu send PROCESS_START
cpu receive PROCESS_END
cpu send PROCESS_START
cpu receive PROCESS_END
cpu send PROCESS_START
cpu receive PROCESS_END
cpu send PROCESS_START
cpu receive PROCESS_END
cpu send PROCESS_START
cpu receive PROCESS_END
^C //按下ctrl+c后
cpu send PROCESS_START
cpu receive PROCESS_END
dsp process_command>task 0: deinit done
task 0 is disabled
exit: task0 is disabled
cpu2dsp_task_demo: exit successful
```

**免責事項を翻訳します**  
お客様の便宜のために、カナアンはAI翻訳プログラムを使用してテキストを複数の言語に翻訳し、エラーが含まれている可能性があります。 当社は、提供される翻訳の正確性、信頼性、または適時性を保証するものではありません。 カナアンは、翻訳された情報の正確性または信頼性への依存に起因するいかなる損失または損害についても責任を負いません。 異なる言語翻訳間でコンテンツの違いがある場合は、簡体字中国語版が優先されます。

翻訳エラーや不正確な問題を報告する場合は、メールでお問い合わせください。
