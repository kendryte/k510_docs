![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 ISP Tuning Tool Guide</font>**

<font face="黑体"  size=3>Versione del documento: V1.0.0</font>

<font face="黑体"  size=3>Data di pubblicazione: 2022-03-31</font>

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
Questo documento è una documentazione di ISP Tuning Tool.

**<font face="黑体"  size=5>Oggetti lettore</font>**

Il pubblico principale di questo documento è costituito da ingegneri software esperti, ingegneri di algoritmi di immagine, progettisti di sistemi e integratori di sistemi che desiderano implementare applicazioni e driver proprietari.

**<font face="黑体"  size=5>Cronologia delle revisioni</font>**
 <font face="宋体"  size=2>La cronologia delle revisioni accumula una descrizione di ogni aggiornamento del documento. La versione più recente del documento contiene gli aggiornamenti per tutte le versioni precedenti. </font>

| Il numero di versione   | Modificato da     | Data della revisione | Note di revisione |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 · | Gruppi di software di sistema | 2022-03-31 | SDK V1.6 rilasciato |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contenuto</font>**

[TOC]

<div style="page-break-after:always"></div>

# Introduzione al framework dello strumento di ottimizzazione dell'ISP

In questa sezione vengono descritti gli strumenti di ottimizzazione dell'ISP e le descrizioni dei flussi di dati forniti ai processori di livello superiore per controllare l'ottimizzazione complessiva dell'immagine dell'ISP.

```text
+----------------------------------------------------+
|                                                    |
|                      K510                          |
|                                                    |
|    +-------+        +--------------------------+   |
|    |       |        |                          |   |
|    |  ISP  +------> |   v4l2_drm_isptool.out   |   |
|    |       |        |                          |   |
|    +-------+        +-------------+------------+   |
|                                   |                |
|                                   |                |
|    +-----------------+            |                |
|    |                 |            |                |
|    |   isp-tuningd   | <----------+                |
|    |                 |                             |
|    +^-+--------------+                             |
|     | |                                            |
|     | |                                            |
+----------------------------------------------------+
      | |
      | |
+-------------------------------+
|     | |                       |
|     | |       PC              |
|     | |                       |
|    ++-v------------------+    |
|    |                     |    |
|    |  ISP Tuning Tool    |    |
|    |                     |    |
|    +---------------------+    |
|                               |
+-------------------------------+
```

## Ottimizza il traffico degli strumenti

Il protocollo di comunicazione può essere trovato nella documentazione nel repository del codice client e lo strumento è costituito da due parti, una è l'isp-tuningd del client in esecuzione sul PC, il programma si trova in /app/mediactl_lib/isp-tuningd e l'altra parte è il server in esecuzione sul K510. Per impostazione predefinita, la porta TCP 9982 viene utilizzata per la comunicazione.

### cliente

ISP Tuning Tool è un'applicazione che viene eseguita su un PC. Oltre a poter impostare i registri, sono supportate anche la calibrazione AWB e la calibrazione CCM.

### Lato server

isp-tuningd riceve un'immagine yuv (NV12) in dimensioni di 3133440 byte dall'ingresso standard e la trasmette a tutti i client, possiamo usare v4l2_drm_isptool, avvierà automaticamente isp-tuningd e invierà i dati dell'immagine, l'uso specifico è coerente con il v4l2_drm. Possiamo eseguirlo con il seguente comando

```shell
cd /app/mediactl_lib
./v4l2_drm_isptool -f video_drm_1080x1920.conf
```

# Opzioni di ottimizzazione dell'ISP

Molti registri e tabelle sono forniti nell'ISP K510 per il controllo e la messa a punto. L'impostazione dei registri hardware dell'ISP è molto importante per la qualità dell'immagine. Allo stato attuale, sulla piattaforma K510, il processo di ottimizzazione delle immagini è implementato solo tramite TCP Socket.

## Finestra principale dello strumento di ottimizzazione

In questa sezione vengono descritte le funzionalità di questi pannelli nella finestra di ottimizzazione.

La Figura 3-1 mostra l'intero pannello operatore nella finestra di sintonizzazione

- Il pannello 1 è il**menu**che può facoltativamente caricare il file ISP configurato o eseguire la calibrazione.
- Il pannello 2 è il **pannello di controllo della connessione**, inserire l'indirizzo IP e il numero di porta della scheda di sviluppo (porta predefinita 9982) e fare clic sul pulsante verde di connessione per connettersi.
- Il pannello 3 è il **pannello del registro**, se è necessario impostare o leggere il registro non è in questo, è possibile utilizzare questo pannello per impostare e leggere.
- Il pannello 4 è un **pannello di selezione dei parametri di sintonizzazione**, l'utente può selezionare vari parametri o gruppi di parametri in base al testo del prompt del pannello, i registri di queste selezioni verranno visualizzati sul pannello 5.
- Il pannello 5 è il **pannello Impostazioni parametri di ottimizzazione**, che viene utilizzato per impostare o ottenere valori di parametro dal server di ottimizzazione.
- Il pannello 6 è un **pannello di visualizzazione**delle immagini, che visualizza l'output dell'immagine da parte dell'ISP e può fare clic sul pulsante di pausa al centro quando non è necessario riprodurre tutto il tempo.

![Figura 3-1 Finestra principale dello strumento di ottimizzazione](../zh/images/sdk_application/clip_image033.png)

LO STRUMENTO DI OTTIMIZZAZIONE ISP**non**acquisisce automaticamente tutti i valori del registro dopo la connessione e, se è necessario ottenere tutti i valori del registro, è possibile fare clic**sul pulsante Leggi sul lato destro del pannello di controllo della connessione** per estrarre tutti i valori del registro corrente.

# Calibrazione e calibrazione

In questa sezione vengono descritte le istruzioni per la calibrazione e la calibrazione mediante gli strumenti di ottimizzazione dell'ISP, tra cui il bilanciamento automatico del bianco (AWB), la matrice di correzione del colore (CCM), la gamma e le ombre dell'obiettivo (LSC).

## AWB

### Preparazioni

1. Scatola luminosa standard con sorgente luminosa D65 standard
2. Scheda colore standard a 24 colori, attualmente è supportata solo la scheda colore X-RITE
3. Una fotocamera pronta per la calibrazione può emettere un'immagine originale del sensore o un'immagine elaborata
4. ISP inoltre apre solo il modulo di correzione del livello del nero e dell'algoritmo di de-mosaico, CSC e altri moduli di conversione del formato devono prestare attenzione alla simmetria (la matrice è matrice inversa), oltre alla riduzione del rumore, la nitidezza e altri moduli hanno poco impatto, ma anche provare a chiudere, i moduli non lineari e i moduli di elaborazione del colore (GAMMA, wide dynamic, AWB, CCM, regolazione della saturazione, ecc.) devono essere disattivati

### Ottiene l'immagine

1. La fotocamera è puntata sulla scheda a 24 colori, assicurarsi che la scheda a 24 colori riempia l'intera immagine, quindi afferrare l'immagine, che può essere cliccata per mettere in pausa la riproduzione senza garantire la precisione, come mostrato nella figura seguente

    ![Figura 4-1 Vengono prese 24 carte a colori](../zh/images/sdk_application/clip_image014.jpg)

2. L'immagine acquisita dovrebbe prestare attenzione alla luminosità e all'oscurità moderate, e troppo luminose e troppo scure influenzeranno la calibrazione

### demarcare

Fare clic su "Calibrazione" nella barra dei menu, selezionare "AWB" per eseguire la calibrazione e il programma selezionerà automaticamente la scheda colore

![Figura 4-2 Selettore colore casella automatica](../zh/images/sdk_application/clip_image016.jpg)

Premere un tasto qualsiasi per continuare, facendo apparire l'immagine al termine del bilanciamento del bianco

![Figura 4-3 Calibrazione AWB completa](../zh/images/sdk_application/clip_image018.jpg)

Se non ci sono problemi, continua a premere qualsiasi tasto, lo strumento aprirà una finestra di dialogo che chiede se il parametro è ragionevole, sì lo riempirà nei registri principali relativi all'interfaccia, altrimenti abbandonerà il risultato della calibrazione, in tal caso, lo strumento continuerà a chiedere se scrivere sul registro del dispositivo.

## CC

Coerentemente con la calibrazione AWB, non verrà ripetuto.

## Gamma

La formula per la curva di gamma standard è
$$
Y=aX^b
$$
Dove $b$ è il coefficiente Gamma, che è generalmente inferiore a 1 all'estremità dell'immagine e maggiore di 1 all'estremità del display. Il valore di $a$ può essere calcolato in base al valore di $b$

$$
a=\frac{256}{256^b}
$$
Il principio della formula è che l'input è 256, che è ancora 256 dopo la correzione gamma.

Quando il coefficiente gamma b è 0,5, la curva è illustrata nella figura riportata di seguito

![](../zh/images/sdk_application/clip_image025.png)

## LSC

### Preparazioni

- Uno scatto cattura una fotografia in formato RAW

### principio

Poiché il centro dell'obiettivo non è coerente con la trasmissione della luce circostante, la luminosità dell'immagine non è uniforme, quindi l'adattamento della curva genera una superficie correttiva per compensare questo problema.

La correzione è mostrata nella figura seguente

![Prima della correzione](../zh/images/sdk_application/clip_image029.png)

Dopo la correzione, è mostrato nella figura riportata di seguito

![Dopo la correzione](../zh/images/sdk_application/clip_image031.png)

**Traduzione Disclaimer**  
Per la comodità dei clienti, Canaan utilizza un traduttore AI per tradurre il testo in più lingue, che possono contenere errori. Non garantiamo l'accuratezza, l'affidabilità o la tempestività delle traduzioni fornite. Canaan non sarà responsabile per eventuali perdite o danni causati dall'affidamento sull'accuratezza o sull'affidabilità delle informazioni tradotte. Se c'è una differenza di contenuto tra le traduzioni in lingue diverse, prevarrà la versione cinese semplificata.

Se desideri segnalare un errore di traduzione o un'inesattezza, non esitare a contattarci via mail.
