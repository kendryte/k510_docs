![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 U-boot Podręcznik programisty</font>**

<font face="黑体"  size=3>Wersja dokumentu: V1.0.0</font>

<font face="黑体"  size=3>Opublikowano: 2022-03-09</font>

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
Ten dokument jest dokumentem pomocniczym K510 demo board sdk, wprowadzającym głównie treści związane z uboot, takie jak plik konfiguracyjny płyty demonstracyjnej k510, drzewo urządzeń, lokalizacja sterownika i inne informacje w uboot. 

**<font face="黑体"  size=5>Obiekty programu Reader</font>**

Główne osoby, których dotyczy ten dokument (ten przewodnik):

- Programiści
- Personel wsparcia technicznego

**<font face="黑体"  size=5>Historia</font>**
 zmian <font face="宋体"  size=2>Historia zmian gromadzi opis każdej aktualizacji dokumentu. Najnowsza wersja dokumentu zawiera aktualizacje dla wszystkich poprzednich wersji. </font>

| Numer wersji   | Zmodyfikowane przez     | Data aktualizacji | Uwagi do poprawek |
|  :-----  |-------   |  ------  |  ------  |
| Wersja 1.0.0 | Grupy oprogramowania systemowego | 2022-03-09 |          |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Treść</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Wprowadzenie do U-Boot

U-boot jest częścią sdk, a wersja u-boot obecnie używana przez SDK to 2020.01. Uboot to program bootloadera opracowany przez niemiecką grupę DENX dla różnych wbudowanych procesorów, UBoot nie tylko obsługuje rozruch wbudowanych systemów Linux, obecnie obsługuje również NetBSD, VxWorks, QNX, RTEMS, ARTOS, LynxOS wbudowany system operacyjny. Oprócz obsługi serii procesorów PowerPC, UBoot może również obsługiwać MIPS, x86, ARM, NIOS, RISICV itp., Główne funkcje to inicjowanie pamięci, uruchamianie systemów Linux, więcej wprowadzenia u-boot, patrz<https://www.denx.de/wiki/U-Boot>

# 2 Wprowadzenie do środowiska programistycznego

- System operacyjny

| numerowanie | Zasoby dotyczące oprogramowania | Ilustrują        |
| ---- | -------- | ----------- |
| 1    | Ubuntu   | 18.04/20.04 |

- Środowisko oprogramowania

Wymagania dotyczące środowiska oprogramowania przedstawiono w poniższej tabeli:

| numerowanie | Zasoby dotyczące oprogramowania | Ilustrują |
| ---- | -------- | ---- |
| 1    | K510 SDK |      |

# 3 Jak go zdobyć

Pobierz i skompiluj sdk, sdk pobierze kod uboot podczas kompilacji i skompiluje kod uboot. Aby uzyskać więcej informacji na temat pobierania i kompilowania zestawu SDK, zobacz[ K510_SDK_Build_and_Burn_Guide.md](./K510_SDK_Build_and_Burn_Guide.md)

# 4 Ważne katalogi i opisy plików

W tym rozdziale użyto skompilowanych k510_evb_lp3_v1_1_defconfig jako przykładu. Odpowiednią metodą kompilacji sdk jest conf=k510_evb_lp3_v1_1_defconfig, a katalog po kompilacji jest następujący:

![obraz-20210930135634105](../zh/images/uboot_guides/build_out.png)

k510_evb_lp3_v1_1_defconfig/build/uboot-custom --- kod uboot i katalog kompilacji;

board/canaan/k510/uboot-sdcard.env--- domyślny plik konfiguracyjny zmiennej środowiskowej uboot

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/configs/k510_evb_lp3_v1_1_defconfig --uboot plik konfiguracyjny;

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/arch/riscv/dts/k510_evb_lp3_v1_1.dts---- plik drzewa urządzenia;

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/include/configs/k510_evb_lp3_v1_1.h--- plik nagłówka;

k510_evb_lp3_v1_1_defconfig/images/u-boot_burn.bin ---uboot oprogramowanie układowe

buildroot-2020.02.11/boot/uboot ----buildroot w skrypcie kompilacji o uboot, generalnie nie trzeba go modyfikować;

Plik konfiguracyjny Configs/k510_evb_lp3_v1_1_defconfig---sdk, BR2_TARGET_UBOOT_BOARD_DEFCONFIG określić plik konfiguracyjny uboot;

# 5 uboot rozpoczyna proces

_start (arch / riscv / cpu / start. S, linia 43)

board_init_f(common/board_f.c, wiersz 1013)

board_init_r(common/board_r.c, linia 845)

run_main_loop(common/board_r.c, linia 637)

# 6 uboot pod opisem kierowcy

## Sterownik 6.1 ddr

deska/Canaan/k510_evb_lp3/ddr_init.c

## Napęd 6.2 eth

drivers/net/macb.c

Drzewo urządzeń:

```text
ethernet@93030000 {
    compatible = "cdns,macb";
    reg = <0x0 0x93030000 0x0 0x10000>;
    phy-mode = "rmii";
    interrupts = <0x36 0x4>;
    interrupt-parent = <0x4>;
    clocks = <0x5 0x5>;
    clock-names = "hclk", "pclk";
};
```

## 6.3 Napęd z portem szeregowym

sterowniki/szeregowy/ns16550.c

Drzewo urządzeń:

```text
serial@96000000 {
    compatible = "andestech,uart16550", "ns16550a";
    reg = <0x0 0x96000000 0x0 0x1000>;
    interrupts = <0x19 0x4>;
    clock-frequency = <0x17d7840>;
    reg-shift = <0x2>;
    reg-io-width = <0x4>;
    no-loopback-test = <0x1>;
    interrupt-parent = <0x4>;
};
```

## 6.4 iomux

drivers/pinctrl/pinctrl-single.c

Drzewo urządzeń:

```text
iomux@97040000 {
    compatible = "pinctrl-single";
    reg = <0x0 0x97040000 0x0 0x10000>;
    #address-cells = <0x1>;
    #size-cells = <0x0>;
    #pinctrl-cells = <0x1>;
    pinctrl-single,register-width = <0x20>;
    pinctrl-single,function-mask = <0xffffffff>;
    pinctrl-names = "default";
    pinctrl-0 = <0x6 0x7 0x8 0x9 0xa>;

    iomux_uart0_pins {
        pinctrl-single,pins = <0x1c0 0x540ca8 0x1c4 0x5a0c69>;
        phandle = <0x6>;
    };

    iomux_emac_pins {
        pinctrl-single,pins = <0x8c 0x4e 0x90 0xce 0x88 0x8e 0x98 0x4e 0x80 0x8e 0xb8 0x4e 0xb4 0x4e 0xa8 0x8e 0xa4 0x8e 0x74 0x8e>;
        phandle = <0x7>;
    };

    iomux_spi0_pins {
        pinctrl-single,pins = <0x158 0x4e 0x15c 0x4e 0x160 0xce 0x164 0xce 0x168 0xce 0x16c 0xce 0x170 0xce 0x174 0xce 0x178 0xce 0x17c 0xce 0x180 0x8e>;
        phandle = <0x8>;
    };

    iomux_mmc0_pins {
        pinctrl-single,pins = <0x1c 0x4e 0x20 0xce 0x24 0xce 0x28 0xce 0x2c 0xce 0x30 0xce 0x34 0xce 0x38 0xce 0x3c 0xce 0x40 0xce>;
        phandle = <0x9>;
    };

    iomux_mmc2_pins {
        pinctrl-single,pins = <0x5c 0x4e 0x60 0xce 0x64 0xce 0x68 0xce 0x6c 0xce 0x70 0xce>;
        phandle = <0xa>;
    };
};
```

## Napęd kart 6,5 mmc i SD

drivers/mmc/sdhci-cadence.c

Drzewo urządzeń

```text
mmc0@93000000 {
    compatible = "socionext,uniphier-sd4hc", "cdns,sd4hc";
    reg = <0x0 0x93000000 0x0 0x400>;
    interrupts = <0x30 0x4>;
    interrupt-parent = <0x4>;
    clocks = <0xb 0x4>;
    max-frequency = <0xbebc200>;
    cap-mmc-highspeed;
    bus-width = <0x8>;
};

mmc2@93020000 {
    compatible = "socionext,uniphier-sd4hc", "cdns,sd4hc";
    reg = <0x0 0x93020000 0x0 0x400>;
    interrupts = <0x32 0x4>;
    interrupt-parent = <0x4>;
    clocks = <0xb 0x4>;
    max-frequency = <0xbebc200>;
    cap-sd-highspeed;
    bus-width = <0x1>;
};
```

# 7 Domyślna zmienna środowiskowa Uboot

Domyślna zmienna środowiskowa dla uboot znajduje się w katalogu SDK board/canaan/k510, predefiniowanym jako plik tekstowy:

uboot-emmc.plv

uboot-nfs.env

uboot-sdcard.plv

Skrypt POST zestawu SDK wywoła mkenvimage w czasie kompilacji, aby skompilować definicję zmiennej środowiskowej tekstu do obrazu binarnego, który uboot może załadować i umieścić na partycji rozruchowej.

Oto kilka przykładów:

uboot-sdcard.plv

```text
bootm_size=0x2000000
bootdelay=3

stderr=serial@96000000
stdin=serial@96000000
stdout=serial@96000000
arch=riscv
baudrate=115200

ipaddr=10.100.226.221
netmask=255.255.255.0
gatewayip=10.100.226.254
serverip=10.100.226.63
bootargs=root=/dev/mmcblk1p2 rw console=ttyS0,115200n8 debug loglevel=7

bootcmd=fatload mmc 1:1 0x600000 bootm-bbl.img;fatload mmc 1:1 0x2000000 k510.dtb;bootm 0x600000 - 0x2000000
bootcmd_nfs=tftp 0x600000 bootm-bbl.img;tftp 0x2000000 k510_nfsroot.dtb;bootm 0x600000 - 0x2000000
```

Uwaga: Parametr rozruchowy jądra bootargs jest ustawiany przez domyślną zmienną środowiskową uboot, a bootargs w dts zostanie nadpisany. Zobacz FAQ - Skąd bootargs dostał się i przeszedł do jądra?

# 8 Aktualizacje programu Uboot

## 8.1 Metoda kopii lustrzanej Flashing sdk

Obraz sdk zawiera już program uboot, bezpośrednio obraz sdk, taki jak: k510_evb_lp3_v1_1_defconfig/images/sysimage-sdcard.img plik

## 8.2 Linux aktualizuj program uboot na karcie sD

Umieść plik u-boot_burn.bin w katalogu tftp, skonfiguruj adres IP urządzenia Port sieciowy i wprowadź katalog /root/sd/p1; Wykonaj polecenie tftp -gr u-boot_burn.bin xxx.xxx.xxx.xxx.xx;

## 8.3 Linux aktualizuje program uboot wewnątrz emmc

Umieść plik u-boot_burn.bin w katalogu tftp, skonfiguruj adres IP portu sieciowego urządzenia i pobierz plik do urządzenia za pośrednictwem tftp -gr u-boot_burn.bin xxx.xxx.xxx.xxx.xxx.xx;

Wykonaj polecenie dd if=u-boot_burn.bin of=/dev/mmcblk0p1, aby zapisać plik na karcie mmc.

# 9 Najczęściej zadawane pytania

## 9.1 Jak skonfigurowana jest częstotliwość DDR?

Odp .: Obecnie EVB może działać tylko 800, a CRB może ustawić 800 lub 1600. CrB board ddr metoda ustawiania częstotliwości patrz uboot board\Canaan\k510_crb_lp3\ddr_param.h file, 800M odpowiada #define DDR_800 1, 1600M odpowiada #define DDR_1600 1.

## 9.2 Skąd bootargs wziął się i przeszedł do jądra?

O: Uzyskane ze zmiennej środowiskowej bootargs uboot, uboot zmodyfikuje parametry bootargs w drzewie urządzeń pamięci zgodnie z wartością zmiennej środowiskowej bootargs podczas uruchamiania jądra. Odpowiedni kod jest następujący:

```c
int fdt_chosen(void *fdt)
{
    int   nodeoffset;
    int   err;
    char  *str; /* used to set string properties */

    err = fdt_check_header(fdt);
    if (err < 0) {
        printf("fdt_chosen: %s\n", fdt_strerror(err));
        return err;
    }

    /* find or create "/chosen" node. */
    nodeoffset = fdt_find_or_add_subnode(fdt, 0, "chosen");
    if (nodeoffset < 0)
        return nodeoffset;

    str = env_get("bootargs");
    if (str) {
        err = fdt_setprop(fdt, nodeoffset, "bootargs", str,
                    strlen(str) + 1);
        if (err < 0) {
            printf("WARNING: could not set bootargs %s.\n",
                    fdt_strerror(err));
            return err;
        }
    }

    return fdt_fixup_stdout(fdt, nodeoffset);
}
```

## 9.3 Czy parametry uruchamiania są niezgodne ze skompilowanym plikiem drzewa urządzeń?

Odp .: uboot dynamicznie uzyskuje zmienne środowiskowe zgodnie z trybem rozruchu i aktualizuje drzewo urządzeń w pamięci zgodnie ze zmiennymi środowiskowymi bootargs podczas uruchamiania jądra. Po zmodyfikowaniu parametrów rozruchu zobacz węzeł /sys/firmware/devicetree/base/chosen.

## 9.4 Gdzie są zapisywane zmienne środowiskowe uboot?

Odpowiedź:

| Tryb uruchamiania | uboot odczyt i zapis lokalizacji | Pliki odpowiadające czasowi kompilacji |
| :-: | :-: | :-: |
| Buty EMMC | Emmc plik uboot-emmc.env dla drugiej partycji | board\canaan\k510\uboot-emmc.env |
| Uruchamianie karty SD | Plik uboot-sd.env pierwszej partycji karty SD | board\canaan\k510\uboot-sd.env |

## 9.5 Jak skonfigurować qos?

O: Rejestry związane z QOS są QOS_CTRL0 QOS_CTRL1 QOS_CTRL2 QOS_CTRL3 QOS_CTRL4. Przykład:
Po ustawieniu qos poprawiła się wydajność demonstracyjna nncase

```c
*(uint32_t *)0x970E00FC = (0x2 << 8) | (0x2 << 12) | (0x2 << 16) | (0x2 << 20) | (0x2 << 24);
*(uint32_t *)0x970E0100 = (0x3 << 4) | 0x3;
*(uint32_t *)0x970E00F4 = (0x5 << 16) | (0x5 << 20);
```

**Zrzeczenie się odpowiedzialności za **tłumaczenie  
Dla wygody klientów Canaan używa tłumacza AI do tłumaczenia tekstu na wiele języków, które mogą zawierać błędy. Nie gwarantujemy dokładności, rzetelności ani terminowości dostarczonych tłumaczeń. Canaan nie ponosi odpowiedzialności za jakiekolwiek straty lub szkody spowodowane poleganiem na dokładności lub wiarygodności przetłumaczonych informacji. W przypadku różnic w treści tłumaczeń w różnych językach, pierwszeństwo ma chińska wersja uproszczona. 

Jeśli chcesz zgłosić błąd lub niedokładność tłumaczenia, skontaktuj się z nami pocztą.