![](../zh/images/canaan-cover.png)
&nbsp;
&nbsp;
**<font face="黑体" size="6" style="float:right">K510 CRB V1.2ハードウェアガイド</font>**

<font face="黑体" size=100>&nbsp;
&nbsp;
&nbsp;</font>

<font face="黑体"  size=3>ドキュメントのバージョン: V1.0.0</font>

<font face="黑体"  size=3>発売日:2022-03-15</font>

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

| バージョン番号 | 変更者    | 改訂日   | 修正の説明           |
| :----- | --------- | ---------- | ------------------ |
| V1.0.0 | AI製品部 | 2022-03-15 | |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>目録</font>**

[目次]

<div style="page-break-after:always"></div>

# 1 概要

&emsp; &emsp; K510 CRBは、カネケンドライトK510 AIチップ用に開発されたリファレンス設計、チップデバッグとテスト、K510チップの強力な計算力と機能を実証するユーザー製品開発検証のためのハードウェア開発プラットフォームです。 同時に、K510チップベースのハードウェアリファレンス設計をお客様に提供し、リファレンス設計のモジュール回路を変更したり、簡単に変更したりすることなく、K510チップをコアとする製品ハードウェア開発作業を完了できます。

&emsp; &emsp; K510 CRBは、K510チップのハードウェア開発、アプリケーションソフトウェア設計、デバッグ、運用などをサポートしており、異なる使用環境を考慮してチップのフル機能検証を行うため、さまざまなインターフェースと設計が比較的完全です。 K510 CRB は、USB ケーブルを介して PC に接続したり、基本的な開発システムとして使用したり、次のようなデバイスやコンポーネントを接続するより完全な開発システムおよびプレゼンテーション環境を実現したりできます。

- 電源

- TF Card ストレージ デバイス

- MIPI DSI LCD ディスプレイ

- MIPI CSIカメラモジュール

- DVPカメラモジュール

- イーサネット ネットワーク ケーブル

- HDMIディスプレイ

- ヘッドフォンまたはホーン

- スペアパーツの拡張

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-K510_Core.png">
</div>

  <center>図 1-1 K510 CRB レンダリング図</center>

    **禁止事项**

  1. コアモジュールと周辺モジュールのライブスワップを禁止!
  2. 静電気の放出や静電気に対する保護措置なしに、本製品を直接操作しないでください。
  3. 有機溶剤や腐食性液体による洗浄は禁止されています。
  4. ノックやねじれなど、物理的な損傷を引き起こす可能性のある操作は禁止されています。

    **注意事項**

  1. 人体に静電気を放出した後、アプライアンスを操作し、静電気ブレスレットを着用することをお勧めします。
  2. 操作する前に、ベースプレートの電源電圧とアダプタ電圧が、このドキュメントで説明されている許容範囲内であることを確認してください。
  3. 設計する前に、このドキュメントとエンジニアリング ドキュメントの考慮事項を必ずお読みください。
  4. 高温、高湿、高腐食環境での製品の使用には、冷却、排水、シール、その他の特別な処理が必要です。
  5. 自分で修理したり、分解したりしないでください。

<div style="page-break-after:always"></div>

## 1.1 システムブロック図

&emsp; &emsp; システム ブロック図は、K510 CRB の設計原理とコンポーネント間の関係を記述するために使用され、K510 CRB の使用と開発者がシステム全体のアーキテクチャと原則を直感的に理解できるようにします。

&emsp; &emsp; K510の機能の詳細については、K510 Full Datasheetを参照してください。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_1_2.png">
</div>

<center>図1-2 K510 CRB組成</center>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_1_3.png">
</div>

<center>図 1-3 K510 CRB システム ブロック図 </center>

<div style="page-break-after:always"></div>

&emsp; &emsp; K510 CRB 開発キットには、主に次のコンポーネントが含まれています。

| 部品 | 数量 |
| :-: | :-: |
| K510 CRBマザーボード | 1 |
| USBタイプ C线缆 | 2 |
| Micro USB OTG ケーブル | 1 |
| MIPI DSIディスプレイ、解像度1920x1080 | 1 |
| MIPI CSIカメラサブボード、オンボードSony IMX219 image sensor 2 | 1 |
| ヤクリはシェルを保護します | 1 |

<div style="page-break-after:always"></div>

## 1.2 機能の概要

&emsp; &emsp; K510 SDKはbuildrootを基本フレームワークとし、K510 linux kernel(linuxバージョン4.17.0)、u-boot(u-bootバージョン2020.01)、riscv-pk-k510を使用しています

&emsp; &emsp; K510 CRB V1.2 (特別な声明がない場合、このドキュメントで後述する CRB のバージョンはすべて V1.2 です) の主な機能は次のとおりです。

- PMIC: 電源管理
- 32 bit LPDDR3EE、総容量 512MByte
- 8bit eMMC、総容量4GByte
- QSPI NAND、総容量128MByte
- TF カード: 外部拡張 TF カード ストレージをサポートします。
- USB OTG: Host/Device スイッチをサポートするシステム アップグレードが使用されます
- SDIO WIFI: ワイヤレス インターネット接続と Bluetooth 接続をサポートします
- Audio: 音声入出力をサポートします
- PDM MIC:VAD ウェイクアップ機能
- Uart &JTAG Debug: 開発ボード Debug が使用されます
- Video Input: デュアル MIPI CSI 2lane カメラ入力
- Video Output: MIPI DSI 4lane, 1080P ディスプレイ
- RGMII: ギガビット イーサネット接続
- HDMI: 高解像度マルチメディア インターフェイス
- 拡張インターフェイス:電源、GPIO、I2C、SPI
- キー、ライト

<div style="page-break-after:always"></div>

# 2 ハードウェア リソースの概要

## 2.1 全体的な効果図

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_1.png" width=80%>
</div>

<center> 図2-1 マザーボードの正面図 </center>

<div style="page-break-after:always"></div>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_2.png" width=80%>
</div>

<center> 図2-1 マザーボードの背面図 </center>

<div style="page-break-after:always"></div>

## 2.2 構造およびインターフェイスの概略図

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_3.png" width=120%>
</div>

<center> 図 2-3 マザーボードの前面にある各デバイスの位置 </center>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2-4.png" width=120%>
</div>

<center> 図 2-4 システム基板の背面 </center>

<div style="page-break-after:always"></div>

## 2.3 電源ブロック図

&emsp; &emsp; K510 CRB は、DC-5V をボード全体の入力電源として使用し、K510 CORE コア モジュールに DC-5V を供給し、2 つの DC-DC を介してベース プレートの他の周辺機器に 1.8V と 3.3V の 2 つの電源を供給します。

## 2.4 I2C デバイス アドレス

<center>表 2-1 I2C デバイス アドレス テーブル</center>

| 名前 | ピン(SCL、SDA) | アドレス | 備考 |
| :-: | :-: | :-: | :-: |
| タッチスクリーン | IO_103、IO_102 | 0x14または0x5D | |
| ティッカー | IO_117、IO_116 | 0x3B | |
| オーディオコーデック | IO_117、IO_116 | 0x1A | |
| ミピCSIカメラ0 | IO_120、IO_121 | 0x10 | |
| ミピCSIカメラ1 | IO_47、IO_48   | 0x10 | |

## 2.5 回路図

&emsp; &emsp; K510 CRB開発ボードに対応するリファレンス回路図は[、release](https://github.com/kendryte/k510_docs/releases)でダウンロードしてください。

<div style="page-break-after:always"></div>

# 3 開発ボードの各部で紹介します

## 3.1 コアモジュール

&emsp; &emsp; K510 CRB を使用して学習および開発する前に、K510 マニュアルのチップの詳細なアーキテクチャを参照して、K510 の電源、ストレージ、コンピューティング リソース、周辺機器をより深く理解し、チップ ソリューションの親しみやすさと開発を容易にすることをお勧めします。 K510コアプレートは、図3-1に示されています。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_1.png">
</div>

<center>図3-1 K510コアコアモジュール</center>

<div style="page-break-after:always"></div>

## 3.2 電源を入力します

&emsp; &emsp; K510 CRBは、外部5V電源を使用し、オンボードは、両方のUSBタイプCインターフェイスを搭載し、開発ボードに電力を供給することができ、UARTインターフェイスは、コンピュータを接続するために使用され、コンピュータのUSBインターフェイスは、500mAの電流しか供給できず、電源不足が発生した場合は、DC:5Vでアダプタを使用して電源を供給してください。 インターフェイスを次の図に示します。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_2.png" width=60%>
</div>

<center> 図 3-2 電源入力インターフェイス </center>

**メモ:5V電源の使用を制限し、クイック充電アダプタを使用する場合は、クイック充電アダプタが5V以上の電源を誤って出力し、開発ボードの電源部分が損傷するのを防ぐために、携帯電話やその他のデバイスを同時に接続しないようにしてください。**
&emsp; &emsp; 次の図に示すように、K2トグルスイッチを使用して電源投入時と電源オフ操作を行います。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-3.jpg" width=50%>
</div>

<center>図 3-3 電源スイッチの説明</center>

<div style="page-break-after:always"></div>

## 3.3 ストレージデバイス

&emsp; &emsp; K510 CRB は、DDR、eMMC、NAND Flash、TF カードなど、さまざまなストレージ デバイスをオンボードします。

### 3.3.1 eMMC

&emsp; &emsp; K510 CRB オンボードの 4G Bytes eMMC メモリは、コア モジュール上にあり、起動コードやユーザー ファイルなどのデータを格納するために使用できます。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-eMMC.png" width=70%>
</div>

<center>図3-4 eMMCメモリ</center>

### 3.3.2 ナンドフラッシュ

&emsp; &emsp; K510 CRB は 128M Bytes の NAND フラッシュ メモリをオンボードし、起動コードやユーザー ファイルなどのデータを格納するために使用できます。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_5.jpg " width=75%>
</div>

<center>図 3-5 NAND フラッシュ メモリ</center>

### 3.3.2 TFカード

&emsp; &emsp; K510 CRB は TF カード ホルダーをマウントし、起動コードやユーザー ファイルなどのデータを格納するために TF カードを外部に接続できます。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_6.png">
</div>

<center>図 3-6 TF カードホルダー</center>

<div style="page-break-after:always"></div>

## 3.4 キーを押します

&emsp; &emsp; K510 CRBは、システム入力トリガやソフトウェア関連のその他の機能として、ユーザーがカスタムプログラミングを行うことができる2つのユーザータップキーをオンボードします。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_7.jpg" width=50%>
</div>

<center>図 3-7 キーを押します</center>

## 3.5 インジケータ

&emsp; &emsp; K510 CRBは、K510チップのGPIOピンに直接接続された発光ダイオードを搭載しています。

&emsp; &emsp; K510 CRBは、K510チップのGPIOピンに直接接続されたカラー発光ダイオードWS2812を搭載しています。

&emsp; &emsp; 2 つのライトをカスタム プログラムして点灯または消灯し、システム出力やソフトウェア関連のステータス表示などの機能として使用できます。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_8.jpg" width=60%>
</div>

<center>図 3-8 インジケータ</center>

<div style="page-break-after:always"></div>

## 3.6 起動モードとリセット

&emsp; &emsp; K510 CRBは、起動時にBOOT0とBOOT1の2つのピンのレベルを設定することで起動モードを選択する複数のストレージデバイスをオンボードし、0と1はローレベルとハイレベルを表します。

&emsp; &emsp; PCBは、次の図に示すダイヤルスイッチを介して起動モードを選択し、コアモジュール設計は、BOOT0とBOOT1のプルアップ設計を行い、ダイヤルコードオンマークONの片側は、対応するビットプルダウンが有効であることを示し、ON対応する反対側OFFはプルアップが有効であることを意味する。

&emsp; &emsp; K510 は、BOOT0 と BOOT1 の 2 つのハードウェア ピンの状態によってチップ ブート モードを決定し、ブート モードは次の表に示すように選択されます。

<center>表 2-1 起動モード</center>

| ブート1   | ブート0   | 起動方法      |
| ------- | ------- | ------------ |
| 0(オン)   | 0(オン)   | シリアルが起動します      |
| 0(オン)   | 1(オフ)  | SDカードが起動します      |
| 1(オフ)  | 0(オン)   | NANDFLASH が起動します |
| 1(オフ)  | 1(オフ)  | EMMC が起動します      |

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_9.jpg" width=60%>
</div>

<center>図3-9 リセットスイッチとスタートモードダイヤルスイッチ</center>

&emsp; &emsp; K510 CRBオンボードリセットボタンは図3-9のK2で、押すとシステムのハードウェアリセット動作が可能です。

<div style="page-break-after:always"></div>

## 3.7 Audio入出力

&emsp; &emsp; K510 CRB は、音声の入出力機能を実現するために、nuvoton のオーディオ コーデック チップ NAU88C22 を使用します。 オンボードマイク、標準3.5mmヘッドフォンソケット、2Pスピーカーコネクタが含まれています。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-10.jpg" width=60%>
</div>

<center>図 3-10 Audio</center>

## 3.8 USB OTGソケット

&emsp; &emsp; K510 CRB オンボード USB OTG ソケットは、USB host/device 機能を実装するために使用できます。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_11.jpg">
</div>

<center>図3-11 USB-OTGシート</center>

<div style="page-break-after:always"></div>

## 3.9 UART インターフェイス

&emsp; &emsp; K510 CRBは、ユーザーの開発と試運転を容易にするために、USB->UARTインターフェイスをオンボードし、PC-USBケーブルを介してK510のUARTシリアル通信とデバッグを行うことができます。 最初の使用には、セクション 4.2 を参照して、ロード ドライブが必要になる場合があります。 オンボードUARTインタフェースを次の図に示します。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_12.jpg" width=50%>
</div>

<center>図 3-12 USB-UART インターフェイス</center>

## 3.10 WIFI/BTモジュール

&emsp; &emsp; K510 CRB は、次の図に示すように、ネットワーク接続と Bluetooth 通信機能用の開発ボードを拡張する WIFI/BT 2 in-in-1 モジュール AP6212 をオンボードで提供します。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-13.jpg" width=40%>
</div>

<center>図3-13 WIFI/BTモジュール</center>

<div style="page-break-after:always"></div>

## 3.11 イーサネット

&emsp; &emsp; K510 CRB オンボード ギガビット イーサネット ホルダー、K510 はRGMII インターフェイスを介して PHY チップを外部接続することによって実現されます。 オンボードインタフェースを次の図に示します。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_14.jpg" width=60%>
</div>

<center>図 3-14 イーサネット インターフェイス</center>

## 3.12 hdmi出力

&emsp; &emsp; K510 CRBオンボードHDMI-Aメスシートは、K510のmipi dsiインタフェース出力変換を使用して、標準HDMIケーブルを介して外部ディスプレイを接続することができます。 オンボードインタフェースを次の図に示します。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_15.jpg" width=60%>
</div>

<center>図 3-15 HDMI インターフェイス</center>

 **注:**HDMI と 1080P TFT ディスプレイはどちらも mipi dsi で駆動されるため、2 つのディスプレイのみを選択し、同時に使用できず、ピン GPIO を制御して出力の 1 つを選択するように切り替えます。

<div style="page-break-after:always"></div>

## 3.13 ビデオ入力

&emsp; &emsp; K510 CRB は、MIPI CSI、DVP、電源、および GPIO の一部を 0.8 mm ピッチ ボードツーボード コネクタで引き出し、さまざまなシナリオやニーズに合わせてカメラ入力を可能にします。 オンボードインタフェースを次の図に示します。 インターフェイス定義を次の表に示します。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-16.jpg">
</div>

<center>図 3-16 Video IN インターフェイス</center>

<center>表 3-2 Video IN インターフェイス定義を示します</center>

| 番号 | 定義             | 番号 | 定義                       |
| ---- | ---------------- | ---- | --------------- |
| 1    | VDD_5V           | 60   | GPIO_1V8_59_DVP_D12      |
| 2    | VDD_5V           | 59   | GPIO_1V8_58_DVP_D11      |
| 3    | VDD_5V           | 58   | GPIO_1V8_50_DVP_D3       |
| 4    | VDD_5V           | 57   | GPIO_1V8_51_DVP_D4       |
| 5    | ティッカー              | 56   | GPIO_1V8_60_DVP_D13      |
| 6    | ティッカー              | 55   | GPIO_1V8_55_DVP_D8       |
| 7    | MIPI_CSI_D0_P    | 54   | GPIO_1V8_61_DVP_D14      |
| 8    | MIPI_CSI_D0_N    | 53   | GPIO_1V8_52_DVP_D5       |
| 9    | ティッカー              | 52   | GPIO_1V8_47_DVP_D0       |
| 10   | MIPI_CSI_CLK0_P  | 51   | GPIO_1V8_56_DVP_D9       |
| 11   | MIPI_CSI_CLK0_N  | 50   | GPIO_1V8_53_DVP_D6       |
| 12   | ティッカー              | 49   | GPIO_1V8_57_DVP_D10      |
| 13   | MIPI_CSI_D1_P    | 48   | GPIO_1V8_48_DVP_D1       |
| 14   | MIPI_CSI_D1_N    | 47   | GPIO_1V8_54_DVP_D7       |
| 15   | ティッカー              | 46   | GPIO_1V8_64_DVP_HREF     |
| 16   | MIPI_CSI_D2_N    | 45   | GPIO_1V8_49_DVP_D2       |
| 17   | MIPI_CSI_D2_P    | 44   | GPIO_1V8_65_DVP_DEN      |
| 18   | ティッカー              | 43   | GPIO_1V8_66_DVP_PCLK     |
| 19   | MIPI_CSI_CLK1_N  | 42   | GPIO_1V8_62_DVP_D15      |
| 20   | MIPI_CSI_CLK1_P  | 41   | GPIO_1V8_63_DVP_VSYNC    |
| 21   | ティッカー              | 40   | GPIO_1V8_82 |
| 22   | MIPI_CSI_D3_N    | 39   | GPIO_1V8_67  |
| 23   | MIPI_CSI_D3_P    | 38   | GPIO_1V8_68  |
| 24   | ティッカー              | 37   | GPIO_1V8_72  |
| 25   | MIPI_CSI_I2C_SCL | 36   | GPIO_1V8_73  |
| 26   | MIPI_CSI_I2C_SCA | 35   | GPIO_1V8_74  |
| 27   | ティッカー              | 34   | ティッカー          |
| 28   | ティッカー              | 33   | ティッカー          |
| 29   | 1V8              | 32   | 3V3          |
| 30   | 1V8              | 31   | 3V3          |

**注意:**接続ピンのレベル範囲に注意し、間違った電圧入力がK510チップに永久的に損傷するのを防ぐために、外部接続時に注意してください。

<div style="page-break-after:always"></div>

## 3.14 ビデオ出力

&emsp; &emsp; K510 CRBは、次の図に示すように、外部LCDディスプレイを接続するための0.5mmピッチ30Pフリップカバー下部FPCコネクタをオンボードします。 インターフェイス定義を次の表に示します。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-17.jpg">
</div>

<center>図 3-17 Video Out インターフェイス</center>

<center>表 3-3 Video Out インターフェイス定義を示します</center>

| 番号 | 定義              | 番号 | 定義             |
| ---- | ----------------- | ---- | ---------------- |
| 1    | ティッカー               | 16   | MIPI_DSI_D1_N    |
| 2    | ティッカー               | 17   | MIPI_DSI_D1_P    |
| 3    | VDD_5V            | 18   | ティッカー              |
| 4    | VDD_5V            | 19   | MIPI_DSI_CLK_N   |
| 5    | VDD_3V3           | 20   | MIPI_DSI_CLK_P   |
| 6    | VDD_3V3           | 21   | ティッカー              |
| 7    | ティッカー               | 22   | MIPI_DSI_D0_N    |
| 8    | TOUCH_1V8_I2C_SCL | 23   | MIPI_DSI_D0_P    |
| 9    | TOUCH_1V8_I2C_SDA | 24   | ティッカー              |
| 10   | TOUCH_1V8_INT     | 25   | MIPI_DSI_D3_N    |
| 11   | TOUCH_1V8_RST     | 26   | MIPI_DSI_D3_P    |
| 12   | ティッカー               | 27   | ティッカー              |
| 13   | MIPI_DSI_D2_N     | 28   | MIPI_DSI_LCD_RST |
| 14   | MIPI_DSI_D2_P     | 29   | MIPI_DSI_LCD_EN  |
| 15   | ティッカー               | 30   | ティッカー              |

<div style="page-break-after:always"></div>

## 3.15 インターフェイスを拡張します

&emsp; &emsp; カスタム拡張機能の実装を容易にするために、K510 CRBには30Pの2.54mm拡張ピンが予約されており、電源とGPIOの一部を含むものが引き出され、ユーザーはソフトウェアiomux操作を介してI2C、UART、SPIなどのハードウェアリソースを適切なGPIOにマッピングし、対応する機能の外部接続と拡張を実現します。 オンボードインタフェースを次の図に示します。 詳細な定義を次の表に示します。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw-3-18.jpg">
</div>

<center>図 3-18 40P ピン拡張インターフェイス</center>

<center>表 3-4 インターフェイス定義の拡張</center>

| 番号 | 定義         | 番号 | 定義         |
| ---- | ------------ | ---- | ------------ |
| 1    | VDD_1V8      | 2    | ティッカー          |
| 3    | VDD_1V8      | 4    | ティッカー          |
| 5    | VDD_3V3      | 6    | ティッカー          |
| 7    | VDD_3V3      | 8    | ティッカー          |
| 9    | VDD_5V       | 10   | ティッカー          |
| 11   | VDD_5V       | 12   | GPIO_1V8_95  |
| 13   | GPIO_3V3_114 | 14   | GPIO_3V3_115 |
| 15   | GPIO_1V8_92  | 16   | GPIO_1V8_96  |
| 17   | GPIO_1V8_105 | 18   | GPIO_1V8_107 |
| 19   | GPIO_1V8_104 | 20   | GPIO_1V8_106 |
| 21   | GPIO_1V8_118 | 22   | GPIO_1V8_119 |
| 23   | GPIO_1V8_93  | 24   | GPIO_1V8_94  |
| 25   | GPIO_3V3_125 | 26   | GPIO_3V3_124 |
| 27   | GPIO_3V3_127 | 28   | GPIO_3V3_126 |
| 29   | ティッカー          | 30   | ティッカー          |

**注意:**接続ピンのレベル範囲に注意し、間違った電圧入力がK510チップに永久的に損傷するのを防ぐために、外部接続時に注意してください。

<div style="page-break-after:always"></div>

# 4 開発ボードの使用

## 4.1 ドライブをインストールします

&emsp; &emsp; K510 CRBはCH340Eを搭載し、USB-UART通信機能を実現するため、使用前に対応するドライバを取り付ける必要があります。

&emsp; &emsp; パッケージ内のドライバを使用するか、次のアドレスでダウンロードしてインストールします。

&emsp;&emsp;<http://www.wch.cn/product/CH340.html>

## 4.2 ファームウェアのバーンイン

&emsp; &emsp; K510_SDK_Build_and_Burn_Guideドキュメントを参照してください[](./K510_SDK_Build_and_Burn_Guide.md)。

## 4.3 スイッチマシン

&emsp; &emsp; 1)電源コードとUSBデバッグケーブルを取り付けます。

&emsp; &emsp; 2)ダイヤルスイッチはTFカードから起動することを選択します。

&emsp; &emsp; 3)3.2節に示す方法でスイッチをトグルして電源投入を行います。

## 4.4 シリアルポートデバッグ

&emsp; &emsp; ドライブのインストールが完了したら、K510 CRB の電源投入を行い、PC のデバイス マネージャ ポートにポートが表示されます。

&emsp; &emsp; シリアルデバッグツールを使用して、デバイスのポート番号を開き、ボーレート115200を設定します。

&emsp; &emsp; 次の図に示すように、デバイスは "COM6" で、PC デバイス マネージャに表示される場合が優先されます。

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_4_1.jpg">
</div>

<center>図 4-1 インストールが完了した後のデバイス マネージャを駆動します</center>

**免責事項を翻訳します**  
お客様の便宜のために、カナアンはAI翻訳プログラムを使用してテキストを複数の言語に翻訳し、エラーが含まれている可能性があります。 当社は、提供される翻訳の正確性、信頼性、または適時性を保証するものではありません。 カナアンは、翻訳された情報の正確性または信頼性への依存に起因するいかなる損失または損害についても責任を負いません。 異なる言語翻訳間でコンテンツの違いがある場合は、簡体字中国語版が優先されます。

翻訳エラーや不正確な問題を報告する場合は、メールでお問い合わせください。
