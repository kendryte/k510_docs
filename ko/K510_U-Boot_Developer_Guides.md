![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 U-부트 개발자 안내서</font>**

<font face="黑体"  size=3>문서 버전: V1.0.0</font>

<font face="黑体"  size=3>게시 날짜: 2022-03-09</font>

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
이 문서는 K510 demo 보드 sdk 컴패니언 문서이며, 주로 uboot 아래 k510 데모 보드 구성 파일, 장치 트리, 드라이브 위치 등과 같은 uboot 관련 콘텐츠를 소개합니다. 

**<font face="黑体"  size=5>독자 개체입니다</font>**

이 문서(이 가이드)가 주로 적용되는 사람:

- 소프트웨어 개발자
- 기술 지원 담당자

**<font face="黑体"  size=5>레코드를 수정합니다</font>**
 <font face="宋体"  size=2>개정 레코드에는 각 문서 업데이트에 대한 설명이 누적됩니다. 문서의 최신 버전에는 이전 버전의 모든 업데이트가 포함되어 있습니다. </font>

| 버전 번호입니다   | 수정자     | 개정일입니다 | 개정 지침 |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | 시스템 소프트웨어 그룹입니다 | 2022-03-09 |          |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>카탈로그</font>**

[목차]

<div style="page-break-after:always"></div>

# 1 U-Boot 소개

u-boot는 sdk의 일부이며 sdk는 현재 2020.01의 u-boot 버전을 사용하고 있습니다. Uboot는 다양한 임베디드 CPU를 위해 독일 DENX 팀에 의해 개발 된 bootloader 프로그램이며, UBoot는 임베디드 Linux 시스템의 부팅뿐만 아니라 현재 NetBSD, VxWorks, QNX, RTEMS, ARTOS, LynxOS 임베디드 운영 체제를 지원합니다. UBoot는 PowerPC 시리즈 프로세서뿐만 아니라 MIPS, x86, ARM, NIOS, RISICV 등을 지원할 수 있으며, 주요 기능은 메모리 초기화, Linux 부팅, 더 많은 u-boot 소개를 참조하십시오<https://www.denx.de/wiki/U-Boot>

# 2 개발 환경에 대한 간략한 소개

- 운영 체제

| 번호입니다 | 소프트웨어 리소스 | 설명합니다        |
| ---- | -------- | ----------- |
| 1    | 우분투   | 18.04/20.04 |

- 소프트웨어 환경

소프트웨어 환경 요구 사항은 다음 표에 나와 있습니다.

| 번호입니다 | 소프트웨어 리소스 | 설명합니다 |
| ---- | -------- | ---- |
| 1    | K510 SDK |      |

# 3 획득 방법

sdk를 다운로드하고 컴파일하면 sdk가 컴파일될 때 ubiot 코드를 다운로드하고 ubiot 코드를 컴파일합니다. sdk의 다운로드 및 컴파일 방법은[ K510_SDK_Build_and_Burn_Guide.md를 참조하십시오](./K510_SDK_Build_and_Burn_Guide.md)

# 4 중요한 디렉토리 및 문서 설명

이 장에서는 컴파일된 k510_evb_lp3_v1_1_defconfig 예로 들어 보겠습니다. 해당 sdk 컴파일 방법은 make CONF=k510_evb_lp3_v1_1_defconfig, 컴파일 후 디렉토리는 다음과 같습니다.

![이미지-20210930135634105](../zh/images/uboot_guides/build_out.png)

k510_evb_lp3_v1_1_defconfig/build/uboot-custom ---uboot의 코드 및 컴파일 디렉토리;

board/canaan/k510/uboot-sdcard.env---uboot 기본 환경 변수 구성 파일입니다

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/configs/k510_evb_lp3_v1_1_defconfig --uboot 구성 파일;

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/arch/riscv/dts/k510_evb_lp3_v1_1.dts---- 장치 트리 파일;

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/include/configs/k510_evb_lp3_v1_1.h--- 헤더 파일;

k510_evb_lp3_v1_1_defconfig/images/u-boot_burn.bin ---uboot 펌웨어를 구울 수 있습니다

buildroot-2020.02.11/boot/uboot ---- 빌드 루트의 uboot에 대한 컴파일 스크립트는 일반적으로 수정할 필요가 없습니다.

configs/k510_evb_lp3_v1_1_defconfig--- sdk의 구성 파일, BR2_TARGET_UBOOT_BOARD_DEFCONFIG ubiot의 구성 파일을 지정하는 것;

# 5 uboot 시작 프로세스

_start (아치 / riscv / cpu / 시작. S, 줄 43)

board_init_f(일반/board_f.c, 1013행)

board_init_r(일반/board_r.c, 845행)

run_main_loop(일반/board_r.c, 637호선)

# 6 uboot 아래 드라이브 지침

## 6.1 ddr 드라이브

보드/가나안/k510_evb_lp3/ddr_init.c

## 6.2 eth 드라이브

드라이버/넷/맥b.c

장치 트리:

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

## 6.3 직렬 드라이브

드라이버/직렬/ns16550.c

장치 트리:

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

## 6.4 요오점

드라이버/핀틸/핀틸-싱글.c

장치 트리:

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

## 6.5mmc 및 sd 카드 드라이버

drivers/mmc/sdhci-cadence.c

장치 트리입니다

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

# 7 Uboot 기본 환경 변수입니다

uboot의 기본 환경 변수는 SDK의 board/canaan/k510 디렉토리에 텍스트 파일로 미리 정의되어 있습니다.

uboot-emmc.env

uboot-nfs.env

uboot-sdcard.env

SDK의 포스트 스크립트는 컴파일 타임에 mkenvimage를 호출하여 텍스트의 환경 변수 정의를 ubiot가 로드할 수 있는 이진 이미지로 컴파일하여 시작 파티션에 배치합니다.

예를 들면 다음과 같습니다.

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

참고: 커널 시작 매개 변수 bootargs는 uboott의 기본 환경 변수에 의해 설정되며 dts의 bootargs는 재정의됩니다. 자주 묻는 질문(FAQ)-bootargs를 참조하여 커널을 획득하고 전달하는 곳은 어디입니까?

# 8 Uboot 프로그램 업데이트

## 8.1 sdk 미러링 메서드를 굽습니다

sdk 이미지에는 이미 k510_evb_lp3_v1_1_defconfig/images/sysimage-sdcard.img 파일과 같은 sdk 이미지를 직접 태우는 uduot 프로그램이 포함되어 있습니다

## 8.2 linux에서 sd 카드 내부의 ubiot 프로그램을 업데이트하십시오

tftp 디렉토리에 u-boot_burn.bin 파일을 넣고 장치 네트워크 IP 주소를 구성하고 /root/sd/p1 디렉토리를 입력합니다. tftp -gr u-boot_burn.bin xxx.xxx.xxx.xx 명령을 실행합니다.

## 8.3 linux 업데이트emmc 내부의 ubiot 프로그램

tftp 디렉토리에 u-boot_burn.bin 파일을 배치하고, 장치 네트워크 IP 주소를 구성하고, tftp -gr u-boot_burn.bin xxx.xxx.xxx.xx를 통해 장치에 파일을 다운로드합니다.

dd if=u-boot_burn.bin of=/dev/mmcblk0p1 명령을 실행하여 mmc 카드에 파일을 씁니다.

# 9 자주 묻는 질문

## 9.1 DDR 주파수는 어떻게 구성됩니까?

A: 현재 evb는 800개만 실행할 수 있으며 CRB는 800 또는 1600을 설정할 수 있습니다. CRB 보드 ddr 주파수 설정 방법은 uboott의 board\Canaan\k510_crb_lp3\ddr_param.h 파일을 참조하며, 800M은 #define DDR_800 1,1600M에 해당합니다.#define DDR_1600 1.

## 9.2 bootargs 커널은 어디에서 획득하여 커널로 전송됩니다.

A: uboott 환경 변수 bootargs에서 가져온 uboot는 bootargs 환경 변수 값에 따라 메모리 장치 트리의 bootargs 매개 변수를 수정합니다. 관련 코드는 다음과 같습니다.

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

## 9.3 시작 매개 변수와 컴파일된 장치 트리 파일이 일치하지 않나요?

A: uboot는 시작 방법에 따라 환경 변수를 동적으로 가져오고 커널을 부팅할 때 bootargs 환경 변수에 따라 메모리의 장치 트리를 업데이트합니다. 수정된 시작 매개변수는 /sys/firmware/devicetree/base/chosen 노드를 참조하십시오.

## 9.4 uboot 환경 변수는 어디에 저장됩습니까?

A:

| 시작 방법 | uboot 읽기 및 저장 위치입니다 | 컴파일 타임에 해당하는 파일입니다 |
| :-: | :-: | :-: |
| emmc가 시작됩니다 | emmc 두 번째 파티션의 ubiot-emmc.env 파일입니다 | 보드\가나안\k510\uboot-emmc.env |
| sd 카드가 시작됩니다 | sd 카드의 첫 번째 파티션에 대한 ubiott-sd.env 파일 | 보드\가나안\k510\uboot-sd.env |

## 9.5 qos는 어떻게 설정하나요?

A: qos 관련 레지스터는 QOS_CTRL0 QOS_CTRL1 QOS_CTRL2 QOS_CTRL3 QOS_CTRL4. 예:
qos를 설정하면 nncase demo 성능이 향상됩니다

```c
*(uint32_t *)0x970E00FC = (0x2 << 8) | (0x2 << 12) | (0x2 << 16) | (0x2 << 20) | (0x2 << 24);
*(uint32_t *)0x970E0100 = (0x3 << 4) | 0x3;
*(uint32_t *)0x970E00F4 = (0x5 << 16) | (0x5 << 20);
```

**번역 면책 조항**  
고객의 편의를 위해 Canan은 AI 번역 프로그램을 사용하여 오류를 포함할 수 있는 여러 언어로 텍스트를 번역합니다. 당사는 제공된 번역의 정확성, 신뢰성 또는 적시성을 보장하지 않습니다. Canan은 번역된 정보의 정확성이나 신뢰성에 의존하여 발생하는 손실이나 손해에 대해 책임을 지지 않습니다. 언어 번역 간에 콘텐츠 차이가 있는 경우 중국어 간체 버전이 우선합니다. 

번역 오류 또는 부정확한 문제를 신고하려면 이메일로 문의하시기 바랍니다.