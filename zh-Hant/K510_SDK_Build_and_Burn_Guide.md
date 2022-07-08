![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 SDK 構建和刻錄指南</font>**

<font face="黑体"  size=3>文件版本：V1.0.0</font>

<font face="黑体"  size=3>發佈日期：2022-03-07</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**免責聲明**</font>
您購買的產品、服務或特性等應受北京嘉楠捷思資訊技術有限公司（“本公司”，下同）商業合同和條款的約束，本文檔中描述的全部或部分產品、服務或特性可能不在您的購買或使用範圍之內。 除非合同另有約定，本公司不對本文檔的任何陳述、資訊、內容的準確性、可靠性、完整性、行銷型、特定目的性和非侵略性提供任何明示或默示的聲明或保證。 除非另有約定，本文檔僅作為使用指導的參考。
由於產品版本升級或其他原因，本文檔內容將可能在未經任何通知的情況下，不定期進行更新或修改。

**<font face="黑体"  size=3>商標聲明</font>**

“<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />”、“Canaan”圖示、嘉楠和嘉楠其他商標均為北京嘉楠捷思資訊技術有限公司的商標。 本文檔可能提及的其他所有商標或註冊商標，由各自的所有人擁有。

**<font face="黑体"  size=3>版權所有©2022北京嘉楠捷思資訊技術有限公司</font>**
本文檔僅適用K510平台開發設計，非經本公司書面許可，任何單位和個人不得以任何形式對本文檔的部分或全部內容傳播。

**<font face="黑体"  size=3>北京嘉楠捷思資訊技術有限公司</font>**
網址：canaan-creative.com
商務垂詢：salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# 前言
**<font face="黑体"  size=5>文件目的</font>**
本文檔為K510 sdk的配套文檔，旨在幫助工程師瞭解 k510 sdk的編譯和燒錄。

**<font face="黑体"  size=5>讀者物件</font>**

本文檔（本指南）主要適用的人員：

- 軟體開發人員
- 技術支持人員

**<font face="黑体"  size=5>修訂記錄</font>**
 <font face="宋体"  size=2>修訂記錄累積了每次文檔更新的說明。 最新版本的文件包含以前所有版本的更新內容。 </font>

| 版本號   | 修改者     | 修訂日期 | 修訂說明 |
|  :-----  |-------   |  ------  |  ------  |
| 1.0.0 版 | AI 產品部 | 2022-03-07 |          |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>目 錄</font>**

[目錄]

<div style="page-break-after:always"></div>

# 1 簡介

本文檔介紹K510 SDK的下載、編譯和燒錄等開發環境搭建部分的內容。

# 2 k510 開發工具包

## 2.1 k510 sdk下載

k510 SDK 專案位址： <https://github.com/kendryte/k510_buildroot>

取得k510 SDK：

```shell
git clone https://github.com/kendryte/k510_buildroot.git
```

## 2.2 k510 sdk軟體包介紹

K510 SDK是以buildroot為基本框架，以K510 linux kernel（linux版本4.17.0），u-boot（u-boot版本2020.01），riscv-pk-k510（BBL）源碼包為基礎構建的嵌入式Linux開發環境，K510 SDK目錄結構如下圖所示。

![](../zh/images/sdk_build/image-buildroot.png)

 K510 SDK各檔描述如下：

| **檔**        | **內容描述**                                                 |
| --------------- | ------------------------------------------------------------ |
| 板           | 資料夾，其是K510各種配置檔和腳本，如生成鏡像的配置檔（genimage-xxx.cfg），buildroot的post-image腳本，U-Boot默認環境變數等。 |
| Config.in       | 其中內容指示了需要buildroot編譯的package。 |
| 配置         | 資料夾，其中是開發板預設編譯配置檔。 目前保存有K510 CRB-V0.1、K510 CRB-V1.2和K510 EVB三塊板的默認編譯配置檔：<br />- `k510_crb_lp3_v1_2_defconfig`<br />- `k510_crb_lp3_v0_1_defconfig`<br />- `k510_evb_lp3_v1_1_defconfig` |
| external.desc   | buildroot的external機制配置檔。 |
| external.mk     | |
| 製作檔        | k510 SDK的主Makefile。 |
| 包         | 資料夾，其中主要是K510 應用程式，Config.in 檔中的內容將決定該目錄下哪些應用程式被編譯。 |
| 補丁         | 資料夾，其中是buildroot的補丁檔，Makefile在解壓源碼的時候會將此目錄下的補丁檔打到相應源碼目錄。 |
| pkg-download    | 資料夾，其中是dl資料夾的壓縮包。 |
| README.md       | sdk 相關說明。 |
| release_note.md | |
| 工具鏈       | 資料夾，其中是交叉編譯工具鏈。 |
| 分升              | 資料夾，是pkg-download中的dl 解壓縮包，如果有添加其它包也會下載到該目錄下。 |

## 2.3 k510 sdk版本

把k510 sdk編譯生成的鏡像燒錄到板上啟動時，會列印版本資訊，如下圖所示：

```text
#############SDK VERSION############################################
MX2_DEV_0106-02e87077-20220428-153936CST-xxxxx-server
####################################################################
```

啟動完成以後，在shell終端輸入如下可以查看 sdk版本資訊：

```shell
cat /etc/version/release_version
#############SDK VERSION############################################
MX2_REL_0106-02e87077-20220428-153936CST-xxxx-server
####################################################################
```

**注： k510 sdk版本不同，上面的資訊可能不同**。

# 3 docker 編譯環境

下載完k510 sdk後，在sdk上級目錄執行以下命令啟動docker：

```shell
sh k510_buildroot/tools/docker/run_k510_docker.sh
```

後續編譯操作預設都在docker中執行。
如果需要搭建本地環境請參考[本地環境搭建](#env_set)

# 4 編譯

## 4.1編譯準備

### 4.1.1下載源碼包（可選，可以加速編譯）

執行以下命令下載來源碼包：

```shell
make dl
```

## 4.2編譯

k510_buildroot/config 目錄下有三個開發板的編譯配置檔，分別是`k510_crb_lp3_v0_1_defconfig` 、`k510_crb_lp3_v1_2_defconfig`和`k510_evb_lp3_v1_1_defconfig`， **本文檔以選擇 k510_crb_lp3_v1_2_defconfig 作為編譯目標來說明**。

在k510 docker環境下輸入如下命令啟動編譯：

```shell
make CONF=k510_crb_lp3_v1_2_defconfig
```

![](../zh/images/sdk_build/image-make.png)

輸出如下資訊表示編譯成功完成。

![](../zh/images/sdk_build/image-uboot_r.png)

在編譯完成後，會生成`k510_crb_lp3_v1_2_defconfig`資料夾。

![圖片-20220311121912711](../zh/images/sdk_build/image-makeout.png)

其中各檔描述如下：

| **檔**    | **內容描述**                                                 |
| ----------- | ------------------------------------------------------------ |
| 製作檔    | 編譯鏡像使用的Makefile。                                     |
| 建       | 所有源碼包的編譯目錄。 例如linux kernel，u-boot，BBL，busybox等，源碼都會解壓到build目錄下並編譯。 |
| 主機        | 所有host package的安裝路徑，toolchain也會拷貝至此目錄下，用於構建交叉編譯環境。 |
| 圖像      | 編譯生成的目標檔目錄（詳見下面的說明）                     |
| nand_target | 根檔案系統原始目錄（產生NandFlash鏡像使用）                  |
| 目標      | 根檔案系統原始目錄（生成eMMC和SD卡鏡像使用）                 |

k510_crb_lp3_v1_2_defconfig/images目錄下是燒錄鏡像，其中各個文件的說明如下。

| **檔**                   | **內容描述**                                                 |
| -------------------------- | ------------------------------------------------------------ |
| bootm-bbl.img              | Linux+bbl內核鏡像（打包過內核的bbl目標檔，用於uboot引導bbl） |
| k510.dtb                   | 設備樹                                                       |
| sysimage-emmc.img          | emmc燒錄檔：已整個打包uboot_burn、kernel和bbl              |
| sysImage-sdcard.img        | sdcard燒錄檔：已整個打包uboot_burn、kernel和bbl            |
| sysImage-nand.img          | nand燒錄檔：已整個打包uboot_burn、kernel和bbl              |
| u-boot.bin                 | uboot 二進位檔                                             |
| u-boot_burn.bin            | uboot 燒錄檔                                               |
| uboot-emmc.env             | uboot環境變數：用於emmc啟動                                  |
| uboot-sd.env               | uboot環境變數：用於sdcard啟動                                |
| uboot-nand.env             | uboot環境變數：用於nand啟動                                  |
| vmlinux                    | Linux內核鏡像檔（帶elf調試資訊）                           |
| rootfs.ext2                | buildroot格式rootfs ext2鏡像檔                             |
| sysimage-sdcard-debian.img | sdcard燒錄檔：卡鏡像（debian格式rootfs）                     |

k510_crb_lp3_v1_2_defconfig/build 目錄下是所有被編譯物件的源碼，其中幾個重要的文件說明如下。

| **檔**         | **內容描述**                  |
| ---------------- | ----------------------------- |
| linux-xxx        | 被編譯的Linux kernel源碼目錄 |
| uboot-xxx        | 被編譯的Uboot源碼目錄       |
| riscv-hp-k510-xxx| 被編譯的 bbl 源碼目錄         |
| ...              |                               |

注： xxx是版本號。 後面章節引用kernle，bbl和uboot的路徑時，xxx均表示版本號。

**需要特別注意：**當make clean 的時候，k510_crb_lp3_v1_2_defconfig資料夾下所有內容將被刪除。 所以，如果需要修改kernel、bbl或者uboot代碼，不要直接在build目錄下修改，可以參考第5章內容，使用override source的方式。

## 4.1 配置 buildroot

在k510 docker環境下輸入配置 buildroot命令：

```shell
make CONF=k510_crb_lp3_v1_2_defconfig menuconfig
```

執行結果如下：

![](../zh/images/sdk_build/image-make_men.png)

![](../zh/images/sdk_build/image-make_menu.png)

完成配置后保存並退出，還需要執行如下buildroot配置保存命令：

```shell
make CONF=k510_crb_lp3_v1_2_defconfig savedefconfig
```

執行結果如下：

![](../zh/images/sdk_build/image-make_savedef.png)

以上操作完成後，用戶可輸入如下命令重新編譯：

```shell
make CONF=k510_crb_lp3_v1_2_defconfig
```

## 4.2 配置 U-Boot

當使用者需要對 uboot 配置進行修改，可進入k510_crb_lp3_v1_2_defconfig目錄， 輸入如下命令啟動 U-Boot 配置：

```shell
make uboot-menuconfig
```

執行結果如下：

![](../zh/images/sdk_build/image-uboot_men.png)

![](../zh/images/sdk_build/image-uboot_menu.png)

完成配置后退出menuconfig時，選擇保存配置，還需要執行如下配置保存命令：

```shell
make uboot-savedefconfig
```

執行結果如下：

![](../zh/images/sdk_build/image-uboot_savedefconfig.png)

最後在k510_crb_lp3_v1_2_defconfig目錄，輸入如下命令啟動編譯：

```shell
make uboot-rebuild
```

詳細信息見下一節的描述。

## 4.3 編譯 U-Boot

k510_crb_lp3_v1_2_defconfig/build/uboot-xxx 目錄下保存有被編譯的U-Boot源碼，無論是使用者對 U-Boot原始程式碼進行了修改，還是對uboot 進行了重新配置，都需要重新編譯U-Boot。

進入k510_crb_lp3_v1_2_defconfig目錄，輸入如下命令重新編譯 U-Boot：

```shell
make uboot-rebuild
```

執行結果如下：

![](../zh/images/sdk_build/image-uboot-rebuild.png)

編譯完成後，會在k510_crb_lp3_v1_2_defconfig/images目錄下生成新的 u-boot.bin 檔。

如果要用新u-boot重新生成燒錄鏡像檔，在`k510_crb_lp3_v1_2_defconfig`目錄下執行：

```shell
make
```

執行結果如下：

![](../zh/images/sdk_build/image-make_u.png)

編譯完成會看到如下鏡像檔生成的資訊。

![](../zh/images/sdk_build/image-uboot_r.png)

## 4.4 配置 Linux kernel

當使用者需要對 kernel 設定進行修改，可進入k510_crb_lp3_v1_2_defconfig目錄， 輸入如下命令啟動 kernel 配置：

```shell
make linux-menuconfig
```

執行結果如下：

![](../zh/images/sdk_build/image-linux_men.png)

![](../zh/images/sdk_build/image-linux_menu.png)

修改配置後退出menuconfig時，選擇保存配置，最後還需要執行如下配置保存命令：

```shell
make linux-savedefconfig
```

執行結果如下：

![](../zh/images/sdk_build/image-linux_savedefconfig.png)

最後在k510_crb_lp3_v1_2_defconfig目錄，輸入如下命令啟動編譯：

```shell
make linux-rebuild
```

詳細信息見下一節的描述。

## 4.5 編譯Linux kernel

k510_crb_lp3_v1_2_defconfig/build/linux-xxx 目錄下保存有被編譯的linux源碼，無論是使用者對 linux 原始碼進行了修改，還是對linux 進行了重新配置，都需要重新編譯linux 。

進入k510_crb_lp3_v1_2_defconfig目錄，輸入如下命令重新編譯 linux：

```shell
make linux-rebuild
```

執行結果如下：

![](../zh/images/sdk_build/image-linux_rebuild.png)

編譯完成後會在k510_crb_lp3_v1_2_defconfig/images目錄下生成新的vmlinux。

linux kernel鏡像需要用bbl打包，重編linux kernel后，需要重編bbl生成新的bbl/kernel鏡像用於u-boot引導，因此輸入如下兩條命令。

```shell
make riscv-pk-k510-dirclean
make riscv-pk-k510
```

執行結果如下：

![](../zh/images/sdk_build/image-riscv.png)

編譯完成，會在`k510_crb_lp3_v1_2_defconfig/images`目錄下生成新的`bootm-bbl.img`。

最後在k510_crb_lp3_v1_2_defconfig目錄下輸入make，用新的bootm-bbl.img打包生成emmc和sd卡鏡像檔。

```shell
make
```

執行結果如下：

![](../zh/images/sdk_build/image-make_u.png)

編譯完成會看到如下鏡像檔生成的資訊。

![](../zh/images/sdk_build/image-uboot_r.png)

## 4.6 編譯 dts

設備樹檔位於 k510_buildroot/k510_crb_lp3_v1_2_defconfig/build/linux-4.17/arch/riscv/boot/dts/canaan 目錄下，當使用者只修改了設備樹，可只對設備樹進行編譯和反編譯。

編寫一個 mkdtb-local.sh 腳本，其中的內容為：

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

將 mkdtb-local.sh 放到 K510_buildroot 目錄下，執行如下命令即可對 k510_crb_lp3_v1_2_defconfig板設備樹進行編譯：

```shell
./mkdtb-local.sh k510_crb_lp3_v1_2_defconfig
```

執行結果如下：

![](../zh/images/sdk_build/image-mdk_dts.png)

編譯完成在k510_crb_lp3_v1_2_defconfig/images目錄下的 k510.dtb是新生成的設備樹資料庫檔，all.dts是反編譯后的設備樹檔。

## 4.7 編譯 app

用戶可參考 `package/hello_world` 中 Config.in 和makefile檔寫法，構建自己的應用程式，使用者應用程式放置到 k510_buildroot/package 目錄下。

這裡以將 hello_world 工程放置到 k510_buildroot/package 為例，來說明編譯應用程式的過程。

在宿主機環境下修改k510_buildroot目錄下的 Config.in 檔。

![](../zh/images/sdk_build/image-vi_config.png)

在 Config.in 中添加package/hello_world/Config.in所在的路徑並保存。

![](../zh/images/sdk_build/image-config_list.png)

在 k510 docker環境下輸入設定 buildroot命令：

```shell
make CONF=k510_crb_lp3_v1_2_defconfig menuconfig
```

執行結果如下：

![](../zh/images/sdk_build/image-build_menu.png)

出現buildroot配置頁面，選擇External option，最後選中其中的hello_world后保存退出。

![](../zh/images/sdk_build/image-extern_option.png)

在k510_buildroot目錄下輸入保存配置命令。

```shell
make CONF=k510_crb_lp3_v1_2_defconfig savedefconfig
```

執行結果如下：

![](../zh/images/sdk_build/image-build_savedef.png)

1）若是第一次編譯，執行步驟如下：

在k510_buildroot目錄下，輸入如下命令編譯整個項目程式，並將hello打包到emmc和sd卡鏡像文件當中。

```shell
make CONF=k510_crb_lp3_v1_2_defconfig
```

執行結果如下：

![](../zh/images/sdk_build/image-build_make_def.png)

在k510_buildroot/k510_crb_lp3_v1_2_defconfig/target 目錄下，可以看到生成的hello應用程式，由此可判斷應用程式是否被正確編譯。

![](../zh/images/sdk_build/image-hello.png)

2）若已經編譯過，只是對app進行編譯並打包到燒錄鏡像中，執行步驟如下：

進入到 k510_buildroot/k510_crb_lp3_v1_2_defconfig目錄下，輸入如下命令編譯 hello應用程式。

```shell
make hello_world-rebuild
```

執行結果如下：

![](../zh/images/sdk_build/image-app_build-1.png)

進入到 k510_buildroot/k510_crb_lp3_v1_2_defconfig目錄下，輸入make命令將hello打包到emmc和sd卡鏡像檔當中。

```shell
make
```

執行結果如下：

![](../zh/images/sdk_build/image-app-build-2.png)

# 5 使用K510 SDK進行開發

## 5.1 linux kernel/BBL/uboot源碼

本sdk使用的uboot版本是2020.01，uboot補丁目錄是package/patches/uboot，打完補丁后的目錄是k510_xxx_defconfig/build/uboot-2020.01。

本sdk使用的kernel版本是4.17，kernel補丁目錄是package/patches/linux，打完補丁后的目錄是k510_xxx_defconfig/build/linux-4.17。

本sdk的 BBL作為一個target package，放在package/riscv-pk-k510/目錄下，riscv-pk-k510.mk 中指定了bbl的代碼源和版本號：

```text
RISCV_PK_K510_VERSION = 1e666d6c5dbab220d2ca57fbd9bec49702599b75
RISCV_PK_K510_SITE = git@github.com:kendryte/k510_BBL.git
RISCV_PK_K510_SITE_METHOD = git
```

## 5.2 開發linux kernel/BBL/uboot

Buildroot下編譯的每一個pacakge，包括linux kernel/BBL/uboot，都是通過下載tarball，解壓，配置，編譯，安裝等統一的包管理步驟來實現的，因此在k510_buildroot/k510_crb_lp3_v1_2_defconfig/build目錄下雖然可以看到全部的源碼，但是都沒有版本控制資訊， 即使代碼是從git 倉庫下載的。

雖然在dl/目錄下可以看到包含了git倉庫數據的kernel/BBL/uboot源碼，但是buildroot僅僅把dl目錄下的源碼作為緩存，不建議直接在這個目錄的進行開發。

針對開發模式，buildroot提供了OVERRIDE_SRCDIR的方式。

簡單來說就是可以在k510_crb_lp3_v1_2_defconfig目錄下添加一個 local.mk 檔，在裡面添加：

```text
<pkg1>_OVERRIDE_SRCDIR = /path/to/pkg1/sources
```

- LINUX 是kernel的package name
- UBOOT 是uboot的PACKAGE name
- RISCV_PK_K510 是bbl的package name

我們以linux kernel為例，介紹如何使用。
假設我已經在/data/yourname/workspace/k510_linux_kernel目錄下clone了kernel的代碼，並做了修改，想要在buildroot下編譯並在crb v1.2板子上測試，可以在k510_crb_lp3_v1_2_defconfig目錄下創建一個 local.mk 並添加如下內容：

```text
LINUX_OVERRIDE_SRCDIR = /data/yourname/workspace/k510_linux_kernel
```

在k510_crb_lp3_v1_2_defconfig目錄下執行

```shell
make linux-rebuild
```

就可以看到build/linux-custom目錄下重新編譯了kernel，用的就是/data/yourname/workspace/k510_linux_kernel下修改過的代碼。
uboot和bbl也類似。 這樣就可以直接修改內核代碼並在buildroot下重編內核，增量編譯鏡像去測試。
注： override的源碼在k510_crb_lp3_v1_2_defconfig/build目錄下的目錄名稱會加上custom的後綴，來區分buildroot的預設配置中的每個package的代碼源的不同。 例如上述linux kernel的例子，編譯會看到override指定的代碼是在k510_crb_lp3_v1_2_defconfig/build/linux-custom目錄下編譯，而不是之前我們看到的k510_crb_lp3_v1_2_defconfig/build/linux-xxx目錄。

對於package目錄下的其他代碼，或者buildroot原生的package，都可以通過這種方式在buildroot的框架下進行開發工作。

# 6 燒錄鏡像

K510 支援sdcard和eMMC啟動方式，每次編譯時在k510_buildroot/k510_crb_lp3_v1_2_defconfig/image目錄下將同時生成sysimage-sdcard.img和sysimg-emmc.img鏡像檔，兩份檔可分別燒錄到sdcard和eMMC。

K510 通過 BOOT0 和 BOOT1 兩個硬體管腳的狀態決定晶片啟動方式，具體設置請參考開發板的啟動說明章節。

| 啟動1   | BOOT0   | 啟動方式      |
| ------- | ------- | ------------ |
| 0（開）   | 0（開）   | 串口啟動      |
| 0（開）   | 1（關）  | SD卡啟動      |
| 1（關）  | 0（開）   | NANDFLASH啟動 |
| 1（關）  | 1（關）  | EMMC啟動      |

![](../zh/images/hw_crb_v1_2/clip_hw_3_9.jpg)

## 6.1 燒錄鏡像到sd卡

### 6.1.1 ubuntu下燒錄

在sd卡插到宿主機之前，輸入：

```shell
ls -l /dev/sd*
```

查看當前的存放設備。

將sd卡插入宿主機后，再次輸入：

```shell
ls -l /dev/sd*
```

查看此時的存儲設備，新增加的就是 sd 卡設備節點。

將sd卡插入宿主機後，ls 命令執行結果如下：

![](../zh/images/sdk_build/image-dev_sd.png)

/dev/sdc 就是 sd卡設備節點。 **注意： 用戶環境下生成的 sd卡設備節點可能不是 /dev/sdc，後續操作需要根據實際節點做相應修改。**

在宿主機下進入k510_buildroot/k510_crb_lp3_v1_2_defconfig/image目錄，輸入dd命令將sysimage-sdcard.img燒錄到sdcard：

```shell
sudo dd if=sysimage-sdcard.img of=/dev/sdc bs=1M oflag=sync
```

宿主機下的執行結果如下：

![](../zh/images/sdk_build/image-dd.png)

### 6.1.2 Windows下燒錄

Windows下可通過balenaEtcher工具對sd卡進行燒錄（balenaEtcher工具下載位址<https://www.balena.io/etcher/>）。

1）將TF卡插入PC，然後啟動balenaEtcher工具，點擊工具介面的“Flash from file”按鈕，選擇待燒寫的固件，如下圖。

![](../zh/images/sdk_build/image-sd_pre0.png)

2）點擊工具介面的“Select target”按鈕，選擇目標sdcard卡。

![](../zh/images/sdk_build/image-pre1.png)

3）點擊“Flash”按鈕開始燒寫，燒寫過程有進度條展示，燒寫結束後會提示Flash Finish。

| ![](../zh/images/sdk_build/clip_image_p1.jpg) | ![](../zh/images/sdk_build/clip_image_p2.jpg) |
| --------------------------------------- | --------------------------------------- |
|                                         |                                         |

4）當燒錄完成後，將SD卡插入開發板卡槽，選擇BOOT為從SD啟動，最後開發板上電即可從SD卡啟動。

## 6.2 燒錄鏡像到emmc

將sysimage-emmc.img燒錄到板載eMMC需要藉助於sdcard，在ubuntu環境下，將sysimage-emmc.img 存放到sdcard的使用者分區，然後將sdcard插入開發板並上電啟動。

燒錄emmc鏡像前，需要卸載掉emmc相關文件系統，請參考如下步驟進行卸載。

```shell
mount | grep emmc
```

執行結果如下圖：

![](../zh/images/sdk_build/image-emmc_1.png)

輸入如下命令卸載和檢查。

```shell
umount /root/emmc/p2
umount /root/emmc/p3
umount /root/emmc/p4
mount | grep emmc
```

執行結果如下圖：

![](../zh/images/sdk_build/image-emmc_2.png)

最後進入sysimage-emmc.img鏡像所在路徑，輸入如下命令燒錄eMMC。

```shell
dd if=sysimage-emmc.img of=/dev/mmcblk0 bs=1M
```

執行結果如下圖：

![](../zh/images/sdk_build/image-emmc3.png)

**注：燒錄過程較慢，大約需要30秒，請耐心等待。**

當燒錄完成後，選擇 BOOT 為從EMMC啟動，最後開發板上電即可從EMMC啟動。

# 7 使用者設定編譯環境 <a id="env_set"> </a>

若使用者不使用上述的docker環境，可在ubuntu18.04/20.04參考如下命令配置自己的開發環境，如果沒有許可權請使用`sudo`。

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

**翻譯免責聲明**  
為方便客戶，Canaan 使用 AI 翻譯程式將文字翻譯為多種語言，它可能包含錯誤。 我們不保證提供的譯文的準確性、可靠性或時效性。 對於因依賴已翻譯信息的準確性或可靠性而造成的任何損失或損害，Canaan 概不負責。 如果不同語言翻譯之間存在內容差異，以簡體中文版本為準。

如果您要報告翻譯錯誤或不準確的問題，歡迎通過郵件與我們聯繫。
