![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 SDKビルドと書き込みガイド</font>**

<font face="黑体"  size=3>ドキュメントのバージョン: V1.0.0</font>

<font face="黑体"  size=3>発売日:2022-03-07</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**免責事項**</font>
お客様が購入した製品、サービス、または機能は、北京Jiayuan Jetts情報技術有限公司(以下「当社」、以下同じ)の商業契約および条件の対象となり、本書に記載されている製品、サービス、または機能の全部または一部がお客様の購入または使用の範囲外となる場合があります。 契約に別段の定めがない限り、当社は、本書の記述、情報、内容の正確性、信頼性、完全性、マーケティング、特定目的、非攻撃性について、明示または黙示を問わず、いかなる表明または保証も行いません。 特に断りのない限り、このドキュメントは使用ガイダンスの参照としてのみ使用してください。
このドキュメントの内容は、製品バージョンのアップグレードまたはその他の理由により、予告なく随時更新または変更されることがあります。 

**<font face="黑体"  size=3>商標表示</font>**

「<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />」アイコン、カナン、その他の商標は、北京Jiayuan Jets情報技術有限公司の商標です。 本書で言及されるその他すべての商標または登録商標は、それぞれの所有者が所有しています。 

**<font face="黑体"  size=3>©著作権2022北京Jiayuan Jetth情報技術有限公司</font>**
このドキュメントは、K510プラットフォーム開発設計にのみ適用され、当社の書面による許可なく、いかなるユニットまたは個人も、このドキュメントの一部または全部をいかなる形式でも配布することはできません。 

**<font face="黑体"  size=3>北京Jiayuan Jetth情報技術有限公司</font>**
URL: canaan-creative.com
ビジネスお問い合わせ:salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# 序文
**<font face="黑体"  size=5>ドキュメントの目的</font>**
このドキュメントは、K510 sdk のコンパニオン ドキュメントであり、エンジニアが k510 sdk のコンパイルとバーンインを理解するのに役立ちます。 

**<font face="黑体"  size=5>リーダー オブジェクト</font>**

このドキュメント (このガイド) は、主に次の担当者に適用されます。

- ソフトウェア開発者
- テクニカル サポート スタッフ

**<font face="黑体"  size=5>レコードを改訂します</font>**
 <font face="宋体"  size=2>リビジョン レコードには、ドキュメントが更新されるたびに説明が蓄積されます。 ドキュメントの最新バージョンには、以前のすべてのバージョンの更新が含まれています。 </font>

| バージョン番号   | 変更者     | 改訂日 | 修正の説明 |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | AI製品部 | 2022-03-07 |          |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>目録</font>**

[目次]

<div style="page-break-after:always"></div>

# 1 はじめに

このドキュメントでは、K510 SDK のダウンロード、コンパイル、バーンインなどの開発環境の構築セクションについて説明します。

# 2 k510 SDK

## 2.1 k510 sdkのダウンロード

k510 SDK プロジェクトアドレス: <https://github.com/kendryte/k510_buildroot>

取得K510 SDK:

```shell
git clone https://github.com/kendryte/k510_buildroot.git
```

## 2.2 k510 sdk パッケージの概要

K510 SDKはbuildrootを基本フレームワークとし,K510 linux kernel(linuxバージョン4.17.0),u-boot(u-bootバージョン2020.01),riscv-pk-k510(BBL)ソースパッケージをベースに構築した組み込みLinux開発環境であり,K510 SDKディレクトリ構造を以下の図に示す.

![](../zh/images/sdk_build/image-buildroot.png)

 K510 SDK の各ファイルは次のように記述されています。

| **ファイル**です        | **コンテンツの説明**                                                 |
| --------------- | ------------------------------------------------------------ |
| 板           | フォルダは、K510の様々なプロファイルやスクリプトは、ミラーを生成するプロファイル(genimage - xxx.cfg)、buildrootのpost -imageスクリプト、U -ブートデフォルトの環境変数などです。 |
| Config.in       | 内容は、buildroot コンパイルが必要な package を示します。 |
| 設定         | 開発ボードの既定のコンパイル プロファイルであるフォルダ。 K510 CRB-V0.1、K510 CRB-V1.2、および K510 EVB の 3 つのボードの既定のコンパイル プロファイルが<br /> `k510_crb_lp3_v1_2_defconfig`<br /> `k510_crb_lp3_v0_1_defconfig`<br /> `k510_evb_lp3_v1_1_defconfig` 現在保存されています|
| 外部.desc   | buildrootのexternalメカニズムプロファイル. |
| external.mk     | |
| メイクファイル        | k510 SDKのマスターMakefile。 |
| パッケージ         | フォルダは、主にK510アプリケーションであり、Config.in ファイルの内容は、そのディレクトリの下にコンパイルされているアプリケーションを決定します。 |
| 斑         | フォルダ (buildroot のパッチ ファイル) は、Makefile がソースを解凍するときに、このディレクトリの下のパッチ ファイルを適切なソース ディレクトリにヒットします。 |
| パックダウンロード    | dl フォルダの圧縮パッケージであるフォルダ。 |
| README.md       | sdk に関する注意事項。 |
| release_note.md | |
| ツールチェーン       | クロスコンパイル ツール チェーンであるフォルダ。 |
| ティッカー              | フォルダは、pkg-download の dl 解凍パッケージであり、追加したパッケージがある場合は、そのディレクトリにダウンロードされます。 |

## 2.3 k510 sdk バージョン

次の図に示すように、k510 sdk コンパイルによって生成されたミラーをボードに書き込むときにバージョン情報が印刷されます。

```text
#############SDK VERSION############################################
MX2_DEV_0106-02e87077-20220428-153936CST-xxxxx-server
####################################################################
```

起動が完了すると、シェルターミナルに次のように入力すると、sdk バージョン情報が表示されます。

```shell
cat /etc/version/release_version
#############SDK VERSION############################################
MX2_REL_0106-02e87077-20220428-153936CST-xxxx-server
####################################################################
```

**注: k510 sdk のバージョンは異なり、上記の情報は異なる場合があります**。 

# 3 docker コンパイル環境

k510 sdk をダウンロードしたら、sdk 上位ディレクトリで次のコマンドを実行して docker を起動します。

```shell
sh k510_buildroot/tools/docker/run_k510_docker.sh
```

後続のコンパイル操作は、既定では docker で実行されます。
ローカル環境を構築する必要がある場合は、[ローカル環境の構築を参照してください](#env_set)

# 4 コンパイル

## 4.1 コンパイルの準備

### 4.1.1 ソースパッケージのダウンロード(オプション、コンパイルを高速化可能)

ソース パッケージをダウンロードするには、次のコマンドを実行します。

```shell
make dl
```

## 4.2 コンパイル

k510_buildroot/config ディレクトリには、 と の 3 つの開発ボードのコンパイルプロファイルがあり、`k510_crb_lp3_v0_1_defconfig` `k510_crb_lp3_v1_2_defconfig``k510_evb_lp3_v1_1_defconfig` **このドキュメントではコンパイルターゲットとして k510_crb_lp3_v1_2_defconfig を選択します**。 

k510 docker 環境で次のようなコマンドを入力してコンパイルを開始します。

```shell
make CONF=k510_crb_lp3_v1_2_defconfig
```

![](../zh/images/sdk_build/image-make.png)

次のような情報を出力して、コンパイルが正常に完了したことを示します。

![](../zh/images/sdk_build/image-uboot_r.png)

コンパイルが完了すると、フォルダが生成されます`k510_crb_lp3_v1_2_defconfig`。 

![画像-20220311121912711](../zh/images/sdk_build/image-makeout.png)

これらのドキュメントは次のように記述されます。

| **ファイル**です    | **コンテンツの説明**                                                 |
| ----------- | ------------------------------------------------------------ |
| メイクファイル    | コンパイル ミラーで使用される Makefile。                                     |
| 建てる       | すべてのソース パッケージのコンパイル済みディレクトリ。 たとえば、linux kernel、u-boot、BBL、busybox など、ソースは build ディレクトリに解凍され、コンパイルされます。 |
| ホスト        | すべての host package のインストール パスは、クロスコンパイル環境を構築するために toolchain もこのディレクトリにコピーされます。 |
| 画像      | コンパイルビルドのターゲット ファイル ディレクトリ (以下の説明を参照)                     |
| nand_target | ルートファイルシステムの元のディレクトリ(NandFlashイメージの生成で使用)                  |
| ターゲット      | ルートファイルシステムの元のディレクトリ(eMMCとSDカードミラーの使用を生成)                 |

k510_crb_lp3_v1_2_defconfig/images ディレクトリの下にはバーンイン ミラーがあり、各ファイルの説明は次のとおりです。

| **ファイル**です                   | **コンテンツの説明**                                                 |
| -------------------------- | ------------------------------------------------------------ |
| bootm-bbl.img              | Linux+bbl カーネルミラーリング(カーネルをパッケージ化したbblターゲットファイル、ubootブートbbl用) |
| k510.dtb                   | デバイス ツリー                                                       |
| sysimage-emmc.img          | emmc バーンイン ファイル: パッケージ化されたuboot_burn、kernel、および bbl              |
| sysImage-sdcard.img        | sdcard バーンイン ファイル: パッケージ化されたuboot_burn、kernel、および bbl            |
| sysImage-nand.img          | nand バーンイン ファイル: パッケージ化されたuboot_burn、kernel、および bbl              |
| Uブート.bin                 | uboot バイナリ                                             |
| ユー boot_burn.bin            | uboot バーンイン ファイル                                               |
| uboot-emmc.env             | uboot 環境変数: emmc 起動用                                  |
| uboot-sd.env               | uboot 環境変数: sdcard 起動に使用します                                |
| uboot-nand.env             | uboot 環境変数: nand 起動用                                  |
| vmlinux                    | Linux カーネルミラーファイル(elfデバッグ情報付き)                           |
| rootfs.ext2                | buildroot 形式rootfs ext2ミラーファイル                             |
| sysimage-sdcard-debian.img | sdcard バーンインファイル: カードミラー (debian フォーマットrootfs)                     |

k510_crb_lp3_v1_2_defconfig/build ディレクトリの下には、コンパイルされたすべてのオブジェクトのソースがあり、その重要なファイルの一部は次のとおりです。

| **ファイル**です         | **コンテンツの説明**                  |
| ---------------- | ----------------------------- |
| リナックス - xxxの        | コンパイルされた Linux kernel ソースディレクトリ |
| uboot-xxx        | コンパイルされた Uboot ソース ディレクトリ       |
| リスクブ - 馬力 - k510 - xxxの| コンパイルされた bbl ソース ディレクトリ         |
| ...              |                               |

注: xxx はバージョン番号です。 後の章でkernle、bbl、および uboot へのパスを参照する場合、xxx はバージョン番号を表します。

**特別な注意: make clean の場合、k510_crb_lp3_v1_2_defconfigフォルダの下にあるすべてのコンテンツが削除されます。 したがって、kernel、bbl、または uboot コードを変更する必要がある場合は、build ディレクトリで直接変更しないでください。

## 4.1 buildroot を設定します

k510 docker 環境で設定 buildroot コマンドを入力します。

```shell
make CONF=k510_crb_lp3_v1_2_defconfig menuconfig
```

実行結果は次のとおりです。

![](../zh/images/sdk_build/image-make_men.png)

![](../zh/images/sdk_build/image-make_menu.png)

設定が完了したら保存して終了し、次のようなbuildroot設定保存コマンドも実行する必要があります。

```shell
make CONF=k510_crb_lp3_v1_2_defconfig savedefconfig
```

実行結果は次のとおりです。

![](../zh/images/sdk_build/image-make_savedef.png)

上記の操作が完了すると、ユーザーは次のようなコマンドを入力して再コンパイルできます。

```shell
make CONF=k510_crb_lp3_v1_2_defconfig
```

## 4.2 U-Boot を設定します

ユーザーが uboot 構成を変更する必要がある場合は、k510_crb_lp3_v1_2_defconfigディレクトリに移動し、次のようなコマンドを入力して U-Boot 構成を開始します。

```shell
make uboot-menuconfig
```

実行結果は次のとおりです。

![](../zh/images/sdk_build/image-uboot_men.png)

![](../zh/images/sdk_build/image-uboot_menu.png)

構成が完了したら、menuconfig を終了するときに[構成の保存] を選択し、次のような構成保存コマンドも実行する必要があります。

```shell
make uboot-savedefconfig
```

実行結果は次のとおりです。

![](../zh/images/sdk_build/image-uboot_savedefconfig.png)

最後に、k510_crb_lp3_v1_2_defconfigディレクトリで、コンパイルを開始するには、次のようなコマンドを入力します。

```shell
make uboot-rebuild
```

詳細については、次のセクションの説明を参照してください。

## 4.3 U-Boot をコンパイルします

k510_crb_lp3_v1_2_defconfig/build/uboot-xxx ディレクトリの下にコンパイルされた U-Boot ソースが保存され、ユーザーが U-Boot ソース コードを変更したか、uboot を再構成したかにかかわらず、U-Boot を再コンパイルする必要があります。

k510_crb_lp3_v1_2_defconfigディレクトリに移動し、U-Boot を再コンパイルするには、次のコマンドを入力します。

```shell
make uboot-rebuild
```

実行結果は次のとおりです。

![](../zh/images/sdk_build/image-uboot-rebuild.png)

コンパイルが完了すると、k510_crb_lp3_v1_2_defconfig/images ディレクトリの下に新しい u-boot ファイルが生成されます.bin。

新しい u-boot でバーンイン ミラー ファイルを再生成する場合は、`k510_crb_lp3_v1_2_defconfig`ディレクトリの下で次の操作を行います

```shell
make
```

実行結果は次のとおりです。

![](../zh/images/sdk_build/image-make_u.png)

コンパイルが完了すると、次のようなミラー ファイルによって生成された情報が表示されます。

![](../zh/images/sdk_build/image-uboot_r.png)

## 4.4 Linux kernel を設定します

ユーザーが kernel 構成を変更する必要がある場合は、k510_crb_lp3_v1_2_defconfig ディレクトリに移動し、次のコマンドを入力して kernel 構成を開始します。

```shell
make linux-menuconfig
```

実行結果は次のとおりです。

![](../zh/images/sdk_build/image-linux_men.png)

![](../zh/images/sdk_build/image-linux_menu.png)

構成を変更した後に menuconfig を終了する場合は、[構成の保存] を選択し、最後に次のような構成保存コマンドを実行する必要があります。

```shell
make linux-savedefconfig
```

実行結果は次のとおりです。

![](../zh/images/sdk_build/image-linux_savedefconfig.png)

最後に、k510_crb_lp3_v1_2_defconfigディレクトリで、コンパイルを開始するには、次のようなコマンドを入力します。

```shell
make linux-rebuild
```

詳細については、次のセクションの説明を参照してください。

## 4.5 Linux kernel をコンパイルします

k510_crb_lp3_v1_2_defconfig/build/linux-xxx ディレクトリにはコンパイルされた linux ソースが保存されており、ユーザーが linux ソースコードを変更したり、Linux を再構成したりした場合でも、Linux を再コンパイルする必要があります。

k510_crb_lp3_v1_2_defconfigディレクトリに移動し、次のようなコマンドを入力して linux を再コンパイルします。

```shell
make linux-rebuild
```

実行結果は次のとおりです。

![](../zh/images/sdk_build/image-linux_rebuild.png)

コンパイルが完了すると、k510_crb_lp3_v1_2_defconfig/images ディレクトリの下に新しい vmlinux が生成されます。

linux kernelミラーはbblでパッケージ化する必要があり,linux kernelをリコンポストした後,bblを再構成してu-bootブート用の新しいbbl/kernelミラーを生成する必要があるため,次の2つのコマンドを入力する.

```shell
make riscv-pk-k510-dirclean
make riscv-pk-k510
```

実行結果は次のとおりです。

![](../zh/images/sdk_build/image-riscv.png)

コンパイルが完了すると、`k510_crb_lp3_v1_2_defconfig/images`ディレクトリの下に新しいビルドが生成`bootm-bbl.img`されます。 

最後に、k510_crb_lp3_v1_2_defconfigディレクトリにmakeを入力し、新しいbootm-bbl.imgパッケージでemmcとsdカードミラーファイルを生成します。

```shell
make
```

実行結果は次のとおりです。

![](../zh/images/sdk_build/image-make_u.png)

コンパイルが完了すると、次のようなミラー ファイルによって生成された情報が表示されます。

![](../zh/images/sdk_build/image-uboot_r.png)

## 4.6 dts をコンパイルします

デバイスツリーファイルは、k510_buildroot/k510_crb_lp3_v1_2_defconfig/build/linux-4.17/arch/riscv/boot/dts/canaan ディレクトリにあり、ユーザーがデバイスツリーのみを変更した場合、デバイスツリーのみをコンパイルおよび逆コンパイルできます。

mkdtb-local.sh スクリプトを記述します。

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

mkdtb-local.sh を K510_buildroot ディレクトリに配置し、次のコマンドを実行して、k510_crb_lp3_v1_2_defconfigボード デバイス ツリーをコンパイルします。

```shell
./mkdtb-local.sh k510_crb_lp3_v1_2_defconfig
```

実行結果は次のとおりです。

![](../zh/images/sdk_build/image-mdk_dts.png)

コンパイルが完了したk510_crb_lp3_v1_2_defconfig/images ディレクトリの下の k510.dtb は、新しく生成されたデバイス ツリー データベース ファイルであり、all.dts は逆コンパイルされたデバイス ツリー ファイルです。

## 4.7 アプリをコンパイルします

ユーザーは、 `package/hello_world` の Config.in と makefile ファイルの書き込みを参照して、独自のアプリケーションを構築し、ユーザー アプリケーションを k510_buildroot/package ディレクトリの下に配置できます。 

ここでは、k510_buildroot/package に hello_world プロジェクトを配置する場合を例にとり、アプリケーションをコンパイルするプロセスについて説明します。

ホスト環境でk510_buildroot ディレクトリの下の Config.in ファイルを変更します。

![](../zh/images/sdk_build/image-vi_config.png)

Config.in に package/hello_world/Config.in が存在するパスを追加して保存します。

![](../zh/images/sdk_build/image-config_list.png)

k510 docker 環境で設定 buildroot コマンドを入力します。

```shell
make CONF=k510_crb_lp3_v1_2_defconfig menuconfig
```

実行結果は次のとおりです。

![](../zh/images/sdk_build/image-build_menu.png)

bildroot 設定ページが表示され、External option を選択し、最後にその中のhello_worldを選択して終了を保存します。

![](../zh/images/sdk_build/image-extern_option.png)

k510_buildrootディレクトリーの下に「構成の保存」コマンドを入力します。

```shell
make CONF=k510_crb_lp3_v1_2_defconfig savedefconfig
```

実行結果は次のとおりです。

![](../zh/images/sdk_build/image-build_savedef.png)

1) 最初のコンパイルの場合、実行手順は次のとおりです。

k510_buildrootディレクトリで、次のようなコマンドを入力してプロジェクトプログラム全体をコンパイルし、helloをemmcおよびsdカードミラーファイルにパッケージ化します。

```shell
make CONF=k510_crb_lp3_v1_2_defconfig
```

実行結果は次のとおりです。

![](../zh/images/sdk_build/image-build_make_def.png)

k510_buildroot/k510_crb_lp3_v1_2_defconfig/target ディレクトリの下には、生成された hello アプリケーションが表示され、アプリケーションが正しくコンパイルされているかどうかを判断できます。

![](../zh/images/sdk_build/image-hello.png)

2)コンパイル済みで、アプリをコンパイルしてバーンインミラーにパッケージ化するだけの場合は、次の手順に従います。

k510_buildroot/k510_crb_lp3_v1_2_defconfigディレクトリに移動し、helloアプリケーションをコンパイルするには、次のようなコマンドを入力します。

```shell
make hello_world-rebuild
```

実行結果は次のとおりです。

![](../zh/images/sdk_build/image-app_build-1.png)

k510_buildroot/k510_crb_lp3_v1_2_defconfigディレクトリに移動し、make コマンドを入力して、hello を emmc および sd カード ミラー ファイルにパッケージ化します。

```shell
make
```

実行結果は次のとおりです。

![](../zh/images/sdk_build/image-app-build-2.png)

# 5 K510 SDKで開発

## 5.1 linux kernel/BBL/uboot ソース

このsdkで使用されるubootバージョンは2020.01であり、ubootパッチディレクトリはpackage/patches/ubootであり、パッチがヒットした後のディレクトリはk510_xxx_defconfig/build/uboot-2020.01です。

このsdkで使用されるkernelバージョンは4.17であり、kernelパッチディレクトリはpackage/patches/linuxであり、パッチがヒットした後のディレクトリはk510_xxx_defconfig/build/linux-4.17です。

この sdk の BBL は、riscv-pk-k510.mk で bbl のコード ソースとバージョン番号を指定するタグレット package として、package/riscv-pk-k510/ディレクトリの下に配置されます。

```text
RISCV_PK_K510_VERSION = 1e666d6c5dbab220d2ca57fbd9bec49702599b75
RISCV_PK_K510_SITE = git@github.com:kendryte/k510_BBL.git
RISCV_PK_K510_SITE_METHOD = git
```

## 5.2 linux kernel/BBL/uboot を開発する

Buildrootでコンパイルされた各pacakgeは、linux kernel/BBL/ubootを含む、tarball、解凍、構成、コンパイル、インストールなどの統一されたパッケージ管理ステップをダウンロードすることによって達成されるため、k510_buildroot/k510_crb_lp3_v1_2_defconfig/buildディレクトリの下には、すべてのソースコードが表示されますが、バージョン管理情報はありません。 コードが git リポジトリからダウンロードされた場合でも。

gitリポジトリデータを含むkernel/BBL/ubootソースはdl/ディレクトリの下に見ることができますが,buildrootはdlディレクトリ下のソースコードのみをキャッシュとして扱い,このディレクトリで直接開発することはお勧めしません.

開発モードでは、buildroot はOVERRIDE_SRCDIR方法を提供します。

簡単に言うと、k510_crb_lp3_v1_2_defconfig ディレクトリの下に local.mk ファイルを追加できます。

```text
<pkg1>_OVERRIDE_SRCDIR = /path/to/pkg1/sources
```

- LINUX 是kernel的package name
- UBOOT は uboot の PACKAGE name です
- RISCV_PK_K510 は bbl の package name です

Linux kernel を例にとり、その使用方法を説明します。
/data/yourname/workspace/k510_linux_kernelディレクトリの下に clone でカーnelのコードを作成し、bildroot でコンパイルして crb v1.2 ボードでテストする変更を加えたとしますk510_crb_lp3_v1_2_defconfigディレクトリの下に local.mk を作成し、次のように追加します。

```text
LINUX_OVERRIDE_SRCDIR = /data/yourname/workspace/k510_linux_kernel
```

k510_crb_lp3_v1_2_defconfigディレクトリで実行します

```shell
make linux-rebuild
```

bild/linux-custom ディレクトリの下に、/data/yourname/workspace/k510_linux_kernelで変更されたコードを使用して、kernel が再コンパイルされていることがわかります。
uboot と bbl も同様です。 これにより、カーネル コードを直接変更し、bildroot でカーネルをリコンピレーションし、ミラーをインクリメンタルにコンパイルしてテストできます。
注: k510_crb_lp3_v1_2_defconfig/build ディレクトリの下の override のソース名には、custom のサフィックスが付加され、buildroot の既定の構成で各 package のコード ソースが異なります。 たとえば、上記の linux kernel の例では、コンパイルでは、override で指定されたコードが、k510_crb_lp3_v1_2_defconfig/build/linux-xxx ディレクトリではなく、k510_crb_lp3_v1_2_defconfig/build/linux-custom ディレクトリでコンパイルされていることがわかります。

package ディレクトリの下の他のコード、または buildroot ネイティブの package では、この方法で buildroot のフレームワークで開発作業を行うことができます。

# 6 バーンインミラー

K510 は sdcard と eMMC の起動方法をサポートしており、各コンパイル時にk510_buildroot/k510_crb_lp3_v1_2_defconfig/image ディレクトリの下に sysimage-sdcard.img と sysimg-emmc.img ミラー ファイルの両方が生成され、それぞれ sdcard と eMMC に書き込まれます。

K510 は、BOOT0 と BOOT1 の 2 つのハードウェア ピンの状態によってチップの起動方法を決定します。

| ブート1   | ブート0   | 起動方法      |
| ------- | ------- | ------------ |
| 0(オン)   | 0(オン)   | シリアルが起動します      |
| 0(オン)   | 1(オフ)  | SDカードが起動します      |
| 1(オフ)  | 0(オン)   | NANDFLASH が起動します |
| 1(オフ)  | 1(オフ)  | EMMC が起動します      |

![](../zh/images/hw_crb_v1_2/clip_hw_3_9.jpg)

## 6.1 SDカードにミラーを焼く

### 6.1.1 ubuntuの下で焼く

sd カードがホストに接続される前に、次の入力を行います。

```shell
ls -l /dev/sd*
```

現在のストレージ デバイスを表示します。

sd カードをホストに挿入したら、もう一度次の値を入力します。

```shell
ls -l /dev/sd*
```

この時点でストレージ デバイスを見ると、SD カード デバイス ノードが新しく追加されます。

sd カードをホストに挿入すると、ls コマンドは次のように実行されます。

![](../zh/images/sdk_build/image-dev_sd.png)

/dev/sdc は sd カード デバイス ノードです。 **注: ユーザー環境で生成された sd カード デバイス ノードは /dev/sdc ではなく、後続の操作では実際のノードに応じて変更する必要があります。 **

ホストマシンの下にk510_buildroot/k510_crb_lp3_v1_2_defconfig/imageディレクトリに移動し、ddコマンドを入力してsysimage-sdcard.imgをsdcardに書き込みます。

```shell
sudo dd if=sysimage-sdcard.img of=/dev/sdc bs=1M oflag=sync
```

ホストマシンの下での実行結果は次のとおりです。

![](../zh/images/sdk_build/image-dd.png)

### 6.1.2 Windows で焼く

Windows では、balenaEtcher ツールを使用して sd カードを書き込み (balenaEtcher ツールのダウンロード アドレス<https://www.balena.io/etcher/>) できます。 

1)PCにTFカードを挿入し、balenaEtcherツールを起動し、ツールインターフェイスの「Flash from file」ボタンをクリックして、次の図のように書き込むファームウェアを選択します。

![](../zh/images/sdk_build/image-sd_pre0.png)

2)ツールインタフェースの「Select target」ボタンをクリックして、ターゲットsdcardカードを選択します。

![](../zh/images/sdk_build/image-pre1.png)

3)「Flash」ボタンをクリックして書き込みを開始し、書き込みプロセスは、進行状況バーが表示され、書き込みが終了するとFlash Finishをプロンプトします。

| ![](../zh/images/sdk_build/clip_image_p1.jpg) | ![](../zh/images/sdk_build/clip_image_p2.jpg) |
| --------------------------------------- | --------------------------------------- |
|                                         |                                         |

4)バーンインが完了したら、SDカードを開発ボードカードスロットに挿入し、BOOTをSDから起動し、最後に開発ボードに電気を投入し、SDカードから起動することができます。

## 6.2 バーンインミラーをemmcに

sysimage-emmc.img をオンボード eMMC にバーンインするには、sdcard を使用して、sysimage-emmc.img を ubuntu 環境で sdcard のユーザー パーティションに格納し、sdcard を開発ボードに挿入して電源を投入して起動する必要があります。

emmc イメージを書き込む前に、emmc 関連ファイルシステムをアンマウントする必要があります。

```shell
mount | grep emmc
```

実行結果を次の図に示します。

![](../zh/images/sdk_build/image-emmc_1.png)

アンインストールとチェックには、次のようなコマンドを入力します。

```shell
umount /root/emmc/p2
umount /root/emmc/p3
umount /root/emmc/p4
mount | grep emmc
```

実行結果を次の図に示します。

![](../zh/images/sdk_build/image-emmc_2.png)

最後にsysimage-emmc.imgミラーが存在する経路に入り,次のようなコマンドでeMMCを書き込みます。

```shell
dd if=sysimage-emmc.img of=/dev/mmcblk0 bs=1M
```

実行結果を次の図に示します。

![](../zh/images/sdk_build/image-emmc3.png)

**注:バーンインプロセスは遅く、約30秒かかりますので、しばらくお待ちください。**

バーンインが完了したら、BOOT を EMMC から起動し、最後に開発ボードの電源を EMMC から起動します。

# 7 コンパイル環境をユーザが構成します <a id="env_set"> </a>

ユーザーが上記の docker 環境を使用しない場合は、ubuntu18.04/20.04 で次のコマンドを参照して独自の開発環境を構成できます`sudo`。 

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

**免責事項を翻訳します**  
お客様の便宜のために、カナアンはAI翻訳プログラムを使用してテキストを複数の言語に翻訳し、エラーが含まれている可能性があります。 当社は、提供される翻訳の正確性、信頼性、または適時性を保証するものではありません。 カナアンは、翻訳された情報の正確性または信頼性への依存に起因するいかなる損失または損害についても責任を負いません。 異なる言語翻訳間でコンテンツの違いがある場合は、簡体字中国語版が優先されます。 

翻訳エラーや不正確な問題を報告する場合は、メールでお問い合わせください。