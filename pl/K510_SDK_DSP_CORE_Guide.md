![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 DSP CORE Przewodnik</font>**

<font face="黑体"  size=3>Wersja dokumentu: V1.0.0</font>

<font face="黑体"  size=3>Opublikowano: 2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Zrzeczenie się**</font>
Zakupione produkty, usługi lub funkcje podlegają umowom handlowym i warunkom Beijing Canaan Jiesi Information Technology Co., Ltd. ("Spółka", ta sama poniżej), a wszystkie lub część produktów, usług lub funkcji opisanych w niniejszym dokumencie może nie być objęta zakresem zakupu lub użytkowania. O ile nie uzgodniono inaczej w umowie, Firma zrzeka się wszelkich oświadczeń lub gwarancji, wyraźnych lub dorozumianych, co do dokładności, niezawodności, kompletności, marketingu, konkretnego celu i nieagresji jakichkolwiek oświadczeń, informacji lub treści tego dokumentu. O ile nie uzgodniono inaczej, niniejszy dokument jest dostarczany jako wskazówka wyłącznie do użytku.
Ze względu na aktualizacje wersji produktu lub z innych powodów zawartość tego dokumentu może być od czasu do czasu aktualizowana lub modyfikowana bez powiadomienia. 

**<font face="黑体"  size=3>Informacje o znakach towarowych</font>**

""<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, ikona "Canaan", Canaan i inne znaki towarowe Canaan oraz inne znaki towarowe Canaan są znakami towarowymi Beijing Canaan Jiesi Information Technology Co., Ltd. Wszystkie inne znaki towarowe lub zarejestrowane znaki towarowe, które mogą być wymienione w niniejszym dokumencie, są własnością ich odpowiednich właścicieli. 

**<font face="黑体"  size=3>Prawa autorskie ©2022 Beijing Canaan Jiesi Information Technology Co., Ltd</font>**
Niniejszy dokument ma zastosowanie wyłącznie do rozwoju i projektowania platformy K510, bez pisemnej zgody firmy, żadna jednostka ani osoba fizyczna nie może rozpowszechniać części lub całości treści tego dokumentu w jakiejkolwiek formie. 

**<font face="黑体"  size=3>Pekin Canaan Jiesi Information Technology Co Ltd</font>**
Adres internetowy: canaan-creative.com
Zapytania biznesowe: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# przedmowa
**<font face="黑体"  size=5>Przeznaczenie </font>**dokumentu
Ten dokument jest przewodnikiem dotyczącym korzystania z rdzenia DSP K510. 

**<font face="黑体"  size=5>Obiekty programu Reader</font>**

Główne osoby, których dotyczy ten dokument (ten przewodnik):

- Programiści
- Personel wsparcia technicznego

**<font face="黑体"  size=5>Historia</font>**
 zmian <font face="宋体"  size=2>Historia zmian gromadzi opis każdej aktualizacji dokumentu. Najnowsza wersja dokumentu zawiera aktualizacje dla wszystkich poprzednich wersji. </font>

| Numer wersji   | Zmodyfikowane przez     | Data aktualizacji | Uwagi do poprawek |
|  :-----  |-------   |  ------  |  ------  |
| Wersja 1.0.0 | Grupy oprogramowania systemowego | 2022-03-09 |         |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Treść</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Przegląd

W układzie K510 znajdują się trzy procesory, z których procesor Dwurdzeniowy działa pod kontrolą systemu Linux, a rdzeń DSP jest bezczynny dla użytkowników do opracowania i używania, a ten dokument zawiera rdzeń DSP jako procedurę referencyjną dla koprocesora do uruchamiania programów fizycznych.

![](../zh/images/doc_dsp/image-dsp_1.png)

<center> Rysunek 1 k510 schemat blokowy </center>

# Załadowano 1 program DSP

 k510_buildroot katalogu/package/dsp_app_new jest kodem, który ładuje DSP i uruchamia go w przestrzeni użytkownika Linuksa. dsp_app_new kod implementuje głównie ładowanie oprogramowania układowego DSP do określonej lokalizacji i uruchamianie DSP w celu rozpoczęcia wykonywania, jego główny kod jest następujący:

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

dsp_app_new skompilowany program wykonywalny jest przechowywany w katalogu głównego systemu plików/aplikacji/dsp_app_new.

# 2 Drukowanie informacji DSP

 k510_buildroot/package/dsp_log to kod, który, czy rdzeń DSP ma dane wyjściowe dziennika, które działają w przestrzeni użytkownika systemu Linux. dsp_log Skompilowany program wykonywalny jest przechowywany w katalogu głównego systemu plików/app/dsp_log.

Po włączeniu zasilania dsp_log będzie domyślnie wykonywany w tle, a jego plik konfiguracyjny to: k510_buildroot/board/canaan/k510/k510_rootfs_skeleton/etc/init.d/rc.sysinit

![](../zh/images/doc_dsp/image-dsp_log.png)

# 3 DSP bare metal demo

## 3.1 fft

Znajduje się program demonstracyjny fft`/app/dsp_app_new/fft.bin`.
Kod źródłowy programu demonstracyjnego fft jest umieszczony w`k510_buildroot/package/k510_evb_test/src/test/fft` katalogu. 

Przejdź do katalogu /app/dsp_app_new':

- `dsp_app`: Programy, które ładują DSP i uruchamiają dsp (uruchamiają w przestrzeni użytkownika Linuksa)
- `fft.bin`: Program DSP bare metal

Uruchom program fft i uruchom:

```shell
cd /app/dsp_app_new
./dsp_app fft.bin
```

Możesz zobaczyć następujący wydruk:

![DSP Demo](../zh/images/doc_dsp/demo_dsp.png)

Teraz oprogramowanie układowe działające na DSP jest programem demonstracyjnym dla fct.

## 3.2 simd_umul8

Simd_umul8 znajduje się program demonstracyjny`/app/dsp_app_new/simd_umul8_demo.bin`.
simd_umul8 kod źródłowy programu demonstracyjnego zostanie umieszczony`k510_buildroot/package/k510_evb_test/src/test/simd_umul8_demo` w katalogu, główna praca wykonana jest następująca:

- W wersji demonstracyjnej pozwól dwóm 32-bitowym danym "pomnożyć", to znaczy podzielić każde 32-bitowe dane na 4 8-bitowe dane, a następnie pomnożyć je odpowiednio, aby uzyskać 4 wyniki 16-bitowe i sprawdzić, czy wyniki obliczeń są zgodne z oczekiwaniami. Na przykład 0x05050505 pomnożony przez 0x02020202 daje 0x000a000a000a000a.
- Jeśli jest zgodnie z oczekiwaniami, wydrukuj`DSP SIMD UMUL8 TEST PASS` informacje, w przeciwnym razie wydrukuj`DSP SIMD UMUL8 TEST FAIL` informacje

Metoda uruchamiania demo:

```shell
cd /app/dsp_app_new
./dsp_app simd_umul8_demo.bin
```

Szczegółowe instrukcje można znaleźć w [Dokumentacji produktu - Andes Technology](http://www.andestech.com/en/products-solutions/product-documentation/) , aby pobrać AndeStar V5 DSP ISA Extension Specification .PDF (v1.0, 2019-03-25), patrz Rozdział 3.172. 

## 3.3 Interfejs API harmonogramu DSP

Gdy wydajność procesora nie może spełnić niektórych aplikacji, można podzielić część funkcji, aby uruchomić ją na procesorze DSP, aby zmniejszyć obciążenie procesora. Na dsP nie ma systemu operacyjnego, więc zaimplementowany jest menedżer planowania zadań, a kod znajduje się w katalogu k510_buildroot/package/dsp_scheduler. Zadania uruchomione na dsp są kompilowane do bibliotek statycznych, wstępnie połączone z harmonogramem DSP, a procesor środowiska wykonawczego wysyła komunikat do dsp za pośrednictwem skrzynki pocztowej, aby rozpocząć odpowiednie uruchomienie zadania.

Użytkownicy mogą definiować priorytety podczas rejestrowania zadań, a harmonogram DSP planuje zadania zgodnie z priorytetami. Zwracana wartość funkcji uruchamiania interfejsu uruchamiania zadania określa, czy jest on RUN_ONCE, czy CONTINUE_RUN, dzięki czemu użytkownik może sam zdecydować, ile razy zadanie jest wykonywane.

Jak wysyłać wiadomości do dsps za pośrednictwem struktury skrzynek pocztowych Linux, zapoznaj się z odpowiednim wprowadzeniem w dokumencie K510_Mailbox_Developer_Guides. Implementacja referencyjna znajduje się w k510_buildroot/package/k510_evb_test/src/test/mailbox_demo/cpu2dsp_task_demo.c

### 3.3.1 Opisy plików nagłówkowych

1. k510_buildroot/pakiet/dsp_scheduler/src/dsp_tasks.h

    Program uruchomiony na procesorze musi zawierać ten plik nagłówka, który definiuje typ i strukturę wiadomości między procesorem a dsp, a komunikacja komunikatu systemowego przyjmuje metodę pytań i odpowiedzi, a procesor musi poczekać, aż ten sam komunikat zostanie wysłany przez dsp po wysłaniu wiadomości, aby wskazać, że dsp jest przetwarzany. Komunikaty użytkowników mogą w razie potrzeby definiować własne mechanizmy. Komunikat oznacza:

    - DSP_TASK_ENABLE

    Gdy odpowiednie zadanie zaczyna działać, po tym komunikacie może nastąpić adres pamięci dla informacji o debugowaniu wydruku zadania w dsp

    - DSP_TASK_DISABLE

    Odpowiednie zadanie przestaje działać

    - DSP_TASK_PRINT_INFO

    Drukuje wszystkie zarejestrowane informacje o zadaniu

    - DSP_TASK_USER_MSG

    Zdefiniowane przez użytkownika komunikaty zadań, które następują po adresie pamięci, umożliwiają użytkownikom projektowanie własnych mechanizmów kolejkowania wiadomości i komunikacji wiadomości w razie potrzeby

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
    Programy działające na dsp wymagają dołączenia tego pliku nagłówka

### 3.3.2 Opis funkcji API

#### 3.3.2.1 SCHE_TaskRegister

【Opis】

Zarejestruj zadanie. Na procesorze DSP można zarejestrować do 8 zadań, z których każde komunikuje się za pośrednictwem kanału skrzynki pocztowej i procesora. Zadanie 0 odpowiada numerowi kanału skrzynki pocztowej 0, DSP_TASK_0_CH odpowiada MBOX_CHAN_0_TX skrzynki pocztowej procesora i tak dalej.

Implementacja następującej struktury zadań

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

W k510_buildroot/package/dsp_scheduler/alltasks.c zarejestruj zadanie za pomocą następującego kodu:

```c
{
    extern DSP_TASK dsp_sample_task;
    SCHE_TaskRegister(&dsp_sample_task, DSP_TASK_0_CH);
}
```

【Gramatyka】

```c
ScheStatus SCHE_TaskRegister(DSP_TASK *task, DspTaskChannel ch)
```

【Parametry】

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

【Opis】

Zadania na dsp wysyłają komunikaty do procesora za pośrednictwem tego interfejsu

```c
ScheStatus SCHE_SendMessage(DSP_MESSAGE *pMsg, DspTaskChannel ch)
```

【Parametry】

Patrz sekcja 3.3.1, aby uzyskać instrukcje.

#### 3.2.3 SCHE_GetMessage

【Opis】

Zadania na dsp odbierają komunikaty z procesora za pośrednictwem tego interfejsu

```c
ScheStatus SCHE_GetMessage(DSP_MESSAGE *pMsg, DspTaskChannel ch)
```

【Parametry】

Patrz sekcja 3.3.1, aby uzyskać instrukcje.

### 3.3.3 Harmonogram DSP stosuje rzeczywiste kolumny

Uruchom następujące polecenie, aby załadować harmonogram dsp programu od zera:

```shell
cd /app/dsp_app_new
./dsp_app ../dsp_scheduler/scheduler.bin
```

W oknie powłoki można zobaczyć następujący dziennik, wskazujący, że harmonogram dsp został pomyślnie załadowany.

```text
dsp schduler start
dsp schduler: register sample task successful, ch 0
dsp schduler: register audio3a task successful, ch 1
```

Wprowadź katalog /app/mailbox_demo, wprowadź następujące polecenie, procesor wyśle polecenie do dsp, aby rozpocząć zadanie, i wyśle żądanie przetworzenia danych, przetwarzanie dsp wyśle komunikat, aby powiadomić procesor, aby pętla.

```shell
cd /app/mailbox_demo
/app/mailbox_demo/cpu2dsp_task_demo
```

Zobacz poniższy dziennik, wskazujący, że zadanie określone przez procesor określony przez dsp powiodło się.

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

**Zrzeczenie się odpowiedzialności za **tłumaczenie  
Dla wygody klientów Canaan używa tłumacza AI do tłumaczenia tekstu na wiele języków, które mogą zawierać błędy. Nie gwarantujemy dokładności, rzetelności ani terminowości dostarczonych tłumaczeń. Canaan nie ponosi odpowiedzialności za jakiekolwiek straty lub szkody spowodowane poleganiem na dokładności lub wiarygodności przetłumaczonych informacji. W przypadku różnic w treści tłumaczeń w różnych językach, pierwszeństwo ma chińska wersja uproszczona. 

Jeśli chcesz zgłosić błąd lub niedokładność tłumaczenia, skontaktuj się z nami pocztą.