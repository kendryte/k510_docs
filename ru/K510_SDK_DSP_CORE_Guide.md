![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 DSP CORE Руководство</font>**

<font face="黑体"  size=3>Версия документа: V1.0.0</font>

<font face="黑体"  size=3>Опубликовано: 2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Отказ**</font>
Продукты, услуги или функции, которые вы покупаете, регулируются коммерческими контрактами и условиями Beijing Canaan Jiesi Information Technology Co., Ltd. («Компания», то же самое далее), и все или часть продуктов, услуг или функций, описанных в этом документе, могут не входить в сферу вашей покупки или использования. Если иное не оговорено в договоре, Компания отказывается от всех заявлений или гарантий, явных или подразумеваемых, в отношении точности, надежности, полноты, маркетинга, конкретной цели и ненападения любых заявлений, информации или содержания этого документа. Если не согласовано иное, настоящий документ предоставляется только в качестве руководства для использования.
В связи с обновлением версии продукта или по другим причинам содержимое этого документа может время от времени обновляться или изменяться без какого-либо уведомления. 

**<font face="黑体"  size=3>Уведомления о товарных знаках</font>**

""<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, значок "Canaan", Canaan и другие товарные знаки Canaan и другие товарные знаки Canaan являются товарными знаками Beijing Canaan Jiesi Information Technology Co., Ltd. Все другие товарные знаки или зарегистрированные товарные знаки, которые могут быть упомянуты в этом документе, принадлежат их соответствующим владельцам. 

**<font face="黑体"  size=3>Copyright ©2022 Пекин Ханаан Цзеси Информационные технологии Co., Ltd</font>**
Настоящий документ применим только к разработке и проектированию платформы K510, без письменного разрешения компании, ни одно подразделение или частное лицо не может распространять часть или все содержание этого документа в любой форме. 

**<font face="黑体"  size=3>Пекин Ханаан Цзеси Информационные Технологии Co., Ltd</font>**
URL: canaan-creative.com
Бизнес-запросы: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# предисловие
**<font face="黑体"  size=5>Назначение </font>**документа
Этот документ представляет собой руководство по использованию ядра DSP K510. 

**<font face="黑体"  size=5>Объекты чтения</font>**

Основные люди, к которым относится этот документ (это руководство):

- Разработчики программного обеспечения
- Персонал технической поддержки

**<font face="黑体"  size=5>История изменений</font>**
 <font face="宋体"  size=2>Журнал изменений накапливает описание каждого обновления документа. Последняя версия документа содержит обновления для всех предыдущих версий. </font>

| Номер версии   | Изменено     | Дата пересмотра | Примечания к пересмотру |
|  :-----  |-------   |  ------  |  ------  |
| Версия 1.0.0 | Группы системного программного обеспечения | 2022-03-09 |         |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Содержание</font>**

[ОГЛАВЛЕНИЯ]

<div style="page-break-after:always"></div>

# 1 Обзор

В чипе K510 есть три процессора, из которых двухъядерные процессоры работают под управлением Linux, а ядро DSP простаивает для разработки и использования пользователями, и этот документ предоставляет ядро DSP в качестве эталонной процедуры для сопроцессора для запуска программ без операционной системы.

![](../zh/images/doc_dsp/image-dsp_1.png)

<center> Рисунок 1 блок-схема k510 </center>

# Загружена 1 программа DSP

 k510_buildroot/package/dsp_app_new — это код, который загружает DSP и запускает его в пользовательском пространстве Linux. dsp_app_new код в основном реализует загрузку прошивки DSP в указанное место и запуск DSP для запуска выполнения, его основной код выглядит следующим образом:

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

dsp_app_new скомпилированная исполняемая программа хранится в каталоге корневой файловой системы/приложения/dsp_app_new.

# 2 Печать информации DSP

 k510_buildroot/package/dsp_log — это код, который запрашивает, имеет ли ядро DSP выходные данные Журнала, которые выполняются в пользовательском пространстве Linux. dsp_log Скомпилированная исполняемая программа хранится в каталоге корневой файловой системы/app/dsp_log.

После включения dsp_log по умолчанию будет выполняться в фоновом режиме, а его конфигурационный файл: k510_buildroot/board/canaan/k510/k510_rootfs_skeleton/etc/init.d/rc.sysinit

![](../zh/images/doc_dsp/image-dsp_log.png)

# 3 DSP голые металлические демо

## 3.1 кифт

Демо-программа fft находится`/app/dsp_app_new/fft.bin`.
Исходный код демонстрационной программы fft размещен в`k510_buildroot/package/k510_evb_test/src/test/fft` каталоге. 

Перейдите в каталог /app/dsp_app_new':

- `dsp_app`: Программы, которые загружают DSP и запускают DSP (запускаются в пользовательском пространстве Linux)
- `fft.bin`: Программа DSP для голого металла

Запустите программу fft и выполните:

```shell
cd /app/dsp_app_new
./dsp_app fft.bin
```

Вы можете увидеть следующую печать:

![Демонстрация DSP](../zh/images/doc_dsp/demo_dsp.png)

Теперь прошивка, работающая на DSP, является демонстрационной программой для fct.

## 3.2 simd_umul8

Simd_umul8 находится демо-программа`/app/dsp_app_new/simd_umul8_demo.bin`.
simd_umul8 исходный код демо-программы размещается `k510_buildroot/package/k510_evb_test/src/test/simd_umul8_demo`в каталоге, основная работа выполняется следующим образом:

- В демонстрации пусть два 32-битных данных «умножаются», то есть делят каждые 32-битные данные на 4 8-битных данных, а затем умножают их соответственно, чтобы получить 4 16-битных результата, и проверьте, соответствуют ли результаты вычислений ожидаемым. Например, 0x05050505 умножение на 0x02020202 приводит к 0x000a000a000a000a.
- Если это так, как ожидалось, распечатайте `DSP SIMD UMUL8 TEST PASS`информацию, в противном случае распечатайте`DSP SIMD UMUL8 TEST FAIL` информацию

Метод запуска демонстрации:

```shell
cd /app/dsp_app_new
./dsp_app simd_umul8_demo.bin
```

Конкретные инструкции можно найти в [документации по продукту - Andes Technology](http://www.andestech.com/en/products-solutions/product-documentation/) для загрузки спецификации расширения AndeStar V5 DSP ISA .PDF (v1.0, 2019-03-25), см. Раздел 3.172. 

## 3.3 API планировщика DSP

Когда производительность ЦП не может соответствовать некоторым приложениям, можно разделить часть функции для запуска на DSP, чтобы уменьшить нагрузку на процессор. На DSP нет операционной системы, поэтому реализован диспетчер планирования задач, а код находится в каталоге k510_buildroot/package/dsp_scheduler. Задачи, выполняемые на DSP, компилируются в статические библиотеки, предварительно связанные с планировщиком DSP, и ЦП среды выполнения отправляет сообщение DSP через почтовый ящик для запуска соответствующего запуска задачи.

Пользователи могут определять приоритеты при регистрации задач, а планировщик DSP планирует задачи в соответствии с приоритетами. Возвращаемое значение функции run интерфейса запуска задачи определяет, является ли она RUN_ONCE или CONTINUE_RUN, чтобы пользователь мог сам решить, сколько раз выполняется задача.

Как отправлять сообщения в dsps через инфраструктуру почтовых ящиков Linux, пожалуйста, обратитесь к соответствующему введению в документе K510_Mailbox_Developer_Guides. Эталонная реализация находится в k510_buildroot/package/k510_evb_test/src/test/mailbox_demo/cpu2dsp_task_demo.c

### 3.3.1 Описания файлов заголовков

1. k510_buildroot/пакет/dsp_scheduler/src/dsp_tasks.h

    Программа, работающая на ЦП, должна включать этот заголовочный файл, который определяет тип сообщения и структуру между ЦП и DSP, а системное сообщение использует метод вопросов и ответов, и ЦП должен дождаться того же сообщения, отправленного DSP после отправки сообщения, чтобы указать, что DSP обработан. Пользовательские сообщения могут определять свои собственные механизмы по мере необходимости. Сообщение означает следующее:

    - DSP_TASK_ENABLE

    Когда соответствующая задача начинает выполняться, за этим сообщением может последовать адрес памяти для задачи, распечатать отладочную информацию на DSP

    - DSP_TASK_DISABLE

    Соответствующая задача перестает выполняться

    - DSP_TASK_PRINT_INFO

    Печать всех зарегистрированных сведений о задаче

    - DSP_TASK_USER_MSG

    Пользовательские сообщения задач, которые следуют за адресом памяти, позволяют пользователям создавать свои собственные механизмы очереди сообщений и передачи сообщений по мере необходимости.

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

2. k510_buildroot/пакет/dsp_scheduler/src/планировщик.h
    Программы, работающие на DSP, должны включать этот заголовочный файл

### 3.3.2 Описание функции API

#### 3.3.2.1 SCHE_TaskRegister

【Описание】

Зарегистрируйте задачу. На DSP может быть зарегистрировано до 8 задач, каждая из которых взаимодействует через канал почтового ящика и ЦП. Задача 0 соответствует номеру канала почтового ящика 0, DSP_TASK_0_CH соответствует MBOX_CHAN_0_TX почтового ящика процессора и так далее.

Реализация следующей структуры задач

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

В k510_buildroot/package/dsp_scheduler/alltasks.c зарегистрируйте задачу со следующим кодом:

```c
{
    extern DSP_TASK dsp_sample_task;
    SCHE_TaskRegister(&dsp_sample_task, DSP_TASK_0_CH);
}
```

【Грамматика】

```c
ScheStatus SCHE_TaskRegister(DSP_TASK *task, DspTaskChannel ch)
```

【Параметры】

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

【Описание】

Задачи на DSP отправляют сообщения в ЦП через этот интерфейс

```c
ScheStatus SCHE_SendMessage(DSP_MESSAGE *pMsg, DspTaskChannel ch)
```

【Параметры】

Инструкции см. в разделе 3.3.1

#### 3.2.3 SCHE_GetMessage

【Описание】

Задачи на DSP получают сообщения от ЦП через этот интерфейс

```c
ScheStatus SCHE_GetMessage(DSP_MESSAGE *pMsg, DspTaskChannel ch)
```

【Параметры】

Инструкции см. в разделе 3.3.1

### 3.3.3 Планировщик DSP применяет реальные столбцы

Выполните следующую команду, чтобы загрузить планировщик dsp программы без операционной системы:

```shell
cd /app/dsp_app_new
./dsp_app ../dsp_scheduler/scheduler.bin
```

В окне оболочки можно увидеть следующий журнал, указывающий на успешную загрузку планировщика dsp.

```text
dsp schduler start
dsp schduler: register sample task successful, ch 0
dsp schduler: register audio3a task successful, ch 1
```

Войдите в каталог /app/mailbox_demo, введите следующую команду, процессор отправит команду dsp для запуска задачи, и отправит запрос на обработку данных, dsp processing отправит сообщение, чтобы уведомить процессор, так что цикл.

```shell
cd /app/mailbox_demo
/app/mailbox_demo/cpu2dsp_task_demo
```

Просмотрите следующий журнал, показывающий, что задача, указанная процессором, заданным dsp, была успешной.

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

**Отказ от ответственности за **перевод  
Для удобства клиентов Canaan использует переводчик AI для перевода текста на несколько языков, которые могут содержать ошибки. Мы не гарантируем точность, надежность или своевременность предоставленных переводов. Компания Canaan не несет ответственности за любые убытки или ущерб, вызванные доверием к точности или надежности переведенной информации. При наличии разницы в содержании переводов на разные языки преимущественную силу имеет упрощенная версия на китайском языке. 

Если вы хотите сообщить об ошибке или неточности перевода, пожалуйста, не стесняйтесь обращаться к нам по почте.