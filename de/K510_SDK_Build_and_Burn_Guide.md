![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 SDK Build- und Brennhandbuch</font>**

<font face="黑体"  size=3>Dokumentversion: V1.0.0</font>

<font face="黑体"  size=3>Veröffentlicht: 2022-03-07</font>

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

| Die Versionsnummer   | Geändert von     | Datum der Überarbeitung | Revisionshinweise |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | Geschäftsbereich KI-Produkte | 2022-03-07 |          |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Inhalt</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Einleitung

In diesem Dokument wird der Inhalt des Abschnitts zur Erstellung der Entwicklungsumgebung beschrieben, z. B. das Herunterladen, Kompilieren und Brennen des K510 SDK.

# 2 K510-SDK

## 2.1 K510 SDK herunterladen

k510 SDK-Projektadresse: <https://github.com/kendryte/k510_buildroot>

Holen Sie sich das k510 SDK:

```shell
git clone https://github.com/kendryte/k510_buildroot.git
```

## 2.2 Einführung in das K510 SDK-Gehäuse

Das K510 SDK ist eine Embedded-Linux-Entwicklungsumgebung, die auf der Buildroot als Grundgerüst basiert, basierend auf dem K510 Linux-Kernel (Linux-Version 4.17.0), u-boot (u-boot Version 2020.01), riscv-pk-k510 (BBL) Quellcode-Paket, die K510 SDK-Verzeichnisstruktur ist in der folgenden Abbildung dargestellt.

![](../zh/images/sdk_build/image-buildroot.png)

 Die K510 SDK-Dateien werden wie folgt beschrieben:

| **Datei**        | **Beschreibung des Inhalts**                                                 |
| --------------- | ------------------------------------------------------------ |
| Brett           | Ordner, der K510 verschiedene Konfigurationsdateien und Skripte ist, wie die Konfigurationsdatei zum Generieren von Images (genimage-xxx.cfg), Buildroot-Post-Image-Skripte, U-Boot-Standard-Umgebungsvariablen, etc. |
| Config.in       | Es gibt das Paket an, das eine buildroot-Kompilierung erfordert. |
| Konfigurationen         | Ordner, wobei die Standardkonfigurationsdatei für die Standardkompilierung des Boards ist. Speichert derzeit die standardmäßigen Kompilierungskonfigurationsdateien für die K510 CRB-V0.1-, K510 CRB-V1.2- und K510 EVB-Boards:<br />  --`k510_crb_lp3_v1_2_defconfig`<br />-`k510_crb_lp3_v0_1_defconfig`<br /> `k510_evb_lp3_v1_1_defconfig` |
| extern.desc   | Die Konfigurationsdatei des externen Mechanismus von Buildroot. |
| external.mk     | |
| Makefile        | Das Haupt-Makefile des k510 SDK. |
| Paket         | Ordner, bei denen es sich in erster Linie um K510-Anwendungen handelt, bestimmen Config.in Inhalt der Datei, welche Anwendungen in diesem Verzeichnis kompiliert werden. |
| Patches         | Ordner, wobei die buildroot-Patch-Datei ist, entpackt Makefile den Quellcode, wenn die Patch-Datei in diesem Verzeichnis in das entsprechende Quellcode-Verzeichnis entpackt. |
| pkg-download    | Ordner, ein komprimiertes Paket des dl-Ordners. |
| README.md       | SDK-bezogene Anweisungen. |
| release_note.md | |
| Werkzeugkette       | -Ordner, wobei die kompilierungsübergreifende Toolchain ist. |
| Dl              | Ordner, ist das dl-Extraktpaket in pkg-download, wenn andere Pakete hinzugefügt werden, wird auch in dieses Verzeichnis heruntergeladen. |

## 2.3 K510 SDK-Version

Wenn Sie das vom k510 SDK generierte Bild auf die Platine brennen, werden die Versionsinformationen gedruckt, wie in der folgenden Abbildung dargestellt:

```text
#############SDK VERSION############################################
MX2_DEV_0106-02e87077-20220428-153936CST-xxxxx-server
####################################################################
```

Geben Sie nach Abschluss des Startvorgangs Folgendes in das Shell-Terminal ein, um die SDK-Versionsinformationen anzuzeigen:

```shell
cat /etc/version/release_version
#############SDK VERSION############################################
MX2_REL_0106-02e87077-20220428-153936CST-xxxx-server
####################################################################
```

**Hinweis: Die obigen Informationen können je nach k510 SDK-Version variieren.**

# 3 Docker-Kompilierungsumgebung

Nachdem Sie das k510 sdk heruntergeladen haben, führen Sie den folgenden Befehl im übergeordneten Verzeichnis des SDK aus, um das Docker zu starten:

```shell
sh k510_buildroot/tools/docker/run_k510_docker.sh
```

Nachfolgende Kompilierungsvorgänge werden standardmäßig im Docker ausgeführt.
Wenn Sie eine lokale Umgebung einrichten müssen, lesen Sie Einrichten der[lokalen Umgebung.](#env_set)

# 4 Kompilieren

## 4.1 Vorbereitung der Zusammenstellung

### 4.1.1 Quellcode-Paket herunterladen (optional, kann die Kompilierung beschleunigen)

Führen Sie den folgenden Befehl aus, um das Quellpaket herunterzuladen:

```shell
make dl
```

## 4.2 Kompilierung

K510_buildroot/config-Verzeichnis enthält Kompilierungskonfigurationsdateien für drei Entwicklungsboards, nämlich`k510_crb_lp3_v0_1_defconfig`  , , und , wird `k510_crb_lp3_v1_2_defconfig`dieses Dokument veranschaulicht, indem k510_crb_lp3_v1_2_defconfig als Kompilierungsziel`k510_evb_lp3_v1_1_defconfig` ausgewählt **wird**.

Geben Sie in der k510 Docker-Umgebung den folgenden Befehl ein, um mit der Kompilierung zu beginnen:

```shell
make CONF=k510_crb_lp3_v1_2_defconfig
```

![](../zh/images/sdk_build/image-make.png)

Die folgende Meldung weist darauf hin, dass die Kompilierung erfolgreich abgeschlossen wurde.

![](../zh/images/sdk_build/image-uboot_r.png)

Nachdem die Kompilierung abgeschlossen ist, wird der Ordner generiert`k510_crb_lp3_v1_2_defconfig`.

![Bild-20220311121912711](../zh/images/sdk_build/image-makeout.png)

Jedes dieser Dokumente wird wie folgt beschrieben:

| **Datei**    | **Beschreibung des Inhalts**                                                 |
| ----------- | ------------------------------------------------------------ |
| Makefile    | Kompilieren Sie das Bild für die Verwendung von Makefile.                                     |
| bauen       | Das Kompilierungsverzeichnis für alle Quellpakete. Zum Beispiel, Linux-Kernel, u-boot, BBL, busybox, etc., wird der Quellcode in das Build-Verzeichnis extrahiert und kompiliert. |
| Gastgeber        | Alle Hostpaket-Installationspfade und Toolchain werden ebenfalls in dieses Verzeichnis kopiert, um kompilierungsübergreifende Umgebungen zu erstellen. |
| Bilder      | Kompilieren Sie das resultierende Zieldateiverzeichnis (weitere Informationen finden Sie in den Anweisungen unten)                     |
| nand_target | Raw-Verzeichnis des Root-Dateisystems (zum Generieren von NandFlash-Images)                  |
| Ziel      | Root-Dateisystem-Rohverzeichnis (zum Generieren von eMMC- und SD-Karten-Images für die Verwendung)                 |

K510_crb_lp3_v1_2_defconfig/images-Verzeichnis ist ein gebranntes Bild, in dem die Beschreibung jeder Datei wie folgt lautet.

| **Datei**                   | **Beschreibung des Inhalts**                                                 |
| -------------------------- | ------------------------------------------------------------ |
| bootm-bbl.img              | Linux+bbl Kernel-Image (gepackte Kernel-BPL-Zieldatei für uboot boot bbl) |
| K510.dtb                   | Gerätebaum                                                       |
| sysimage-emmc.img          | emmc burn-Dateien: Das gesamte Paket wurde uboot_burn, Kernel und bbl gepackt              |
| sysImage-sdcard.img        | SDCard-Brenndateien: Das gesamte Paket wurde uboot_burn, Kernel und BBL gepackt            |
| sysImage-nand.img          | nand burn-Dateien: Das gesamte Paket wurde uboot_burn, Kernel und bbl gepackt              |
| u-boot.bin                 | uboot-Binärdatei                                             |
| U-boot_burn.bin            | uboot brennt Dateien                                               |
| uboot-emmc.env             | uboot-Umgebungsvariable: Wird für den Emmc-Start verwendet                                  |
| uboot-sd.env               | uboot-Umgebungsvariable: Wird für den Start der SD-Karte verwendet                                |
| uboot-nand.env             | uboot-Umgebungsvariable: Wird für den nand-Start verwendet                                  |
| VMlinux                    | Linux-Kernel-Image-Datei (mit Elf-Debug-Informationen)                           |
| rootfs.ext2                | Buildroot-Format rootfs ext2 Image-Datei                             |
| sysimage-sdcard-debian.img | SDCard-Brenndateien: Karten-Images (rootfs im Debian-Format)                     |

K510_crb_lp3_v1_2_defconfig/build-Verzeichnis ist der Quellcode für alle kompilierten Objekte, von denen einige wichtige Dokumente sind, die im Folgenden beschrieben werden.

| **Datei**         | **Beschreibung des Inhalts**                  |
| ---------------- | ----------------------------- |
| linux-xxx        | Das Quellverzeichnis des kompilierten Linux-Kernels |
| uboot-xxx        | Das kompilierte Uboot-Quellverzeichnis       |
| RISCV-HP-K510-xxx| Das bbl-Quellverzeichnis, in das der Code kompiliert wird         |
| ...              |                               |

Hinweis: xxx ist die Versionsnummer. Wenn in späteren Abschnitten auf die Pfade von kernle, bbl und uboot verwiesen wird, stellen xxx alle Versionsnummern dar.

**Benötigen Sie besondere Aufmerksamkeit:** Wenn Sie eine Bereinigung vornehmen, wird alles unter dem k510_crb_lp3_v1_2_defconfig Ordner gelöscht. Wenn Sie also den Kernel-, Bbl- oder uboot-Code ändern müssen, ändern Sie ihn nicht direkt im Build-Verzeichnis, Sie können Kapitel 5 lesen, um die Override-Quellmethode zu verwenden.

## 4.1 Buildroot konfigurieren

Geben Sie den Befehl configuration buildroot in der docker-Umgebung k510 ein:

```shell
make CONF=k510_crb_lp3_v1_2_defconfig menuconfig
```

Die Ergebnisse der Ausführung sind wie folgt:

![](../zh/images/sdk_build/image-make_men.png)

![](../zh/images/sdk_build/image-make_menu.png)

Nachdem Sie die Konfiguration, das Speichern und Beenden abgeschlossen haben, müssen Sie auch den folgenden Befehl buildroot configuration save ausführen:

```shell
make CONF=k510_crb_lp3_v1_2_defconfig savedefconfig
```

Die Ergebnisse der Ausführung sind wie folgt:

![](../zh/images/sdk_build/image-make_savedef.png)

Nachdem der obige Vorgang abgeschlossen ist, kann der Benutzer den folgenden Befehl zur Neukompilierung eingeben:

```shell
make CONF=k510_crb_lp3_v1_2_defconfig
```

## 4.2 U-Boot konfigurieren

Wenn Sie die uboot-Konfiguration ändern müssen, können Sie das Verzeichnis k510_crb_lp3_v1_2_defconfig eingeben und den folgenden Befehl eingeben, um die U-Boot-Konfiguration zu starten:

```shell
make uboot-menuconfig
```

Die Ergebnisse der Ausführung sind wie folgt:

![](../zh/images/sdk_build/image-uboot_men.png)

![](../zh/images/sdk_build/image-uboot_menu.png)

Wenn Sie das menuuonfig nach Abschluss der Konfiguration beenden, wählen Sie Konfiguration speichern, und Sie müssen den folgenden Konfigurationsspeicherbefehl ausführen:

```shell
make uboot-savedefconfig
```

Die Ergebnisse der Ausführung sind wie folgt:

![](../zh/images/sdk_build/image-uboot_savedefconfig.png)

Geben Sie abschließend im Verzeichnis k510_crb_lp3_v1_2_defconfig den folgenden Befehl ein, um die Kompilierung zu starten:

```shell
make uboot-rebuild
```

Weitere Informationen finden Sie in der Beschreibung im nächsten Abschnitt.

## 4.3 U-Boot kompilieren

Der kompilierte U-Boot-Quellcode wird im Verzeichnis k510_crb_lp3_v1_2_defconfig/build/uboot-xxx gespeichert, und der U-Boot muss neu kompiliert werden, unabhängig davon, ob der Benutzer den U-Boot-Quellcode ändert oder den uboot neu konfiguriert.

Geben Sie das Verzeichnis k510_crb_lp3_v1_2_defconfig ein und geben Sie den folgenden Befehl ein, um U-Boot neu zu kompilieren:

```shell
make uboot-rebuild
```

Die Ergebnisse der Ausführung sind wie folgt:

![](../zh/images/sdk_build/image-uboot-rebuild.png)

Nachdem die Kompilierung abgeschlossen ist, wird eine neue U-Boot-.bin Datei im Verzeichnis k510_crb_lp3_v1_2_defconfig/images generiert.

Wenn Sie die gebrannte Image-Datei mit einem neuen u-boot neu generieren möchten, führen Sie`k510_crb_lp3_v1_2_defconfig` :in the directory

```shell
make
```

Die Ergebnisse der Ausführung sind wie folgt:

![](../zh/images/sdk_build/image-make_u.png)

Wenn die Kompilierung abgeschlossen ist, werden die von der folgenden Abbilddatei generierten Informationen angezeigt.

![](../zh/images/sdk_build/image-uboot_r.png)

## 4.4 Konfigurieren des Linux-Kernels

Wenn Sie die Kernelkonfiguration ändern müssen, können Sie das Verzeichnis k510_crb_lp3_v1_2_defconfig eingeben und den folgenden Befehl eingeben, um die Kernelkonfiguration zu starten:

```shell
make linux-menuconfig
```

Die Ergebnisse der Ausführung sind wie folgt:

![](../zh/images/sdk_build/image-linux_men.png)

![](../zh/images/sdk_build/image-linux_menu.png)

Wenn Sie menuufig nach dem Ändern der Konfiguration beenden, wählen Sie Konfiguration speichern aus, und führen Sie schließlich den folgenden Befehl zum Speichern der Konfiguration aus:

```shell
make linux-savedefconfig
```

Die Ergebnisse der Ausführung sind wie folgt:

![](../zh/images/sdk_build/image-linux_savedefconfig.png)

Geben Sie abschließend im Verzeichnis k510_crb_lp3_v1_2_defconfig den folgenden Befehl ein, um die Kompilierung zu starten:

```shell
make linux-rebuild
```

Weitere Informationen finden Sie in der Beschreibung im nächsten Abschnitt.

## 4.5 Kompilieren Sie den Linux-Kernel

K510_crb_lp3_v1_2_defconfig/build/linux-xxx-Verzeichnis enthält den kompilierten Linux-Quellcode, unabhängig davon, ob der Benutzer den Linux-Quellcode ändert oder das Linux neu konfiguriert, muss es neu kompiliert werden.

Geben Sie das Verzeichnis k510_crb_lp3_v1_2_defconfig ein und geben Sie den folgenden Befehl ein, um Linux neu zu kompilieren:

```shell
make linux-rebuild
```

Die Ergebnisse der Ausführung sind wie folgt:

![](../zh/images/sdk_build/image-linux_rebuild.png)

Nach dem Kompilieren wird im Verzeichnis k510_crb_lp3_v1_2_defconfig/images ein neues vmlinux generiert.

Linux-Kernel-Image muss mit bbl gepackt werden, nachdem Sie den Linux-Kernel neu geschrieben haben, müssen Sie die bbl neu kompilieren, um ein neues bbl / kernel-Image für you-boot-boot zu generieren, also geben Sie die folgenden beiden Befehle ein.

```shell
make riscv-pk-k510-dirclean
make riscv-pk-k510
```

Die Ergebnisse der Ausführung sind wie folgt:

![](../zh/images/sdk_build/image-riscv.png)

Wenn die Kompilierung abgeschlossen ist, wird eine`k510_crb_lp3_v1_2_defconfig/images` neue im Verzeichnis generiert`bootm-bbl.img`.

Geben Sie abschließend make in das Verzeichnis k510_crb_lp3_v1_2_defconfig ein und verwenden Sie das neue Paket bootm-bbl.img, um emmc- und SD-Karten-Image-Dateien zu generieren.

```shell
make
```

Die Ergebnisse der Ausführung sind wie folgt:

![](../zh/images/sdk_build/image-make_u.png)

Wenn die Kompilierung abgeschlossen ist, werden die von der folgenden Abbilddatei generierten Informationen angezeigt.

![](../zh/images/sdk_build/image-uboot_r.png)

## 4.6 dts kompilieren

Die Gerätestrukturdatei befindet sich im Verzeichnis k510_buildroot/k510_crb_lp3_v1_2_defconfig/build/linux-4.17/arch/riscv/boot/dts/canaan, und wenn der Benutzer nur die Gerätestruktur ändert, kann nur die Gerätestruktur kompiliert und dekompiliert werden.

Schreiben Sie ein mkdtb-local.sh Skript, das wie folgt lautet:

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

Platzieren Sie die mkdtb-local.sh im Verzeichnis K510_buildroot und führen Sie den folgenden Befehl aus, um den Gerätebaum der k510_crb_lp3_v1_2_defconfig-Platine zu kompilieren:

```shell
./mkdtb-local.sh k510_crb_lp3_v1_2_defconfig
```

Die Ergebnisse der Ausführung sind wie folgt:

![](../zh/images/sdk_build/image-mdk_dts.png)

K510.dtb im Verzeichnis k510_crb_lp3_v1_2_defconfig/images ist die neu generierte Gerätestruktur-Datenbankdatei, und all.dts ist die dekompilierte Gerätestrukturdatei.

## 4.7 Kompilieren der App

Benutzer können sich auf `package/hello_world` das Schreiben von Config.in- und Makefile-Dateien beziehen, um ihre eigenen Anwendungen zu erstellen, und die Benutzeranwendungen werden im Verzeichnis k510_buildroot/package abgelegt.

Der Prozess der Kompilierung einer Anwendung wird veranschaulicht, indem hello_world Projekte als Beispiel in k510_buildroot/package platziert werden.

Ändern Sie die Config.in Dateien im Verzeichnis k510_buildroot in der Hostumgebung.

![](../zh/images/sdk_build/image-vi_config.png)

Fügen Sie im Config.in den Pfad hinzu, in dem sich package/hello_world/Config.in befindet, und speichern Sie ihn.

![](../zh/images/sdk_build/image-config_list.png)

Geben Sie den Befehl configuration buildroot in der docker-Umgebung k510 ein:

```shell
make CONF=k510_crb_lp3_v1_2_defconfig menuconfig
```

Die Ergebnisse der Ausführung sind wie folgt:

![](../zh/images/sdk_build/image-build_menu.png)

Die Konfigurationsseite buildroot wird angezeigt, wählen Sie die Option Erweitert aus, wählen Sie schließlich die hello_world aus und speichern und beenden Sie sie.

![](../zh/images/sdk_build/image-extern_option.png)

Geben Sie im Verzeichnis k510_buildroot den Befehl Konfiguration speichern ein.

```shell
make CONF=k510_crb_lp3_v1_2_defconfig savedefconfig
```

Die Ergebnisse der Ausführung sind wie folgt:

![](../zh/images/sdk_build/image-build_savedef.png)

1) Wenn es das erste Mal ist, es zu kompilieren, sind die Schritte wie folgt:

    Geben Sie im Verzeichnis k510_buildroot den folgenden Befehl ein, um das gesamte Projektprogramm zu kompilieren und hello in emmc- und SD-Kartenbilddateien zu verpacken.

    ```shell
    make CONF=k510_crb_lp3_v1_2_defconfig
    ```

    Die Ergebnisse der Ausführung sind wie folgt:

    ![](../zh/images/sdk_build/image-build_make_def.png)

    Im Verzeichnis k510_buildroot/k510_crb_lp3_v1_2_defconfig/target sehen Sie die resultierende hello-Anwendung, die angibt, ob die Anwendung korrekt kompiliert wurde.

    ![](../zh/images/sdk_build/image-hello.png)

2) Wenn es kompiliert wurde, kompilieren Sie einfach die App und verpacken Sie es in das Brennbild, folgen Sie diesen Schritten:

    Geben Sie das Verzeichnis k510_buildroot/k510_crb_lp3_v1_2_defconfig ein und geben Sie den folgenden Befehl ein, um die hello-Anwendung zu kompilieren.

    ```shell
    make hello_world-rebuild
    ```

    Die Ergebnisse der Ausführung sind wie folgt:

    ![](../zh/images/sdk_build/image-app_build-1.png)

    Gehen Sie in das Verzeichnis k510_buildroot/k510_crb_lp3_v1_2_defconfig und geben Sie den Befehl make ein, um hello in die emmc- und sd-Kartenbilddateien zu packen.

    ```shell
    make
    ```

    Die Ergebnisse der Ausführung sind wie folgt:

    ![](../zh/images/sdk_build/image-app-build-2.png)

# 5 Entwickeln mit dem K510 SDK

## 5.1 Linux-Kernel/BBL/uboot-Quellcode

Die von diesem SDK verwendete uboot-Version ist 2020.01, das uboot-Patch-Verzeichnis ist package/patches/uboot und das Verzeichnis nach dem Patchen ist k510_xxx_defconfig/build/uboot-2020.01.

Das von diesem SDK verwendete Kernel-Patch-Verzeichnis ist 4.17, das Kernel-Patch-Verzeichnis ist package/patches/linux und das gepatchte Verzeichnis ist k510_xxx_defconfig/build/linux-4.17.

Die BBL dieses SDK wird als Zielpaket im Verzeichnis package/riscv-pk-k510/ abgelegt, und die Quell- und Versionsnummer der bbl werden im riscv-pk-k510.mk angegeben:

```text
RISCV_PK_K510_VERSION = 1e666d6c5dbab220d2ca57fbd9bec49702599b75
RISCV_PK_K510_SITE = git@github.com:kendryte/k510_BBL.git
RISCV_PK_K510_SITE_METHOD = git
```

## 5.2 Linux-Kernel/BBL/uboot entwickeln

Jede unter Buildroot kompilierte Befriedung, einschließlich Linux-Kernel / BBL / uboot, wird durch Herunterladen von Tarball, Dekomprimieren, Konfigurieren, Kompilieren, Installieren und andere einheitliche Paketverwaltungsschritte implementiert, so dass, obwohl der gesamte Quellcode im Verzeichnis k510_buildroot / k510_crb_lp3_v1_2_defconfig / build angezeigt werden kann, keine Versionskontrollinformationen vorhanden sind. Auch wenn der Code aus einem Git-Repository heruntergeladen wird.

Obwohl der Kernel/BBL/uboot-Quellcode, der die Git-Repository-Daten enthält, im dl/directory zu sehen ist, speichert buildroot nur den Quellcode im dl-Verzeichnis und es wird nicht empfohlen, direkt in diesem Verzeichnis zu entwickeln.

Für das Entwicklungsmodell bietet buildroot eine Möglichkeit, OVERRIDE_SRCDIR.

In einfachen Worten können Sie eine local.mk Datei unter dem Verzeichnis k510_crb_lp3_v1_2_defconfig hinzufügen und hinzufügen:

```text
<pkg1>_OVERRIDE_SRCDIR = /path/to/pkg1/sources
```

- LINUX ist der Paketname des Kernels
- UBOOT ist der PAKETNAME von uboot
- RISCV_PK_K510 ist der Paketname der BBL

Nehmen wir den Linux-Kernel als Beispiel, um zu beschreiben, wie man ihn benutzt.
Angenommen, ich habe den Kernel-Code im Verzeichnis /data/yourname/workspace/k510_linux_kernel geklont und Änderungen vorgenommen und möchte unter buildroot kompilieren und auf dem crb v1.2-Board testen, können Sie eine local.mk im k510_crb_lp3_v1_2_defconfig-Verzeichnis erstellen und Folgendes hinzufügen:

```text
LINUX_OVERRIDE_SRCDIR = /data/yourname/workspace/k510_linux_kernel
```

Im Verzeichnis k510_crb_lp3_v1_2_defconfig ausführen

```shell
make linux-rebuild
```

Sie können sehen, dass der Kernel im Verzeichnis build/linux-custom mit dem geänderten Code unter /data/yourname/workspace/k510_linux_kernel neu kompiliert wurde.
UBOOT und BBL sind ähnlich. Auf diese Weise können Sie den Kernelcode direkt ändern und den Kernel unter buildroot neu schreiben und das zu testende Image inkrementell kompilieren.
Hinweis: Der Quellcode der Außerkraftsetzung wird dem Suffix custom im Verzeichnisnamen des Verzeichnisses k510_crb_lp3_v1_2_defconfig/build hinzugefügt, um die Quelle jedes Pakets in der Standardkonfiguration von buildroot zu unterscheiden. Im obigen Beispiel des Linux-Kernels sieht die Kompilierung beispielsweise, dass der von der Overrideide angegebene Code im Verzeichnis k510_crb_lp3_v1_2_defconfig/build/linux-custom kompiliert wird und nicht im Verzeichnis k510_crb_lp3_v1_2_defconfig/build/linux-xxx, das wir zuvor gesehen haben.

Für anderen Code im Paketverzeichnis oder native buildroot-Pakete ist es möglich, auf diese Weise unter dem buildroot-Framework zu entwickeln.

# 6 Brennen Sie das Bild

K510 unterstützt den sdcard- und eMMC-Boot-Modus, jedes Mal, wenn beim Kompilieren im Verzeichnis k510_buildroot/k510_crb_lp3_v1_2_defconfig/image die Image-Dateien sysimage-sdcard.img und sysimg-emmc.img generiert werden, können die beiden Dateien auf sdcard bzw. eMMC gebrannt werden.

Der K510 bestimmt den Chip-Boot-Modus durch den Status der Boot0- und BOOT1-Hardware-Pins, bitte beachten Sie den Boot-Tutorial-Abschnitt des Entwicklungsboards für spezifische Einstellungen.

| BOOT1   | BOOT0   | Startmodus      |
| ------- | ------- | ------------ |
| 0(EIN)   | 0(EIN)   | Booten der seriellen Schnittstelle      |
| 0(EIN)   | 1(AUS)  | Die SD-Karte bootet      |
| 1(AUS)  | 0(EIN)   | NANDFLASH-Stiefel |
| 1(AUS)  | 1(AUS)  | EMMC-Stiefel      |

![](../zh/images/hw_crb_v1_2/clip_hw_3_9.jpg)

## 6.1 Brennen Sie das Image auf die SD-Karte

### 6.1.1 ubuntu verbrannt

Geben Sie vor dem Einsetzen der SD-Karte in den Host Folgendes ein:

```shell
ls -l /dev/sd*
```

Zeigen Sie das aktuelle Speichergerät an.

Nachdem Sie die sD-Karte in den Host eingelegt haben, geben Sie sie erneut ein:

```shell
ls -l /dev/sd*
```

Wenn man sich das Speichergerät zu diesem Zeitpunkt ansieht, ist die neue Ergänzung der SD-Kartengeräteknoten.

Nach dem Einsetzen der sD-Karte in den Host lautet das Ergebnis der Ausführung des ls-Befehls wie folgt:

![](../zh/images/sdk_build/image-dev_sd.png)

/dev/sdc ist der Geräteknoten der SD-Karten. **Hinweis: Der in der Benutzerumgebung generierte SD-Kartengeräteknoten ist möglicherweise nicht /dev/sdc, und nachfolgende Operationen müssen entsprechend dem tatsächlichen Knoten geändert werden.**

Geben Sie das Verzeichnis k510_buildroot/k510_crb_lp3_v1_2_defconfig/image unter dem Host ein und geben Sie den Befehl dd ein, um sysimage-sdcard.img in das SDK zu brennen:

```shell
sudo dd if=sysimage-sdcard.img of=/dev/sdc bs=1M oflag=sync
```

Das Ausführungsergebnis unter dem Host lautet wie folgt:

![](../zh/images/sdk_build/image-dd.png)

### 6.1.2 Brennen unter Windows

Unter Windows kann die sD-Karte mit dem Bananen-Etcher-Tool gebrannt werden (Balena Etcher Tool Download-Adresse<https://www.balena.io/etcher/>).

1) Legen Sie die TF-Karte in den PC ein, starten Sie dann das ColumnEtcher-Tool, klicken Sie auf die Schaltfläche "Flash from file" der Tool-Schnittstelle, wählen Sie die zu brennende Firmware aus, wie in der folgenden Abbildung gezeigt.

    ![](../zh/images/sdk_build/image-sd_pre0.png)

2) Klicken Sie auf die Schaltfläche "Ziel auswählen" der Werkzeugoberfläche und wählen Sie die Ziel-SD-Karte aus.

    ![](../zh/images/sdk_build/image-pre1.png)

3) Klicken Sie auf die Schaltfläche "Flash", um mit dem Blinken zu beginnen, der Blinkvorgang hat eine Fortschrittsanzeige, Flash Finish wird nach dem Ende des Blinkens aufgefordert.

    | ![](../zh/images/sdk_build/clip_image_p1.jpg) | ![](../zh/images/sdk_build/clip_image_p2.jpg) |
    | --------------------------------------- | --------------------------------------- |
    |                                         |                                         |

4) Wenn das Flashen abgeschlossen ist, setzen Sie die SD-Karte in den Steckplatz der Entwicklungsplatine ein, wählen Sie BOOT, um von der SD zu starten, und schließlich kann die Entwicklungsplatine eingeschaltet werden, um von der SD-Karte zu starten.

## 6.2 Brennen Sie das Image auf emmc

Um die sysimage-emmc.img mit Hilfe des SDK in der ubuntu-Umgebung auf die integrierte eMMC zu brennen, wird die sysimage-emmc.img in der Benutzerpartition des SDK gespeichert, und dann wird das SDK in das Board eingefügt und eingeschaltet.

Bevor Sie das emmc-Image brennen, müssen Sie das emmc-bezogene Dateisystem aushängen, siehe die folgenden Schritte, um es zu enthängen.

```shell
mount | grep emmc
```

Das Ausführungsergebnis lautet wie folgt:

![](../zh/images/sdk_build/image-emmc_1.png)

Geben Sie den folgenden Befehl ein, um zu deinstallieren und zu überprüfen.

```shell
umount /root/emmc/p2
umount /root/emmc/p3
umount /root/emmc/p4
mount | grep emmc
```

Das Ausführungsergebnis lautet wie folgt:

![](../zh/images/sdk_build/image-emmc_2.png)

Geben Sie abschließend den Pfad ein, in dem sich das Image befindet, und geben Sie den folgenden Befehl ein, um eMMC zu brennen.

```shell
dd if=sysimage-emmc.img of=/dev/mmcblk0 bs=1M
```

Das Ausführungsergebnis lautet wie folgt:

![](../zh/images/sdk_build/image-emmc3.png)

**Hinweis: Der Brennvorgang ist langsam, es dauert etwa 30 Sekunden, bitte haben Sie etwas Geduld.**

Wenn das Flashen abgeschlossen ist, wählen Sie BOOT, um von EMMC zu booten, und schalten Sie schließlich das Board ein, um von EMMC zu booten.

# 7 Benutzerkonfigurierte Kompilierungsumgebung <a id="env_set"> </a>

Wenn Sie die obige Docker-Umgebung nicht verwenden, können Sie Ihre eigene Entwicklungsumgebung konfigurieren, indem Sie sich auf den folgenden Befehl unter ubuntu18.04 / 20.04 beziehen, wenn Sie keine Berechtigung haben, verwenden Sie sie bitte.`sudo`  

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

**Haftungsausschluss**für Übersetzungen  
Für die Bequemlichkeit der Kunden verwendet Canaan einen KI-Übersetzer, um Text in mehrere Sprachen zu übersetzen, die Fehler enthalten können. Wir übernehmen keine Gewähr für die Genauigkeit, Zuverlässigkeit oder Aktualität der bereitgestellten Übersetzungen. Canaan haftet nicht für Verluste oder Schäden, die durch das Vertrauen auf die Richtigkeit oder Zuverlässigkeit der übersetzten Informationen verursacht werden. Wenn es einen inhaltlichen Unterschied zwischen den Übersetzungen in verschiedenen Sprachen gibt, ist die vereinfachte chinesische Version maßgebend.

Wenn Sie einen Übersetzungsfehler oder eine Ungenauigkeit melden möchten, können Sie uns gerne per E-Mail kontaktieren.
