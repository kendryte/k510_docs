![](../zh/images/canaan-cover.png)
&nbsp;
&nbsp;
**<font face="黑体" size="6" style="float:right">K510 CRB V1.2 하드웨어 가이드</font>**

<font face="黑体" size=100>&nbsp;
&nbsp;
&nbsp;</font>

<font face="黑体"  size=3>문서 버전: V1.0.0</font>

<font face="黑体"  size=3>게시 날짜: 2022-03-15</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**면책 조항**</font>
귀하가 구매한 제품, 서비스 또는 기능은 베이징 Jiananges 정보 기술 유한 회사(이하 "회사")의 상업 계약 및 약관의 적용을 받으며, 이 문서에 설명된 제품, 서비스 또는 기능의 전부 또는 일부는 구매 또는 사용의 범위를 벗어납니다. 계약에 달리 합의하지 않는 한, 회사는 본 문서의 진술, 정보, 내용의 정확성, 신뢰성, 완전성, 마케팅, 특정 목적 및 비침략성에 대해 명시적 또는 묵시적으로 어떠한 진술이나 보증도 하지 않습니다. 달리 합의하지 않는 한, 이 문서는 사용 지침의 참조로만 사용됩니다.
이 문서의 내용은 제품 버전 업그레이드 또는 기타 이유로 인해 예고 없이 수시로 업데이트되거나 수정될 수 있습니다.

**<font face="黑体"  size=3>상표 고지</font>**

베이징 <img src="../zh/images/canaan-logo.png" style="zoom:33%;" />Jianan Jets 정보 기술 유한 공사의 상표는 Jianan, Jianan 및 Jianan의 다른 상표입니다. 이 문서에 언급될 수 있는 기타 모든 상표 또는 등록 상표는 해당 소유자가 소유합니다.

**<font face="黑体"  size=3>저작권 ©2022 베이징 Jiananjets 정보 기술 유한 회사</font>**
이 문서는 K510 플랫폼 개발 및 설계에만 적용되며, 어떠한 단위나 개인도 회사의 서면 허가 없이 이 문서의 일부 또는 전부를 어떤 형태로든 배포할 수 없습니다.

**<font face="黑体"  size=3>베이징 Jiananjets 정보 기술 유한 회사</font>**
웹 사이트: canaan-creative.com
비즈니스 문의: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# 서문
**<font face="黑体"  size=5>문서의 목적</font>**
이 문서는 엔지니어가 k510 sdk의 컴파일 및 레코딩을 이해하는 데 도움이 되는 K510 sdk에 대한 컴패니언 문서입니다.

**<font face="黑体"  size=5>독자 개체입니다</font>**

이 문서(이 가이드)가 주로 적용되는 사람:

- 소프트웨어 개발자
- 기술 지원 담당자

**<font face="黑体"  size=5>레코드를 수정합니다</font>**
 <font face="宋体"  size=2>개정 레코드에는 각 문서 업데이트에 대한 설명이 누적됩니다. 문서의 최신 버전에는 이전 버전의 모든 업데이트가 포함되어 있습니다. </font>

| 버전 번호입니다 | 수정자    | 개정일입니다   | 개정 지침           |
| :----- | --------- | ---------- | ------------------ |
| V1.0.0 | AI 제품 부서 | 2022-03-15 | |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |
|        |           |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>카탈로그</font>**

[목차]

<div style="page-break-after:always"></div>

# 1 개요

&emsp; &emsp; K510 CRB는 Canan Kendryte K510 AI 칩 개발을 위한 레퍼런스 설계, 칩 디버깅 및 테스트, 사용자 제품 개발 검증 등을 결합한 하드웨어 개발 플랫폼으로 K510 칩의 강력한 컴퓨팅 파워와 기능 등을 시연하는 데 사용된다. 동시에 고객에게 K510 칩 기반 하드웨어 참조 설계를 제공하여 고객이 참조 설계 모듈 회로를 수정하거나 단순히 수정할 필요가 없도록 K510 칩을 핵심으로 하는 제품 하드웨어 개발을 완료할 수 있습니다.

&emsp; &emsp; K510 CRB는 K510 칩의 하드웨어 개발, 응용 프로그램 소프트웨어 설계, 디버깅 및 실행을 지원하며, 다양한 사용 환경을 고려하여 칩의 완전한 기능을 검증하기 때문에 다양한 인터페이스가 완료되고 설계가 비교적 완전합니다. K510 CRB는 USB 케이블을 통해 PC에 연결하거나, 기본 개발 시스템으로 사용하거나, 다음과 같은 장치 및 구성 요소를 연결하는 보다 완전한 개발 시스템 및 데모 환경을 구현할 수 있습니다.

- 전원 공급 장치

- TF 카드 스토리지 디바이스

- MIPI DSI LCD 디스플레이

- MIPI CSI 카메라 모듈

- DVP 카메라 모듈

- 이더넷 네트워크 케이블

- HDMI 디스플레이

- 헤드폰 또는 스피커

- 예비 부품을 확장합니다

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-K510_Core.png">
</div>

  <center>그림 1-1 K510 CRB 렌더링</center>

    **禁止事项**

  1. 전원을 뽑는 코어 모듈 및 주변 모듈은 허용되지 않습니다!
  2. 정전기 방전 또는 정전기 방지 조치 없이 제품을 직접 작동하는 것은 금지되어 있습니다.
  3. 유기 용제 또는 부식성 액체로 제품을 세척하는 것은 금지되어 있습니다.
  4. 물리적 손상을 일으킬 수 있는 노크, 비틀기 및 기타 작업은 금지됩니다.

    **주의 사항**

  1. 이 제품을 작동하기 전에 인체에 정전기를 방출 한 후 정전기 팔찌를 착용하는 것이 좋습니다.
  2. 작동하기 전에 이 문서에 설명된 허용 범위 내에서 베이스 플레이트의 공급 전압과 어댑터 전압을 확인하십시오.
  3. 설계하기 전에 이 문서 및 엔지니어링 문서의 고려 사항을 읽어 보시기 바랍니다.
  4. 고온, 고습, 고부식 환경에서 제품을 사용하려면 열 방출, 배수, 밀봉 및 기타 특수 처리가 필요합니다.
  5. 직접 수리하거나 분해하지 마십시오, 그렇지 않으면 무료 애프터 서비스를 즐길 수 없습니다.

<div style="page-break-after:always"></div>

## 1.1 블록 다이어그램

&emsp; &emsp; 시스템 블록 다이어그램은 K510 CRB의 설계 원칙과 구성 요소 간의 관계를 설명하여 K510 CRB의 사용과 개발자가 전체 시스템의 아키텍처와 원리에 대한 직관적인 이해를 가질 수 있도록 합니다.

&emsp; &emsp; K510 기능에 대한 자세한 내용은 K510 Full Datasheet을 참조하십시오.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_1_2.png">
</div>

<center>그림 1-2 K510 CRB 구성</center>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_1_3.png">
</div>

<center>그림 1-3 K510 CRB 블록 다이어그램 </center>

<div style="page-break-after:always"></div>

&emsp; &emsp; K510 CRB 개발 키트에는 다음과 같은 주요 구성 요소가 포함되어 있습니다.

| 부품 | 수량입니다 |
| :-: | :-: |
| K510 CRB 마더보드 | 1 |
| USB 타입 C线缆 | 2 |
| Micro USB OTG 케이블 | 1 |
| MIPI DSI 디스플레이, 해상도 1920x1080 | 1 |
| MIPI CSI 카메라 서브플레이트, 온보드 Sony IMX219 image sensor 2개 | 1 |
| 아크릴 보호 케이스 | 1 |

<div style="page-break-after:always"></div>

## 1.2 기능 개요

&emsp; &emsp; K510 SDK는 빌드루트를 기본 프레임워크로, K510 linux kernel(linux 버전 4.17.0), u-boot(u-boot 버전 2020.01), riscv-pk-k510으로 구성됩니다

&emsp; &emsp; K510 CRB V1.2의 주요 기능(이 문서의 후속 버전은 특별한 선언이 없는 경우 V1.2입니다)은 다음과 같습니다.

- PMIC: 전원 관리
- 32비트 LPDDR3EE, 총 용량 512MByte
- 8bit eMMC, 총 용량 4GByte
- QSPI NAND, 총 용량 128MByte
- TF 카드: 외부 확장 TF 카드 스토리지를 지원합니다.
- USB OTG: 시스템 업그레이드 사용, Host/Device 전환 지원
- SDIO WIFI: 무선 인터넷 및 블루투스 연결을 지원합니다
- Audio: 음성 입력 및 출력이 지원됩니다
- PDM MIC: VAD 웨이크업 기능
- Uart &JTAG Debug: 보드 Debug 사용
- Video Input: 2소켓 MIPI CSI 2lane 카메라 입력
- Video Output: MIPI DSI 4lane, 1080P 디스플레이
- RGMII: 기가비트 이더넷 연결
- HDMI: 고화질 멀티미디어 인터페이스
- 확장 인터페이스: 전원 공급 장치, GPIO, I2C, SPI
- 키, 표시등

<div style="page-break-after:always"></div>

# 2 하드웨어 리소스 소개

## 2.1 전체 효과 맵

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_1.png" width=80%>
</div>

<center> 그림 2-1 마더보드 전면 이미지 </center>

<div style="page-break-after:always"></div>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_2.png" width=80%>
</div>

<center> 그림 2-1 마더보드 뒷면 </center>

<div style="page-break-after:always"></div>

## 2.2 구조 및 인터페이스 다이어그램

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2_3.png" width=120%>
</div>

<center> 그림 2-3 마더보드 앞면의 장치 위치입니다 </center>

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_2-4.png" width=120%>
</div>

<center> 그림 2-4 마더보드 뒷면 </center>

<div style="page-break-after:always"></div>

## 2.3 전원 블록 다이어그램

&emsp; &emsp; K510 CRB는 DC-5V를 전체 보드의 입력 전원으로 사용하여 K510 CORE 코어 모듈에 DC-5V를 제공하는 동시에 두 개의 DC-DC를 통해 베이스 플레이트의 다른 주변 장치에 1.8V 및 3.3V 전원 공급 장치를 제공합니다.

## 2.4 I2C 장치 주소

<center>표 2-1 I2C 장치 주소 표</center>

| 이름입니다 | 핀(SCL, SDA) | 주소입니다 | 참고 사항 |
| :-: | :-: | :-: | :-: |
| 터치 스크린 | IO_103、IO_102 | 0x14 또는 0x5D | |
| 증권 시세 표시기 | IO_117、IO_116 | 0x3B | |
| 오디오 코덱 | IO_117、IO_116 | 0x1A | |
| MIPI CSI 카메라0 | IO_120、IO_121 | 0x10 | |
| MIPI CSI 카메라1 | IO_47、IO_48   | 0x10 | |

## 2.5 회로도

&emsp; &emsp; K510 CRB 보드에 대한 참조 회로도는[release](https://github.com/kendryte/k510_docs/releases)에서 다운로드하십시오.

<div style="page-break-after:always"></div>

# 3 보드 섹션 소개

## 3.1 코어 모듈

&emsp; &emsp; K510 CRB를 사용하여 학습하고 개발하기 전에 K510 설명서의 칩 세부 아키텍처를 참조하여 K510의 전원 공급 장치, 스토리지, 컴퓨팅 리소스 및 주변 장치에 대한 심층적인 이해를 얻고 칩 솔루션의 친숙함과 개발을 용이하게 하는 것이 좋습니다. K510 코어 보드는 그림 3-1에 있습니다.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_1.png">
</div>

<center>그림 3-1 K510 코어 모듈</center>

<div style="page-break-after:always"></div>

## 3.2 전원 공급 장치를 입력합니다

&emsp; &emsp; K510 CRB는 외부 5V 전원 공급 장치, 두 개의 USB type C 인터페이스를 사용하여 개발 보드에 전원을 공급할 수 있으며, UART 인터페이스는 컴퓨터에 연결되며, 컴퓨터의 USB 인터페이스는 500mA 전류만 제공할 수 있으며, 전원 공급 장치가 부족할 때 DC:5V에서 어댑터를 동시에 사용하십시오. 인터페이스는 다음 그림과 같습니다.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_2.png" width=60%>
</div>

<center> 그림 3-2 전원 입력 커넥터 </center>

**참고 : 5V 전원 공급 장치의 사용을 제한, 빠른 충전 어댑터를 사용할 때, 빠른 충전 어댑터 오류 출력이 5V 전원 공급 장치보다 높은 원인이되지 않도록, 휴대 전화 및 기타 장치를 연결하지 않으려고, 개발 보드 전원 공급 장치의 부분 손상을 일으킬 수 있습니다.**
&emsp; &emsp; 아래 그림과 같이 K2 토글 스위치를 사용하여 전원 켜기 및 끄기 작업을 수행합니다.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-3.jpg" width=50%>
</div>

<center>그림 3-3 전원 스위치에 대한 설명입니다</center>

<div style="page-break-after:always"></div>

## 3.3 저장 장치

&emsp; &emsp; K510 CRB에는 DDR, eMMC, NAND Flash, TF Card 등 다양한 저장 장치가 온보드되어 있습니다.

### 3.3.1 eMMC

&emsp; &emsp; 핵심 모듈에 위치한 K510 CRB 온보드 4G Bytes eMMC 메모리는 시작 코드 및 사용자 파일과 같은 데이터를 저장하는 데 사용할 수 있습니다.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-eMMC.png" width=70%>
</div>

<center>그림 3-4 eMMC 메모리</center>

### 3.3.2 낸드플래시

&emsp; &emsp; K510 CRB는 128M Bytes의 NAND Flash 메모리를 온보드하여 시작 코드 및 사용자 파일과 같은 데이터를 저장할 수 있습니다.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_5.jpg " width=75%>
</div>

<center>그림 3-5 NAND Flash 메모리</center>

### 3.3.2 TF 카드

&emsp; &emsp; K510 CRB는 부팅 코드 및 사용자 파일과 같은 데이터를 저장하기 위해 외부 TF 카드를 사용할 수 있는 TF 카드 홀더를 온보드로 제공합니다.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/image-hw_3_6.png">
</div>

<center>그림 3-6 TF 카드 홀더</center>

<div style="page-break-after:always"></div>

## 3.4 키

&emsp; &emsp; K510 CRB는 두 개의 사용자 버튼이 포함되어 있으며, 사용자는 시스템 입력 트리거 또는 소프트웨어 관련 기타 기능으로 사용자 정의 할 수 있습니다.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_7.jpg" width=50%>
</div>

<center>그림 3-7 키</center>

## 3.5 표시등

&emsp; &emsp; K510 CRB는 K510 칩의 GPIO 핀에 직접 연결된 발광 다이오드를 플레이트에 부착합니다.

&emsp; &emsp; K510 CRB는 K510 칩의 GPIO 핀에 직접 연결된 컬러 발광 다이오드 WS2812를 플레이트에 부착합니다.

&emsp; &emsp; 시스템 출력 또는 소프트웨어 관련 상태 표시와 같은 기능으로 사용할 수 있는 두 개의 표시기를 사용자 지정하여 켜거나 끕니다.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_8.jpg" width=60%>
</div>

<center>그림 3-8 표시등</center>

<div style="page-break-after:always"></div>

## 3.6 시작 모드 및 재설정

&emsp; &emsp; K510 CRB는 부팅 시 BOOT0 및 BOOT1 핀의 레벨을 구성하여 시작 모드를 선택하는 다양한 저장 장치를 온보드하며, 0과 1은 낮음과 높음을 나타냅니다.

&emsp; &emsp; PCB는 아래 그림과 같이 다이얼 스위치를 통해 시작 모드를 선택하며, 코어 모듈은 BOOT0 및 BOOT1에 대한 풀업 설계를 수행하도록 설계되었으며, 다이얼링은 ON의 한쪽에 표시된 해당 비트 풀아래를 나타내며, ON의 다른 쪽 OFF는 풀업이 유효합니다.

&emsp; &emsp; K510은 BOOT0 및 BOOT1 하드웨어 핀의 상태에 따라 칩 시작 모드를 결정하며, 시작 모드 선택은 아래 표에 나와 있습니다.

<center>표 2-1 시작 모드</center>

| 부트1   | 부트0   | 시작 방법      |
| ------- | ------- | ------------ |
| 0(켜짐)   | 0(켜짐)   | 직렬 포트가 시작됩니다      |
| 0(켜짐)   | 1(꺼짐)  | SD 카드가 시작됩니다      |
| 1(꺼짐)  | 0(켜짐)   | NANDFLASH가 시작됩니다 |
| 1(꺼짐)  | 1(꺼짐)  | EMMC가 시작됩니다      |

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_9.jpg" width=60%>
</div>

<center>그림 3-9 리셋 스위치 및 시작 모드 다이얼 스위치</center>

&emsp; &emsp; K510 CRB 온보드 리셋 버튼은 그림 3-9의 K2이며, 누르면 시스템의 하드웨어 재설정이 가능합니다.

<div style="page-break-after:always"></div>

## 3.7 Audio 입력 및 출력

&emsp; &emsp; K510 CRB는 음성 입력 및 출력 기능을 위해 nuvoton의 오디오 코덱 칩 NAU88C22를 사용합니다. 온보드 마이크, 표준 3.5mm 헤드폰 소켓 및 2P 스피커 커넥터가 포함되어 있습니다.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-10.jpg" width=60%>
</div>

<center>그림 3-10 Audio</center>

## 3.8 USB OTG 소켓

&emsp; &emsp; K510 CRB 온보드 USB OTG 소켓은 USB host/device 기능을 구현하는 데 사용할 수 있습니다.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_11.jpg">
</div>

<center>그림 3-11 USB-OTG 시트</center>

<div style="page-break-after:always"></div>

## 3.9 UART 인터페이스

&emsp; &emsp; K510 CRB는 사용자 개발 및 디버깅을 용이하게 하기 위해 USB-> UART 인터페이스를 온보드로 제공하며 PC-USB 케이블을 통해 K510의 UART 직렬 통신 및 디버깅을 수행할 수 있습니다. 4.2절에 설명된 대로 초기 사용 시 드라이버를 로드해야 할 수 있습니다. 온보드 UART 인터페이스는 아래 그림과 같습니다.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_12.jpg" width=50%>
</div>

<center>그림 3-12 USB-UART 커넥터</center>

## 3.10 WIFI/BT 모듈

&emsp; &emsp; K510 CRB는 다음 그림과 같이 개발 보드의 네트워크 연결 및 Bluetooth 통신 기능을 확장하기 위해 WIFI/BT 2-in-1 모듈 AP6212를 온보드로 제공합니다.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-13.jpg" width=40%>
</div>

<center>그림 3-13 WIFI/BT 모듈</center>

<div style="page-break-after:always"></div>

## 3.11 이더넷

&emsp; &emsp; K510 CRB 온보드 기가비트 이더넷 시트, K510은 RGMII 인터페이스 외부 PHY 칩을 통해 구현됩니다. 온보드 인터페이스는 아래 그림과 같습니다.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_14.jpg" width=60%>
</div>

<center>그림 3-14 이더넷 인터페이스</center>

## 3.12 hdmi 출력

&emsp; &emsp; K510 CRB 온보드 HDMI-A 암은 K510의 mipi dsi 인터페이스 출력 변환을 사용하여 표준 HDMI 케이블을 통해 외부 디스플레이를 연결할 수 있습니다. 온보드 인터페이스는 아래 그림과 같습니다.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3_15.jpg" width=60%>
</div>

<center>그림 3-15 HDMI 커넥터</center>

 **참고**: HDMI 및 1080P TFT 디스플레이는 모두 mipi dsi 드라이버를 사용하기 때문에 두 가지 옵션만 표시할 수 있으며 동시에 사용할 수 없으며 스위치는 핀 GPIO를 제어하여 출력 중 하나를 선택할 수 있습니다.

<div style="page-break-after:always"></div>

## 3.13 비디오 입력

&emsp; &emsp; K510 CRB는 0.8mm 피치 기판 간 커넥터를 통해 MIPI CSI, DVP, 전원 공급 장치 및 일부 GPIO를 유도하여 다양한 시나리오와 다양한 요구 사항에 대한 카메라 입력을 가능하게 합니다. 온보드 인터페이스는 아래 그림과 같습니다. 인터페이스 정의는 다음 표에 나와 있습니다.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-16.jpg">
</div>

<center>그림 3-16 Video IN 인터페이스</center>

<center>표 3-2 Video IN 인터페이스 정의</center>

| 번호입니다 | 정의             | 번호입니다 | 정의                       |
| ---- | ---------------- | ---- | --------------- |
| 1    | VDD_5V           | 60   | GPIO_1V8_59_DVP_D12      |
| 2    | VDD_5V           | 59   | GPIO_1V8_58_DVP_D11      |
| 3    | VDD_5V           | 58   | GPIO_1V8_50_DVP_D3       |
| 4    | VDD_5V           | 57   | GPIO_1V8_51_DVP_D4       |
| 5    | GND              | 56   | GPIO_1V8_60_DVP_D13      |
| 6    | GND              | 55   | GPIO_1V8_55_DVP_D8       |
| 7    | MIPI_CSI_D0_P    | 54   | GPIO_1V8_61_DVP_D14      |
| 8    | MIPI_CSI_D0_N    | 53   | GPIO_1V8_52_DVP_D5       |
| 9    | GND              | 52   | GPIO_1V8_47_DVP_D0       |
| 10   | MIPI_CSI_CLK0_P  | 51   | GPIO_1V8_56_DVP_D9       |
| 11   | MIPI_CSI_CLK0_N  | 50   | GPIO_1V8_53_DVP_D6       |
| 12   | GND              | 49   | GPIO_1V8_57_DVP_D10      |
| 13   | MIPI_CSI_D1_P    | 48   | GPIO_1V8_48_DVP_D1       |
| 14   | MIPI_CSI_D1_N    | 47   | GPIO_1V8_54_DVP_D7       |
| 15   | GND              | 46   | GPIO_1V8_64_DVP_HREF     |
| 16   | MIPI_CSI_D2_N    | 45   | GPIO_1V8_49_DVP_D2       |
| 17   | MIPI_CSI_D2_P    | 44   | GPIO_1V8_65_DVP_DEN      |
| 18   | GND              | 43   | GPIO_1V8_66_DVP_PCLK     |
| 19   | MIPI_CSI_CLK1_N  | 42   | GPIO_1V8_62_DVP_D15      |
| 20   | MIPI_CSI_CLK1_P  | 41   | GPIO_1V8_63_DVP_VSYNC    |
| 21   | GND              | 40   | GPIO_1V8_82 |
| 22   | MIPI_CSI_D3_N    | 39   | GPIO_1V8_67  |
| 23   | MIPI_CSI_D3_P    | 38   | GPIO_1V8_68  |
| 24   | GND              | 37   | GPIO_1V8_72  |
| 25   | MIPI_CSI_I2C_SCL | 36   | GPIO_1V8_73  |
| 26   | MIPI_CSI_I2C_SCA | 35   | GPIO_1V8_74  |
| 27   | GND              | 34   | GND          |
| 28   | GND              | 33   | GND          |
| 29   | 1V8              | 32   | 3V3          |
| 30   | 1V8              | 31   | 3V3          |

**참고**: 잘못된 전압 입력이 K510 칩을 영구적으로 손상시키지 않도록 외부 연결 시 연결된 핀의 레벨 범위에 주의를 기울이십시오.

<div style="page-break-after:always"></div>

## 3.14 비디오 출력

&emsp; &emsp; K510 CRB는 아래 그림과 같이 외부 LCD 디스플레이를 연결하기 위해 0.5mm 피치 30P 플립 FPC 커넥터를 함께 제공합니다. 인터페이스 정의는 다음 표에 나와 있습니다.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_3-17.jpg">
</div>

<center>그림 3-17 Video Out 인터페이스</center>

<center>표 3-3 Video Out 인터페이스 정의</center>

| 번호입니다 | 정의              | 번호입니다 | 정의             |
| ---- | ----------------- | ---- | ---------------- |
| 1    | GND               | 16   | MIPI_DSI_D1_N    |
| 2    | GND               | 17   | MIPI_DSI_D1_P    |
| 3    | VDD_5V            | 18   | GND              |
| 4    | VDD_5V            | 19   | MIPI_DSI_CLK_N   |
| 5    | VDD_3V3           | 20   | MIPI_DSI_CLK_P   |
| 6    | VDD_3V3           | 21   | GND              |
| 7    | GND               | 22   | MIPI_DSI_D0_N    |
| 8    | TOUCH_1V8_I2C_SCL | 23   | MIPI_DSI_D0_P    |
| 9    | TOUCH_1V8_I2C_SDA | 24   | GND              |
| 10   | TOUCH_1V8_INT     | 25   | MIPI_DSI_D3_N    |
| 11   | TOUCH_1V8_RST     | 26   | MIPI_DSI_D3_P    |
| 12   | GND               | 27   | GND              |
| 13   | MIPI_DSI_D2_N     | 28   | MIPI_DSI_LCD_RST |
| 14   | MIPI_DSI_D2_P     | 29   | MIPI_DSI_LCD_EN  |
| 15   | GND               | 30   | GND              |

<div style="page-break-after:always"></div>

## 3.15 인터페이스를 확장합니다

&emsp; &emsp; 사용자가 사용자 정의 확장 기능을 쉽게 달성 할 수 있도록, K510 CRB는 30P 2.54mm 확장 핀을 예약, 전원 공급 장치 및 GPIO의 일부를 포함, 사용자는 소프트웨어 iomux 작업을 통해, I2C, UART, SPI 및 기타 하드웨어 리소스는 해당 GPIO에 매핑 할 수 있습니다, 해당 기능의 외부 연결 및 확장을 달성하기 위해. 온보드 인터페이스는 아래 그림과 같습니다. 자세한 정의는 다음 표에 나와 있습니다.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw-3-18.jpg">
</div>

<center>그림 3-18 40P 핀 확장 인터페이스</center>

<center>표 3-4는 인터페이스 정의를 확장합니다</center>

| 번호입니다 | 정의         | 번호입니다 | 정의         |
| ---- | ------------ | ---- | ------------ |
| 1    | VDD_1V8      | 2    | GND          |
| 3    | VDD_1V8      | 4    | GND          |
| 5    | VDD_3V3      | 6    | GND          |
| 7    | VDD_3V3      | 8    | GND          |
| 9    | VDD_5V       | 10   | GND          |
| 11   | VDD_5V       | 12   | GPIO_1V8_95  |
| 13   | GPIO_3V3_114 | 14   | GPIO_3V3_115 |
| 15   | GPIO_1V8_92  | 16   | GPIO_1V8_96  |
| 17   | GPIO_1V8_105 | 18   | GPIO_1V8_107 |
| 19   | GPIO_1V8_104 | 20   | GPIO_1V8_106 |
| 21   | GPIO_1V8_118 | 22   | GPIO_1V8_119 |
| 23   | GPIO_1V8_93  | 24   | GPIO_1V8_94  |
| 25   | GPIO_3V3_125 | 26   | GPIO_3V3_124 |
| 27   | GPIO_3V3_127 | 28   | GPIO_3V3_126 |
| 29   | GND          | 30   | GND          |

**참고**: 잘못된 전압 입력이 K510 칩을 영구적으로 손상시키지 않도록 외부 연결 시 연결된 핀의 레벨 범위에 주의를 기울이십시오.

<div style="page-break-after:always"></div>

# 4 보드 사용

## 4.1 드라이버를 설치합니다

&emsp; &emsp; K510 CRB는 USB-UART 통신 기능을 달성하기 위해 CH340E를 온보드하므로 사용하기 전에 해당 드라이버를 설치해야 합니다.

&emsp; &emsp; 패키지의 드라이버를 사용하거나 다음 주소로 다운로드하여 설치하십시오.

&emsp;&emsp;<http://www.wch.cn/product/CH340.html>

## 4.2 펌웨어 레코딩

&emsp; &emsp; K510_SDK_Build_and_Burn_Guide 설명서를 참조하십시오[](./K510_SDK_Build_and_Burn_Guide.md).

## 4.3 스위치

&emsp; &emsp; 1) 전원 코드 및 USB 디버그 케이블을 설치합니다.

&emsp; &emsp; 2) 전화 걸기 스위치는 TF 카드에서 부팅하도록 선택합니다.

&emsp; &emsp; 3) 섹션 3.2에 표시된 방법에 따라 스위치를 켜서 전원을 끄십시오.

## 4.4 직렬 포트 디버깅

&emsp; &emsp; 드라이버 설치가 완료되면 K510 CRB의 전원이 켜지며, 이 때 PC의 장치 관리자 포트에 포트가 나타납니다.

&emsp; &emsp; 직렬 포트 디버깅 도구를 사용하여 장치의 포트 번호인 115200을 엽니다.

&emsp; &emsp; 아래 그림과 같이 장치는 PC 장치 관리자에 표시된 대로 "COM6"입니다.

<div align="center">
    <img src="../zh/images/hw_crb_v1_2/clip_hw_4_1.jpg">
</div>

<center>그림 4-1은 설치가 완료된 후 장치 관리자를 구동합니다</center>

**번역 면책 조항**  
고객의 편의를 위해 Canan은 AI 번역 프로그램을 사용하여 오류를 포함할 수 있는 여러 언어로 텍스트를 번역합니다. 당사는 제공된 번역의 정확성, 신뢰성 또는 적시성을 보장하지 않습니다. Canan은 번역된 정보의 정확성이나 신뢰성에 의존하여 발생하는 손실이나 손해에 대해 책임을 지지 않습니다. 언어 번역 간에 콘텐츠 차이가 있는 경우 중국어 간체 버전이 우선합니다.

번역 오류 또는 부정확한 문제를 신고하려면 이메일로 문의하시기 바랍니다.
