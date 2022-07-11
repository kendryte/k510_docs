![](../zh/images/canaan-cover.png)
&nbsp;
&nbsp;
**<font face="黑体" size="6" style="float:right">K510 CRB V1.2 Guide hardware</font>**

<font face="黑体" size=100>&nbsp;
&nbsp;
&nbsp;</font>

<font face="黑体"  size=3>Versione del documento: V1.0.0</font>

<font face="黑体"  size=3>Data di pubblicazione: 2022-03-15</font>

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

| Il numero di versione | Modificato da    | Data della revisione   | Note di revisione           |
| :----- | --------- | ---------- | ------------------ |
| V1.0.0 · | Divisione Prodotti AI | 2022-03-15 | |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenuto</font>**

[Toc]

<div style="page-break-after:always"></div>

# 1 Panoramica

&emsp; &emsp; K510 CRB è una piattaforma di sviluppo hardware per il chip CANaan Kendryte K510 AI che integra progettazione di riferimento, debug e test dei chip e verifica dello sviluppo del prodotto utente, che viene utilizzata per dimostrare la potente potenza di calcolo e le funzioni del chip K510. Allo stesso tempo, fornisce ai clienti progetti di riferimento hardware basati su chip K510, in modo che i clienti non debbano modificare o semplicemente modificare il circuito del modulo del progetto di riferimento e possano completare il lavoro di sviluppo hardware del prodotto con chip K510 come nucleo.

&emsp; &emsp; K510 CRB supporta lo sviluppo hardware, la progettazione del software applicativo, il debug e il funzionamento del chip K510, perché considerando diversi ambienti di utilizzo, il chip è una verifica completamente funzionale, quindi le varie interfacce sono complete e il design è relativamente completo. Il K510 CRB può essere collegato a un PC tramite un cavo USB, utilizzato come sistema di sviluppo di base, o a un sistema di sviluppo più completo e un ambiente demo, collegando i seguenti dispositivi e componenti:

- alimentatore

- Dispositivo di archiviazione TF Card

- Display LCD MIPI DSI

- Modulo telecamera MIPI CSI

- Modulo telecamera DVP

- Cavo di rete Ethernet

- Display HDMI

- Cuffie o altoparlanti

- Espandi i pezzi di ricambio

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-K510_Core.png">
</div>

  <center>Figura 1-1 Rendering CRB K510</center>

    **禁止事项**

  1. È vietato collegare e scollegare il modulo principale e i moduli periferici dal vivo!
  2. È vietato utilizzare questo prodotto direttamente senza le misure di scarica di elettricità statica o senza protezione statica.
  3. È vietato utilizzare solventi organici o liquidi corrosivi per pulire questo prodotto.
  4. È vietato eseguire operazioni come la maschiatura e la torsione che possono causare danni fisici.

    **Precauzioni**

  1. Si prega di notare che dopo la scarica elettrostatica del corpo umano, prima di utilizzare questo prodotto, si consiglia di indossare un braccialetto elettrostatico.
  2. Prima del funzionamento, confermare la tensione di alimentazione e la tensione dell'adattatore del backplane entro l'intervallo consentito descritto in questo documento.
  3. Assicurarsi di leggere questo documento e le considerazioni nel file di progettazione prima della progettazione.
  4. Si noti che l'uso di prodotti in ambienti ad alta temperatura, alta umidità, alta corrosione richiede un trattamento speciale come dissipazione del calore, drenaggio e sigillatura.
  5. Si prega di non riparare e smontare se stessi, altrimenti non sarà possibile usufruire del servizio post-vendita gratuito.

<div style="page-break-after:always"></div>

## 1.1 Diagramma a blocchi del sistema

&emsp; &emsp; Il diagramma a blocchi del sistema viene utilizzato per descrivere i principi di progettazione del CRB K510 e la relazione tra i componenti, in modo che l'uso del CRB K510 e gli sviluppatori possano avere una comprensione intuitiva dell'architettura e dei principi dell'intero sistema.

&emsp; &emsp; Per ulteriori informazioni sulle funzionalità di K510, fare riferimento alla scheda tecnica completa di K510.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_1_2.png">
</div>

<center>Figura 1-2 K510 Composizione CRB</center>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_1_3.png">
</div>

<center>Figura 1-3 Diagramma a blocchi del sistema CRB K510 </center>

<div style="page-break-after:always"></div>

&emsp; &emsp; Il kit di sviluppo K510 CRB è composto principalmente dai seguenti componenti:

| Parti | quantità |
| :-: | :-: |
| K510 CRB scheda madre | 1 |
| USB tipo C线缆 | 2 |
| Cavo Micro USB OTG | 1 |
| Display MIPI DSI con risoluzione di 1920x1080 | 1 |
| Sottoscheda telecamera MIPI CSI, sensore di immagine Sony IMX219 integrato due | 1 |
| Custodia protettiva in acrilico | 1 |

<div style="page-break-after:always"></div>

## 1.2 Panoramica delle funzioni

&emsp; &emsp; L'SDK K510 è basato su buildroot come framework di base, con kernel linux K510 (linux versione 4.17.0), u-boot (u-boot versione 2020.01), riscv-pk-k510

&emsp; &emsp; Le caratteristiche principali di K510 CRB V1.2 (se non ci sono dichiarazioni speciali, le versioni di CRB descritte più avanti in questo documento sono V1.2) sono le seguenti:

- PMIC: Gestione dell'alimentazione
- LPDDR3EE a 32 bit, capacità totale 512MByte
- 8bit eMMC, capacità totale 4GByte
- QSPI NAND, capacità totale 128MByte
- TF Card: supporta l'espansione esterna della memoria della scheda TF.
- USB OTG: aggiornamento del sistema, supporto per la commutazione di host / dispositivo
- SDIO WIFI: supporta la funzione Internet wireless e la connessione Bluetooth
- Audio: supporta l'ingresso e l'uscita vocale
- PDM MIC: funzione di sveglia VAD
- Uart & JTAG Debug: schede di sviluppo utilizzate da Debug
- Ingresso video: doppio ingresso telecamera MIPI CSI a 2 corsie
- Uscita video: MIPI DSI 4lane, display 1080P
- RGMII: Connessione Gigabit Ethernet
- HDMI: interfaccia multimediale ad alta definizione
- Interfacce estese: alimentazione, GPIO, I2C, SPI
- Tasti, indicatori

<div style="page-break-after:always"></div>

# 2 Introduzione alle risorse hardware

## 2.1 Rendering complessivi

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_1.png" width=80%>
</div>

<center> Figura 2-1 Fronte scheda madre </center>

<div style="page-break-after:always"></div>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_2.png" width=80%>
</div>

<center> Figura 2-1 Sul retro della scheda madre </center>

<div style="page-break-after:always"></div>

## 2.2 Schema schematico di struttura e interfaccia

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_3.png" width=120%>
</div>

<center> Figura 2-3 Posizione di ciascun dispositivo sulla parte anteriore della scheda madre </center>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2-4.png" width=120%>
</div>

<center> Figura 2-4 Retro della scheda madre </center>

<div style="page-break-after:always"></div>

## 2.3 Diagramma a blocchi di potenza

&emsp; &emsp; Il K510 CRB utilizza DC-5V come potenza di ingresso dell'intera scheda, fornendo DC-5V per il modulo core K510 CORE e 1,8V e 3,3V per le altre periferiche del backplane attraverso due DC-DC.

## 2.4 Indirizzo del dispositivo I2C

<center>Tabella 2-1 Tabella indirizzi dispositivo I2C</center>

| nome | Pin (SCL, SDA) | indirizzo | osservazione |
| :-: | :-: | :-: | :-: |
| schermo tattile | IO_103、IO_102 | 0x14 o 0x5D | |
| HDMI | IO_117、IO_116 | 0x3B | |
| Audio Codec | IO_117、IO_116 | 0x1A | |
| Fotocamera MIPI CSI0 | IO_120、IO_121 | 0x10 | |
| Fotocamera MIPI CSI1 | IO_47、IO_48   | 0x10 | |

## 2.5 Schemi

&emsp; &emsp; Lo schema di riferimento per la scheda di sviluppo CRB K510 deve essere[scaricato al momento del rilascio](https://github.com/kendryte/k510_docs/releases).

<div style="page-break-after:always"></div>

# 3 Introduzione a ciascuna sezione della scheda di sviluppo

## 3.1 Moduli principali

&emsp; &emsp; Prima di utilizzare K510 CRB per l'apprendimento e lo sviluppo, si consiglia di fare riferimento all'architettura dettagliata del chip nel manuale K510, in modo da poter avere una comprensione più profonda dell'alimentazione, dello storage, delle risorse di calcolo e delle periferiche del K510, che favorisce la familiarità e lo sviluppo della soluzione chip. La scheda principale K510 è mostrata nella Figura 3-1.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_1.png">
</div>

<center>Figura 3-1 Modulo Core K510</center>

<div style="page-break-after:always"></div>

## 3.2 Alimentazione in ingresso

&emsp; &emsp; K510 CRB utilizza alimentazione esterna a 5V, a bordo due interfacce USB di tipo C, può essere utilizzato per alimentare la scheda di sviluppo, di cui l'interfaccia UART viene utilizzata per connettersi al computer, l'interfaccia USB del COMPUTER può fornire solo 500mA di corrente, in caso di alimentazione insufficiente, si prega di utilizzare l'adattatore allo stesso tempo per alimentare l'alimentazione a DC: 5V. L'interfaccia è illustrata nella figura riportata di seguito.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_2.png" width=60%>
</div>

<center> Figura 3-2 Connettore di alimentazione </center>

**Nota: Limitare l'uso dell'alimentatore a 5 V, quando si utilizza l'adattatore di ricarica rapida, provare a non collegare contemporaneamente altri dispositivi come i telefoni cellulari, in modo da non causare l'uscita errata dell'adattatore di ricarica rapida da un alimentatore superiore a 5 V, con conseguente danno alla parte di alimentazione della scheda di sviluppo.**
&emsp; &emsp; Utilizzate l'interruttore a levetta K2 per il funzionamento di accensione e spegnimento, come illustrato nella figura riportata di seguito.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-3.jpg" width=50%>
</div>

<center>Figura 3-3 Descrizione dell'interruttore di alimentazione</center>

<div style="page-break-after:always"></div>

## 3.3 Dispositivi di archiviazione

&emsp; &emsp; Il K510 CRB include una varietà di dispositivi di archiviazione a bordo, tra cui DDR, eMMC, NAND Flash e TF Card.

### 3.3.1 eMMC

&emsp; &emsp; Una memoria eMMC 4G Bytes a bordo del K510 CRB, situata sul modulo principale, può essere utilizzata per memorizzare dati come il codice di avvio e i file utente.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-eMMC.png" width=70%>
</div>

<center>Figura 3-4 Memoria eMMC</center>

### 3.3.2 NandFlash

&emsp; &emsp; Il CRB K510 include 128 milioni di byte di memoria NAND Flash, che può essere utilizzata per archiviare dati come il codice di avvio e i file utente.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_5.jpg " width=75%>
</div>

<center>Figura 3-5 Memoria NAND Flash</center>

### 3.3.2 Carta di TF

&emsp; &emsp; Il K510 CRB ha un supporto per schede TF a bordo che può essere collegato esternamente a una scheda TF per memorizzare dati come il codice di avvio e i file utente.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_6.png">
</div>

<center>Figura 3-6 Supporto per carte TF</center>

<div style="page-break-after:always"></div>

## 3.4 Sequenze di tasti

&emsp; &emsp; Il K510 CRB contiene due pulsanti a sfioramento utente che consentono agli utenti di personalizzare i pulsanti di tocco da attivare come input di sistema o altre funzioni correlate al software.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_7.jpg" width=50%>
</div>

<center>Figura 3-7 Tasti</center>

## 3.5 LED

&emsp; &emsp; Il K510 CRB ha un diodo a emissione luminosa a bordo che è collegato direttamente al pin GPIO del chip K510.

&emsp; &emsp; Il K510 CRB è a bordo di un LED colorato WS2812 che è collegato direttamente al pin GPIO del chip K510.

&emsp; &emsp; I due LED sono programmati su misura per illuminare o spegnere e possono essere utilizzati come uscite di sistema o indicazioni di stato relative al software.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_8.jpg" width=60%>
</div>

<center>Figura 3-8 LED</center>

<div style="page-break-after:always"></div>

## 3.6 Modalità di avvio e ripristino

&emsp; &emsp; Il K510 CRB ha una varietà di dispositivi di archiviazione a bordo e la modalità di avvio viene selezionata configurando i livelli dei pin di avvio, BOOT0 e BOOT1, con 0 e 1 che rappresentano livelli bassi e alti.

&emsp; &emsp; Sul PCB, la modalità di avvio è selezionata dall'interruttore DIP mostrato nella figura seguente, e il modulo principale è stato progettato per tirare su BOOT0 e BOOT1, e il lato della spia di composizione che contrassegna ON rappresenta il corrispondente bit pull down efficace, e l'altro lato di ON corrisponde a OFF rappresenta il pull-up efficace.

&emsp; &emsp; Il K510 determina la modalità di avvio del chip in base allo stato dei pin hardware boot0 e BOOT1 e la selezione della modalità di avvio è illustrata nella tabella seguente.

<center>Tabella 2-1 Modalità di avvio</center>

| AVVIO1   | AVVIO0   | Modalità di avvio      |
| ------- | ------- | ------------ |
| 0(ON)   | 0(ON)   | Avvio della porta seriale      |
| 0(ON)   | 1 (OFF)  | La scheda SD si avvia      |
| 1 (OFF)  | 0(ON)   | Stivali NANDFLASH |
| 1 (OFF)  | 1 (OFF)  | Stivali EMMC      |

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_9.jpg" width=60%>
</div>

<center>Figura 3-9 Interruttore di ripristino e dip switch di avvio</center>

&emsp; &emsp; Il pulsante di ripristino integrato K510 CRB è K2 nella Figura 3-9, che può essere premuto per eseguire un'operazione di ripristino hardware del sistema.

<div style="page-break-after:always"></div>

## 3.7 Ingresso e uscita audio

&emsp; &emsp; Il K510 CRB utilizza il chip codec audio di Nuvoton, NAU88C22, per implementare le funzioni di input e output per il parlato. Include un microfono integrato, jack per cuffie standard da 3,5 mm e connettore per altoparlanti 2P.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-10.jpg" width=60%>
</div>

<center>Figura 3-10 Audio</center>

## 3.8 Presa USB OTG

&emsp; &emsp; La presa USB OTG integrata K510 CRB può essere utilizzata per implementare la funzionalità host/dispositivo USB.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_11.jpg">
</div>

<center>Figura 3-11 Sedile USB-OTG</center>

<div style="page-break-after:always"></div>

## 3.9 Interfaccia UART

&emsp; &emsp; K510 CRB Al fine di facilitare lo sviluppo e il debug dell'utente, il K510 CRB ha un'interfaccia UART USB-> a bordo, che può essere gestita dalla comunicazione della porta seriale USART e dal debug del K510 tramite il cavo PC-USB. L'uso iniziale può richiedere il caricamento del driver, come descritto nella sezione 4.2. L'interfaccia UART integrata è mostrata nella figura seguente.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_12.jpg" width=50%>
</div>

<center>Figura 3-12 Interfaccia USB-UART</center>

## Modulo 3.10 WIFI/BT

&emsp; &emsp; Il K510 CRB include un modulo WIFI/BT 2-in-1 AP6212 per estendere la scheda di sviluppo per la connettività di rete e le funzioni di comunicazione Bluetooth, come mostrato nell'interfaccia integrata di seguito.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-13.jpg" width=40%>
</div>

<center>Figura 3-13 Modulo WIFI/BT</center>

<div style="page-break-after:always"></div>

## 3.11 Ethernet

&emsp; &emsp; Il K510 CRB ha un supporto Gigabit Ethernet integrato e il K510 è implementato tramite un chip PHY esterno con un'interfaccia RGMII. L'interfaccia integrata è illustrata nella figura riportata di seguito.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_14.jpg" width=60%>
</div>

<center>Figura 3-14 Interfaccia Ethernet</center>

## Uscita hdmi 3.12

&emsp; &emsp; Il supporto femmina HDMI-A integrato K510 CRB può essere collegato al display esterno tramite un cavo HDMI standard, utilizzando la conversione dell'uscita dell'uscita dell'interfaccia mipi dsi del K510. L'interfaccia integrata è illustrata nella figura riportata di seguito.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_15.jpg" width=60%>
</div>

<center>Figura 3-15 Interfaccia HDMI</center>

 **Nota**: Poiché entrambi i display HDMI e 1080P TFT utilizzano driver mipi dsi, possono scegliere solo uno dei due display, non possono essere utilizzati contemporaneamente, passare attraverso il pin di controllo GPIO per selezionare una delle uscite.

<div style="page-break-after:always"></div>

## 3.13 Video In

&emsp; &emsp; Il K510 CRB attira mipi CSI, DVP, alimentatore e GPIO parziale attraverso un connettore da scheda a scheda con passo di 0,8 mm per ottenere l'ingresso della telecamera in diversi scenari e diverse situazioni di domanda. L'interfaccia integrata è illustrata nella figura riportata di seguito. Le definizioni dell'interfaccia sono illustrate nella tabella seguente.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-16.jpg">
</div>

<center>Figura 3-16 Interfaccia Video IN</center>

<center>Tabella 3-2 Definizioni dell'interfaccia Video IN</center>

| numerazione | definizione             | numerazione | definizione                       |
| ---- | ---------------- | ---- | --------------- |
| 1    | VDD_5V           | 60   | GPIO_1V8_59_DVP_D12      |
| 2    | VDD_5V           | 59   | GPIO_1V8_58_DVP_D11      |
| 3    | VDD_5V           | 58   | GPIO_1V8_50_DVP_D3       |
| 4    | VDD_5V           | 57   | GPIO_1V8_51_DVP_D4       |
| 5    | GND              | 56   | GPIO_1V8_60_DVP_D13      |
| 6    | GND              | 55   | GPIO_1V8_55_DVP_D8       |
| 7    | MIPI_CSI_D0_P    | 54   | GPIO_1V8_61_DVP_D14      |
| 8    | MIPI_CSI_D0_N    | 53   | GPIO_1V8_52_DVP_D5       |
| 9    | GND              | 52   | GPIO_1V8_47_DVP_D0       |
| 10   | MIPI_CSI_CLK0_P  | 51   | GPIO_1V8_56_DVP_D9       |
| 11   | MIPI_CSI_CLK0_N  | 50   | GPIO_1V8_53_DVP_D6       |
| 12   | GND              | 49   | GPIO_1V8_57_DVP_D10      |
| 13   | MIPI_CSI_D1_P    | 48   | GPIO_1V8_48_DVP_D1       |
| 14   | MIPI_CSI_D1_N    | 47   | GPIO_1V8_54_DVP_D7       |
| 15   | GND              | 46   | GPIO_1V8_64_DVP_HREF     |
| 16   | MIPI_CSI_D2_N    | 45   | GPIO_1V8_49_DVP_D2       |
| 17   | MIPI_CSI_D2_P    | 44   | GPIO_1V8_65_DVP_DEN      |
| 18   | GND              | 43   | GPIO_1V8_66_DVP_PCLK     |
| 19   | MIPI_CSI_CLK1_N  | 42   | GPIO_1V8_62_DVP_D15      |
| 20   | MIPI_CSI_CLK1_P  | 41   | GPIO_1V8_63_DVP_VSYNC    |
| 21   | GND              | 40   | GPIO_1V8_82 |
| 22   | MIPI_CSI_D3_N    | 39   | GPIO_1V8_67  |
| 23   | MIPI_CSI_D3_P    | 38   | GPIO_1V8_68  |
| 24   | GND              | 37   | GPIO_1V8_72  |
| 25   | MIPI_CSI_I2C_SCL | 36   | GPIO_1V8_73  |
| 26   | MIPI_CSI_I2C_SCA | 35   | GPIO_1V8_74  |
| 27   | GND              | 34   | GND          |
| 28   | GND              | 33   | GND          |
| 29   | 1V8 ·              | 32   | 3V3 ·          |
| 30   | 1V8 ·              | 31   | 3V3 ·          |

**Nota**: Prestare attenzione all'intervallo di livello dei pin collegati quando si collegano esternamente per evitare che l'ingresso di tensione errato danneggi in modo permanente il chip K510.

<div style="page-break-after:always"></div>

## 3.14 Uscita video

&emsp; &emsp; Il K510 CRB ha un flap 30P con passo di 0,5 mm sotto il connettore FPC per il collegamento a un display LCD esterno, come mostrato nella figura seguente. Le definizioni dell'interfaccia sono illustrate nella tabella seguente.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-17.jpg">
</div>

<center>Figura 3-17 Interfaccia di uscita video</center>

<center>Tabella 3-3 Definizioni dell'interfaccia video out</center>

| numerazione | definizione              | numerazione | definizione             |
| ---- | ----------------- | ---- | ---------------- |
| 1    | GND               | 16   | MIPI_DSI_D1_N    |
| 2    | GND               | 17   | MIPI_DSI_D1_P    |
| 3    | VDD_5V            | 18   | GND              |
| 4    | VDD_5V            | 19   | MIPI_DSI_CLK_N   |
| 5    | VDD_3V3           | 20   | MIPI_DSI_CLK_P   |
| 6    | VDD_3V3           | 21   | GND              |
| 7    | GND               | 22   | MIPI_DSI_D0_N    |
| 8    | TOUCH_1V8_I2C_SCL | 23   | MIPI_DSI_D0_P    |
| 9    | TOUCH_1V8_I2C_SDA | 24   | GND              |
| 10   | TOUCH_1V8_INT     | 25   | MIPI_DSI_D3_N    |
| 11   | TOUCH_1V8_RST     | 26   | MIPI_DSI_D3_P    |
| 12   | GND               | 27   | GND              |
| 13   | MIPI_DSI_D2_N     | 28   | MIPI_DSI_LCD_RST |
| 14   | MIPI_DSI_D2_P     | 29   | MIPI_DSI_LCD_EN  |
| 15   | GND               | 30   | GND              |

<div style="page-break-after:always"></div>

## 3.15 Estensione dell'interfaccia

&emsp; &emsp; Al fine di facilitare l'implementazione di funzioni di espansione personalizzate per gli utenti, un pin di espansione 30P 2.54mm è riservato sul K510 CRB, che porta a un alimentatore e parte del GPIO, che l'utente può utilizzare attraverso il software iomux per mappare risorse hardware come I2C, UART, SPI al GPIO corrispondente per ottenere la connessione esterna e l'espansione delle funzioni corrispondenti. L'interfaccia integrata è illustrata nella figura riportata di seguito. Le definizioni dettagliate sono riportate nella tabella seguente.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw-3-18.jpg">
</div>

<center>Figura 3-18 Interfaccia di estensione pin 40P</center>

<center>Tabella 3-4 Definizioni estese dell'interfaccia</center>

| numerazione | definizione         | numerazione | definizione         |
| ---- | ------------ | ---- | ------------ |
| 1    | VDD_1V8      | 2    | GND          |
| 3    | VDD_1V8      | 4    | GND          |
| 5    | VDD_3V3      | 6    | GND          |
| 7    | VDD_3V3      | 8    | GND          |
| 9    | VDD_5V       | 10   | GND          |
| 11   | VDD_5V       | 12   | GPIO_1V8_95  |
| 13   | GPIO_3V3_114 | 14   | GPIO_3V3_115 |
| 15   | GPIO_1V8_92  | 16   | GPIO_1V8_96  |
| 17   | GPIO_1V8_105 | 18   | GPIO_1V8_107 |
| 19   | GPIO_1V8_104 | 20   | GPIO_1V8_106 |
| 21   | GPIO_1V8_118 | 22   | GPIO_1V8_119 |
| 23   | GPIO_1V8_93  | 24   | GPIO_1V8_94  |
| 25   | GPIO_3V3_125 | 26   | GPIO_3V3_124 |
| 27   | GPIO_3V3_127 | 28   | GPIO_3V3_126 |
| 29   | GND          | 30   | GND          |

**Nota**: Prestare attenzione all'intervallo di livello dei pin collegati quando si collegano esternamente per evitare che l'ingresso di tensione errato danneggi in modo permanente il chip K510.

<div style="page-break-after:always"></div>

# 4 Utilizzo della scheda di sviluppo

## 4.1 Installazione del driver

&emsp; &emsp; Il K510 CRB ha ch340E integrato per implementare la funzione di comunicazione USB-UART, quindi il driver corrispondente deve essere installato prima dell'uso.

&emsp; &emsp; Utilizzare il driver nel pacchetto o scaricarlo e installarlo al seguente indirizzo.

&emsp;&emsp;<http://www.wch.cn/product/CH340.html>

## 4.2 Masterizzazione firmware

&emsp; &emsp; Fare riferimento alla[](./K510_SDK_Build_and_Burn_Guide.md)documentazione K510_SDK_Build_and_Burn_Guide.

## 4.3 Accensione e spegnimento

&emsp; &emsp; 1) Installare il cavo di alimentazione e il cavo di debug USB.

&emsp; &emsp; 2) Interruttore DIP selezionato per iniziare dalla scheda TF.

&emsp; &emsp; 3) Accendere l'interruttore attivando l'interruttore come mostrato nella Sezione 3.2.

## 4.4 Debug della porta seriale

&emsp; &emsp; Dopo aver installato il driver, accendere il CRB K510, a quel punto la porta appare in Gestione periferiche - Porta del PC.

&emsp; &emsp; Utilizzando lo strumento di debug della porta seriale, aprire il numero di porta del dispositivo, baud rate 115200.

&emsp; &emsp; Come illustrato nella figura seguente, il dispositivo è "COM6", visualizzato in Gestione periferiche PC.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_4_1.jpg">
</div>

<center>Figura 4-1 Gestione periferiche al termine dell'installazione del driver</center>

**Traduzione Disclaimer**  
Per la comodità dei clienti, Canaan utilizza un traduttore AI per tradurre il testo in più lingue, che possono contenere errori. Non garantiamo l'accuratezza, l'affidabilità o la tempestività delle traduzioni fornite. Canaan non sarà responsabile per eventuali perdite o danni causati dall'affidamento sull'accuratezza o sull'affidabilità delle informazioni tradotte. Se c'è una differenza di contenuto tra le traduzioni in lingue diverse, prevarrà la versione cinese semplificata.

Se desideri segnalare un errore di traduzione o un'inesattezza, non esitare a contattarci via mail.
