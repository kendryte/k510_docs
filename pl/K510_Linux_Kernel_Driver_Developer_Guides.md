![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 Linux Kernel Driver Podręcznik programisty</font>**

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
Ten dokument jest dokumentem pomocniczym dla K510 SDK, ten dokument mówi głównie o sterownikach związanych z Linuksem, konfiguracji, debugowaniu itp.

**<font face="黑体"  size=5>Obiekty programu Reader</font>**

Główne osoby, których dotyczy ten dokument (ten przewodnik):

- Programiści
- Personel wsparcia technicznego

**<font face="黑体"  size=5>Historia</font>**
 zmian <font face="宋体"  size=2>Historia zmian gromadzi opis każdej aktualizacji dokumentu. Najnowsza wersja dokumentu zawiera aktualizacje dla wszystkich poprzednich wersji. </font>

| Numer wersji   | Zmodyfikowane przez     | Data aktualizacji | Uwagi do poprawek |
|  :-----  |-------   |  ------  |  ------  |
| Wersja 1.0.0 | Grupy oprogramowania systemowego | 2022-03-09 | SDK V1.5 wydany |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Treść</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Wprowadzenie do jądra Linuksa

Wersja Linuksa obecnie używana przez sdk to 4.17.0. Linux, pełna nazwa GNU/Linux, jest darmowym i swobodnie rozpowszechnianym systemem operacyjnym podobnym do UNIX-a z jądrem wydanym po raz pierwszy przez Linusa Bennadicta Torvaza 5 października 1991 roku, jest inspirowany głównie ideami Minix i Unix, i jest wieloużytkownikowym, wielozadaniowym, wielowątkowym i opartym na wielu procesorach systemem operacyjnym opartym na POSIX. Uruchamia główne oprogramowanie narzędzi uniksowych, aplikacje i protokoły sieciowe. Obsługuje zarówno sprzęt 32-bitowy, jak i 64-bitowy. Linux dziedziczy filozofię projektowania zorientowanego na sieć Uniksa i jest stabilnym sieciowym systemem operacyjnym dla wielu użytkowników. Linux ma setki różnych dystrybucji, takich jak oparty na społeczności debian, archlinux i komercyjnie opracowany Red Hat Enterprise Linux, SUSE, Oracle Linux itp.

Aby uzyskać więcej informacji na temat jądra Linuksa, odwiedź:<https://docs.kernel.org/>

## 1.1 Jak go zdobyć

Pobierz i skompiluj SDK, SDK pobierze i skompiluje kod Linuksa podczas kompilacji.

Aby uzyskać więcej informacji na temat pobierania i kompilowania zestawu SDK, zobacz[ K510_SDK_Build_and_Burn_Guide](./K510_SDK_Build_and_Burn_Guide.md). 

## 1.2 Wymagania środowiska programistycznego

- System operacyjny

| numerowanie | Zasoby dotyczące oprogramowania | Ilustrują        |
| ---- | -------- | ----------- |
| 1    | Ubuntu   | 18.04/20.04 |

- Wymagania dotyczące środowiska oprogramowania przedstawiono w poniższej tabeli:

| numerowanie | Zasoby dotyczące oprogramowania | Ilustrują |
| ---- | -------- | ---- |
| 1    | K510 SDK | wersja 1.5 |

# 2 Domyślny plik konfiguracyjny jądra i dts

Domyślna ścieżka pliku konfiguracyjnego jądra:

arch/riscv/configs/k510_defconfig

Jądro obsługuje dwie płytki rozwojowe, K510 CRB i EVB, a odpowiednie pliki dts są następujące:

arch/riscv/boot/dts/canaan/k510_crb_lp3_v0_1.dts

arch/riscv/boot/dts/canaan/k510_evb_lp3_v1_1.dts

W katalogu arch/riscv/boot/dts/canaan/k510_common znajduje się publiczna definicja dts na poziomie soc.

# 3 Debugowanie

## 3.1 Debugowanie jądra Linuksa za pomocą JTAG

1. Zainstaluj Andesight v3.2.1
2. Przejdź do katalogu ice w katalogu instalacyjnym andesight i uruchom ICEMAN

    ```shell
    #ICEman -Z v5 --smp
    ```

3. Używając debugowania gdb, oto przykład kodu jądra /dev/mem/char/mem.c

    ```shell
    riscv64-linux-gdb --eval-command="target remote 192.168.200.100:1111"
    (gdb) symbol-file vmlinux
    (gdb) hbreak mmap_mem
    ```

4. Aplikacja otwiera /dev/mem, wywołuje mmap i wchodzi w punkt przerwania

# 4 Opis kierowcy

## 4.1 UART

Opcje konfiguracji:

```shell
CONFIG_SERIAL_8250_DW
```

Pliki sterownika:

```shell
/tty/serial/8250
```

Drzewo urządzeń:

```text
serial@96000000 {
    status = "okay";
    #address-cells = <0x2>;
    #size-cells = <0x2>;
    compatible = "snps,dw-apb-uart";
    reg = <0x0 0x96000000 0x0 0x100>;
    interrupt-parent = <0x6>;
    interrupts = <0x1 0x4>;
    resets = <0x4 0x58 0x1 0x1f 0x0>;
    reset-names = "uart0_rst";
    power-domains = <0x5 0x6>;
    clock-frequency = <0x17d7840>;
    reg-shift = <0x2>;
    reg-io-width = <0x4>;
    no-loopback-test = <0x1>;
    pinctrl-names = "default";
    pinctrl-0 = <0x1f>;
};
```

API: Węzeł pliku urządzenia:

```shell
/dev/ttyS0
/dev/ttyS1/2/3    #目前dts中disable
```

Interfejs programowania: standardowy sterownik portu szeregowego, patrz strona podręcznika systemowego Systemu Linux

```shell
man termios
```

## 4.2 ETH

Opcje konfiguracji:

```shell
CONFIG_NET_CADENCE
```

Pliki sterownika:

```shell
drivers/net/ethernet/cadence
```

Drzewo urządzeń:

```text
emac@93030000 {
    status = "okay";
    compatible = "cdns,k510-gem";
    reg = <0x0 0x93030000 0x0 0x10000>;
    interrupt-parent = <0x6>;
    interrupts = <0x36 0x4 0x37 0x4 0x38 0x4>;
    clocks = <0x1b 0x1b 0x1b 0x1b 0x1b 0x1b>;
    clock-names = "hclk", "pclk", "ether_clk", "tx_clk", "rx_clk", "tsu_clk";
    clock-config = <0x97001104>;
    resets = <0x4 0xe4 0x1 0x1f 0x0>;
    reset-names = "emac_rst";
    power-domains = <0x5 0x5>;
    phy-mode = "rgmii";
    pinctrl-names = "default";
    pinctrl-0 = <0x1c>;
};
```

Urządzenie:`eth0`
Opis API: Standardowy sterownik portu Ethernet, patrz programowanie gniazd tcp / ip; 

Konfiguracja IP portu Ethernet:

```shell
ifconfig eth0 xxx.xxx.xxx.xxx
```

## 4.3 EMMC

Opcje konfiguracji:

```shell
CONFIG_MMC_SDHCI_CADENCE
```

Pliki sterownika:

```shell
drivers/mmc/host/sdhci-cadence.c
```

Drzewo urządzeń:

```text
sdio@93000000 {
    status = "okay";
    compatible = "socionext,uniphier-sd4hc", "cdns,sd4hc";
    reg = <0x0 0x93000000 0x0 0x2000>;
    interrupt-parent = <0x6>;
    interrupts = <0x30 0x4>;
    clocks = <0x14>;
    max-frequency = <0x2faf080>;
    resets = <0x4 0xc8 0x1 0x1f 0x0>;
    reset-names = "sdio0_rst";
    power-domains = <0x5 0x5>;
    bus-width = <0x8>;
    pinctrl-names = "default";
    pinctrl-0 = <0x15>;
};
```

Urządzenia i partycje:

```shell
[root@k510-test ~ ]$ ls -l /dev/ | grep mmcblk0
brw------- 179,  0 Jan 1 1970 mmcblk0      # emmc
brw------- 179,  8 Jan 1 1970 mmcblk0boot0
brw------- 179, 16 Jan 1 1970 mmcblk0boot1
brw------- 179,  1 Jan 1 1970 mmcblk0p1    # emmc第一个分区(boot)
brw------- 179,  2 Jan 1 1970 mmcblk0p2    # emmc第二个分区(kenrel,env,vfat)
brw------- 179,  3 Jan 1 1970 mmcblk0p3    # emmmc第三个分区(rootfs文件系统，ext2)
```

Interfejs API sterownika: Standardowy sterownik, jako zwykły plik do odczytu i zapisu.

## 4.4 KARTA SD

Opcje konfiguracji:

```shell
CONFIG_MMC_SDHCI_CADENCE
```

Pliki sterownika:

```shell
drivers/mmc/host/sdhci-cadence.c
```

Drzewo urządzeń:

```text
sdio@93020000 {
    status = "okay";
    compatible = "socionext,uniphier-sd4hc", "cdns,sd4hc";
    reg = <0x0 0x93020000 0x0 0x2000>;
    interrupt-parent = <0x6>;
    interrupts = <0x32 0x4>;
    clocks = <0x19>;
    max-frequency = <0x2faf080>;
    resets = <0x4 0xd0 0x1 0x1f 0x0>;
    reset-names = "sdio2_rst";
    power-domains = <0x5 0x5>;
    bus-width = <0x4>;
    cap-sd-highspeed;
    cdns,phy-input-delay-legacy = <0xf>;
    cdns,phy-input-delay-sd-highspeed = <0xf>;
    pinctrl-names = "default";
    pinctrl-0 = <0x1a>;
};
```

Sprzęt:

```shell
[root@k510-test ~ ]$ ls -l /dev/ | grep mmcblk1
brw------- 179, 24 mmcblk1      # sd卡设备
brw------- 179, 25 mmcblk1p1    # sd卡第一个分区(boot,kenrel,env,vfat)
brw------- 179, 26 mmcblk1p2    # sd卡第二个分区(rootfs文件系统，ext2)
brw------- 179, 27 mmcblk1p3    # sd卡第三个分区(用户分区)
```

Interfejs API sterownika: Standardowy sterownik, jako zwykły plik do odczytu i zapisu.

## 4.5 WDT

Opcje konfiguracji:

```shell
CONFIG_DW_WATCHDOG
```

Pliki sterownika:

```shell
drivers/watchdog/dw_wdt.c
```

Drzewo urządzeń:

```text
wdt@97010000 {
    status = "okay";
    compatible = "snps,dw-wdt";
    reg = <0x0 0x97010000 0x0 0x100>;
    clocks = <0x44>;
    resets = <0x4 0x40 0x2 0x0 0x3>;
    reset-names = "wdt0_rst";
};

wdt@97020000 {
    status = "okay";
    compatible = "snps,dw-wdt";
    reg = <0x0 0x97020000 0x0 0x100>;
    clocks = <0x45>;
    resets = <0x4 0x40 0x2 0x0 0x4>;
    reset-names = "wdt1_rst";
};

wdt@97030000 {
    status = "okay";
    compatible = "snps,dw-wdt";
    reg = <0x0 0x97030000 0x0 0x100>;
    clocks = <0x46>;
    resets = <0x4 0x40 0x2 0x0 0x5>;
    reset-names = "wdt2_rst";
};
```

API: Węzeł pliku urządzenia:

```shell
/dev/watchdog
/dev/watchdog0/1/2
```

Interfejs programowania: linux file IO(open, close, ioctl), zobacz stronę podręcznika Linuksa
Kod źródłowy jądra zawiera dokumentację:`Documentation/watchdog/watchdog-api.txt`

## 4.6 PWM

Opcje konfiguracji:

```shell
CONFIG_PWM_GPIO
CONFIG_PWM_CANAAN
```

Pliki sterownika:

```shell
drivers/pwm/pwm-canaan.c
drivers/pwm/pwm-gpio.c
```

Drzewo urządzeń:

```text
pwm0@970f0000 {
    status = "okay";
    compatible = "canaan,k510-pwm";
    reg = <0x0 0x970f0000 0x0 0x40>;
    clocks = <0x55>;
    clock-names = "pwm";
    resets = <0x4 0x40 0x2 0x0 0xb>;
    reset-names = "pwm_rst";
    pinctrl-names = "default";
    pinctrl-0 = <0x56>;
};

pwm1@970f0000 {
    status = "okay";
    compatible = "canaan,k510-pwm";
    reg = <0x0 0x970f0040 0x0 0x40>;
    clocks = <0x55>;
    clock-names = "pwm";
    resets = <0x4 0x40 0x2 0x0 0xb>;
    reset-names = "pwm_rst";
    pinctrl-names = "default";
    pinctrl-0 = <0x57>;
};
```

API: sterownik pwm w stanie użytkownika jest dostępny poprzez sysfs, `/sys/class/pwm/`

Interfejs programowania: IO pliku Linux (otwieranie, odczytywanie, zapisywanie), patrz strona podręcznika systemowego systemu Linux

Kod źródłowy jądra zawiera dokumentację:`Documentation/pwm.txt`

## 4.7 I2C

Opcje konfiguracji:

```shell
CONFIG_I2C_DESIGNWARE_CORE
CONFIG_I2C0_TEST_DRIVER
```

Pliki sterownika:

```shell
drivers/misc/canaan/i2c/test-i2c0.c
drivers/i2c/busses/i2c-designware-platdrv.c
```

Drzewo urządzeń:

```text
i2c@97060000 {
    status = "disable";
    compatible = "snps,designware-i2c";
    reg = <0x0 0x97060000 0x0 0x100>;
    interrupt-parent = <0x6>;
    interrupts = <0xc 0x4>;
    clocks = <0x48>;
    clock-frequency = <0x186a0>;
    resets = <0x4 0x40 0x2 0x0 0x0>;
    reset-names = "i2c0_rst";
};
```

API: Sterownik I2C jest sterownikiem magistrali i jest zaimplementowany przy użyciu struktury podsystemu I2C jądra Linuksa. Dostęp do stanu użytkownika można uzyskać za pośrednictwem plików sysfs lub można użyć programów narzędziowych stanu użytkownika, takich jak i2c-tools.

```shell
/sys/bus/i2c/devices/
```

Interfejs programowania: IO pliku Linux (otwórz, odczyt, zapis), zobacz stronę podręcznika systemu Linux
Kod źródłowy jądra zawiera dokumentację:`Documentation/i2c/dev-interface`

## 4.8 USB OTG

Opcje konfiguracji:

```shell
USB_CANAAN_OTG20
```

Stacja dysków:

```shell
drivers/usb/canaan_otg20/core_drv_mod
```

Drzewo urządzeń:

```text
usb@93060000 {
    status = "okay";
    compatible = "Cadence,usb-dev1.00";
    reg = <0x0 0x93060000 0x0 0x10000>;
    interrupt-parent = <0x6>;
    interrupts = <0x2d 0x4 0x2e 0x4>;
    resets = <0x4 0x18c 0x1 0x1f 0x0>;
    reset-names = "usb_rst";
    power-domains = <0x5 0xc>;
    otg_power_supply-gpios = <0x13 0x10 0x0>;
};
```

USB jako host, może być podłączony do dysku U, jako urządzenie, może być używany jako dysk U.

## 4.9 CLK

Opcje konfiguracji:

```shell
CONFIG_COMMON_CLK_CAN_K510
```

Pliki sterownika:

```shell
drivers/reset/canaan/reset-k510.c
```

Drzewo urządzeń:

```shell
arch/riscv/boot/dts/canaan/k510_common/clock_provider.dtsi
arch/riscv/boot/dts/canaan/k510_common/clock_consumer.dtsi
```

- `clock_provider.dtsi`Zdefiniuj wszystkie węzły zegara w
- `clock_consumer.dtsi`Odwołania w każdym węźle dts sterownika

## 4.10 MOC

Opcje konfiguracji:

```shell
CONFIG_CANAAN_PM_DOMAIN
```

Pliki sterownika:

```shell
drivers/soc/canaan/k510_pm_domains.c
```

Drzewo urządzeń:

```shell
arch/riscv/boot/dts/canaan/k510_common/power_provider.dtsi
arch/riscv/boot/dts/canaan/k510_common/power_consumer.dtsi
```

```text
sysctl_power@97003000 {
    status = "okay";
    compatible = "canaan, k510-sysctl-power";
    reg = <0x0 0x97003000 0x0 0x1000>;
    #power-domain-cells = <0x1>;
    phandle = <0x5>;
};
```

- `power_provider.dtsi` Zdefiniowany jest węzeł dts dostawcy
- `include/dt-bindings/soc/canaan,k510_pm_domains.h` Wszystkie domeny mocy są zdefiniowane w
- `power_consumer.dtsi`<a0> jest przywoływany w odpowiednich węzłach dts sterowników

## 4.11 RESET

Opcje konfiguracji:

```shell
CONFIG_COMMON_RESET_K510
```

Pliki sterownika:

```shell
drivers/reset/canaan/reset-k510.c
```

Drzewo urządzeń:

```shell
arch/riscv/boot/dts/canaan/k510_common/reset_provider.dtsi
arch/riscv/boot/dts/canaan/k510_common/reset_consumer.dtsi
```

```text
sysctl_reset@97002000 {
    status = "okay";
    compatible = "canaan,k510-sysctl-reset";
    reg = <0x0 0x97002000 0x0 0x1000>;
    #reset-cells = <0x4>;
    phandle = <0x4>;
};
```

- `reset_provider.dtsi` Zdefiniowany jest węzeł dts dostawcy
- `include/ dt-bindings/reset/canaan-k510-reset.h` Wszystkie sygnały resetowania są zdefiniowane w
- `reset_consumer.dtsi`<a0> jest przywoływany w odpowiednich węzłach dts sterowników

## 4.12 PINCTL

Opcje konfiguracji:

```shell
CONFIG_PINCTRL_K510
```

Pliki sterownika:

```shell
drivers/pinctrl/canaan
```

Powiązane drzewo urządzeń:

```shell
arch/riscv/boot/dts/canaan/k510_common/iomux_provider.dtsi
arch/riscv/boot/dts/canaan/k510_common/iomux_consumer.dtsi
```

```text
iomux@97040000 {
    status = "okay";
    compatible = "pinctrl-k510";
    reg = <0x0 0x97040000 0x0 0x1000>;
    resets = <0x4 0x40 0x2 0x0 0x9>;
    reset-names = "iomux_rst";
    #pinctrl-cells = <0x1>;
    pinctrl-k510,register-width = <0x20>;
    pinctrl-k510,function-mask = <0xffffffff>;

    iomux_emac_pins {
        pinctrl-k510,pins = <0x23 0x23012d 0x24 0x24012e 0x22 0x22012c 0x26 0x260132 0x20 0x20012a 0x2e 0x2e013a 0x2d 0x2d0139 0x2a 0x2a0136 0x29 0x290135 0x1d 0x1d0126>;
    };

    iomux_mmc0_pins {
        pinctrl-k510,pins = <0x7 0x70107 0x8 0x80108 0x9 0x90109 0xa 0xa010a 0xb 0xb010b 0xc 0xc010c 0xd 0xd010d 0xe 0xe010e 0xf 0xf010f 0x10 0x100110>;
        phandle = <0x15>;
    };

    iomux_mmc2_pins {
        pinctrl-k510,pins = <0x17 0x170117 0x18 0x180118 0x19 0x190119 0x1a 0x1a011a 0x1b 0x1b011b 0x1c 0x1c011c>;
        phandle = <0x1a>;
    };

    iomux_uart0_pins {
        pinctrl-k510,pins = <0x70 0x54 0x71 0x5a>;
        phandle = <0x1f>;
    };

    iomux_uart1_pins {
        pinctrl-k510,pins = <0x72 0x64 0x73 0x6a>;
        phandle = <0x20>;
    };

    iomux_emac_rgmii_pins {
        pinctrl-k510,pins = <0x23 0x23012d 0x24 0x24012e 0x1d 0x1d0123 0x26 0x260131 0x2e 0x2e013a 0x2d 0x2d0139 0x2c 0x2c0138 0x2b 0x2b0137 0x1e 0x1e0128 0x25 0x25012f 0x2a 0x2a0136 0x29 0x290135 0x28 0x280134 0x27 0x270133>;
        phandle = <0x1c>;
    };

    iomux_i2s_pins {
        pinctrl-k510,pins = <0x64 0xab 0x65 0xad 0x63 0xa3 0x62 0x93>;
        phandle = <0x22>;
    };

    iomux_i2c1_pins {
        pinctrl-k510,pins = <0x78 0x44 0x79 0x45>;
        phandle = <0x4a>;
    };

    iomux_i2c2_pins {
        pinctrl-k510,pins = <0x67 0x46 0x66 0x47>;
        phandle = <0x4d>;
    };

    iomux_i2c3_pins {
        pinctrl-k510,pins = <0x74 0x49 0x75 0x48>;
        phandle = <0x4f>;
    };

    iomux_i2c4_pins {
        pinctrl-k510,pins = <0x30 0x4b 0x2f 0x4a>;
        phandle = <0x52>;
    };

    iomux_dvp_pins {
        pinctrl-k510,pins = <0x33 0x33013f 0x34 0x340140 0x35 0x350141 0x36 0x360142 0x37 0x370143 0x38 0x380144 0x39 0x390145 0x3a 0x3a0146 0x3b 0x3b0147 0x3c 0x3c0148 0x3d 0x3d0149 0x3e 0x3e014a 0x3f 0x3f014b 0x40 0x40014c 0x42 0x42014e>;
        phandle = <0x6c>;
    };

    iomux_gpio_pins {
        pinctrl-k510,pins = <0x20 0x20 0x22 0x1f 0x45 0xc 0x46 0xd 0x47 0xe 0x4b 0xf 0x4c 0x10 0x4d 0x11 0x4e 0x1d 0x4f 0x1e 0x50 0x14 0x51 0x15 0x53 0x16 0x54 0x17 0x55 0x18 0x61 0x19 0x7b 0x1a>;
        phandle = <0x47>;
    };

    iomux_pwm0_pins {
        pinctrl-k510,pins = <0x7e 0xb3>;
        phandle = <0x56>;
    };

    iomux_pwm1_pins {
        pinctrl-k510,pins = <0x7f 0xb7>;
        phandle = <0x57>;
    };

    iomux_spi0_pins {
        pinctrl-k510,pins = <0x56 0x560162 0x57 0x570163 0x58 0x580164 0x59 0x590165 0x5a 0x5a0166 0x5b 0x5b0167>;
        phandle = <0xc>;
    };

    iomux_spi1_pins {
        pinctrl-k510,pins = <0x68 0x8 0x69 0x9 0x6a 0x0 0x6b 0x1>;
        phandle = <0xf>;
    };

    iomux_spi2_pins {
        pinctrl-k510,pins = <0x7a 0x2a>;
        phandle = <0x12>;
    };

    iomux_mmc1_pins {
        pinctrl-k510,pins = <0x11 0x110111 0x12 0x120112 0x13 0x130113 0x14 0x140114 0x15 0x150115 0x16 0x160116>;
        phandle = <0x17>;
    };
};
```

`iomux_provider.dtsi` Zdefiniowany jest węzeł dts dostawcy
`include/include/dt-bindings/pinctrl/k510.h`Wszystkie numery funkcji IO są zdefiniowane w
`iomux_consumer.dtsi`<a0> jest przywoływany w odpowiednich węzłach dts sterowników

## 4,13 H264

Opcje konfiguracji:

```shell
CONFIG_ ALLEGRO_CODEC_DRIVER
```

Pliki sterownika:

```shell
drivers/media/platform/canaan/al5r
```

Powiązane drzewo urządzeń:

```text
h264@92740000 {
    status = "okay";
    compatible = "al,al5r";
    reg = <0x0 0x92740000 0x0 0x10000>;
    interrupt-parent = <0x6>;
    interrupts = <0x3f 0x4>;
    clocks = <0x7f>;
    resets = <0x4 0x184 0x1 0x1f 0x0>;
    reset-names = "h264_rst";
    power-domains = <0x5 0xb>;
};
```

API: Węzeł pliku urządzenia: `/dev/h264-codec`

Interfejs programowania: IO pliku Linux (open, close, ioctl), patrz strona podręcznika systemu Linux

Obsługiwane polecenia IOCTL:

```c
#define AL_CMD_IP_WRITE_REG    _IOWR('q', 10, struct al5_reg)
#define AL_CMD_IP_READ_REG     _IOWR('q', 11, struct al5_reg)
#define AL_CMD_IP_WAIT_IRQ     _IOWR('q', 12, int)
#define AL_CMD_IP_IRQ_CNT      _IOWR('q', 13, int)
#define AL_CMD_IP_CLR_IRQ      _IOWR('q', 14, int)
```

Przykładowy kod:`package/h264_demo/src`

## 4.14 Procesor danych

Opcje konfiguracji:

```shell
CONFIG_ K510_DSP_DRIVER
```

Pliki sterownika:

```shell
drivers/misc/canaan/k510-dsp
```

Powiązane drzewo urządzeń:

```text
dsp@99800000 {
    status = "okay";
    compatible = "k510-dsp";
    reg = <0x0 0x99800000 0x0 0x80000>;
    resets = <0x4 0x14 0x0 0x1e 0x0>;
    reset-names = "dsp_rst";
    power-domains = <0x5 0x1>;
    sysctl-phy-addr = <0x97000000>;
};
```

API: Węzeł pliku urządzenia: `/dev/k510-dsp`

Interfejs programowania: IO pliku Linux (open, close, ioctl), patrz strona podręcznika systemu Linux

Obsługiwane polecenia ioctl:

```c
#define DSP_CMD_BOOT       _IOWR('q', 1, unsigned long)
```

Przykładowy kod:

```shell
package/dsp_app/src/
package/dsp_app_evb_lp3_v1_1/src/
```

## 4,15 GNNE

Opcje konfiguracji:

```shell
CONFIG_ K510_GNNE_DRIVER
```

Pliki sterownika:

```shell
drivers/misc/canaan/gnne
```

Powiązane drzewo urządzeń:

```text
gnne@94000000 {
    status = "okay";
    compatible = "k510-gnne";
    reg = <0x0 0x94180000 0x0 0x80000>;
    interrupt-parent = <0x6>;
    interrupts = <0x27 0x4>;
    resets = <0x4 0x2c 0x1 0x1f 0x0>;
    reset-names = "gnne_rst";
    power-domains = <0x5 0x3>;
};
```

API: Węzeł pliku urządzenia: /dev/k510-gnne
Interfejs programowania: IO pliku Linux (open, close, ioctl), patrz strona podręcznika systemu Linux
Obsługiwane polecenia ioctl:

```c
#define GNNE_ENABLE                   _IOWR('g', 1, unsigned long)
#define GNNE_RESET                    _IOWR('g', 2, unsigned long)
#define GNNE_DISABLE                  _IOWR('g', 3, unsigned long)
#define GNNE_SET_PC                   _IOWR('g', 4, unsigned long)
#define GNNE_SET_MEM_BASE             _IOWR('g', 5, unsigned long)
#define GNNE_GET_STATUS               _IOWR('g', 10, unsigned long)
#define GNNE_SET_PC_ENABLE            _IOWR('g', 11, unsigned long)
#define GNNE_SET_MEM0                 _IOWR('g', 12, unsigned long)
#define GNNE_SET_MEM1                 _IOWR('g', 13, unsigned long)
#define GNNE_SET_MEM2                 _IOWR('g', 14, unsigned long)
#define GNNE_SET_MEM3                 _IOWR('g', 15, unsigned long)
#define GNNE_GET_PC                   _IOWR('g', 16, unsigned long)
#define GNNE_GET_CTRL                 _IOWR('g', 17, unsigned long)
#define GNNE_GET_DSP_INTR_MASK        _IOWR('g', 18, unsigned long)
#define GNNE_GET_MEM0                 _IOWR('g', 19, unsigned long)
#define GNNE_GET_MEM1                 _IOWR('g', 20, unsigned long)
#define GNNE_GET_MEM2                 _IOWR('g', 21, unsigned long)
#define GNNE_GET_MEM3                 _IOWR('g', 22, unsigned long)
#define GNNE_GET_LOAD_STROE_PC_ADDR   _IOWR('g', 23, unsigned long)
#define GNNE_GET_TCU_MFU_PC_ADDR      _IOWR('g', 24, unsigned long)
#define GNNE_GET_CCR_STATUS0          _IOWR('g', 25, unsigned long)
#define GNNE_GET_CCR_STATUS1          _IOWR('g', 26, unsigned long)
#define GNNE_GET_CCR_STATUS2          _IOWR('g', 27, unsigned long)
#define GNNE_GET_CCR_STATUS3          _IOWR('g', 28, unsigned long)
```

Przykładowy kod:

```shell
package/nncase_demo/src/mobilenetv2
```

## 4.16 TWOD

Opcje konfiguracji:

```shell
CONFIG_K510_2D_DRIVER
```

Pliki sterownika:

```shell
drivers/media/platform/canaan/kendryte_2d.c
```

Powiązane drzewo urządzeń:

```text
twod@92720000 {
    status = "okay";
    compatible = "k510, kendrty_2d";
    reg = <0x0 0x92720000 0x0 0x10000>;
    interrupt-parent = <0x6>;
    interrupts = <0x44 0x0>;
    clocks = <0x6f 0x70>;
    clock-names = "twod_apb", "twod_axi";
};
```

API: Węzeł pliku urządzenia: /dev/kendryte_2d
Interfejs programowania: IO pliku Linux (open, close, ioctl), patrz strona podręcznika systemu Linux
Obsługiwane polecenia ioctl:

```c
#define KENDRTY_2DROTATION_90     _IOWR('k', 0, unsigned long)
#define KENDRTY_2DROTATION_270    _IOWR('k', 1, unsigned long)

#define KENDRTY_2DROTATION_INPUT_ADDR     _IOWR('k', 2, unsigned long)
#define KENDRTY_2DROTATION_OUTPUT_ADDR    _IOWR('k', 3, unsigned long)
#define KENDRTY_2DROTATION_GET_REG_VAL    _IOWR('k', 4, unsigned long)
```

## 4.17 AES i SHA

Opcje konfiguracji:

```shell
CONFIG_CRYPTO_DEV_KENDRYTE_CRYP
```

Pliki sterownika:

```shell
drivers/crypto/kendryte/kendryte-aes.c
drivers/crypto/kendryte/kendryte-aes.h
drivers/crypto/kendryte/kendryte-hash.c
drivers/crypto/kendryte/kendryte-hash.h
```

Powiązane drzewo urządzeń:

```text
aes@91000000 {
    status = "okay";
    compatible = "canaan,k510-aes";
    reg = <0x0 0x91000000 0x0 0x10000>;
    clocks = <0x7>;
    resets = <0x4 0x9c 0x1 0x1f 0x0>;
    reset-names = "aes_rst";
    power-domains = <0x5 0x4>;
    dmas = <0x8 0x1 0xfff 0x0 0x21 0x8 0x1 0xfff 0x0 0x22>;
    dma-names = "tx", "rx";
};

sha@91010000 {
    status = "okay";
    compatible = "canaan,k510-sha";
    reg = <0x0 0x91010000 0x0 0x10000>;
    clocks = <0x9>;
    resets = <0x4 0x94 0x1 0x1f 0x0>;
    reset-names = "sha_rst";
    power-domains = <0x5 0x4>;
    dmas = <0x8 0x1 0xfff 0x0 0x20>;
    dma-names = "tx";
};
```

API: Pliki węzłów urządzenia:`/sys/bus/platform/devices/91000000.aes`
`/sys/bus/platform/devices/91010000.sha`

Interfejs programowania: Programy stanu użytkownika używają gniazd do uzyskania dostępu do interfejsu API sterownika jądra, w którym znajduje się dokumentacja referencyjna`/Documentation/crypto/userspace-if.rst`

Przykładowy kod:

```shell
package/crypto_demo/src
```

## 4.18 Monitorowanie temperatury - termiczne

Opcje konfiguracji:

```shell
CONFIG_THERMAL
CONFIG_CANAAN_THERMAL
```

Pliki sterownika:

```shell
drivers/thermal/canaan_thermal.c
```

Powiązane drzewo urządzeń:

```text
tsensor@970e0300 {
    status = "okay";
    compatible = "canaan,k510-tsensor";
    reg = <0x0 0x970e0300 0x0 0x100>;
    interrupt-parent = <0x6>;
    interrupts = <0x1c 0x4>;
    clocks = <0x54>;
};
```

Sposób użycia:

```shell
cd /sys/class/thermal/thermal_zone0/
echo enabled > mode
cat temp
```

## 4.19 Obrót 2D - twod

Opcje konfiguracji:

```shell
CONFIG_KENDRYTE_TWOD_SUPPORT
CONFIG_KENDRYTE_TWOD
```

Pliki sterownika:

```shell
drivers/video/canaan/twod/kendryte_td.c
drivers/video/canaan/twod/kendryte_td_reg.c
drivers/video/canaan/twod/kendryte_td.h
drivers/video/canaan/twod/kendryte_td_table.h
```

Powiązane drzewo urządzeń:

```text
twod@92720000 {
    status = "okay";
    compatible = "k510, kendrty_2d";
    reg = <0x0 0x92720000 0x0 0x10000>;
    interrupt-parent = <0x6>;
    interrupts = <0x44 0x0>;
    clocks = <0x6f 0x70>;
    clock-names = "twod_apb", "twod_axi";
};
```

# 5 Środki ostrożności

nie

**Zrzeczenie się odpowiedzialności za **tłumaczenie  
Dla wygody klientów Canaan używa tłumacza AI do tłumaczenia tekstu na wiele języków, które mogą zawierać błędy. Nie gwarantujemy dokładności, rzetelności ani terminowości dostarczonych tłumaczeń. Canaan nie ponosi odpowiedzialności za jakiekolwiek straty lub szkody spowodowane poleganiem na dokładności lub wiarygodności przetłumaczonych informacji. W przypadku różnic w treści tłumaczeń w różnych językach, pierwszeństwo ma chińska wersja uproszczona. 

Jeśli chcesz zgłosić błąd lub niedokładność tłumaczenia, skontaktuj się z nami pocztą.