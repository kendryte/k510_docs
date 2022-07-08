![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 SDK Build and Burn Guide</font>**

<font face="黑体"  size=3>Document version: V1.0.0</font>

<font face="黑体"  size=3>Published: 2022-03-07</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Disclaimer**</font>
The products, services or features you purchase shall be subject to the commercial contracts and terms of Beijing Canaan Jiesi Information Technology Co., Ltd. ("the Company", the same hereinafter), and all or part of the products, services or features described in this document may not be within the scope of your purchase or use. Except as otherwise agreed in the contract, the Company disclaims all representations or warranties, express or implied, as to the accuracy, reliability, completeness, marketing, specific purpose and non-aggression of any representations, information, or content of this document. Unless otherwise agreed, this document is provided as a guide for use only.
Due to product version upgrades or other reasons, the contents of this document may be updated or modified from time to time without any notice. 

**<font face="黑体"  size=3>Trademark Notices</font>**

""<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, "Canaan" icon, Canaan and other trademarks of Canaan and other trademarks of Canaan are trademarks of Beijing Canaan Jiesi Information Technology Co., Ltd. All other trademarks or registered trademarks that may be mentioned in this document are owned by their respective owners. 

**<font face="黑体"  size=3>Copyright ©2022 Beijing Canaan Jiesi Information Technology Co., Ltd</font>**
This document is only applicable to the development and design of the K510 platform, without the written permission of the company, no unit or individual may disseminate part or all of the content of this document in any form. 

**<font face="黑体"  size=3>Beijing Canaan Jiesi Information Technology Co., Ltd</font>**
URL: canaan-creative.com
Business Enquiries: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# preface
**<font face="黑体"  size=5>Document purpose</font>**
This document is a companion document to the K510 sdk and is intended to help engineers understand the compilation and burning of the K510 sdk. 

**<font face="黑体"  size=5>Reader Objects</font>**

The main people to whom this document (this guide) applies:

- Software developers
- Technical support personnel

**<font face="黑体"  size=5>Revision history</font>**
 <font face="宋体"  size=2>The revision history accumulates a description of each document update. The latest version of the document contains updates for all previous versions. </font>

| The version number   | Modified by     | Date of revision | Revision Notes |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | AI Products Division | 2022-03-07 |          |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |
|        |            |            |              |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contents</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Introduction

This document describes the content of the development environment construction section such as downloading, compiling, and burning the K510 SDK.

# 2 k510 sdk

## 2.1 k510 sdk download

k510 SDK Project Address: <https://github.com/kendryte/k510_buildroot>

Get the k510 SDK:

```shell
git clone https://github.com/kendryte/k510_buildroot.git
```

## 2.2 k510 sdk package introduction

The K510 SDK is an embedded Linux development environment based on the buildroot as the basic framework, based on the K510 linux kernel (linux version 4.17.0), u-boot (u-boot version 2020.01), riscv-pk-k510 (BBL) source code package, the K510 SDK directory structure is shown in the following figure.

![](../zh/images/sdk_build/image-buildroot.png)

 The K510 SDK files are described as follows:

| **file**        | **Description of the content**                                                 |
| --------------- | ------------------------------------------------------------ |
| board           | Folder, which is K510 various configuration files and scripts, such as the configuration file for generating images (genimage-xxx.cfg), buildroot post-image scripts, U-Boot default environment variables, etc. |
| Config.in       | It indicates the package that requires buildroot compilation. |
| configs         | Folder, where is the board default compilation configuration file. Currently saves the default compilation configuration files for the K510 CRB-V0.1, K510 CRB-V1.2, and K510 EVB boards:<br /> -`k510_crb_lp3_v1_2_defconfig`<br />-`k510_crb_lp3_v0_1_defconfig`<br />- `k510_evb_lp3_v1_1_defconfig` |
| external.desc   | Buildroot's external mechanism configuration file. |
| external.mk     | |
| Makefile        | The main Makefile of the k510 SDK. |
| package         | Folders, which are primarily K510 applications, Config.in the contents of the file will determine which applications are compiled under that directory. |
| patches         | Folder, where is the buildroot patch file, Makefile will unzip the source code when the patch file in this directory to the corresponding source code directory. |
| pkg-download    | Folder, which is a compressed package of the dl folder. |
| README.md       | SDK-related instructions. |
| release_note.md | |
| toolchain       | folder, where is the cross-compilation toolchain. |
| dl              | Folder, is the dl extract package in pkg-download, if there are other packages added will also be downloaded to this directory. |

## 2.3 k510 sdk version

When you burn the image generated by the k510 sdk to the board, the version information is printed, as shown in the following figure:

```text
#############SDK VERSION############################################
MX2_DEV_0106-02e87077-20220428-153936CST-xxxxx-server
####################################################################
```

After the startup is complete, enter the following in the shell terminal to view the SDK version information:

```shell
cat /etc/version/release_version
#############SDK VERSION############################################
MX2_REL_0106-02e87077-20220428-153936CST-xxxx-server
####################################################################
```

**Note: The information above may vary depending on the k510 sdk version**. 

# 3 docker compilation environment

After downloading the k510 sdk, execute the following command in the sdk parent directory to start the docker:

```shell
sh k510_buildroot/tools/docker/run_k510_docker.sh
```

Subsequent compilation operations are performed in docker by default.
If you need to set up a local environment, refer to[ Local Environment Setup](#env_set)

# 4 Compile

## 4.1 Compilation Preparation

### 4.1.1 Download the source code package (optional, can speed up compilation)

Execute the following command to download the source package:

```shell
make dl
```

## 4.2 Compilation

K510_buildroot/config directory has compilation configuration files for three development boards, namely`k510_crb_lp3_v0_1_defconfig` , , `k510_crb_lp3_v1_2_defconfig`and `k510_evb_lp3_v1_1_defconfig`, this document is illustrated by selecting k510_crb_lp3_v1_2_defconfig as the compilation target****. 

In the k510 docker environment, enter the following command to start compiling:

```shell
make CONF=k510_crb_lp3_v1_2_defconfig
```

![](../zh/images/sdk_build/image-make.png)

The following message indicates that the compilation completed successfully.

![](../zh/images/sdk_build/image-uboot_r.png)

After the compilation is complete, the folder is generated`k510_crb_lp3_v1_2_defconfig`. 

![image-20220311121912711](../zh/images/sdk_build/image-makeout.png)

Each of these documents is described as follows:

| **file**    | **Description of the content**                                                 |
| ----------- | ------------------------------------------------------------ |
| Makefile    | Compile the image to use Makefile.                                     |
| build       | The compilation directory for all source packages. For example, linux kernel, u-boot, BBL, busybox, etc., the source code will be extracted to the build directory and compiled. |
| host        | All host package installation paths, toolchain will also be copied to this directory for building cross-compilation environments. |
| images      | Compile the resulting target file directory (see instructions below for details)                     |
| nand_target | Root file system raw directory (used to generate NandFlash images)                  |
| target      | Root file system raw directory (to generate eMMC and SD card images to use)                 |

K510_crb_lp3_v1_2_defconfig/images directory is a burned image, in which the description of each file is as follows.

| **file**                   | **Description of the content**                                                 |
| -------------------------- | ------------------------------------------------------------ |
| bootm-bbl.img              | Linux+bbl kernel image (packaged kernel bpl target file for uboot boot bbl) |
| k510.dtb                   | Device tree                                                       |
| sysimage-emmc.img          | emmc burn files: The entire package has been packaged uboot_burn, kernel, and bbl              |
| sysImage-sdcard.img        | sdcard burn files: the entire package has been packaged uboot_burn, kernel, and bbl            |
| sysImage-nand.img          | nand burn files: The entire package has been packaged uboot_burn, kernel, and bbl              |
| u-boot.bin                 | uboot binary file                                             |
| u-boot_burn.bin            | uboot burns files                                               |
| uboot-emmc.env             | uboot environment variable: Used for emmc startup                                  |
| uboot-sd.env               | uboot environment variable: Used for sdcard startup                                |
| uboot-nand.env             | uboot environment variable: Used for nand startup                                  |
| vmlinux                    | Linux kernel image file (with elf debug information)                           |
| rootfs.ext2                | Buildroot format rootfs ext2 image file                             |
| sysimage-sdcard-debian.img | sdcard burn files: card images (rootfs in debian format)                     |

K510_crb_lp3_v1_2_defconfig/build directory is the source code for all compiled objects, several of which are important documents described below.

| **file**         | **Description of the content**                  |
| ---------------- | ----------------------------- |
| linux-xxx        | The compiled Linux kernel source directory |
| uboot-xxx        | The compiled Uboot source directory       |
| riscv-hp-k510-xxx| The bbl source directory where the code is compiled         |
| ...              |                               |

Note: xxx is the version number. When references to the paths of kernle, bbl, and uboot in later sections, xxx all represent version numbers.

**Need special attention:**When making clean, everything under the k510_crb_lp3_v1_2_defconfig folder will be deleted. Therefore, if you need to modify the kernel, bbl or uboot code, do not modify it directly in the build directory, you can refer to Chapter 5 to use the override source method.

## 4.1 Configure buildroot

Enter the configuration buildroot command in the k510 docker environment:

```shell
make CONF=k510_crb_lp3_v1_2_defconfig menuconfig
```

The results of the execution are as follows:

![](../zh/images/sdk_build/image-make_men.png)

![](../zh/images/sdk_build/image-make_menu.png)

After completing the configuration, save and exit, you also need to execute the following buildroot configuration save command:

```shell
make CONF=k510_crb_lp3_v1_2_defconfig savedefconfig
```

The results of the execution are as follows:

![](../zh/images/sdk_build/image-make_savedef.png)

After the above operation is completed, the user can enter the following command to recompile:

```shell
make CONF=k510_crb_lp3_v1_2_defconfig
```

## 4.2 Configure U-Boot

When you need to modify the uboot configuration, you can enter the k510_crb_lp3_v1_2_defconfig directory and enter the following command to start the U-Boot configuration:

```shell
make uboot-menuconfig
```

The results of the execution are as follows:

![](../zh/images/sdk_build/image-uboot_men.png)

![](../zh/images/sdk_build/image-uboot_menu.png)

When you exit the menuuonfig after completing the configuration, select Save Configuration, and you need to execute the following configuration save command:

```shell
make uboot-savedefconfig
```

The results of the execution are as follows:

![](../zh/images/sdk_build/image-uboot_savedefconfig.png)

Finally, in the k510_crb_lp3_v1_2_defconfig directory, enter the following command to start the compilation:

```shell
make uboot-rebuild
```

See the description in the next section for more information.

## 4.3 Compile the U-Boot

The compiled U-Boot source code is stored in the k510_crb_lp3_v1_2_defconfig/build/uboot-xxx directory, and the U-Boot needs to be recompiled whether the user modifies the U-Boot source code or reconfigures the uboot.

Enter the k510_crb_lp3_v1_2_defconfig directory and enter the following command to recompile U-Boot:

```shell
make uboot-rebuild
```

The results of the execution are as follows:

![](../zh/images/sdk_build/image-uboot-rebuild.png)

After the compilation is complete, a new u-boot .bin file is generated in the k510_crb_lp3_v1_2_defconfig/images directory.

If you want to regenerate the burned image file with a new u-boot,`k510_crb_lp3_v1_2_defconfig` execute :in the directory

```shell
make
```

The results of the execution are as follows:

![](../zh/images/sdk_build/image-make_u.png)

When the compilation is complete, you will see the information generated by the following image file.

![](../zh/images/sdk_build/image-uboot_r.png)

## 4.4 Configure the Linux kernel

When you need to modify the kernel configuration, you can enter the k510_crb_lp3_v1_2_defconfig directory and enter the following command to start the kernel configuration:

```shell
make linux-menuconfig
```

The results of the execution are as follows:

![](../zh/images/sdk_build/image-linux_men.png)

![](../zh/images/sdk_build/image-linux_menu.png)

When you exit menuufig after modifying the configuration, select Save Configuration, and finally execute the following configuration save command:

```shell
make linux-savedefconfig
```

The results of the execution are as follows:

![](../zh/images/sdk_build/image-linux_savedefconfig.png)

Finally, in the k510_crb_lp3_v1_2_defconfig directory, enter the following command to start the compilation:

```shell
make linux-rebuild
```

See the description in the next section for more information.

## 4.5 Compile the Linux kernel

K510_crb_lp3_v1_2_defconfig/build/linux-xxx directory holds the compiled Linux source code, whether the user modifies the Linux source code or reconfigures the Linux, it needs to be recompiled.

Enter the k510_crb_lp3_v1_2_defconfig directory and enter the following command to recompile linux:

```shell
make linux-rebuild
```

The results of the execution are as follows:

![](../zh/images/sdk_build/image-linux_rebuild.png)

After compiling, a new vmlinux is generated in the k510_crb_lp3_v1_2_defconfig/images directory.

Linux kernel image needs to be packaged with bbl, after rewriting the Linux kernel, you need to recompile the bbl to generate a new bbl/kernel image for u-boot boot, so enter the following two commands.

```shell
make riscv-pk-k510-dirclean
make riscv-pk-k510
```

The results of the execution are as follows:

![](../zh/images/sdk_build/image-riscv.png)

When the compilation is complete, a `k510_crb_lp3_v1_2_defconfig/images`new one is generated in the directory`bootm-bbl.img`. 

Finally, enter make in the k510_crb_lp3_v1_2_defconfig directory, and use the new bootm-bbl.img package to generate emmc and SD card image files.

```shell
make
```

The results of the execution are as follows:

![](../zh/images/sdk_build/image-make_u.png)

When the compilation is complete, you will see the information generated by the following image file.

![](../zh/images/sdk_build/image-uboot_r.png)

## 4.6 Compile dts

The device tree file is located in the k510_buildroot/k510_crb_lp3_v1_2_defconfig/build/linux-4.17/arch/riscv/boot/dts/canaan directory, and when the user only modifies the device tree, only the device tree can be compiled and decompiled.

Write a mkdtb-local.sh script that reads:

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

Place the mkdtb-local.sh in the K510_buildroot directory and execute the following command to compile the k510_crb_lp3_v1_2_defconfig board device tree:

```shell
./mkdtb-local.sh k510_crb_lp3_v1_2_defconfig
```

The results of the execution are as follows:

![](../zh/images/sdk_build/image-mdk_dts.png)

K510.dtb in the k510_crb_lp3_v1_2_defconfig/images directory is the newly generated device tree database file, and all.dts is the decompiled device tree file.

## 4.7 Compile the app

Users can refer to `package/hello_world` the Config.in and makefile file writing in to build their own applications, and the user applications are placed in the k510_buildroot/package directory. 

The process of compiling an application is illustrated by placing hello_world projects into k510_buildroot/package as an example.

Modify the Config.in files in the k510_buildroot directory in the hosting environment.

![](../zh/images/sdk_build/image-vi_config.png)

In the Config.in, add the path where package/hello_world/Config.in is located and save.

![](../zh/images/sdk_build/image-config_list.png)

Enter the configuration buildroot command in the k510 docker environment:

```shell
make CONF=k510_crb_lp3_v1_2_defconfig menuconfig
```

The results of the execution are as follows:

![](../zh/images/sdk_build/image-build_menu.png)

The buildroot configuration page appears, select The Extended option, and finally select the hello_world and then save and exit.

![](../zh/images/sdk_build/image-extern_option.png)

Enter the Save Configuration command in the k510_buildroot directory.

```shell
make CONF=k510_crb_lp3_v1_2_defconfig savedefconfig
```

The results of the execution are as follows:

![](../zh/images/sdk_build/image-build_savedef.png)

1) If it is the first time to compile, the steps are as follows:

In the k510_buildroot directory, enter the following command to compile the entire project program and package hello into emmc and sd card image files.

```shell
make CONF=k510_crb_lp3_v1_2_defconfig
```

The results of the execution are as follows:

![](../zh/images/sdk_build/image-build_make_def.png)

In the k510_buildroot/k510_crb_lp3_v1_2_defconfig/target directory, you can see the resulting hello application, which tells if the application was compiled correctly.

![](../zh/images/sdk_build/image-hello.png)

2) If it has been compiled, just compile the app and package it into the burn image, follow these steps:

Enter the k510_buildroot/k510_crb_lp3_v1_2_defconfig directory and enter the following command to compile the hello application.

```shell
make hello_world-rebuild
```

The results of the execution are as follows:

![](../zh/images/sdk_build/image-app_build-1.png)

Go to the k510_buildroot/k510_crb_lp3_v1_2_defconfig directory and enter the make command to package hello into the emmc and sd card image files.

```shell
make
```

The results of the execution are as follows:

![](../zh/images/sdk_build/image-app-build-2.png)

# 5 Develop using the K510 SDK

## 5.1 linux kernel/BBL/uboot source code

The uboot version used by this SDK is 2020.01, the uboot patch directory is package/patches/uboot, and the directory after patching is k510_xxx_defconfig/build/uboot-2020.01.

The kernel patch directory used by this sdk is 4.17, the kernel patch directory is package/patches/linux, and the patched directory is k510_xxx_defconfig/build/linux-4.17.

The BBL of this sdk is placed as a target package in the package/riscv-pk-k510/directory, and the source and version number of the bbl are specified in the riscv-pk-k510.mk:

```text
RISCV_PK_K510_VERSION = 1e666d6c5dbab220d2ca57fbd9bec49702599b75
RISCV_PK_K510_SITE = git@github.com:kendryte/k510_BBL.git
RISCV_PK_K510_SITE_METHOD = git
```

## 5.2 Develop linux kernel/BBL/uboot

Each pacification compiled under Buildroot, including linux kernel/BBL/uboot, is implemented by downloading tarball, decompressing, configuring, compiling, installing and other unified package management steps, so although all the source code can be seen in the k510_buildroot/k510_crb_lp3_v1_2_defconfig/build directory, there is no version control information. Even if the code is downloaded from a git repository.

Although the kernel/BBL/uboot source code containing the git repository data can be seen in the dl/directory, buildroot only caches the source code in the dl directory and is not recommended to develop directly in this directory.

For the development model, buildroot provides a way to OVERRIDE_SRCDIR.

In simple terms, you can add a local.mk file under the k510_crb_lp3_v1_2_defconfig directory and add it:

```text
<pkg1>_OVERRIDE_SRCDIR = /path/to/pkg1/sources
```

- LINUX is the package name of kernel
- UBOOT is the PACKAGE name of uboot
- RISCV_PK_K510 is the package name of the bbl

Let's take the Linux kernel as an example to describe how to use it.
Supposing that I have cloned the kernel code in the /data/yourname/workspace/k510_linux_kernel directory and made modifications, and want to compile under buildroot and test it on the crb v1.2 board, you can create a local.mk in the k510_crb_lp3_v1_2_defconfig directory and add the following:

```text
LINUX_OVERRIDE_SRCDIR = /data/yourname/workspace/k510_linux_kernel
```

Execute in the k510_crb_lp3_v1_2_defconfig directory

```shell
make linux-rebuild
```

You can see that the kernel has been recompiled in the build/linux-custom directory, using the modified code under /data/yourname/workspace/k510_linux_kernel.
UBOOT and BBL are similar. In this way, you can directly modify the kernel code and rewrite the kernel under buildroot, and incrementally compile the image to test.
Note: The source code of override will be added to the suffix of custom in the directory name of the k510_crb_lp3_v1_2_defconfig/build directory to distinguish the source of each package in the default configuration of buildroot. For example, in the example of the Linux kernel above, the compilation will see that the code specified by the overrideide is compiled in the k510_crb_lp3_v1_2_defconfig/build/linux-custom directory, rather than the k510_crb_lp3_v1_2_defconfig/build/linux-xxx directory we saw earlier.

For other code in the package directory, or buildroot native packages, it is possible to develop under the buildroot framework in this way.

# 6 Burn the image

K510 supports sdcard and eMMC boot mode, each time compiling in the k510_buildroot/k510_crb_lp3_v1_2_defconfig/image directory will generate sysimage-sdcard.img and sysimg-emmc.img image files, the two files can be burned to sdcard and eMMC respectively.

The K510 determines the chip boot mode by the status of the boot0 and BOOT1 hardware pins, please refer to the boot instructions section of the development board for specific settings.

| BOOT1   | BOOT0   | Startup mode      |
| ------- | ------- | ------------ |
| 0(ON)   | 0(ON)   | Serial port boot      |
| 0(ON)   | 1(OFF)  | The SD card boots      |
| 1(OFF)  | 0(ON)   | NANDFLASH boots |
| 1(OFF)  | 1(OFF)  | EMMC boots      |

![](../zh/images/hw_crb_v1_2/clip_hw_3_9.jpg)

## 6.1 Burn the image to the sd card

### 6.1.1 ubuntu burned

Before inserting the sD card into the host, enter:

```shell
ls -l /dev/sd*
```

View the current storage device.

After inserting the sD card into the host, enter it again:

```shell
ls -l /dev/sd*
```

Looking at the storage device at this time, the new addition is the sd card device node.

After inserting the sD card into the host, the ls command execution result is as follows:

![](../zh/images/sdk_build/image-dev_sd.png)

/dev/sdc is the sd card device node. **Note: The sd card device node generated in the user environment may not be /dev/sdc, and subsequent operations need to be modified according to the actual node. **

Enter the k510_buildroot/k510_crb_lp3_v1_2_defconfig/image directory under the host and enter the dd command to burn sysimage-sdcard.img to the sdk:

```shell
sudo dd if=sysimage-sdcard.img of=/dev/sdc bs=1M oflag=sync
```

The execution result under the host is as follows:

![](../zh/images/sdk_build/image-dd.png)

### 6.1.2 Burn under Windows

Under Windows, the sD card can be burned by the banana Etcher tool (balena Etcher tool download address<https://www.balena.io/etcher/>). 

1) Insert the TF card into the PC, then launch the ColumnEtcher tool, click the "Flash from file" button of the tool interface, select the firmware to be burned, as shown in the following figure.

![](../zh/images/sdk_build/image-sd_pre0.png)

2) Click the "Select target" button of the tool interface and select the target sdcard card.

![](../zh/images/sdk_build/image-pre1.png)

3) Click the "Flash" button to start flashing, the flashing process has a progress bar display, flash Finish will be prompted after the end of the flashing.

| ![](../zh/images/sdk_build/clip_image_p1.jpg) | ![](../zh/images/sdk_build/clip_image_p2.jpg) |
| --------------------------------------- | --------------------------------------- |
|                                         |                                         |

4) When the flashing is complete, insert the SD card into the development board slot, select BOOT to start from SD, and finally the development board can be powered on to start from the SD card.

## 6.2 Burn the image to emmc

To burn the sysimage-emmc.img to the on-board eMMC, with the help of the sdk, in the ubuntu environment, the sysimage-emmc.img is stored in the user partition of the sdk, and then the sdk is inserted into the board and powered on.

Before burning the emmc image, you need to unmount the emmc-related file system, please refer to the following steps to unmount it.

```shell
mount | grep emmc
```

The execution result is as follows:

![](../zh/images/sdk_build/image-emmc_1.png)

Enter the following command to uninstall and check.

```shell
umount /root/emmc/p2
umount /root/emmc/p3
umount /root/emmc/p4
mount | grep emmc
```

The execution result is as follows:

![](../zh/images/sdk_build/image-emmc_2.png)

Finally, enter the path where the image is located, enter the following command to burn eMMC.

```shell
dd if=sysimage-emmc.img of=/dev/mmcblk0 bs=1M
```

The execution result is as follows:

![](../zh/images/sdk_build/image-emmc3.png)

**Note: The burning process is slow, it takes about 30 seconds, please be patient.**

When the flashing is complete, select BOOT to Boot from EMMC, and finally power on the board to boot from EMMC.

# 7 User-configured compilation environment <a id="env_set"> </a>

If you do not use the above docker environment, you can configure your own development environment by referring to the following command at ubuntu18.04/20.04, if you do not have permission, please use`sudo` it. 

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

**Translation Disclaimer**  
For the convenience of customers, Canaan uses an AI translator to translate text into multiple languages, which may contain errors. We do not guarantee the accuracy, reliability or timeliness of the translations provided. Canaan shall not be liable for any loss or damage caused by reliance on the accuracy or reliability of the translated information. If there is a content difference between the translations in different languages, the Chinese Simplified version shall prevail. 

If you would like to report a translation error or inaccuracy, please feel free to contact us by mail.