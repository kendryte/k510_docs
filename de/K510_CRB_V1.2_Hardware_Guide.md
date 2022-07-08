![](../zh/images/canaan-cover.png)
&nbsp;
&nbsp;
**<font face="黑体" size="6" style="float:right">K510 CRB V1.2 Hardware-Handbücher</font>**

<font face="黑体" size=100>&nbsp;
&nbsp;
&nbsp;</font>

<font face="黑体"  size=3>Dokumentversion: V1.0.0</font>

<font face="黑体"  size=3>Veröffentlicht: 2022-03-15</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Verzichtserklärung**</font>
Die Produkte, Dienstleistungen oder Funktionen, die Sie erwerben, unterliegen den kommerziellen Verträgen und Bedingungen von Beijing Canaan Jiesi Information Technology Co., Ltd. ("das Unternehmen", dasselbe im Folgenden), und alle oder ein Teil der in diesem Dokument beschriebenen Produkte, Dienstleistungen oder Funktionen fallen möglicherweise nicht in den Rahmen Ihres Kaufs oder Ihrer Nutzung. Sofern im Vertrag nicht anders vereinbart, lehnt das Unternehmen alle ausdrücklichen oder stillschweigenden Zusicherungen oder Gewährleistungen hinsichtlich der Genauigkeit, Zuverlässigkeit, Vollständigkeit, des Marketings, des spezifischen Zwecks und der Nichtverletzung von Zusicherungen, Informationen oder Inhalten dieses Dokuments ab. Sofern nicht anders vereinbart, wird dieses Dokument nur als Leitfaden für die Verwendung zur Verfügung gestellt.
Aufgrund von Produktversions-Upgrades oder anderen Gründen kann der Inhalt dieses Dokuments von Zeit zu Zeit ohne vorherige Ankündigung aktualisiert oder geändert werden. 

**<font face="黑体"  size=3>Markenhinweise</font>**

"", "Canaan"-Symbol, Canaan und andere Marken von Canaan und andere Marken von Canaan <img src="../zh/images/canaan-logo.png" style="zoom:33%;" />sind Marken von Beijing Canaan Jiesi Information Technology Co., Ltd. Alle anderen Marken oder eingetragenen Warenzeichen, die in diesem Dokument erwähnt werden können, sind Eigentum ihrer jeweiligen Inhaber. 

**<font face="黑体"  size=3>Copyright ©2022 Peking Canaan Jiesi Information Technology Co., Ltd</font>**
Dieses Dokument gilt nur für die Entwicklung und das Design der K510-Plattform, ohne die schriftliche Genehmigung des Unternehmens darf keine Einheit oder Einzelperson einen Teil oder den gesamten Inhalt dieses Dokuments in irgendeiner Form verbreiten. 

**<font face="黑体"  size=3>Peking Canaan Jiesi Informationstechnologie Co., Ltd</font>**
URL: canaan-creative.com
Geschäftliche Anfragen: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# Vorwort
**<font face="黑体"  size=5>Zweck des Dokuments</font>**
Dieses Dokument ist ein Begleitdokument zum K510 SDK und soll Ingenieuren helfen, die Kompilierung und das Brennen des K510 SDK zu verstehen. 

**<font face="黑体"  size=5>Reader-Objekte</font>**

Die wichtigsten Personen, für die sich dieses Dokument (dieser Leitfaden) richtet:

- Softwareentwickler
- Mitarbeiter des technischen Supports

**<font face="黑体"  size=5>Revisionshistorie</font>**
 <font face="宋体"  size=2>In der Revisionshistorie wird eine Beschreibung jeder Dokumentaktualisierung gesammelt. Die neueste Version des Dokuments enthält Updates für alle vorherigen Versionen. </font>

| Die Versionsnummer | Geändert von    | Datum der Überarbeitung   | Revisionshinweise           |
| :----- | --------- | ---------- | ------------------ |
| V1.0.0 | Geschäftsbereich KI-Produkte | 2022-03-15 | |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Inhalt</font>**

[Toc]

<div style="page-break-after:always"></div>

# 1 Übersicht

&emsp; &emsp; K510 CRB ist eine Hardware-Entwicklungsplattform für den Canaan Kendryte K510 AI-Chip, die Referenzdesign, Chip-Debugging und -Tests sowie die Überprüfung der Benutzerproduktentwicklung integriert, um die leistungsstarke Rechenleistung und Funktionen des K510-Chips zu demonstrieren. Gleichzeitig bietet es Kunden Hardware-Referenzdesigns auf Basis von K510-Chips, so dass Kunden die Modulschaltung des Referenzdesigns nicht modifizieren oder einfach modifizieren müssen und die Produkthardware-Entwicklungsarbeit mit K510-Chips als Kern abschließen können.

&emsp; &emsp; K510 CRB unterstützt die Hardwareentwicklung, das Design der Anwendungssoftware, das Debugging und den Betrieb des K510-Chips, da der Chip unter Berücksichtigung verschiedener Nutzungsumgebungen voll funktionsfähig verifiziert ist, so dass die verschiedenen Schnittstellen vollständig sind und das Design relativ vollständig ist. Der K510 CRB kann über ein USB-Kabel an einen PC angeschlossen werden, der als grundlegendes Entwicklungssystem verwendet wird, oder an ein vollständigeres Entwicklungssystem und eine Demoumgebung, die die folgenden Geräte und Komponenten verbindet:

- Stromversorgung

- TF-Karten-Speichergerät

- MIPI DSI LCD-Display

- MIPI CSI Kameramodul

- DVP-Kameramodul

- Ethernet-Netzwerkkabel

- HDMI-Anzeige

- Kopfhörer oder Lautsprecher

- Ersatzteile erweitern

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-K510_Core.png">
</div>

  <center>Abbildung 1-1 K510 CRB-Rendering</center>

    **禁止事项**

  1. Es ist verboten, das Kernmodul und die Peripheriemodule live ein- und auszustecken!
  2. Es ist verboten, dieses Produkt direkt ohne die Maßnahmen der Entladung statischer Elektrizität oder ohne statischen Schutz zu betreiben.
  3. Es ist verboten, organische Lösungsmittel oder korrosive Flüssigkeiten zu verwenden, um dieses Produkt zu reinigen.
  4. Es ist verboten, Operationen wie Klopfen und Verdrehen durchzuführen, die physische Schäden verursachen können.

    **Vorsichtsmaßnahmen**

  1. Bitte beachten Sie, dass nach der elektrostatischen Entladung des menschlichen Körpers vor dem Betrieb dieses Produkts empfohlen wird, ein elektrostatisches Armband zu tragen.
  2. Überprüfen Sie vor dem Betrieb die Versorgungsspannung und die Adapterspannung der Rückwandplatine innerhalb des in diesem Dokument beschriebenen zulässigen Bereichs.
  3. Lesen Sie dieses Dokument und die Überlegungen in der Engineering-Datei, bevor Sie entwerfen.
  4. Beachten Sie, dass die Verwendung von Produkten in Umgebungen mit hoher Temperatur, hoher Luftfeuchtigkeit und hoher Korrosion eine spezielle Behandlung wie Wärmeableitung, Drainage und Abdichtung erfordert.
  5. Bitte reparieren und demontieren Sie nicht selbst, da Sie sonst keinen kostenlosen Kundendienst genießen können.

<div style="page-break-after:always"></div>

## 1.1 Systemblockdiagramm

&emsp; &emsp; Das Systemblockdiagramm wird verwendet, um die Konstruktionsprinzipien des K510 CRB und die Beziehung zwischen den Komponenten zu beschreiben, so dass der Einsatz des K510 CRB und die Entwickler ein intuitives Verständnis der Architektur und der Prinzipien des gesamten Systems haben können.

&emsp; &emsp; Weitere Informationen zu den Funktionen des K510 finden Sie im vollständigen Datenblatt des K510.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_1_2.png">
</div>

<center>Abbildung 1-2 K510 CRB-Zusammensetzung</center>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_1_3.png">
</div>

<center>Abbildung 1-3 K510 CRB-Systemblockdiagramm </center>

<div style="page-break-after:always"></div>

&emsp; &emsp; Das K510 CRB Development Kit besteht hauptsächlich aus den folgenden Komponenten:

| Teile | Menge |
| :-: | :-: |
| K510 CRB Motherboard | 1 |
| USB-Typ C线缆 | 2 |
| Micro-USB-OTG-Kabel | 1 |
| MIPI DSI Display mit einer Auflösung von 1920x1080 | 1 |
| MIPI CSI Kamera Sub-Board, On-Board Sony IMX219 Bildsensor zwei | 1 |
| Acryl-Schutzgehäuse | 1 |

<div style="page-break-after:always"></div>

## 1.2 Funktionsübersicht

&emsp; &emsp; Das K510 SDK basiert auf buildroot als Basisframework, mit K510 Linux-Kernel (Linux-Version 4.17.0), u-boot (u-boot-Version 2020.01), riscv-pk-k510

&emsp; &emsp; Die Hauptmerkmale von K510 CRB V1.2 (wenn es keine speziellen Deklarationen gibt, sind die später in diesem Dokument beschriebenen Versionen von CRB V1.2) sind wie folgt:

- PMIC: Energieverwaltung
- 32 Bit LPDDR3EE, Gesamtkapazität 512MByte
- 8bit eMMC, Gesamtkapazität 4GByte
- QSPI NAND, Gesamtkapazität 128MByte
- TF-Karte: Unterstützt externe Erweiterung des TF-Kartenspeichers.
- USB OTG: System-Upgrade, Unterstützung Host/Device Switching
- SDIO WIFI: Unterstützt drahtlose Internetfunktion und Bluetooth-Verbindung
- Audio: Unterstützt Spracheingabe und -ausgabe
- PDM MIC: VAD-Weckfunktion
- Uart & JTAG Debug: Von Debug verwendete Entwicklungsboards
- Videoeingang: Dual MIPI CSI 2lane Kameraeingang
- Videoausgang: MIPI DSI 4lane, 1080P Display
- RGMII: Gigabit-Ethernet-Verbindung
- HDMI: High-Definition-Multimedia-Schnittstelle
- Erweiterte Schnittstellen: Stromversorgung, GPIO, I2C, SPI
- Schlüssel, Indikatoren

<div style="page-break-after:always"></div>

# 2 Einführung in Hardwareressourcen

## 2.1 Gesamtrenderings

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_1.png" width=80%>
</div>

<center> Abbildung 2-1 Vorderseite der Hauptplatine </center>

<div style="page-break-after:always"></div>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_2.png" width=80%>
</div>

<center> Abbildung 2-1 Auf der Rückseite der Hauptplatine </center>

<div style="page-break-after:always"></div>

## 2.2 Schematische Darstellung von Struktur und Schnittstelle

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_3.png" width=120%>
</div>

<center> Abbildung 2-3 Position der einzelnen Geräte auf der Vorderseite der Hauptplatine </center>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2-4.png" width=120%>
</div>

<center> Abbildung 2-4 Rückseite der Hauptplatine </center>

<div style="page-break-after:always"></div>

## 2.3 Leistungsblockdiagramm

&emsp; &emsp; Der K510 CRB verwendet DC-5V als Eingangsleistung der gesamten Platine und liefert DC-5V für das K510 CORE Core-Modul und 1,8 V und 3,3 V für die anderen Peripheriegeräte der Backplane über zwei DC-DCs.

## 2.4 I2C-Geräteadresse

<center>Tabelle 2-1 Adresstabelle für I2C-Geräte</center>

| Name | Pins (SCL, SDA) | Adresse | Bemerkung |
| :-: | :-: | :-: | :-: |
| Sensorbildschirm | IO_103、IO_102 | 0x14 oder 0x5D | |
| HDMI-Anschluss | IO_117、IO_116 | 0x3B | |
| Audio-Codec | IO_117、IO_116 | 0x1A | |
| MIPI CSI-Kamera0 | IO_120、IO_121 | 0x10 | |
| MIPI CSI-Kamera1 | IO_47、IO_48   | 0x10 | |

## 2.5 Schaltpläne

&emsp; &emsp; Der Referenzschaltplan für das K510 CRB-Entwicklungsboard sollte[ bei der Veröffentlichung heruntergeladen](https://github.com/kendryte/k510_docs/releases) werden. 

<div style="page-break-after:always"></div>

# 3 Einführung in jeden Abschnitt des Entwicklungsboards

## 3.1 Kernmodule

&emsp; &emsp; Bevor Sie K510 CRB für das Lernen und die Entwicklung verwenden, wird empfohlen, sich auf die detaillierte Architektur des Chips im K510-Handbuch zu beziehen, damit Sie ein tieferes Verständnis der Stromversorgung, des Speichers, der Rechenressourcen und der Peripherie des K510 haben, was der Vertrautheit und Entwicklung der Chiplösung förderlich ist. Die K510-Kernplatine ist in Abbildung 3-1 dargestellt.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_1.png">
</div>

<center>Abbildung 3-1 Kernmodul K510</center>

<div style="page-break-after:always"></div>

## 3.2 Eingangsnetzteil

&emsp; &emsp; K510 CRB verwendet externe 5V-Stromversorgung, on-board zwei USB-Typ-C-Schnittstellen, kann verwendet werden, um die Entwicklungsplatine mit Strom zu versorgen, von der die UART-Schnittstelle verwendet wird, um an den Computer anzuschließen, die USB-Schnittstelle des COMPUTERS kann nur 500mA Strom liefern, im Falle einer unzureichenden Stromversorgung, verwenden Sie bitte den Adapter gleichzeitig, um Strom bei DC: 5V zu liefern. Die Schnittstelle ist in der folgenden Abbildung dargestellt.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_2.png" width=60%>
</div>

<center> Abbildung 3-2 Stromeingangsanschluss </center>

**Hinweis: Beschränken Sie die Verwendung von 5V-Netzteilen, wenn Sie den Schnellladeadapter verwenden, versuchen Sie, andere Geräte wie Mobiltelefone nicht gleichzeitig anzuschließen, um nicht dazu zu führen, dass der Schnellladeadapter ein Netzteil mit einem höheren als 5 V falsch ausgibt, was zu einer Beschädigung des Stromversorgungsteils der Entwicklungsplatine führt. **
&emsp; &emsp; Verwenden Sie den K2-Kippschalter zum Ein- und Ausschalten, wie in der folgenden Abbildung dargestellt. 

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-3.jpg" width=50%>
</div>

<center>Abbildung 3-3 Beschreibung des Netzschalters</center>

<div style="page-break-after:always"></div>

## 3.3 Speichergeräte

&emsp; &emsp; Der K510 CRB enthält eine Vielzahl von Speichergeräten an Bord, darunter DDR-, eMMC-, NAND-Flash- und TF-Karten.

### 3.3.1 eMMC

&emsp; &emsp; Ein 4G Bytes eMMC-Speicher auf dem K510 CRB, der sich auf dem Kernmodul befindet, kann zum Speichern von Daten wie Startcode und Benutzerdateien verwendet werden.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-eMMC.png" width=70%>
</div>

<center>Abbildung 3-4 eMMC-Speicher</center>

### 3.3.2 NandFlash

&emsp; &emsp; Der K510 CRB verfügt über 128 MB NAND-Flash-Speicher, der zum Speichern von Daten wie Startcode und Benutzerdateien verwendet werden kann.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_5.jpg " width=75%>
</div>

<center>Abbildung 3-5 NAND-Flash-Speicher</center>

### 3.3.2 TF-Karte

&emsp; &emsp; Der K510 CRB verfügt über einen TF-Kartenhalter an Bord, der extern an eine TF-Karte angeschlossen werden kann, um Daten wie Startcode und Benutzerdateien zu speichern.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_6.png">
</div>

<center>Abbildung 3-6 TF-Kartenhalter</center>

<div style="page-break-after:always"></div>

## 3.4 Tastenanschläge

&emsp; &emsp; Der K510 CRB enthält zwei Benutzertasten, mit denen Benutzer die Tipptasten so anpassen können, dass sie als Systemeingaben oder andere softwarebezogene Funktionen ausgelöst werden.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_7.jpg" width=50%>
</div>

<center>Abbildung 3-7 Tasten</center>

## 3,5 LEDs

&emsp; &emsp; Der K510 CRB hat eine Leuchtdiode an Bord, die direkt mit dem GPIO-Pin des K510-Chips verbunden ist.

&emsp; &emsp; Der K510 CRB befindet sich an Bord einer farbigen LED WS2812, die direkt mit dem GPIO-Pin des K510-Chips verbunden ist.

&emsp; &emsp; Die beiden LEDs sind individuell auf Licht oder Löschen programmiert und können als Systemausgänge oder softwarebezogene Statusanzeigen verwendet werden.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_8.jpg" width=60%>
</div>

<center>Abbildung 3-8 LED</center>

<div style="page-break-after:always"></div>

## 3.6 Boot-Modus und Reset

&emsp; &emsp; Der K510 CRB verfügt über eine Vielzahl von Speichergeräten an Bord, und der Boot-Modus wird durch Konfigurieren der Ebenen der Boot-Pins BOOT0 und BOOT1 ausgewählt, wobei 0 und 1 niedrige und hohe Pegel darstellen.

&emsp; &emsp; Auf der Leiterplatte wird der Startmodus durch den in der folgenden Abbildung gezeigten DIP-Schalter ausgewählt, und das Kernmodul wurde entwickelt, um BOOT0 und BOOT1 hochzuziehen, und die Seite des Einwahllichts, das ON markiert, stellt den entsprechenden Bit-Pull-Down-Effekt dar, und die andere Seite von ON entspricht OFF stellt den effektiven Pull-up dar.

&emsp; &emsp; Der K510 bestimmt den Chip-Boot-Modus anhand des Status der Boot0- und BOOT1-Hardware-Pins, und die Auswahl des Boot-Modus ist in der folgenden Tabelle dargestellt.

<center>Tabelle 2-1 Boot-Modi</center>

| BOOT1   | BOOT0   | Startmodus      |
| ------- | ------- | ------------ |
| 0(EIN)   | 0(EIN)   | Booten der seriellen Schnittstelle      |
| 0(EIN)   | 1(AUS)  | Die SD-Karte bootet      |
| 1(AUS)  | 0(EIN)   | NANDFLASH-Stiefel |
| 1(AUS)  | 1(AUS)  | EMMC-Stiefel      |

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_9.jpg" width=60%>
</div>

<center>Abbildung 3-9 Rücksetzschalter und DIP-Schalter für den Startmodus</center>

&emsp; &emsp; Die integrierte Reset-Taste K510 CRB ist in Abbildung 3-9 K2, die gedrückt werden kann, um einen Hardware-Reset-Vorgang des Systems durchzuführen.

<div style="page-break-after:always"></div>

## 3.7 Audio-Eingang und -Ausgang

&emsp; &emsp; Der K510 CRB verwendet Nuvotons Audio-Codec-Chip NAU88C22, um Ein- und Ausgabefunktionen für Sprache zu implementieren. Enthält ein integriertes Mikrofon, eine standardmäßige 3,5-mm-Kopfhörerbuchse und einen 2P-Lautsprecheranschluss.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-10.jpg" width=60%>
</div>

<center>Abbildung 3-10 Audio</center>

## 3.8 USB-OTG-Buchse

&emsp; &emsp; Die integrierte USB-OTG-Buchse K510 CRB kann zur Implementierung von USB-Host-/Gerätefunktionen verwendet werden.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_11.jpg">
</div>

<center>Abbildung 3-11 USB-OTG-Sitz</center>

<div style="page-break-after:always"></div>

## 3.9 UART-Schnittstelle

&emsp; &emsp; K510 CRB Um die Anwenderentwicklung und das Debugging zu erleichtern, verfügt das K510 CRB über eine USB->-UART-Schnittstelle, die über die serielle USART-Port-Kommunikation und das Debugging des K510 über das PC-USB-Kabel betrieben werden kann. Die erste Verwendung kann das Laden des Treibers erfordern, wie in Abschnitt 4.2 beschrieben. Die integrierte UART-Schnittstelle ist in der folgenden Abbildung dargestellt.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_12.jpg" width=50%>
</div>

<center>Abbildung 3-12 USB-UART-Schnittstelle</center>

## 3.10 WIFI/BT-Modul

&emsp; &emsp; Der K510 CRB enthält ein WIFI/BT 2-in-1-Modul AP6212, um die Entwicklungsplatine für Netzwerkkonnektivität und Bluetooth-Kommunikationsfunktionen zu erweitern, wie in der On-Board-Schnittstelle unten gezeigt.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-13.jpg" width=40%>
</div>

<center>Abbildung 3-13 WIFI/BT-Modul</center>

<div style="page-break-after:always"></div>

## 3.11 Ethernet

&emsp; &emsp; Der K510 CRB verfügt über einen integrierten Gigabit-Ethernet-Halter, und der K510 wird über einen externen PHY-Chip mit RGMII-Schnittstelle realisiert. Die integrierte Schnittstelle ist in der folgenden Abbildung dargestellt.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_14.jpg" width=60%>
</div>

<center>Abbildung 3-14 Ethernet-Schnittstelle</center>

## 3.12 HDMI-Ausgang

&emsp; &emsp; Die integrierte HDMI-A-Buchse des K510 CRB kann über ein Standard-HDMI-Kabel über die mipi-DSI-Schnittstellenausgangskonvertierung des K510 an das externe Display angeschlossen werden. Die integrierte Schnittstelle ist in der folgenden Abbildung dargestellt.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_15.jpg" width=60%>
</div>

<center>Abbildung 3-15 HDMI-Schnittstelle</center>

 **Hinweis**: Da sowohl die HDMI- als auch die 1080P-TFT-Displays mipi-dsi-Treiber verwenden, können sie nur eines der beiden Displays auswählen, können nicht gleichzeitig verwendet werden, schalten über den Steuerpin GPIO um, um einen der Ausgänge auszuwählen. 

<div style="page-break-after:always"></div>

## 3.13 Video-Eingang

&emsp; &emsp; Der K510 CRB zieht mipi CSI, DVP, Netzteil und partielles GPIO über einen 0,8-mm-Raster-Board-zu-Board-Anschluss, um Kameraeingaben in verschiedenen Szenarien und unterschiedlichen Nachfragesituationen zu erzielen. Die integrierte Schnittstelle ist in der folgenden Abbildung dargestellt. Die Schnittstellendefinitionen sind in der folgenden Tabelle aufgeführt.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-16.jpg">
</div>

<center>Abbildung 3-16 Video-IN-Schnittstelle</center>

<center>Tabelle 3-2 Definition der Video-IN-Schnittstelle</center>

| Nummerierung | Definition             | Nummerierung | Definition                       |
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
| 29   | 1V8              | 32   | 3V3          |
| 30   | 1V8              | 31   | 3V3          |

**Hinweis**: Achten Sie beim externen Anschluss auf den Pegelbereich der angeschlossenen Pins, um zu verhindern, dass der falsche Spannungseingang den K510-Chip dauerhaft beschädigt. 

<div style="page-break-after:always"></div>

## 3.14 Videoausgang

&emsp; &emsp; Der K510 CRB verfügt über eine 30P-Klappe mit einem Rastermaß von 0,5 mm unter dem FPC-Anschluss für den Anschluss an ein externes LCD-Display, wie in der folgenden Abbildung dargestellt. Die Schnittstellendefinitionen sind in der folgenden Tabelle aufgeführt.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-17.jpg">
</div>

<center>Abbildung 3-17 Videoausgang-Schnittstelle</center>

<center>Tabelle 3-3 Videoausgang-Schnittstellendefinitionen</center>

| Nummerierung | Definition              | Nummerierung | Definition             |
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

## 3.15 Erweitern der Schnittstelle

&emsp; &emsp; Um die Implementierung von benutzerdefinierten Erweiterungsfunktionen für Benutzer zu erleichtern, ist beim K510 CRB ein 30P 2,54mm Erweiterungspin reserviert, der zu einer Stromversorgung und einem Teil des GPIO führt, den der Benutzer über die Software iomux bedienen kann, um Hardwareressourcen wie I2C, UART, SPI auf den entsprechenden GPIO abzubilden, um eine externe Verbindung und Erweiterung der entsprechenden Funktionen zu erreichen. Die integrierte Schnittstelle ist in der folgenden Abbildung dargestellt. Die detaillierten Definitionen sind in der folgenden Tabelle aufgeführt.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw-3-18.jpg">
</div>

<center>Abbildung 3-18 40P-Pin-Erweiterungsschnittstelle</center>

<center>Tabelle 3-4 Erweiterte Schnittstellendefinitionen</center>

| Nummerierung | Definition         | Nummerierung | Definition         |
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

**Hinweis**: Achten Sie beim externen Anschluss auf den Pegelbereich der angeschlossenen Pins, um zu verhindern, dass der falsche Spannungseingang den K510-Chip dauerhaft beschädigt. 

<div style="page-break-after:always"></div>

# 4 Verwendung von Entwicklungsboards

## 4.1 Installieren des Treibers

&emsp; &emsp; Der K510 CRB verfügt über einen integrierten ch340E, um die USB-UART-Kommunikationsfunktion zu implementieren, daher muss der entsprechende Treiber vor der Verwendung installiert werden.

&emsp; &emsp; Verwenden Sie den Treiber im Paket oder laden Sie ihn herunter und installieren Sie ihn unter der folgenden Adresse.

&emsp;&emsp;<http://www.wch.cn/product/CH340.html>

## 4.2 Firmware-Brennen

&emsp; &emsp; Bitte beachten Sie[ die K510_SDK_Build_and_Burn_Guide ](./K510_SDK_Build_and_Burn_Guide.md)Dokumentation. 

## 4.3 Ein- und Ausschalten

&emsp; &emsp; 1) Installieren Sie das Netzkabel und das USB-Debugging-Kabel.

&emsp; &emsp; 2) DIP-Schalter ausgewählt, um von der TF-Karte zu starten.

&emsp; &emsp; 3) Schalten Sie den Schalter ein, indem Sie den Schalter umschalten, wie in Abschnitt 3.2 gezeigt.

## 4.4 Debugging der seriellen Schnittstelle

&emsp; &emsp; Schalten Sie nach der Installation des Treibers den K510 CRB ein, woraufhin der Port im Geräte-Manager - Port des PCs angezeigt wird.

&emsp; &emsp; Öffnen Sie mit dem Debugging-Tool für den seriellen Port die Portnummer des Geräts, Baudrate 115200.

&emsp; &emsp; Wie in der folgenden Abbildung dargestellt, handelt es sich bei dem Gerät um "COM6", das im PC-Geräte-Manager angezeigt wird.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_4_1.jpg">
</div>

<center>Abbildung 4-1 Geräte-Manager nach Abschluss der Treiberinstallation</center>

**Haftungsausschluss **für Übersetzungen  
Für die Bequemlichkeit der Kunden verwendet Canaan einen KI-Übersetzer, um Text in mehrere Sprachen zu übersetzen, die Fehler enthalten können. Wir übernehmen keine Gewähr für die Genauigkeit, Zuverlässigkeit oder Aktualität der bereitgestellten Übersetzungen. Canaan haftet nicht für Verluste oder Schäden, die durch das Vertrauen auf die Richtigkeit oder Zuverlässigkeit der übersetzten Informationen verursacht werden. Wenn es einen inhaltlichen Unterschied zwischen den Übersetzungen in verschiedenen Sprachen gibt, ist die vereinfachte chinesische Version maßgebend. 

Wenn Sie einen Übersetzungsfehler oder eine Ungenauigkeit melden möchten, können Sie uns gerne per E-Mail kontaktieren.
