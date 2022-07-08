![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 SDK — przewodnik kompilacji i nagrywania</font>**

<font face="黑体"  size=3>Wersja dokumentu: V1.0.0</font>

<font face="黑体"  size=3>Opublikowano: 2022-03-07</font>

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

| Numer wersji   | Zmodyfikowane przez     | Data aktualizacji | Uwagi do poprawek |
|  :-----  |-------   |  ------  |  ------  |
| Wersja 1.0.0 | Dział Produktów AI | 2022-03-07 |          |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Treść</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Wstęp

W tym dokumencie opisano zawartość sekcji budowy środowiska programistycznego, taką jak pobieranie, kompilowanie i nagrywanie zestawu SDK K510.

# 2 k510 sdk

## 2.1 k510 sdk do pobrania

k510 SDK Adres projektu: <https://github.com/kendryte/k510_buildroot>

Pobierz k510 SDK:

```shell
git clone https://github.com/kendryte/k510_buildroot.git
```

## 2.2 Wprowadzenie do pakietu sdk k510

K510 SDK to wbudowane środowisko programistyczne Linux oparte na buildroot jako podstawowej strukturze, oparte na pakiecie kodu źródłowego K510 linux (linux wersja 4.17.0), u-boot (u-boot wersja 2020.01), riscv-pk-k510 (BBL), struktura katalogów K510 SDK jest pokazana na poniższym rysunku.

![](../zh/images/sdk_build/image-buildroot.png)

 Pliki K510 SDK są opisane w następujący sposób:

| **plik**        | **Opis treści**                                                 |
| --------------- | ------------------------------------------------------------ |
| deska           | Folder, który jest K510 różne pliki konfiguracyjne i skrypty, takie jak plik konfiguracyjny do generowania obrazów (genimage-xxx.cfg), skrypty post-image buildroot, domyślne zmienne środowiskowe U-Boot itp. |
| Config.in       | Wskazuje pakiet, który wymaga kompilacji buildroot. |
| konfiguracje         | Folder, gdzie jest domyślnym plikiem konfiguracyjnym kompilacji płyty. Obecnie zapisuje domyślne pliki konfiguracyjne kompilacji dla płyt K510 CRB-V0.1, K510 CRB-V1.2 i K510 EVB:<br /> -`k510_crb_lp3_v1_2_defconfig`<br />-`k510_crb_lp3_v0_1_defconfig`<br />- `k510_evb_lp3_v1_1_defconfig` |
| external.desc   | Plik konfiguracyjny mechanizmu zewnętrznego Buildroot. |
| external.mk     | |
| Makefile        | Główny plik Makefile k510 SDK. |
| pakiet         | Foldery, które są głównie aplikacjami K510, Config.in zawartość pliku określi, które aplikacje są kompilowane w tym katalogu. |
| Poprawki         | Folder, w którym znajduje się plik poprawki buildroot, Makefile rozpakuje kod źródłowy, gdy plik poprawki w tym katalogu do odpowiedniego katalogu kodu źródłowego. |
| pkg-pobierz    | Folder, który jest skompresowanym pakietem folderu dl. |
| README.md       | Instrukcje związane z zestawem SDK. |
| release_note.md | |
| toolchain       | , gdzie znajduje się łańcuch narzędzi kompilacji krzyżowej. |
| Dl              | Folder, jest pakietem dl extract w pkg-download, jeśli są inne pakiety dodane zostaną również pobrane do tego katalogu. |

## Wersja 2.3 k510 sdk

Podczas nagrywania obrazu wygenerowanego przez k510 sdk na tablicy drukowane są informacje o wersji, jak pokazano na poniższym rysunku:

```text
#############SDK VERSION############################################
MX2_DEV_0106-02e87077-20220428-153936CST-xxxxx-server
####################################################################
```

Po zakończeniu uruchamiania wprowadź następujące informacje w terminalu powłoki, aby wyświetlić informacje o wersji zestawu SDK:

```shell
cat /etc/version/release_version
#############SDK VERSION############################################
MX2_REL_0106-02e87077-20220428-153936CST-xxxx-server
####################################################################
```

**Uwaga: Powyższe informacje mogą się różnić w zależności od wersji k510 sdk**.

# 3 środowisko kompilacji docker

Po pobraniu k510 sdk wykonaj następujące polecenie w katalogu nadrzędnym sdk, aby uruchomić okno dokowane:

```shell
sh k510_buildroot/tools/docker/run_k510_docker.sh
```

Kolejne operacje kompilacji są domyślnie wykonywane w oknie Docker.
Jeśli chcesz skonfigurować środowisko lokalne, zapoznaj się z sekcją[Konfiguracja środowiska lokalnego](#env_set)

# 4 Kompiluj

## 4.1 Przygotowanie kompilacji

### 4.1.1 Pobierz pakiet kodu źródłowego (opcjonalnie, może przyspieszyć kompilację)

Wykonaj następujące polecenie, aby pobrać pakiet źródłowy:

```shell
make dl
```

## 4.2 Kompilacja

K510_buildroot/config zawiera pliki konfiguracyjne kompilacji dla trzech płyt programistycznych, a mianowicie`k510_crb_lp3_v0_1_defconfig` , `k510_crb_lp3_v1_2_defconfig`i `k510_evb_lp3_v1_1_defconfig`, ten dokument jest zilustrowany przez wybranie k510_crb_lp3_v1_2_defconfig jako celu** kompilacji**.

W środowisku docker k510 wprowadź następujące polecenie, aby rozpocząć kompilację:

```shell
make CONF=k510_crb_lp3_v1_2_defconfig
```

![](../zh/images/sdk_build/image-make.png)

Poniższy komunikat wskazuje, że kompilacja zakończyła się pomyślnie.

![](../zh/images/sdk_build/image-uboot_r.png)

Po zakończeniu kompilacji folder jest generowany`k510_crb_lp3_v1_2_defconfig`.

![obraz-20220311121912711](../zh/images/sdk_build/image-makeout.png)

Każdy z tych dokumentów jest opisany w następujący sposób:

| **plik**    | **Opis treści**                                                 |
| ----------- | ------------------------------------------------------------ |
| Makefile    | Skompiluj obraz, aby użyć Makefile.                                     |
| budować       | Katalog kompilacji dla wszystkich pakietów źródłowych. Na przykład, jądro Linuksa, u-boot, BBL, busybox itp., Kod źródłowy zostanie wyodrębniony do katalogu kompilacji i skompilowany. |
| gospodarz        | Wszystkie ścieżki instalacji pakietów hosta, toolchain zostaną również skopiowane do tego katalogu w celu zbudowania środowisk kompilacji krzyżowej. |
| Obrazów      | Skompiluj wynikowy katalog plików docelowych (szczegółowe informacje można znaleźć w instrukcjach poniżej)                     |
| nand_target | Katalog raw głównego systemu plików (używany do generowania obrazów NandFlash)                  |
| cel      | Katalog raw głównego systemu plików (do generowania obrazów eMMC i kart SD do użycia)                 |

K510_crb_lp3_v1_2_defconfig/images to wypalony obraz, w którym opis każdego pliku jest następujący.

| **plik**                   | **Opis treści**                                                 |
| -------------------------- | ------------------------------------------------------------ |
| bootm-bbl.img              | Obraz jądra Linux + bbl (spakowany plik docelowy bpl jądra dla rozruchu uboot bbl) |
| k510.dtb                   | Drzewo urządzeń                                                       |
| sysimage-emmc.img          | emmc burn files: Cały pakiet został spakowany uboot_burn, kernel i bbl              |
| sysImage-sdcard.img        | pliki sdcard burn: cały pakiet został spakowany uboot_burn, jądro i bbl            |
| sysImage-nand.img          | pliki nagrywania nand: Cały pakiet został spakowany uboot_burn, jądro i bbl              |
| u-boot.bin                 | Plik binarny uboot                                             |
| U-boot_burn.bin            | uboot nagrywa pliki                                               |
| uboot-emmc.plv             | Zmienna środowiskowa uboot: Używana do uruchamiania emmc                                  |
| uboot-sd.plv               | Zmienna środowiskowa uboot: używana do uruchamiania sdcard                                |
| uboot-nand.plv             | Zmienna środowiskowa uboot: Używana do uruchamiania nand                                  |
| vmlinux                    | Plik obrazu jądra systemu Linux (z informacjami o debugowaniu elfów)                           |
| rootfs.ext2                | Plik obrazu rootfs ext2 w formacie Buildroot                             |
| sysimage-sdcard-debian.img | sdcard burn files: obrazy kart (rootfs w formacie debian)                     |

K510_crb_lp3_v1_2_defconfig/build jest kodem źródłowym dla wszystkich skompilowanych obiektów, z których kilka jest ważnymi dokumentami opisanymi poniżej.

| **plik**         | **Opis treści**                  |
| ---------------- | ----------------------------- |
| linux-xxx        | Skompilowany katalog źródłowy jądra Linuksa |
| uboot-xxx        | Skompilowany katalog źródłowy Uboot       |
| riscv-hp-k510-xxx| Katalog źródłowy bbl, w którym kompilowany jest kod         |
| ...              |                               |

Uwaga: xxx to numer wersji. W przypadku odwołań do ścieżek kernle, bbl i uboot w późniejszych sekcjach, xxx wszystkie reprezentują numery wersji.

**Potrzebujesz szczególnej uwagi:** Podczas czyszczenia wszystko pod folderem k510_crb_lp3_v1_2_defconfig zostanie usunięte. Dlatego, jeśli chcesz zmodyfikować kod jądra, bbl lub uboot, nie modyfikuj go bezpośrednio w katalogu kompilacji, możesz odwołać się do rozdziału 5, aby użyć metody nadpisywania źródła.

## 4.1 Konfigurowanie buildroot

Wprowadź polecenie buildroot konfiguracji w środowisku docker k510:

```shell
make CONF=k510_crb_lp3_v1_2_defconfig menuconfig
```

Wyniki wykonania są następujące:

![](../zh/images/sdk_build/image-make_men.png)

![](../zh/images/sdk_build/image-make_menu.png)

Po zakończeniu konfiguracji, zapisz i wyjdź, musisz również wykonać następujące polecenie zapisywania konfiguracji buildroot:

```shell
make CONF=k510_crb_lp3_v1_2_defconfig savedefconfig
```

Wyniki wykonania są następujące:

![](../zh/images/sdk_build/image-make_savedef.png)

Po zakończeniu powyższej operacji użytkownik może wprowadzić następujące polecenie, aby ponownie skompilować:

```shell
make CONF=k510_crb_lp3_v1_2_defconfig
```

## 4.2 Konfiguracja U-Boot

Gdy chcesz zmodyfikować konfigurację uboot, możesz wejść do katalogu k510_crb_lp3_v1_2_defconfig i wprowadzić następujące polecenie, aby uruchomić konfigurację U-Boot:

```shell
make uboot-menuconfig
```

Wyniki wykonania są następujące:

![](../zh/images/sdk_build/image-uboot_men.png)

![](../zh/images/sdk_build/image-uboot_menu.png)

Po zamknięciu menuuonfig po zakończeniu konfiguracji wybierz Zapisz konfigurację i musisz wykonać następujące polecenie zapisu konfiguracji:

```shell
make uboot-savedefconfig
```

Wyniki wykonania są następujące:

![](../zh/images/sdk_build/image-uboot_savedefconfig.png)

Na koniec w katalogu k510_crb_lp3_v1_2_defconfig wprowadź następujące polecenie, aby rozpocząć kompilację:

```shell
make uboot-rebuild
```

Zobacz opis w następnej sekcji, aby uzyskać więcej informacji.

## 4.3 Skompiluj U-Boot

Skompilowany kod źródłowy U-Boot jest przechowywany w katalogu k510_crb_lp3_v1_2_defconfig/build/uboot-xxx, a U-Boot musi zostać ponownie skompilowany, niezależnie od tego, czy użytkownik modyfikuje kod źródłowy U-Boot, czy ponownie konfiguruje uboot.

Wejdź do katalogu k510_crb_lp3_v1_2_defconfig i wprowadź następujące polecenie, aby ponownie skompilować U-Boot:

```shell
make uboot-rebuild
```

Wyniki wykonania są następujące:

![](../zh/images/sdk_build/image-uboot-rebuild.png)

Po zakończeniu kompilacji w katalogu k510_crb_lp3_v1_2_defconfig/images generowany jest nowy plik .bin u-boot.

Jeśli chcesz ponownie wygenerować nagrany plik obrazu za pomocą nowego u-boota,`k510_crb_lp3_v1_2_defconfig` wykonaj :w katalogu

```shell
make
```

Wyniki wykonania są następujące:

![](../zh/images/sdk_build/image-make_u.png)

Po zakończeniu kompilacji zostaną wyświetlone informacje wygenerowane przez następujący plik obrazu.

![](../zh/images/sdk_build/image-uboot_r.png)

## 4.4 Konfiguracja jądra Linuksa

Gdy musisz zmodyfikować konfigurację jądra, możesz wejść do katalogu k510_crb_lp3_v1_2_defconfig i wprowadzić następujące polecenie, aby uruchomić konfigurację jądra:

```shell
make linux-menuconfig
```

Wyniki wykonania są następujące:

![](../zh/images/sdk_build/image-linux_men.png)

![](../zh/images/sdk_build/image-linux_menu.png)

Po wyjściu z menuufig po zmodyfikowaniu konfiguracji wybierz Zapisz konfigurację, a na koniec wykonaj następujące polecenie zapisu konfiguracji:

```shell
make linux-savedefconfig
```

Wyniki wykonania są następujące:

![](../zh/images/sdk_build/image-linux_savedefconfig.png)

Na koniec w katalogu k510_crb_lp3_v1_2_defconfig wprowadź następujące polecenie, aby rozpocząć kompilację:

```shell
make linux-rebuild
```

Zobacz opis w następnej sekcji, aby uzyskać więcej informacji.

## 4.5 Skompiluj jądro Linuksa

K510_crb_lp3_v1_2_defconfig/build/linux-xxx przechowuje skompilowany kod źródłowy Linuksa, niezależnie od tego, czy użytkownik modyfikuje kod źródłowy Linuksa, czy rekonfiguruje Linuksa, musi on zostać ponownie skompilowany.

Wejdź do katalogu k510_crb_lp3_v1_2_defconfig i wprowadź następujące polecenie, aby ponownie skompilować linuksa:

```shell
make linux-rebuild
```

Wyniki wykonania są następujące:

![](../zh/images/sdk_build/image-linux_rebuild.png)

Po skompilowaniu nowy vmlinux jest generowany w katalogu k510_crb_lp3_v1_2_defconfig/images.

Obraz jądra Linuksa musi być spakowany z bbl, po przepisaniu jądra Linuksa, musisz ponownie skompilować bbl, aby wygenerować nowy obraz bbl / jądra dla rozruchu, więc wprowadź następujące dwa polecenia.

```shell
make riscv-pk-k510-dirclean
make riscv-pk-k510
```

Wyniki wykonania są następujące:

![](../zh/images/sdk_build/image-riscv.png)

Po zakończeniu kompilacji `k510_crb_lp3_v1_2_defconfig/images`w katalogu generowana jest nowa`bootm-bbl.img`.

Na koniec wprowadź make w katalogu k510_crb_lp3_v1_2_defconfig i użyj nowego pakietu bootm-bbl.img do wygenerowania plików obrazów kart emmc i SD.

```shell
make
```

Wyniki wykonania są następujące:

![](../zh/images/sdk_build/image-make_u.png)

Po zakończeniu kompilacji zostaną wyświetlone informacje wygenerowane przez następujący plik obrazu.

![](../zh/images/sdk_build/image-uboot_r.png)

## 4.6 Kompiluj dts

Plik drzewa urządzeń znajduje się w katalogu k510_buildroot/k510_crb_lp3_v1_2_defconfig/build/linux-4.17/arch/riscv/boot/dts/canaan, a gdy użytkownik modyfikuje tylko drzewo urządzeń, tylko drzewo urządzeń może zostać skompilowane i zdekompilowane.

Napisz skrypt mkdtb-local.sh, który brzmi:

```shell
# !/bin/sh

set -Eeuo pipefail

export BUILDROOT="$(dirname "$(realpath "$0")")"
export VARIANT="${1:-k510_crb_lp3_v1_2}"

if [[ "$VARIANT" = *_defconfig ]]; then
        VARIANT="${VARIANT:0:-10}"
fi

export KERNEL_BUILD_DIR="$BUILDROOT/${VARIANT}_defconfig/build/linux-4.17"
export BINARIES_DIR="$BUILDROOT/${VARIANT}_defconfig/images"
export PATH+=":$BUILDROOT/toolchain/nds64le-linux-glibc-v5d/bin"

riscv64-linux-cpp -nostdinc -I "${KERNEL_BUILD_DIR}/include" -I "${KERNEL_BUILD_DIR}/arch" -undef -x assembler-with-cpp "${KERNEL_BUILD_DIR}/arch/riscv/boot/dts/canaan/${VARIANT}.dts" "${BINARIES_DIR}/${VARIANT}.dts.tmp"

"${KERNEL_BUILD_DIR}/scripts/dtc/dtc" -I dts -o "${BINARIES_DIR}/k510.dtb" "${BINARIES_DIR}/${VARIANT}.dts.tmp"
"${KERNEL_BUILD_DIR}/scripts/dtc/dtc" -I dtb -O dts "${BINARIES_DIR}/k510.dtb" -o "${BINARIES_DIR}/all.dts"

echo "DONE"
echo "${BINARIES_DIR}/k510.dtb"
echo "${BINARIES_DIR}/all.dts"
```

Umieść mkdtb-local.sh w katalogu K510_buildroot i wykonaj następujące polecenie, aby skompilować drzewo urządzeń k510_crb_lp3_v1_2_defconfig płyty:

```shell
./mkdtb-local.sh k510_crb_lp3_v1_2_defconfig
```

Wyniki wykonania są następujące:

![](../zh/images/sdk_build/image-mdk_dts.png)

K510.dtb w katalogu k510_crb_lp3_v1_2_defconfig/images jest nowo wygenerowanym plikiem bazy danych drzewa urządzeń, a all.dts jest plikiem drzewa zdekompilowanych urządzeń.

## 4.7 Kompilowanie aplikacji

Użytkownicy mogą odwoływać się do `package/hello_world` Config.in i pliku makefile w celu zbudowania własnych aplikacji, a aplikacje użytkownika są umieszczane w katalogu k510_buildroot/pakietu.

Proces kompilacji aplikacji ilustruje umieszczenie hello_world projektów w k510_buildroot/pakiecie jako przykład.

Zmodyfikuj pliki Config.in w katalogu k510_buildroot w środowisku hostującym.

![](../zh/images/sdk_build/image-vi_config.png)

W Config.in dodaj ścieżkę, w której znajduje się package/hello_world/Config.in i zapisz.

![](../zh/images/sdk_build/image-config_list.png)

Wprowadź polecenie buildroot konfiguracji w środowisku docker k510:

```shell
make CONF=k510_crb_lp3_v1_2_defconfig menuconfig
```

Wyniki wykonania są następujące:

![](../zh/images/sdk_build/image-build_menu.png)

Zostanie wyświetlona strona konfiguracji katalogu głównego kompilacji, wybierz opcję Rozszerzone, a na koniec wybierz hello_world a następnie zapisz i wyjdź.

![](../zh/images/sdk_build/image-extern_option.png)

Wprowadź polecenie Zapisz konfigurację w katalogu k510_buildroot.

```shell
make CONF=k510_crb_lp3_v1_2_defconfig savedefconfig
```

Wyniki wykonania są następujące:

![](../zh/images/sdk_build/image-build_savedef.png)

1) Jeśli kompilacja odbywa się po raz pierwszy, kroki są następujące:

    W katalogu k510_buildroot wprowadź następujące polecenie, aby skompilować cały program projektu i spakować hello do plików obrazów kart emmc i SD.

    ```shell
    make CONF=k510_crb_lp3_v1_2_defconfig
    ```

    Wyniki wykonania są następujące:

    ![](../zh/images/sdk_build/image-build_make_def.png)

    W katalogu k510_buildroot/k510_crb_lp3_v1_2_defconfig/target można zobaczyć wynikową aplikację hello, która informuje, czy aplikacja została skompilowana poprawnie.

    ![](../zh/images/sdk_build/image-hello.png)

2) Jeśli został skompilowany, po prostu skompiluj aplikację i spakuj ją do obrazu nagrywania, wykonaj następujące kroki:

    Wejdź do katalogu k510_buildroot/k510_crb_lp3_v1_2_defconfig i wprowadź następujące polecenie, aby skompilować aplikację hello.

    ```shell
    make hello_world-rebuild
    ```

    Wyniki wykonania są następujące:

    ![](../zh/images/sdk_build/image-app_build-1.png)

    Przejdź do katalogu k510_buildroot/k510_crb_lp3_v1_2_defconfig i wprowadź polecenie make, aby spakować hello do plików obrazów kart emmc i SD.

    ```shell
    make
    ```

    Wyniki wykonania są następujące:

    ![](../zh/images/sdk_build/image-app-build-2.png)

# 5 Programowanie przy użyciu K510 SDK

## 5.1 kod źródłowy jądra linux/BBL/uboot

Wersja uboot używana przez ten zestaw SDK to 2020.01, katalog poprawek uboot to package/patches/uboot, a katalog po aktualizacji to k510_xxx_defconfig/build/uboot-2020.01.

Katalog poprawek jądra używany przez ten zestaw SDK to 4.17, katalog poprawek jądra to package/patches/linux, a poprawiony katalog to k510_xxx_defconfig/build/linux-4.17.

BBL tego sdk jest umieszczany jako pakiet docelowy w katalogu package/riscv-pk-k510/, a źródło i numer wersji bbl są określone w riscv-pk-k510.mk:

```text
RISCV_PK_K510_VERSION = 1e666d6c5dbab220d2ca57fbd9bec49702599b75
RISCV_PK_K510_SITE = git@github.com:kendryte/k510_BBL.git
RISCV_PK_K510_SITE_METHOD = git
```

## 5.2 Rozwijanie jądra Linux/BBL/uboot

Każda pacyfikacja skompilowana w ramach Buildroot, w tym linux kernel/BBL/uboot, jest implementowana przez pobieranie tarballa, dekompresję, konfigurację, kompilację, instalację i inne ujednolicone kroki zarządzania pakietami, więc chociaż cały kod źródłowy można zobaczyć w katalogu k510_buildroot/k510_crb_lp3_v1_2_defconfig/build, nie ma informacji o kontroli wersji. Nawet jeśli kod jest pobierany z repozytorium git.

Chociaż kod źródłowy jądra/BBL/uboot zawierający dane repozytorium git można zobaczyć w katalogu dl/directory, buildroot buforuje tylko kod źródłowy w katalogu dl i nie zaleca się tworzenia bezpośrednio w tym katalogu.

W przypadku modelu programowania buildroot zapewnia sposób na OVERRIDE_SRCDIR.

Mówiąc prościej, możesz dodać plik local.mk w katalogu k510_crb_lp3_v1_2_defconfig i dodać go:

```text
<pkg1>_OVERRIDE_SRCDIR = /path/to/pkg1/sources
```

- LINUX to nazwa pakietu jądra
- UBOOT to nazwa PAKIETU uboot
- RISCV_PK_K510 jest nazwą pakietu bbl

Weźmy jądro Linuksa jako przykład, aby opisać, jak go używać.
Przypuśćmy, że sklonowałem kod jądra w katalogu /data/yourname/workspace/k510_linux_kernel i dokonałem modyfikacji, a także chcę skompilować w ramach buildroot i przetestować go na płycie crb v1.2, możesz utworzyć local.mk w katalogu k510_crb_lp3_v1_2_defconfig i dodać następujące:

```text
LINUX_OVERRIDE_SRCDIR = /data/yourname/workspace/k510_linux_kernel
```

Wykonaj w katalogu k510_crb_lp3_v1_2_defconfig

```shell
make linux-rebuild
```

Widać, że jądro zostało ponownie skompilowane w katalogu build/linux-custom, używając zmodyfikowanego kodu w /data/yourname/workspace/k510_linux_kernel.
UBOOT i BBL są podobne. W ten sposób można bezpośrednio zmodyfikować kod jądra i przepisać jądro w kompilowaniu i stopniowo kompilować obraz do testowania.
Uwaga: Kod źródłowy override zostanie dodany do sufiksu custom w nazwie katalogu k510_crb_lp3_v1_2_defconfig/build, aby odróżnić źródło każdego pakietu w domyślnej konfiguracji buildroot. Na przykład w powyższym przykładzie jądra Linuksa kompilacja zobaczy, że kod określony przez nadpisanie jest kompilowany w katalogu k510_crb_lp3_v1_2_defconfig/build/linux-custom, a nie w katalogu k510_crb_lp3_v1_2_defconfig/build/linux-xxx, który widzieliśmy wcześniej.

W przypadku innego kodu w katalogu pakietów lub pakietów natywnych buildroot możliwe jest rozwijanie w ramach struktury buildroot w ten sposób.

# 6 Nagrywanie obrazu

K510 obsługuje tryb rozruchu sdcard i eMMC, za każdym razem, gdy kompilacja w katalogu k510_buildroot/k510_crb_lp3_v1_2_defconfig/image wygeneruje pliki obrazów sysimage-sdcard.img i sysimg-emmc.img, oba pliki można nagrać odpowiednio na sdcard i eMMC.

K510 określa tryb rozruchu układu na podstawie stanu pinów sprzętowych boot0 i BOOT1, zapoznaj się z sekcją instrukcji rozruchu na płycie programistycznej, aby uzyskać określone ustawienia.

| ROZRUCH1   | BOOT0   | Tryb uruchamiania      |
| ------- | ------- | ------------ |
| 0(WŁ.)   | 0(WŁ.)   | Rozruch z portu szeregowego      |
| 0(WŁ.)   | 1 (WYŁ.)  | Uruchamianie karty SD      |
| 1 (WYŁ.)  | 0(WŁ.)   | Buty NANDFLASH |
| 1 (WYŁ.)  | 1 (WYŁ.)  | Buty EMMC      |

![](../zh/images/hw_crb_v1_2/clip_hw_3_9.jpg)

## 6.1 Nagraj obraz na kartę SD

### 6.1.1 Ubuntu spalone

Przed włożeniem karty sD do hosta wprowadź:

```shell
ls -l /dev/sd*
```

Wyświetl bieżące urządzenie pamięci masowej.

Po włożeniu karty sD do hosta wprowadź ją ponownie:

```shell
ls -l /dev/sd*
```

Patrząc na urządzenie pamięci masowej w tym momencie, nowym dodatkiem jest węzeł urządzenia karty SD.

Po włożeniu karty sD do hosta wynik wykonania polecenia ls jest następujący:

![](../zh/images/sdk_build/image-dev_sd.png)

/dev/sdc jest węzłem urządzenia karty SD. **Uwaga: Węzeł urządzenia karty SD wygenerowany w środowisku użytkownika może nie być /dev/sdc, a kolejne operacje muszą być modyfikowane zgodnie z rzeczywistym węzłem.**

Wejdź do katalogu k510_buildroot/k510_crb_lp3_v1_2_defconfig/image pod hostem i wprowadź polecenie dd, aby nagrać sysimage-sdcard.img do sdk:

```shell
sudo dd if=sysimage-sdcard.img of=/dev/sdc bs=1M oflag=sync
```

Wynik wykonania pod hostem jest następujący:

![](../zh/images/sdk_build/image-dd.png)

### 6.1.2 Nagrywanie w systemie Windows

W systemie Windows kartę sD można spalić za pomocą narzędzia banana Etcher (adres pobierania narzędzia balena Etcher<https://www.balena.io/etcher/>).

1) Włóż kartę TF do komputera, a następnie uruchom narzędzie ColumnEtcher, kliknij przycisk "Flash from file" interfejsu narzędzia, wybierz oprogramowanie układowe do nagrania, jak pokazano na poniższym rysunku.

    ![](../zh/images/sdk_build/image-sd_pre0.png)

2) Kliknij przycisk "Wybierz cel" w interfejsie narzędzia i wybierz docelową kartę SDcard.

    ![](../zh/images/sdk_build/image-pre1.png)

3) Kliknij przycisk "Flash", aby rozpocząć, proces ma wyświetlacz paska postępu, zakończenie lampy błyskowej zostanie poproszone po zakończeniu.

    | ![](../zh/images/sdk_build/clip_image_p1.jpg) | ![](../zh/images/sdk_build/clip_image_p2.jpg) |
    | --------------------------------------- | --------------------------------------- |
    |                                         |                                         |

4) Po zakończeniu włóż kartę SD do gniazda płytki rozwojowej, wybierz BOOT, aby rozpocząć od SD, a na koniec płytka rozwojowa może być włączona, aby rozpocząć od karty SD.

## 6.2 Nagraj obraz do emmc

Aby nagrać sysimage-emmc.img na wbudowanym eMMC, za pomocą sdk, w środowisku ubuntu, sysimage-emmc.img jest przechowywany na partycji użytkownika sdk, a następnie sdk jest wkładany do płyty i włączany.

Przed nagraniem obrazu emmc należy odinstalować system plików związany z emmc, należy wykonać następujące kroki, aby go odinstalować.

```shell
mount | grep emmc
```

Wynik wykonania jest następujący:

![](../zh/images/sdk_build/image-emmc_1.png)

Wprowadź następujące polecenie, aby odinstalować i sprawdzić.

```shell
umount /root/emmc/p2
umount /root/emmc/p3
umount /root/emmc/p4
mount | grep emmc
```

Wynik wykonania jest następujący:

![](../zh/images/sdk_build/image-emmc_2.png)

Na koniec wprowadź ścieżkę, w której znajduje się obraz, wprowadź następujące polecenie, aby nagrać eMMC.

```shell
dd if=sysimage-emmc.img of=/dev/mmcblk0 bs=1M
```

Wynik wykonania jest następujący:

![](../zh/images/sdk_build/image-emmc3.png)

**Uwaga: Proces spalania jest powolny, trwa około 30 sekund, prosimy o cierpliwość.**

Po zakończeniu wybierz BOOT to Boot z EMMC, a na koniec włącz płytę, aby uruchomić z EMMC.

# 7 Środowisko   <a id="env_set">kompilacji skonfigurowane przez użytkownika </a>

Jeśli nie korzystasz z powyższego środowiska docker, możesz skonfigurować własne środowisko programistyczne, odwołując się do następującego polecenia w ubuntu18.04 / 20.04, jeśli nie masz uprawnień, użyj`sudo` go.

```shell
apt-get update
apt-get upgrade
apt-get install libc6-i386 libc6-dev-i386

apt-get install mtools
apt-get install dosfstools
apt-get install python
apt-get install python-pip
python2 -m pip install pycrypto

apt-get install python3.7
apt-get install python3-pip
python3.7 -m pip install --upgrade pip
ln -sf /usr/bin/python3.7 /usr/bin/python3
python3 -m pip install onnx==1.9.0 onnx-simplifier==0.3.6 onnxoptimizer==0.2.6 onnxruntime==1.8.0 -i https://pypi.tuna.tsinghua.edu.cn/simple

#进行下一步，需进入k510_buildroot/nncase目录，将nncase_v1.4.0.tgz解压后进入k510_buildroot/nncase/nncase_v1.4.0目录，输入如下命令安装*.whl
python3 -m pip install x86_64/*.whl
#运行python3 -m pip show nncase，若看到nncase版本信息则表示AI应用程序环境部署成功。
python3 -m pip show nncase

python3 -m pip install xlrd==1.2.0
python3 -m  pip install pystache
dpkg --add-architecture i386
apt update
apt install libncurses5:i386
apt-get install wget
apt-get install cpio
apt-get install unzip
apt-get install rsync
apt-get install bc
apt-get install libssl-dev
pip3 install pycryptodome
```

**Zrzeczenie się odpowiedzialności za**tłumaczenie  
Dla wygody klientów Canaan używa tłumacza AI do tłumaczenia tekstu na wiele języków, które mogą zawierać błędy. Nie gwarantujemy dokładności, rzetelności ani terminowości dostarczonych tłumaczeń. Canaan nie ponosi odpowiedzialności za jakiekolwiek straty lub szkody spowodowane poleganiem na dokładności lub wiarygodności przetłumaczonych informacji. W przypadku różnic w treści tłumaczeń w różnych językach, pierwszeństwo ma chińska wersja uproszczona.

Jeśli chcesz zgłosić błąd lub niedokładność tłumaczenia, skontaktuj się z nami pocztą.
