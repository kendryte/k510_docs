![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">Guida di K510 DSP CORE</font>**

<font face="黑体"  size=3>Versione del documento: V1.0.0</font>

<font face="黑体"  size=3>Data di pubblicazione: 2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Disconoscimento**</font>
I prodotti, i servizi o le funzionalità acquistati saranno soggetti ai contratti e ai termini commerciali di Beijing Canaan Jiesi Information Technology Co., Ltd. ("la Società", la stessa di seguito), e tutti o parte dei prodotti, servizi o funzionalità descritti in questo documento potrebbero non rientrare nell'ambito dell'acquisto o dell'utilizzo. Salvo quanto diversamente concordato nel contratto, la Società declina ogni dichiarazione o garanzia, espressa o implicita, in merito all'accuratezza, affidabilità, completezza, marketing, scopo specifico e non aggressione di qualsiasi dichiarazione, informazione o contenuto di questo documento. Salvo diverso accordo, questo documento è fornito solo come guida per l'uso.
A causa di aggiornamenti della versione del prodotto o altri motivi, il contenuto di questo documento può essere aggiornato o modificato di volta in volta senza alcun preavviso. 

**<font face="黑体"  size=3>Avvisi sui marchi</font>**

""<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, l'icona "Canaan", Canaan e altri marchi di Canaan e altri marchi di Canaan sono marchi di Beijing Canaan Jiesi Information Technology Co., Ltd. Tutti gli altri marchi o marchi registrati che possono essere menzionati in questo documento sono di proprietà dei rispettivi proprietari. 

**<font face="黑体"  size=3>Copyright ©2022 Pechino Canaan Jiesi Information Technology Co., Ltd</font>**
Questo documento è applicabile solo allo sviluppo e alla progettazione della piattaforma K510, senza il permesso scritto della società, nessuna unità o individuo può diffondere parte o tutto il contenuto di questo documento in qualsiasi forma. 

**<font face="黑体"  size=3>Pechino Canaan Jiesi Information Technology Co., Ltd</font>**
URL: canaan-creative.com
Richieste commerciali: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# prefazione
**<font face="黑体"  size=5>Scopo </font>**del documento
Questo documento è una guida per l'utilizzo del core DSP K510. 

**<font face="黑体"  size=5>Oggetti lettore</font>**

Le principali persone a cui si applica questo documento (questa guida):

- Sviluppatori di software
- Personale di supporto tecnico

**<font face="黑体"  size=5>Cronologia delle revisioni</font>**
 <font face="宋体"  size=2>La cronologia delle revisioni accumula una descrizione di ogni aggiornamento del documento. La versione più recente del documento contiene gli aggiornamenti per tutte le versioni precedenti. </font>

| Il numero di versione   | Modificato da     | Data della revisione | Note di revisione |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 · | Gruppi di software di sistema | 2022-03-09 |         |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenuto</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Panoramica

Ci sono tre processori nel chip K510, di cui i dual core della CPU eseguono Linux, e il core DSP è inattivo per gli utenti da sviluppare e utilizzare, e questo documento fornisce il core DSP come routine di riferimento per il coprocessore per eseguire programmi bare metal.

![](../zh/images/doc_dsp/image-dsp_1.png)

<center> Figura 1 diagramma a blocchi k510 </center>

# 1 programma DSP caricato

 k510_buildroot/package/dsp_app_new directory, è il codice che carica il DSP e lo esegue nello spazio utente Linux. dsp_app_new codice implementa principalmente il caricamento del firmware DSP nella posizione specificata e l'avvio del DSP per avviare l'esecuzione, il suo codice principale è il seguente:

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

dsp_app_new programma eseguibile compilato è memorizzato nella directory root file system/app/dsp_app_new.

# 2 Stampa di informazioni DSP

 k510_buildroot/package/dsp_log directory, è il codice che chiede se il core DSP ha l'output Log, che viene eseguito nello spazio utente Linux. dsp_log Il programma eseguibile compilato è memorizzato nella directory root file system/app/dsp_log.

Dopo l'accensione, il dsp_log verrà eseguito in background per impostazione predefinita e il suo file di configurazione è: k510_buildroot /board/canaan/k510/k510_rootfs_skeleton/etc/init.d/rc.sysinit

![](../zh/images/doc_dsp/image-dsp_log.png)

# 3 DSP bare metal demo

## 3,1 fft

Il programma demo fft si trova`/app/dsp_app_new/fft.bin`.
Il codice sorgente del programma demo fft viene inserito nella`k510_buildroot/package/k510_evb_test/src/test/fft` directory. 

Vai alla directory /app/dsp_app_new':

- `dsp_app`: Programmi che caricano il DSP e fanno funzionare il dsp (eseguiti nello spazio utente Linux)
- `fft.bin`: Programma bare metal DSP

Avviare il programma fft ed eseguire:

```shell
cd /app/dsp_app_new
./dsp_app fft.bin
```

Puoi vedere la seguente stampa:

![DSP Demo](../zh/images/doc_dsp/demo_dsp.png)

Ora il firmware in esecuzione su DSP è un programma demo per fct.

## 3.2 simd_umul8

Simd_umul8 programma demo si trova`/app/dsp_app_new/simd_umul8_demo.bin`.
simd_umul8 il codice sorgente del programma demo viene inserito `k510_buildroot/package/k510_evb_test/src/test/simd_umul8_demo`nella directory, il lavoro principale svolto è il seguente:

- Nella demo, lascia che due dati a 32 bit "si moltiplichino", cioè dividino ogni dato a 32 bit in 4 dati a 8 bit, quindi moltiplicali rispettivamente per ottenere 4 risultati a 16 bit e controlla se i risultati del calcolo sono come previsto. Ad esempio, 0x05050505 moltiplicato per 0x02020202 si traduce in 0x000a000a000a000a.
- Se è come previsto, stampare `DSP SIMD UMUL8 TEST PASS`le informazioni, altrimenti stampare`DSP SIMD UMUL8 TEST FAIL` le informazioni

Metodo per eseguire la demo:

```shell
cd /app/dsp_app_new
./dsp_app simd_umul8_demo.bin
```

Istruzioni specifiche sono disponibili nella [Documentazione del prodotto - Andes Technology](http://www.andestech.com/en/products-solutions/product-documentation/) per scaricare la specifica di estensione ISA AndeStar V5 DSP .PDF (v1.0, 2019-03-25), vedere Sezione 3.172. 

## 3.3 API DSP Scheduler

Quando le prestazioni della CPU non possono soddisfare alcune applicazioni, è possibile dividere una parte della funzione da eseguire sul DSP per ridurre il carico della CPU. Non esiste un sistema operativo sul DSP, quindi viene implementato un task scheduling manager e il codice si trova nella directory di k510_buildroot/package/dsp_scheduler. Le attività in esecuzione sul DSP vengono compilate in librerie statiche, precollegate all'utilità di pianificazione DSP e la CPU di runtime invia un messaggio al dsp tramite la cassetta postale per avviare l'esecuzione dell'attività corrispondente.

Gli utenti possono definire le priorità durante la registrazione delle attività e l'utilità di pianificazione DSP pianifica le attività in base alle priorità. Il valore restituito della funzione run dell'interfaccia di esecuzione dell'attività determina se si tratta di RUN_ONCE o CONTINUE_RUN, in modo che l'utente possa decidere autonomamente quante volte l'attività viene eseguita.

Come inviare messaggi a dsps attraverso il framework delle cassette postali Linux, fare riferimento all'introduzione corrispondente nel documento K510_Mailbox_Developer_Guides. L'implementazione di riferimento è in k510_buildroot/package/k510_evb_test/src/test/mailbox_demo/cpu2dsp_task_demo.c

### 3.3.1 Descrizioni dei file di intestazione

1. k510_buildroot/pacchetto/dsp_scheduler/src/dsp_tasks.h

    Il programma in esecuzione sulla CPU deve includere questo file di intestazione, che definisce il tipo e la struttura del messaggio tra la CPU e il dsp, e la comunicazione del messaggio di sistema adotta un metodo di domanda e risposta e la CPU deve attendere fino a quando lo stesso messaggio inviato dal dsp dopo aver inviato il messaggio per indicare che il dsp viene elaborato. I messaggi utente possono definire i propri meccanismi in base alle esigenze. Il messaggio indica quanto segue:

    - DSP_TASK_ENABLE

    Quando l'attività corrispondente inizia a essere eseguita, questo messaggio può essere seguito da un indirizzo di memoria per le informazioni di debug di stampa dell'attività sul DSP

    - DSP_TASK_DISABLE

    L'attività corrispondente smette di funzionare

    - DSP_TASK_PRINT_INFO

    Stampa tutte le informazioni sulle attività registrate

    - DSP_TASK_USER_MSG

    I messaggi di attività definiti dall'utente, che seguono un indirizzo di memoria, consentono agli utenti di progettare i propri meccanismi di accodamento e comunicazione dei messaggi in base alle esigenze

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
    I programmi in esecuzione su dsp richiedono di includere questo file di intestazione

### 3.3.2 Descrizione della funzione API

#### 3.3.2.1 SCHE_TaskRegister

【Descrizione】

Registrare un'attività. È possibile registrare fino a 8 attività sul DSP, ognuna delle quali comunica tramite un canale di cassetta postale e cpu. L'attività 0 corrisponde al numero di canale della cassetta postale pari a 0, DSP_TASK_0_CH corrisponde alla MBOX_CHAN_0_TX della cassetta postale della CPU e così via.

Implementare la seguente struttura di attività

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

In k510_buildroot/package/dsp_scheduler/alltasks.c registrare l'attività con il codice seguente:

```c
{
    extern DSP_TASK dsp_sample_task;
    SCHE_TaskRegister(&dsp_sample_task, DSP_TASK_0_CH);
}
```

【Grammatica】

```c
ScheStatus SCHE_TaskRegister(DSP_TASK *task, DspTaskChannel ch)
```

【Parametri】

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

【Descrizione】

Le attività sul DSP inviano messaggi alla CPU tramite questa interfaccia

```c
ScheStatus SCHE_SendMessage(DSP_MESSAGE *pMsg, DspTaskChannel ch)
```

【Parametri】

Vedere Sezione 3.3.1 per le istruzioni

#### 3.2.3 SCHE_GetMessage

【Descrizione】

Le attività sul DSP ricevono messaggi dalla CPU tramite questa interfaccia

```c
ScheStatus SCHE_GetMessage(DSP_MESSAGE *pMsg, DspTaskChannel ch)
```

【Parametri】

Vedere Sezione 3.3.1 per le istruzioni

### 3.3.3 DSP Scheduler applica colonne reali

Eseguire il comando seguente per caricare l'utilità di pianificazione dSP del programma bare metal:

```shell
cd /app/dsp_app_new
./dsp_app ../dsp_scheduler/scheduler.bin
```

Nella finestra della shell, è possibile visualizzare il seguente registro, che indica che l'utilità di pianificazione DSP è stata caricata correttamente.

```text
dsp schduler start
dsp schduler: register sample task successful, ch 0
dsp schduler: register audio3a task successful, ch 1
```

Immettere la directory /app/mailbox_demo, immettere il seguente comando, la cpu invierà un comando a dsp per avviare un'attività e invierà una richiesta per elaborare i dati, l'elaborazione dsp invierà un messaggio per notificare la cpu, in modo che il ciclo.

```shell
cd /app/mailbox_demo
/app/mailbox_demo/cpu2dsp_task_demo
```

Vedere il registro seguente, che indica che l'attività specificata dalla CPU specificata da dsp ha avuto esito positivo.

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

**Traduzione Disclaimer**  
Per la comodità dei clienti, Canaan utilizza un traduttore AI per tradurre il testo in più lingue, che possono contenere errori. Non garantiamo l'accuratezza, l'affidabilità o la tempestività delle traduzioni fornite. Canaan non sarà responsabile per eventuali perdite o danni causati dall'affidamento sull'accuratezza o sull'affidabilità delle informazioni tradotte. Se c'è una differenza di contenuto tra le traduzioni in lingue diverse, prevarrà la versione cinese semplificata. 

Se desideri segnalare un errore di traduzione o un'inesattezza, non esitare a contattarci via mail.