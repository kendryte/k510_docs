![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 리눅스 커널 드라이버 개발자 가이드</font>**

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
이 문서는 K510 sdk에 대한 컴패니언 문서이며 Linux 관련 드라이버, 구성, 디버깅 등에 중점을 줍니다

**<font face="黑体"  size=5>독자 개체입니다</font>**

이 문서(이 가이드)가 주로 적용되는 사람:

- 소프트웨어 개발자
- 기술 지원 담당자

**<font face="黑体"  size=5>레코드를 수정합니다</font>**
 <font face="宋体"  size=2>개정 레코드에는 각 문서 업데이트에 대한 설명이 누적됩니다. 문서의 최신 버전에는 이전 버전의 모든 업데이트가 포함되어 있습니다. </font>

| 버전 번호입니다   | 수정자     | 개정일입니다 | 개정 지침 |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | 시스템 소프트웨어 그룹입니다 | 2022-03-09 | SDK V1.5 릴리스 |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>카탈로그</font>**

[목차]

<div style="page-break-after:always"></div>

# 1 Linux Kernel 소개

현재 sdk에서 사용하는 Linux 버전은 4.17.0입니다. Linux, 전체 이름 GNU/Linux, 무료 사용 및 무료 확산 클래스 UNIX 운영 체제, 리누스 베나딕트 토바즈에 의해 처음 출시 된 커널 1991년 10월 5일, 주로 미니 엑스와 유닉스 아이디어에서 영감을, POSIX 기반 다중 사용자, 멀티 태스킹, 멀티 스레드 및 멀티 CPU 운영 체제. 주요 유닉스 도구 소프트웨어, 응용 프로그램 및 네트워크 프로토콜을 실행합니다. 32비트 및 64비트 하드웨어를 지원합니다. Linux는 유닉스의 네트워크 중심 설계 아이디어를 계승하며 안정적인 다중 사용자 네트워크 운영 체제입니다. Linux에는 커뮤니티 기반 Debian, archlinux, 상용 개발 기반 Red Hat Enterprise Linux, SUSE, Oracle Linux 등 수백 가지 배포판이 있습니다.

Linux kernel에 대해 자세히 알아보려면 다음 사이트를 방문하십시오.<https://docs.kernel.org/>

## 1.1 획득 방법

sdk를 다운로드하고 컴파일하면 sdk가 컴파일될 때 linux 코드가 다운로드되고 컴파일됩니다.

sdk의 다운로드 및 컴파일 방법은[K510_SDK_Build_and_Burn_Guide](./K510_SDK_Build_and_Burn_Guide.md)참조하십시오.

## 1.2 개발 환경 요구 사항

- 운영 체제

| 번호입니다 | 소프트웨어 리소스 | 설명합니다        |
| ---- | -------- | ----------- |
| 1    | 우분투   | 18.04/20.04 |

- 소프트웨어 환경 요구 사항은 다음 표에 나와 있습니다.

| 번호입니다 | 소프트웨어 리소스 | 설명합니다 |
| ---- | -------- | ---- |
| 1    | K510 SDK | v1.5 버전 |

# 2 커널 기본 프로필 및 dts

기본 커널 프로필 경로:

arch/riscv/configs/k510_defconfig

kernel은 두 개의 보드 K510 CRB 및 EVB를 지원하며 해당 dts 파일은 다음과 같습니다.

아치/riscv/boot/dts/canaan/k510_crb_lp3_v0_1.dts

아치/riscv/boot/dts/canaan/k510_evb_lp3_v1_1.dts

soc 수준 공용 dts 정의는 arch/riscv/boot/dts/canaan/k510_common 디렉토리에 저장됩니다.

# 3 디버깅

## 3.1 JTAG를 사용하여 Linux 커널을 디버깅합니다

1. Andight v3.2.1을 설치합니다
2. andesight 설치 디렉토리에서 ice 디렉토리로 이동하여 ICEMAN을 실행합니다

    ```shell
    #ICEman -Z v5 --smp
    ```

3. /dev/mem 커널 코드 driver/char/mem.c를 예로 들어 gdb 디버깅을 사용합니다

    ```shell
    riscv64-linux-gdb --eval-command="target remote 192.168.200.100:1111"
    (gdb) symbol-file vmlinux
    (gdb) hbreak mmap_mem
    ```

4. 응용 프로그램이 열려 있습니다/dev/mem, mmap을 호출 한 후 중단점에 입력

# 4 드라이버 설명

## 4.1 UART

구성 옵션:

```shell
CONFIG_SERIAL_8250_DW
```

드라이브 파일:

```shell
/tty/serial/8250
```

장치 트리:

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

API:장치 파일 노드:

```shell
/dev/ttyS0
/dev/ttyS1/2/3    #目前dts中disable
```

프로그래밍 인터페이스: 표준 직렬 드라이버, Linux man page 참조

```shell
man termios
```

## 4.2 ETH

구성 옵션:

```shell
CONFIG_NET_CADENCE
```

드라이브 파일:

```shell
drivers/net/ethernet/cadence
```

장치 트리:

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

장치:`eth0`
Api 설명: 표준 네트워크 포트 드라이버, tcp/ip socket 프로그래밍을 참조하십시오.

네트워크 포트 IP 구성:

```shell
ifconfig eth0 xxx.xxx.xxx.xxx
```

## 4.3 EMMC

구성 옵션:

```shell
CONFIG_MMC_SDHCI_CADENCE
```

드라이브 파일:

```shell
drivers/mmc/host/sdhci-cadence.c
```

장치 트리:

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

장치 및 파티션:

```shell
[root@k510-test ~ ]$ ls -l /dev/ | grep mmcblk0
brw------- 179,  0 Jan 1 1970 mmcblk0      # emmc
brw------- 179,  8 Jan 1 1970 mmcblk0boot0
brw------- 179, 16 Jan 1 1970 mmcblk0boot1
brw------- 179,  1 Jan 1 1970 mmcblk0p1    # emmc第一个分区(boot)
brw------- 179,  2 Jan 1 1970 mmcblk0p2    # emmc第二个分区(kenrel,env,vfat)
brw------- 179,  3 Jan 1 1970 mmcblk0p3    # emmmc第三个分区(rootfs文件系统，ext2)
```

드라이버 API: 표준 드라이버, 일반 파일로 읽고 쓸 수 있습니다.

## 4.4 SD 카드

구성 옵션:

```shell
CONFIG_MMC_SDHCI_CADENCE
```

드라이브 파일:

```shell
drivers/mmc/host/sdhci-cadence.c
```

장치 트리:

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

장치:

```shell
[root@k510-test ~ ]$ ls -l /dev/ | grep mmcblk1
brw------- 179, 24 mmcblk1      # sd卡设备
brw------- 179, 25 mmcblk1p1    # sd卡第一个分区(boot,kenrel,env,vfat)
brw------- 179, 26 mmcblk1p2    # sd卡第二个分区(rootfs文件系统，ext2)
brw------- 179, 27 mmcblk1p3    # sd卡第三个分区(用户分区)
```

드라이버 API: 표준 드라이버, 일반 파일로 읽고 쓸 수 있습니다.

## 4.5 WDT

구성 옵션:

```shell
CONFIG_DW_WATCHDOG
```

드라이브 파일:

```shell
drivers/watchdog/dw_wdt.c
```

장치 트리:

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

API:장치 파일 노드:

```shell
/dev/watchdog
/dev/watchdog0/1/2
```

프로그래밍 인터페이스: Linux 파일 IO(open, close , ioctl), Linux man page 참조
커널 소스에는 다음과 같은 문서가 함께 제공됩니다.`Documentation/watchdog/watchdog-api.txt`

## 4.6 PWM

구성 옵션:

```shell
CONFIG_PWM_GPIO
CONFIG_PWM_CANAAN
```

드라이브 파일:

```shell
drivers/pwm/pwm-canaan.c
drivers/pwm/pwm-gpio.c
```

장치 트리:

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

API: pwm은 sysfs를 통해 액세스할 수 있는 사용자 상태에서 구동됩니다. `/sys/class/pwm/`

프로그래밍 인터페이스: Linux 파일 IO(open, read, write), Linux man page 참조

커널 소스에는 다음과 같은 문서가 함께 제공됩니다.`Documentation/pwm.txt`

## 4.7 I2C

구성 옵션:

```shell
CONFIG_I2C_DESIGNWARE_CORE
CONFIG_I2C0_TEST_DRIVER
```

드라이브 파일:

```shell
drivers/misc/canaan/i2c/test-i2c0.c
drivers/i2c/busses/i2c-designware-platdrv.c
```

장치 트리:

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

API: I2C 드라이버는 Linux kernel I2C 하위 시스템 프레임워크를 사용하여 구현되는 버스 드라이버입니다. 사용자 상태는 sysfs를 통해 액세스할 수 있으며 i2c-tools와 같은 사용자 상태 도구 프로그램을 사용할 수도 있습니다.

```shell
/sys/bus/i2c/devices/
```

프로그래밍 인터페이스: Linux 파일 IO(open, read, write), Linux man page 참조
커널 소스에는 다음과 같은 문서가 함께 제공됩니다.`Documentation/i2c/dev-interface`

## 4.8 USB OTG

구성 옵션:

```shell
USB_CANAAN_OTG20
```

드라이브:

```shell
drivers/usb/canaan_otg20/core_drv_mod
```

장치 트리:

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

USB는 호스트로서 USB 스틱을 마운트할 수 있으며 device로 USB 드라이브로 사용할 수 있습니다.

## 4.9 증권 시세 표시기

구성 옵션:

```shell
CONFIG_COMMON_CLK_CAN_K510
```

드라이브 파일:

```shell
drivers/reset/canaan/reset-k510.c
```

장치 트리:

```shell
arch/riscv/boot/dts/canaan/k510_common/clock_provider.dtsi
arch/riscv/boot/dts/canaan/k510_common/clock_consumer.dtsi
```

- `clock_provider.dtsi`에서 모든 클럭 노드를 정의합니다
- `clock_consumer.dtsi`에서 각 드라이버 dts 노드에서 참조됩니다

## 4.10 전원

구성 옵션:

```shell
CONFIG_CANAAN_PM_DOMAIN
```

드라이브 파일:

```shell
drivers/soc/canaan/k510_pm_domains.c
```

장치 트리:

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

- `power_provider.dtsi` provider의 dts 노드가 정의됩니다
- `include/dt-bindings/soc/canaan,k510_pm_domains.h` 모든 전원 도메인이 정의되어 있습니다
- `power_consumer.dtsi`는 각 dts 노드를 구동하는 데 참조됩니다

## 4.11 리셋

구성 옵션:

```shell
CONFIG_COMMON_RESET_K510
```

드라이브 파일:

```shell
drivers/reset/canaan/reset-k510.c
```

장치 트리:

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

- `reset_provider.dtsi` provider의 dts 노드가 정의됩니다
- `include/ dt-bindings/reset/canaan-k510-reset.h` 모든 reset 신호가 정의됩니다
- `reset_consumer.dtsi`는 각 dts 노드를 구동하는 데 참조됩니다

## 4.12 핀트틀

구성 옵션:

```shell
CONFIG_PINCTRL_K510
```

드라이브 파일:

```shell
drivers/pinctrl/canaan
```

관련 장치 트리:

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

`iomux_provider.dtsi` provider의 dts 노드가 정의됩니다
`include/include/dt-bindings/pinctrl/k510.h`모든 IO function number가 정의되어 있습니다
`iomux_consumer.dtsi`는 각 dts 노드를 구동하는 데 참조됩니다

## 4.13 H264

구성 옵션:

```shell
CONFIG_ ALLEGRO_CODEC_DRIVER
```

드라이브 파일:

```shell
drivers/media/platform/canaan/al5r
```

관련 장치 트리:

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

API: 장치 파일 노드: `/dev/h264-codec`

프로그래밍 인터페이스: Linux man page에 설명된 linux 파일 IO(open, close , ioctl)

지원되는 IOCTL 명령:

```c
#define AL_CMD_IP_WRITE_REG    _IOWR('q', 10, struct al5_reg)
#define AL_CMD_IP_READ_REG     _IOWR('q', 11, struct al5_reg)
#define AL_CMD_IP_WAIT_IRQ     _IOWR('q', 12, int)
#define AL_CMD_IP_IRQ_CNT      _IOWR('q', 13, int)
#define AL_CMD_IP_CLR_IRQ      _IOWR('q', 14, int)
```

샘플 코드:`package/h264_demo/src`

## 4.14 DSP

구성 옵션:

```shell
CONFIG_ K510_DSP_DRIVER
```

드라이브 파일:

```shell
drivers/misc/canaan/k510-dsp
```

관련 장치 트리:

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

API: 장치 파일 노드: `/dev/k510-dsp`

프로그래밍 인터페이스: Linux man page에 설명된 linux 파일 IO(open, close , ioctl)

지원되는 ioctl 명령:

```c
#define DSP_CMD_BOOT       _IOWR('q', 1, unsigned long)
```

샘플 코드:

```shell
package/dsp_app/src/
package/dsp_app_evb_lp3_v1_1/src/
```

## 4.15 GNNE

구성 옵션:

```shell
CONFIG_ K510_GNNE_DRIVER
```

드라이브 파일:

```shell
drivers/misc/canaan/gnne
```

관련 장치 트리:

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

API: 장치 파일 노드: /dev/k510-gnne
프로그래밍 인터페이스: Linux man page에 설명된 linux 파일 IO(open, close , ioctl)
지원되는 ioctl 명령:

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

샘플 코드:

```shell
package/nncase_demo/src/mobilenetv2
```

## 4.16 투드

구성 옵션:

```shell
CONFIG_K510_2D_DRIVER
```

드라이브 파일:

```shell
drivers/media/platform/canaan/kendryte_2d.c
```

관련 장치 트리:

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

API: 장치 파일 노드:/dev/kendryte_2d
프로그래밍 인터페이스: Linux man page에 설명된 linux 파일 IO(open, close , ioctl)
지원되는 ioctl 명령:

```c
#define KENDRTY_2DROTATION_90     _IOWR('k', 0, unsigned long)
#define KENDRTY_2DROTATION_270    _IOWR('k', 1, unsigned long)

#define KENDRTY_2DROTATION_INPUT_ADDR     _IOWR('k', 2, unsigned long)
#define KENDRTY_2DROTATION_OUTPUT_ADDR    _IOWR('k', 3, unsigned long)
#define KENDRTY_2DROTATION_GET_REG_VAL    _IOWR('k', 4, unsigned long)
```

## 4.17 AES 및 SHA

구성 옵션:

```shell
CONFIG_CRYPTO_DEV_KENDRYTE_CRYP
```

드라이브 파일:

```shell
drivers/crypto/kendryte/kendryte-aes.c
drivers/crypto/kendryte/kendryte-aes.h
drivers/crypto/kendryte/kendryte-hash.c
drivers/crypto/kendryte/kendryte-hash.h
```

관련 장치 트리:

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

API: 장치 노드 파일:`/sys/bus/platform/devices/91000000.aes`
`/sys/bus/platform/devices/91010000.sha`

프로그래밍 인터페이스: 사용자 상태 프로그램은 소켓을 사용하여 참조 문서가 있는 커널의 드라이버 API에 액세스합니다`/Documentation/crypto/userspace-if.rst`

샘플 코드:

```shell
package/crypto_demo/src
```

## 4.18 온도 모니터링 - thermal

구성 옵션:

```shell
CONFIG_THERMAL
CONFIG_CANAAN_THERMAL
```

드라이브 파일:

```shell
drivers/thermal/canaan_thermal.c
```

관련 장치 트리:

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

사용 방법:

```shell
cd /sys/class/thermal/thermal_zone0/
echo enabled > mode
cat temp
```

## 4.19 2D 회전 - twod

구성 옵션:

```shell
CONFIG_KENDRYTE_TWOD_SUPPORT
CONFIG_KENDRYTE_TWOD
```

드라이브 파일:

```shell
drivers/video/canaan/twod/kendryte_td.c
drivers/video/canaan/twod/kendryte_td_reg.c
drivers/video/canaan/twod/kendryte_td.h
drivers/video/canaan/twod/kendryte_td_table.h
```

관련 장치 트리:

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

# 5 주의 사항

아니요, 없습니다

**번역 면책 조항**  
고객의 편의를 위해 Canan은 AI 번역 프로그램을 사용하여 오류를 포함할 수 있는 여러 언어로 텍스트를 번역합니다. 당사는 제공된 번역의 정확성, 신뢰성 또는 적시성을 보장하지 않습니다. Canan은 번역된 정보의 정확성이나 신뢰성에 의존하여 발생하는 손실이나 손해에 대해 책임을 지지 않습니다. 언어 번역 간에 콘텐츠 차이가 있는 경우 중국어 간체 버전이 우선합니다.

번역 오류 또는 부정확한 문제를 신고하려면 이메일로 문의하시기 바랍니다.
