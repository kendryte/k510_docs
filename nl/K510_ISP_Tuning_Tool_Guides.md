![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 ISP Tuning Tool Gidsen</font>**

<font face="黑体"  size=3>Document versie: V1.0.0</font>

<font face="黑体"  size=3>Publicatiedatum: 2022-03-31</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Disclaimer**</font>
De producten, diensten of functies die u koopt, zijn onderworpen aan de commerciële contracten en voorwaarden van Beijing Canaan Jiesi Information Technology Co., Ltd. ("het Bedrijf", hierna hetzelfde), en alle of een deel van de producten, diensten of functies die in dit document worden beschreven, vallen mogelijk niet binnen het bereik van uw aankoop of gebruik. Tenzij anders overeengekomen in het contract, wijst het bedrijf alle verklaringen of garanties af, expliciet of impliciet, met betrekking tot de nauwkeurigheid, betrouwbaarheid, volledigheid, marketing, specifiek doel en niet-agressie van verklaringen, informatie of inhoud van dit document. Tenzij anders overeengekomen, wordt dit document uitsluitend verstrekt als leidraad voor gebruik.
Vanwege upgrades van de productversie of andere redenen kan de inhoud van dit document van tijd tot tijd zonder enige kennisgeving worden bijgewerkt of gewijzigd.

**<font face="黑体"  size=3>Handelsmerkkennisgevingen</font>**

""<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, "Canaan" icoon, Kanaän en andere handelsmerken van Kanaän en andere handelsmerken van Kanaän zijn handelsmerken van Beijing Canaan Jiesi Information Technology Co., Ltd. Alle andere handelsmerken of geregistreerde handelsmerken die in dit document kunnen worden genoemd, zijn eigendom van hun respectieve eigenaars.

**<font face="黑体"  size=3>Copyright ©2022 Beijing Canaan Jiesi Information Technology Co, Ltd</font>**
Dit document is alleen van toepassing op de ontwikkeling en het ontwerp van het K510-platform, zonder de schriftelijke toestemming van het bedrijf mag geen enkele eenheid of persoon een deel of de inhoud van dit document in welke vorm dan ook verspreiden.

**<font face="黑体"  size=3>Beijing Canaan Jiesi Information Technology Co, Ltd</font>**
URL: canaan-creative.com
Zakelijke vragen: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# inleiding
**<font face="黑体"  size=5>Doel van het document</font>**
Dit document is een isp Tuning Tool documentatie.

**<font face="黑体"  size=5>Reader Objecten</font>**

De primaire doelgroep voor dit document zijn ervaren software-ingenieurs, image algorithm engineers, systeemontwerpers en systeemintegrators die eigen applicaties en stuurprogramma's willen implementeren.

**<font face="黑体"  size=5>Revisiegeschiedenis</font>**
 <font face="宋体"  size=2>De revisiegeschiedenis bevat een beschrijving van elke documentupdate. De nieuwste versie van het document bevat updates voor alle voorgaande versies. </font>

| Het versienummer   | Gewijzigd door     | Datum van herziening | Opmerkingen bij herziening |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | Systeemsoftwaregroepen | 2022-03-31 | SDK V1.6 vrijgegeven |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Inhoud</font>**

[INHOUDSOPGAVE]

<div style="page-break-after:always"></div>

# Inleiding tot het ISP Tuning Tool Framework

In deze sectie worden de hulpprogramma's voor het afstemmen van internetproviders en beschrijvingen van de gegevensstromen beschreven die worden geleverd aan de processors op het hoogste niveau om de algehele optimalisatie van de installatiekopie van de internetprovider te beheren.

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

## Het gereedschapsverkeer afstemmen

Het communicatieprotocol is te vinden in de documentatie in de clientcoderepository en de tool bestaat uit twee delen, één is de client isp-tuningd die op de pc wordt uitgevoerd, het programma bevindt zich in de / app / mediactl_lib / isp-tuningd en het andere deel is de server die op de K510 draait. Tcp-poort 9982 wordt standaard gebruikt voor communicatie.

### klant

De ISP Tuning Tool is een applicatie die draait op een PC. Naast het kunnen instellen van registers worden ook AWB-kalibratie en CCM-kalibratie ondersteund.

### Serverzijde

isp-tuningd ontvangt een yuv-image (NV12) ter grootte van 3133440 bytes van de standaardinvoer en zendt deze uit naar alle clients, we kunnen v4l2_drm_isptool gebruiken, hij zal automatisch isp-tuning starten en de beeldgegevens verzenden, het specifieke gebruik is consistent met de v4l2_drm. We kunnen het uitvoeren met de volgende opdracht

```shell
cd /app/mediactl_lib
./v4l2_drm_isptool -f video_drm_1080x1920.conf
```

# Opties voor afstemmen door internetproviders

Veel registers en tabellen zijn voorzien in de K510 ISP voor controle en tuning. De instelling van de ISP hardware registers is erg belangrijk voor de beeldkwaliteit. Op dit moment wordt op het K510-platform het beeldafstemmingsproces alleen geïmplementeerd via TCP Socket.

## Hoofdvenster van het tuninggereedschap

In dit gedeelte worden de functies van deze panelen in het afstemmingsvenster beschreven.

Figuur 3-1 toont het volledige bedieningspaneel op het tuningvenster

- Paneel 1 is het**menu**dat optioneel het geconfigureerde ISP-bestand kan laden of kalibratie kan uitvoeren.
- Paneel 2 is het **verbindingsbedieningspaneel**, vul het IP-adres en poortnummer van de ontwikkelkaart in (standaardpoort 9982) en klik op de groene verbindingsknop om verbinding te maken.
- Paneel 3 is het**registerpaneel**, als u het register moet instellen of lezen, staat het niet in deze, u kunt dit paneel gebruiken om in te stellen en te lezen.
- Paneel 4 is een **afstemmingsparameterselectiepaneel**, de gebruiker kan verschillende parameters of groepen parameters selecteren op basis van de paneelprompttekst, de registers van deze selecties worden weergegeven op paneel 5.
- Paneel 5 is het **deelvenster Instellingen voor afstemmingsparameters**, dat wordt gebruikt om parameterwaarden in te stellen of op te halen van de afstemmingsserver.
- Paneel 6 is een **beeldweergavepaneel**, dat de beelduitvoer van de ISP weergeeft en op de pauzeknop in het midden kan klikken wanneer het niet nodig is om de hele tijd te spelen.

![Figuur 3-1 Hoofdvenster van tuninggereedschap](../zh/images/sdk_application/clip_image033.png)

DE ISP Tuning Tool****verkrijgt niet automatisch alle registerwaarden na het aansluiten, en als u alle registerwaarden wilt ophalen, kunt u op de**knop Lezen aan de rechterkant van het verbindingsbedieningspaneel** klikken om alle huidige registerwaarden op te halen.

# Kalibratie & Kalibratie

In dit gedeelte worden instructies beschreven voor kalibratie en kalibratie met behulp van isp-tuningtools, waaronder automatische witbalans (AWB), kleurcorrectiematrix (CCM), gamma en lensschaduwen (LSC).

## AWB

### Voorbereidingen

1. Standaard lichtbak met standaard D65 lichtbron
2. Standaard 24 kleuren kaart, momenteel wordt alleen X-RITE kleurenkaart ondersteund
3. Een camera die klaar is voor kalibratie kan een origineel beeld van de sensor of een verwerkt beeld uitvoeren
4. ISP opent ook alleen de zwartniveaucorrectie en de-mozaïek algoritmemodule, CSC en andere formaatconversiemodules moeten aandacht besteden aan symmetrie (matrix is inverse matrix), naast ruisonderdrukking hebben verscherping en andere modules weinig impact, maar ook proberen te sluiten, niet-lineaire modules en kleurverwerkingsmodules (GAMMA, wide dynamic, AWB, CCM, verzadigingsaanpassing, enz.) moeten worden uitgeschakeld

### Krijgt de afbeelding

1. De camera is gericht op de 24-kleurenkaart, zorg ervoor dat de 24-kleurenkaart het hele beeld vult en pak vervolgens het beeld, dat kan worden geklikt om het afspelen te pauzeren zonder nauwkeurigheid te garanderen, zoals weergegeven in de volgende afbeelding

    ![Figuur 4-1 24 kleurenkaarten worden genomen](../zh/images/sdk_application/clip_image014.jpg)

2. Het vastgelegde beeld moet letten op matige helderheid en duisternis, en te helder en te donker zal de kalibratie beïnvloeden

### afbakenen

Klik op "Kalibratie" in de menubalk, selecteer "AWB" om kalibratie uit te voeren en het programma selecteert automatisch de kleurenkaart

![Figuur 4-2 Auto Box Color Selector](../zh/images/sdk_application/clip_image016.jpg)

Druk op een willekeurige toets om door te gaan en het beeld te openen nadat de witbalans is voltooid

![Figuur 4-3 Volledige AWB-kalibratie](../zh/images/sdk_application/clip_image018.jpg)

Als er geen probleem is, blijf dan op een toets drukken, de tool zal een dialoogvenster openen met de vraag of de parameter redelijk is, ja zal deze invullen in de hoofdinterfacegerelateerde registers, anders verlaat u het kalibratieresultaat, zo ja, dan zal de tool blijven vragen of naar het apparaatregister moet worden geschreven.

## CC

In overeenstemming met AWB-kalibratie wordt deze niet herhaald.

## Gamma

De formule voor de standaard gammacurve is
$$
Y=aX^b
$$
Waar $b$ is, is de Gamma-coëfficiënt, die over het algemeen minder is dan 1 aan het beeldeinde en groter dan 1 aan het uiteinde van het scherm. De waarde van $a$ kan worden berekend op basis van de waarde van $b$

$$
a=\frac{256}{256^b}
$$
Het principe van de formule is dat de ingang 256 is, wat na Gamma-correctie nog steeds 256 is.

Wanneer de gammacoëfficiënt b 0,5 is, wordt de curve weergegeven in de volgende figuur

![](../zh/images/sdk_application/clip_image025.png)

## LSC

### Voorbereidingen

- Een opname legt een foto vast in RAW-formaat

### principe

Omdat het midden van de lens niet consistent is met de omringende lichttransmissie, is de helderheid van het beeld ongelijk, dus de curve fit genereert een corrigerend oppervlak om dit probleem te compenseren.

De correctie is weergegeven in onderstaande figuur

![Vóór correctie](../zh/images/sdk_application/clip_image029.png)

Na correctie wordt het weergegeven in de volgende afbeelding

![Na correctie](../zh/images/sdk_application/clip_image031.png)

**Vertaling Disclaimer**  
Voor het gemak van klanten gebruikt Canaan een AI-vertaler om tekst in meerdere talen te vertalen, wat fouten kan bevatten. Wij garanderen niet de nauwkeurigheid, betrouwbaarheid of tijdigheid van de geleverde vertalingen. Canaan is niet aansprakelijk voor enig verlies of schade veroorzaakt door het vertrouwen op de nauwkeurigheid of betrouwbaarheid van de vertaalde informatie. Als er een inhoudelijk verschil is tussen de vertalingen in verschillende talen, prevaleert de vereenvoudigd Chinese versie.

Als u een vertaalfout of onnauwkeurigheid wilt melden, neem dan gerust contact met ons op via e-mail.
