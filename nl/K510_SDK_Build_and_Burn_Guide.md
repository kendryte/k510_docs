![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 SDK Build and Burn Gids</font>**

<font face="黑体"  size=3>Document versie: V1.0.0</font>

<font face="黑体"  size=3>Publicatiedatum: 2022-03-07</font>

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

| Het versienummer   | Gewijzigd door     | Datum van herziening | Opmerkingen bij herziening |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | Divisie AI-producten | 2022-03-07 |          |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Inhoud</font>**

[INHOUDSOPGAVE]

<div style="page-break-after:always"></div>

# 1 Inleiding

In dit document wordt de inhoud van de constructiesectie van de ontwikkelomgeving beschreven, zoals het downloaden, compileren en branden van de K510 SDK.

# 2 k510 SDK

## 2.1 k510 sdk te downloaden

k510 SDK-projectadres: <https://github.com/kendryte/k510_buildroot>

Verkrijg de K510 SDK:

```shell
git clone https://github.com/kendryte/k510_buildroot.git
```

## 2.2 k510 SDK pakket introductie

De K510 SDK is een embedded Linux ontwikkelomgeving gebaseerd op de buildroot als basis framework, gebaseerd op het K510 linux kernel (linux versie 4.17.0), u-boot (u-boot versie 2020.01), riscv-pk-k510 (BBL) broncodepakket, de K510 SDK directory structuur wordt getoond in de volgende afbeelding.

![](../zh/images/sdk_build/image-buildroot.png)

 De K510 SDK-bestanden worden als volgt beschreven:

| **bestand**        | **Beschrijving van de inhoud**                                                 |
| --------------- | ------------------------------------------------------------ |
| plank           | Map, dat is K510 verschillende configuratiebestanden en scripts, zoals het configuratiebestand voor het genereren van images (genimage-xxx.cfg), buildroot post-image scripts, U-Boot standaard omgevingsvariabelen, enz. |
| Config.in       | Het geeft het pakket aan waarvoor buildroot-compilatie vereist is. |
| configuraties         | Map, waar is het standaard compilatieconfiguratiebestand van het bord. Slaat momenteel de standaard compilatieconfiguratiebestanden op voor de K510 CRB-V0.1, K510 CRB-V1.2 en K510 EVB-borden:<br /> -`k510_crb_lp3_v1_2_defconfig`<br />-`k510_crb_lp3_v0_1_defconfig`<br />- `k510_evb_lp3_v1_1_defconfig` |
| extern.desc   | Het configuratiebestand voor externe mechanismen van Buildroot. |
| external.mk     | |
| Makefile        | De belangrijkste Makefile van de k510 SDK. |
| pak         | Mappen, die voornamelijk K510-toepassingen zijn, Config.in de inhoud van het bestand bepalen welke toepassingen onder die map worden gecompileerd. |
| Patches         | Map, waar is het buildroot patchbestand, Makefile zal de broncode uitpakken wanneer het patchbestand in deze map naar de overeenkomstige broncode map. |
| pkg-downloaden    | Map, een gecomprimeerd pakket van de dl-map. |
| README.md       | SDK-gerelateerde instructies. |
| release_note.md | |
| toolchain       | map, waar is de cross-compilatie toolchain. |
| Dl              | Map, is het dl extract pakket in pkg-download, als er andere pakketten worden toegevoegd zal ook worden gedownload naar deze map. |

## 2.3 k510 sdk versie

Wanneer u de afbeelding die door de k510 sdk wordt gegenereerd op het bord brandt, wordt de versie-informatie afgedrukt, zoals weergegeven in de volgende afbeelding:

```text
#############SDK VERSION############################################
MX2_DEV_0106-02e87077-20220428-153936CST-xxxxx-server
####################################################################
```

Nadat het opstarten is voltooid, voert u het volgende in de shellterminal in om de SDK-versiegegevens weer te geven:

```shell
cat /etc/version/release_version
#############SDK VERSION############################################
MX2_REL_0106-02e87077-20220428-153936CST-xxxx-server
####################################################################
```

**Opmerking: De bovenstaande informatie kan variëren, afhankelijk van de K510 SDK-versie**.

# 3 docker compilatie omgeving

Nadat u de k510 sdk hebt gedownload, voert u de volgende opdracht uit in de bovenliggende map van de SDK om de docker te starten:

```shell
sh k510_buildroot/tools/docker/run_k510_docker.sh
```

Volgende compilatiebewerkingen worden standaard in docker uitgevoerd.
Als u een lokale omgeving moet instellen, raadpleegt u[Local Environment Setup](#env_set)

# 4 Compileren

## 4.1 Compilatie voorbereiding

### 4.1.1 Download het broncodepakket (optioneel, kan de compilatie versnellen)

Voer de volgende opdracht uit om het bronpakket te downloaden:

```shell
make dl
```

## 4.2 Compilatie

K510_buildroot/config directory heeft compilatie configuratiebestanden voor drie ontwikkelborden, namelijk`k510_crb_lp3_v0_1_defconfig` , ,`k510_crb_lp3_v1_2_defconfig` en `k510_evb_lp3_v1_1_defconfig`, dit document wordt geïllustreerd door k510_crb_lp3_v1_2_defconfig te selecteren als het compilatiedoel****.

Voer in de k510 docker-omgeving de volgende opdracht in om te beginnen met compileren:

```shell
make CONF=k510_crb_lp3_v1_2_defconfig
```

![](../zh/images/sdk_build/image-make.png)

Het volgende bericht geeft aan dat de compilatie is voltooid.

![](../zh/images/sdk_build/image-uboot_r.png)

Nadat de compilatie is voltooid, wordt de map gegenereerd`k510_crb_lp3_v1_2_defconfig`.

![afbeelding-20220311121912711](../zh/images/sdk_build/image-makeout.png)

Elk van deze documenten wordt als volgt beschreven:

| **bestand**    | **Beschrijving van de inhoud**                                                 |
| ----------- | ------------------------------------------------------------ |
| Makefile    | Compileer de afbeelding om Makefile te gebruiken.                                     |
| bouwen       | De compilatiemap voor alle bronpakketten. Bijvoorbeeld, linux kernel, u-boot, BBL, busybox, etc., de broncode zal worden geëxtraheerd naar de build directory en gecompileerd. |
| gastheer        | Alle installatiepaden van het hostpakket, toolchain worden ook naar deze map gekopieerd voor het bouwen van cross-compilatie-omgevingen. |
| beelden      | Compileer de resulterende doelbestandmap (zie onderstaande instructies voor meer informatie)                     |
| nand_target | Root bestandssysteem raw directory (gebruikt om NandFlash-afbeeldingen te genereren)                  |
| doel      | Root bestandssysteem raw directory (om eMMC en SD-kaartafbeeldingen te genereren om te gebruiken)                 |

K510_crb_lp3_v1_2_defconfig/images directory is een gebrande afbeelding, waarin de beschrijving van elk bestand als volgt is.

| **bestand**                   | **Beschrijving van de inhoud**                                                 |
| -------------------------- | ------------------------------------------------------------ |
| bootm-bbl.img              | Linux+bbl kernel image (verpakt kernel bpl doelbestand voor uboot boot bbl) |
| K510.dTB                   | Apparaatstructuur                                                       |
| Sysimage-emmc.img          | emmc burn bestanden: Het hele pakket is verpakt uboot_burn, kernel en bbl              |
| sysImage-sdcard.img        | sdcard burn files: het hele pakket is verpakt uboot_burn, kernel en bbl            |
| sysImage-nand.img          | nand burn-bestanden: Het hele pakket is verpakt uboot_burn, kernel en bbl              |
| u-boot.bin                 | uboot binair bestand                                             |
| U-boot_burn.bin            | uboot brandt bestanden                                               |
| uboot-emmc.nlv             | uboot environment variable: Gebruikt voor emmc opstarten                                  |
| uboot-sd.nld               | uboot omgevingsvariabele: Gebruikt voor het opstarten van sdcard                                |
| uboot-nand.nl             | uboot environment variable: Gebruikt voor nand opstarten                                  |
| Vmlinux                    | Linux kernel image file (met elf debug informatie)                           |
| Rootfs.ext2                | Buildroot formaat rootfs ext2 afbeeldingsbestand                             |
| sysimage-sdcard-debian.img | sdcard burn files: card images (rootfs in debian formaat)                     |

K510_crb_lp3_v1_2_defconfig/build directory is de broncode voor alle gecompileerde objecten, waarvan er verschillende belangrijke documenten zijn die hieronder worden beschreven.

| **bestand**         | **Beschrijving van de inhoud**                  |
| ---------------- | ----------------------------- |
| Linux-xxx        | De gecompileerde Linux kernel bronmap |
| UBOOT-XXX        | De gecompileerde Uboot-bronmap       |
| riscv-pk-k510-xxx| De bbl-bronmap waarin de code is gecompileerd         |
| ...              |                               |

Opmerking: xxx is het versienummer. Wanneer verwijzingen naar de paden van kernle, bbl en uboot in latere secties, xxx allemaal versienummers vertegenwoordigen.

**Speciale aandacht nodig:** Bij het schoonmaken wordt alles onder de map k510_crb_lp3_v1_2_defconfig verwijderd. Daarom, als u de kernel-, bbl- of uboot-code moet wijzigen, wijzig deze dan niet rechtstreeks in de build-map, u kunt hoofdstuk 5 raadplegen om de override source-methode te gebruiken.

## 4.1 Buildroot configureren

Voer de configuratie buildroot commando in de k510 docker omgeving:

```shell
make CONF=k510_crb_lp3_v1_2_defconfig menuconfig
```

De resultaten van de uitvoering zijn als volgt:

![](../zh/images/sdk_build/image-make_men.png)

![](../zh/images/sdk_build/image-make_menu.png)

Nadat u de configuratie hebt voltooid, opslaan en afsluiten, moet u ook de volgende buildroot-configuratie-opslagopdracht uitvoeren:

```shell
make CONF=k510_crb_lp3_v1_2_defconfig savedefconfig
```

De resultaten van de uitvoering zijn als volgt:

![](../zh/images/sdk_build/image-make_savedef.png)

Nadat de bovenstaande bewerking is voltooid, kan de gebruiker de volgende opdracht invoeren om opnieuw te compileren:

```shell
make CONF=k510_crb_lp3_v1_2_defconfig
```

## 4.2 U-Boot configureren

Wanneer u de uboot-configuratie moet wijzigen, kunt u de map k510_crb_lp3_v1_2_defconfig invoeren en de volgende opdracht invoeren om de U-Boot-configuratie te starten:

```shell
make uboot-menuconfig
```

De resultaten van de uitvoering zijn als volgt:

![](../zh/images/sdk_build/image-uboot_men.png)

![](../zh/images/sdk_build/image-uboot_menu.png)

Wanneer u de menuuonfig afsluit na het voltooien van de configuratie, selecteert u Configuratie opslaan en moet u de volgende opdracht voor het opslaan van configuraties uitvoeren:

```shell
make uboot-savedefconfig
```

De resultaten van de uitvoering zijn als volgt:

![](../zh/images/sdk_build/image-uboot_savedefconfig.png)

Voer ten slotte in de map k510_crb_lp3_v1_2_defconfig de volgende opdracht in om de compilatie te starten:

```shell
make uboot-rebuild
```

Zie de beschrijving in de volgende sectie voor meer informatie.

## 4.3 Compileer de U-Boot

De gecompileerde U-Boot broncode wordt opgeslagen in de map k510_crb_lp3_v1_2_defconfig/build/uboot-xxx en de U-Boot moet opnieuw worden gecompileerd, ongeacht of de gebruiker de U-Boot-broncode wijzigt of de uboot opnieuw configureert.

Voer de map k510_crb_lp3_v1_2_defconfig in en voer de volgende opdracht in om U-Boot opnieuw te compileren:

```shell
make uboot-rebuild
```

De resultaten van de uitvoering zijn als volgt:

![](../zh/images/sdk_build/image-uboot-rebuild.png)

Nadat de compilatie is voltooid, wordt een nieuw u-boot .bin-bestand gegenereerd in de map k510_crb_lp3_v1_2_defconfig/images.

Als u het gebrande afbeeldingsbestand opnieuw wilt genereren met een nieuwe u-boot,`k510_crb_lp3_v1_2_defconfig` voert u :in de map uit

```shell
make
```

De resultaten van de uitvoering zijn als volgt:

![](../zh/images/sdk_build/image-make_u.png)

Wanneer de compilatie is voltooid, ziet u de informatie die wordt gegenereerd door het volgende afbeeldingsbestand.

![](../zh/images/sdk_build/image-uboot_r.png)

## 4.4 Configureer de Linux kernel

Wanneer u de kernelconfiguratie moet wijzigen, kunt u de map k510_crb_lp3_v1_2_defconfig invoeren en de volgende opdracht invoeren om de kernelconfiguratie te starten:

```shell
make linux-menuconfig
```

De resultaten van de uitvoering zijn als volgt:

![](../zh/images/sdk_build/image-linux_men.png)

![](../zh/images/sdk_build/image-linux_menu.png)

Wanneer u menuufig afsluit nadat u de configuratie hebt gewijzigd, selecteert u Configuratie opslaan en voert u ten slotte de volgende opdracht voor het opslaan van configuratie uit:

```shell
make linux-savedefconfig
```

De resultaten van de uitvoering zijn als volgt:

![](../zh/images/sdk_build/image-linux_savedefconfig.png)

Voer ten slotte in de map k510_crb_lp3_v1_2_defconfig de volgende opdracht in om de compilatie te starten:

```shell
make linux-rebuild
```

Zie de beschrijving in de volgende sectie voor meer informatie.

## 4.5 Compileer de Linux kernel

K510_crb_lp3_v1_2_defconfig/build/linux-xxx directory bevat de gecompileerde Linux broncode, of de gebruiker nu de Linux broncode wijzigt of de Linux opnieuw configureert, deze moet opnieuw worden gecompileerd.

Voer de map k510_crb_lp3_v1_2_defconfig in en voer de volgende opdracht in om linux opnieuw te compileren:

```shell
make linux-rebuild
```

De resultaten van de uitvoering zijn als volgt:

![](../zh/images/sdk_build/image-linux_rebuild.png)

Na het compileren wordt een nieuwe vmlinux gegenereerd in de map k510_crb_lp3_v1_2_defconfig/images.

Linux kernel image moet worden verpakt met bbl, na het herschrijven van de Linux kernel, moet u de bbl opnieuw compileren om een nieuwe bbl/kernel image te genereren voor you-boot boot, dus voer de volgende twee commando's in.

```shell
make riscv-pk-k510-dirclean
make riscv-pk-k510
```

De resultaten van de uitvoering zijn als volgt:

![](../zh/images/sdk_build/image-riscv.png)

Wanneer de compilatie is voltooid, wordt er een`k510_crb_lp3_v1_2_defconfig/images` nieuwe gegenereerd in de directory`bootm-bbl.img`.

Voer ten slotte make in de map k510_crb_lp3_v1_2_defconfig in en gebruik het nieuwe pakket bootm-bbl.img om emmc- en SD-kaartimagebestanden te genereren.

```shell
make
```

De resultaten van de uitvoering zijn als volgt:

![](../zh/images/sdk_build/image-make_u.png)

Wanneer de compilatie is voltooid, ziet u de informatie die wordt gegenereerd door het volgende afbeeldingsbestand.

![](../zh/images/sdk_build/image-uboot_r.png)

## 4.6 Dts compileren

Het apparaatstructuurbestand bevindt zich in de map k510_buildroot/k510_crb_lp3_v1_2_defconfig/build/linux-4.17/arch/riscv/boot/dts/canaan en wanneer de gebruiker alleen de apparaatstructuur wijzigt, kan alleen de apparaatstructuur worden gecompileerd en gedecompileerd.

Schrijf een mkdtb-local.sh script dat luidt:

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

Plaats de mkdtb-local.sh in de map K510_buildroot en voer de volgende opdracht uit om de k510_crb_lp3_v1_2_defconfig board-apparaatstructuur te compileren:

```shell
./mkdtb-local.sh k510_crb_lp3_v1_2_defconfig
```

De resultaten van de uitvoering zijn als volgt:

![](../zh/images/sdk_build/image-mdk_dts.png)

K510.dtb in de map k510_crb_lp3_v1_2_defconfig/images is het nieuw gegenereerde databasebestand van de apparaatstructuur en all.dts is het gedecompileerde apparaatstructuurbestand.

## 4.7 Compileer de app

Gebruikers kunnen verwijzen naar `package/hello_world` de Config.in en makefile-bestand schrijven om hun eigen toepassingen te bouwen, en de gebruikerstoepassingen worden in de map k510_buildroot / pakket geplaatst.

Het proces van het samenstellen van een applicatie wordt geïllustreerd door hello_world projecten als voorbeeld in k510_buildroot/pakket te plaatsen.

Wijzig de Config.in bestanden in de map k510_buildroot in de hostingomgeving.

![](../zh/images/sdk_build/image-vi_config.png)

Voeg in de Config.in het pad toe waar package/hello_world/Config.in zich bevindt en sla op.

![](../zh/images/sdk_build/image-config_list.png)

Voer de configuratie buildroot commando in de k510 docker omgeving:

```shell
make CONF=k510_crb_lp3_v1_2_defconfig menuconfig
```

De resultaten van de uitvoering zijn als volgt:

![](../zh/images/sdk_build/image-build_menu.png)

De buildroot-configuratiepagina verschijnt, selecteer De uitgebreide optie en selecteer ten slotte de hello_world en sla deze op en sluit af.

![](../zh/images/sdk_build/image-extern_option.png)

Voer de opdracht Configuratie opslaan in de map k510_buildroot in.

```shell
make CONF=k510_crb_lp3_v1_2_defconfig savedefconfig
```

De resultaten van de uitvoering zijn als volgt:

![](../zh/images/sdk_build/image-build_savedef.png)

1) Als het de eerste keer is om te compileren, zijn de stappen als volgt:

    Voer in de map k510_buildroot de volgende opdracht in om het volledige projectprogramma te compileren en hello te verpakken in emmc- en sd-kaartafbeeldingsbestanden.

    ```shell
    make CONF=k510_crb_lp3_v1_2_defconfig
    ```

    De resultaten van de uitvoering zijn als volgt:

    ![](../zh/images/sdk_build/image-build_make_def.png)

    In de map k510_buildroot/k510_crb_lp3_v1_2_defconfig/target ziet u de resulterende hello-toepassing, die vertelt of de toepassing correct is gecompileerd.

    ![](../zh/images/sdk_build/image-hello.png)

2) Als het is gecompileerd, compileer dan gewoon de app en verpak deze in de brandafbeelding, volg deze stappen:

    Voer de map k510_buildroot/k510_crb_lp3_v1_2_defconfig in en voer de volgende opdracht in om de hello-toepassing te compileren.

    ```shell
    make hello_world-rebuild
    ```

    De resultaten van de uitvoering zijn als volgt:

    ![](../zh/images/sdk_build/image-app_build-1.png)

    Ga naar de map k510_buildroot/k510_crb_lp3_v1_2_defconfig en voer de opdracht make in om hello te verpakken in de emmc- en sd-kaartimagebestanden.

    ```shell
    make
    ```

    De resultaten van de uitvoering zijn als volgt:

    ![](../zh/images/sdk_build/image-app-build-2.png)

# 5 Ontwikkelen met de K510 SDK

## 5.1 linux kernel/BBL/uboot broncode

De uboot-versie die door deze SDK wordt gebruikt, is 2020.01, de uboot-patchmap is package/patches/uboot en de map na het patchen is k510_xxx_defconfig/build/uboot-2020.01.

De kernel patch directory die door deze sdk wordt gebruikt is 4.17, de kernel patch directory is package/patches/linux en de patched directory is k510_xxx_defconfig/build/linux-4.17.

De BBL van deze sdk wordt als doelpakket in de map package/riscv-pk-k510/map geplaatst en de bron en het versienummer van de bbl worden opgegeven in de riscv-pk-k510.mk:

```text
RISCV_PK_K510_VERSION = 1e666d6c5dbab220d2ca57fbd9bec49702599b75
RISCV_PK_K510_SITE = git@github.com:kendryte/k510_BBL.git
RISCV_PK_K510_SITE_METHOD = git
```

## 5.2 Ontwikkel linux kernel/BBL/uboot

Elke pacificatie gecompileerd onder Buildroot, inclusief linux kernel/BBL/uboot, wordt geïmplementeerd door tarball te downloaden, te decomprimeren, configureren, compileren, installeren en andere unified package management stappen, dus hoewel alle broncode kan worden gezien in de k510_buildroot/ k510_crb_lp3_v1_2_defconfig / build directory, is er geen versiebeheer informatie. Zelfs als de code is gedownload van een git repository.

Hoewel de kernel/BBL/uboot broncode met de git repository data te zien is in de dl/directory, cachet buildroot alleen de broncode in de dl directory en wordt het niet aanbevolen om direct in deze directory te ontwikkelen.

Voor het ontwikkelingsmodel biedt buildroot een manier om OVERRIDE_SRCDIR.

In eenvoudige bewoordingen kunt u een local.mk bestand toevoegen onder de map k510_crb_lp3_v1_2_defconfig en deze toevoegen:

```text
<pkg1>_OVERRIDE_SRCDIR = /path/to/pkg1/sources
```

- LINUX is de pakketnaam van de kernel
- UBOOT is de PAKKETnaam van uboot
- RISCV_PK_K510 is de pakketnaam van de bbl

Laten we de Linux-kernel als voorbeeld nemen om te beschrijven hoe deze te gebruiken.
Stel dat ik de kernelcode in de map /data/yourname/workspace/k510_linux_kernel heb gekloond en wijzigingen heb aangebracht, en deze onder buildroot wil compileren en testen op het crb v1.2-bord, kunt u een local.mk maken in de map k510_crb_lp3_v1_2_defconfig en het volgende toevoegen:

```text
LINUX_OVERRIDE_SRCDIR = /data/yourname/workspace/k510_linux_kernel
```

Uitvoeren in de map k510_crb_lp3_v1_2_defconfig

```shell
make linux-rebuild
```

U kunt zien dat de kernel opnieuw is gecompileerd in de build/linux-custom directory, met behulp van de gewijzigde code onder /data/yourname/workspace/k510_linux_kernel.
UBOOT en BBL zijn vergelijkbaar. Op deze manier kunt u de kernelcode direct wijzigen en de kernel onder buildroot herschrijven en de image stapsgewijs compileren om te testen.
Opmerking: De broncode van override wordt toegevoegd aan het achtervoegsel custom in de mapnaam van de map k510_crb_lp3_v1_2_defconfig/build-map om de bron van elk pakket te onderscheiden in de standaardconfiguratie van buildroot. In het voorbeeld van de Linux-kernel hierboven zal de compilatie bijvoorbeeld zien dat de code die door de overrideide wordt opgegeven, wordt gecompileerd in de map k510_crb_lp3_v1_2_defconfig/build/linux-custom, in plaats van de map k510_crb_lp3_v1_2_defconfig/build/linux-xxx die we eerder zagen.

Voor andere code in de pakketmap, of buildroot native pakketten, is het mogelijk om op deze manier te ontwikkelen onder het buildroot framework.

# 6 Brand de afbeelding

K510 ondersteunt sdcard en eMMC boot mode, elke keer dat het compileren in de k510_buildroot / k510_crb_lp3_v1_2_defconfig / image directory zal genereren sysimage-sdcard.img en sysimg-emmc.img image bestanden, de twee bestanden kunnen worden gebrand op sdcard en eMMC respectievelijk.

De K510 bepaalt de chip boot mode door de status van de boot0 en BOOT1 hardware pinnen, raadpleeg de boot instructies sectie van de development board voor specifieke instellingen.

| BOOT1   | BOOT0   | Opstartmodus      |
| ------- | ------- | ------------ |
| 0(AAN)   | 0(AAN)   | Seriële poort boot      |
| 0(AAN)   | 1 (UIT)  | De SD-kaart start op      |
| 1 (UIT)  | 0(AAN)   | NANDFLASH laarzen |
| 1 (UIT)  | 1 (UIT)  | EMMC laarzen      |

![](../zh/images/hw_crb_v1_2/clip_hw_3_9.jpg)

## 6.1 Brand de afbeelding op de SD-kaart

### 6.1.1 Ubuntu gebrand

Voer voordat u de SD-kaart in de host plaatst het volgende in:

```shell
ls -l /dev/sd*
```

Bekijk het huidige opslagapparaat.

Nadat u de SD-kaart in de host hebt geplaatst, voert u deze opnieuw in:

```shell
ls -l /dev/sd*
```

Kijkend naar het opslagapparaat op dit moment, is de nieuwe toevoeging de sd-kaart apparaat node.

Na het plaatsen van de sD-kaart in de host is het uitvoeringsresultaat van de ls-opdracht als volgt:

![](../zh/images/sdk_build/image-dev_sd.png)

/dev/sdc is het knooppunt van het SD-kaartapparaat. **Opmerking: Het sd-kaartapparaatknooppunt dat in de gebruikersomgeving wordt gegenereerd, is mogelijk niet /dev/sdc en latere bewerkingen moeten worden gewijzigd op basis van het werkelijke knooppunt.**

Voer de map k510_buildroot/k510_crb_lp3_v1_2_defconfig/image in onder de host en voer de opdracht dd in om sysimage-sdcard.img op de sdk te branden:

```shell
sudo dd if=sysimage-sdcard.img of=/dev/sdc bs=1M oflag=sync
```

Het uitvoeringsresultaat onder de host is als volgt:

![](../zh/images/sdk_build/image-dd.png)

### 6.1.2 Branden onder Windows

Onder Windows kan de sD-kaart worden gebrand door de banana Etcher-tool (balena Etcher tool downloadadres<https://www.balena.io/etcher/>).

1) Plaats de TF-kaart in de pc, start vervolgens de ColumnEtcher-tool, klik op de knop "Flash uit bestand" van de toolinterface, selecteer de firmware die moet worden gebrand, zoals weergegeven in de volgende afbeelding.

    ![](../zh/images/sdk_build/image-sd_pre0.png)

2) Klik op de knop "Doel selecteren" van de toolinterface en selecteer de doel sdcard-kaart.

    ![](../zh/images/sdk_build/image-pre1.png)

3) Klik op de knop "Flash" om te beginnen met knipperen, het knipperproces heeft een voortgangsbalkweergave, flash Finish wordt gevraagd na het einde van het knipperen.

    | ![](../zh/images/sdk_build/clip_image_p1.jpg) | ![](../zh/images/sdk_build/clip_image_p2.jpg) |
    | --------------------------------------- | --------------------------------------- |
    |                                         |                                         |

4) Wanneer het knipperen is voltooid, plaatst u de SD-kaart in de sleuf van de ontwikkelingskaart, selecteert u BOOT om vanaf SD te starten en ten slotte kan het ontwikkelingsbord worden ingeschakeld om vanaf de SD-kaart te starten.

## 6.2 Brand de afbeelding op emmc

Om de sysimage-emmc.img op de on-board eMMC te branden, met behulp van de sdk, in de ubuntu-omgeving, wordt de sysimage-emmc.img opgeslagen in de gebruikerspartitie van de sdk en vervolgens wordt de sdk in het bord ingevoegd en ingeschakeld.

Voordat u de emmc-afbeelding brandt, moet u het emmc-gerelateerde bestandssysteem ontkoppelen, raadpleegt u de volgende stappen om het te ontkoppelen.

```shell
mount | grep emmc
```

Het uitvoeringsresultaat is als volgt:

![](../zh/images/sdk_build/image-emmc_1.png)

Voer de volgende opdracht in om te verwijderen en te controleren.

```shell
umount /root/emmc/p2
umount /root/emmc/p3
umount /root/emmc/p4
mount | grep emmc
```

Het uitvoeringsresultaat is als volgt:

![](../zh/images/sdk_build/image-emmc_2.png)

Voer ten slotte het pad in waar de afbeelding zich bevindt, voer de volgende opdracht in om eMMC te branden.

```shell
dd if=sysimage-emmc.img of=/dev/mmcblk0 bs=1M
```

Het uitvoeringsresultaat is als volgt:

![](../zh/images/sdk_build/image-emmc3.png)

**Opmerking: Het brandproces is langzaam, het duurt ongeveer 30 seconden, wees geduldig.**

Wanneer het knipperen is voltooid, selecteert u BOOT to Boot from EMMC en schakelt u ten slotte het bord in om op te starten vanuit EMMC.

# 7 Door de gebruiker geconfigureerde compilatieomgeving <a id="env_set"> </a>

Als u de bovenstaande docker-omgeving niet gebruikt, kunt u uw eigen ontwikkelomgeving configureren door te verwijzen naar de volgende opdracht op ubuntu18.04 /20.04, als u geen toestemming hebt, gebruik deze dan`sudo`.

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

**Vertaling Disclaimer**  
Voor het gemak van klanten gebruikt Canaan een AI-vertaler om tekst in meerdere talen te vertalen, wat fouten kan bevatten. Wij garanderen niet de nauwkeurigheid, betrouwbaarheid of tijdigheid van de geleverde vertalingen. Canaan is niet aansprakelijk voor enig verlies of schade veroorzaakt door het vertrouwen op de nauwkeurigheid of betrouwbaarheid van de vertaalde informatie. Als er een inhoudelijk verschil is tussen de vertalingen in verschillende talen, prevaleert de vereenvoudigd Chinese versie.

Als u een vertaalfout of onnauwkeurigheid wilt melden, neem dan gerust contact met ons op via e-mail.
