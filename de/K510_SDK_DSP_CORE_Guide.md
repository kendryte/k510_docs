![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 DSP CORE Anleitung</font>**

<font face="黑体"  size=3>Dokumentversion: V1.0.0</font>

<font face="黑体"  size=3>Veröffentlicht: 2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Verzichtserklärung**</font>
Die Produkte, Dienstleistungen oder Funktionen, die Sie erwerben, unterliegen den kommerziellen Verträgen und Bedingungen von Beijing Canaan Jiesi Information Technology Co., Ltd. ("das Unternehmen", dasselbe im Folgenden), und alle oder ein Teil der in diesem Dokument beschriebenen Produkte, Dienstleistungen oder Funktionen fallen möglicherweise nicht in den Rahmen Ihres Kaufs oder Ihrer Nutzung. Sofern im Vertrag nicht anders vereinbart, lehnt das Unternehmen alle ausdrücklichen oder stillschweigenden Zusicherungen oder Gewährleistungen hinsichtlich der Genauigkeit, Zuverlässigkeit, Vollständigkeit, des Marketings, des spezifischen Zwecks und der Nichtverletzung von Zusicherungen, Informationen oder Inhalten dieses Dokuments ab. Sofern nicht anders vereinbart, wird dieses Dokument nur als Leitfaden für die Verwendung zur Verfügung gestellt.
Aufgrund von Produktversions-Upgrades oder anderen Gründen kann der Inhalt dieses Dokuments von Zeit zu Zeit ohne vorherige Ankündigung aktualisiert oder geändert werden. 

**<font face="黑体"  size=3>Markenhinweise</font>**

"", "Canaan"-Symbol, Canaan und andere Marken von Canaan und andere Marken von Canaan <img src="../zh/images/canaan-logo.png" style="zoom:33%;" />sind Marken von Beijing Canaan Jiesi Information Technology Co., Ltd. Alle anderen Marken oder eingetragenen Warenzeichen, die in diesem Dokument erwähnt werden können, sind Eigentum ihrer jeweiligen Inhaber. 

**<font face="黑体"  size=3>Copyright ©2022 Peking Canaan Jiesi Information Technology Co., Ltd</font>**
Dieses Dokument gilt nur für die Entwicklung und das Design der K510-Plattform, ohne die schriftliche Genehmigung des Unternehmens darf keine Einheit oder Einzelperson einen Teil oder den gesamten Inhalt dieses Dokuments in irgendeiner Form verbreiten. 

**<font face="黑体"  size=3>Peking Canaan Jiesi Informationstechnologie Co., Ltd</font>**
URL: canaan-creative.com
Geschäftliche Anfragen: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# Vorwort
**<font face="黑体"  size=5>Zweck des Dokuments</font>**
Dieses Dokument ist eine Anleitung zur Verwendung des K510 DSP-Kerns. 

**<font face="黑体"  size=5>Reader-Objekte</font>**

Die wichtigsten Personen, für die sich dieses Dokument (dieser Leitfaden) richtet:

- Softwareentwickler
- Mitarbeiter des technischen Supports

**<font face="黑体"  size=5>Revisionshistorie</font>**
 <font face="宋体"  size=2>In der Revisionshistorie wird eine Beschreibung jeder Dokumentaktualisierung gesammelt. Die neueste Version des Dokuments enthält Updates für alle vorherigen Versionen. </font>

| Die Versionsnummer   | Geändert von     | Datum der Überarbeitung | Revisionshinweise |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | Systemsoftwaregruppen | 2022-03-09 |         |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Inhalt</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Übersicht

Es gibt drei Prozessoren im K510-Chip, von denen die CPU Dual-Kerne Linux ausführen, und der DSP-Kern ist für Benutzer inaktiv zu entwickeln und zu verwenden, und dieses Dokument stellt den DSP-Kern als Referenzroutine für den Coprozessor zum Ausführen von Bare-Metal-Programmen bereit.

![](../zh/images/doc_dsp/image-dsp_1.png)

<center> Abbildung 1 k510-Blockdiagramm </center>

# 1 DSP-Programm geladen

 k510_buildroot/package/dsp_app_new ist der Code, der den DSP lädt und im Linux-Benutzerbereich ausführt. dsp_app_new Code implementiert hauptsächlich das Laden der DSP-Firmware an den angegebenen Speicherort und das Starten des DSP, um die Ausführung zu starten, lautet der Hauptcode wie folgt:

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

dsp_app_new kompilierte ausführbare Datei wird im Verzeichnis Root-Dateisystem/App/dsp_app_new gespeichert.

# 2 DSP-Informationsdruck

 k510_buildroot/package/dsp_log ist der Code, der abfragt, ob der DSP-Kern über eine Protokollausgabe verfügt, die im Linux-Benutzerbereich ausgeführt wird. dsp_log Das kompilierte ausführbare Programm wird im Verzeichnis Root-Dateisystem/app/dsp_log gespeichert.

Nach dem Einschalten wird die dsp_log standardmäßig im Hintergrund ausgeführt, und ihre Konfigurationsdatei lautet: k510_buildroot/board/canaan/k510/k510_rootfs_skeleton/etc/init.d/rc.sysinit

![](../zh/images/doc_dsp/image-dsp_log.png)

# 3 DSP Bare-Metal-Demo

## 3,1 fft

Das fft-Demoprogramm befindet sich`/app/dsp_app_new/fft.bin`.
Der Quellcode des fft-Demoprogramms wird im Verzeichnis abgelegt`k510_buildroot/package/k510_evb_test/src/test/fft`. 

Wechseln Sie zum Verzeichnis /app/dsp_app_new':

- `dsp_app`: Programme, die den DSP laden und den DSP ausführen lassen (im Linux-Benutzerbereich ausgeführt)
- `fft.bin`: DSP Bare-Metal-Programm

Starten Sie das fft-Programm und führen Sie Folgendes aus:

```shell
cd /app/dsp_app_new
./dsp_app fft.bin
```

Sie können den folgenden Druck sehen:

![DSP-Demo](../zh/images/doc_dsp/demo_dsp.png)

Jetzt ist die Firmware, die auf DSP läuft, ein Demoprogramm für fct.

## 3.2 simd_umul8

Simd_umul8 Demoprogramm befindet sich`/app/dsp_app_new/simd_umul8_demo.bin`.
simd_umul8 der Quellcode des Demoprogramms im Verzeichnis abgelegt wird`k510_buildroot/package/k510_evb_test/src/test/simd_umul8_demo`, ist die Hauptarbeit wie folgt:

- Lassen Sie in der Demo zwei 32-Bit-Daten "multiplizieren", dh teilen Sie jede 32-Bit-Daten in 4 8-Bit-Daten auf und multiplizieren Sie sie dann, um 4 16-Bit-Ergebnisse zu erhalten, und prüfen Sie, ob die Berechnungsergebnisse wie erwartet sind. Beispielsweise ergibt 0x05050505 multipliziert mit 0x02020202 0x000a000a000a000a.
- Wenn es wie erwartet ist, drucken Sie `DSP SIMD UMUL8 TEST PASS`die Informationen, andernfalls drucken Sie`DSP SIMD UMUL8 TEST FAIL` die Informationen

Methode zum Ausführen der Demo:

```shell
cd /app/dsp_app_new
./dsp_app simd_umul8_demo.bin
```

Spezifische Anweisungen finden Sie in [ der Produktdokumentation - Andes-Technologie](http://www.andestech.com/en/products-solutions/product-documentation/) zum Herunterladen der AndeStar V5 DSP ISA Extension Specification .PDF (v1.0, 2019-03-25), siehe Abschnitt 3.172. 

## 3.3 DSP-Scheduler-API

Wenn die CPU-Leistung einige Anwendungen nicht erfüllen kann, können Sie einen Teil der Funktion aufteilen, der auf dem DSP ausgeführt werden soll, um die CPU-Last zu reduzieren. Es gibt kein Betriebssystem auf dem DSP, daher ist ein Task-Scheduling-Manager implementiert, und der Code befindet sich im Verzeichnis k510_buildroot/package/dsp_scheduler. Tasks, die auf dem DSP ausgeführt werden, werden in statische Bibliotheken kompiliert, vorab mit dem DSP-Scheduler verknüpft, und die Laufzeit-CPU sendet über das Postfach eine Nachricht an den DSP, um die entsprechende Taskausführung zu starten.

Benutzer können bei der Registrierung von Aufgaben Prioritäten definieren, und der DSP-Planer plant Aufgaben nach Prioritäten. Der Rückgabewert der run-Funktion der Task-Run-Schnittstelle bestimmt, ob sie RUN_ONCE oder CONTINUE_RUN ist, so dass der Benutzer selbst entscheiden kann, wie oft der Task ausgeführt wird.

Wie Sie Nachrichten über das Linux-Postfach-Framework an DSPs senden, lesen Sie bitte die entsprechende Einführung im Dokument K510_Mailbox_Developer_Guides. Die Referenzimplementierung befindet sich in k510_buildroot/package/k510_evb_test/src/test/mailbox_demo/cpu2dsp_task_demo.c

### 3.3.1 Beschreibungen der Header-Datei

1. k510_buildroot/Paket/dsp_scheduler/src/dsp_tasks.h

    Das Programm, das auf der CPU ausgeführt wird, muss diese Headerdatei enthalten, die den Nachrichtentyp und die Struktur zwischen der CPU und dem DSP definiert, und die Systemnachrichtenkommunikation nimmt eine Frage-und-Antwort-Methode an, und die CPU muss warten, bis die gleiche Nachricht, die vom dsp nach dem Senden der Nachricht gesendet wird, um anzuzeigen, dass der dsp verarbeitet wird. Benutzernachrichten können bei Bedarf eigene Mechanismen definieren. Die Nachricht bedeutet Folgendes:

    - DSP_TASK_ENABLE

    Wenn die entsprechende Aufgabe ausgeführt wird, kann auf diese Meldung eine Speicheradresse für die Task-Druckdebuginformationen auf dem DSP folgen

    - DSP_TASK_DISABLE

    Der entsprechende Task wird nicht mehr ausgeführt

    - DSP_TASK_PRINT_INFO

    Druckt alle registrierten Aufgabeninformationen

    - DSP_TASK_USER_MSG

    Benutzerdefinierte Aufgabenmeldungen, die einer Speicheradresse folgen, ermöglichen es Benutzern, ihre eigenen Message Queuing- und Nachrichtenkommunikationsmechanismen nach Bedarf zu entwerfen

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

2. k510_buildroot/Paket/dsp_scheduler/src/scheduler.h
    Programme, die auf dsp ausgeführt werden, benötigen diese Headerdatei

### 3.3.2 Beschreibung der API-Funktion

#### 3.3.2.1 SCHE_TaskRegister

【Beschreibung】

Registrieren Sie eine Aufgabe. Auf dem DSP können bis zu 8 Aufgaben registriert werden, die jeweils über einen Postfachkanal und eine CPU kommunizieren. Aufgabe 0 entspricht der Postfachkanalnummer 0, DSP_TASK_0_CH entspricht der MBOX_CHAN_0_TX des CPU-Postfachs usw.

Implementieren Sie die folgende Aufgabenstruktur

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

Registrieren Sie die Aufgabe in k510_buildroot/package/dsp_scheduler/alltasks.c mit dem folgenden Code:

```c
{
    extern DSP_TASK dsp_sample_task;
    SCHE_TaskRegister(&dsp_sample_task, DSP_TASK_0_CH);
}
```

【Grammatik】

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

【Beschreibung】

Aufgaben auf dem DSP senden über diese Schnittstelle Nachrichten an die CPU

```c
ScheStatus SCHE_SendMessage(DSP_MESSAGE *pMsg, DspTaskChannel ch)
```

【Parameters】

Siehe Abschnitt 3.3.1 für Anweisungen

#### 3.2.3 SCHE_GetMessage

【Beschreibung】

Aufgaben auf dem DSP empfangen über diese Schnittstelle Nachrichten von der CPU

```c
ScheStatus SCHE_GetMessage(DSP_MESSAGE *pMsg, DspTaskChannel ch)
```

【Parameters】

Siehe Abschnitt 3.3.1 für Anweisungen

### 3.3.3 DSP Scheduler wendet echte Spalten an

Führen Sie den folgenden Befehl aus, um den dsp-Scheduler des Bare-Metal-Programms zu laden:

```shell
cd /app/dsp_app_new
./dsp_app ../dsp_scheduler/scheduler.bin
```

Im Shell-Fenster sehen Sie das folgende Protokoll, das angibt, dass der DSP-Scheduler erfolgreich geladen wurde.

```text
dsp schduler start
dsp schduler: register sample task successful, ch 0
dsp schduler: register audio3a task successful, ch 1
```

Geben Sie das Verzeichnis /app/mailbox_demo ein, geben Sie den folgenden Befehl ein, die CPU sendet einen Befehl an dsp, um eine Aufgabe zu starten, und sendet eine Anforderung zur Verarbeitung der Daten, dsp-Verarbeitung sendet eine Nachricht, um die CPU zu benachrichtigen, so dass die Schleife.

```shell
cd /app/mailbox_demo
/app/mailbox_demo/cpu2dsp_task_demo
```

Weitere Informationen finden Sie im folgenden Protokoll, das angibt, dass die von der von dsp angegebenen CPU angegebene Aufgabe erfolgreich war.

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

**Haftungsausschluss **für Übersetzungen  
Für die Bequemlichkeit der Kunden verwendet Canaan einen KI-Übersetzer, um Text in mehrere Sprachen zu übersetzen, die Fehler enthalten können. Wir übernehmen keine Gewähr für die Genauigkeit, Zuverlässigkeit oder Aktualität der bereitgestellten Übersetzungen. Canaan haftet nicht für Verluste oder Schäden, die durch das Vertrauen auf die Richtigkeit oder Zuverlässigkeit der übersetzten Informationen verursacht werden. Wenn es einen inhaltlichen Unterschied zwischen den Übersetzungen in verschiedenen Sprachen gibt, ist die vereinfachte chinesische Version maßgebend. 

Wenn Sie einen Übersetzungsfehler oder eine Ungenauigkeit melden möchten, können Sie uns gerne per E-Mail kontaktieren.