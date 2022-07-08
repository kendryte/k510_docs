![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 Uブーツ開発者ガイド</font>**

<font face="黑体"  size=3>ドキュメントのバージョン: V1.0.0</font>

<font face="黑体"  size=3>発売日:2022-03-09</font>

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
このドキュメントは、K510 demo ボード sdk コンパニオン ドキュメントであり、uboot の下の k510 demo ボード プロファイル、デバイス ツリー、ドライブ位置などの uboot 関連コンテンツを中心に説明しています。 

**<font face="黑体"  size=5>リーダー オブジェクト</font>**

このドキュメント (このガイド) は、主に次の担当者に適用されます。

- ソフトウェア開発者
- テクニカル サポート スタッフ

**<font face="黑体"  size=5>レコードを改訂します</font>**
 <font face="宋体"  size=2>リビジョン レコードには、ドキュメントが更新されるたびに説明が蓄積されます。 ドキュメントの最新バージョンには、以前のすべてのバージョンの更新が含まれています。 </font>

| バージョン番号   | 変更者     | 改訂日 | 修正の説明 |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | システム ソフトウェア グループ | 2022-03-09 |          |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>目録</font>**

[目次]

<div style="page-break-after:always"></div>

# 1 U-Boot の概要

u-boot は sdk の一部であり、sdk が現在使用している u-boot バージョンは 2020.01 です。 Uboot は、さまざまな組み込み CPU 用の Bootloader プログラムを開発するドイツの DENX チームであり、組み込み Linux システムのブートだけでなく、NetBSD、VxWorks、QNX、RTEMS、ARTOS、LynxOS 組み込みオペレーティング システムもサポートしています。 UBootは、PowerPCシリーズのプロセッサをサポートするだけでなく、MIPS、x86、ARM、NIOS、RISICVなどをサポートし、主な機能は初期化メモリ、ブートLinuxシステム、より多くのu-boot導入を参照してください<https://www.denx.de/wiki/U-Boot>

# 2 開発環境の概要

- オペレーティング システム

| 番号 | ソフトウェア リソース | 命令        |
| ---- | -------- | ----------- |
| 1    | ウブンツ   | 18.04/20.04 |

- ソフトウェア環境

ソフトウェア環境の要件を次の表に示します。

| 番号 | ソフトウェア リソース | 命令 |
| ---- | -------- | ---- |
| 1    | K510 SDK |      |

# 3 取得方法

sdk をダウンロードしてコンパイルし、sdk がコンパイルされると uboot コードがダウンロードされ、uboot コードがコンパイルされます。 sdk のダウンロード コンパイル方法については、[K510_SDK_Build_and_Burn_Guide.md を参照してください](./K510_SDK_Build_and_Burn_Guide.md)

# 4 重要なディレクトリとファイルの説明

この章では、コンパイルk510_evb_lp3_v1_1_defconfigを例にとります。 対応する sdk コンパイル メソッドは make CONF=k510_evb_lp3_v1_1_defconfigであり、コンパイル後のディレクトリは次のようになります。

![画像-20210930135634105](../zh/images/uboot_guides/build_out.png)

k510_evb_lp3_v1_1_defconfig/build/uboot-custom ---ubootのコードとコンパイルディレクトリ。

board/canaan/k510/uboot-sdcard.env---uboot デフォルト環境変数プロファイル

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/configs/k510_evb_lp3_v1_1_defconfig --uboot プロファイル;

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/arch/riscv/dts/k510_evb_lp3_v1_1.dts----デバイスツリーファイル;

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/include/configs/k510_evb_lp3_v1_1.h---ヘッダーファイル;

k510_evb_lp3_v1_1_defconfig/images/u-boot_burn.bin ---ubootはファームウェアを燃やします

buildroot-2020.02.11/boot/uboot ----buildroot 内の uboot のコンパイルスクリプトは、通常、変更する必要はありません。

configs/k510_evb_lp3_v1_1_defconfig---sdkのプロファイルBR2_TARGET_UBOOT_BOARD_DEFCONFIG、ubootのプロファイルを指定します。

# 5 uboot はプロセスを開始します

_start(arch/riscv/cpu/start.S、ライン 43)

board_init_f(共通/board_f.c、1013行目)

board_init_r(共通/board_r.c、845行目)

run_main_loop(共通/board_r.c、637行目)

# 6 ubootの下でドライブの指示

## 6.1 ddrドライブ

ボード/カナン/k510_evb_lp3/ddr_init.c

## 6.2 ethドライブ

ドライバ/ネット/macb.c

デバイス ツリー:

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

## 6.3 シリアル駆動

ドライバ/シリアル/ns16550.c

デバイス ツリー:

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

ドライバ/pinctrl/pinctrl-single.c

デバイス ツリー:

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

## 6.5 mmcおよびsdカードドライブ

ドライバ/mmc/sdhci-cadence.c

デバイス ツリー

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

# 7 Uboot デフォルトの環境変数

uboot のデフォルト環境変数は、SDK の board/canaan/k510 ディレクトリの下にあり、テキスト ファイルで事前定義されています。

uboot-emmc.env

uboot-nfs.env

uboot-sdcard.env

SDK の post スクリプトは、コンパイル時に mkenvimage を呼び出して、テキストの環境変数定義を uboot がロードできるバイナリ イメージにコンパイルし、ブート パーティションに配置します。

たとえば、次のようになります。

uboot-sdcard.env

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

注: カーネルブートパラメータ bootargs は uboot のデフォルト環境変数によって設定され、dts の bootargs は上書きされます。 よく寄せられる質問 - bootargs はどこでカーネルに入手して渡しましたか?

# 8 Ubootプログラムの更新

## 8.1 sdk ミラーリング メソッドを書き込みます

sdk イメージには、k510_evb_lp3_v1_1_defconfig/images/sysimage-sdcard.img ファイルなどの sdk イメージを直接書き込む uboot プログラムが既に含まれています

## 8.2 linuxの下でアップデートsdカード内のubootプログラム

u-boot_burn.binファイルを tftp ディレクトリに配置し、デバイス ゲート ip アドレスを設定し、/root/sd/p1 ディレクトリに入ります。 tftp -gr u-boot_burn.bin xxx.xxx.xxx.xx コマンドを実行します。

## 8.3 linuxアップデートemmc内のubootプログラム

u-boot_burn.binファイルを tftp ディレクトリに配置し、デバイスゲート ip アドレスを設定し、tftp -gr u-boot_burn.bin xxx.xxx.xxx.xx を使用してデバイスにファイルをダウンロードします。

dd if=u-boot_burn.bin of=/dev/mmcblk0p1 コマンドを実行して、ファイルを mmc カードに書き込みます。

# 9 よく寄せられる質問

## 9.1 DDR 周波数はどのように設定されますか?

A: 現在、evb は 800 しか実行できず、CRB は 800 または 1600 を設定できます。 CRBボードddr周波数設定方法はubootのboard\Canaan\k510_crb_lp3\ddr_param.hファイル,800M対応#define DDR_800 1,1600M 対応#define DDR_1600 1 を参照してください。

## 9.2 bootargs はどこでカーネルに渡されますか?

A: uboot 環境変数 bootargs から取得すると、uboot はカーネルをブートするときに、bootargs 環境変数の値に基づいて、メモリデバイスツリー内の bootargs パラメータを変更します。 関連するコードは次のとおりです。

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

## 9.3 起動パラメータとコンパイルされたデバイスツリーファイルが一致していませんか?

A: uboot は、ブート方法に従って環境変数を動的に取得し、カーネルをブートするときに bootargs 環境変数に基づいてメモリ内のデバイス ツリーを更新します。 変更された起動パラメータは/sys/firmware/devicetree/base/chosen ノードを参照してください。

## 9.4 uboot環境変数はそこに保存されますか?

A:

| 起動方法 | uboot は場所を読み取って保存します | コンパイル時にファイルに対応します |
| :-: | :-: | :-: |
| emmc が起動します | emmc の 2 番目のパーティションの uboot-emmc.env ファイル | board\canaan\k510\uboot-emmc.env |
| SDカードが起動します | sd カードの最初のパーティションの uboot-sd.env ファイル | board\canaan\k510\uboot-sd.env |

## 9.5 qosはどのように設定されますか?

A:qos関連レジスタはQOS_CTRL0 QOS_CTRL1 QOS_CTRL2 QOS_CTRL3 QOS_CTRL4です。 例:
qos を設定すると、nncase demo のパフォーマンスが向上します

```c
*(uint32_t *)0x970E00FC = (0x2 << 8) | (0x2 << 12) | (0x2 << 16) | (0x2 << 20) | (0x2 << 24);
*(uint32_t *)0x970E0100 = (0x3 << 4) | 0x3;
*(uint32_t *)0x970E00F4 = (0x5 << 16) | (0x5 << 20);
```

**免責事項を翻訳します**  
お客様の便宜のために、カナアンはAI翻訳プログラムを使用してテキストを複数の言語に翻訳し、エラーが含まれている可能性があります。 当社は、提供される翻訳の正確性、信頼性、または適時性を保証するものではありません。 カナアンは、翻訳された情報の正確性または信頼性への依存に起因するいかなる損失または損害についても責任を負いません。 異なる言語翻訳間でコンテンツの違いがある場合は、簡体字中国語版が優先されます。 

翻訳エラーや不正確な問題を報告する場合は、メールでお問い合わせください。