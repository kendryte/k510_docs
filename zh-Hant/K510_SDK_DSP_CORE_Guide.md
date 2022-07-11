![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 數字信號處理器核心指南</font>**

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
本文檔為K510 DSP核使用指導說明。

**<font face="黑体"  size=5>讀者物件</font>**

本文檔（本指南）主要適用的人員：

- 軟體開發人員
- 技術支持人員

**<font face="黑体"  size=5>修訂記錄</font>**
 <font face="宋体"  size=2>修訂記錄累積了每次文檔更新的說明。 最新版本的文件包含以前所有版本的更新內容。 </font>

| 版本號   | 修改者     | 修訂日期 | 修訂說明 |
|  :-----  |-------   |  ------  |  ------  |
| 1.0.0 版 | 系統軟體組 | 2022-03-09 |         |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>目 錄</font>**

[目錄]

<div style="page-break-after:always"></div>

# 1 概述

K510晶元中一共有三個處理器，其中CPU Dual cores運行Linux，DSP核空閒留待用戶開發使用，本文檔提供了DSP核作為協處理器運行裸機程序的參考例程。

![](../zh/images/doc_dsp/image-dsp_1.png)

<center> 圖1 k510框圖 </center>

# 1 DSP 程式載入

 k510_buildroot/package/dsp_app_new 目錄下，是載入DSP並使之運行的代碼，該代碼運行於Linux用戶空間。 dsp_app_new代碼主要實現載入DSP韌體到指定位置，並啟動DSP開始執行，其主要的代碼如下：

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

dsp_app_new編譯后的可執行程式將存放在根文件系統/app/dsp_app_new目錄下。

# 2 DSP 資訊列印

 k510_buildroot/package/dsp_log 目錄下，是查詢是否DSP核是否有Log輸出的代碼，該代碼運行於Linux用戶空間。 dsp_log 編譯后的可執行程式將存放在根文件系統/app/dsp_log目錄下。

開機后，dsp_log預設將在後台執行，其配置檔在：k510_buildroot/board/canaan/k510/k510_rootfs_skeleton/etc/init.d/rc.sysinit

![](../zh/images/doc_dsp/image-dsp_log.png)

# 3 DSP 裸機Demo

## 3.1 英尺

fft demo 程式位於`/app/dsp_app_new/fft.bin`。
fft demo 程式源碼放在`k510_buildroot/package/k510_evb_test/src/test/fft`目錄下。

進入 /app/dsp_app_new'目錄下：

- `dsp_app`：載入DSP並使得dsp運行的程式（運行於Linux 使用者空間）
- `fft.bin`： DSP 裸機程式

啟動 fft 程式執行：

```shell
cd /app/dsp_app_new
./dsp_app fft.bin
```

可以看到如下列印：

![數位信號處理器演示](../zh/images/doc_dsp/demo_dsp.png)

現在dsp上運行的firmware是fft的demo程式。

## 3.2 simd_umul8

simd_umul8 demo 程式位於`/app/dsp_app_new/simd_umul8_demo.bin`。
simd_umul8 demo 程式源碼放在`k510_buildroot/package/k510_evb_test/src/test/simd_umul8_demo`目錄下，所做的主要工作如下：

- 在 demo 中讓兩個 32 位的數據“相乘”，即將每個 32 位的數據分成 4 個 8 位的數據，然後分別對應相乘，得到 4 個 16 位的結果，檢查計算結果是否符合預期。 例如，0x05050505 與 0x02020202 「相乘」后的結果為 0x000a000a000a000a。
- 如果符合預期，列印信息`DSP SIMD UMUL8 TEST PASS`，否則列印資訊`DSP SIMD UMUL8 TEST FAIL`.

執行 demo 的方法：

```shell
cd /app/dsp_app_new
./dsp_app simd_umul8_demo.bin
```

具體指令的可到 [Product Documentation - Andes Technology](http://www.andestech.com/en/products-solutions/product-documentation/) 下載 AndeStar V5 DSP ISA Extension Specification.PDF（v1.0，2019-03-25），查看第 3.172 節。

## 3.3 DSP調度程式介面

當cpu性能不能滿足一些應用的時候，可以分割一部分功能運行到DSP上，以減輕cpu負載。 DSP上沒有作業系統，因此實現了一個任務調度管理器，代碼在k510_buildroot/package/dsp_scheduler目錄下。 在DSP上運行的任務編譯成靜態庫，預先和DSP scheduler靜態連結在一起，運行時cpu通過mailbox向dsp發送消息啟動相應的任務運行。

用戶在註冊任務的時候可以定義優先順序，DSP scheduler根據優先順序進行任務調度。 任務運行介面run函數的返回值決定是RUN_ONCE還是CONTINUE_RUN，這樣使用者能自己決定任務的執行次數。

cpu如何通過linux mailbox框架給dsp發消息，請參考文檔K510_Mailbox_Developer_Guides里的相應介紹。 參考實現在k510_buildroot/package/k510_evb_test/src/test/mailbox_demo/cpu2dsp_task_demo.c

### 3.3.1 頭文件說明

1. k510_buildroot/package/dsp_scheduler/src/dsp_tasks.h

    cpu上運行的程式需要include此頭檔，此頭檔里定義了cpu和dsp之間的消息類型和結構，系統消息通信採用一問一答的方式，cpu發完消息后要等到dsp發來的相同消息表明dsp處理完畢。 使用者消息可以根據需要自行定義機制。 消息含義如下：

    - DSP_TASK_ENABLE

    相應的任務開始運行，此消息可以跟隨一個記憶體位址，用於dsp上任務列印調試資訊

    - DSP_TASK_DISABLE

    相應的任務停止運行

    - DSP_TASK_PRINT_INFO

    列印所有已經註冊的任務資訊

    - DSP_TASK_USER_MSG

    使用者自定義的任務消息，此消息跟隨一個記憶體位址，用戶可根據需要自行設計消息佇列和消息通信機制

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
    dsp上運行的程式需要include此頭檔

### 3.3.2 API函數說明

#### 3.3.2.1 SCHE_TaskRegister

【描述】

註冊一個任務。 DSP上最多能註冊8個任務，每個任務通過一個mailbox通道和cpu進行通信。 Task 0對應的mailbox通道號是0，DSP_TASK_0_CH對應於cpu mailbox的MBOX_CHAN_0_TX，以此類推。

實現如下的task結構體

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

在k510_buildroot/package/dsp_scheduler/alltasks.c里，進行任務註冊，代碼如下：

```c
{
    extern DSP_TASK dsp_sample_task;
    SCHE_TaskRegister(&dsp_sample_task, DSP_TASK_0_CH);
}
```

【語法】

```c
ScheStatus SCHE_TaskRegister(DSP_TASK *task, DspTaskChannel ch)
```

【參數】

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

【描述】

dsp上的任務通過此介面給cpu發消息

```c
ScheStatus SCHE_SendMessage(DSP_MESSAGE *pMsg, DspTaskChannel ch)
```

【參數】

參見章節3.3.1里的說明

#### 3.2.3 SCHE_GetMessage

【描述】

dsp上的任務通過此介面接收來自cpu的消息

```c
ScheStatus SCHE_GetMessage(DSP_MESSAGE *pMsg, DspTaskChannel ch)
```

【參數】

參見章節3.3.1里的說明

### 3.3.3 DSP Scheduler應用實列

執行如下命令載入任務調度裸機程式dsp scheduler：

```shell
cd /app/dsp_app_new
./dsp_app ../dsp_scheduler/scheduler.bin
```

在shell視窗能看到如下log，表明dsp scheduler載入成功。

```text
dsp schduler start
dsp schduler: register sample task successful, ch 0
dsp schduler: register audio3a task successful, ch 1
```

進入/app/mailbox_demo目錄，輸入如下命令，cpu會發命令給dsp啟動一個任務，並且發送處理數據的請求，dsp處理完成會發消息通知cpu，這樣一直迴圈。

```shell
cd /app/mailbox_demo
/app/mailbox_demo/cpu2dsp_task_demo
```

看到如下log，說明dsp運行cpu指定的任務成功。

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

**翻譯免責聲明**  
為方便客戶，Canaan 使用 AI 翻譯程式將文字翻譯為多種語言，它可能包含錯誤。 我們不保證提供的譯文的準確性、可靠性或時效性。 對於因依賴已翻譯信息的準確性或可靠性而造成的任何損失或損害，Canaan 概不負責。 如果不同語言翻譯之間存在內容差異，以簡體中文版本為準。

如果您要報告翻譯錯誤或不準確的問題，歡迎通過郵件與我們聯繫。
