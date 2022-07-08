![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 SDK 빌드 및 굽기 가이드</font>**

<font face="黑体"  size=3>문서 버전: V1.0.0</font>

<font face="黑体"  size=3>게시 날짜: 2022-03-07</font>

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

| 버전 번호입니다   | 수정자     | 개정일입니다 | 개정 지침 |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | AI 제품 부서 | 2022-03-07 |          |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>카탈로그</font>**

[목차]

<div style="page-break-after:always"></div>

# 1 소개

이 문서에서는 K510 SDK의 다운로드, 컴파일 및 레코딩과 같은 개발 환경 설정 섹션에 대해 설명합니다.

# 2 k510 SDK

## 2.1 k510 sdk 다운로드

k510 SDK 프로젝트 주소: <https://github.com/kendryte/k510_buildroot>

k510 SDK 받기:

```shell
git clone https://github.com/kendryte/k510_buildroot.git
```

## 2.2 k510 sdk 패키지 소개

K510 SDK는 빌드루트를 기본 프레임워크로 하며, K510 linux kernel(linux 버전 4.17.0), u-boot(u-boot 버전 2020.01), riscv-pk-k510(BBL) 소스 패키지를 기반으로 구축된 임베디드 Linux 개발 환경으로, K510 SDK 디렉토리 구조는 아래 그림과 같다.

![](../zh/images/sdk_build/image-buildroot.png)

 K510 SDK 파일은 다음과 같습니다.

| **파일입니다**        | **콘텐츠 설명**입니다                                                 |
| --------------- | ------------------------------------------------------------ |
| 판           | 폴더는 미러 생성 프로파일(genimage-xxx.cfg), 빌드루트의 포스트맵 스크립트, U-부트 기본 환경 변수 등 K510의 다양한 구성 파일 및 스크립트이다. |
| Config.in       | 여기서 내용은 빌드 루트 컴파일이 필요한 패키지입니다. |
| 구성         | 보드의 기본 컴파일 구성 파일인 폴더입니다. 현재 K510 CRB-V0.1, K510 CRB-V1.2 및 K510 EVB 보드의 기본 컴파일 구성 파일이 저장됩니다.<br /> - `k510_crb_lp3_v1_2_defconfig`<br />- `k510_crb_lp3_v0_1_defconfig`<br /> `k510_evb_lp3_v1_1_defconfig` |
| 외부.desc   | 빌드 루트의 external 메커니즘 구성 파일입니다. |
| external.mk     | |
| 메이크파일        | k510 SDK의 기본 Makefile입니다. |
| 패키지         | 주로 K510 응용 프로그램인 폴더는 Config.in 파일의 내용에 따라 해당 디렉터리에서 컴파일되는 응용 프로그램이 결정됩니다. |
| 패치         | 폴더, 여기서 빌드 루트의 패치 파일, Makefile은 소스 코드를 압축을 풀 때 해당 디렉토리의 패치 파일을 해당 소스 디렉토리에 놓습니다. |
| PKG 다운로드    | 폴더, 여기서 dl 폴더의 패키지입니다. |
| README.md       | sdk에 대한 설명입니다. |
| release_note.md | |
| 도구 체인       | 교차 컴파일 도구 체인이 있는 폴더입니다. |
| dl              | 폴더는 pkg-download의 dl 압축 해제 패키지이며 추가 패키지가 추가되면 해당 디렉터리에 다운로드됩니다. |

## 2.3 k510 sdk 버전

k510 sdk 컴파일에서 생성된 이미지를 보드의 시작에 레코딩하면 다음 그림과 같이 버전 정보가 인쇄됩니다.

```text
#############SDK VERSION############################################
MX2_DEV_0106-02e87077-20220428-153936CST-xxxxx-server
####################################################################
```

시작이 완료되면 셸 터미널에 다음을 입력하여 sdk 버전 정보를 볼 수 있습니다.

```shell
cat /etc/version/release_version
#############SDK VERSION############################################
MX2_REL_0106-02e87077-20220428-153936CST-xxxx-server
####################################################################
```

**참고: k510 sdk 버전은 다르며 위의 정보는 다를 수 있습니다**. 

# 3 docker 컴파일 환경

k510 sdk를 다운로드한 후 sdk 상위 디렉터리에서 다음 명령을 실행하여 docker를 시작합니다.

```shell
sh k510_buildroot/tools/docker/run_k510_docker.sh
```

후속 컴파일 작업은 기본적으로 docker에서 수행됩니다.
로컬 환경을 빌드해야 하는 경우[ 로컬 환경 빌드를 참조하십시오](#env_set)

# 4 컴파일

## 4.1 컴파일 준비

### 4.1.1 소스 패키지 다운로드(선택 사항, 컴파일 속도 향상)

다음 명령을 실행하여 소스 패키지를 다운로드합니다.

```shell
make dl
```

## 4.2 컴파일

k510_buildroot/config 디렉토리에는 , 및 의 세 가지 보드에 대한 컴파일 구성 파일이`k510_crb_lp3_v0_1_defconfig` `k510_crb_lp3_v1_2_defconfig``k510_evb_lp3_v1_1_defconfig`있으며 이 **문서에서는 컴파일 대상으로 k510_crb_lp3_v1_2_defconfig 선택합니다**. 

k510 docker 환경에서 다음 명령을 입력하여 컴파일을 시작합니다.

```shell
make CONF=k510_crb_lp3_v1_2_defconfig
```

![](../zh/images/sdk_build/image-make.png)

다음 정보를 출력하면 컴파일이 성공적으로 완료되었습니다.

![](../zh/images/sdk_build/image-uboot_r.png)

컴파일이 완료되면 폴더가 생성됩니다`k510_crb_lp3_v1_2_defconfig`. 

![이미지-20220311121912711](../zh/images/sdk_build/image-makeout.png)

이러한 각 문서는 다음과 같이 설명됩니다.

| **파일입니다**    | **콘텐츠 설명**입니다                                                 |
| ----------- | ------------------------------------------------------------ |
| 메이크파일    | 컴파일 미러에서 사용하는 Makefile입니다.                                     |
| 체격       | 모든 소스 패키지의 컴파일된 디렉터리입니다. 예를 들어 linux kernel, u-boot, BBL, busybox 등과 같은 소스 코드는 빌드 디렉토리로 압축을 풀고 컴파일됩니다. |
| 호스트        | 모든 host package의 설치 경로와 toolchain이 이 디렉토리에 복사되어 교차 컴파일 환경을 구축합니다. |
| 이미지      | 생성된 대상 파일 디렉토리 컴파일(아래 설명 참조)                     |
| nand_target | 루트 파일 시스템 원시 디렉토리(NandFlash 이미지 생성에 사용됨)                  |
| 과녁      | 루트 파일 시스템 원시 디렉토리(eMMC 및 SD 카드 이미지 생성에 사용)                 |

k510_crb_lp3_v1_2_defconfig/images 디렉토리는 레코딩된 이미지이며 각 파일에 대한 설명은 다음과 같습니다.

| **파일입니다**                   | **콘텐츠 설명**입니다                                                 |
| -------------------------- | ------------------------------------------------------------ |
| bootm-bbl.img              | Linux+bbl 커널 이미지(ubiot 부팅 bbl용 커널을 패키징된 bbl 대상 파일) |
| k510.dtb                   | 장치 트리입니다                                                       |
| sysimage-emmc.img          | emmc 레코딩 파일: 전체 패키지 uboot_burn, kernel 및 bbl              |
| sysImage-sdcard.img        | sdcard 굽기 파일: 전체 패키지 uboot_burn, kernel 및 bbl            |
| sysImage-nand.img          | nand 레코딩 파일: 전체 패키지 uboot_burn, kernel 및 bbl              |
| u-부트.bin                 | uboot 바이너리입니다                                             |
| 유boot_burn.bin            | uboot 굽기 파일입니다                                               |
| uboot-emmc.env             | uboot 환경 변수: emmc 시작에 사용됩니다                                  |
| uboot-sd.env               | uboot 환경 변수: sdcard 시작에 사용됩니다                                |
| uboot-nand.env             | uboot 환경 변수: nand 시작에 사용됩니다                                  |
| VM리눅스                    | Linux 커널 이미지 파일(elf 디버그 정보 포함)                           |
| rootfs.ext2                | buildroot 형식 rootfs ext2 미러 파일                             |
| sysimage-sdcard-debian.img | sdcard 굽기 파일:카드 미러링(debian 형식 rootfs)                     |

k510_crb_lp3_v1_2_defconfig/build 디렉터리 아래에는 컴파일된 모든 개체의 소스 코드가 있으며, 그 중 몇 가지 중요한 파일은 아래에 설명되어 있습니다.

| **파일입니다**         | **콘텐츠 설명**입니다                  |
| ---------------- | ----------------------------- |
| 리눅스 - xxx        | 컴파일된 Linux kernel 소스 디렉토리입니다 |
| uboot-xxx        | 컴파일된 Uboot 소스 디렉토리입니다       |
| riscv-hp-k510-xxx| 컴파일된 bbl 소스 디렉토리입니다         |
| ...              |                               |

참고: xxx는 버전 번호입니다. 다음 장에서kernle, bbl 및 ubiot 경로를 참조할 때 xxx는 버전 번호를 나타냅니다.

**주의 사항: **make clean이 k510_crb_lp3_v1_2_defconfig 폴더 아래의 모든 콘텐츠가 삭제됩니다. 따라서 build 디렉토리에서 직접 수정하지 않고 kernel, bbl 또는 ubaott 코드를 수정해야 하는 경우 5장 내용을 참조하여 override source를 사용할 수 있습니다.

## 4.1 빌드 루트를 구성합니다

k510 docker 환경에서 buildroot 구성 명령을 입력합니다.

```shell
make CONF=k510_crb_lp3_v1_2_defconfig menuconfig
```

실행 결과는 다음과 같습니다.

![](../zh/images/sdk_build/image-make_men.png)

![](../zh/images/sdk_build/image-make_menu.png)

구성이 완료되면 저장하고 종료하고 다음과 같은 빌드 루트 구성 저장 명령을 실행해야 합니다.

```shell
make CONF=k510_crb_lp3_v1_2_defconfig savedefconfig
```

실행 결과는 다음과 같습니다.

![](../zh/images/sdk_build/image-make_savedef.png)

이 작업이 완료되면 사용자는 다음 명령을 입력하여 다시 컴파일할 수 있습니다.

```shell
make CONF=k510_crb_lp3_v1_2_defconfig
```

## 4.2 U-Boot를 구성합니다

uboot 구성을 수정해야 하는 경우 k510_crb_lp3_v1_2_defconfig 디렉토리로 이동하여 다음 명령을 입력하여 U-Boot 구성을 시작합니다.

```shell
make uboot-menuconfig
```

실행 결과는 다음과 같습니다.

![](../zh/images/sdk_build/image-uboot_men.png)

![](../zh/images/sdk_build/image-uboot_menu.png)

구성을 완료한 후 menuconfig를 종료할 때 구성 저장을 선택하고 다음 구성 저장 명령을 실행해야 합니다.

```shell
make uboot-savedefconfig
```

실행 결과는 다음과 같습니다.

![](../zh/images/sdk_build/image-uboot_savedefconfig.png)

마지막으로 k510_crb_lp3_v1_2_defconfig 디렉토리에서 다음 명령을 입력하여 컴파일을 시작합니다.

```shell
make uboot-rebuild
```

자세한 내용은 다음 섹션에 설명되어 있습니다.

## 4.3 U-Boot를 컴파일합니다

k510_crb_lp3_v1_2_defconfig/build/uboot-xxx 디렉토리에 컴파일된 U-Boot 소스 코드가 저장되어 사용자가 U-Boot 소스 코드를 수정하든 ubot을 다시 구성하든 U-Boot를 다시 컴파일해야 합니다.

k510_crb_lp3_v1_2_defconfig 디렉토리로 이동하여 다음 명령을 입력하여 U-Boot를 다시 컴파일합니다.

```shell
make uboot-rebuild
```

실행 결과는 다음과 같습니다.

![](../zh/images/sdk_build/image-uboot-rebuild.png)

컴파일이 완료되면 k510_crb_lp3_v1_2_defconfig/images 디렉토리에 새 u-boot .bin 파일이 생성됩니다.

새 u-boot를 사용하여 레코딩 미러 파일을 다시 생성하려면 디렉토리에서`k510_crb_lp3_v1_2_defconfig` 다음을 수행합니다

```shell
make
```

실행 결과는 다음과 같습니다.

![](../zh/images/sdk_build/image-make_u.png)

컴파일이 완료되면 다음과 같은 미러 파일 생성 정보가 표시됩니다.

![](../zh/images/sdk_build/image-uboot_r.png)

## 4.4 Linux kernel을 구성합니다

사용자가 kernel 구성을 수정해야 하는 경우 k510_crb_lp3_v1_2_defconfig 디렉토리로 이동하여 다음 명령을 입력하여 kernel 구성을 시작합니다.

```shell
make linux-menuconfig
```

실행 결과는 다음과 같습니다.

![](../zh/images/sdk_build/image-linux_men.png)

![](../zh/images/sdk_build/image-linux_menu.png)

구성을 수정한 후 menuconfig를 종료할 때 구성 저장을 선택하고 마지막으로 다음 구성 저장 명령을 실행합니다.

```shell
make linux-savedefconfig
```

실행 결과는 다음과 같습니다.

![](../zh/images/sdk_build/image-linux_savedefconfig.png)

마지막으로 k510_crb_lp3_v1_2_defconfig 디렉토리에서 다음 명령을 입력하여 컴파일을 시작합니다.

```shell
make linux-rebuild
```

자세한 내용은 다음 섹션에 설명되어 있습니다.

## 4.5 Linux kernel을 컴파일합니다

k510_crb_lp3_v1_2_defconfig/build/linux-xxx 디렉토리에 컴파일된 Linux 소스 코드가 저장되어 있으며, 사용자가 linux 소스 코드를 수정하든 Linux를 다시 구성하든 Linux를 다시 컴파일해야 합니다.

k510_crb_lp3_v1_2_defconfig 디렉토리로 이동하여 다음 명령을 입력하여 linux를 다시 컴파일합니다.

```shell
make linux-rebuild
```

실행 결과는 다음과 같습니다.

![](../zh/images/sdk_build/image-linux_rebuild.png)

컴파일이 완료되면 k510_crb_lp3_v1_2_defconfig/images 디렉토리에 새 vmlinux가 생성됩니다.

linux kernel 미러는 bbl로 패키징해야 하며 linux kernel을 다시 편집한 후 bbl을 다시 편집하여 u-boot 부트에 대한 새 bbl/kernel 이미지를 생성해야 하므로 다음 두 명령을 입력합니다.

```shell
make riscv-pk-k510-dirclean
make riscv-pk-k510
```

실행 결과는 다음과 같습니다.

![](../zh/images/sdk_build/image-riscv.png)

컴파일이 완료되면 `k510_crb_lp3_v1_2_defconfig/images`디렉터리에서 새 빌드가 생성됩니다`bootm-bbl.img`. 

마지막으로 k510_crb_lp3_v1_2_defconfig 디렉토리에 make를 입력하고 새 bootm-bbl.img 패키지로 emmc 및 sd 카드 이미지 파일을 생성합니다.

```shell
make
```

실행 결과는 다음과 같습니다.

![](../zh/images/sdk_build/image-make_u.png)

컴파일이 완료되면 다음과 같은 미러 파일 생성 정보가 표시됩니다.

![](../zh/images/sdk_build/image-uboot_r.png)

## 4.6 dts를 컴파일합니다

장치 트리 파일은 k510_buildroot/k510_crb_lp3_v1_2_defconfig/build/linux-4.17/arch/riscv/boot/dts/canaan 디렉토리에 있으며 사용자가 장치 트리만 수정할 때 장치 트리만 컴파일하고 디컴파일할 수 있습니다.

다음과 같은 mkdtb-local.sh 스크립트를 작성합니다.

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

K510_buildroot 디렉토리에 mkdtb-local.sh 놓고 다음 명령을 실행하여 k510_crb_lp3_v1_2_defconfig 보드 장치 트리를 컴파일합니다.

```shell
./mkdtb-local.sh k510_crb_lp3_v1_2_defconfig
```

실행 결과는 다음과 같습니다.

![](../zh/images/sdk_build/image-mdk_dts.png)

k510_crb_lp3_v1_2_defconfig/images 디렉토리에서 컴파일이 완료된 k510.dtb는 새로 생성된 장치 트리 데이터베이스 파일이며 all.dts는 디컴파일된 장치 트리 파일입니다.

## 4.7 앱을 컴파일합니다

사용자는 `package/hello_world` 의 Config.in 및 makefile 파일 쓰기를 참조하여 k510_buildroot/package 디렉토리에 배치되는 자체 응용 프로그램을 빌드할 수 있습니다. 

hello_world 프로젝트를 k510_buildroot/package에 배치하여 응용 프로그램을 컴파일하는 프로세스를 보여 줍니다.

호스트 환경에서 k510_buildroot 디렉토리의 Config.in 파일을 수정합니다.

![](../zh/images/sdk_build/image-vi_config.png)

Config.in 패키지/hello_world/Config.in이 있는 경로를 추가하고 저장합니다.

![](../zh/images/sdk_build/image-config_list.png)

k510 docker 환경에서 buildroot 구성 명령을 입력합니다.

```shell
make CONF=k510_crb_lp3_v1_2_defconfig menuconfig
```

실행 결과는 다음과 같습니다.

![](../zh/images/sdk_build/image-build_menu.png)

빌드 루트 구성 페이지가 나타나고 External option을 선택한 다음 hello_world 선택한 후 종료를 저장합니다.

![](../zh/images/sdk_build/image-extern_option.png)

k510_buildroot 디렉토리에 구성 저장 명령을 입력합니다.

```shell
make CONF=k510_crb_lp3_v1_2_defconfig savedefconfig
```

실행 결과는 다음과 같습니다.

![](../zh/images/sdk_build/image-build_savedef.png)

1) 첫 번째 컴파일의 경우 단계는 다음과 같습니다.

k510_buildroot 디렉토리에서 다음 명령을 입력하여 전체 프로젝트 프로그램을 컴파일하고 hello를 emmc 및 sd 카드 이미지 파일로 패키징합니다.

```shell
make CONF=k510_crb_lp3_v1_2_defconfig
```

실행 결과는 다음과 같습니다.

![](../zh/images/sdk_build/image-build_make_def.png)

k510_buildroot/k510_crb_lp3_v1_2_defconfig/target 디렉토리에서 생성된 hello 응용 프로그램을 볼 수 있으며, 이 경우 응용 프로그램이 올바르게 컴파일되었는지 확인할 수 있습니다.

![](../zh/images/sdk_build/image-hello.png)

2) 컴파일 된 경우, 그냥 컴파일하고 레코딩 이미지에 패키지, 단계는 다음과 같습니다 :

k510_buildroot/k510_crb_lp3_v1_2_defconfig 디렉토리로 이동하여 다음 명령을 입력하여 hello 응용 프로그램을 컴파일합니다.

```shell
make hello_world-rebuild
```

실행 결과는 다음과 같습니다.

![](../zh/images/sdk_build/image-app_build-1.png)

k510_buildroot/k510_crb_lp3_v1_2_defconfig 디렉토리로 이동하여 make 명령을 입력하여 hello를 emmc 및 sd 카드 이미지 파일로 패키징합니다.

```shell
make
```

실행 결과는 다음과 같습니다.

![](../zh/images/sdk_build/image-app-build-2.png)

# 5 K510 SDK를 사용하여 개발합니다

## 5.1 linux kernel/BBL/uboot 소스

이 sdk에서 사용하는 uboot 버전은 2020.01이며 uboot 패치 디렉토리는 패키지/patches/uboot이며 패치가 적용된 디렉토리는 k510_xxx_defconfig/build/uboot-2020.01입니다.

이 sdk에서 사용하는 kernel 버전은 4.17이고 kernel 패치 디렉토리는 패키지/patches/linux이고 패치가 완료되면 k510_xxx_defconfig/build/linux-4.17입니다.

이 sdk의 BBL은 package/riscv-pk-k510/디렉토리에 배치된 target package로 riscv-pk-k510.mk bbl의 코드 소스 및 버전 번호를 지정합니다.

```text
RISCV_PK_K510_VERSION = 1e666d6c5dbab220d2ca57fbd9bec49702599b75
RISCV_PK_K510_SITE = git@github.com:kendryte/k510_BBL.git
RISCV_PK_K510_SITE_METHOD = git
```

## 5.2 linux kernel/BBL/uboot를 개발합니다

Buildroot에서 컴파일된 모든 pacakge는 linux kernel/BBL/uboot를 포함하여 tarball, 압축 해제, 구성, 컴파일, 설치 및 기타 통합 패키지 관리 단계를 다운로드하여 수행되므로 k510_buildroot/k510_crb_lp3_v1_2_defconfig/build 디렉토리에서 모든 소스 코드를 볼 수 있지만 버전 제어 정보는 없습니다. 코드가 git 리포지토리에서 다운로드된 경우에도 마찬가지입니다.

git 리포지토리 데이터가 포함된 kernel/BBL/uboot 소스 코드는 dl/디렉토리에서 볼 수 있지만 빌드루트는 dl 디렉터리의 소스 코드만 캐시로 사용하며 이 디렉터리에서 직접 개발하는 것은 권장되지 않습니다.

빌드 루트는 개발 모드에 대한 OVERRIDE_SRCDIR 방법을 제공합니다.

간단히 말해서 k510_crb_lp3_v1_2_defconfig 디렉토리에 local.mk 파일을 추가하여 다음을 추가 할 수 있습니다.

```text
<pkg1>_OVERRIDE_SRCDIR = /path/to/pkg1/sources
```

- LINUX는 kernel의 package name입니다
- UBOOT는 ubot의 PACKAGE name입니다
- RISCV_PK_K510 bbl의 패키지 이름입니다

Linux kernel을 예로 들어 사용 방법을 살펴보겠습니다.
/data/yourname/workspace/k510_linux_kernel 디렉토리에서 clonekernel 코드를 수정했으며 빌드로ot에서 컴파일하고 crb v1.2 보드에서 테스트하려는 경우 k510_crb_lp3_v1_2_defconfig 디렉토리 아래에 local.mk 만들고 다음을 추가할 수 있습니다.

```text
LINUX_OVERRIDE_SRCDIR = /data/yourname/workspace/k510_linux_kernel
```

k510_crb_lp3_v1_2_defconfig 디렉토리에서 실행됩니다

```shell
make linux-rebuild
```

빌드/linux-custom 디렉토리에서 수정된 코드를 사용하여 /data/yourname/workspace/k510_linux_kernel 다시 컴파일된 것을 볼 수 있습니다.
uboot와 bbl도 비슷합니다. 이렇게 하면 커널 코드를 직접 수정하고 빌드 루트에서 커널을 다시 편집하여 이미지를 점진적으로 컴파일하여 테스트할 수 있습니다.
참고: k510_crb_lp3_v1_2_defconfig/build 디렉토리의 override 소스 이름에는 buildroot의 기본 구성에서 각 패키지의 코드 소스를 구분하기 위해 custom 접미사가 추가됩니다. 예를 들어 위의 linux kernel 예제에서 컴파일은 오버라이드가 지정한 코드가 이전에 본 k510_crb_lp3_v1_2_defconfig/build/linux-xxx 디렉터리가 아닌 k510_crb_lp3_v1_2_defconfig/build/linux-custom 디렉토리에서 컴파일되는 것을 볼 수 있습니다.

package 디렉터리의 다른 코드 또는 빌드 루트의 기본 패키지의 경우 이러한 방식으로 빌드 루트의 프레임워크에서 개발 작업을 수행할 수 있습니다.

# 6 이미지를 레코딩합니다

K510은 sdcard 및 eMMC 부팅을 지원하며, k510_buildroot/k510_crb_lp3_v1_2_defconfig/image 디렉토리에서 컴파일할 때마다 sysimage-sdcard.img 및 sysimg-emmc.img 미러 파일이 생성되며, 두 파일은 각각 sdcard 및 eMMC로 레코딩할 수 있습니다.

K510은 BOOT0 및 BOOT1 하드웨어 핀의 상태에 따라 칩이 시작되는 방식을 결정하며, 자세한 내용은 개발 보드의 시작 지침 섹션을 참조하십시오.

| 부트1   | 부트0   | 시작 방법      |
| ------- | ------- | ------------ |
| 0(켜짐)   | 0(켜짐)   | 직렬 포트가 시작됩니다      |
| 0(켜짐)   | 1(꺼짐)  | SD 카드가 시작됩니다      |
| 1(꺼짐)  | 0(켜짐)   | NANDFLASH가 시작됩니다 |
| 1(꺼짐)  | 1(꺼짐)  | EMMC가 시작됩니다      |

![](../zh/images/hw_crb_v1_2/clip_hw_3_9.jpg)

## 6.1 SD 카드에 미러를 구울 수 있습니다

### 6.1.1 우분투 아래 굽기

sd 카드를 호스트에 연결하기 전에 다음을 입력합니다.

```shell
ls -l /dev/sd*
```

현재 저장 장치를 봅니다.

SD 카드를 호스트에 삽입한 후 다음을 다시 입력합니다.

```shell
ls -l /dev/sd*
```

이 시점에서 저장 장치를 보면 sd 카드 장치 노드가 새로 추가됩니다.

SD 카드를 호스트에 삽입하면 ls 명령 실행 결과는 다음과 같습니다.

![](../zh/images/sdk_build/image-dev_sd.png)

/dev/sdc는 sd 카드 장치 노드입니다. **참고: 사용자 환경에서 생성된 SD 카드 장치 노드는 /dev/sdc가 아닐 수 있으며 후속 작업은 실제 노드에 따라 수정해야 합니다. **

호스트에서 k510_buildroot/k510_crb_lp3_v1_2_defconfig/image 디렉토리로 이동하여 dd 명령을 입력하여 sysimage-sdcard.img를 sdcard로 구울 수 있습니다.

```shell
sudo dd if=sysimage-sdcard.img of=/dev/sdc bs=1M oflag=sync
```

호스트 아래의 실행 결과는 다음과 같습니다.

![](../zh/images/sdk_build/image-dd.png)

### 6.1.2 Windows에서 레코딩합니다

Windows에서는 balenaEtcher 도구를 사용하여 sd 카드를 레코딩할 수 있습니다(balenaEtcher 도구 다운로드 주소<https://www.balena.io/etcher/>). 

1) PC에 TF 카드를 삽입 한 다음 balenaEtcher 도구를 시작하고 도구 인터페이스의 "Flash from file"버튼을 클릭하고 아래 그림과 같이 구울 펌웨어를 선택하십시오.

![](../zh/images/sdk_build/image-sd_pre0.png)

2) 도구 인터페이스의 "Select target" 버튼을 클릭하고 대상 sdcard 카드를 선택합니다.

![](../zh/images/sdk_build/image-pre1.png)

3) 플래시 버튼을 클릭하여 쓰기를 시작하고, 굽기 프로세스는 진행률 표시줄을 표시하고, 굽기는 플래시 피니시를 알려줍니다.

| ![](../zh/images/sdk_build/clip_image_p1.jpg) | ![](../zh/images/sdk_build/clip_image_p2.jpg) |
| --------------------------------------- | --------------------------------------- |
|                                         |                                         |

4) 레코딩이 완료되면 SD 카드를 개발 보드 슬롯에 삽입하고 SD에서 부팅하기 위해 BOOT를 선택하고 마지막으로 SD 카드에서 전원을 공급합니다.

## 6.2 emmc에 미러를 레코딩합니다

sysimage-emmc.img을 온보드 eMMC에 레코딩하려면 sdcard를 사용하여 우분투 환경에서 sysimage-emmc.img을 sdcard의 사용자 파티션에 저장한 다음 sdcard를 개발 보드에 연결하고 전원을 켜서 시작해야 합니다.

emmc 이미지를 레코딩하기 전에 emmc 관련 파일 시스템을 마운트 해제해야 합니다.

```shell
mount | grep emmc
```

실행 결과는 다음과 같습니다.

![](../zh/images/sdk_build/image-emmc_1.png)

다음 명령을 입력하여 제거하고 확인합니다.

```shell
umount /root/emmc/p2
umount /root/emmc/p3
umount /root/emmc/p4
mount | grep emmc
```

실행 결과는 다음과 같습니다.

![](../zh/images/sdk_build/image-emmc_2.png)

마지막으로 sysimage-emmc.img 미러가 있는 경로로 이동하여 다음 명령을 입력하여 eMMC를 레코딩합니다.

```shell
dd if=sysimage-emmc.img of=/dev/mmcblk0 bs=1M
```

실행 결과는 다음과 같습니다.

![](../zh/images/sdk_build/image-emmc3.png)

**참고 : 레코딩 프로세스가 느리고 약 30 초가 걸리며 기다려주십시오.**

레코딩이 완료되면 BOOT를 EMMC에서 시작하도록 선택하고 최종 개발 보드에서 전원을 켜서 EMMC에서 시작할 수 있습니다.

# 7 사용자 구성 컴파일 환경 <a id="env_set"> </a>

사용자가 위의 docker 환경을 사용하지 않는 경우 우분투 18.04/20.04에서 다음 명령을 참조하여 자체 개발 환경을 구성할 수 있습니다`sudo`. 

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

**번역 면책 조항**  
고객의 편의를 위해 Canan은 AI 번역 프로그램을 사용하여 오류를 포함할 수 있는 여러 언어로 텍스트를 번역합니다. 당사는 제공된 번역의 정확성, 신뢰성 또는 적시성을 보장하지 않습니다. Canan은 번역된 정보의 정확성이나 신뢰성에 의존하여 발생하는 손실이나 손해에 대해 책임을 지지 않습니다. 언어 번역 간에 콘텐츠 차이가 있는 경우 중국어 간체 버전이 우선합니다. 

번역 오류 또는 부정확한 문제를 신고하려면 이메일로 문의하시기 바랍니다.