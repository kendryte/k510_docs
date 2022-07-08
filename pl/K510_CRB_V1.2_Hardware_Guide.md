![](../zh/images/canaan-cover.png)
&nbsp;
&nbsp;
**<font face="黑体" size="6" style="float:right">K510 CRB V1.2 Przewodniki sprzętowe</font>**

<font face="黑体" size=100>&nbsp;
&nbsp;
&nbsp;</font>

<font face="黑体"  size=3>Wersja dokumentu: V1.0.0</font>

<font face="黑体"  size=3>Opublikowano: 2022-03-15</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Zrzeczenie się**</font>
Zakupione produkty, usługi lub funkcje podlegają umowom handlowym i warunkom Beijing Canaan Jiesi Information Technology Co., Ltd. ("Spółka", ta sama poniżej), a wszystkie lub część produktów, usług lub funkcji opisanych w niniejszym dokumencie może nie być objęta zakresem zakupu lub użytkowania. O ile nie uzgodniono inaczej w umowie, Firma zrzeka się wszelkich oświadczeń lub gwarancji, wyraźnych lub dorozumianych, co do dokładności, niezawodności, kompletności, marketingu, konkretnego celu i nieagresji jakichkolwiek oświadczeń, informacji lub treści tego dokumentu. O ile nie uzgodniono inaczej, niniejszy dokument jest dostarczany jako wskazówka wyłącznie do użytku.
Ze względu na aktualizacje wersji produktu lub z innych powodów zawartość tego dokumentu może być od czasu do czasu aktualizowana lub modyfikowana bez powiadomienia. 

**<font face="黑体"  size=3>Informacje o znakach towarowych</font>**

""<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, ikona "Canaan", Canaan i inne znaki towarowe Canaan oraz inne znaki towarowe Canaan są znakami towarowymi Beijing Canaan Jiesi Information Technology Co., Ltd. Wszystkie inne znaki towarowe lub zarejestrowane znaki towarowe, które mogą być wymienione w niniejszym dokumencie, są własnością ich odpowiednich właścicieli. 

**<font face="黑体"  size=3>Prawa autorskie ©2022 Beijing Canaan Jiesi Information Technology Co., Ltd</font>**
Niniejszy dokument ma zastosowanie wyłącznie do rozwoju i projektowania platformy K510, bez pisemnej zgody firmy, żadna jednostka ani osoba fizyczna nie może rozpowszechniać części lub całości treści tego dokumentu w jakiejkolwiek formie. 

**<font face="黑体"  size=3>Pekin Canaan Jiesi Information Technology Co Ltd</font>**
Adres internetowy: canaan-creative.com
Zapytania biznesowe: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# przedmowa
**<font face="黑体"  size=5>Przeznaczenie </font>**dokumentu
Ten dokument jest dokumentem towarzyszącym zestawowi K510 SDK i ma na celu pomóc inżynierom w zrozumieniu kompilacji i nagrywania zestawu K510 SDK. 

**<font face="黑体"  size=5>Obiekty programu Reader</font>**

Główne osoby, których dotyczy ten dokument (ten przewodnik):

- Programiści
- Personel wsparcia technicznego

**<font face="黑体"  size=5>Historia</font>**
 zmian <font face="宋体"  size=2>Historia zmian gromadzi opis każdej aktualizacji dokumentu. Najnowsza wersja dokumentu zawiera aktualizacje dla wszystkich poprzednich wersji. </font>

| Numer wersji | Zmodyfikowane przez    | Data aktualizacji   | Uwagi do poprawek           |
| :----- | --------- | ---------- | ------------------ |
| Wersja 1.0.0 | Dział Produktów AI | 2022-03-15 | |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Treść</font>**

[Toc]

<div style="page-break-after:always"></div>

# 1 Przegląd

&emsp; &emsp; K510 CRB to platforma rozwoju sprzętu dla układu Canaan Kendryte K510 AI, która integruje projekt referencyjny, debugowanie i testowanie chipów oraz weryfikację rozwoju produktu użytkownika, która służy do zademonstrowania potężnej mocy obliczeniowej i funkcji układu K510. Jednocześnie zapewnia klientom sprzętowe projekty referencyjne oparte na układach K510, dzięki czemu klienci nie muszą modyfikować ani po prostu modyfikować obwodu modułu projektu referencyjnego i mogą ukończyć prace nad rozwojem sprzętu produktu z układami K510 jako rdzeniem.

&emsp; &emsp; K510 CRB obsługuje rozwój sprzętu, projektowanie oprogramowania aplikacyjnego, debugowanie i działanie układu K510, ponieważ biorąc pod uwagę różne środowiska użytkowania, układ jest w pełni funkcjonalną weryfikacją, więc różne interfejsy są kompletne, a projekt jest stosunkowo kompletny. K510 CRB można podłączyć do komputera za pomocą USB, używanego jako podstawowy system programistyczny, lub do bardziej kompletnego systemu programistycznego i środowiska demonstracyjnego, łącząc następujące urządzenia i komponenty:

- zasilacz

- Urządzenie pamięci masowej TF Card

- Wyświetlacz LCD MIPI DSI

- Moduł kamery MIPI CSI

- Moduł kamery DVP

- sieciowy Ethernet

- Wyświetlacz HDMI

- Słuchawki lub głośniki

- Rozszerz części zamienne

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-K510_Core.png">
</div>

  <center>Rysunek 1-1 Renderowanie CRB K510</center>

    **禁止事项**

  1. Zabrania się podłączania i odłączania modułu rdzeniowego i modułów peryferyjnych na żywo!
  2. Zabrania się bezpośredniej obsługi tego produktu bez środków wyładowania elektryczności statycznej lub bez ochrony statycznej.
  3. Zabrania się używania rozpuszczalników organicznych lub cieczy do czyszczenia tego produktu.
  4. Zabronione jest wykonywanie czynności takich jak stukanie i skręcanie, które mogą spowodować uszkodzenia fizyczne.

    **Środki ostrożności**

  1. Należy pamiętać, że po wyładowaniu elektrostatycznym ludzkiego ciała, przed użyciem tego produktu, zaleca się noszenie bransoletki elektrostatycznej.
  2. Przed rozpoczęciem pracy należy potwierdzić napięcie zasilania i napięcie adaptera płyty montażowej w dopuszczalnym zakresie opisanym w niniejszym dokumencie.
  3. Pamiętaj, aby przeczytać ten dokument i uwagi w pliku inżynierskim przed projektowaniem.
  4. Należy pamiętać, że stosowanie produktów w środowisku o wysokiej temperaturze, wysokiej wilgotności i wysokiej korozji wymaga specjalnej obróbki, takiej jak rozpraszanie ciepła, drenaż i uszczelnianie.
  5. Nie naprawiaj i nie demontuj się, w przeciwnym razie nie będziesz mógł cieszyć się bezpłatną obsługą posprzedażną.

<div style="page-break-after:always"></div>

## 1.1 Schemat blokowy systemu

&emsp; &emsp; Schemat blokowy systemu służy do opisania zasad projektowania K510 CRB i relacji między komponentami, dzięki czemu korzystanie z K510 CRB i programistów może intuicyjnie zrozumieć architekturę i zasady całego systemu.

&emsp; &emsp; Więcej informacji na temat funkcji K510 można znaleźć w pełnej karcie katalogowej K510.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_1_2.png">
</div>

<center>Rysunek 1-2 Skład K510 CRB</center>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_1_3.png">
</div>

<center>Rysunek 1-3 Schemat blokowy systemu CRB K510 </center>

<div style="page-break-after:always"></div>

&emsp; &emsp; Zestaw rozwojowy K510 CRB składa się głównie z następujących komponentów:

| Części | ilość |
| :-: | :-: |
| K510 CRB płyta główna | 1 |
| USB typu C线缆 | 2 |
| Micro USB OTG | 1 |
| Wyświetlacz MIPI DSI o rozdzielczości 1920x1080 | 1 |
| Sub-board kamery MIPI CSI, wbudowany czujnik obrazu Sony IMX219 dwa | 1 |
| Akrylowa obudowa ochronna | 1 |

<div style="page-break-after:always"></div>

## 1.2 Przegląd funkcji

&emsp; &emsp; K510 SDK jest oparty na buildroot jako podstawowej strukturze, z jądrem K510 linux (linux wersja 4.17.0), u-boot (wersja u-boot 2020.01), riscv-pk-k510

&emsp; &emsp; Główne cechy K510 CRB V1.2 (jeśli nie ma specjalnych deklaracji, wersje CRB opisane w dalszej części tego dokumentu to V1.2) są następujące:

- PMIC: Zarządzanie energią
- 32-bitowy LPDDR3EE, całkowita pojemność 512MByte
- 8-bitowy eMMC, całkowita pojemność 4GByte
- QSPI NAND, całkowita pojemność 128MByte
- Karta TF: Obsługuje zewnętrzną rozbudowę pamięci kart TF.
- USB OTG: Aktualizacja systemu, obsługa przełączania hosta / urządzenia
- SDIO WIFI: Obsługuje funkcję bezprzewodowego Internetu i połączenie Bluetooth
- Audio: Obsługa wejścia i wyjścia głosowego
- PDM MIC: funkcja budzenia VAD
- Uart & JTAG Debug: Płytki programistyczne używane przez Debug
- Wejście wideo: Podwójne wejście kamery MIPI CSI 2lane
- Wyjście wideo: MIPI DSI 4lane, wyświetlacz 1080P
- RGMII: Połączenie Gigabit Ethernet
- HDMI: Interfejs multimedialny o wysokiej rozdzielczości
- Rozszerzone interfejsy: zasilanie, GPIO, I2C, SPI
- Klucze, wskaźniki

<div style="page-break-after:always"></div>

# 2 Wprowadzenie do zasobów sprzętowych

## 2.1 Ogólne renderowanie

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_1.png" width=80%>
</div>

<center> Rysunek 2-1 Przód płyty głównej </center>

<div style="page-break-after:always"></div>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_2.png" width=80%>
</div>

<center> Rysunek 2-1 Z tyłu płyty głównej </center>

<div style="page-break-after:always"></div>

## 2.2 Schematyczny schemat struktury i interfejsu

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_3.png" width=120%>
</div>

<center> Rysunek 2-3 Położenie każdego urządzenia z przodu płyty głównej </center>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2-4.png" width=120%>
</div>

<center> Rysunek 2-4 Tył płyty głównej </center>

<div style="page-break-after:always"></div>

## 2.3 Schemat bloków zasilania

&emsp; &emsp; K510 CRB wykorzystuje DC-5V jako moc wejściową całej płyty, zapewniając DC-5V dla modułu rdzeniowego K510 CORE oraz 1,8 V i 3,3 V dla innych urządzeń peryferyjnych płyty montażowej przez dwa DC-DC.

## 2.4 Adres urządzenia I2C

<center>Tabela 2-1 Tabela adresowa urządzeń I2C</center>

| nazwa | Piny (SCL, SDA) | adres | uwaga |
| :-: | :-: | :-: | :-: |
| ekran dotykowy | IO_103、IO_102 | 0x14 lub 0x5D | |
| Złącze HDMI | IO_117、IO_116 | 0x3B | |
| Kodek audio | IO_117、IO_116 | 0x1A | |
| Kamera MIPI CSI0 | IO_120、IO_121 | 0x10 | |
| Kamera MIPI CSI1 | IO_47、IO_48   | 0x10 | |

## 2.5 Schematy

&emsp; &emsp; Schemat referencyjny dla płytki rozwojowej K510 CRB należy pobrać[ w momencie wydania](https://github.com/kendryte/k510_docs/releases). 

<div style="page-break-after:always"></div>

# 3 Wprowadzenie do każdej sekcji rady rozwoju

## 3.1 Podstawowe moduły

&emsp; &emsp; Przed użyciem K510 CRB do nauki i rozwoju zaleca się zapoznanie się ze szczegółową architekturą układu w instrukcji K510, aby można było lepiej zrozumieć zasilanie, pamięć masową, zasoby obliczeniowe i urządzenia peryferyjne K510, co sprzyja znajomości i rozwojowi rozwiązania chipowego. Płyta rdzenia K510 pokazano na rysunku 3-1.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_1.png">
</div>

<center>Rysunek 3-1 K510 Core Core Module</center>

<div style="page-break-after:always"></div>

## 3.2 Zasilanie wejściowe

&emsp; &emsp; K510 CRB wykorzystuje zewnętrzny zasilacz 5V, na pokładzie dwa interfejsy USB typu C, może być używany do zasilania płytki rozwojowej, z której interfejs UART służy do podłączenia do komputera, interfejs USB KOMPUTERA może dostarczyć tylko prąd 500mA, w przypadku niewystarczającego zasilania należy jednocześnie użyć adaptera do zasilania prądem stałym: 5V. Interfejs pokazano na poniższym rysunku.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_2.png" width=60%>
</div>

<center> Rysunek 3-2 Złącze wejściowe zasilania </center>

**Uwaga: Ogranicz korzystanie z zasilacza 5V, podczas korzystania z adaptera szybkiego ładowania staraj się nie podłączać innych urządzeń, takich jak telefony komórkowe w tym samym czasie, aby nie spowodować nieprawidłowego wyjścia zasilacza przez adapter szybkiego ładowania wyższego niż 5V, co spowoduje uszkodzenie części zasilacza płytki rozwojowej. **
&emsp; &emsp; Użyj przełącznika K2 do włączania i wyłączania zasilania, jak pokazano na poniższym rysunku. 

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-3.jpg" width=50%>
</div>

<center>Rysunek 3-3 Opis przełącznika zasilania</center>

<div style="page-break-after:always"></div>

## 3.3 Urządzenia pamięci masowej

&emsp; &emsp; K510 CRB zawiera na pokładzie wiele urządzeń pamięci masowej, w tym DDR, eMMC, NAND Flash i tf Card.

### 3.3.1 eMMC

&emsp; &emsp; Pamięć 4G Bytes eMMC na pokładzie K510 CRB, umieszczona na module podstawowym, może być używana do przechowywania danych, takich jak kod startowy i pliki użytkownika.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-eMMC.png" width=70%>
</div>

<center>Rysunek 3-4 Pamięć eMMC</center>

### 3.3.2 NandFlash

&emsp; &emsp; K510 CRB zawiera 128 MB bajtów pamięci NAND Flash, która może być używana do przechowywania danych, takich jak kod startowy i pliki użytkownika.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_5.jpg " width=75%>
</div>

<center>Rysunek 3-5 Pamięć NAND Flash</center>

### 3.3.2 Karta TF

&emsp; &emsp; K510 CRB ma na pokładzie uchwyt na kartę TF, który można podłączyć zewnętrznie do karty TF w celu przechowywania danych, takich jak kod startowy i pliki użytkownika.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_6.png">
</div>

<center>Rysunek 3-6 Uchwyt karty TF</center>

<div style="page-break-after:always"></div>

## 3.4 Naciśnięcia

&emsp; &emsp; K510 CRB zawiera dwa przyciski dotykowe użytkownika, które umożliwiają użytkownikom dostosowanie przycisków stuknięć, aby wyzwalały je jako wejścia systemowe lub inne funkcje związane z oprogramowaniem.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_7.jpg" width=50%>
</div>

<center>Rysunek 3-7</center>

## 3.5 Diody LED

&emsp; &emsp; K510 CRB ma na pokładzie diodę elektroluminescencyjną, która jest podłączona bezpośrednio do pinu GPIO układu K510.

&emsp; &emsp; K510 CRB znajduje się na pokładzie kolorowej diody LED WS2812, która jest podłączona bezpośrednio do pinu GPIO układu K510.

&emsp; &emsp; Obie diody LED są specjalnie zaprogramowane do świecenia lub gaszenia i mogą być używane jako wyjścia systemowe lub wskazania stanu związane z oprogramowaniem.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_8.jpg" width=60%>
</div>

<center>Rysunek 3-8 LED</center>

<div style="page-break-after:always"></div>

## 3.6 Tryb rozruchu i resetowania

&emsp; &emsp; K510 CRB ma na pokładzie wiele urządzeń pamięci masowej, a tryb rozruchu jest wybierany przez skonfigurowanie poziomów pinów rozruchowych, BOOT0 i BOOT1, przy czym 0 i 1 reprezentują niskie i wysokie poziomy.

&emsp; &emsp; Na płytce drukowanej tryb uruchamiania jest wybierany przez przełącznik DIP pokazany na poniższym rysunku, a moduł rdzeniowy został zaprojektowany do podciągania BOOT0 i BOOT1, a bok oznaczenia światła on-dialing ON reprezentuje odpowiedni bit pull down effective, a druga strona ON odpowiada OFF reprezentuje efektywne podciąganie.

&emsp; &emsp; K510 określa tryb rozruchu układu na podstawie stanu pinów sprzętowych boot0 i BOOT1, a wybór trybu rozruchu pokazano w poniższej tabeli.

<center>Tabela 2-1 Tryby rozruchu</center>

| ROZRUCH1   | BOOT0   | Tryb uruchamiania      |
| ------- | ------- | ------------ |
| 0(WŁ.)   | 0(WŁ.)   | Rozruch z portu szeregowego      |
| 0(WŁ.)   | 1 (WYŁ.)  | Uruchamianie karty SD      |
| 1 (WYŁ.)  | 0(WŁ.)   | Buty NANDFLASH |
| 1 (WYŁ.)  | 1 (WYŁ.)  | Buty EMMC      |

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_9.jpg" width=60%>
</div>

<center>Rysunek 3-9 Przełącznik resetowania i przełącznik DIP trybu startu</center>

&emsp; &emsp; Wbudowany przycisk resetowania K510 CRB to K2 na rysunku 3-9, który można nacisnąć, aby wykonać operację resetowania sprzętowego systemu.

<div style="page-break-after:always"></div>

## 3.7 Wejście i wyjście audio

&emsp; &emsp; K510 CRB wykorzystuje układ kodeka audio Nuvoton, NAU88C22, do implementacji funkcji wejściowych i wyjściowych dla mowy. Zawiera wbudowany mikrofon, standardowe gniazdo słuchawkowe 3,5 mm i złącze głośnika 2P.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-10.jpg" width=60%>
</div>

<center>Rysunek 3-10 Audio</center>

## Gniazdo OTG 3.8 USB

&emsp; &emsp; Wbudowane gniazdo USB OTG K510 CRB może być użyte do zaimplementowania funkcji hosta/urządzenia USB.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_11.jpg">
</div>

<center>Rysunek 3-11 Gniazdo USB-OTG</center>

<div style="page-break-after:always"></div>

## 3.9 Interfejs UART

&emsp; &emsp; K510 CRB Aby ułatwić rozwój i debugowanie użytkownika, K510 CRB ma na pokładzie interfejs USB-> UART, który może być obsługiwany przez komunikację portu szeregowego USART i debugowanie K510 za pomocą PC-USB. Początkowe użycie może wymagać załadowania sterownika, jak opisano w sekcji 4.2. Wbudowany interfejs UART pokazano na poniższym rysunku.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_12.jpg" width=50%>
</div>

<center>Rysunek 3-12 Interfejs USB-UART</center>

## 3.10 Moduł WIFI/BT

&emsp; &emsp; K510 CRB zawiera moduł 2-w-1 WIFI/BT AP6212, który rozszerza płytkę rozwojową o łączność sieciową i funkcje komunikacji Bluetooth, jak pokazano w interfejsie pokładowym poniżej.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-13.jpg" width=40%>
</div>

<center>Rysunek 3-13 Moduł WIFI/BT</center>

<div style="page-break-after:always"></div>

## 3.11 Ethernet

&emsp; &emsp; K510 CRB ma wbudowany uchwyt Gigabit Ethernet, a K510 jest realizowany za pośrednictwem zewnętrznego układu PHY z interfejsem RGMII. Interfejs pokładowy pokazano na poniższym rysunku.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_14.jpg" width=60%>
</div>

<center>Rysunek 3-14 Interfejs Ethernet</center>

## Wyjście hdmi 3.12

&emsp; &emsp; Żeński uchwyt USB-A K510 CRB można podłączyć do zewnętrznego wyświetlacza za pomocą standardowego HDMI, korzystając z konwersji wyjściowej interfejsu mipi dsi K510. Interfejs pokładowy pokazano na poniższym rysunku.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_15.jpg" width=60%>
</div>

<center>Rysunek 3-15 Interfejs HDMI</center>

 **Uwaga**: Ponieważ zarówno wyświetlacze TFT HDMI, jak i 1080P używają sterowników mipi dsi, mogą wybrać tylko jeden z dwóch wyświetlaczy, nie mogą być używane w tym samym czasie, przełącz się przez pin sterujący GPIO, aby wybrać jedno z wyjść. 

<div style="page-break-after:always"></div>

## 3.13 Wejście wideo

&emsp; &emsp; K510 CRB pobiera mipi CSI, DVP, zasilacz i częściowe GPIO przez złącze 0,8 mm od płytki do płyty, aby uzyskać wejście kamery w różnych scenariuszach i różnych sytuacjach zapotrzebowania. Interfejs pokładowy pokazano na poniższym rysunku. Definicje interfejsów przedstawiono w poniższej tabeli.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-16.jpg">
</div>

<center>Rysunek 3-16 Interfejs Video IN</center>

<center>Tabela 3-2 Definicje interfejsu Video IN</center>

| numerowanie | definicja             | numerowanie | definicja                       |
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
| 29   | 1 na 8              | 32   | 3V3          |
| 30   | 1 na 8              | 31   | 3V3          |

**Uwaga**: Zwróć uwagę na zakres poziomów podłączonych pinów podczas podłączania zewnętrznego, aby zapobiec trwałemu uszkodzeniu układu K510 przez niewłaściwe wejście napięciowe. 

<div style="page-break-after:always"></div>

## 3.14 Wyjście wideo

&emsp; &emsp; K510 CRB ma klapę 30P o skoku 0,5 mm pod złączem FPC do podłączenia do zewnętrznego wyświetlacza LCD, jak pokazano na poniższym rysunku. Definicje interfejsów przedstawiono w poniższej tabeli.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-17.jpg">
</div>

<center>Rysunek 3-17 Interfejs wyjścia wideo</center>

<center>Tabela 3-3 Definicje interfejsu wyjścia wideo</center>

| numerowanie | definicja              | numerowanie | definicja             |
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

## 3.15 Rozszerzenie interfejsu

&emsp; &emsp; Aby ułatwić użytkownikom wdrożenie niestandardowych funkcji rozszerzeń, pin rozszerzeń 30P 2,54 mm jest zarezerwowany na K510 CRB, co prowadzi do zasilacza i części GPIO, które użytkownik może obsługiwać za pomocą oprogramowania iomux, aby mapować zasoby sprzętowe, takie jak I2C, UART, SPI do odpowiedniego GPIO, aby uzyskać zewnętrzne połączenie i rozszerzenie odpowiednich funkcji. Interfejs pokładowy pokazano na poniższym rysunku. Szczegółowe definicje przedstawiono w poniższej tabeli.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw-3-18.jpg">
</div>

<center>Rysunek 3-18 40P pinowy interfejs przedłużający</center>

<center>Tabela 3-4 Rozszerzone definicje interfejsu</center>

| numerowanie | definicja         | numerowanie | definicja         |
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

**Uwaga**: Zwróć uwagę na zakres poziomów podłączonych pinów podczas podłączania zewnętrznego, aby zapobiec trwałemu uszkodzeniu układu K510 przez niewłaściwe wejście napięciowe. 

<div style="page-break-after:always"></div>

# 4 Wykorzystanie płytki rozwojowej

## 4.1 Instalacja sterownika

&emsp; &emsp; K510 CRB ma na pokładzie ch340E do implementacji funkcji komunikacji USB-UART, więc odpowiedni sterownik musi zostać zainstalowany przed użyciem.

&emsp; &emsp; Użyj sterownika w pakiecie lub pobierz i zainstaluj go pod następującym adresem.

&emsp;&emsp;<http://www.wch.cn/product/CH340.html>

## 4.2 Nagrywanie oprogramowania układowego

&emsp; &emsp; Zapoznaj się [z dokumentacją K510_SDK_Build_and_Burn_Guide](./K510_SDK_Build_and_Burn_Guide.md). 

## 4.3 Włączanie i wyłączanie

&emsp; &emsp; 1) Zainstaluj zasilający i debugujący USB.

&emsp; &emsp; 2) Przełącznik DIP wybrany do rozpoczęcia od karty TF.

&emsp; &emsp; 3) Włącz przełącznik, przełączając przełącznik, jak pokazano w sekcji 3.2.

## 4.4 Debugowanie portów szeregowych

&emsp; &emsp; Po zainstalowaniu sterownika włącz K510 CRB, w którym to momencie port pojawi się w Menedżerze urządzeń komputera - Port.

&emsp; &emsp; Za pomocą narzędzia do debugowania portów szeregowych otwórz numer portu urządzenia, szybkość transmisji 115200.

&emsp; &emsp; Jak pokazano na poniższym rysunku, urządzenie to "COM6", co jest pokazane w Menedżerze urządzeń PC.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_4_1.jpg">
</div>

<center>Rysunek 4-1 Menedżer urządzeń po zakończeniu instalacji sterownika</center>

**Zrzeczenie się odpowiedzialności za **tłumaczenie  
Dla wygody klientów Canaan używa tłumacza AI do tłumaczenia tekstu na wiele języków, które mogą zawierać błędy. Nie gwarantujemy dokładności, rzetelności ani terminowości dostarczonych tłumaczeń. Canaan nie ponosi odpowiedzialności za jakiekolwiek straty lub szkody spowodowane poleganiem na dokładności lub wiarygodności przetłumaczonych informacji. W przypadku różnic w treści tłumaczeń w różnych językach, pierwszeństwo ma chińska wersja uproszczona. 

Jeśli chcesz zgłosić błąd lub niedokładność tłumaczenia, skontaktuj się z nami pocztą.
