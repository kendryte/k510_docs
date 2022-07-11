![](../zh/images/canaan-cover.png)
&nbsp;
&nbsp;
**<font face="黑体" size="6" style="float:right">K510 CRB V1.2 Hardware Handleidingen</font>**

<font face="黑体" size=100>&nbsp;
&nbsp;
&nbsp;</font>

<font face="黑体"  size=3>Document versie: V1.0.0</font>

<font face="黑体"  size=3>Publicatiedatum: 2022-03-15</font>

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
Dit document is een begeleidend document bij de K510 sdk en is bedoeld om ingenieurs te helpen de compilatie en het branden van de K510 sdk te begrijpen.

**<font face="黑体"  size=5>Reader Objecten</font>**

De belangrijkste personen op wie dit document (deze gids) van toepassing is:

- Softwareontwikkelaars
- Technisch ondersteunend personeel

**<font face="黑体"  size=5>Revisiegeschiedenis</font>**
 <font face="宋体"  size=2>De revisiegeschiedenis bevat een beschrijving van elke documentupdate. De nieuwste versie van het document bevat updates voor alle voorgaande versies. </font>

| Het versienummer | Gewijzigd door    | Datum van herziening   | Opmerkingen bij herziening           |
| :----- | --------- | ---------- | ------------------ |
| V1.0.0 | Divisie AI-producten | 2022-03-15 | |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Inhoud</font>**

[Inhoudsopgave]

<div style="page-break-after:always"></div>

# 1 Overzicht

&emsp; &emsp; K510 CRB is een hardwareontwikkelingsplatform voor Canaan Kendryte K510 AI-chip die referentieontwerp, chipdebuggen en testen en verificatie van gebruikersproductontwikkeling integreert, die wordt gebruikt om de krachtige rekenkracht en functies van de K510-chip te demonstreren. Tegelijkertijd biedt het klanten hardwarereferentieontwerpen op basis van K510-chips, zodat klanten het modulecircuit van het referentieontwerp niet hoeven te wijzigen of eenvoudigweg hoeven aan te passen en het producthardwareontwikkelingswerk kunnen voltooien met K510-chips als kern.

&emsp; &emsp; K510 CRB ondersteunt de hardwareontwikkeling, het ontwerp van applicatiesoftware, de foutopsporing en de werking van de K510-chip, omdat gezien verschillende gebruiksomgevingen de chip volledig functionele verificatie is, dus de verschillende interfaces zijn compleet en het ontwerp is relatief compleet. De K510 CRB kan worden aangesloten op een pc via een USB-kabel, worden gebruikt als een basisontwikkelingssysteem, of op een completer ontwikkelingssysteem en demo-omgeving, waarbij de volgende apparaten en componenten worden aangesloten:

- voeding

- TF-kaart opslagapparaat

- MIPI DSI LCD-scherm

- MIPI CSI camera module

- DVP camera module

- Ethernet-netwerkkabel

- HDMI-scherm

- Hoofdtelefoons of luidsprekers

- Reserveonderdelen uitbreiden

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-K510_Core.png">
</div>

  <center>Figuur 1-1 K510 CRB rendering</center>

    **禁止事项**

  1. Het is verboden om de core module en randapparatuur modules live aan te sluiten en los te koppelen!
  2. Het is verboden om dit product rechtstreeks te gebruiken zonder de maatregelen van ontlading van statische elektriciteit of zonder statische bescherming.
  3. Het is verboden om organische oplosmiddelen of corrosieve vloeistoffen te gebruiken om dit product te reinigen.
  4. Het is verboden om handelingen uit te voeren zoals tikken en draaien die fysieke schade kunnen veroorzaken.

    **Voorzorgsmaatregelen**

  1. Houd er rekening mee dat na de elektrostatische ontlading van het menselijk lichaam, voordat u dit product gebruikt, het wordt aanbevolen om een elektrostatische armband te dragen.
  2. Controleer vóór de bediening de voedingsspanning en adapterspanning van de backplane binnen het toegestane bereik dat in dit document wordt beschreven.
  3. Zorg ervoor dat u dit document en de overwegingen in het engineeringbestand leest voordat u gaat ontwerpen.
  4. Merk op dat het gebruik van producten bij hoge temperaturen, hoge luchtvochtigheid, hoge corrosieomgevingen een speciale behandeling vereist, zoals warmteafvoer, drainage en afdichting.
  5. Repareer en demonteer niet zelf, anders kunt u niet genieten van een gratis after-sales service.

<div style="page-break-after:always"></div>

## 1.1 Systeemblokdiagram

&emsp; &emsp; Het systeemblokdiagram wordt gebruikt om de ontwerpprincipes van de K510 CRB en de relatie tussen de componenten te beschrijven, zodat het gebruik van de K510 CRB en ontwikkelaars een intuïtief begrip kunnen hebben van de architectuur en principes van het hele systeem.

&emsp; &emsp; Voor meer informatie over K510 functies, verwijzen wij u naar K510 Full Datasheet.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_1_2.png">
</div>

<center>Figuur 1-2 K510 CRB samenstelling</center>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_1_3.png">
</div>

<center>Figuur 1-3 K510 CRB-systeemblokdiagram </center>

<div style="page-break-after:always"></div>

&emsp; &emsp; De K510 CRB development kit bestaat voornamelijk uit de volgende onderdelen:

| delen | hoeveelheid |
| :-: | :-: |
| K510 CRB moederbord | 1 |
| USB type C线缆 | 2 |
| Micro USB OTG-kabel | 1 |
| MIPI DSI-scherm met een resolutie van 1920x1080 | 1 |
| MIPI CSI camera sub-board, on-board Sony IMX219 beeldsensor twee | 1 |
| Acryl beschermende behuizing | 1 |

<div style="page-break-after:always"></div>

## 1.2 Functie overzicht

&emsp; &emsp; De K510 SDK is gebaseerd op buildroot als basisframework, met K510 linux kernel (linux versie 4.17.0), u-boot (u-boot versie 2020.01), riscv-pk-k510

&emsp; &emsp; De belangrijkste kenmerken van K510 CRB V1.2 (als er geen speciale verklaringen zijn, zijn de versies van CRB die verderop in dit document worden beschreven V1.2) als volgt:

- PMIC: Energiebeheer
- 32 bit LPDDR3EE, totale capaciteit 512MByte
- 8bit eMMC, totale capaciteit 4GByte
- QSPI NAND, totale capaciteit 128MByte
- TF-kaart: Ondersteunt externe uitbreiding van TF-kaartopslag.
- USB OTG: Systeemupgrade, ondersteuning voor host / apparaatschakeling
- SDIO WIFI: Ondersteunt draadloze internetfunctie en Bluetooth-verbinding
- Audio: Ondersteuning van spraakinvoer en -uitvoer
- PDM MIC: VAD wake-up functie
- Uart & JTAG Debug: Ontwikkelborden gebruikt door Debug
- video-ingang: dubbele MIPI CSI 2lane camera-ingang
- Video-uitgang: MIPI DSI 4lane, 1080P-scherm
- RGMII: Gigabit Ethernet-verbinding
- HDMI: High-definition multimedia-interface
- Uitgebreide interfaces: voeding, GPIO, I2C, SPI
- Sleutels, indicatoren

<div style="page-break-after:always"></div>

# 2 Inleiding tot hardwarebronnen

## 2.1 Algemene renderings

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_1.png" width=80%>
</div>

<center> Figuur 2-1 Moederbord front </center>

<div style="page-break-after:always"></div>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_2.png" width=80%>
</div>

<center> Figuur 2-1 Op de achterkant van het moederbord </center>

<div style="page-break-after:always"></div>

## 2.2 Schematisch schema van structuur en interface

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_3.png" width=120%>
</div>

<center> Figuur 2-3 Positie van elk apparaat aan de voorkant van het moederbord </center>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2-4.png" width=120%>
</div>

<center> Figuur 2-4 Achterkant van het moederbord </center>

<div style="page-break-after:always"></div>

## 2.3 Power Block Diagram

&emsp; &emsp; De K510 CRB gebruikt DC-5V als het ingangsvermogen van het hele bord en levert DC-5V voor de K510 CORE-kernmodule en 1,8 V en 3,3 V voor de andere randapparatuur van de backplane via twee DC-DC's.

## 2.4 I2C-apparaatadres

<center>Tabel 2-1 I2C-apparaatadrestabel</center>

| naam | Pinnen (SCL, SDA) | adres | opmerking |
| :-: | :-: | :-: | :-: |
| aanraakscherm | IO_103、IO_102 | 0x14 of 0x5D | |
| Hdmi | IO_117、IO_116 | 0x3B | |
| Audiocodec | IO_117、IO_116 | 0x1A | |
| MIPI CSI Camera0 | IO_120、IO_121 | 0x10 | |
| MIPI CSI Camera1 | IO_47、IO_48   | 0x10 | |

## 2.5 Schema's

&emsp; &emsp; Het referentieschema voor de K510 CRB-ontwikkelingskaart moet[bij de release worden gedownload](https://github.com/kendryte/k510_docs/releases).

<div style="page-break-after:always"></div>

# 3 Inleiding tot elke sectie van de ontwikkelingsraad

## 3.1 Kernmodules

&emsp; &emsp; Voordat u K510 CRB gebruikt voor leren en ontwikkeling, wordt het aanbevolen om de gedetailleerde architectuur van de chip in de K510-handleiding te raadplegen, zodat u een dieper inzicht kunt krijgen in de voeding, opslag, computerbronnen en randapparatuur van de K510, wat bevorderlijk is voor de bekendheid en ontwikkeling van de chipoplossing. Het K510 kernbord is weergegeven in figuur 3-1.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_1.png">
</div>

<center>Figuur 3-1 K510 Core Core Module</center>

<div style="page-break-after:always"></div>

## 3.2 Ingangsvoeding

&emsp; &emsp; K510 CRB maakt gebruik van externe 5V-voeding, aan boord twee USB type C-interfaces, kan worden gebruikt om de ontwikkelingskaart van stroom te voorzien, waarvan de UART-interface wordt gebruikt om verbinding te maken met de computer, de USB-interface van de COMPUTER kan slechts 500mA stroom leveren, in het geval van onvoldoende voeding, gebruik de adapter tegelijkertijd om stroom te leveren op DC: 5V. De interface wordt weergegeven in de volgende afbeelding.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_2.png" width=60%>
</div>

<center> Figuur 3-2 Voedingsingang </center>

**Opmerking: Beperk het gebruik van een 5V-voeding, probeer bij gebruik van de snellaadadapter niet tegelijkertijd andere apparaten zoals mobiele telefoons aan te sluiten, zodat de snellaadadapter niet ten onrechte een voeding van meer dan 5 V uitvoert, wat resulteert in schade aan het voedingsgedeelte van de ontwikkelingskaart.**
&emsp; &emsp; Gebruik de K2-tuimelschakelaar voor het in- en uitschakelen, zoals weergegeven in de volgende afbeelding.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-3.jpg" width=50%>
</div>

<center>Figuur 3-3 Beschrijving van de aan/uit-schakelaar</center>

<div style="page-break-after:always"></div>

## 3.3 Opslagapparaten

&emsp; &emsp; De K510 CRB bevat een verscheidenheid aan opslagapparaten aan boord, waaronder DDR, eMMC, NAND Flash en TF Card.

### 3.3.1. eMMC

&emsp; &emsp; Een 4G Bytes eMMC-geheugen aan boord op de K510 CRB, gelegen op de kernmodule, kan worden gebruikt om gegevens zoals opstartcode en gebruikersbestanden op te slaan.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-eMMC.png" width=70%>
</div>

<center>Figuur 3-4 eMMC-geheugen</center>

### 3.3.2. NandFlash

&emsp; &emsp; De K510 CRB bevat 128M Bytes NAND Flash-geheugen, dat kan worden gebruikt om gegevens zoals opstartcode en gebruikersbestanden op te slaan.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_5.jpg " width=75%>
</div>

<center>Figuur 3-5 NAND Flash-geheugen</center>

### 3.3.2 TF-kaart

&emsp; &emsp; De K510 CRB heeft een TF-kaarthouder aan boord die extern op een TF-kaart kan worden aangesloten om gegevens zoals opstartcode en gebruikersbestanden op te slaan.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_6.png">
</div>

<center>Figuur 3-6 TF-kaarthouder</center>

<div style="page-break-after:always"></div>

## 3.4 Toetsaanslagen

&emsp; &emsp; De K510 CRB bevat twee aanraakknoppen voor gebruikers waarmee gebruikers de tikknoppen kunnen aanpassen om te activeren als systeemingangen of andere softwaregerelateerde functies.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_7.jpg" width=50%>
</div>

<center>Figuur 3-7 Toetsen</center>

## 3.5 LED's

&emsp; &emsp; De K510 CRB heeft een lichtgevende diode aan boord die rechtstreeks is aangesloten op de GPIO-pin van de K510-chip.

&emsp; &emsp; De K510 CRB is aan boord van een gekleurde LED WS2812 die rechtstreeks is aangesloten op de GPIO-pin van de K510-chip.

&emsp; &emsp; De twee LED's zijn op maat geprogrammeerd om te branden of te doven en kunnen worden gebruikt als systeemuitgangen of softwaregerelateerde statusindicaties.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_8.jpg" width=60%>
</div>

<center>Figuur 3-8 LED</center>

<div style="page-break-after:always"></div>

## 3.6 Opstartmodus en reset

&emsp; &emsp; De K510 CRB heeft een verscheidenheid aan opslagapparaten aan boord en de opstartmodus wordt geselecteerd door de niveaus van de opstartpennen, BOOT0 en BOOT1, te configureren, waarbij 0 en 1 lage en hoge niveaus vertegenwoordigen.

&emsp; &emsp; Op de pcb wordt de opstartmodus geselecteerd door de DIP-schakelaar die in de volgende afbeelding wordt weergegeven, en de kernmodule is ontworpen om BOOT0 en BOOT1 op te trekken, en de zijkant van het aan-kieslicht dat AAN markeert, vertegenwoordigt de overeenkomstige bit pull-down effectief, en de andere kant van ON komt overeen met OFF vertegenwoordigt de pull-up effectief.

&emsp; &emsp; De K510 bepaalt de chip-opstartmodus door de status van de boot0- en BOOT1-hardwarepennen en de opstartmodusselectie wordt weergegeven in de volgende tabel.

<center>Tabel 2-1 Opstartmodi</center>

| BOOT1   | BOOT0   | Opstartmodus      |
| ------- | ------- | ------------ |
| 0(AAN)   | 0(AAN)   | Seriële poort boot      |
| 0(AAN)   | 1 (UIT)  | De SD-kaart start op      |
| 1 (UIT)  | 0(AAN)   | NANDFLASH laarzen |
| 1 (UIT)  | 1 (UIT)  | EMMC laarzen      |

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_9.jpg" width=60%>
</div>

<center>Figuur 3-9 Reset schakelaar en startmodus DIP schakelaar</center>

&emsp; &emsp; De K510 CRB on-board resetknop is K2 in figuur 3-9, die kan worden ingedrukt om een hardwareresetbewerking van het systeem uit te voeren.

<div style="page-break-after:always"></div>

## 3.7 Audio-in- en uitgang

&emsp; &emsp; De K510 CRB maakt gebruik van Nuvoton's audio codec chip, NAU88C22, om input en output functies voor spraak te implementeren. Inclusief een ingebouwde microfoon, standaard 3,5 mm koptelefoonaansluiting en 2P-luidsprekeraansluiting.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-10.jpg" width=60%>
</div>

<center>Figuur 3-10 Audio</center>

## 3.8 USB OTG-aansluiting

&emsp; &emsp; De K510 CRB on-board USB OTG-aansluiting kan worden gebruikt om USB-host/apparaatfunctionaliteit te implementeren.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_11.jpg">
</div>

<center>Figuur 3-11 USB-OTG-stoel</center>

<div style="page-break-after:always"></div>

## 3.9 UART-interface

&emsp; &emsp; K510 CRB Om de ontwikkeling en foutopsporing van gebruikers te vergemakkelijken, heeft de K510 CRB een USB-> UART-interface aan boord, die kan worden bediend door USART seriële poortcommunicatie en foutopsporing van de K510 via de PC-USB-kabel. Voor het eerste gebruik kan het nodig zijn de bestuurder te laden, zoals beschreven in punt 4.2. De ingebouwde UART-interface wordt weergegeven in de onderstaande afbeelding.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_12.jpg" width=50%>
</div>

<center>Figuur 3-12 USB-UART-interface</center>

## 3.10 WIFI /BT-module

&emsp; &emsp; De K510 CRB bevat een WIFI/BT 2-in-1 module AP6212 om de ontwikkelingskaart voor netwerkconnectiviteit en Bluetooth-communicatiefuncties uit te breiden, zoals weergegeven in de onderstaande on-board interface.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-13.jpg" width=40%>
</div>

<center>Figuur 3-13 WIFI/BT module</center>

<div style="page-break-after:always"></div>

## 3.11 Ethernet

&emsp; &emsp; De K510 CRB heeft een ingebouwde Gigabit Ethernet-houder en de K510 wordt geïmplementeerd via een externe PHY-chip met een RGMII-interface. De ingebouwde interface wordt weergegeven in de volgende afbeelding.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_14.jpg" width=60%>
</div>

<center>Figuur 3-14 Ethernet-interface</center>

## 3,12 HDMI-uitgang

&emsp; &emsp; De K510 CRB on-board HDMI-A female mount kan via een standaard HDMI-kabel op het externe scherm worden aangesloten, met behulp van de mipi dsi interface output conversie van de K510. De ingebouwde interface wordt weergegeven in de volgende afbeelding.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_15.jpg" width=60%>
</div>

<center>Figuur 3-15 HDMI-interface</center>

 **Opmerking**: Omdat zowel de HDMI- als de 1080P TFT-schermen mipi dsi-stuurprogramma's gebruiken, kunnen ze slechts een van de twee schermen kiezen, kunnen ze niet tegelijkertijd worden gebruikt, schakelen ze door de bedieningspin GPIO om een van de uitgangen te selecteren.

<div style="page-break-after:always"></div>

## 3.13 Video in

&emsp; &emsp; De K510 CRB trekt mipi CSI, DVP, voeding en gedeeltelijke GPIO via een 0,8 mm pitch board-to-board connector om camera-ingang te bereiken in verschillende scenario's en verschillende vraagsituaties. De ingebouwde interface wordt weergegeven in de volgende afbeelding. De interfacedefinities worden weergegeven in de volgende tabel.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-16.jpg">
</div>

<center>Figuur 3-16 Video IN-interface</center>

<center>Tabel 3-2 Video IN interface definities</center>

| Nummering | definitie             | Nummering | definitie                       |
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
| 29   | 1v8              | 32   | 3v3          |
| 30   | 1v8              | 31   | 3v3          |

**Opmerking**: Let op het niveaubereik van de aangesloten pinnen bij het extern aansluiten om te voorkomen dat de verkeerde spanningsingang de K510-chip permanent beschadigt.

<div style="page-break-after:always"></div>

## 3.14 Video-uitgang

&emsp; &emsp; De K510 CRB heeft een 0,5 mm pitch 30P-klep onder de FPC-connector voor aansluiting op een extern LCD-scherm, zoals weergegeven in de onderstaande afbeelding. De interfacedefinities worden weergegeven in de volgende tabel.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-17.jpg">
</div>

<center>Figuur 3-17 Video-uitgang interface</center>

<center>Tabel 3-3 Interfacedefinities voor video-uitgangen</center>

| Nummering | definitie              | Nummering | definitie             |
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

## 3.15 Uitbreiding van de interface

&emsp; &emsp; Om de implementatie van aangepaste uitbreidingsfuncties voor gebruikers te vergemakkelijken, is een 30P 2,54 mm uitbreidingspin gereserveerd op de K510 CRB, die leidt tot een voeding en een deel van de GPIO, die de gebruiker via de software iomux kan bedienen om hardwarebronnen zoals I2C, UART, SPI toe te wijzen aan de bijbehorende GPIO om externe verbinding en uitbreiding van de bijbehorende functies te bereiken. De ingebouwde interface wordt weergegeven in de volgende afbeelding. De gedetailleerde definities worden weergegeven in de volgende tabel.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw-3-18.jpg">
</div>

<center>Figuur 3-18 40P pin extensie interface</center>

<center>Tabel 3-4 Uitgebreide interfacedefinities</center>

| Nummering | definitie         | Nummering | definitie         |
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

**Opmerking**: Let op het niveaubereik van de aangesloten pinnen bij het extern aansluiten om te voorkomen dat de verkeerde spanningsingang de K510-chip permanent beschadigt.

<div style="page-break-after:always"></div>

# 4 Gebruik van ontwikkelborden

## 4.1 Het stuurprogramma installeren

&emsp; &emsp; De K510 CRB heeft ch340E aan boord om de USB-UART-communicatiefunctie te implementeren, dus het bijbehorende stuurprogramma moet voor gebruik worden geïnstalleerd.

&emsp; &emsp; Gebruik het stuurprogramma in het pakket of download en installeer het op het volgende adres.

&emsp;&emsp;<http://www.wch.cn/product/CH340.html>

## 4.2 Firmware branden

&emsp; &emsp; Raadpleeg[de K510_SDK_Build_and_Burn_Guide](./K510_SDK_Build_and_Burn_Guide.md)documentatie.

## 4.3 In- en uitschakelen

&emsp; &emsp; 1) Installeer de voedingskabel en USB-foutopsporingskabel.

&emsp; &emsp; 2) DIP-schakelaar geselecteerd om te starten vanaf de TF-kaart.

&emsp; &emsp; 3) Schakel de schakelaar in door de schakelaar in te schakelen zoals weergegeven in punt 3.2.

## 4.4 Seriële poort debuggen

&emsp; &emsp; Nadat het stuurprogramma is geïnstalleerd, schakelt u de K510 CRB in, waarna de poort verschijnt in apparaatbeheer - poort van de pc.

&emsp; &emsp; Gebruik het hulpprogramma voor foutopsporing in seriële poorten en open het poortnummer van het apparaat, baudrate 115200.

&emsp; &emsp; Zoals weergegeven in de volgende afbeelding, is het apparaat "COM6", wat wordt weergegeven in pc-apparaatbeheer.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_4_1.jpg">
</div>

<center>Figuur 4-1 Apparaatbeheer nadat de installatie van het stuurprogramma is voltooid</center>

**Vertaling Disclaimer**  
Voor het gemak van klanten gebruikt Canaan een AI-vertaler om tekst in meerdere talen te vertalen, wat fouten kan bevatten. Wij garanderen niet de nauwkeurigheid, betrouwbaarheid of tijdigheid van de geleverde vertalingen. Canaan is niet aansprakelijk voor enig verlies of schade veroorzaakt door het vertrouwen op de nauwkeurigheid of betrouwbaarheid van de vertaalde informatie. Als er een inhoudelijk verschil is tussen de vertalingen in verschillende talen, prevaleert de vereenvoudigd Chinese versie.

Als u een vertaalfout of onnauwkeurigheid wilt melden, neem dan gerust contact met ons op via e-mail.
