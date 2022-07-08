![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">Mappa della memoria di sistema K510</font>**

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
Questo documento è un documento di descrizione per l'esempio di applicazione K510 SDK. 

**<font face="黑体"  size=5>Oggetti lettore</font>**

Le principali persone a cui si applica questo documento (questa guida):

- Sviluppatori di software
- Personale di supporto tecnico

**<font face="黑体"  size=5>Cronologia delle revisioni</font>**
 <font face="宋体"  size=2>La cronologia delle revisioni accumula una descrizione di ogni aggiornamento del documento. La versione più recente del documento contiene gli aggiornamenti per tutte le versioni precedenti. </font>

| Il numero di versione   | Modificato da     | Data della revisione | Note di revisione |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 · | Gruppi di software di sistema | 2022-03-09 |   |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenuto</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Pianificazione della memoria di sistema K510

Il piano di memoria del K510 è illustrato nella figura seguente:

![](../zh/images/system_memory_map/k510-system-memory-map.png)

C'è un DDR da 512 MB sulla scheda di riferimento CRB K510, con un totale di quattro aree pianificate:

- 0 ~ 240M pianificazione per il kernel Linux
- 240M ~ 496MB è previsto per condividere la memoria, utilizzando il metodo di riserva del pool di memoria CMA, in modo che il sottosistema di gestione della memoria del kernel Linux possa anche allocare memoria dal pool CMA in assenza di utilizzo della memoria Share
- 496M ~ 510M è previsto per l'uso DSP
- 510M ~ 512M è previsto per l'uso del logo

# 2 Descrizione dell'albero dei dispositivi

La pianificazione della memoria del K510 è descritta in modo riservato-meory, attraverso i nodi di memoria riservata dell'albero dei dispositivi. Le informazioni rilevanti sul nodo dell'albero dei dispositivi sono le seguenti:

```text
ddr_memory: memory@0 {
    status              = "okay";
    device_type         = "memory";
    reg                 = <0x0 0x00000000 0x0 0x20000000>;
};

sharem_cma:sharem_cma@8000000 {
    compatible          = "k510-share-memory-cma";
    reg                 = <0x0 0xf000000 0x0 0x10000000>;  /*240M~496M*/
};

reserved-memory {
    #address-cells = <2>;
    #size-cells = <2>;
    ranges;

    cma_buffer: buffer@f000000 {
        compatible = "shared-dma-pool";
        reusable;
        linux,cma-default;
        reg = <0x0 0xf000000 0x0 0x10000000>;
    };

    dsp_buffer: buffer@1f000000 {
        no-map;
        reg = <0x0 0x1f000000 0x0 0xe00000>;
    };

    logo_buffer: buffer@1fe00000 {
        no-map;
        reg = <0x0 0x1fe00000 0x0 0x200000>;
    };
};
```

# 3 Configurazione relativa a Buildroot

Il piano di memoria di sistema è tutto descritto in dts del kernel Linux, ma l'indirizzo di caricamento del firmware dsp deve essere configurato in buildroot:

configs/k510_crb_lp3_v0_1_defconfig:

configs/k510_crb_lp3_v1_2_defconfig:

BR2_TARGET_EVB_FIRMWARE_LOAD_ADD=0x1f000000

**Traduzione Disclaimer**  
Per la comodità dei clienti, Canaan utilizza un traduttore AI per tradurre il testo in più lingue, che possono contenere errori. Non garantiamo l'accuratezza, l'affidabilità o la tempestività delle traduzioni fornite. Canaan non sarà responsabile per eventuali perdite o danni causati dall'affidamento sull'accuratezza o sull'affidabilità delle informazioni tradotte. Se c'è una differenza di contenuto tra le traduzioni in lingue diverse, prevarrà la versione cinese semplificata. 

Se desideri segnalare un errore di traduzione o un'inesattezza, non esitare a contattarci via mail.