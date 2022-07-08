![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 Руководство разработчика драйверов ядра Linux</font>**

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
Этот документ является вспомогательным документом для K510 SDK, в этом документе в основном говорится о драйверах, связанных с Linux, конфигурации, отладке и т. Д.

**<font face="黑体"  size=5>Объекты чтения</font>**

Основные люди, к которым относится этот документ (это руководство):

- Разработчики программного обеспечения
- Персонал технической поддержки

**<font face="黑体"  size=5>История изменений</font>**
 <font face="宋体"  size=2>Журнал изменений накапливает описание каждого обновления документа. Последняя версия документа содержит обновления для всех предыдущих версий. </font>

| Номер версии   | Изменено     | Дата пересмотра | Примечания к пересмотру |
|  :-----  |-------   |  ------  |  ------  |
| Версия 1.0.0 | Группы системного программного обеспечения | 2022-03-09 | Выпущен пакет SDK версии 1.5 |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |
|        |        |            |                    |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Содержание</font>**

[ОГЛАВЛЕНИЯ]

<div style="page-break-after:always"></div>

# 1 Введение в ядро Linux

Версия Linux, используемая в настоящее время SDK, - 4.17.0. Linux, полное название GNU/Linux, является свободно используемой и свободно распространяемой UNIX-подобной операционной системой с ядром, впервые выпущенным Линусом Беннадиктом Торвазом 5 октября 1991 года, она в основном вдохновлена идеями Minix и Unix, и является многопользовательской, многозадачной, многопоточной и многопроцессорной операционной системой на основе POSIX. Он запускает основное программное обеспечение Unix, приложения и сетевые протоколы. Он поддерживает как 32-разрядное, так и 64-разрядное оборудование. Linux наследует философию проектирования Unix, ориентированную на сеть, и является стабильной многопользовательской сетевой операционной системой. Linux имеет сотни различных дистрибутивов, таких как debian, archlinux и коммерчески разработанные Red Hat Enterprise Linux, SUSE, Oracle Linux и т. Д.

Для получения дополнительной информации о ядре Linux, пожалуйста, посетите:<https://docs.kernel.org/>

## 1.1 Как его получить

Загрузите и скомпилируйте SDK, SDK загрузит и скомпилирует код Linux при компиляции.

Дополнительные сведения о загрузке и компиляции пакета SDK см. в разделе[ K510_SDK_Build_and_Burn_Guide](./K510_SDK_Build_and_Burn_Guide.md). 

## 1.2 Требования к среде разработки

- Операционная система

| нумерация | Программные ресурсы | иллюстрировать        |
| ---- | -------- | ----------- |
| 1    | Убунту   | 18.04/20.04 |

- Требования к программной среде приведены в следующей таблице:

| нумерация | Программные ресурсы | иллюстрировать |
| ---- | -------- | ---- |
| 1    | K510 SDK | Версия 1.5 |

# 2 Файл конфигурации ядра по умолчанию и dts

Путь к файлу конфигурации ядра по умолчанию:

arch/riscv/configs/k510_defconfig

Ядро поддерживает две платы разработки, K510 CRB и EVB, и соответствующие файлы dts следующие:

arch/riscv/boot/dts/canaan/k510_crb_lp3_v0_1.dts

arch/riscv/boot/dts/canaan/k510_evb_lp3_v1_1.dts

В каталоге arch/riscv/boot/dts/canaan/k510_common находится публичное определение dts на уровне soc.

# 3 Отладка

## 3.1 Отладка ядра Linux с помощью JTAG

1. Установка Andesight v3.2.1
2. Перейдите в каталог ice в каталоге установки andesight и запустите ICEMAN

    ```shell
    #ICEman -Z v5 --smp
    ```

3. Используя отладку gdb, вот драйвер кода ядра /dev/mem/char/mem.c в качестве примера

    ```shell
    riscv64-linux-gdb --eval-command="target remote 192.168.200.100:1111"
    (gdb) symbol-file vmlinux
    (gdb) hbreak mmap_mem
    ```

4. Приложение открывает /dev/mem, вызывает mmap и вводит точку останова

# 4 Описание драйвера

## 4.1 УАРТ

Параметры конфигурации:

```shell
CONFIG_SERIAL_8250_DW
```

Файлы драйвера:

```shell
/tty/serial/8250
```

Дерево устройств:

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

API: Узел файла устройства:

```shell
/dev/ttyS0
/dev/ttyS1/2/3    #目前dts中disable
```

Программный интерфейс: стандартный драйвер последовательного порта, обратитесь к справочной странице Linux

```shell
man termios
```

## 4.2 ETH

Параметры конфигурации:

```shell
CONFIG_NET_CADENCE
```

Файлы драйвера:

```shell
drivers/net/ethernet/cadence
```

Дерево устройств:

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

Устройство:`eth0`
Описание API: Стандартный драйвер порта Ethernet, пожалуйста, обратитесь к программированию сокета tcp/ip; 

Конфигурация IP порта Ethernet:

```shell
ifconfig eth0 xxx.xxx.xxx.xxx
```

## 4.3 ЭММК

Параметры конфигурации:

```shell
CONFIG_MMC_SDHCI_CADENCE
```

Файлы драйвера:

```shell
drivers/mmc/host/sdhci-cadence.c
```

Дерево устройств:

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

Устройства и разделы:

```shell
[root@k510-test ~ ]$ ls -l /dev/ | grep mmcblk0
brw------- 179,  0 Jan 1 1970 mmcblk0      # emmc
brw------- 179,  8 Jan 1 1970 mmcblk0boot0
brw------- 179, 16 Jan 1 1970 mmcblk0boot1
brw------- 179,  1 Jan 1 1970 mmcblk0p1    # emmc第一个分区(boot)
brw------- 179,  2 Jan 1 1970 mmcblk0p2    # emmc第二个分区(kenrel,env,vfat)
brw------- 179,  3 Jan 1 1970 mmcblk0p3    # emmmc第三个分区(rootfs文件系统，ext2)
```

Driver API: Стандартный драйвер, как обычный файл для чтения и записи.

## 4.4 SD-КАРТА

Параметры конфигурации:

```shell
CONFIG_MMC_SDHCI_CADENCE
```

Файлы драйвера:

```shell
drivers/mmc/host/sdhci-cadence.c
```

Дерево устройств:

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

Оборудование:

```shell
[root@k510-test ~ ]$ ls -l /dev/ | grep mmcblk1
brw------- 179, 24 mmcblk1      # sd卡设备
brw------- 179, 25 mmcblk1p1    # sd卡第一个分区(boot,kenrel,env,vfat)
brw------- 179, 26 mmcblk1p2    # sd卡第二个分区(rootfs文件系统，ext2)
brw------- 179, 27 mmcblk1p3    # sd卡第三个分区(用户分区)
```

Driver API: Стандартный драйвер, как обычный файл для чтения и записи.

## 4.5 WDT

Параметры конфигурации:

```shell
CONFIG_DW_WATCHDOG
```

Файлы драйвера:

```shell
drivers/watchdog/dw_wdt.c
```

Дерево устройств:

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

API: Узел файла устройства:

```shell
/dev/watchdog
/dev/watchdog0/1/2
```

Интерфейс программирования: linux файл IO(открыть, закрыть, ioctl), см. справочную страницу Linux
Исходный код ядра поставляется с документацией:`Documentation/watchdog/watchdog-api.txt`

## 4.6 ШИМ

Параметры конфигурации:

```shell
CONFIG_PWM_GPIO
CONFIG_PWM_CANAAN
```

Файлы драйвера:

```shell
drivers/pwm/pwm-canaan.c
drivers/pwm/pwm-gpio.c
```

Дерево устройств:

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

API: доступ к драйверу pwm в пользовательском состоянии можно получить через sysfs, `/sys/class/pwm/`

Интерфейс программирования: Linux file IO (открытие, чтение, запись), см. справочную страницу Linux

Исходный код ядра поставляется с документацией:`Documentation/pwm.txt`

## 4.7 I2C

Параметры конфигурации:

```shell
CONFIG_I2C_DESIGNWARE_CORE
CONFIG_I2C0_TEST_DRIVER
```

Файлы драйвера:

```shell
drivers/misc/canaan/i2c/test-i2c0.c
drivers/i2c/busses/i2c-designware-platdrv.c
```

Дерево устройств:

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

API: Драйвер I2C является драйвером шины и реализован с использованием инфраструктуры подсистемы I2C ядра Linux. Доступ к пользовательскому состоянию можно получить через sysfs или использовать программы пользовательского состояния, такие как i2c-tools.

```shell
/sys/bus/i2c/devices/
```

Интерфейс программирования: Linux файл IO (открытие, чтение, запись), см. справочную страницу Linux
Исходный код ядра поставляется с документацией:`Documentation/i2c/dev-interface`

## 4.8 USB OTG

Параметры конфигурации:

```shell
USB_CANAAN_OTG20
```

Гнать:

```shell
drivers/usb/canaan_otg20/core_drv_mod
```

Дерево устройств:

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

USB в качестве хоста, может быть подключен к U-диску, как устройство, может использоваться как U-диск.

## 4.9 КЛК

Параметры конфигурации:

```shell
CONFIG_COMMON_CLK_CAN_K510
```

Файлы драйвера:

```shell
drivers/reset/canaan/reset-k510.c
```

Дерево устройств:

```shell
arch/riscv/boot/dts/canaan/k510_common/clock_provider.dtsi
arch/riscv/boot/dts/canaan/k510_common/clock_consumer.dtsi
```

- `clock_provider.dtsi`Определение всех тактовых узлов в
- `clock_consumer.dtsi`Ссылки в каждом узле dts драйвера

## 4.10 МОЩНОСТЬ

Параметры конфигурации:

```shell
CONFIG_CANAAN_PM_DOMAIN
```

Файлы драйвера:

```shell
drivers/soc/canaan/k510_pm_domains.c
```

Дерево устройств:

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

- `power_provider.dtsi` Определен узел dts поставщика
- `include/dt-bindings/soc/canaan,k510_pm_domains.h` Все домены питания определяются в
- `power_consumer.dtsi`Ссылка на <a0> указана в соответствующих узлах dts драйверов

## 4.11 СБРОС

Параметры конфигурации:

```shell
CONFIG_COMMON_RESET_K510
```

Файлы драйвера:

```shell
drivers/reset/canaan/reset-k510.c
```

Дерево устройств:

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

- `reset_provider.dtsi` Определен узел dts поставщика
- `include/ dt-bindings/reset/canaan-k510-reset.h` Все сигналы сброса определяются в
- `reset_consumer.dtsi`Ссылка на <a0> указана в соответствующих узлах dts драйверов

## 4.12 PINCTL

Параметры конфигурации:

```shell
CONFIG_PINCTRL_K510
```

Файлы драйвера:

```shell
drivers/pinctrl/canaan
```

Связанное дерево устройств:

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

`iomux_provider.dtsi` Определен узел dts поставщика
`include/include/dt-bindings/pinctrl/k510.h`Все номера функций ввода-вывода определяются в
`iomux_consumer.dtsi`Ссылка на <a0> указана в соответствующих узлах dts драйверов

## 4.13 H264

Параметры конфигурации:

```shell
CONFIG_ ALLEGRO_CODEC_DRIVER
```

Файлы драйвера:

```shell
drivers/media/platform/canaan/al5r
```

Связанное дерево устройств:

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

API: Узел файла устройства: `/dev/h264-codec`

Интерфейс программирования: Linux файл IO(открыть, закрыть, ioctl), см. справочную страницу Linux

Поддерживаемые команды IOCTL:

```c
#define AL_CMD_IP_WRITE_REG    _IOWR('q', 10, struct al5_reg)
#define AL_CMD_IP_READ_REG     _IOWR('q', 11, struct al5_reg)
#define AL_CMD_IP_WAIT_IRQ     _IOWR('q', 12, int)
#define AL_CMD_IP_IRQ_CNT      _IOWR('q', 13, int)
#define AL_CMD_IP_CLR_IRQ      _IOWR('q', 14, int)
```

Пример кода:`package/h264_demo/src`

## 4.14 DSP

Параметры конфигурации:

```shell
CONFIG_ K510_DSP_DRIVER
```

Файлы драйвера:

```shell
drivers/misc/canaan/k510-dsp
```

Связанное дерево устройств:

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

API: Узел файла устройства: `/dev/k510-dsp`

Интерфейс программирования: Linux файл IO(открыть, закрыть, ioctl), см. справочную страницу Linux

Поддерживаемые команды ioctl:

```c
#define DSP_CMD_BOOT       _IOWR('q', 1, unsigned long)
```

Пример кода:

```shell
package/dsp_app/src/
package/dsp_app_evb_lp3_v1_1/src/
```

## 4.15 ГНН

Параметры конфигурации:

```shell
CONFIG_ K510_GNNE_DRIVER
```

Файлы драйвера:

```shell
drivers/misc/canaan/gnne
```

Связанное дерево устройств:

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

API: Узел файла устройства: /dev/k510-gnne
Интерфейс программирования: Linux файл IO(открыть, закрыть, ioctl), см. справочную страницу Linux
Поддерживаемые команды ioctl:

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

Пример кода:

```shell
package/nncase_demo/src/mobilenetv2
```

## 4.16 ДВАД

Параметры конфигурации:

```shell
CONFIG_K510_2D_DRIVER
```

Файлы драйвера:

```shell
drivers/media/platform/canaan/kendryte_2d.c
```

Связанное дерево устройств:

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

API: узел файла устройства: /dev/kendryte_2d
Интерфейс программирования: Linux файл IO(открыть, закрыть, ioctl), см. справочную страницу Linux
Поддерживаемые команды ioctl:

```c
#define KENDRTY_2DROTATION_90     _IOWR('k', 0, unsigned long)
#define KENDRTY_2DROTATION_270    _IOWR('k', 1, unsigned long)

#define KENDRTY_2DROTATION_INPUT_ADDR     _IOWR('k', 2, unsigned long)
#define KENDRTY_2DROTATION_OUTPUT_ADDR    _IOWR('k', 3, unsigned long)
#define KENDRTY_2DROTATION_GET_REG_VAL    _IOWR('k', 4, unsigned long)
```

## 4.17 AES и SHA

Параметры конфигурации:

```shell
CONFIG_CRYPTO_DEV_KENDRYTE_CRYP
```

Файлы драйвера:

```shell
drivers/crypto/kendryte/kendryte-aes.c
drivers/crypto/kendryte/kendryte-aes.h
drivers/crypto/kendryte/kendryte-hash.c
drivers/crypto/kendryte/kendryte-hash.h
```

Связанное дерево устройств:

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

API: Файлы узла устройства:`/sys/bus/platform/devices/91000000.aes`
`/sys/bus/platform/devices/91010000.sha`

Интерфейс программирования: пользовательские программы используют сокеты для доступа к API драйвера ядра, где находится справочная документация`/Documentation/crypto/userspace-if.rst`

Пример кода:

```shell
package/crypto_demo/src
```

## 4.18 Мониторинг температуры - тепловой

Параметры конфигурации:

```shell
CONFIG_THERMAL
CONFIG_CANAAN_THERMAL
```

Файлы драйвера:

```shell
drivers/thermal/canaan_thermal.c
```

Связанное дерево устройств:

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

Способ применения:

```shell
cd /sys/class/thermal/thermal_zone0/
echo enabled > mode
cat temp
```

## 4.19 2D вращение - два

Параметры конфигурации:

```shell
CONFIG_KENDRYTE_TWOD_SUPPORT
CONFIG_KENDRYTE_TWOD
```

Файлы драйвера:

```shell
drivers/video/canaan/twod/kendryte_td.c
drivers/video/canaan/twod/kendryte_td_reg.c
drivers/video/canaan/twod/kendryte_td.h
drivers/video/canaan/twod/kendryte_td_table.h
```

Связанное дерево устройств:

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

# 5 Меры предосторожности

не

**Отказ от ответственности за **перевод  
Для удобства клиентов Canaan использует переводчик AI для перевода текста на несколько языков, которые могут содержать ошибки. Мы не гарантируем точность, надежность или своевременность предоставленных переводов. Компания Canaan не несет ответственности за любые убытки или ущерб, вызванные доверием к точности или надежности переведенной информации. При наличии разницы в содержании переводов на разные языки преимущественную силу имеет упрощенная версия на китайском языке. 

Если вы хотите сообщить об ошибке или неточности перевода, пожалуйста, не стесняйтесь обращаться к нам по почте.