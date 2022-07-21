![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 U-boot Developer's Guide</font>**

<font face="黑体"  size=3>Document version: V1.0.0</font>

<font face="黑体"  size=3>Published: 2022-03-09</font>

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
This document is a K510 demo board sdk supporting document, mainly introducing uboot related content, such as k510 demo board configuration file, device tree, driver location and other information under uboot.

**<font face="黑体"  size=5>Reader Objects</font>**

The main people to whom this document (this guide) applies:

- Software developers
- Technical support personnel

**<font face="黑体"  size=5>Revision history</font>**
 <font face="宋体"  size=2>The revision history accumulates a description of each document update. The latest version of the document contains updates for all previous versions. </font>

| The version number   | Modified by     | Date of revision | Revision Notes |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.0 | System software groups | 2022-03-09 |          |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Contents</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1 Introduction to U-Boot

U-boot is part of sdk, and the u-boot version currently used by the SDK is 2020.01. Uboot is a bootloader program developed by the German DENX group for a variety of embedded CPUs, UBoot not only supports the boot of embedded Linux systems, currently, it also supports NetBSD, VxWorks, QNX, RTEMS, ARTOS, LynxOS embedded operating system. In addition to supporting the PowerPC series of processors, UBoot can also support MIPS, x86, ARM, NIOS, RISICV, etc., the main functions are initializing memory, booting Linux systems, more u-boot introduction, please refer to<https://www.denx.de/wiki/U-Boot>

# 2 Introduction to the development environment

- operating system

| numbering | Software resources | illustrate        |
| ---- | -------- | ----------- |
| 1    | Ubuntu   | 18.04/20.04 |

- Software environment

The software environment requirements are shown in the following table:

| numbering | Software resources | illustrate |
| ---- | -------- | ---- |
| 1    | K510 SDK |      |

# 3 How to get it

Download and compile the sdk, the sdk will download the uboot code when compiling, and compile the uboot code. For more information about how to download and compile the SDK, see[K510_SDK_Build_and_Burn_Guide.md](./K510_SDK_Build_and_Burn_Guide.md)

# 4 Important directories and file descriptions

This chapter uses compiled k510_evb_lp3_v1_1_defconfig as an example. The corresponding sdk compilation method is make CONF=k510_evb_lp3_v1_1_defconfig, and the directory after compilation is as follows:

![image-20210930135634105](../zh/images/uboot_guides/build_out.png)

k510_evb_lp3_v1_1_defconfig/build/uboot-custom --- uboot's code and compilation directory;

board/canaan/k510/uboot-sdcard.env--- uboot default environment variable configuration file

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/configs/k510_evb_lp3_v1_1_defconfig --uboot configuration file;

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/arch/riscv/dts/k510_evb_lp3_v1_1.dts---- device tree file;

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/include/configs/k510_evb_lp3_v1_1.h--- header file;

k510_evb_lp3_v1_1_defconfig/images/u-boot_burn.bin ---uboot flashes the firmware

buildroot-2020.02.11/boot/uboot ----buildroot in the compilation script about uboot, generally does not need to be modified;

Configs/k510_evb_lp3_v1_1_defconfig---sdk configuration file, BR2_TARGET_UBOOT_BOARD_DEFCONFIG specify the configuration file of uboot;

# 5 uboot starts the process

_start(arch/riscv/cpu/start. S, line 43)

board_init_f(common/board_f.c, line 1013)

board_init_r(common/board_r.c, line 845)

run_main_loop(common/board_r.c, line 637)

# 6 uboot under driver description

## 6.1 ddr driver

board/Canaan/k510_evb_lp3/ddr_init.c

## 6.2 eth drive

drivers/net/macb.c

Device Tree:

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

## 6.3 Serial port drive

drivers/serial/ns16550.c

Device Tree:

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

drivers/pinctrl/pinctrl-single.c

Device Tree:

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

## 6.5 mmc and sd card drive

drivers/mmc/sdhci-cadence.c

Device tree

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

# 7 Uboot default environment variable

The default environment variable for uboot is in the SDK's board/canaan/k510 directory, predefined as a text file:

uboot-emmc.env

uboot-nfs.env

uboot-sdcard.env

The POST script of the SDK will call mkenvimage at compile time to compile the text environment variable definition into a binary image that uboot can load and place in the boot partition.

Here are some examples:

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

Note: The kernel boot parameter bootargs are set by the default environment variable of uboot, and the bootargs in dts will be overwritten. See FAQ - Where did bootargs get and pass to the kernel?

# 8 Uboot program updates

## 8.1 Flashing sdk mirror method

The sdk image already contains a uboot program, directly flashing the sdk image, such as: k510_evb_lp3_v1_1_defconfig/images/sysimage-sdcard.img file

## 8.2 Linux update the uboot program inside the sD card

Put the u-boot_burn.bin file in the tftp directory, configure the ip address of the device Network port, and enter the /root/sd/p1 directory; Execute the tftp -gr u-boot_burn.bin xxx.xxx.xxx.xxx.xx command;

## 8.3 Linux updates the uboot program inside emmc

Put the u-boot_burn.bin file in the tftp directory, configure the device's network port IP address, and download the file to the device via tftp -gr u-boot_burn.bin xxx.xxx.xxx.xxx.xx;

Execute the dd if=u-boot_burn.bin of=/dev/mmcblk0p1 command to write the file to the mmc card.

# 9 Frequently Asked Questions

## 9.1 How is the DDR frequency configured?

A: At present, the EVB can only run 800, and the CRB can set 800 or 1600. CrB board ddr frequency setting method see uboot board\Canaan\k510_crb_lp3\ddr_param.h file, 800M corresponds to #define DDR_800 1, 1600M corresponds to #define DDR_1600 1.

## 9.2 Where did bootargs get and pass to the kernel?

A: Obtained from the uboot environment variable bootargs, uboot will modify the bootargs parameters in the memory device tree according to the bootargs environment variable value when booting the kernel. The relevant code is as follows:

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

## 9.3 Are the startup parameters inconsistent with the compiled device tree file?

A: uboot dynamically obtains the environment variables according to the boot mode, and updates the device tree in memory according to the bootargs environment variables when booting the kernel. After the modified boot parameters, see the /sys/firmware/devicetree/base/chosen node.

## 9.4 Where are uboot environment variables saved?

Answer:

| Startup mode | uboot read and save location | Compile-time corresponding files |
| :-: | :-: | :-: |
| EMMC boots | Emmc the uboot-emmc.env file for the second partition | board\canaan\k510\uboot-emmc.env |
| Sd card boot | The uboot-sd.env file of the first partition of the sd card | board\canaan\k510\uboot-sd.env |

## 9.5 How to set up qos?

A: QOS-related registers are QOS_CTRL0 QOS_CTRL1 QOS_CTRL2 QOS_CTRL3 QOS_CTRL4. Example:
After setting qos, nncase demo performance has improved

```c
*(uint32_t *)0x970E00FC = (0x2 << 8) | (0x2 << 12) | (0x2 << 16) | (0x2 << 20) | (0x2 << 24);
*(uint32_t *)0x970E0100 = (0x3 << 4) | 0x3;
*(uint32_t *)0x970E00F4 = (0x5 << 16) | (0x5 << 20);
```

**Translation Disclaimer**  
For the convenience of customers, Canaan uses an AI translator to translate text into multiple languages, which may contain errors. We do not guarantee the accuracy, reliability or timeliness of the translations provided. Canaan shall not be liable for any loss or damage caused by reliance on the accuracy or reliability of the translated information. If there is a content difference between the translations in different languages, the Chinese Simplified version shall prevail.

If you would like to report a translation error or inaccuracy, please feel free to contact us by mail.
