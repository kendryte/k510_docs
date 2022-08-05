![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 DSP CORE Guide</font>**

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
This document is a guide for using the K510 DSP core.

**<font face="黑体"  size=5>Reader Objects</font>**

The main people to whom this document (this guide) applies:

- Software developers
- Technical support personnel

**<font face="黑体"  size=5>Revision history</font>**
 <font face="宋体"  size=2>The revision history accumulates a description of each document update. The latest version of the document contains updates for all previous versions. </font>

| The version number   | Modified by     | Date of revision | Revision Notes |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | System software groups | 2022-03-09 |         |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contents</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Overview

There are three processors in the K510 chip, of which the CPU Dual cores run Linux, and the DSP core is idle for users to develop and use, and this document provides the DSP core as a reference routine for the coprocessor to run bare metal programs.

![](../zh/images/doc_dsp/image-dsp_1.png)

<center> Figure 1 k510 block diagram </center>

# 1 DSP program loaded

 k510_buildroot/package/dsp_app_new directory, is the code that loads the DSP and runs it in Linux user space. dsp_app_new code mainly implements loading the DSP firmware to the specified location and starting the DSP to start execution, its main code is as follows:

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

dsp_app_new compiled executable program is stored in the root file system/app/dsp_app_new directory.

# 2 DSP information printing

 k510_buildroot/package/dsp_log directory, is the code that queries whether the DSP core has Log output, which runs in Linux user space. dsp_log The compiled executable program is stored in the root file system/app/dsp_log directory.

After powering on, the dsp_log will be executed in the background by default, and its configuration file is: k510_buildroot/board/canaan/k510/k510_rootfs_skeleton/etc/init.d/rc.sysinit

![](../zh/images/doc_dsp/image-dsp_log.png)

# 3 DSP bare metal demo

## 3.1 fft

The fft demo program is located`/app/dsp_app_new/fft.bin`.
The fft demo program source code is placed in`k510_buildroot/package/k510_evb_test/src/test/fft` the directory.

Go to the /app/dsp_app_new' directory:

- `dsp_app`: Programs that load the DSP and make the dsp run (run in Linux user space)
- `fft.bin`: DSP bare metal program

Start the fft program and run:

```shell
cd /app/dsp_app_new
./dsp_app fft.bin
```

You can see the following print:

![DSP Demo](../zh/images/doc_dsp/demo_dsp.png)

Now the firmware running on DSP is a demo program for fct.

## 3.2 simd_umul8

Simd_umul8 demo program is located`/app/dsp_app_new/simd_umul8_demo.bin`.
simd_umul8 the demo program source code is placed `k510_buildroot/package/k510_evb_test/src/test/simd_umul8_demo`in the directory, the main work done is as follows:

- In the demo, let two 32-bit data "multiply", that is, divide each 32-bit data into 4 8-bit data, and then multiply them respectively to get 4 16-bit results, and check whether the calculation results are as expected. For example, 0x05050505 multiplied by 0x02020202 results in 0x000a000a000a000a.
- If it is as expected, print `DSP SIMD UMUL8 TEST PASS`the information, otherwise print`DSP SIMD UMUL8 TEST FAIL` the information

Method to run the demo:

```shell
cd /app/dsp_app_new
./dsp_app simd_umul8_demo.bin
```

Specific instructions can be found in [Product Documentation - Andes Technology](http://www.andestech.com/en/products-solutions/product-documentation/) to download the AndeStar V5 DSP ISA Extension Specification .PDF (v1.0, 2019-03-25), see Section 3.172.

## 3.3 DSP Scheduler API

When the CPU performance can not meet some applications, you can split a part of the function to run on the DSP to reduce the CPU load. There is no operating system on the DSP, so a task scheduling manager is implemented, and the code is in the directory of k510_buildroot/package/dsp_scheduler. Tasks running on the DSP are compiled into static libraries, pre-linked with the DSP scheduler, and the runtime CPU sends a message to the dsp through the mailbox to start the corresponding task run.

Users can define priorities when registering tasks, and the DSP scheduler schedules tasks according to priorities. The return value of the run function of the task run interface determines whether it is RUN_ONCE or CONTINUE_RUN, so that the user can decide for himself how many times the task is executed.

How to send messages to dsps through the Linux mailbox framework, please refer to the corresponding introduction in the document K510_Mailbox_Developer_Guides. The reference implementation is in k510_buildroot/package/k510_evb_test/src/test/mailbox_demo/cpu2dsp_task_demo.c

### 3.3.1 Header File Descriptions

1. k510_buildroot/package/dsp_scheduler/src/dsp_tasks.h

    The program running on the cpu needs to include this header file, which defines the message type and structure between the CPU and the dsp, and the system message communication adopts a question-and-answer method, and the CPU must wait until the same message sent by the dsp after sending the message to indicate that the dsp is processed. User messages can define their own mechanisms as needed. The message means the following:

    - DSP_TASK_ENABLE

    When the corresponding task starts running, this message can be followed by a memory address for the task print debug information on the dsp

    - DSP_TASK_DISABLE

    The corresponding task stops running

    - DSP_TASK_PRINT_INFO

    Prints all registered task information

    - DSP_TASK_USER_MSG

    User-defined task messages, which follow a memory address, allow users to design their own message queuing and message communication mechanisms as needed

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
    Programs running on dsp require include this header file

### 3.3.2 API Function Description

#### 3.3.2.1 SCHE_TaskRegister

【Description】

Register a task. Up to 8 tasks can be registered on the DSP, each communicating through a mailbox channel and CPU. Task 0 corresponds to the mailbox channel number of 0, DSP_TASK_0_CH corresponds to the MBOX_CHAN_0_TX of the cpu mailbox, and so on.

Implement the following task structure

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

In k510_buildroot/package/dsp_scheduler/alltasks.c, register the task with the following code:

```c
{
    extern DSP_TASK dsp_sample_task;
    SCHE_TaskRegister(&dsp_sample_task, DSP_TASK_0_CH);
}
```

【Grammar】

```c
ScheStatus SCHE_TaskRegister(DSP_TASK *task, DspTaskChannel ch)
```

【Parameters】

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

【Description】

Tasks on the dsp send messages to the CPU through this interface

```c
ScheStatus SCHE_SendMessage(DSP_MESSAGE *pMsg, DspTaskChannel ch)
```

【Parameters】

See Section 3.3.1 for instructions

#### 3.2.3 SCHE_GetMessage

【Description】

Tasks on the dsp receive messages from the CPU through this interface

```c
ScheStatus SCHE_GetMessage(DSP_MESSAGE *pMsg, DspTaskChannel ch)
```

【Parameters】

See Section 3.3.1 for instructions

### 3.3.3 DSP Scheduler applies real columns

Run the following command to load the bare metal program dsp scheduler:

```shell
cd /app/dsp_app_new
./dsp_app ../dsp_scheduler/scheduler.bin
```

In the shell window, you can see the following log, indicating that the dsp scheduler is successfully loaded.

```text
dsp schduler start
dsp schduler: register sample task successful, ch 0
dsp schduler: register audio3a task successful, ch 1
```

Enter the /app/mailbox_demo directory, enter the following command, the cpu will send a command to dsp to start a task, and send a request to process the data, dsp processing will send a message to notify the cpu, so that the loop.

```shell
cd /app/mailbox_demo
/app/mailbox_demo/cpu2dsp_task_demo
```

See the following log, indicating that the task specified by the cpu specified by dsp was successful.

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

**Translation Disclaimer**  
For the convenience of customers, Canaan uses an AI translator to translate text into multiple languages, which may contain errors. We do not guarantee the accuracy, reliability or timeliness of the translations provided. Canaan shall not be liable for any loss or damage caused by reliance on the accuracy or reliability of the translated information. If there is a content difference between the translations in different languages, the Chinese Simplified version shall prevail.

If you would like to report a translation error or inaccuracy, please feel free to contact us by mail.
