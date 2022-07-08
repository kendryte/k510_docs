![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">Guida alla compilazione e alla masterizzazione di K510 SDK</font>**

<font face="黑体"  size=3>Versione del documento: V1.0.0</font>

<font face="黑体"  size=3>Data di pubblicazione: 2022-03-07</font>

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
Questo documento è un documento complementare all'sdk K510 e ha lo scopo di aiutare gli ingegneri a comprendere la compilazione e la masterizzazione dell'sdk K510. 

**<font face="黑体"  size=5>Oggetti lettore</font>**

Le principali persone a cui si applica questo documento (questa guida):

- Sviluppatori di software
- Personale di supporto tecnico

**<font face="黑体"  size=5>Cronologia delle revisioni</font>**
 <font face="宋体"  size=2>La cronologia delle revisioni accumula una descrizione di ogni aggiornamento del documento. La versione più recente del documento contiene gli aggiornamenti per tutte le versioni precedenti. </font>

| Il numero di versione   | Modificato da     | Data della revisione | Note di revisione |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 · | Divisione Prodotti AI | 2022-03-07 |          |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenuto</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Introduzione

In questo documento viene descritto il contenuto della sezione relativa alla costruzione dell'ambiente di sviluppo, ad esempio il download, la compilazione e la masterizzazione dell'SDK K510.

# 2 K510 SDK

## 2.1 k510 sdk scaricare

Indirizzo del progetto SDK k510: <https://github.com/kendryte/k510_buildroot>

Scarica l'SDK k510:

```shell
git clone https://github.com/kendryte/k510_buildroot.git
```

## 2.2 Introduzione al pacchetto sdk k510

L'SDK K510 è un ambiente di sviluppo Linux embedded basato su buildroot come framework di base, basato sul kernel linux K510 (linux versione 4.17.0), u-boot (u-boot versione 2020.01), riscv-pk-k510 (BBL) pacchetto di codice sorgente, la struttura di directory K510 SDK è mostrata nella figura seguente.

![](../zh/images/sdk_build/image-buildroot.png)

 I file SDK K510 sono descritti come segue:

| **file**        | **Descrizione del contenuto**                                                 |
| --------------- | ------------------------------------------------------------ |
| tavola           | Cartella, che è K510 vari file di configurazione e script, come il file di configurazione per la generazione di immagini (genimage-xxx.cfg), buildroot post-image scripts, U-Boot variabili di ambiente predefinite, ecc. |
| Config.in       | Indica il pacchetto che richiede la compilazione buildroot. |
| configurazioni         | Cartella, dove si trova il file di configurazione di compilazione predefinito della scheda. Attualmente salva i file di configurazione di compilazione predefiniti per le schede K510 CRB-V0.1, K510 CRB-V1.2 e K510 EVB:<br /> -`k510_crb_lp3_v1_2_defconfig`<br />-`k510_crb_lp3_v0_1_defconfig`<br />- `k510_evb_lp3_v1_1_defconfig` |
| external.desc   | File di configurazione del meccanismo esterno di Buildroot. |
| external.mk     | |
| Makefile        | Il Makefile principale dell'SDK k510. |
| pacco         | Le cartelle, che sono principalmente applicazioni K510, Config.in il contenuto del file determineranno quali applicazioni vengono compilate in quella directory. |
| Patch         | Cartella, dove è il file di patch buildroot, Makefile decomprimerà il codice sorgente quando il file di patch in questa directory nella directory del codice sorgente corrispondente. |
| pkg-scaricare    | Cartella, che è un pacchetto compresso della cartella dl. |
| README.md       | Istruzioni relative all'SDK. |
| release_note.md | |
| toolchain       | , dove si trova la toolchain di compilazione incrociata. |
| Dl              | Folder, è il pacchetto di estrazione dl in pkg-download, se ci sono altri pacchetti aggiunti verrà scaricato anche in questa directory. |

## 2.3 k510 versione sdk

Quando si masterizza l'immagine generata dall'sdk k510 sulla scheda, vengono stampate le informazioni sulla versione, come illustrato nella figura seguente:

```text
#############SDK VERSION############################################
MX2_DEV_0106-02e87077-20220428-153936CST-xxxxx-server
####################################################################
```

Al termine dell'avvio, immettere quanto segue nel terminale della shell per visualizzare le informazioni sulla versione dell'SDK:

```shell
cat /etc/version/release_version
#############SDK VERSION############################################
MX2_REL_0106-02e87077-20220428-153936CST-xxxx-server
####################################################################
```

**Nota: le informazioni di cui sopra possono variare a seconda della versione di k510 sdk**. 

# 3 ambiente di compilazione docker

Dopo aver scaricato l'sdk k510, eseguire il seguente comando nella directory padre dell'sdk per avviare la finestra mobile:

```shell
sh k510_buildroot/tools/docker/run_k510_docker.sh
```

Le successive operazioni di compilazione vengono eseguite in docker per impostazione predefinita.
Se è necessario configurare un ambiente locale, fare riferimento a Configurazione[ ambiente locale](#env_set)

# 4 Compilare

## 4.1 Preparazione alla compilazione

### 4.1.1 Scarica il pacchetto del codice sorgente (opzionale, può velocizzare la compilazione)

Eseguire il comando seguente per scaricare il pacchetto di origine:

```shell
make dl
```

## 4.2 Compilazione

K510_buildroot/config contiene file di configurazione di compilazione per tre schede di sviluppo, ovvero`k510_crb_lp3_v0_1_defconfig` , e`k510_crb_lp3_v1_2_defconfig`  `k510_evb_lp3_v1_1_defconfig`, questo documento è illustrato selezionando k510_crb_lp3_v1_2_defconfig come destinazione di compilazione****. 

Nell'ambiente docker k510, immettere il comando seguente per avviare la compilazione:

```shell
make CONF=k510_crb_lp3_v1_2_defconfig
```

![](../zh/images/sdk_build/image-make.png)

Il messaggio seguente indica che la compilazione è stata completata correttamente.

![](../zh/images/sdk_build/image-uboot_r.png)

Al termine della compilazione, viene generata la cartella`k510_crb_lp3_v1_2_defconfig`. 

![immagine-20220311121912711](../zh/images/sdk_build/image-makeout.png)

Ognuno di questi documenti è descritto come segue:

| **file**    | **Descrizione del contenuto**                                                 |
| ----------- | ------------------------------------------------------------ |
| Makefile    | Compilare l'immagine per utilizzare Makefile.                                     |
| costruire       | Directory di compilazione per tutti i pacchetti di origine. Ad esempio, kernel linux, u-boot, BBL, busybox, ecc., Il codice sorgente verrà estratto nella directory di compilazione e compilato. |
| ospite        | Tutti i percorsi di installazione del pacchetto host, toolchain verranno copiati anche in questa directory per la creazione di ambienti di compilazione incrociata. |
| Immagini      | Compilare la directory del file di destinazione risultante (vedere le istruzioni riportate di seguito per i dettagli)                     |
| nand_target | Directory raw del file system root (utilizzata per generare immagini NandFlash)                  |
| bersaglio      | Directory raw del file system root (per generare immagini eMMC e schede SD da utilizzare)                 |

K510_crb_lp3_v1_2_defconfig/images directory è un'immagine masterizzata, in cui la descrizione di ciascun file è la seguente.

| **file**                   | **Descrizione del contenuto**                                                 |
| -------------------------- | ------------------------------------------------------------ |
| bootm-bbl.img              | Immagine del kernel Linux+bbl (file di destinazione bpl del kernel pacchettizzato per uboot boot bbl) |
| k510.dtb                   | Albero dei dispositivi                                                       |
| sysimage-emmc.img          | emmc masterizzare file: l'intero pacchetto è stato impacchettato uboot_burn, kernel e bbl              |
| sysImage-sdcard.img        | sdcard masterizzare file: l'intero pacchetto è stato impacchettato uboot_burn, kernel e bbl            |
| sysImage-nand.img          | nand masterizzare file: l'intero pacchetto è stato impacchettato uboot_burn, kernel e bbl              |
| u-boot.bin                 | UBOOT file binario                                             |
| u-boot_burn.bin            | uboot masterizza i file                                               |
| uboot-emmc.itv             | Variabile di ambiente uboot: utilizzata per l'avvio di EMMC                                  |
| uboot-sd.itv               | Variabile di ambiente uboot: utilizzata per l'avvio di SDCard                                |
| uboot-nand.itv             | Variabile di ambiente uboot: utilizzata per l'avvio nand                                  |
| vmlinux                    | File immagine del kernel Linux (con informazioni sul debug degli elfi)                           |
| rootfs.ext2                | File immagine ext2 rootfs formato Buildroot                             |
| sysimage-sdcard-debian.img | sdcard masterizzare file: immagini di schede (rootfs in formato debian)                     |

K510_crb_lp3_v1_2_defconfig/build è il codice sorgente di tutti gli oggetti compilati, molti dei quali sono documenti importanti descritti di seguito.

| **file**         | **Descrizione del contenuto**                  |
| ---------------- | ----------------------------- |
| linux-xxx        | La directory sorgente del kernel Linux compilata |
| uboot-xxx        | La directory di origine Uboot compilata       |
| riscv-hp-k510-xxx| La directory di origine bbl in cui viene compilato il codice         |
| ...              |                               |

Nota: xxx è il numero di versione. Quando i riferimenti ai percorsi di kernle, bbl e uboot nelle sezioni successive, xxx rappresentano tutti i numeri di versione.

** Hai bisogno di particolare attenzione: ** Quando si pulisce, tutto sotto la cartella k510_crb_lp3_v1_2_defconfig verrà eliminato. Pertanto, se è necessario modificare il kernel, bbl o il codice uboot, non modificarlo direttamente nella directory di compilazione, è possibile fare riferimento al Capitolo 5 per utilizzare il metodo di override source.

## 4.1 Configurare buildroot

Immettere il comando buildroot di configurazione nell'ambiente docker k510:

```shell
make CONF=k510_crb_lp3_v1_2_defconfig menuconfig
```

I risultati dell'esecuzione sono i seguenti:

![](../zh/images/sdk_build/image-make_men.png)

![](../zh/images/sdk_build/image-make_menu.png)

Dopo aver completato la configurazione, salvare e uscire, è inoltre necessario eseguire il seguente comando buildroot configuration save:

```shell
make CONF=k510_crb_lp3_v1_2_defconfig savedefconfig
```

I risultati dell'esecuzione sono i seguenti:

![](../zh/images/sdk_build/image-make_savedef.png)

Al termine dell'operazione di cui sopra, l'utente può immettere il seguente comando per ricompilare:

```shell
make CONF=k510_crb_lp3_v1_2_defconfig
```

## 4.2 Configurare U-Boot

Quando è necessario modificare la configurazione uboot, è possibile accedere alla directory k510_crb_lp3_v1_2_defconfig e immettere il seguente comando per avviare la configurazione U-Boot:

```shell
make uboot-menuconfig
```

I risultati dell'esecuzione sono i seguenti:

![](../zh/images/sdk_build/image-uboot_men.png)

![](../zh/images/sdk_build/image-uboot_menu.png)

Quando si esce dal menuuonfig dopo aver completato la configurazione, selezionare Salva configurazione ed è necessario eseguire il seguente comando di salvataggio della configurazione:

```shell
make uboot-savedefconfig
```

I risultati dell'esecuzione sono i seguenti:

![](../zh/images/sdk_build/image-uboot_savedefconfig.png)

Infine, nella directory k510_crb_lp3_v1_2_defconfig, immettere il seguente comando per avviare la compilazione:

```shell
make uboot-rebuild
```

Per ulteriori informazioni, vedere la descrizione nella sezione successiva.

## 4.3 Compilare l'U-Boot

Il codice sorgente U-Boot compilato viene memorizzato nella directory k510_crb_lp3_v1_2_defconfig/build/uboot-xxx e u-Boot deve essere ricompilato se l'utente modifica il codice sorgente U-Boot o riconfigura l'uboot.

Immettere la directory k510_crb_lp3_v1_2_defconfig e immettere il seguente comando per ricompilare U-Boot:

```shell
make uboot-rebuild
```

I risultati dell'esecuzione sono i seguenti:

![](../zh/images/sdk_build/image-uboot-rebuild.png)

Al termine della compilazione, viene generato un nuovo file di .bin u-boot nella directory k510_crb_lp3_v1_2_defconfig/images.

Se si desidera rigenerare il file di immagine masterizzato con un nuovo u-boot,`k510_crb_lp3_v1_2_defconfig` eseguire :nella directory

```shell
make
```

I risultati dell'esecuzione sono i seguenti:

![](../zh/images/sdk_build/image-make_u.png)

Al termine della compilazione, verranno visualizzate le informazioni generate dal seguente file di immagine.

![](../zh/images/sdk_build/image-uboot_r.png)

## 4.4 Configurare il kernel Linux

Quando è necessario modificare la configurazione del kernel, è possibile inserire la directory k510_crb_lp3_v1_2_defconfig e immettere il seguente comando per avviare la configurazione del kernel:

```shell
make linux-menuconfig
```

I risultati dell'esecuzione sono i seguenti:

![](../zh/images/sdk_build/image-linux_men.png)

![](../zh/images/sdk_build/image-linux_menu.png)

Quando si esce da menuufig dopo aver modificato la configurazione, selezionare Salva configurazione e infine eseguire il seguente comando di salvataggio della configurazione:

```shell
make linux-savedefconfig
```

I risultati dell'esecuzione sono i seguenti:

![](../zh/images/sdk_build/image-linux_savedefconfig.png)

Infine, nella directory k510_crb_lp3_v1_2_defconfig, immettere il seguente comando per avviare la compilazione:

```shell
make linux-rebuild
```

Per ulteriori informazioni, vedere la descrizione nella sezione successiva.

## 4.5 Compilare il kernel Linux

K510_crb_lp3_v1_2_defconfig directory /build/linux-xxx contiene il codice sorgente Linux compilato, sia che l'utente modifichi il codice sorgente Linux o riconfiguri Linux, deve essere ricompilato.

Inserisci la directory k510_crb_lp3_v1_2_defconfig e inserisci il seguente comando per ricompilare linux:

```shell
make linux-rebuild
```

I risultati dell'esecuzione sono i seguenti:

![](../zh/images/sdk_build/image-linux_rebuild.png)

Dopo la compilazione, viene generato un nuovo vmlinux nella directory k510_crb_lp3_v1_2_defconfig/images.

L'immagine del kernel Linux deve essere impacchettata con bbl, dopo aver riscritto il kernel Linux, è necessario ricompilare il bbl per generare una nuova immagine bbl / kernel per l'avvio, quindi immettere i seguenti due comandi.

```shell
make riscv-pk-k510-dirclean
make riscv-pk-k510
```

I risultati dell'esecuzione sono i seguenti:

![](../zh/images/sdk_build/image-riscv.png)

Al termine della compilazione, `k510_crb_lp3_v1_2_defconfig/images`ne viene generata una nuova nella directory`bootm-bbl.img`. 

Infine, inserisci make nella directory k510_crb_lp3_v1_2_defconfig e usa il nuovo pacchetto bootm-bbl.img per generare file immagine emmc e scheda SD.

```shell
make
```

I risultati dell'esecuzione sono i seguenti:

![](../zh/images/sdk_build/image-make_u.png)

Al termine della compilazione, verranno visualizzate le informazioni generate dal seguente file di immagine.

![](../zh/images/sdk_build/image-uboot_r.png)

## 4.6 Compilare dts

Il file dell'albero del dispositivo si trova nella directory k510_buildroot/k510_crb_lp3_v1_2_defconfig/build/linux-4.17/arch/riscv/boot/dts/canaan e quando l'utente modifica solo l'albero del dispositivo, solo l'albero del dispositivo può essere compilato e decompilato.

Scrivi uno script mkdtb-local.sh che recita:

```shell
# !/bin/sh

set -Eeuo pipefail

export BUILDROOT="$(dirname "$(realpath "$0")")"
export VARIANT="${1:-k510_crb_lp3_v1_2}"

if [[ "$VARIANT" = *_defconfig ]]; then
        VARIANT="${VARIANT:0:-10}"
fi

export KERNEL_BUILD_DIR="$BUILDROOT/${VARIANT}_defconfig/build/linux-4.17"
export BINARIES_DIR="$BUILDROOT/${VARIANT}_defconfig/images"
export PATH+=":$BUILDROOT/toolchain/nds64le-linux-glibc-v5d/bin"

riscv64-linux-cpp -nostdinc -I "${KERNEL_BUILD_DIR}/include" -I "${KERNEL_BUILD_DIR}/arch" -undef -x assembler-with-cpp "${KERNEL_BUILD_DIR}/arch/riscv/boot/dts/canaan/${VARIANT}.dts" "${BINARIES_DIR}/${VARIANT}.dts.tmp"

"${KERNEL_BUILD_DIR}/scripts/dtc/dtc" -I dts -o "${BINARIES_DIR}/k510.dtb" "${BINARIES_DIR}/${VARIANT}.dts.tmp"
"${KERNEL_BUILD_DIR}/scripts/dtc/dtc" -I dtb -O dts "${BINARIES_DIR}/k510.dtb" -o "${BINARIES_DIR}/all.dts"

echo "DONE"
echo "${BINARIES_DIR}/k510.dtb"
echo "${BINARIES_DIR}/all.dts"
```

Posizionare il mkdtb-local.sh nella directory K510_buildroot ed eseguire il comando seguente per compilare l'albero dei dispositivi della scheda k510_crb_lp3_v1_2_defconfig:

```shell
./mkdtb-local.sh k510_crb_lp3_v1_2_defconfig
```

I risultati dell'esecuzione sono i seguenti:

![](../zh/images/sdk_build/image-mdk_dts.png)

K510.dtb nella directory k510_crb_lp3_v1_2_defconfig/images è il file di database dell'albero dei dispositivi appena generato e all.dts è il file dell'albero del dispositivo decompilato.

## 4.7 Compilare l'app

Gli utenti possono fare riferimento al `package/hello_world` file Config.in e makefile per creare le proprie applicazioni e le applicazioni utente vengono inserite nella directory k510_buildroot/package. 

Il processo di compilazione di un'applicazione viene illustrato inserendo hello_world progetti in k510_buildroot/pacchetto come esempio.

Modificare i file Config.in nella directory k510_buildroot nell'ambiente di hosting.

![](../zh/images/sdk_build/image-vi_config.png)

Nella Config.in, aggiungere il percorso in cui si trova package/hello_world/Config.in e salvare.

![](../zh/images/sdk_build/image-config_list.png)

Immettere il comando buildroot di configurazione nell'ambiente docker k510:

```shell
make CONF=k510_crb_lp3_v1_2_defconfig menuconfig
```

I risultati dell'esecuzione sono i seguenti:

![](../zh/images/sdk_build/image-build_menu.png)

Viene visualizzata la pagina di configurazione buildroot, selezionare l'opzione Estesa e infine selezionare il hello_world quindi salvare e uscire.

![](../zh/images/sdk_build/image-extern_option.png)

Immettere il comando Salva configurazione nella directory k510_buildroot.

```shell
make CONF=k510_crb_lp3_v1_2_defconfig savedefconfig
```

I risultati dell'esecuzione sono i seguenti:

![](../zh/images/sdk_build/image-build_savedef.png)

1) Se è la prima volta che si compila, i passaggi sono i seguenti:

Nella directory k510_buildroot, immettere il seguente comando per compilare l'intero programma del progetto e creare il pacchetto hello in file di immagine emmc e sd card.

```shell
make CONF=k510_crb_lp3_v1_2_defconfig
```

I risultati dell'esecuzione sono i seguenti:

![](../zh/images/sdk_build/image-build_make_def.png)

Nella directory k510_buildroot/k510_crb_lp3_v1_2_defconfig/target, è possibile visualizzare l'applicazione hello risultante, che indica se l'applicazione è stata compilata correttamente.

![](../zh/images/sdk_build/image-hello.png)

2) Se è stato compilato, basta compilare l'app e impacchettarla nell'immagine di masterizzazione, attenersi alla seguente procedura:

Immettere la directory k510_buildroot/k510_crb_lp3_v1_2_defconfig e immettere il seguente comando per compilare l'applicazione hello.

```shell
make hello_world-rebuild
```

I risultati dell'esecuzione sono i seguenti:

![](../zh/images/sdk_build/image-app_build-1.png)

Vai alla directory k510_buildroot / k510_crb_lp3_v1_2_defconfig e inserisci il comando make per impacchettare hello nei file di immagine emmc e sd card.

```shell
make
```

I risultati dell'esecuzione sono i seguenti:

![](../zh/images/sdk_build/image-app-build-2.png)

# 5 Sviluppare utilizzando l'SDK K510

## 5.1 kernel linux/BBL/uboot codice sorgente

La versione uboot utilizzata da questo SDK è 2020.01, la directory delle patch uboot è package/patches/uboot e la directory dopo l'applicazione delle patch è k510_xxx_defconfig/build/uboot-2020.01.

La directory delle patch del kernel utilizzata da questo sdk è 4.17, la directory delle patch del kernel è package/patches/linux e la directory delle patch è k510_xxx_defconfig/build/linux-4.17.

Il BBL di questo sdk viene inserito come pacchetto di destinazione nella directory package/riscv-pk-k510/e il numero di origine e di versione del bbl sono specificati nel riscv-pk-k510.mk:

```text
RISCV_PK_K510_VERSION = 1e666d6c5dbab220d2ca57fbd9bec49702599b75
RISCV_PK_K510_SITE = git@github.com:kendryte/k510_BBL.git
RISCV_PK_K510_SITE_METHOD = git
```

## 5.2 Sviluppare kernel linux/BBL/uboot

Ogni pacificazione compilata sotto Buildroot, incluso il kernel linux / BBL / uboot, viene implementata scaricando tarball, decomprimendo, configurando, compilando, installando e altri passaggi di gestione dei pacchetti unificati, quindi sebbene tutto il codice sorgente possa essere visto nella directory k510_buildroot / k510_crb_lp3_v1_2_defconfig / build, non ci sono informazioni sul controllo della versione. Anche se il codice viene scaricato da un repository git.

Sebbene il codice sorgente kernel/BBL/uboot contenente i dati del repository git possa essere visualizzato nella directory dl/directory, buildroot memorizza nella cache solo il codice sorgente nella directory dl e non è consigliabile svilupparlo direttamente in questa directory.

Per il modello di sviluppo, buildroot fornisce un modo per OVERRIDE_SRCDIR.

In termini semplici, è possibile aggiungere un file local.mk nella directory k510_crb_lp3_v1_2_defconfig e aggiungerlo:

```text
<pkg1>_OVERRIDE_SRCDIR = /path/to/pkg1/sources
```

- LINUX è il nome del pacchetto del kernel
- UBOOT è il nome PACKAGE di uboot
- RISCV_PK_K510 è il nome del pacchetto del bbl

Prendiamo il kernel Linux come esempio per descrivere come usarlo.
Supponendo di aver clonato il codice del kernel nella directory /data/yourname/workspace/k510_linux_kernel e di aver apportato modifiche, e di voler compilare sotto buildroot e testarlo sulla scheda crb v1.2, è possibile creare un local.mk nella directory k510_crb_lp3_v1_2_defconfig e aggiungere quanto segue:

```text
LINUX_OVERRIDE_SRCDIR = /data/yourname/workspace/k510_linux_kernel
```

Esegui nella directory k510_crb_lp3_v1_2_defconfig

```shell
make linux-rebuild
```

Si può vedere che il kernel è stato ricompilato nella directory build/linux-custom, usando il codice modificato in /data/yourname/workspace/k510_linux_kernel.
UBOOT e BBL sono simili. In questo modo, è possibile modificare direttamente il codice del kernel e riscrivere il kernel sotto buildroot e compilare in modo incrementale l'immagine da testare.
Nota: il codice sorgente dell'override verrà aggiunto al suffisso di custom nel nome della directory k510_crb_lp3_v1_2_defconfig/build per distinguere l'origine di ciascun pacchetto nella configurazione predefinita di buildroot. Ad esempio, nell'esempio del kernel Linux sopra, la compilazione vedrà che il codice specificato dall'overrideide è compilato nella directory k510_crb_lp3_v1_2_defconfig/build/linux-custom, piuttosto che nella directory k510_crb_lp3_v1_2_defconfig/build/linux-xxx che abbiamo visto in precedenza.

Per altro codice nella directory del pacchetto, o pacchetti nativi buildroot, è possibile sviluppare sotto il framework buildroot in questo modo.

# 6 Masterizza l'immagine

K510 supporta la modalità di avvio sdcard ed eMMC, ogni volta che la compilazione nella directory k510_buildroot/k510_crb_lp3_v1_2_defconfig/image genererà file immagine sysimage-sdcard.img e sysimg-emmc.img, i due file possono essere masterizzati rispettivamente su sdcard ed eMMC.

Il K510 determina la modalità di avvio del chip in base allo stato dei pin hardware boot0 e BOOT1, fare riferimento alla sezione delle istruzioni di avvio della scheda di sviluppo per impostazioni specifiche.

| AVVIO1   | AVVIO0   | Modalità di avvio      |
| ------- | ------- | ------------ |
| 0(ON)   | 0(ON)   | Avvio della porta seriale      |
| 0(ON)   | 1 (OFF)  | La scheda SD si avvia      |
| 1 (OFF)  | 0(ON)   | Stivali NANDFLASH |
| 1 (OFF)  | 1 (OFF)  | Stivali EMMC      |

![](../zh/images/hw_crb_v1_2/clip_hw_3_9.jpg)

## 6.1 Masterizzare l'immagine sulla scheda SD

### 6.1.1 ubuntu masterizzato

Prima di inserire la scheda SD nell'host, immettere:

```shell
ls -l /dev/sd*
```

Visualizzare il dispositivo di archiviazione corrente.

Dopo aver inserito la scheda SD nell'host, inseriscila di nuovo:

```shell
ls -l /dev/sd*
```

Guardando il dispositivo di archiviazione in questo momento, la nuova aggiunta è il nodo del dispositivo della scheda SD.

Dopo aver inserito la scheda SD nell'host, il risultato dell'esecuzione del comando ls è il seguente:

![](../zh/images/sdk_build/image-dev_sd.png)

/dev/sdc è il nodo del dispositivo della scheda SD. **Nota: il nodo del dispositivo della scheda SD generato nell'ambiente utente potrebbe non essere /dev/sdc e le operazioni successive devono essere modificate in base al nodo effettivo. **

Immettere la directory k510_buildroot/k510_crb_lp3_v1_2_defconfig/image sotto l'host e immettere il comando dd per masterizzare sysimage-sdcard.img nell'sdk:

```shell
sudo dd if=sysimage-sdcard.img of=/dev/sdc bs=1M oflag=sync
```

Il risultato dell'esecuzione sotto l'host è il seguente:

![](../zh/images/sdk_build/image-dd.png)

### 6.1.2 Masterizza in Windows

Sotto Windows, la scheda SD può essere masterizzata dallo strumento banana Etcher (balena Etcher indirizzo di download dello strumento<https://www.balena.io/etcher/>). 

1) Inserire la scheda TF nel PC, quindi avviare lo strumento ColumnEtcher, fare clic sul pulsante "Flash da file" dell'interfaccia dello strumento, selezionare il firmware da masterizzare, come mostrato nella figura seguente.

![](../zh/images/sdk_build/image-sd_pre0.png)

2) Fare clic sul pulsante "Seleziona destinazione" dell'interfaccia dello strumento e selezionare la scheda sdcard di destinazione.

![](../zh/images/sdk_build/image-pre1.png)

3) Fare clic sul pulsante "Flash" per iniziare a lampeggiare, il processo lampeggiante ha una visualizzazione della barra di avanzamento, flash Finish verrà richiesto dopo la fine del flashing.

| ![](../zh/images/sdk_build/clip_image_p1.jpg) | ![](../zh/images/sdk_build/clip_image_p2.jpg) |
| --------------------------------------- | --------------------------------------- |
|                                         |                                         |

4) Quando il lampeggiamento è completo, inserire la scheda SD nello slot della scheda di sviluppo, selezionare BOOT per iniziare da SD e infine la scheda di sviluppo può essere accesa per iniziare dalla scheda SD.

## 6.2 Masterizza l'immagine su emmc

Per masterizzare sysimage-emmc.img sull'eMMC integrato, con l'aiuto dell'sdk, nell'ambiente ubuntu, il sysimage-emmc.img viene memorizzato nella partizione utente dell'sdk, quindi l'sdk viene inserito nella scheda e acceso.

Prima di masterizzare l'immagine emmc, è necessario smontare il file system relativo a emmc, fare riferimento ai seguenti passaggi per smontarlo.

```shell
mount | grep emmc
```

Il risultato dell'esecuzione è il seguente:

![](../zh/images/sdk_build/image-emmc_1.png)

Immettere il seguente comando per disinstallare e controllare.

```shell
umount /root/emmc/p2
umount /root/emmc/p3
umount /root/emmc/p4
mount | grep emmc
```

Il risultato dell'esecuzione è il seguente:

![](../zh/images/sdk_build/image-emmc_2.png)

Infine, inserisci il percorso in cui si trova l'immagine, inserisci il seguente comando per masterizzare eMMC.

```shell
dd if=sysimage-emmc.img of=/dev/mmcblk0 bs=1M
```

Il risultato dell'esecuzione è il seguente:

![](../zh/images/sdk_build/image-emmc3.png)

**Nota: il processo di masterizzazione è lento, ci vogliono circa 30 secondi, si prega di essere pazienti.**

Al termine del flashing, selezionare BOOT to Boot da EMMC e infine accendere la scheda per l'avvio da EMMC.

# 7 Ambiente di compilazione configurato dall'utente <a id="env_set"> </a>

Se non si utilizza l'ambiente docker di cui sopra, è possibile configurare il proprio ambiente di sviluppo facendo riferimento al seguente comando in ubuntu18.04 / 20.04, se non si dispone dell'autorizzazione, si prega di`sudo` usarlo. 

```shell
apt-get update
apt-get upgrade
apt-get install libc6-i386 libc6-dev-i386

apt-get install mtools
apt-get install dosfstools
apt-get install python
apt-get install python-pip
python2 -m pip install pycrypto

apt-get install python3.7
apt-get install python3-pip
python3.7 -m pip install --upgrade pip
ln -sf /usr/bin/python3.7 /usr/bin/python3
python3 -m pip install onnx==1.9.0 onnx-simplifier==0.3.6 onnxoptimizer==0.2.6 onnxruntime==1.8.0 -i https://pypi.tuna.tsinghua.edu.cn/simple

#进行下一步，需进入k510_buildroot/nncase目录，将nncase_v1.4.0.tgz解压后进入k510_buildroot/nncase/nncase_v1.4.0目录，输入如下命令安装*.whl
python3 -m pip install x86_64/*.whl
#运行python3 -m pip show nncase，若看到nncase版本信息则表示AI应用程序环境部署成功。
python3 -m pip show nncase

python3 -m pip install xlrd==1.2.0
python3 -m  pip install pystache
dpkg --add-architecture i386
apt update
apt install libncurses5:i386
apt-get install wget
apt-get install cpio
apt-get install unzip
apt-get install rsync
apt-get install bc
apt-get install libssl-dev
pip3 install pycryptodome
```

**Traduzione Disclaimer**  
Per la comodità dei clienti, Canaan utilizza un traduttore AI per tradurre il testo in più lingue, che possono contenere errori. Non garantiamo l'accuratezza, l'affidabilità o la tempestività delle traduzioni fornite. Canaan non sarà responsabile per eventuali perdite o danni causati dall'affidamento sull'accuratezza o sull'affidabilità delle informazioni tradotte. Se c'è una differenza di contenuto tra le traduzioni in lingue diverse, prevarrà la versione cinese semplificata. 

Se desideri segnalare un errore di traduzione o un'inesattezza, non esitare a contattarci via mail.