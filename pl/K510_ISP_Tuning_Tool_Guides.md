![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 ISP Tuning Tool Guides</font>**

<font face="黑体"  size=3>Wersja dokumentu: V1.0.0</font>

<font face="黑体"  size=3>Opublikowano: 2022-03-31</font>

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
Ten dokument jest dokumentacją narzędzia ISP Tuning Tool.

**<font face="黑体"  size=5>Obiekty programu Reader</font>**

Głównymi odbiorcami tego dokumentu są doświadczeni inżynierowie oprogramowania, inżynierowie algorytmów obrazu, projektanci systemów i integratorzy systemów, którzy chcą wdrażać zastrzeżone aplikacje i sterowniki.

**<font face="黑体"  size=5>Historia</font>**
 zmian <font face="宋体"  size=2>Historia zmian gromadzi opis każdej aktualizacji dokumentu. Najnowsza wersja dokumentu zawiera aktualizacje dla wszystkich poprzednich wersji. </font>

| Numer wersji   | Zmodyfikowane przez     | Data aktualizacji | Uwagi do poprawek |
|  :-----  |-------   |  ------  |  ------  |
| Wersja 1.0.0 | Grupy oprogramowania systemowego | 2022-03-31 | Sdk V1.6 wydany |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Treść</font>**

[TOC]

<div style="page-break-after:always"></div>

# Wprowadzenie do struktury narzędzi do dostrajania usługodawców internetowych

W tej sekcji opisano narzędzia do dostrajania usługodawcy internetowego i opisy strumieni danych dostarczanych procesorom wyższego poziomu w celu kontrolowania ogólnej optymalizacji obrazu usługodawcy internetowego.

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

## Dostrajanie ruchu narzędzi

Protokół komunikacyjny można znaleźć w dokumentacji w repozytorium kodu klienta, a narzędzie składa się z dwóch części, jedna jest dostrajaniem ISP klienta działającym na komputerze, program znajduje się w /app/mediactl_lib/isp-tuningd, a druga część to serwer działający na K510. Domyślnie port TCP 9982 jest używany do komunikacji.

### klient

Narzędzie dostrajania usługodawcy internetowego to aplikacja działająca na komputerze PC. Oprócz możliwości ustawiania rejestrów, obsługiwana jest również kalibracja AWB i kalibracja CCM.

### Po stronie serwera

isp-tuningd odbiera obraz yuv (NV12) o wielkości 3133440 bajtów ze standardowego wejścia i transmituje go do wszystkich klientów, możemy użyć v4l2_drm_isptool, automatycznie rozpocznie dostrajanie isp i wyśle dane obrazu, konkretne użycie jest zgodne z v4l2_drm. Możemy go uruchomić za pomocą następującego polecenia

```shell
cd /app/mediactl_lib
./v4l2_drm_isptool -f video_drm_1080x1920.conf
```

# Opcje dostrajania usługodawcy internetowego

Wiele rejestrów i tabel jest dostarczanych przez dostawcę usług internetowych K510 do sterowania i strojenia. Ustawienie rejestrów sprzętowych usługodawcy internetowego jest bardzo ważne dla jakości obrazu. Obecnie na platformie K510 proces dostrajania obrazu jest realizowany tylko przez gniazdo TCP.

## Okno główne narzędzia do dostrajania

W tej sekcji opisano funkcje tych paneli w oknie strojenia.

Rysunek 3-1 pokazuje cały panel operatora w oknie strojenia

- Panel 1 to**menu**, które może opcjonalnie załadować skonfigurowany plik ISP lub przeprowadzić kalibrację.
- Panel 2 to **panel sterowania połączeniem**, wypełnij adres IP i numer portu płytki rozwojowej (domyślny port 9982) i kliknij zielony przycisk połącz, aby się połączyć.
- Panel 3 to **panel rejestru**, jeśli chcesz ustawić lub odczytać rejestr nie znajduje się w tym, możesz użyć tego panelu do ustawienia i odczytu.
- Panel 4 jest **panelem wyboru parametrów strojenia**, użytkownik może wybrać różne parametry lub grupy parametrów zgodnie z tekstem monitu panelu, rejestry tych wyborów zostaną wyświetlone na panelu 5.
- Panel 5 to **panel Ustawienia parametrów strojenia**, który służy do ustawiania lub uzyskiwania wartości parametrów z serwera dostrajania.
- Panel 6 to **panel wyświetlania obrazu**, który wyświetla obraz wyjściowy przez dostawcę usług internetowych i może kliknąć przycisk pauzy w środku, gdy nie jest konieczne odtwarzanie przez cały czas.

![Rysunek 3-1 Okno główne narzędzia tuningu](../zh/images/sdk_application/clip_image033.png)

Narzędzie ISP Tuning Tool**nie**pobiera automatycznie wszystkich wartości rejestru po nawiązaniu połączenia, a jeśli chcesz uzyskać wszystkie wartości rejestru, możesz kliknąć**przycisk Odczyt po prawej stronie panelu sterowania połączeniem**, aby pobrać wszystkie bieżące wartości rejestru.

# Kalibracja i kalibracja

W tej sekcji opisano instrukcje dotyczące kalibracji i kalibracji przy użyciu narzędzi do dostrajania usługodawcy internetowego, w tym automatycznego balansu bieli (AWB), matrycy korekcji kolorów (CCM), gamma i cieni obiektywu (LSC).

## AWB

### Preparaty

1. Standardowa skrzynka świetlna ze standardowym źródłem światła D65
2. Standardowa karta kolorów 24, obecnie obsługiwana jest tylko karta kolorów X-RITE
3. Kamera gotowa do kalibracji może wygenerować oryginalny obraz czujnika lub przetworzony obraz
4. ISP również otwiera tylko moduł korekcji poziomu czerni i algorytmu de-mozaiki, CSC i inne moduły konwersji formatu muszą zwracać uwagę na symetrię (matryca jest odwrotną matrycą), oprócz redukcji szumów, ostrzenie i inne moduły mają niewielki wpływ, ale także starają się zamknąć, moduły nieliniowe i moduły przetwarzania kolorów (GAMMA, szeroka dynamika, AWB, CCM, regulacja nasycenia itp.) muszą być wyłączone

### Pobiera obraz

1. Aparat jest skierowany na kartę 24 kolorów, upewnij się, że karta kolorów 24 wypełnia cały obraz, a następnie chwyć obraz, który można kliknąć, aby wstrzymać odtwarzanie bez zagwarantowania dokładności, jak pokazano na poniższym rysunku

    ![Rysunek 4-1 24 karty kolorów](../zh/images/sdk_application/clip_image014.jpg)

2. Przechwycony obraz powinien zwracać uwagę na umiarkowaną jasność i ciemność, a zbyt jasny i zbyt ciemny wpłynie na kalibrację

### rozgraniczenie

Kliknij "Kalibracja" na pasku menu, wybierz "AWB", aby przeprowadzić kalibrację, a program automatycznie wybierze kartę kolorów

![Rysunek 4-2 Selektor kolorów Auto Box](../zh/images/sdk_application/clip_image016.jpg)

Naciśnij dowolny, aby kontynuować, wyskakując obraz po zakończeniu balansu bieli

![Rysunek 4-3 Kompletna kalibracja AWB](../zh/images/sdk_application/clip_image018.jpg)

Jeśli nie ma problemu, kontynuuj naciskanie dowolnego, narzędzie wyświetli okno dialogowe z pytaniem, czy parametr jest rozsądny, tak wypełni go w głównych rejestrach związanych z interfejsem, w przeciwnym razie porzuć wynik kalibracji, jeśli tak, narzędzie będzie nadal pytać, czy zapisać do rejestru urządzenia.

## DW

Zgodnie z kalibracją AWB nie będzie się powtarzać.

## Gamma

Wzór na standardową krzywą gamma jest następujący:
$$
Y=aX^b
$$
Gdzie $b$ jest współczynnikiem gamma, który jest zazwyczaj mniejszy niż 1 na końcu obrazowania i większy niż 1 na końcu wyświetlacza. Wartość $a$ można obliczyć na podstawie wartości $b$

$$
a=\frac{256}{256^b}
$$
Zasada formuły jest taka, że wejście wynosi 256, czyli nadal 256 po korekcji gamma.

Gdy współczynnik gamma b wynosi 0,5, krzywa jest pokazana na poniższym rysunku

![](../zh/images/sdk_application/clip_image025.png)

## LSC

### Preparaty

- Ujęcie przechwytuje zdjęcie w formacie RAW

### zasada

Ponieważ środek obiektywu jest niespójny z otaczającą transmisją światła, jasność obrazu jest nierówna, więc dopasowanie krzywej generuje powierzchnię korekcyjną, aby zrekompensować ten problem.

Korekta jest pokazana na poniższym rysunku

![Przed korektą](../zh/images/sdk_application/clip_image029.png)

Po korekcie pokazano to na poniższym rysunku

![Po korekcie](../zh/images/sdk_application/clip_image031.png)

**Zrzeczenie się odpowiedzialności za**tłumaczenie  
Dla wygody klientów Canaan używa tłumacza AI do tłumaczenia tekstu na wiele języków, które mogą zawierać błędy. Nie gwarantujemy dokładności, rzetelności ani terminowości dostarczonych tłumaczeń. Canaan nie ponosi odpowiedzialności za jakiekolwiek straty lub szkody spowodowane poleganiem na dokładności lub wiarygodności przetłumaczonych informacji. W przypadku różnic w treści tłumaczeń w różnych językach, pierwszeństwo ma chińska wersja uproszczona.

Jeśli chcesz zgłosić błąd lub niedokładność tłumaczenia, skontaktuj się z nami pocztą.
