![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 DSP CORE Guide</font>**

<font face="黑体"  size=3>文档版本：V1.0.0</font>

<font face="黑体"  size=3>发布日期：2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**免责声明**</font>
您购买的产品、服务或特性等应受北京嘉楠捷思信息技术有限公司（“本公司”，下同）商业合同和条款的约束，本文档中描述的全部或部分产品、服务或特性可能不在您的购买或使用范围之内。除非合同另有约定，本公司不对本文档的任何陈述、信息、内容的准确性、可靠性、完整性、营销型、特定目的性和非侵略性提供任何明示或默示的声明或保证。除非另有约定，本文档仅作为使用指导的参考。
由于产品版本升级或其他原因，本文档内容将可能在未经任何通知的情况下，不定期进行更新或修改。

**<font face="黑体"  size=3>商标声明</font>**

“<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />”、“Canaan”图标、嘉楠和嘉楠其他商标均为北京嘉楠捷思信息技术有限公司的商标。本文档可能提及的其他所有商标或注册商标，由各自的所有人拥有。

**<font face="黑体"  size=3>版权所有©2022北京嘉楠捷思信息技术有限公司</font>**
本文档仅适用K510平台开发设计，非经本公司书面许可，任何单位和个人不得以任何形式对本文档的部分或全部内容传播。

**<font face="黑体"  size=3>北京嘉楠捷思信息技术有限公司</font>**
网址：canaan-creative.com
商务垂询：salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# 前言
**<font face="黑体"  size=5>文档目的</font>**
本文档为K510 DSP核使用指导说明。

**<font face="黑体"  size=5>读者对象</font>**

本文档（本指南）主要适用的人员：

- 软件开发人员
- 技术支持人员

**<font face="黑体"  size=5>修订记录</font>**
<font face="宋体"  size=2>修订记录累积了每次文档更新的说明。最新版本的文档包含以前所有版本的更新内容。</font>

| 版本号   | 修改者     | 修订日期 | 修订说明 |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | 系统软件组 | 2022-03-09 |         |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>目 录</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1  概述

K510芯片中一共有三个处理器，其中CPU Dual cores运行Linux，DSP核空闲留待用户开发使用，本文档提供了DSP核作为协处理器运行裸机程序的参考例程。

![](../zh/images/doc_dsp/image-dsp_1.png)

<center> 图1 k510框图 </center>

# 1 DSP 程序加载

 k510_buildroot/package/dsp_app_new 目录下，是加载DSP并使之运行的代码，该代码运行于Linux用户空间。dsp_app_new代码主要实现加载DSP固件到指定位置，并启动DSP开始执行，其主要的代码如下：

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

dsp_app_new编译后的可执行程序将存放在根文件系统/app/dsp_app_new目录下。

# 2 DSP 信息打印

 k510_buildroot/package/dsp_log 目录下，是查询是否DSP核是否有Log输出的代码，该代码运行于 Linux用户空间。dsp_log 编译后的可执行程序将存放在根文件系统/app/dsp_log目录下。

开机后，dsp_log默认将在后台执行，其配置文件在：k510_buildroot/board/canaan/k510/k510_rootfs_skeleton/etc/init.d/rc.sysinit

![](../zh/images/doc_dsp/image-dsp_log.png)

# 3 DSP 裸机Demo

## 3.1 fft

fft demo 程序位于`/app/dsp_app_new/fft.bin`。
fft demo 程序源码放在`k510_buildroot/package/k510_evb_test/src/test/fft`目录下。

进入 /app/dsp_app_new`目录下：

- `dsp_app`：加载DSP并使得dsp运行的程序（运行于Linux 用户空间）
- `fft.bin`:  DSP 裸机程序

启动 fft 程序运行：

```shell
cd /app/dsp_app_new
./dsp_app fft.bin
```

可以看到如下打印：

![DSP Demo](../zh/images/doc_dsp/demo_dsp.png)

现在dsp上运行的firmware是fft的demo程序。

## 3.2 simd_umul8

simd_umul8 demo 程序位于`/app/dsp_app_new/simd_umul8_demo.bin`。
simd_umul8 demo 程序源码放在`k510_buildroot/package/k510_evb_test/src/test/simd_umul8_demo`目录下，所做的主要工作如下：

- 在 demo 中让两个 32 位的数据"相乘”，即将每个 32 位的数据分成 4 个 8 位的数据，然后分别对应相乘，得到 4 个 16 位的结果，检查计算结果是否符合预期。例如，0x05050505 与 0x02020202 “相乘”后的结果为 0x000a000a000a000a。
- 如果符合预期，打印信息`DSP SIMD UMUL8 TEST PASS`，否则打印信息`DSP SIMD UMUL8 TEST FAIL`.

运行 demo 的方法：

```shell
cd /app/dsp_app_new
./dsp_app simd_umul8_demo.bin
```

具体指令的可到 [Product Documentation - Andes Technology](http://www.andestech.com/en/products-solutions/product-documentation/) 下载 AndeStar V5 DSP ISA Extension Specification.PDF（v1.0，2019-03-25），查看第 3.172 节。

## 3.3 DSP Scheduler API

当cpu性能不能满足一些应用的时候，可以分割一部分功能运行到DSP上，以减轻cpu负载。DSP上没有操作系统，因此实现了一个任务调度管理器，代码在k510_buildroot/package/dsp_scheduler目录下。在DSP上运行的任务编译成静态库，预先和DSP scheduler静态链接在一起，运行时cpu通过mailbox向dsp发送消息启动相应的任务运行。

用户在注册任务的时候可以定义优先级，DSP scheduler根据优先级进行任务调度。任务运行接口run函数的返回值决定是RUN_ONCE还是CONTINUE_RUN，这样用户能自己决定任务的执行次数。

cpu如何通过linux mailbox框架给dsp发消息，请参考文档K510_Mailbox_Developer_Guides里的相应介绍。参考实现在k510_buildroot/package/k510_evb_test/src/test/mailbox_demo/cpu2dsp_task_demo.c

### 3.3.1 头文件说明

1. k510_buildroot/package/dsp_scheduler/src/dsp_tasks.h

    cpu上运行的程序需要include此头文件，此头文件里定义了cpu和dsp之间的消息类型和结构，系统消息通信采用一问一答的方式，cpu发完消息后要等到dsp发来的相同消息表明dsp处理完毕。用户消息可以根据需要自行定义机制。消息含义如下：

    - DSP_TASK_ENABLE

    相应的任务开始运行，此消息可以跟随一个内存地址，用于dsp上任务打印调试信息

    - DSP_TASK_DISABLE

    相应的任务停止运行

    - DSP_TASK_PRINT_INFO

    打印所有已经注册的任务信息

    - DSP_TASK_USER_MSG

    用户自定义的任务消息，此消息跟随一个内存地址，用户可根据需要自行设计消息队列和消息通信机制

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
    dsp上运行的程序需要include此头文件

### 3.3.2 API函数说明

#### 3.3.2.1 SCHE_TaskRegister

【描述】

注册一个任务。DSP上最多能注册8个任务，每个任务通过一个mailbox通道和cpu进行通信。Task 0对应的mailbox通道号是0，DSP_TASK_0_CH对应于cpu mailbox的MBOX_CHAN_0_TX，以此类推。

实现如下的task结构体

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

在k510_buildroot/package/dsp_scheduler/alltasks.c里，进行任务注册，代码如下：

```c
{
    extern DSP_TASK dsp_sample_task;
    SCHE_TaskRegister(&dsp_sample_task, DSP_TASK_0_CH);
}
```

【语法】

```c
ScheStatus SCHE_TaskRegister(DSP_TASK *task, DspTaskChannel ch)
```

【参数】

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

dsp上的任务通过此接口给cpu发消息

```c
ScheStatus SCHE_SendMessage(DSP_MESSAGE *pMsg, DspTaskChannel ch)
```

【参数】

参见章节3.3.1里的说明

#### 3.2.3 SCHE_GetMessage

【描述】

dsp上的任务通过此接口接收来自cpu的消息

```c
ScheStatus SCHE_GetMessage(DSP_MESSAGE *pMsg, DspTaskChannel ch)
```

【参数】

参见章节3.3.1里的说明

### 3.3.3 DSP Scheduler应用实列

运行如下命令加载任务调度裸机程序dsp scheduler：

```shell
cd /app/dsp_app_new
./dsp_app ../dsp_scheduler/scheduler.bin
```

在shell窗口能看到如下log，表明dsp scheduler加载成功。

```text
dsp schduler start
dsp schduler: register sample task successful, ch 0
dsp schduler: register audio3a task successful, ch 1
```

进入/app/mailbox_demo目录，输入如下命令，cpu会发命令给dsp启动一个任务，并且发送处理数据的请求，dsp处理完成会发消息通知cpu，这样一直循环。

```shell
cd /app/mailbox_demo
/app/mailbox_demo/cpu2dsp_task_demo
```

看到如下log，说明dsp运行cpu指定的任务成功。

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

**翻译免责声明**  
为方便客户，Canaan 使用 AI 翻译程序将文本翻译为多种语言，它可能包含错误。我们不保证提供的译文的准确性、可靠性或时效性。对于因依赖已翻译信息的准确性或可靠性而造成的任何损失或损害，Canaan 概不负责。如果不同语言翻译之间存在内容差异，以简体中文版本为准。

如果您要报告翻译错误或不准确的问题，欢迎通过邮件与我们联系。
