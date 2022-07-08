![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 U-boot Руководство разработчика</font>**

<font face="黑体"  size=3>Версия документа: V1.0.0</font>

<font face="黑体"  size=3>Опубликовано: 2022-03-09</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Отказ**</font>
Продукты, услуги или функции, которые вы покупаете, регулируются коммерческими контрактами и условиями Beijing Canaan Jiesi Information Technology Co., Ltd. («Компания», то же самое далее), и все или часть продуктов, услуг или функций, описанных в этом документе, могут не входить в сферу вашей покупки или использования. Если иное не оговорено в договоре, Компания отказывается от всех заявлений или гарантий, явных или подразумеваемых, в отношении точности, надежности, полноты, маркетинга, конкретной цели и ненападения любых заявлений, информации или содержания этого документа. Если не согласовано иное, настоящий документ предоставляется только в качестве руководства для использования.
В связи с обновлением версии продукта или по другим причинам содержимое этого документа может время от времени обновляться или изменяться без какого-либо уведомления. 

**<font face="黑体"  size=3>Уведомления о товарных знаках</font>**

""<img src="../zh/images/canaan-logo.png" style="zoom:33%;" />, значок "Canaan", Canaan и другие товарные знаки Canaan и другие товарные знаки Canaan являются товарными знаками Beijing Canaan Jiesi Information Technology Co., Ltd. Все другие товарные знаки или зарегистрированные товарные знаки, которые могут быть упомянуты в этом документе, принадлежат их соответствующим владельцам. 

**<font face="黑体"  size=3>Copyright ©2022 Пекин Ханаан Цзеси Информационные технологии Co., Ltd</font>**
Настоящий документ применим только к разработке и проектированию платформы K510, без письменного разрешения компании, ни одно подразделение или частное лицо не может распространять часть или все содержание этого документа в любой форме. 

**<font face="黑体"  size=3>Пекин Ханаан Цзеси Информационные Технологии Co., Ltd</font>**
URL: canaan-creative.com
Бизнес-запросы: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# предисловие
**<font face="黑体"  size=5>Назначение </font>**документа
Этот документ является документом, поддерживающим SDK демо-платы K510, в основном представляющим контент, связанный с uboot, такой как файл конфигурации демонстрационной платы k510, дерево устройств, местоположение драйвера и другую информацию под uboot. 

**<font face="黑体"  size=5>Объекты чтения</font>**

Основные люди, к которым относится этот документ (это руководство):

- Разработчики программного обеспечения
- Персонал технической поддержки

**<font face="黑体"  size=5>История изменений</font>**
 <font face="宋体"  size=2>Журнал изменений накапливает описание каждого обновления документа. Последняя версия документа содержит обновления для всех предыдущих версий. </font>

| Номер версии   | Изменено     | Дата пересмотра | Примечания к пересмотру |
|  :-----  |-------   |  ------  |  ------  |
| Версия 1.0.0 | Группы системного программного обеспечения | 2022-03-09 |          |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Содержание</font>**

[ОГЛАВЛЕНИЯ]

<div style="page-break-after:always"></div>

# 1 Введение в U-Boot

U-boot является частью SDK, а версия u-boot, используемая в настоящее время SDK, — 2020.01. Uboot - это программа загрузчика, разработанная немецкой группой DENX для различных встроенных процессоров, UBoot не только поддерживает загрузку встроенных систем Linux, в настоящее время она также поддерживает NetBSD, VxWorks, QNX, RTEMS, ARTOS, встроенную операционную систему LynxOS. В дополнение к поддержке серии процессоров PowerPC, UBoot также может поддерживать MIPS, x86, ARM, NIOS, RISICV и т. Д., Основными функциями являются инициализация памяти, загрузка систем Linux, более u-boot введение, пожалуйста, обратитесь к<https://www.denx.de/wiki/U-Boot>

# 2 Введение в среду разработки

- Операционная система

| нумерация | Программные ресурсы | иллюстрировать        |
| ---- | -------- | ----------- |
| 1    | Убунту   | 18.04/20.04 |

- Программная среда

Требования к программной среде приведены в следующей таблице:

| нумерация | Программные ресурсы | иллюстрировать |
| ---- | -------- | ---- |
| 1    | K510 SDK |      |

# 3 Как его получить

Загрузите и скомпилируйте sdk, sdk загрузит код uboot при компиляции и скомпилирует код uboot. Дополнительные сведения о загрузке и компиляции пакета SDK см. в[ K510_SDK_Build_and_Burn_Guide.md](./K510_SDK_Build_and_Burn_Guide.md)

# 4 Важные каталоги и описания файлов

В этой главе в качестве примера используются скомпилированные k510_evb_lp3_v1_1_defconfig. Соответствующий метод компиляции SDK — make CONF=k510_evb_lp3_v1_1_defconfig, а каталог после компиляции выглядит следующим образом:

![изображение-20210930135634105](../zh/images/uboot_guides/build_out.png)

k510_evb_lp3_v1_1_defconfig/build/uboot-custom --- каталог кода и компиляции uboot;

board/canaan/k510/uboot-sdcard.env--- uboot файл конфигурации переменных среды по умолчанию

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/configs/k510_evb_lp3_v1_1_defconfig --uboot конфигурационный файл;

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/arch/riscv/dts/k510_evb_lp3_v1_1.dts---- файл дерева устройств;

k510_evb_lp3_v1_1_defconfig/build/uboot-custom/include/configs/k510_evb_lp3_v1_1.h--- заголовочный файл;

k510_evb_lp3_v1_1_defconfig/images/u-boot_burn.bin ---uboot мигает прошивкой

buildroot-2020.02.11/boot/uboot ----buildroot в скрипте компиляции про uboot, как правило, не нуждается в изменении;

Конфигурационный файл Configs/k510_evb_lp3_v1_1_defconfig---sdk, BR2_TARGET_UBOOT_BOARD_DEFCONFIG указать конфигурационный файл uboot;

# 5 uboot запускает процесс

_start(arch/riscv/cpu/start. S, строка 43)

board_init_f(общий/board_f.c. строка 1013)

board_init_r(common/board_r.c, строка 845)

run_main_loop(общий/board_r.c, строка 637)

# 6 uboot под описанием драйвера

## 6.1 драйвер DDR

доска/Ханаан/k510_evb_lp3/ddr_init.c

## 6.2 eth привод

драйверы/net/macb.c

Дерево устройств:

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

## 6.3 Диск с последовательным портом

драйверы/последовательный/ns16550.c

Дерево устройств:

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

## 6.4 иомукс

драйверы/pinctrl/pinctrl-single.c

Дерево устройств:

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

## Дисковод 6,5 mmc и SD-карты

драйверы/mmc/sdhci-cadence.c

Дерево устройств

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

# 7 Переменная среды Uboot по умолчанию

Переменная среды по умолчанию для uboot находится в каталоге SDK board/canaan/k510, предопределенном как текстовый файл:

uboot-emmc.env

uboot-nfs.env

uboot-sdcard.env

Сценарий POST SDK вызовет mkenvimage во время компиляции для компиляции определения переменной текстовой среды в двоичный образ, который uboot может загрузить и поместить в загрузочный раздел.

Вот несколько примеров:

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

Примечание: Загрузочный параметр ядра bootargs устанавливается переменной среды по умолчанию uboot, и bootargs в dts будут перезаписаны. Смотрите FAQ - Где бутарги попали и перешли в ядро?

# 8 обновлений программы Uboot

## 8.1 Метод мигающего зеркала SDK

Образ SDK уже содержит программу uboot, непосредственно мигающую образ SDK, например: файл k510_evb_lp3_v1_1_defconfig/images/sysimage-sdcard.img

## 8.2 Linux обновляет программу uboot внутри sD-карты

Поместите файл u-boot_burn.bin в каталог tftp, настройте ip-адрес сетевого порта устройства и войдите в каталог /root/sd/p1; Выполните команду tftp -gr u-boot_burn.bin xxx.xxx.xxx.xxx.xx;

## 8.3 Linux обновляет программу uboot внутри emmc

Поместите файл u-boot_burn.bin в каталог tftp, настройте IP-адрес сетевого порта устройства и загрузите файл на устройство через tftp -gr u-boot_burn.bin xxx.xxx.xxx.xxx.xx;

Выполните команду dd if=u-boot_burn.bin of=/dev/mmcblk0p1, чтобы записать файл на карту mmc.

# 9 Часто задаваемые вопросы

## 9.1 Как настраивается частота DDR?

О: В настоящее время EVB может работать только с 800, а CRB может устанавливать 800 или 1600. CrB плата ddr метод настройки частоты см. uboot board\Canaan\k510_crb_lp3\ddr_param.h файл, 800M соответствует #define DDR_800 1, 1600M соответствует #define DDR_1600 1.

## 9.2 Откуда взялись и перешли в ядро?

О: Полученный из переменной среды uboot bootargs, uboot изменит параметры bootargs в дереве устройств памяти в соответствии со значением переменной среды bootargs при загрузке ядра. Соответствующий код выглядит следующим образом:

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

## 9.3 Не согласуются ли параметры запуска с скомпилированным файлом дерева устройств?

A: uboot динамически получает переменные среды в соответствии с режимом загрузки и обновляет дерево устройств в памяти в соответствии с переменными среды bootargs при загрузке ядра. После изменения параметров загрузки см. узел /sys/firmware/devicetree/base/selected.

## 9.4 Где сохраняются переменные среды uboot?

Ответ:

| Режим запуска | uboot чтение и сохранение местоположения | Соответствующие файлы во время компиляции |
| :-: | :-: | :-: |
| Ботинки EMMC | Emmc файл uboot-emmc.env для второго раздела | board\canaan\k510\uboot-emmc.env |
| Загрузка с SD-карты | Файл uboot-sd.env первого раздела SD-карты | board\canaan\k510\uboot-sd.env |

## 9.5 Как настроить qos?

О: Регистры, связанные с QOS, QOS_CTRL0 QOS_CTRL1 QOS_CTRL2 QOS_CTRL3 QOS_CTRL4. Пример:
После установки qos производительность демонстрации nncase улучшилась

```c
*(uint32_t *)0x970E00FC = (0x2 << 8) | (0x2 << 12) | (0x2 << 16) | (0x2 << 20) | (0x2 << 24);
*(uint32_t *)0x970E0100 = (0x3 << 4) | 0x3;
*(uint32_t *)0x970E00F4 = (0x5 << 16) | (0x5 << 20);
```

**Отказ от ответственности за **перевод  
Для удобства клиентов Canaan использует переводчик AI для перевода текста на несколько языков, которые могут содержать ошибки. Мы не гарантируем точность, надежность или своевременность предоставленных переводов. Компания Canaan не несет ответственности за любые убытки или ущерб, вызванные доверием к точности или надежности переведенной информации. При наличии разницы в содержании переводов на разные языки преимущественную силу имеет упрощенная версия на китайском языке. 

Если вы хотите сообщить об ошибке или неточности перевода, пожалуйста, не стесняйтесь обращаться к нам по почте.