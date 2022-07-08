![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 SDK Build and Burn Guide</font>**

<font face="黑体"  size=3>文档版本：V1.0.0</font>

<font face="黑体"  size=3>发布日期：2022-03-07</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**免责声明**</font>
您购买的产品、服务或特性等应受北京嘉楠捷思信息技术有限公司（“本公司”，下同）商业合同和条款的约束，本文档中描述的全部或部分产品、服务或特性可能不在您的购买或使用范围之内。除非合同另有约定，本公司不对本文档的任何陈述、信息、内容的准确性、可靠性、完整性、营销型、特定目的性和非侵略性提供任何明示或默示的声明或保证。除非另有约定，本文档仅作为使用指导的参考。
由于产品版本升级或其他原因，本文档内容将可能在未经任何通知的情况下，不定期进行更新或修改。

**<font face="黑体"  size=3>商标声明</font>**

“<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />”、“Canaan”图标、嘉楠和嘉楠其他商标均为北京嘉楠捷思信息技术有限公司的商标。本文档可能提及的其他所有商标或注册商标，由各自的所有人拥有。

**<font face="黑体"  size=3>版权所有©2022北京嘉楠捷思信息技术有限公司</font>**
本文档仅适用K510平台开发设计，非经本公司书面许可，任何单位和个人不得以任何形式对本文档的部分或全部内容传播。

**<font face="黑体"  size=3>北京嘉楠捷思信息技术有限公司</font>**
网址：canaan-creative.com
商务垂询：salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# 前言
**<font face="黑体"  size=5>文档目的</font>**
本文档为K510 sdk的配套文档，旨在帮助工程师了解 k510 sdk的编译和烧录。

**<font face="黑体"  size=5>读者对象</font>**

本文档（本指南）主要适用的人员：

- 软件开发人员
- 技术支持人员

**<font face="黑体"  size=5>修订记录</font>**
<font face="宋体"  size=2>修订记录累积了每次文档更新的说明。最新版本的文档包含以前所有版本的更新内容。</font>

| 版本号   | 修改者     | 修订日期 | 修订说明 |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | AI 产品部 | 2022-03-07 |          |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>目 录</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 简介

本文档介绍K510 SDK的下载、编译和烧录等开发环境搭建部分的内容。

# 2 k510 sdk

## 2.1 k510 sdk下载

k510 SDK 项目地址: <https://github.com/kendryte/k510_buildroot>

获取k510 SDK：

```shell
git clone https://github.com/kendryte/k510_buildroot.git
```

## 2.2 k510 sdk软件包介绍

K510 SDK是以buildroot为基本框架，以K510 linux kernel（linux版本4.17.0），u-boot（u-boot版本2020.01），riscv-pk-k510（BBL）源码包为基础构建的嵌入式Linux开发环境，K510 SDK目录结构如下图所示。

![](../zh/images/sdk_build/image-buildroot.png)

 K510 SDK各文件描述如下：

| **文件**        | **内容描述**                                                 |
| --------------- | ------------------------------------------------------------ |
| board           | 文件夹，其是K510各种配置文件和脚本，如生成镜像的配置文件（genimage-xxx.cfg），buildroot的post-image脚本，U-Boot默认环境变量等。 |
| Config.in       | 其中内容指示了需要buildroot编译的package。 |
| configs         | 文件夹，其中是开发板默认编译配置文件。当前保存有K510 CRB-V0.1、K510 CRB-V1.2和K510 EVB三块板的默认编译配置文件:<br />- `k510_crb_lp3_v1_2_defconfig`<br />- `k510_crb_lp3_v0_1_defconfig`<br />- `k510_evb_lp3_v1_1_defconfig` |
| external.desc   | buildroot的external机制配置文件。 |
| external.mk     | |
| Makefile        | k510 SDK的主Makefile。 |
| package         | 文件夹，其中主要是K510 应用程序，Config.in文件中的内容将决定该目录下哪些应用程序被编译。 |
| patches         | 文件夹，其中是buildroot的补丁文件，Makefile在解压源码的时候会将此目录下的补丁文件打到相应源码目录。 |
| pkg-download    | 文件夹，其中是dl文件夹的压缩包。 |
| README.md       | sdk 相关说明。 |
| release_note.md | |
| toolchain       | 文件夹，其中是交叉编译工具链。 |
| dl              | 文件夹，是pkg-download中的dl 解压缩包，如果有添加其它包也会下载到该目录下。 |

## 2.3 k510 sdk版本

把k510 sdk编译生成的镜像烧录到板上启动时，会打印版本信息，如下图所示：

```text
#############SDK VERSION############################################
MX2_DEV_0106-02e87077-20220428-153936CST-xxxxx-server
####################################################################
```

启动完成以后，在shell终端输入如下可以查看 sdk版本信息：

```shell
cat /etc/version/release_version
#############SDK VERSION############################################
MX2_REL_0106-02e87077-20220428-153936CST-xxxx-server
####################################################################
```

**注： k510 sdk版本不同，上面的信息可能不同**。

# 3 docker 编译环境

下载完k510 sdk后，在sdk上级目录执行以下命令启动docker:

```shell
sh k510_buildroot/tools/docker/run_k510_docker.sh
```

后续编译操作默认都在docker中执行。
如果需要搭建本地环境请参考[本地环境搭建](#env_set)

# 4 编译

## 4.1编译准备

### 4.1.1下载源码包（可选，可以加速编译）

执行以下命令下载源码包:

```shell
make dl
```

## 4.2编译

k510_buildroot/config 目录下有三个开发板的编译配置文件，分别是`k510_crb_lp3_v0_1_defconfig` 、`k510_crb_lp3_v1_2_defconfig`和`k510_evb_lp3_v1_1_defconfig`， **本文档以选择 k510_crb_lp3_v1_2_defconfig 作为编译目标来说明**。

在k510 docker环境下输入如下命令启动编译：

```shell
make CONF=k510_crb_lp3_v1_2_defconfig
```

![](../zh/images/sdk_build/image-make.png)

输出如下信息表示编译成功完成。

![](../zh/images/sdk_build/image-uboot_r.png)

在编译完成后，会生成`k510_crb_lp3_v1_2_defconfig`文件夹。

![image-20220311121912711](../zh/images/sdk_build/image-makeout.png)

其中各文件描述如下：

| **文件**    | **内容描述**                                                 |
| ----------- | ------------------------------------------------------------ |
| Makefile    | 编译镜像使用的Makefile。                                     |
| build       | 所有源码包的编译目录。例如linux kernel，u-boot，BBL，busybox等，源码都会解压到build目录下并编译。 |
| host        | 所有host package的安装路径，toolchain也会拷贝至此目录下，用于构建交叉编译环境。 |
| images      | 编译生成的目标文件目录（详见下面的说明）                     |
| nand_target | 根文件系统原始目录（生成NandFlash镜像使用）                  |
| target      | 根文件系统原始目录（生成eMMC和SD卡镜像使用）                 |

k510_crb_lp3_v1_2_defconfig/images目录下是烧录镜像，其中各个文件的说明如下。

| **文件**                   | **内容描述**                                                 |
| -------------------------- | ------------------------------------------------------------ |
| bootm-bbl.img              | Linux+bbl内核镜像（打包过内核的bbl目标文件，用于uboot引导bbl） |
| k510.dtb                   | 设备树                                                       |
| sysimage-emmc.img          | emmc烧录文件：已整个打包uboot_burn、kernel和bbl              |
| sysImage-sdcard.img        | sdcard烧录文件：已整个打包uboot_burn、kernel和bbl            |
| sysImage-nand.img          | nand烧录文件：已整个打包uboot_burn、kernel和bbl              |
| u-boot.bin                 | uboot 二进制文件                                             |
| u-boot_burn.bin            | uboot 烧录文件                                               |
| uboot-emmc.env             | uboot环境变量：用于emmc启动                                  |
| uboot-sd.env               | uboot环境变量：用于sdcard启动                                |
| uboot-nand.env             | uboot环境变量：用于nand启动                                  |
| vmlinux                    | Linux内核镜像文件（带elf调试信息）                           |
| rootfs.ext2                | buildroot格式rootfs ext2镜像文件                             |
| sysimage-sdcard-debian.img | sdcard烧录文件：卡镜像(debian格式rootfs)                     |

k510_crb_lp3_v1_2_defconfig/build 目录下是所有被编译对象的源码，其中几个重要的文件说明如下。

| **文件**         | **内容描述**                  |
| ---------------- | ----------------------------- |
| linux-xxx        | 被编译的 Linux kernel源码目录 |
| uboot-xxx        | 被编译的 Uboot 源码目录       |
| riscv-pk-k510-xxx| 被编译的 bbl 源码目录         |
| ...              |                               |

注： xxx是版本号。后面章节引用kernle，bbl和uboot的路径时，xxx均表示版本号。

**需要特别注意：**当make clean 的时候，k510_crb_lp3_v1_2_defconfig文件夹下所有内容将被删除。所以，如果需要修改kernel、bbl或者uboot代码，不要直接在build目录下修改，可以参考第5章内容，使用override source的方式。

## 4.1 配置 buildroot

在k510 docker环境下输入配置 buildroot命令：

```shell
make CONF=k510_crb_lp3_v1_2_defconfig menuconfig
```

执行结果如下：

![](../zh/images/sdk_build/image-make_men.png)

![](../zh/images/sdk_build/image-make_menu.png)

完成配置后保存并退出，还需要执行如下buildroot配置保存命令：

```shell
make CONF=k510_crb_lp3_v1_2_defconfig savedefconfig
```

执行结果如下：

![](../zh/images/sdk_build/image-make_savedef.png)

以上操作完成后，用户可输入如下命令重新编译：

```shell
make CONF=k510_crb_lp3_v1_2_defconfig
```

## 4.2 配置 U-Boot

当用户需要对 uboot配置进行修改，可进入k510_crb_lp3_v1_2_defconfig目录， 输入如下命令启动 U-Boot配置：

```shell
make uboot-menuconfig
```

执行结果如下：

![](../zh/images/sdk_build/image-uboot_men.png)

![](../zh/images/sdk_build/image-uboot_menu.png)

完成配置后退出menuconfig时，选择保存配置，还需要执行如下配置保存命令：

```shell
make uboot-savedefconfig
```

执行结果如下：

![](../zh/images/sdk_build/image-uboot_savedefconfig.png)

最后在k510_crb_lp3_v1_2_defconfig目录，输入如下命令启动编译：

```shell
make uboot-rebuild
```

详细信息见下一节的描述。

## 4.3 编译 U-Boot

k510_crb_lp3_v1_2_defconfig/build/uboot-xxx 目录下保存有被编译的U-Boot源码，无论是用户对 U-Boot源代码进行了修改，还是对uboot 进行了重新配置，都需要重新编译U-Boot。

进入k510_crb_lp3_v1_2_defconfig目录，输入如下命令重新编译 U-Boot：

```shell
make uboot-rebuild
```

执行结果如下：

![](../zh/images/sdk_build/image-uboot-rebuild.png)

编译完成后，会在k510_crb_lp3_v1_2_defconfig/images目录下生成新的 u-boot.bin 文件。

如果要用新u-boot重新生成烧录镜像文件，在`k510_crb_lp3_v1_2_defconfig`目录下执行：

```shell
make
```

执行结果如下：

![](../zh/images/sdk_build/image-make_u.png)

编译完成会看到如下镜像文件生成的信息。

![](../zh/images/sdk_build/image-uboot_r.png)

## 4.4 配置 Linux kernel

当用户需要对 kernel 配置进行修改，可进入k510_crb_lp3_v1_2_defconfig目录， 输入如下命令启动 kernel 配置：

```shell
make linux-menuconfig
```

执行结果如下：

![](../zh/images/sdk_build/image-linux_men.png)

![](../zh/images/sdk_build/image-linux_menu.png)

修改配置后退出menuconfig时，选择保存配置，最后还需要执行如下配置保存命令：

```shell
make linux-savedefconfig
```

执行结果如下：

![](../zh/images/sdk_build/image-linux_savedefconfig.png)

最后在k510_crb_lp3_v1_2_defconfig目录，输入如下命令启动编译：

```shell
make linux-rebuild
```

详细信息见下一节的描述。

## 4.5 编译 Linux kernel

k510_crb_lp3_v1_2_defconfig/build/linux-xxx 目录下保存有被编译的linux源码，无论是用户对 linux 源代码进行了修改，还是对linux 进行了重新配置，都需要重新编译linux 。

进入k510_crb_lp3_v1_2_defconfig目录，输入如下命令重新编译 linux：

```shell
make linux-rebuild
```

执行结果如下：

![](../zh/images/sdk_build/image-linux_rebuild.png)

编译完成后会在k510_crb_lp3_v1_2_defconfig/images目录下生成新的vmlinux。

linux kernel镜像需要用bbl打包，重编linux kernel后，需要重编bbl生成新的bbl/kernel镜像用于u-boot引导，因此输入如下两条命令。

```shell
make riscv-pk-k510-dirclean
make riscv-pk-k510
```

执行结果如下：

![](../zh/images/sdk_build/image-riscv.png)

编译完成，会在`k510_crb_lp3_v1_2_defconfig/images`目录下生成新的`bootm-bbl.img`。

最后在k510_crb_lp3_v1_2_defconfig目录下输入make，用新的bootm-bbl.img打包生成emmc和sd卡镜像文件。

```shell
make
```

执行结果如下：

![](../zh/images/sdk_build/image-make_u.png)

编译完成会看到如下镜像文件生成的信息。

![](../zh/images/sdk_build/image-uboot_r.png)

## 4.6 编译 dts

设备树文件位于 k510_buildroot/k510_crb_lp3_v1_2_defconfig/build/linux-4.17/arch/riscv/boot/dts/canaan 目录下，当用户只修改了设备树，可只对设备树进行编译和反编译。

编写一个 mkdtb-local.sh 脚本，其中的内容为：

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

将 mkdtb-local.sh  放到 K510_buildroot 目录下，执行如下命令即可对 k510_crb_lp3_v1_2_defconfig板设备树进行编译：

```shell
./mkdtb-local.sh k510_crb_lp3_v1_2_defconfig
```

执行结果如下：

![](../zh/images/sdk_build/image-mdk_dts.png)

编译完成在k510_crb_lp3_v1_2_defconfig/images目录下的 k510.dtb是新生成的设备树数据库文件，all.dts是反编译后的设备树文件。

## 4.7 编译 app

用户可参考 `package/hello_world` 中Config.in和makefile文件写法，构建自己的应用程序，用户应用程序放置到 k510_buildroot/package 目录下。

这里以将 hello_world 工程放置到 k510_buildroot/package 为例，来说明编译应用程序的过程。

在宿主机环境下修改k510_buildroot目录下的Config.in文件。

![](../zh/images/sdk_build/image-vi_config.png)

在Config.in 中添加package/hello_world/Config.in所在的路径并保存。

![](../zh/images/sdk_build/image-config_list.png)

在 k510 docker环境下输入配置 buildroot命令：

```shell
make CONF=k510_crb_lp3_v1_2_defconfig menuconfig
```

执行结果如下：

![](../zh/images/sdk_build/image-build_menu.png)

出现buildroot配置页面，选择External option，最后选中其中的hello_world后保存退出。

![](../zh/images/sdk_build/image-extern_option.png)

在k510_buildroot目录下输入保存配置命令。

```shell
make CONF=k510_crb_lp3_v1_2_defconfig savedefconfig
```

执行结果如下：

![](../zh/images/sdk_build/image-build_savedef.png)

1）若是第一次编译，执行步骤如下：

在k510_buildroot目录下，输入如下命令编译整个项目程序，并将hello打包到emmc和sd卡镜像文件当中。

```shell
make CONF=k510_crb_lp3_v1_2_defconfig
```

执行结果如下：

![](../zh/images/sdk_build/image-build_make_def.png)

在k510_buildroot/k510_crb_lp3_v1_2_defconfig/target 目录下，可以看到生成的hello应用程序，由此可判断应用程序是否被正确编译。

![](../zh/images/sdk_build/image-hello.png)

2）若已经编译过，只是对app进行编译并打包到烧录镜像中，执行步骤如下：

进入到 k510_buildroot/k510_crb_lp3_v1_2_defconfig目录下，输入如下命令编译 hello应用程序。

```shell
make hello_world-rebuild
```

执行结果如下：

![](../zh/images/sdk_build/image-app_build-1.png)

进入到 k510_buildroot/k510_crb_lp3_v1_2_defconfig目录下，输入make命令将hello打包到emmc和sd卡镜像文件当中。

```shell
make
```

执行结果如下：

![](../zh/images/sdk_build/image-app-build-2.png)

# 5 使用K510 SDK进行开发

## 5.1 linux kernel/BBL/uboot源码

本sdk使用的uboot版本是2020.01，uboot补丁目录是package/patches/uboot，打完补丁后的目录是k510_xxx_defconfig/build/uboot-2020.01。

本sdk使用的kernel版本是4.17，kernel补丁目录是package/patches/linux，打完补丁后的目录是k510_xxx_defconfig/build/linux-4.17。

本sdk的 BBL作为一个target package，放在package/riscv-pk-k510/目录下，riscv-pk-k510.mk中指定了bbl的代码源和版本号：

```text
RISCV_PK_K510_VERSION = 1e666d6c5dbab220d2ca57fbd9bec49702599b75
RISCV_PK_K510_SITE = git@github.com:kendryte/k510_BBL.git
RISCV_PK_K510_SITE_METHOD = git
```

## 5.2 开发linux kernel/BBL/uboot

Buildroot下编译的每一个pacakge，包括linux kernel/BBL/uboot，都是通过下载tarball，解压，配置，编译，安装等统一的包管理步骤来实现的，因此在k510_buildroot/k510_crb_lp3_v1_2_defconfig/build目录下虽然可以看到全部的源码，但是都没有版本控制信息，即使代码是从git 仓库下载的。

虽然在dl/目录下可以看到包含了git仓库数据的kernel/BBL/uboot源码，但是buildroot仅仅把dl目录下的源码作为缓存，不建议直接在这个目录的进行开发。

针对开发模式，buildroot提供了OVERRIDE_SRCDIR的方式。

简单来说就是可以在k510_crb_lp3_v1_2_defconfig目录下添加一个local.mk文件，在里面添加：

```text
<pkg1>_OVERRIDE_SRCDIR = /path/to/pkg1/sources
```

- LINUX 是kernel的package name
- UBOOT 是uboot的PACKAGE name
- RISCV_PK_K510 是bbl的package name

我们以linux kernel为例，介绍如何使用。
假设我已经在/data/yourname/workspace/k510_linux_kernel目录下clone了kernel的代码，并做了修改，想要在buildroot下编译并在crb v1.2板子上测试，可以在k510_crb_lp3_v1_2_defconfig目录下创建一个local.mk并添加如下内容:

```text
LINUX_OVERRIDE_SRCDIR = /data/yourname/workspace/k510_linux_kernel
```

在k510_crb_lp3_v1_2_defconfig目录下执行

```shell
make linux-rebuild
```

就可以看到build/linux-custom目录下重新编译了kernel，用的就是/data/yourname/workspace/k510_linux_kernel下修改过的代码。
uboot和bbl也类似。这样就可以直接修改内核代码并在buildroot下重编内核，增量编译镜像去测试。
注： override的源码在k510_crb_lp3_v1_2_defconfig/build目录下的目录名称会加上custom的后缀，来区分buildroot的默认配置中的每个package的代码源的不同。例如上述linux kernel的例子，编译会看到override指定的代码是在k510_crb_lp3_v1_2_defconfig/build/linux-custom目录下编译，而不是之前我们看到的k510_crb_lp3_v1_2_defconfig/build/linux-xxx目录。

对于package目录下的其他代码，或者buildroot原生的package，都可以通过这种方式在buildroot的框架下进行开发工作。

# 6 烧录镜像

K510 支持sdcard和eMMC启动方式，每次编译时在k510_buildroot/k510_crb_lp3_v1_2_defconfig/image目录下将同时生成sysimage-sdcard.img和sysimg-emmc.img镜像文件，两份文件可分别烧录到sdcard和eMMC。

K510 通过 BOOT0 和 BOOT1 两个硬件管脚的状态决定芯片启动方式，具体设置请参考开发板的启动说明章节。

| BOOT1   | BOOT0   | 启动方式      |
| ------- | ------- | ------------ |
| 0(ON)   | 0(ON)   | 串口启动      |
| 0(ON)   | 1(OFF)  | SD卡启动      |
| 1(OFF)  | 0(ON)   | NANDFLASH启动 |
| 1(OFF)  | 1(OFF)  | EMMC启动      |

![](../zh/images/hw_crb_v1_2/clip_hw_3_9.jpg)

## 6.1 烧录镜像到sd卡

### 6.1.1 ubuntu下烧录

在sd卡插到宿主机之前，输入：

```shell
ls -l /dev/sd*
```

查看当前的存储设备。

将sd卡插入宿主机后，再次输入：

```shell
ls -l /dev/sd*
```

查看此时的存储设备，新增加的就是 sd 卡设备节点。

将sd卡插入宿主机后，ls 命令执行结果如下：

![](../zh/images/sdk_build/image-dev_sd.png)

/dev/sdc 就是 sd卡设备节点。**注意: 用户环境下生成的 sd卡设备节点可能不是 /dev/sdc，后续操作需要根据实际节点做相应修改。**

在宿主机下进入k510_buildroot/k510_crb_lp3_v1_2_defconfig/image目录，输入dd命令将sysimage-sdcard.img烧录到sdcard：

```shell
sudo dd if=sysimage-sdcard.img of=/dev/sdc bs=1M oflag=sync
```

宿主机下的执行结果如下：

![](../zh/images/sdk_build/image-dd.png)

### 6.1.2 Windows下烧录

Windows下可通过balenaEtcher工具对sd卡进行烧录（balenaEtcher工具下载地址<https://www.balena.io/etcher/>）。

1）将TF卡插入PC，然后启动balenaEtcher工具，点击工具界面的"Flash from file”按钮，选择待烧写的固件，如下图。

![](../zh/images/sdk_build/image-sd_pre0.png)

2）点击工具界面的“Select target”按钮，选择目标sdcard卡。

![](../zh/images/sdk_build/image-pre1.png)

3）点击“Flash”按钮开始烧写，烧写过程有进度条展示，烧写结束后会提示Flash Finish。

| ![](../zh/images/sdk_build/clip_image_p1.jpg) | ![](../zh/images/sdk_build/clip_image_p2.jpg) |
| --------------------------------------- | --------------------------------------- |
|                                         |                                         |

4）当烧录完成后，将SD卡插入开发板卡槽，选择 BOOT为从SD启动，最后开发板上电即可从SD卡启动。

## 6.2 烧录镜像到emmc

将sysimage-emmc.img烧录到板载eMMC需要借助于sdcard，在ubuntu环境下，将sysimage-emmc.img 存放到sdcard的用户分区，然后将sdcard插入开发板并上电启动。

烧录emmc镜像前，需要卸载掉emmc相关文件系统，请参考如下步骤进行卸载。

```shell
mount | grep emmc
```

执行结果如下图：

![](../zh/images/sdk_build/image-emmc_1.png)

输入如下命令卸载和检查。

```shell
umount /root/emmc/p2
umount /root/emmc/p3
umount /root/emmc/p4
mount | grep emmc
```

执行结果如下图：

![](../zh/images/sdk_build/image-emmc_2.png)

最后进入sysimage-emmc.img镜像所在路径，输入如下命令烧录eMMC。

```shell
dd if=sysimage-emmc.img of=/dev/mmcblk0 bs=1M
```

执行结果如下图：

![](../zh/images/sdk_build/image-emmc3.png)

**注：烧录过程较慢，大约需要30秒，请耐心等待。**

当烧录完成后，选择 BOOT为从EMMC启动，最后开发板上电即可从EMMC启动。

# 7 用户配置编译环境 <a id="env_set"> </a>

若用户不使用上述的docker环境，可在ubuntu18.04/20.04参考如下命令配置自己的开发环境，如果没有权限请使用`sudo`。

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

**翻译免责声明**  
为方便客户，Canaan 使用 AI 翻译程序将文本翻译为多国语言，它可能包含错误。我们不保证提供的译文的准确性、可靠性或时效性。对于因依赖已翻译信息的准确性或可靠性而造成的任何损失或损害，Canaan 概不负责。如果不同语言翻译之间存在内容差异，以简体中文版本为准。

如果您要报告翻译错误或不准确的问题，欢迎通过邮件与我们联系。