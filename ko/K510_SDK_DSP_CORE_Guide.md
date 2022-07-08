![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 DSP 코어 가이드</font>**

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
이 문서는 K510 DSP 코어 사용에 대한 지침입니다.

**<font face="黑体"  size=5>독자 개체입니다</font>**

이 문서(이 가이드)가 주로 적용되는 사람:

- 소프트웨어 개발자
- 기술 지원 담당자

**<font face="黑体"  size=5>레코드를 수정합니다</font>**
 <font face="宋体"  size=2>개정 레코드에는 각 문서 업데이트에 대한 설명이 누적됩니다. 문서의 최신 버전에는 이전 버전의 모든 업데이트가 포함되어 있습니다. </font>

| 버전 번호입니다   | 수정자     | 개정일입니다 | 개정 지침 |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | 시스템 소프트웨어 그룹입니다 | 2022-03-09 |         |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>카탈로그</font>**

[목차]

<div style="page-break-after:always"></div>

# 1 개요

K510 칩에는 CPU Dual cores가 Linux를 실행하고 DSP 코어가 개발 및 사용을 위해 유휴 상태인 세 개의 프로세서가 있으며, 이 문서에서는 DSP 코어가 코프로세서로 베어 메탈 프로그램을 실행하는 참조 루틴을 제공합니다.

![](../zh/images/doc_dsp/image-dsp_1.png)

<center> 그림 1 k510 블록 다이어그램 </center>

# 1 DSP 프로그램이 로드됩니다

 k510_buildroot/package/dsp_app_new 디렉토리에는 Linux 사용자 공간에서 실행되는 DSP를 로드하고 실행하는 코드입니다. dsp_app_new 코드는 주로 DSP 펌웨어를 지정된 위치에 로드하고 DSP 실행을 시작하는 것을 구현하며 주요 코드는 다음과 같습니다.

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

dsp_app_new 컴파일된 실행 프로그램은 루트 파일 시스템/앱/dsp_app_new 디렉토리에 저장됩니다.

# 2 DSP 정보 인쇄

 k510_buildroot/package/dsp_log 디렉토리는 Linux 사용자 공간에서 실행되는 DSP 코어에 Log 출력이 있는지 여부를 쿼리하는 코드입니다. dsp_log 컴파일된 실행 프로그램은 루트 파일 시스템/앱/dsp_log 디렉토리에 저장됩니다.

k510_buildroot/board/canaan/k510/k510_rootfs_skeleton/etc/init.d/rc.sysinit의 구성 파일이 있는 dsp_log 기본적으로 백그라운드에서 실행됩니다

![](../zh/images/doc_dsp/image-dsp_log.png)

# 3 DSP 베어 메탈 데모

## 3.1 fft

fft demo 프로그램이 있습니다`/app/dsp_app_new/fft.bin`.
fft demo 프로그램 소스 코드는 디렉토리에 배치됩니다`k510_buildroot/package/k510_evb_test/src/test/fft`.

/app/dsp_app_new' 디렉토리로 이동합니다.

- `dsp_app`: DSP를 로드하고 dsp를 실행하게 하는 프로그램(Linux 사용자 공간에서 실행)
- `fft.bin`: DSP 베어 메탈 프로그램

fft 프로그램 실행 시작:

```shell
cd /app/dsp_app_new
./dsp_app fft.bin
```

다음과 같은 인쇄를 볼 수 있습니다.

![DSP 데모](../zh/images/doc_dsp/demo_dsp.png)

이제 dsp에서 실행되는 firmware는 fft의 데모 프로그램입니다.

## 3.2 simd_umul8

simd_umul8 데모 프로그램이 있습니다`/app/dsp_app_new/simd_umul8_demo.bin`.
simd_umul8 데모 프로그램 소스 코드는 디렉토리에 배치`k510_buildroot/package/k510_evb_test/src/test/simd_umul8_demo`되며 주요 작업은 다음과 같습니다

- 데모에서 두 개의 32비트 데이터를 "곱하기"하여 각 32비트 데이터를 4개의 8비트 데이터로 분할한 다음 각각 곱하여 4개의 16비트 결과를 가져와 계산 결과가 예상과 일치하는지 확인합니다. 예를 들어 0x05050505 0x02020202 "곱하기"의 결과는 0x000a000a000a000a.
- 예상과 일치하면 정보를 인쇄하고 `DSP SIMD UMUL8 TEST PASS`그렇지 않으면 정보를 인쇄`DSP SIMD UMUL8 TEST FAIL`합니다

데모를 실행하는 방법:

```shell
cd /app/dsp_app_new
./dsp_app simd_umul8_demo.bin
```

자세한 지침은 [Product Documentation - Andes Technology 다운로드](http://www.andestech.com/en/products-solutions/product-documentation/) AndeStar V5 DSP ISA Extension Specification.PDF(v1.0, 2019-03-25)에서 3.172절을 참조하십시오.

## 3.3 DSP 스케줄러 API

CPU 성능이 일부 응용 프로그램을 충족하지 않는 경우 일부 기능을 DSP로 분할하여 CPU 부하를 줄일 수 있습니다. DSP에는 운영 체제가 없으므로 k510_buildroot/package/dsp_scheduler 디렉터리에 코드가 있는 작업 일정 관리자가 구현됩니다. DSP에서 실행되는 작업은 정적 라이브러리로 컴파일되고 DSP scheduler와 미리 연결되며 런타임 cpu는 mailbox를 통해 dsp에 메시지를 보내 해당 작업 실행을 시작합니다.

사용자는 작업을 등록할 때 우선 순위를 정의할 수 있으며 DSP scheduler는 우선 순위에 따라 작업을 예약합니다. 작업 실행 인터페이스 run 함수의 반환 값은 사용자가 작업을 실행할 횟수를 스스로 결정할 수 있도록 RUN_ONCE 또는 CONTINUE_RUN 여부를 결정합니다.

cpu가 linux mailbox 프레임워크를 통해 dsp에 메시지를 보내는 방법은 설명서의 K510_Mailbox_Developer_Guides 해당 설명서를 참조하십시오. 참조 구현은 k510_buildroot/package/k510_evb_test/src/test/mailbox_demo/cpu2dsp_task_demo.c입니다

### 3.3.1 헤더 문서에 대한 설명입니다

1. k510_buildroot/패키지/dsp_scheduler/src/dsp_tasks.h

    cpu에서 실행되는 프로그램에는 cpu와 dsp 간의 메시지 유형과 구조를 정의하는 include 헤더 파일이 필요하며, 시스템 메시지 통신은 일문일답을 사용하며, CPU는 dsp가 동일한 메시지를 보낼 때까지 기다렸다가 dsp가 처리되었음을 나타냅니다. 사용자 메시지는 필요에 따라 메커니즘을 직접 정의할 수 있습니다. 메시지는 다음과 같은 의미를 갖습니다.

    - DSP_TASK_ENABLE

    해당 작업이 실행되기 시작하고 이 메시지는 dsp의 작업에 대한 디버그 정보를 인쇄하는 데 사용되는 메모리 주소를 따를 수 있습니다

    - DSP_TASK_DISABLE

    해당 작업이 중지되었습니다

    - DSP_TASK_PRINT_INFO

    등록된 모든 작업 정보를 인쇄합니다

    - DSP_TASK_USER_MSG

    필요에 따라 메시지 큐 및 메시지 통신 메커니즘을 직접 디자인할 수 있는 메모리 주소를 따르는 사용자 지정 작업 메시지입니다

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
    dsp에서 실행되는 프로그램에는 include 헤더 파일이 필요합니다

### 3.3.2 API 함수 설명

#### 3.3.2.1 SCHE_TaskRegister

[설명]

작업을 등록합니다. DSP는 최대 8개의 작업을 등록할 수 있으며, 각 작업은 mailbox 채널과 CPU를 통해 통신합니다. Task 0의 mailbox 채널 번호는 0이며 DSP_TASK_0_CH cpu mailbox의 MBOX_CHAN_0_TX 해당합니다.

다음과 같은 task 구조를 구현합니다

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

k510_buildroot/package/dsp_scheduler/alltasks.c에서 다음과 같이 작업 등록을 수행합니다.

```c
{
    extern DSP_TASK dsp_sample_task;
    SCHE_TaskRegister(&dsp_sample_task, DSP_TASK_0_CH);
}
```

【문법】

```c
ScheStatus SCHE_TaskRegister(DSP_TASK *task, DspTaskChannel ch)
```

[매개변수]

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

[설명]

dsp의 작업은 이 인터페이스를 통해 CPU에 메시지를 보냅니다

```c
ScheStatus SCHE_SendMessage(DSP_MESSAGE *pMsg, DspTaskChannel ch)
```

[매개변수]

섹션 3.3.1의 지침을 참조하십시오

#### 3.2.3 SCHE_GetMessage

[설명]

dsp의 작업은 이 인터페이스를 통해 CPU에서 메시지를 받습니다

```c
ScheStatus SCHE_GetMessage(DSP_MESSAGE *pMsg, DspTaskChannel ch)
```

[매개변수]

섹션 3.3.1의 지침을 참조하십시오

### 3.3.3 DSP Scheduler는 실제 열을 적용합니다

다음 명령을 실행하여 작업 스케줄러 베어 메탈 프로그램 dsp scheduler를 로드합니다.

```shell
cd /app/dsp_app_new
./dsp_app ../dsp_scheduler/scheduler.bin
```

셸 창에는 dsp scheduler가 성공적으로 로드되었음을 나타내는 다음과 같은 로그가 표시됩니다.

```text
dsp schduler start
dsp schduler: register sample task successful, ch 0
dsp schduler: register audio3a task successful, ch 1
```

입력/앱/mailbox_demo 디렉터리, 다음 명령을 입력, cpu는 작업을 시작 하는 dsp에 명령을 보내, 데이터 처리 요청을 보내, dsp 처리 완료는 CPU에 메시지를 보낼 것 이다, 그래서 루프.

```shell
cd /app/mailbox_demo
/app/mailbox_demo/cpu2dsp_task_demo
```

dsp가 CPU에서 지정한 작업을 성공적으로 실행한 다음 로그가 표시됩니다.

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

**번역 면책 조항**  
고객의 편의를 위해 Canan은 AI 번역 프로그램을 사용하여 오류를 포함할 수 있는 여러 언어로 텍스트를 번역합니다. 당사는 제공된 번역의 정확성, 신뢰성 또는 적시성을 보장하지 않습니다. Canan은 번역된 정보의 정확성이나 신뢰성에 의존하여 발생하는 손실이나 손해에 대해 책임을 지지 않습니다. 언어 번역 간에 콘텐츠 차이가 있는 경우 중국어 간체 버전이 우선합니다.

번역 오류 또는 부정확한 문제를 신고하려면 이메일로 문의하시기 바랍니다.
