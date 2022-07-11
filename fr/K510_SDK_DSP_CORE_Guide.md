![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 DSP CORE Guide</font>**

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
Ce document est un guide pour l'utilisation du noyau DSP K510.

**<font face="黑体"  size=5>Objets de lecture</font>**

Les principales personnes auxquelles ce document (ce guide) s'applique :

- Développeurs de logiciels
- Personnel de soutien technique

**<font face="黑体"  size=5>Historique des révisions</font>**
 <font face="宋体"  size=2>L'historique des révisions accumule une description de chaque mise à jour de document. La dernière version du document contient des mises à jour pour toutes les versions précédentes. </font>

| Le numéro de version   | Modifié par     | Date de révision | Notes de révision |
|  :-----  |-------   |  ------  |  ------  |
| Version 1.0.0 | Groupes de logiciels système | 2022-03-09 |         |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenu</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Vue d'ensemble

Il y a trois processeurs dans la puce K510, dont les deux cœurs cpu exécutent Linux, et le cœur DSP est inactif pour que les utilisateurs puissent le développer et l'utiliser, et ce document fournit le cœur DSP comme routine de référence pour que le coprocesseur exécute des programmes bare metal.

![](../zh/images/doc_dsp/image-dsp_1.png)

<center> Figure 1 Diagramme fonctionnel k510 </center>

# 1 programme DSP chargé

 k510_buildroot/package/dsp_app_new, est le code qui charge le DSP et l'exécute dans l'espace utilisateur Linux. dsp_app_new code implémente principalement le chargement du firmware DSP à l'emplacement spécifié et le démarrage du DSP pour démarrer l'exécution, son code principal est le suivant:

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

dsp_app_new programme exécutable compilé est stocké dans le répertoire du système de fichiers racine/app/dsp_app_new.

# 2 Impression d'informations DSP

 k510_buildroot/package/dsp_log, est le code qui interroge si le cœur DSP dispose d'une sortie Log, qui s'exécute dans l'espace utilisateur Linux. dsp_log Le programme exécutable compilé est stocké dans le répertoire du système de fichiers racine/app/dsp_log.

Après la mise sous tension, le dsp_log sera exécuté en arrière-plan par défaut, et son fichier de configuration est : k510_buildroot/board/canaan/k510/k510_rootfs_skeleton/etc/init.d/rc.sysinit

![](../zh/images/doc_dsp/image-dsp_log.png)

# 3 Démo bare metal DSP

## 3,1 fft

Le programme de démonstration fft est localisé`/app/dsp_app_new/fft.bin`.
Le code source du programme de démonstration fft est placé dans`k510_buildroot/package/k510_evb_test/src/test/fft` le répertoire.

Accédez au répertoire /app/dsp_app_new' :

- `dsp_app`: Programmes qui chargent le DSP et font fonctionner le dsp (exécuté dans l'espace utilisateur Linux)
- `fft.bin`: Programme bare metal DSP

Démarrez le programme fft et exécutez :

```shell
cd /app/dsp_app_new
./dsp_app fft.bin
```

Vous pouvez voir l'impression suivante :

![Démo DSP](../zh/images/doc_dsp/demo_dsp.png)

Maintenant, le firmware fonctionnant sur DSP est un programme de démonstration pour fct.

## 3.2 simd_umul8

Simd_umul8 programme de démonstration est situé`/app/dsp_app_new/simd_umul8_demo.bin`.
simd_umul8 le code source du programme de démonstration est placé `k510_buildroot/package/k510_evb_test/src/test/simd_umul8_demo`dans le répertoire, le travail principal effectué est le suivant:

- Dans la démo, laissez deux données 32 bits « se multiplier », c'est-à-dire divisez chaque donnée 32 bits en 4 données 8 bits, puis multipliez-les respectivement pour obtenir 4 résultats 16 bits, et vérifiez si les résultats de calcul sont comme prévu. Par exemple, 0x05050505 multiplié par 0x02020202 entraîne 0x000a000a000a000a.
- Si c'est comme prévu, imprimez `DSP SIMD UMUL8 TEST PASS`les informations, sinon imprimez`DSP SIMD UMUL8 TEST FAIL` les informations

Méthode pour exécuter la démo:

```shell
cd /app/dsp_app_new
./dsp_app simd_umul8_demo.bin
```

Vous trouverez des instructions spécifiques dans [la documentation produit - Andes Technology](http://www.andestech.com/en/products-solutions/product-documentation/) pour télécharger la spécification andeStar V5 DSP ISA Extension .PDF (v1.0, 2019-03-25), voir Section 3.172.

## 3.3 API du planificateur DSP

Lorsque les performances du processeur ne peuvent pas répondre à certaines applications, vous pouvez diviser une partie de la fonction à exécuter sur le DSP pour réduire la charge du processeur. Il n'y a pas de système d'exploitation sur le DSP, donc un gestionnaire de planification des tâches est implémenté, et le code est dans le répertoire de k510_buildroot/package/dsp_scheduler. Les tâches exécutées sur le DSP sont compilées dans des bibliothèques statiques, pré-liées au planificateur DSP, et le processeur d'exécution envoie un message au dsp via la boîte aux lettres pour démarrer l'exécution de la tâche correspondante.

Les utilisateurs peuvent définir des priorités lors de l'inscription des tâches, et le planificateur DSP planifie les tâches en fonction des priorités. La valeur de retour de la fonction d'exécution de l'interface d'exécution de tâche détermine si elle est RUN_ONCE ou CONTINUE_RUN, afin que l'utilisateur puisse décider lui-même combien de fois la tâche est exécutée.

Comment envoyer des messages à dsps via l'infrastructure de boîte aux lettres Linux, veuillez vous référer à l'introduction correspondante dans le document K510_Mailbox_Developer_Guides. L'implémentation de référence se trouve dans k510_buildroot/package/k510_evb_test/src/test/mailbox_demo/cpu2dsp_task_demo.c

### 3.3.1 Descriptions des fichiers d'en-tête

1. k510_buildroot/package/dsp_scheduler/src/dsp_tasks.h

    Le programme exécuté sur le processeur doit inclure ce fichier d'en-tête, qui définit le type de message et la structure entre le processeur et le dsp, et la communication de message système adopte une méthode de questions-réponses, et le processeur doit attendre le même message envoyé par le dsp après l'envoi du message pour indiquer que le dsp est traité. Les messages utilisateur peuvent définir leurs propres mécanismes selon les besoins. Le message signifie ce qui suit :

    - DSP_TASK_ENABLE

    Lorsque la tâche correspondante commence à s'exécuter, ce message peut être suivi d'une adresse mémoire pour les informations de débogage d'impression de la tâche sur le dsp

    - DSP_TASK_DISABLE

    La tâche correspondante cesse de s'exécuter

    - DSP_TASK_PRINT_INFO

    Imprime toutes les informations de tâche enregistrées

    - DSP_TASK_USER_MSG

    Les messages de tâche définis par l'utilisateur, qui suivent une adresse mémoire, permettent aux utilisateurs de concevoir leurs propres mécanismes de mise en file d'attente et de communication de messages selon les besoins.

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
    Les programmes s'exécutant sur dsp nécessitent d'inclure ce fichier d'en-tête

### 3.3.2 Description de la fonction API

#### 3.3.2.1 SCHE_TaskRegister

【Description】

Enregistrer une tâche. Jusqu'à 8 tâches peuvent être enregistrées sur le DSP, chacune communiquant via un canal de boîte aux lettres et un processeur. La tâche 0 correspond au numéro de canal de boîte aux lettres de 0, DSP_TASK_0_CH correspond à la MBOX_CHAN_0_TX de la boîte aux lettres du processeur, etc.

Implémenter la structure de tâches suivante

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

Dans k510_buildroot/package/dsp_scheduler/alltasks.c, enregistrez la tâche avec le code suivant :

```c
{
    extern DSP_TASK dsp_sample_task;
    SCHE_TaskRegister(&dsp_sample_task, DSP_TASK_0_CH);
}
```

【Grammaire】

```c
ScheStatus SCHE_TaskRegister(DSP_TASK *task, DspTaskChannel ch)
```

【Paramètres】

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

Les tâches sur le dsp envoient des messages au processeur via cette interface

```c
ScheStatus SCHE_SendMessage(DSP_MESSAGE *pMsg, DspTaskChannel ch)
```

【Paramètres】

Voir la section 3.3.1 pour obtenir des instructions.

#### 3.2.3 SCHE_GetMessage

【Description】

Les tâches sur le dsp reçoivent des messages du processeur via cette interface

```c
ScheStatus SCHE_GetMessage(DSP_MESSAGE *pMsg, DspTaskChannel ch)
```

【Paramètres】

Voir la section 3.3.1 pour obtenir des instructions.

### 3.3.3 DSP Scheduler applique des colonnes réelles

Exécutez la commande suivante pour charger le planificateur dsp du programme bare metal :

```shell
cd /app/dsp_app_new
./dsp_app ../dsp_scheduler/scheduler.bin
```

Dans la fenêtre shell, vous pouvez voir le journal suivant, indiquant que le planificateur dsp est correctement chargé.

```text
dsp schduler start
dsp schduler: register sample task successful, ch 0
dsp schduler: register audio3a task successful, ch 1
```

Entrez le répertoire /app/mailbox_demo, entrez la commande suivante, le processeur enverra une commande à dsp pour démarrer une tâche et enverra une demande pour traiter les données, le traitement dsp enverra un message pour notifier le processeur, de sorte que la boucle.

```shell
cd /app/mailbox_demo
/app/mailbox_demo/cpu2dsp_task_demo
```

Consultez le journal suivant, indiquant que la tâche spécifiée par le processeur spécifié par dsp a réussi.

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

**Clause de non-responsabilité en matière de**  
Pour la commodité des clients, Canaan utilise un traducteur IA pour traduire du texte en plusieurs langues, ce qui peut contenir des erreurs. Nous ne garantissons pas l'exactitude, la fiabilité ou l'actualité des traductions fournies. Canaan ne sera pas responsable de toute perte ou dommage causé par la confiance accordée à l'exactitude ou à la fiabilité des informations traduites. S'il existe une différence de contenu entre les traductions dans différentes langues, la version simplifiée en chinois prévaudra.

Si vous souhaitez signaler une erreur de traduction ou une inexactitude, n'hésitez pas à nous contacter par courrier.
