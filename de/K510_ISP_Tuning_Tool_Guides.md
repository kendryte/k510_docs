![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 ISP Tuning Tool Anleitungen</font>**

<font face="黑体"  size=3>Dokumentversion: V1.0.0</font>

<font face="黑体"  size=3>Veröffentlicht: 2022-03-31</font>

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
Dieses Dokument ist eine Dokumentation des ISP-Tuning-Tools. 

**<font face="黑体"  size=5>Reader-Objekte</font>**

Die primäre Zielgruppe für dieses Dokument sind erfahrene Softwareingenieure, Bildalgorithmusingenieure, Systemdesigner und Systemintegratoren, die proprietäre Anwendungen und Treiber implementieren möchten.

**<font face="黑体"  size=5>Revisionshistorie</font>**
 <font face="宋体"  size=2>In der Revisionshistorie wird eine Beschreibung jeder Dokumentaktualisierung gesammelt. Die neueste Version des Dokuments enthält Updates für alle vorherigen Versionen. </font>

| Die Versionsnummer   | Geändert von     | Datum der Überarbeitung | Revisionshinweise |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | Systemsoftwaregruppen | 2022-03-31 | SDK V1.6 veröffentlicht |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Inhalt</font>**

[TOC]

<div style="page-break-after:always"></div>

# Einführung in das ISP Tuning Tool Framework

In diesem Abschnitt werden die ISP-Tuning-Tools und Beschreibungen der Datenströme beschrieben, die den Prozessoren der oberen Ebene zur Steuerung der gesamten ISP-Image-Optimierung zur Verfügung gestellt werden.

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

## Optimieren des Werkzeugverkehrs

Das Kommunikationsprotokoll finden Sie in der Dokumentation im Client-Code-Repository, und das Tool besteht aus zwei Teilen, einer ist der Client-ISP-Tuningd, der auf dem PC läuft, das Programm befindet sich in der /app/mediactl_lib/isp-tuningd und der andere Teil ist der Server, der auf dem K510 läuft. Standardmäßig wird der TCP-Port 9982 für die Kommunikation verwendet.

### Kunde

Das ISP Tuning Tool ist eine Anwendung, die auf einem PC ausgeführt wird. Neben der Möglichkeit, Register einzustellen, werden auch AWB-Kalibrierung und CCM-Kalibrierung unterstützt.

### Serverseitig

isp-tuningd empfängt ein Yuv-Image (NV12) in der Größe von 3133440 Bytes vom Standardeingang und sendet es an alle Clients, wir können v4l2_drm_isptool verwenden, er startet automatisch isp-tuningd und sendet die Bilddaten ein, die spezifische Verwendung ist konsistent mit der v4l2_drm. Wir können es mit dem folgenden Befehl ausführen

```shell
cd /app/mediactl_lib
./v4l2_drm_isptool -f video_drm_1080x1920.conf
```

# ISP-Tuning-Optionen

Viele Register und Tabellen werden im K510 ISP zur Steuerung und Abstimmung bereitgestellt. Die Einstellung der ISP-Hardwareregister ist für die Bildqualität sehr wichtig. Derzeit wird auf der K510-Plattform der Image-Tuning-Prozess nur über TCP Socket implementiert.

## Hauptfenster des Tuning-Tools

In diesem Abschnitt werden die Funktionen dieser Bedienfelder im Optimierungsfenster beschrieben.

Abbildung 3-1 zeigt das gesamte Bedienfeld im Tuning-Fenster

- Panel 1 ist das** Menü**, mit dem optional die konfigurierte ISP-Datei geladen oder eine Kalibrierung durchgeführt werden kann. 
- Panel 2 ist das **Verbindungssteuerungsfeld**, geben Sie die IP-Adresse und Portnummer des Entwicklungsboards (Standardport 9982) ein und klicken Sie auf die grüne Verbindungsschaltfläche, um eine Verbindung herzustellen. 
- Panel 3 ist das **Register-Bedienfeld, **wenn Sie das Register einstellen oder lesen müssen, ist nicht in diesem, können Sie dieses Panel zum Festlegen und Lesen verwenden. 
- Panel 4 ist ein** Tuning-Parameter-Auswahl-Panel**, der Benutzer kann verschiedene Parameter oder Gruppen von Parametern entsprechend dem Panel-Eingabeaufforderungstext auswählen, die Register dieser Auswahlen werden auf Panel 5 angezeigt. 
- Panel 5 ist das** Bedienfeld "Tuning Parameter Settings**", das zum Festlegen oder Abrufen von Parameterwerten vom Tuning-Server verwendet wird. 
- Panel 6 ist ein** Bildanzeigefeld, **das die Bildausgabe des ISP anzeigt und auf die Pause-Taste in der Mitte klicken kann, wenn es nicht notwendig ist, die ganze Zeit zu spielen. 

![Abbildung 3-1 Hauptfenster des Tuning-Tools](../zh/images/sdk_application/clip_image033.png)

DAS ISP Tuning Tool erfasst **nach dem Herstellen der Verbindung nicht automatisch alle Registerwerte, und wenn Sie alle Registerwerte **abrufen müssen, können Sie auf die Schaltfläche Lesen auf der rechten Seite des **Verbindungsbedienfelds **klicken, um alle aktuellen Registerwerte abzurufen. 

# Kalibrierung & Kalibrierung

In diesem Abschnitt werden Anweisungen für die Kalibrierung und Kalibrierung mit ISP-Tuning-Tools beschrieben, einschließlich automatischem Weißabgleich (AWB), Farbkorrekturmatrix (CCM), Gamma und Linsenschatten (LSC).

## AWB

### Vorbereitungen

1. Standard-Leuchtkasten mit Standard-D65-Lichtquelle
2. Standard 24 Farbkarte, derzeit wird nur X-RITE Farbkarte unterstützt
3. Eine kamera, die zur Kalibrierung bereit ist, kann ein Sensor-Originalbild oder ein verarbeitetes Bild ausgeben
4. ISP öffnen auch nur das Schwarzpegelkorrektur- und Demosaik-Algorithmus-Modul, CSC und andere Formatkonvertierungsmodule müssen auf Symmetrie achten (Matrix ist inverse Matrix), zusätzlich zur Rauschunterdrückung, Schärfung und andere Module haben wenig Einfluss, sondern versuchen auch zu schließen, nichtlineare Module und Farbverarbeitungsmodule (GAMMA, wide dynamic, AWB, CCM, Sättigungsanpassung usw.) müssen ausgeschaltet werden

### Ruft das Bild ab

1. Die Kamera ist auf die 24-Farbkarte ausgerichtet, stellen Sie sicher, dass die 24-Farbkarte das gesamte Bild ausfüllt, und greifen Sie dann auf das Bild zu, auf das geklickt werden kann, um die Wiedergabe anzuhalten, ohne die Genauigkeit zu garantieren, wie in der folgenden Abbildung dargestellt

    ![Abbildung 4-1 24 Farbkarten werden genommen](../zh/images/sdk_application/clip_image014.jpg)

2. Das aufgenommene Bild sollte auf mäßige Helligkeit und Dunkelheit achten, und zu hell und zu dunkel wirkt sich auf die Kalibrierung aus

### abgrenzen

Klicken Sie in der Menüleiste auf "Kalibrierung", wählen Sie "AWB", um die Kalibrierung durchzuführen, und das Programm wählt automatisch die Farbkarte aus

![Abbildung 4-2 Farbauswahl für automatische Boxen](../zh/images/sdk_application/clip_image016.jpg)

Drücken Sie eine beliebige Taste, um fortzufahren, und zeigen Sie das Bild an, nachdem der Weißabgleich abgeschlossen ist

![Abbildung 4-3 Vollständige AWB-Kalibrierung](../zh/images/sdk_application/clip_image018.jpg)

Wenn es kein Problem gibt, drücken Sie weiterhin eine beliebige Taste, das Tool öffnet ein Dialogfeld, in dem Sie gefragt werden, ob der Parameter angemessen ist, ja, füllt ihn in die Register der Hauptschnittstelle aus, andernfalls bricht das Kalibrierungsergebnis ab, wenn ja, fragt das Tool weiterhin, ob es in das Geräteregister schreiben soll.

## CCM

In Übereinstimmung mit der AWB-Kalibrierung wird sie nicht wiederholt.

## Gamma

Die Formel für die Standard-Gammakurve lautet
$$
Y=aX^b
$$
Dabei ist $b$ der Gamma-Koeffizient, der im Allgemeinen kleiner als 1 am Bildende und größer als 1 am Display-Ende ist. Der Wert von $a$ kann basierend auf dem Wert von $b$ berechnet werden

$$
a=\frac{256}{256^b}
$$
Das Prinzip der Formel ist, dass die Eingabe 256 ist, was nach der Gammakorrektur immer noch 256 ist.

Wenn der Gammakoeffizient b 0,5 ist, ist die Kurve in der folgenden Abbildung dargestellt

![](../zh/images/sdk_application/clip_image025.png)

## LSC

### Vorbereitungen

- Eine Aufnahme nimmt ein Foto im RAW-Format auf

### Prinzip

Da die Mitte des Objektivs nicht mit der umgebenden Lichtdurchlässigkeit übereinstimmt, ist die Bildhelligkeit ungleichmäßig, sodass die Kurvenanpassung eine korrigierende Oberfläche erzeugt, um dieses Problem auszugleichen.

Die Korrektur ist in der folgenden Abbildung dargestellt

![Vor der Korrektur](../zh/images/sdk_application/clip_image029.png)

Nach der Korrektur ist es in der folgenden Abbildung dargestellt

![Nach der Korrektur](../zh/images/sdk_application/clip_image031.png)

**Haftungsausschluss **für Übersetzungen  
Für die Bequemlichkeit der Kunden verwendet Canaan einen KI-Übersetzer, um Text in mehrere Sprachen zu übersetzen, die Fehler enthalten können. Wir übernehmen keine Gewähr für die Genauigkeit, Zuverlässigkeit oder Aktualität der bereitgestellten Übersetzungen. Canaan haftet nicht für Verluste oder Schäden, die durch das Vertrauen auf die Richtigkeit oder Zuverlässigkeit der übersetzten Informationen verursacht werden. Wenn es einen inhaltlichen Unterschied zwischen den Übersetzungen in verschiedenen Sprachen gibt, ist die vereinfachte chinesische Version maßgebend. 

Wenn Sie einen Übersetzungsfehler oder eine Ungenauigkeit melden möchten, können Sie uns gerne per E-Mail kontaktieren.