![ханаанское покрытие.png](http://s2.loli.net/2022/03/30/7UG1IxrOXTo2QKw.png)

**<font face="黑体" size="6" style="float:right">K510 nncase Руководство разработчика</font>**

<font face="黑体"  size=3>Версия документа: V1.0.1</font>

<font face="黑体"  size=3>Опубликовано: 2022-05-10</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**Отказ**</font>
Продукты, услуги или функции, которые вы покупаете, регулируются коммерческими контрактами и условиями Beijing Canaan Jiesi Information Technology Co., Ltd. («Компания», то же самое далее), и все или часть продуктов, услуг или функций, описанных в этом документе, могут не входить в сферу вашей покупки или использования. Если иное не оговорено в договоре, Компания отказывается от всех заявлений или гарантий, явных или подразумеваемых, в отношении точности, надежности, полноты, маркетинга, конкретной цели и ненападения любых заявлений, информации или содержания этого документа. Если не согласовано иное, настоящий документ предоставляется только в качестве руководства для использования.
В связи с обновлением версии продукта или по другим причинам содержимое этого документа может время от времени обновляться или изменяться без какого-либо уведомления.

**<font face="黑体"  size=3>Уведомления о товарных знаках</font>**

""<img src="http://s2.loli.net/2022/03/30/xN21jbhnwSFyGRD.png" style="zoom:33%;" />, значок "Canaan", Canaan и другие товарные знаки Canaan и другие товарные знаки Canaan являются товарными знаками Beijing Canaan Jiesi Information Technology Co., Ltd. Все другие товарные знаки или зарегистрированные товарные знаки, которые могут быть упомянуты в этом документе, принадлежат их соответствующим владельцам.

**<font face="黑体"  size=3>Copyright ©2022 Пекин Ханаан Цзеси Информационные технологии Co., Ltd</font>**
Настоящий документ применим только к разработке и проектированию платформы K510, без письменного разрешения компании, ни одно подразделение или частное лицо не может распространять часть или все содержание этого документа в любой форме.

**<font face="黑体"  size=3>Пекин Ханаан Цзеси Информационные Технологии Co., Ltd</font>**
URL: canaan-creative.com
Бизнес-запросы: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# предисловие
**<font face="黑体"  size=5>Назначение </font>**документа
Этот документ представляет собой документ с описанием использования компилятора nncase/K510, предоставляющий пользователям информацию об установке nncase, вызове API компилятора для компиляции моделей нейронных сетей и API среды выполнения для написания программ вывода ИИ.

**<font face="黑体"  size=5>Объекты чтения</font>**

Основные люди, к которым относится этот документ (это руководство):

- Разработчики программного обеспечения
- Персонал технической поддержки

**<font face="黑体"  size=5>Термины и аббревиатуры</font>**

| срок | Пояснение/ФИО                              |
| ---- | -------------------------------------- |
| ПТК  | Посттренировочное квантование, посттренировочное квантование |
| МШЭ  | среднеквадратическая погрешность, средняя квадратная погрешность            |
|      |                                        |

**<font face="黑体"  size=5>История изменений</font>**
 <font face="宋体"  size=2>Журнал изменений накапливает описание каждого обновления документа. Последняя версия документа содержит обновления для всех предыдущих версий. </font>

| Номер версии   | Изменено     | Дата пересмотра | Примечания к пересмотру |
|  :-----  |-------   |  ------  |  ------  |
| Версия 1.0.1 | Гласность | 2022-05-10 | nncase_v1.6.1 |
| Версия 1.0.0 | Чжан Ян/Чжан Цзичжао/Ян Хаоци | 2022-05-06 | nncase_v1.6.0 |
| V0.9.0 | Гласность | 2022-04-01 | nncase_v1.5.0 |
| Версия 0.8.0 | Чжан Ян/Чжан Цзичжао | 2022-03-03 | nncase_v1.4.0 |
| Версия 0.7.0 | Гласность | 2022-01-28 | nncase_v1.3.0 |
| Версия 0.6.0 | Гласность | 2021-12-31 | nncase_v1.2.0 |
| Версия 0.5.0 | Гласность | 2021-12-03 | nncase_v1.1.0 |
| Версия 0.4.0 | Чжан Ян/Хаоци Ян/Чжэн Цихан | 2021-10-29 | nncase_v1.0.0 |
| Версия 0.3.0 | Чжан Ян / Ян Хаоци | 2021-09-28 | nncase_v1.0.0_rc1 |
| Версия 0.2.0 | Чжан Ян / Ян Хаоци | 2021-09-02 | nncase_v1.0.0_beta2 |
| Версия 0.1.0 | Чжан Ян / Ян Хаоци | 2021-08-31 | nncase_v1.0.0_beta1 |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>Содержание</font>**

[ОГЛАВЛЕНИЯ]

<div style="page-break-after:always"></div>

# 1 Введение в среду разработки

## 1.1 Операционная система

- Ubuntu 18.04/20.04

## 1.2 Программная среда

Требования к программной среде приведены в следующей таблице:

| порядковый номер | Программные ресурсы        | иллюстрировать                        |
| ---- | --------------- | --------------------------- |
| 1    | Питон          | Python 3.6/3.7/3.8/3.9/3.10 |
| 2    | пип3            | pip3 версия > = 20.3            |
| 3    | оннкс            | Версия onnx 1.9.0             |
| 4    | onnx-упрощение | Версия onnx-simplifier - 0.3.6  |
| 5    | onnxoptimizer   | Версия onnxoptimizer - 0.2.6    |

## 1.3 Аппаратная среда

Требования к аппаратной среде приведены в следующей таблице:

| порядковый номер | Аппаратные ресурсы     | иллюстрировать |
| ---- | ------------ | ---- |
| 1    | K510 CRB     |      |
| 2    | SD-карта и устройство чтения карт памяти |      |

# 2 Введение в nncase

## 2.1 Что такое nncase

nncase - это нейросетевой компилятор, предназначенный для ускорителей ИИ, и в настоящее время поддерживает такие цели, как CPU / K210 / K510

Функции, предоставляемые nncase

- Поддержка нескольких входных и нескольких выходных сетей, поддержка многоветвистой структуры
- Статическое выделение памяти, не требуется память кучи
- Объединение и оптимизация операторов
- Поддерживает вывод квантования float и uint8/int8
- Поддержка квантования после обучения с использованием моделей с плавающей запятой и калибровочных наборов квантования
- Плоская модель с поддержкой нулевой загрузки копий

Фреймворк нейронной сети, поддерживаемый nncase

- тфлит
- оннкс
- кафе

## 2.2 Преимущества продукта

- **Простое комплексное развертывание**

  Уменьшите количество взаимодействий с пользователями. Развертывание на ключевых индикаторах производительности может быть выполнено путем использования и развертывания одних и тех же инструментов и процессов для моделей ЦП и ГП. Нет необходимости задавать сложные параметры, снижать порог использования, ускорять цикл итерации алгоритмов ИИ.
- **В полной мере используйте существующую экосистему ИИ**

  Прикреплен к структуре, широко используемой в отрасли. С одной стороны, он может улучшить свою видимость и пользоваться дивидендами зрелой экологии. С другой стороны, затраты на разработку малых и средних разработчиков могут быть снижены, а зрелые модели и алгоритмы в отрасли могут быть непосредственно развернуты.
- **Получите максимальную отдачу от своего оборудования**

  Преимущество NPU заключается в том, что производительность выше, чем у CPU и GPU, и компилятор DL должен быть в состоянии полностью использовать производительность оборудования. Компилятор также должен адаптивно оптимизировать производительность для новой структуры модели, поэтому в дополнение к ручной оптимизации необходимо изучить новый метод автоматической оптимизации.
- **Масштабируемость и удобство сопровождения**

  Возможность поддержки развертывания моделей ИИ для K210, K510 и будущих чипов. Некоторая масштабируемость должна быть обеспечена на архитектурном уровне. Добавление нового целевого объекта обходится дешевле и позволяет повторно использовать как можно больше модулей. Ускорить разработку новых продуктов для достижения технологического накопления DL Compiler.

## 2.3 nncase архитектура

<img src="https://i.loli.net/2021/08/18/IQR12SOJdzxTUZH.png" alt="nncase_arch.png" style="zoom:67%;" />

Программный стек nnncase в настоящее время состоит из двух частей: компилятора и среды выполнения.

**Компилятор:** используется для компиляции моделей нейронных сетей на ПК и в конечном итоге генерирует файл kmodel. Он в основном включает в себя importer, IR, Evaluator, Quantize, Transform optimization, Tiling, Partition, Schedule, Codegen и другие модули.

- Импортер: импорт моделей из других платформ нейронных сетей в nncase
- IR: Среднее представление, разделенное на импортируемый импортером нейтральный ИК (независимый от устройства) и Nutral IR, генерируемый путем понижения конверсии Target IR (зависящий от устройства)
- Оценщик: Оценщик обеспечивает интерпретирующее выполнение ИК и часто используется в таких сценариях, как постоянное складывание /калибровка PTQ.
- Преобразование: для ИК-преобразования и оптимизации обхода графа и т. Д.
- Квантование: квантование после обучения, добавление маркеров квантования к тензору, подлежащему квантованию, вызов оценщика для выполнения интерпретации в соответствии с входным набором коррекций, сбор диапазона тензорных данных, вставка узлов квантования/деквантизации и, наконец, оптимизация для устранения ненужных узлов квантования/деквантизации и т. Д.
- Мозаика: Ограниченная меньшим объемом памяти NPU, большие куски вычислений должны быть разделены. Кроме того, выбор параметра Tilling при большом объеме мультиплексирования данных в расчете повлияет на задержку и пропускную способность.
- Раздел: Разделить график по ModuleType, каждый подграф после разделения будет соответствовать RuntimeModule, разные типы RuntimeModule соответствуют разным устройствам (cpu/K510)
- Расписание: создает порядок вычислений и выделяет буферы на основе зависимостей данных в оптимизированном графе.
- Codegen: вызовите codegen, соответствующий ModuleType для каждого подграфа, для создания RuntimeModule

**Среда выполнения**: интегрированная в пользовательское приложение, она предоставляет такие функции, как загрузка kmodel / настройка входных данных, выполнение KPU и получение выходных данных

# 3 Установка nncase

Компиляторная часть цепочки инструментов nncase включает в себя компилятор nncase и K510, оба из которых должны установить соответствующий пакет колес.

- Пакет nncase wheel был[выпущен на nncase github](https://github.com/kendryte/nncase/releases/tag/v1.6.0), поддерживая Python 3.6 / 3.7 / 3.8 / 3.9 / 3.10, пользователи могут выбрать соответствующую версию для загрузки в соответствии с операционной системой и Python
- Пакет колесика компилятора K510 находится в каталоге x86_64 пакета SDK nncase, не зависит от версии Python и может быть установлен напрямую

Если у вас нет среды Ubuntu, вы можете использовать[nncase docker](https://github.com/kendryte/nncase/blob/master/docs/build.md#docker)(Ubuntu 20.04 + Python 3.8).

```shell
cd /path/to/nncase_sdk
docker pull registry.cn-hangzhou.aliyuncs.com/kendryte/nncase:latest
docker run -it --rm -v `pwd`:/mnt -w /mnt registry.cn-hangzhou.aliyuncs.com/kendryte/nncase:latest /bin/bash -c "/bin/bash"
```

Ниже в качестве примера можно привести установку nncase в Ubuntu 20.04 + Python 3.8

```shell
wget -P x86_64 https://github.com/kendryte/nncase/releases/download/v1.6.0/nncase-1.6.0.20220505-cp38-cp38-manylinux_2_24_x86_64.whl
pip3 install x86_64/*.whl
```
<!-- markdownlint-disable no-emphasis-as-header -->
# 4 Модель компиляции/вывода

nncase предоставляет**API Python**для компиляции/вывода моделей глубокого обучения на ПК

## 4.1 Поддерживаемые операторы

### 4.1.1 Tflite оператор

| Оператор                | Поддерживается |
| ----------------------- | ------------ |
| ПРЕСС                     | ✅            |
| ДОБАВЛЯТЬ                     | ✅            |
| ARG_MAX                 | ✅            |
| ARG_MIN                 | ✅            |
| AVERAGE_POOL_2D         | ✅            |
| BATCH_MATMUL            | ✅            |
| ГИПС                    | ✅            |
| ПОКРЫВАТЬ                    | ✅            |
| КОНКАТЕНАЦИЯ           | ✅            |
| CONV_2D                 | ✅            |
| ТЕЛО                     | ✅            |
| ОБЫЧАЙ                  | ✅            |
| DEPTHWISE_CONV_2D       | ✅            |
| Дивизион                     | ✅            |
| РАВНЫЙ                   | ✅            |
| ЭКСП                     | ✅            |
| EXPAND_DIMS             | ✅            |
| ЭТАЖ                   | ✅            |
| FLOOR_DIV               | ✅            |
| FLOOR_MOD               | ✅            |
| FULLY_CONNECTED         | ✅            |
| БОЛЬШЕ                 | ✅            |
| GREATER_EQUAL           | ✅            |
| L2_NORMALIZATION        | ✅            |
| LEAKY_RELU              | ✅            |
| МЕНЕЕ                    | ✅            |
| LESS_EQUAL              | ✅            |
| ЖУРНАЛ                     | ✅            |
| ЛОГИСТИЧЕСКИЙ                | ✅            |
| MAX_POOL_2D             | ✅            |
| МАКСИМУМ                 | ✅            |
| ЗНАЧИТЬ                    | ✅            |
| МИНИМУМ                 | ✅            |
| Я                     | ✅            |
| ОТРИЦАТЕЛЬНЫЙ                     | ✅            |
| NOT_EQUAL               | ✅            |
| ПОДУШЕЧКА                     | ✅            |
| ПАДВ2                   | ✅            |
| MIRROR_PAD              | ✅            |
| УПАКОВЫВАТЬ                    | ✅            |
| ВОЕННОПЛЕННЫЙ                     | ✅            |
| REDUCE_MAX              | ✅            |
| REDUCE_MIN              | ✅            |
| REDUCE_PROD             | ✅            |
| РЕЛУ                    | ✅            |
| ПРЕЛУ                   | ✅            |
| РЕЛУ6                   | ✅            |
| ПРИОБРЕТАТЬ НОВУЮ ФОРМУ                 | ✅            |
| RESIZE_BILINEAR         | ✅            |
| RESIZE_NEAREST_NEIGHBOR | ✅            |
| КРУГЛЫЙ                   | ✅            |
| РСКРТ                   | ✅            |
| ФОРМА                   | ✅            |
| БЕЗ                     | ✅            |
| ЛОМТИК                   | ✅            |
| СОФТМАКС                 | ✅            |
| SPACE_TO_BATCH_ND       | ✅            |
| СЖИМАТЬ                 | ✅            |
| BATCH_TO_SPACE_ND       | ✅            |
| STRIDED_SLICE           | ✅            |
| СКРТ                    | ✅            |
| ПЛОЩАДЬ                  | ✅            |
| СУБ                     | ✅            |
| СУММА                     | ✅            |
| СОМНИТЕЛЬНЫЙ                    | ✅            |
| КАФЕЛЬ                    | ✅            |
| ТРАНСПОНИРОВАТЬ               | ✅            |
| TRANSPOSE_CONV          | ✅            |
| КВАНТОВАТЬ                | ✅            |
| FAKE_QUANT              | ✅            |
| ДЕКВАНТИЗАЦИЯ              | ✅            |
| СОБИРАТЬ                  | ✅            |
| GATHER_ND               | ✅            |
| ONE_HOT                 | ✅            |
| SQUARED_DIFFERENCE      | ✅            |
| LOG_SOFTMAX             | ✅            |
| РАСКАЛЫВАТЬ                   | ✅            |
| HARD_SWISH              | ✅            |

### 4.1.2 оператор onnx

| Оператор              | Поддерживается |
| --------------------- | ------------ |
| Пресс                   | ✅            |
| Акос                  | ✅            |
| Акош                 | ✅            |
| И                   | ✅            |
| АргМакс                | ✅            |
| АргМин                | ✅            |
| Соленый                  | ✅            |
| Асинх                 | ✅            |
| Добавлять                   | ✅            |
| Среднийпул           | ✅            |
| Пакетнормализация    | ✅            |
| Гипс                  | ✅            |
| Покрывать                  | ✅            |
| Кому                  | ✅            |
| Клип                  | ✅            |
| Конкат                | ✅            |
| Постоянный              | ✅            |
| КонстантаФима       | ✅            |
| Конв                  | ✅            |
| КонвТранспозиция         | ✅            |
| Тело                   | ✅            |
| Спокойный                  | ✅            |
| КумСум                | ✅            |
| ГлубинаПространство          | ✅            |
| ДеквантизЛинейный      | ✅            |
| Див                   | ✅            |
| Отсева               | ✅            |
| Жизнь                   | ✅            |
| Эксп                   | ✅            |
| Расширять                | ✅            |
| Равный                 | ✅            |
| Выравнивать               | ✅            |
| Этаж                 | ✅            |
| Собирать                | ✅            |
| GatherND              | ✅            |
| Гемм                  | ✅            |
| ГлобалСреднийПул     | ✅            |
| ГлобалМаксПул         | ✅            |
| Больше               | ✅            |
| БольшойОрРавный        | ✅            |
| Хардмакс               | ✅            |
| ХардСигмоидный           | ✅            |
| ХардШвиш             | ✅            |
| Тождество              | ✅            |
| ЭкземплярНормализация | ✅            |
| LpНормализация       | ✅            |
| LeakyRelu             | ✅            |
| Менее                  | ✅            |
| LessOrEqual           | ✅            |
| Журнал                   | ✅            |
| ЛогСофтмакс            | ✅            |
| ЛРН                   | ✅            |
| ЛСТМ                  | ✅            |
| МатМуль                | ✅            |
| МаксПул               | ✅            |
| Макс                   | ✅            |
| Мин                   | ✅            |
| Я                   | ✅            |
| Отрицательный                   | ✅            |
| Не                   | ✅            |
| OneHot                | ✅            |
| Подушечка                   | ✅            |
| Военнопленный                   | ✅            |
| Прэлу                 | ✅            |
| QuantizeLinear        | ✅            |
| СлучайныйНормальный          | ✅            |
| СлучайныйНормальныйПодобный      | ✅            |
| РандомУниформа         | ✅            |
| СлучайныйОднородныйПодобный     | ✅            |
| СокращениеL1              | ✅            |
| СокращениеL2              | ✅            |
| УменьшитьЛогСумма          | ✅            |
| УменьшитьЛогСуммаЭксп       | ✅            |
| УменьшитьМакс             | ✅            |
| УменьшитьМеан            | ✅            |
| УменьшитьМин             | ✅            |
| ReduceProd            | ✅            |
| Уменьшениесум             | ✅            |
| УменьшитьСумквадрат       | ✅            |
| Релу                  | ✅            |
| Приобретать новую форму               | ✅            |
| Изменять размеры                | ✅            |
| Обратнаяпоследовательность       | ✅            |
| RoiAlign              | ✅            |
| Круглый                 | ✅            |
| Деревня                  | ✅            |
| Форма                 | ✅            |
| Знак                  | ✅            |
| Без                   | ✅            |
| Рождение                  | ✅            |
| Имеющий форму буквы               | ✅            |
| Размер                  | ✅            |
| Ломтик                 | ✅            |
| Софтмакс               | ✅            |
| Софтплюс              | ✅            |
| Софтшигн              | ✅            |
| ПространствоДляглубь          | ✅            |
| Раскалывать                 | ✅            |
| Скверт                  | ✅            |
| Сжимать               | ✅            |
| Суб                   | ✅            |
| Сумма                   | ✅            |
| Сомнительный                  | ✅            |
| Кафель                  | ✅            |
| ТопК                  | ✅            |
| Транспонировать             | ✅            |
| Трилу                 | ✅            |
| Апсампл              | ✅            |
| Отжать             | ✅            |
| Где                 | ✅            |

### 4.1.3 Оператор кафе

| Оператор              | Поддерживается |
| --------------------- | ------------ |
| Ввод                 | ✅            |
| Конкат                | ✅            |
| Извилина           | ✅            |
| Эльтвайз               | ✅            |
| Трейд-ин               | ✅            |
| релу                  | ✅            |
| Приобретать новую форму               | ✅            |
| Ломтик                 | ✅            |
| Софтмакс               | ✅            |
| Раскалывать                 | ✅            |
| ПродолжениеИндикатор | ✅            |
| Объединения               | ✅            |
| BatchNorm             | ✅            |
| Шкала                 | ✅            |
| Обратный               | ✅            |
| ЛСТМ                  | ✅            |
| ВнутреннийПродукт          | ✅            |

## 4.2 API компиляции модели

В настоящее время API модели компиляции поддерживает фреймворки глубокого обучения, такие как tflite/onnx/caffe.

### 4.2.1 CompileOptions

**Описание функции**

Класс CompileOptions для настройки параметров компиляции nncase

**Определение класса**

```python
py::class_<compile_options>(m, "CompileOptions")
    .def(py::init())
    .def_readwrite("target", &compile_options::target)
    .def_readwrite("quant_type", &compile_options::quant_type)
    .def_readwrite("w_quant_type", &compile_options::w_quant_type)
    .def_readwrite("use_mse_quant_w", &compile_options::use_mse_quant_w)
    .def_readwrite("split_w_to_act", &compile_options::split_w_to_act)
    .def_readwrite("preprocess", &compile_options::preprocess)
    .def_readwrite("swapRB", &compile_options::swapRB)
    .def_readwrite("mean", &compile_options::mean)
    .def_readwrite("std", &compile_options::std)
    .def_readwrite("input_range", &compile_options::input_range)
    .def_readwrite("output_range", &compile_options::output_range)
    .def_readwrite("input_shape", &compile_options::input_shape)
    .def_readwrite("letterbox_value", &compile_options::letterbox_value)
    .def_readwrite("input_type", &compile_options::input_type)
    .def_readwrite("output_type", &compile_options::output_type)
    .def_readwrite("input_layout", &compile_options::input_layout)
    .def_readwrite("output_layout", &compile_options::output_layout)
    .def_readwrite("model_layout", &compile_options::model_layout)
    .def_readwrite("is_fpga", &compile_options::is_fpga)
    .def_readwrite("dump_ir", &compile_options::dump_ir)
    .def_readwrite("dump_asm", &compile_options::dump_asm)
    .def_readwrite("dump_quant_error", &compile_options::dump_quant_error)
    .def_readwrite("dump_dir", &compile_options::dump_dir)
    .def_readwrite("benchmark_only", &compile_options::benchmark_only);
```

Каждое свойство описано ниже

| Название недвижимости         | тип   | Да или нет | описание                                                         |
| ---------------- | ------ | -------- | ------------------------------------------------------------ |
| цель           | струна | быть       | Укажите целевой объект компиляции, например 'k210', 'k510'                               |
| quant_type       | струна | не       | Укажите тип квантования данных, например 'uint8', 'int8'                          |
| w_quant_type     | струна | не       | Укажите тип квантования веса, например 'uint8', 'int8', по умолчанию 'uint8'           |
| use_mse_quant_w  | буль   | не       | Указывает, следует ли использовать алгоритм среднеквадратичной ошибки (MSE) для оптимизации параметров квантования при квантовании весов |
| split_w_to_act   | буль   | не       | Указывает, следует ли балансировать данные частичного веса в активные данные.                       |
| Предварительной обработки       | буль   | не       | Независимо от того, включена ли предварительная обработка или нет, по умолчанию установлено значение False                                  |
| swapRB           | буль   | не       | Следует ли обмениваться входными данными RGB между красным и синим каналами (RGB--> BGR или BGR->RGB), по умолчанию используется значение False |
| значить             | список   | не       | Предварительная обработка нормализует среднее значение параметра, которое по умолчанию имеет значение[0, 0, 0]                        |
| Стд              | список   | не       | Предварительная обработка нормализует дисперсию параметров, которая по умолчанию имеет значение[1, 1, 1]                        |
| input_range      | список   | не       | Диапазон чисел с плавающей запятой после деквантизации входных данных, который по умолчанию имеет значение[0，1]               |
| output_range     | список   | не       | Диапазон чисел с плавающей запятой перед выводом данных с фиксированной точкой, который по умолчанию пустый                     |
| input_shape      | список   | не       | Укажите форму входных данных, макет input_shape должен соответствовать входному макету, а input_shape входных данных не согласуется с входной формой модели, и будет выполнена операция bitbox (resize/pad и т.д.). |
| letterbox_value  | плавать  | не       | Задает значение заполнения поля выборки предварительной обработки.                                  |
| input_type       | струна | не       | Задает тип входных данных, по умолчанию равный 'float32'                          |
| output_type      | струна | не       | Задает тип выходных данных, таких как 'float32', 'uint8' (только для заданного квантования), по умолчанию имеет значение 'float32' |
| input_layout     | струна | не       | Укажите расположение входных данных, таких как 'NCHW', 'NHWC'. Если макет входных данных отличается от самой модели, nncase вставляет транспонирование для преобразования |
| output_layout    | струна | не       | Укажите выходные данные для макета, такие как 'NCHW', 'NHWC'. Если макет выходных данных отличается от самой модели, nncase вставит транспонирование для преобразования |
| model_layout     | струна | не       | Укажите макет модели, который по умолчанию пустый, и укажите, когда макет модели tflite — «NCHW», а модели Onnx и Caffe — «NHWC». |
| is_fpga          | буль   | не       | Указывает, используется ли kmodel для FPGA, значение которого по умолчанию равно False.                          |
| dump_ir          | буль   | не       | Указывает, имеет ли IR дампа значение по умолчанию значение False                                 |
| dump_asm         | буль   | не       | Указывает, является ли файл сборки дампа ASM, который по умолчанию имеет значение False                        |
| dump_quant_error | буль   | не       | Указывает, квантует ли дамп ошибку модели до и после                               |
| dump_dir         | струна | не       | После указания dump_ir и других параметров ранее, здесь вы указываете каталог дампа, который по умолчанию имеет пустую строку  |
| benchmark_only   | буль   | не       | Указывает, используется ли kmodel только для теста производительности, который по умолчанию имеет значение False                   |

> 1. Входной диапазон — это диапазон чисел с плавающей запятой, то есть если тип входных данных uint8, то входным диапазоном является диапазон после деквантизации в плавающую точку (не может быть 0 ~ 1), который может быть свободно указан.
> 2. input_shape должны быть указаны в соответствии с input_layout, [1，224，224，3]например, если input_layout является NCHW, input_shape должен быть указан как[1,3,224,224]; input_layout является NHWC, input_shape должен быть указан как[1,224,224,3];
> 3. mean и std являются параметрами для нормализации чисел с плавающей запятой, которые пользователь может указать;
> 4. При использовании функции letterbox нужно ограничить размер ввода до 1,5 МБ, а размер одного канала находится в пределах 0,75 МБ;
>
> Например:
>
> 1. Тип входных данных установлен в uint8, input_range задано значение[0,255], роль деквантизации заключается только в преобразовании типа, преобразовании данных uint8 в float32, а параметры mean и std все еще могут быть указаны в соответствии с данными 0 ~ 255
> 2. Для типа входных данных задано значение uint8, input_range задано [0,1]значение, число с фиксированной точкой деквантизируется до [0,1]числа с плавающей запятой в диапазоне, а среднее и std должны быть указаны в соответствии с новым диапазоном чисел с плавающей запятой.

Процесс предварительной обработки выглядит следующим образом (зеленые узлы на рисунке являются необязательными):

![препроцесс.png](https://i.loli.net/2021/11/08/fhBLsozUTCbt4dp.png)

**Пример кода**

Создание экземпляра CompileOptions, настройка значений каждого свойства

```python
# compile_options
compile_options = nncase.CompileOptions()
compile_options.target = target
compile_options.input_type = 'float32'  # or 'uint8' 'int8'
compile_options.output_type = 'float32'  # or 'uint8' 'int8'. Only work in PTQ
compile_options.output_range = []  # Only work in PTQ and output type is not "float32"
compile_options.preprocess = True # if False, the args below will unworked
compile_options.swapRB = True
compile_options.input_shape = [1,224,224,3] # keep layout same as input layout
compile_options.input_layout = 'NHWC'
compile_options.output_layout = 'NHWC'
compile_options.model_layout = '' # Specific it when tflite model with "NCHW" layout and Onnx(Caffe) model with "NHWC" layout
compile_options.mean = [0,0,0]
compile_options.std = [1,1,1]
compile_options.input_range = [0,1]
compile_options.letterbox_value = 114. # pad what you want
compile_options.dump_ir = True
compile_options.dump_asm = True
compile_options.dump_dir = 'tmp'
```

### 4.2.2 ИмпортОпции

**Описание функции**

Класс ImportOptions для настройки параметров импорта nncase

**Определение класса**

```python
py::class_<import_options>(m, "ImportOptions")
    .def(py::init())
    .def_readwrite("output_arrays", &import_options::output_arrays);
```

Каждое свойство описано ниже

| Название недвижимости      | тип   | Да или нет | описание     |
| ------------- | ------ | -------- | -------- |
| output_arrays | струна | не       | Выходное имя |

**Пример кода**

Создание экземпляра ImageOptions, настройка значений каждого свойства

```python
# import_options
import_options = nncase.ImportOptions()
import_options.output_arrays = 'output' # Your output node name
```

### 4.2.3 PTQТенсорОпции

**Описание функции**

Класс PTQTensorOptions для настройки параметров PTQ nncase

**Определение класса**

```python
py::class_<ptq_tensor_options>(m, "PTQTensorOptions")
    .def(py::init())
    .def_readwrite("calibrate_method", &ptq_tensor_options::calibrate_method)
    .def_readwrite("samples_count", &ptq_tensor_options::samples_count)
    .def("set_tensor_data", [](ptq_tensor_options &o, py::bytes bytes) {
        uint8_t *buffer;
        py::ssize_t length;
        if (PyBytes_AsStringAndSize(bytes.ptr(), reinterpret_cast<char **>(&buffer), &length))
            throw std::invalid_argument("Invalid bytes");
        o.tensor_data.assign(buffer, buffer + length);
    });
```

Каждое свойство описано ниже

| Имя поля         | тип   | Да или нет | описание                                                                                  |
| ---------------- | ------ | -------- | ------------------------------------------------------------------------------------- |
| calibrate_method | струна | не       | Метод калибровки, поддерживает 'no_clip', 'l2', 'kld_m0', 'kld_m1', 'kld_m2', 'cdf', по умолчанию 'no_clip' |
| samples_count    | инт    | не       | Количество образцов                                                                              |

#### set_tensor_data()

**Описание функции**

Установка данных коррекции

**Определение интерфейса**

```python
set_tensor_data(calib_data)
```

**Входные параметры**

| Имя параметра   | тип   | Да или нет | описание     |
| ---------- | ------ | -------- | -------- |
| calib_data | байт[] | быть       | Исправление данных |

**Возвращаемое значение**

Н/Д

**Пример кода**

```python
# ptq_options
ptq_options = nncase.PTQTensorOptions()
ptq_options.samples_count = cfg.generate_calibs.batch_size
ptq_options.set_tensor_data(np.asarray([sample['data'] for sample in self.calibs]).tobytes())
```

### 4.2.4 Компилятор

**Описание функции**

Класс компилятора для компиляции моделей нейронных сетей

**Определение класса**

```python
py::class_<compiler>(m, "Compiler")
    .def(py::init(&compiler::create))
    .def("import_tflite", &compiler::import_tflite)
    .def("import_onnx", &compiler::import_onnx)
    .def("import_caffe", &compiler::import_caffe)
    .def("compile", &compiler::compile)
    .def("use_ptq", py::overload_cast<ptq_tensor_options>(&compiler::use_ptq))
    .def("gencode", [](compiler &c, std::ostream &stream) { c.gencode(stream); })
    .def("gencode_tobytes", [](compiler &c) {
        std::stringstream ss;
        c.gencode(ss);
        return py::bytes(ss.str());
    })
    .def("create_evaluator", [](compiler &c, uint32_t stage) {
        auto &graph = c.graph(stage);
        return std::make_unique<graph_evaluator>(c.target(), graph);
    });
```

**Пример кода**

```python
compiler = nncase.Compiler(compile_options)
```

#### import_tflite()

**Описание функции**

Импорт модели tflite

**Определение интерфейса**

```python
import_tflite(model_content, import_options)
```

**Входные параметры**

| Имя параметра       | тип          | Да или нет | описание           |
| -------------- | ------------- | -------- | -------------- |
| model_content  | байт[]        | быть       | Чтение содержимого модели |
| import_options | ИмпортОпции | быть       | Параметры импорта       |

**Возвращаемое значение**

Н/Д

**Пример кода**

```python
model_content = read_model_file(model)
compiler.import_tflite(model_content, import_options)
```

#### import_onnx()

**Описание функции**

Импорт модели onnx

**Определение интерфейса**

```python
import_onnx(model_content, import_options)
```

**Входные параметры**

| Имя параметра       | тип          | Да или нет | описание           |
| -------------- | ------------- | -------- | -------------- |
| model_content  | байт[]        | быть       | Чтение содержимого модели |
| import_options | ИмпортОпции | быть       | Параметры импорта       |

**Возвращаемое значение**

Н/Д

**Пример кода**

```python
model_content = read_model_file(model)
compiler.import_onnx(model_content, import_options)
```

#### import_caffe()

**Описание функции**

Импорт модели caffe

> Пользователям необходимо скомпилировать/установить caffe на локальном компьютере.

**Определение интерфейса**

```python
import_caffe(caffemodel, prototxt)
```

**Входные параметры**

| Имя параметра   | тип   | Да или нет | описание                 |
| ---------- | ------ | -------- | -------------------- |
| кафефемодель | байт[] | быть       | Читать содержание кафемодели |
| prototxt   | байт[] | быть       | Чтение содержимого prototxt   |

**Возвращаемое значение**

Н/Д

**Пример кода**

```python
# import
caffemodel = read_model_file('test.caffemodel')
prototxt = read_model_file('test.prototxt')
compiler.import_caffe(caffemodel, prototxt)
```

#### use_ptq()

**Описание функции**

Настройка параметров конфигурации PTQ

**Определение интерфейса**

```python
use_ptq(ptq_options)
```

**Входные параметры**

| Имя параметра    | тип             | Да или нет | описание        |
| ----------- | ---------------- | -------- | ----------- |
| ptq_options | PTQТензорОпционы | быть       | Параметры конфигурации PTQ |

**Возвращаемое значение**

Н/Д

**Пример кода**

```python
compiler.use_ptq(ptq_options)
```

#### compile()

**Описание функции**

Компиляция модели нейронной сети

**Определение интерфейса**

```python
compile()
```

**Входные параметры**

Н/Д

**Возвращаемое значение**

Н/Д

**Пример кода**

```python
compiler.compile()
```

#### gencode_tobytes()

**Описание функции**

Создает поток байтов кода

**Определение интерфейса**

```python
gencode_tobytes()
```

**Входные параметры**

Н/Д

**Возвращаемое значение**

Байт[]

**Пример кода**

```python
kmodel = compiler.gencode_tobytes()
with open(os.path.join(infer_dir, 'test.kmodel'), 'wb') as f:
    f.write(kmodel)
```

## 4.3 Компиляция примера модели

В следующем примере используется модель и скрипт компиляции Python

- Модель находится в подкаталоге /path/to/nncase_sdk/examples/models/subdirectory
- Скрипт компиляции python находится в подкаталоге /path/to/nncase_sdk/examples/scripts

### 4.3.1 Компиляция модели float32 tflite

- Mobilenetv2_tflite_fp32_image.py сценарий выглядит следующим образом

```python
import nncase
import os
import argparse

def read_model_file(model_file):
    with open(model_file, 'rb') as f:
        model_content = f.read()
    return model_content

def main():
    parser = argparse.ArgumentParser(prog="nncase")
    parser.add_argument("--target", type=str, help='target to run')
    parser.add_argument("--model", type=str, help='model file')
    args = parser.parse_args()

    # compile_options
    dump_dir = 'tmp/mobilenetv2_tflite_fp32_image'
    compile_options = nncase.CompileOptions()
    compile_options.target = args.target
    compile_options.dump_ir = True
    compile_options.dump_asm = True
    compile_options.dump_dir = dump_dir

    # compiler
    compiler = nncase.Compiler(compile_options)

    # import_options
    import_options = nncase.ImportOptions()

    # import
    model_content = read_model_file(args.model)
    compiler.import_tflite(model_content, import_options)

    # compile
    compiler.compile()

    # kmodel
    kmodel = compiler.gencode_tobytes()
    with open(os.path.join(dump_dir, 'test.kmodel'), 'wb') as f:
        f.write(kmodel)

if __name__ == '__main__':
    main()
```

- Выполните следующую команду, чтобы скомпилировать tflite модель mobiletv2, target k510

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_tflite_fp32_image.py --target k510 --model models/mobilenet_v2_1.0_224.tflite
```

### 4.3.2 Компиляция модели float32 onnx

- Для моделей onnx рекомендуется упростить использование[ONNX Simplifier](https://github.com/daquexian/onnx-simplifier)перед компиляцией с помощью nncase
- mobilenetv2_onnx_fp32_image.py сценарий выглядит следующим образом

```python
import os
import onnxsim
import onnx
import nncase
import argparse

def parse_model_input_output(model_file):
    onnx_model = onnx.load(model_file)
    input_all = [node.name for node in onnx_model.graph.input]
    input_initializer = [node.name for node in onnx_model.graph.initializer]
    input_names = list(set(input_all) - set(input_initializer))
    input_tensors = [node for node in onnx_model.graph.input if node.name in input_names]

    # input
    inputs= []
    for _, e in enumerate(input_tensors):
        onnx_type = e.type.tensor_type
        input_dict = {}
        input_dict['name'] = e.name
        input_dict['dtype'] = onnx.mapping.TENSOR_TYPE_TO_NP_TYPE[onnx_type.elem_type]
        input_dict['shape'] = [(i.dim_value if i.dim_value != 0 else d) for i, d in zip(
            onnx_type.shape.dim, [1, 3, 224, 224])]
        inputs.append(input_dict)


    return onnx_model, inputs

def onnx_simplify(model_file, dump_dir):
    onnx_model, inputs = parse_model_input_output(model_file)
    onnx_model = onnx.shape_inference.infer_shapes(onnx_model)
    input_shapes = {}
    for input in inputs:
        input_shapes[input['name']] = input['shape']

    onnx_model, check = onnxsim.simplify(onnx_model, input_shapes=input_shapes)
    assert check, "Simplified ONNX model could not be validated"

    model_file = os.path.join(dump_dir, 'simplified.onnx')
    onnx.save_model(onnx_model, model_file)
    return model_file


def read_model_file(model_file):
    with open(model_file, 'rb') as f:
        model_content = f.read()
    return model_content


def main():
    parser = argparse.ArgumentParser(prog="nncase")
    parser.add_argument("--target", type=str, help='target to run')
    parser.add_argument("--model", type=str, help='model file')
    args = parser.parse_args()

    dump_dir = 'tmp/mobilenetv2_onnx_fp32_image'
    if not os.path.exists(dump_dir):
        os.makedirs(dump_dir)

    # onnx simplify
    model_file = onnx_simplify(args.model, dump_dir)

    # compile_options
    compile_options = nncase.CompileOptions()
    compile_options.target = args.target
    compile_options.dump_ir = True
    compile_options.dump_asm = True
    compile_options.dump_dir = dump_dir

    # compiler
    compiler = nncase.Compiler(compile_options)

    # import_options
    import_options = nncase.ImportOptions()

    # import
    model_content = read_model_file(model_file)
    compiler.import_onnx(model_content, import_options)

    # compile
    compiler.compile()

    # kmodel
    kmodel = compiler.gencode_tobytes()
    with open(os.path.join(dump_dir, 'test.kmodel'), 'wb') as f:
        f.write(kmodel)

if __name__ == '__main__':
    main()
```

- Выполните следующую команду, чтобы скомпилировать модель onnx mobiletv2, target k510

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_onnx_fp32_image.py --target k510 --model models/mobilenetv2-7.onnx
```

### 4.3.3 Компиляция модели float32 caffe

- Пакет колес кафе[взят из](https://github.com/kendryte/caffe/releases)кафе kendryte caffe
- conv2d_caffe_fp32.py сценарий выглядит следующим образом

```python
import nncase
import os
import argparse

def read_model_file(model_file):
    with open(model_file, 'rb') as f:
        model_content = f.read()
    return model_content

def main():
    parser = argparse.ArgumentParser(prog="nncase")
    parser.add_argument("--target", type=str, help='target to run')
    parser.add_argument("--caffemodel", type=str, help='caffemodel file')
    parser.add_argument("--prototxt", type=str, help='prototxt file')
    args = parser.parse_args()

    # compile_options
    dump_dir = 'tmp/conv2d_caffe_fp32'
    compile_options = nncase.CompileOptions()
    compile_options.target = args.target
    compile_options.dump_ir = True
    compile_options.dump_asm = True
    compile_options.dump_dir = dump_dir

    # compiler
    compiler = nncase.Compiler(compile_options)

    # import_options
    import_options = nncase.ImportOptions()

    # import
    caffemodel = read_model_file(args.caffemodel)
    prototxt = read_model_file(args.prototxt)
    compiler.import_caffe(caffemodel, prototxt)

    # compile
    compiler.compile()

    # kmodel
    kmodel = compiler.gencode_tobytes()
    with open(os.path.join(dump_dir, 'test.kmodel'), 'wb') as f:
        f.write(kmodel)

if __name__ == '__main__':
    main()
```

- Выполните следующую команду, чтобы скомпилировать модель caffe conv2d с целевым k510

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/conv2d_caffe_fp32.py --target k510 --caffemodel models/test.caffemodel --prototxt models/test.prototxt
```

### 4.3.4 Компиляция и добавление предварительной модели float32 onnx

- Для моделей onnx рекомендуется упростить использование[ONNX Simplifier](https://github.com/daquexian/onnx-simplifier)перед компиляцией с помощью nncase
- Mobilenetv2_onnx_fp32_preprocess.py сценарий выглядит следующим образом

```python
import os
import onnxsim
import onnx
import nncase
import argparse

def parse_model_input_output(model_file):
    onnx_model = onnx.load(model_file)
    input_all = [node.name for node in onnx_model.graph.input]
    input_initializer = [node.name for node in onnx_model.graph.initializer]
    input_names = list(set(input_all) - set(input_initializer))
    input_tensors = [node for node in onnx_model.graph.input if node.name in input_names]

    # input
    inputs= []
    for _, e in enumerate(input_tensors):
        onnx_type = e.type.tensor_type
        input_dict = {}
        input_dict['name'] = e.name
        input_dict['dtype'] = onnx.mapping.TENSOR_TYPE_TO_NP_TYPE[onnx_type.elem_type]
        input_dict['shape'] = [(i.dim_value if i.dim_value != 0 else d) for i, d in zip(
            onnx_type.shape.dim, [1, 3, 224, 224])]
        inputs.append(input_dict)


    return onnx_model, inputs

def onnx_simplify(model_file, dump_dir):
    onnx_model, inputs = parse_model_input_output(model_file)
    onnx_model = onnx.shape_inference.infer_shapes(onnx_model)
    input_shapes = {}
    for input in inputs:
        input_shapes[input['name']] = input['shape']

    onnx_model, check = onnxsim.simplify(onnx_model, input_shapes=input_shapes)
    assert check, "Simplified ONNX model could not be validated"

    model_file = os.path.join(dump_dir, 'simplified.onnx')
    onnx.save_model(onnx_model, model_file)
    return model_file


def read_model_file(model_file):
    with open(model_file, 'rb') as f:
        model_content = f.read()
    return model_content


def main():
    parser = argparse.ArgumentParser(prog="nncase")
    parser.add_argument("--target", type=str, help='target to run')
    parser.add_argument("--model", type=str, help='model file')
    args = parser.parse_args()

    dump_dir = 'tmp/mobilenetv2_onnx_fp32_preprocess'
    if not os.path.exists(dump_dir):
        os.makedirs(dump_dir)

    # onnx simplify
    model_file = onnx_simplify(args.model, dump_dir)

    # compile_options
    compile_options = nncase.CompileOptions()
    compile_options.target = args.target
    compile_options.input_type = 'uint8'
    compile_options.preprocess = True
    compile_options.swapRB = True
    compile_options.input_layout = 'NHWC'
    compile_options.output_layout = 'NCHW'
    compile_options.input_shape = [1, 256, 256, 3]
    compile_options.mean = [0.485, 0.456, 0.406]
    compile_options.std = [0.229, 0.224, 0.225]
    compile_options.input_range = [0, 1]
    compile_options.dump_ir = True
    compile_options.dump_asm = True
    compile_options.dump_dir = dump_dir

    # compiler
    compiler = nncase.Compiler(compile_options)

    # import_options
    import_options = nncase.ImportOptions()

    # import
    model_content = read_model_file(model_file)
    compiler.import_onnx(model_content, import_options)

    # compile
    compiler.compile()

    # kmodel
    kmodel = compiler.gencode_tobytes()
    with open(os.path.join(dump_dir, 'test.kmodel'), 'wb') as f:
        f.write(kmodel)

if __name__ == '__main__':
    main()
```

- Выполните следующую команду, чтобы скомпилировать модель onnx mobiletv2 с целевым k510

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_onnx_fp32_preprocess.py --target k510 --model models/mobilenetv2-7.onnx
```

### 4.3.5 Компиляция модели квантования uint8 tflite

- Mobilenetv2_tflite_uint8_image.py сценарий выглядит следующим образом

```python
import nncase
import os
import argparse
import numpy as np

def read_model_file(model_file):
    with open(model_file, 'rb') as f:
        model_content = f.read()
    return model_content

def generate_data(shape, batch):
    shape[0] *= batch
    data = np.random.rand(*shape).astype(np.float32)
    return data

def main():
    parser = argparse.ArgumentParser(prog="nncase")
    parser.add_argument("--target", type=str, help='target to run')
    parser.add_argument("--model", type=str, help='model file')
    args = parser.parse_args()

    input_shape = [1, 224, 224, 3]

    # compile_options
    dump_dir = 'tmp/mobilenetv2_tflite_uint8_image'
    compile_options = nncase.CompileOptions()
    compile_options.target = args.target
    compile_options.input_type = 'float32'
    compile_options.input_layout = 'NHWC'
    compile_options.output_layout = 'NHWC'
    compile_options.dump_ir = True
    compile_options.dump_asm = True
    compile_options.dump_dir = dump_dir

    # compiler
    compiler = nncase.Compiler(compile_options)

    # import_options
    import_options = nncase.ImportOptions()

    # quantize model
    compile_options.quant_type = 'uint8'

    # ptq_options
    ptq_options = nncase.PTQTensorOptions()
    ptq_options.samples_count = 10
    ptq_options.set_tensor_data(generate_data(input_shape, ptq_options.samples_count).tobytes())

    # import
    model_content = read_model_file(args.model)
    compiler.import_tflite(model_content, import_options)

    # compile
    compiler.use_ptq(ptq_options)
    compiler.compile()

    # kmodel
    kmodel = compiler.gencode_tobytes()
    with open(os.path.join(dump_dir, 'test.kmodel'), 'wb') as f:
        f.write(kmodel)

if __name__ == '__main__':
    main()
```

- Выполните следующую команду, чтобы скомпилировать tflite модель uint8 quantized mobiletv2, target k510

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_tflite_uint8_image.py --target k510 --model models/mobilenet_v2_1.0_224.tflite
```

## 4.4 API модели вывода

В дополнение к ap скомпилированной модели, nncase также предоставляет API модели вывода, которые могут быть выведены на ПК перед компиляцией kmodel, который используется для проверки согласованности результатов вывода nncase и результатов времени выполнения соответствующей платформы глубокого обучения.

### 4.4.1 Диапазон памяти

**Описание функции**

Класс MemoryRange, который используется для представления диапазона памяти

**Определение класса**

```python
py::class_<memory_range>(m, "MemoryRange")
    .def_readwrite("location", &memory_range::memory_location)
    .def_property(
        "dtype", [](const memory_range &range) { return to_dtype(range.datatype); },
        [](memory_range &range, py::object dtype) { range.datatype = from_dtype(py::dtype::from_args(dtype)); })
    .def_readwrite("start", &memory_range::start)
    .def_readwrite("size", &memory_range::size);
```

Каждое свойство описано ниже

| Название недвижимости | тип           | Да или нет | описание                                                                       |
| -------- | -------------- | -------- | -------------------------------------------------------------------------- |
| местоположение | инт            | не       | Положение памяти, 0 для входа, 1 для вывода, 2 для rdata, 3 для данных, 4 для shared_data |
| dtype    | Тип данных Python | не       | тип данных                                                                   |
| начало    | инт            | не       | Начальный адрес памяти                                                               |
| размер     | инт            | не       | Объем памяти                                                                   |

**Пример кода**

Создание экземпляра MemoryRange

```python
mr = nncase.MemoryRange()
```

### 4.4.2 Среда выполненияТенсор

**Описание функции**

Класс RuntimeTensor, представляющий тензор среды выполнения

**Определение класса**

```python
py::class_<runtime_tensor>(m, "RuntimeTensor")
    .def_static("from_numpy", [](py::array arr) {
        auto src_buffer = arr.request();
        auto datatype = from_dtype(arr.dtype());
        auto tensor = host_runtime_tensor::create(
            datatype,
            to_rt_shape(src_buffer.shape),
            to_rt_strides(src_buffer.itemsize, src_buffer.strides),
            gsl::make_span(reinterpret_cast<gsl::byte *>(src_buffer.ptr), src_buffer.size * src_buffer.itemsize),
            [=](gsl::byte *) { arr.dec_ref(); })
                          .unwrap_or_throw();
        arr.inc_ref();
        return tensor;
    })
    .def("copy_to", [](runtime_tensor &from, runtime_tensor &to) {
        from.copy_to(to).unwrap_or_throw();
    })
    .def("to_numpy", [](runtime_tensor &tensor) {
        auto host = tensor.as_host().unwrap_or_throw();
        auto src_map = std::move(hrt::map(host, hrt::map_read).unwrap_or_throw());
        auto src_buffer = src_map.buffer();
        return py::array(
            to_dtype(tensor.datatype()),
            tensor.shape(),
            to_py_strides(runtime::get_bytes(tensor.datatype()), tensor.strides()),
            src_buffer.data());
    })
    .def_property_readonly("dtype", [](runtime_tensor &tensor) {
        return to_dtype(tensor.datatype());
    })
    .def_property_readonly("shape", [](runtime_tensor &tensor) {
        return to_py_shape(tensor.shape());
    });
```

Каждое свойство описано ниже

| Название недвижимости | тип | Да или нет | описание             |
| -------- | ---- | -------- | ---------------- |
| dtype    | инт  | не       | Тип данных тензора |
| форма    | список | не       | Форма тензора     |

#### from_numpy()

**Описание функции**

Создание объекта RuntimeTensor из файла numpy.ndarray

**Определение интерфейса**

```python
from_numpy(py::array arr)
```

**Входные параметры**

| Имя параметра | тип          | Да или нет | описание              |
| -------- | ------------- | -------- | ----------------- |
| аррр      | numpy.ndarray | быть       | Объект numpy.ndarray |

**Возвращаемое значение**

Среда выполненияТенсор

**Пример кода**

```python
tensor = nncase.RuntimeTensor.from_numpy(self.inputs[i]['data'])
```

#### copy_to()

**Описание функции**

Копирование тензора среды выполнения

**Определение интерфейса**

```python
copy_to(RuntimeTensor to)
```

**Входные параметры**

| Имя параметра | тип          | Да или нет | описание              |
| -------- | ------------- | -------- | ----------------- |
| Кому       | Среда выполненияТенсор | быть       | Среда выполненияОбъектТенсор |

**Возвращаемое значение**

Н/Д

**Пример кода**

```python
sim.get_output_tensor(i).copy_to(to)
```

#### to_numpy()

**Описание функции**

Преобразование среды выполненияTensor в объект numpy.ndarray

**Определение интерфейса**

```python
to_numpy()
```

**Входные параметры**

Н/Д

**Возвращаемое значение**

Объект numpy.ndarray

**Пример кода**

```python
arr = sim.get_output_tensor(i).to_numpy()
```

### 4.4.3 Симулятор

**Описание функции**

Класс симулятора для вывода кмоделя на ПК

**Определение класса**

```python
py::class_<interpreter>(m, "Simulator")
    .def(py::init())
    .def("load_model", [](interpreter &interp, gsl::span<const gsl::byte> buffer) { interp.load_model(buffer).unwrap_or_throw(); })
    .def_property_readonly("inputs_size", &interpreter::inputs_size)
    .def_property_readonly("outputs_size", &interpreter::outputs_size)
    .def("get_input_desc", &interpreter::input_desc)
    .def("get_output_desc", &interpreter::output_desc)
    .def("get_input_tensor", [](interpreter &interp, size_t index) { return interp.input_tensor(index).unwrap_or_throw(); })
    .def("set_input_tensor", [](interpreter &interp, size_t index, runtime_tensor tensor) { return interp.input_tensor(index, tensor).unwrap_or_throw(); })
    .def("get_output_tensor", [](interpreter &interp, size_t index) { return interp.output_tensor(index).unwrap_or_throw(); })
    .def("set_output_tensor", [](interpreter &interp, size_t index, runtime_tensor tensor) { return interp.output_tensor(index, tensor).unwrap_or_throw(); })
    .def("run", [](interpreter &interp) { interp.run().unwrap_or_throw(); });
```

Каждое свойство описано ниже

| Название недвижимости     | тип | Да или нет | описание     |
| ------------ | ---- | -------- | -------- |
| inputs_size  | инт  | не       | Введите номер |
| outputs_size | инт  | не       | Количество выходов |

**Пример кода**

Создание экземпляра симулятора

```python
sim = nncase.Simulator()
```

#### load_model()

**Описание функции**

Загрузить кмодель

**Определение интерфейса**

```python
load_model(model_content)
```

**Входные параметры**

| Имя параметра      | тип   | Да или нет | описание         |
| ------------- | ------ | -------- | ------------ |
| model_content | байт[] | быть       | Поток Kmodel byte |

**Возвращаемое значение**

Н/Д

**Пример кода**

```python
sim.load_model(kmodel)
```

#### get_input_desc()

**Описание функции**

Получает описание входных данных для указанного индекса.

**Определение интерфейса**

```python
get_input_desc(index)
```

**Входные параметры**

| Имя параметра | тип | Да или нет | описание       |
| -------- | ---- | -------- | ---------- |
| индекс    | инт  | быть       | Индекс входных данных |

**Возвращаемое значение**

Диапазон памяти

**Пример кода**

```python
input_desc_0 = sim.get_input_desc(0)
```

#### get_output_desc()

**Описание функции**

Получает описание выходных данных указанного индекса.

**Определение интерфейса**

```python
get_output_desc(index)
```

**Входные параметры**

| Имя параметра | тип | Да или нет | описание       |
| -------- | ---- | -------- | ---------- |
| индекс    | инт  | быть       | Индекс выходных данных |

**Возвращаемое значение**

Диапазон памяти

**Пример кода**

```python
output_desc_0 = sim.get_output_desc(0)
```

#### get_input_tensor()

**Описание функции**

Получает объект RuntimeTensor для входных данных для указанного индекса.

**Определение интерфейса**

```python
get_input_tensor(index)
```

**Входные параметры**

| Имя параметра | тип | Да или нет | описание             |
| -------- | ---- | -------- | ---------------- |
| индекс    | инт  | быть       | Введите индекс тензора |

**Возвращаемое значение**

Среда выполненияТенсор

**Пример кода**

```python
input_tensor_0 = sim.get_input_tensor(0)
```

#### set_input_tensor()

**Описание функции**

Задает тензор среды выполнения для ввода указанного индекса

**Определение интерфейса**

```python
set_input_tensor(index, tensor)
```

**Входные параметры**

| Имя параметра | тип          | Да или нет | описание                    |
| -------- | ------------- | -------- | ----------------------- |
| индекс    | инт           | быть       | Введите индекс Среды выполненияТенсора |
| тензор   | Среда выполненияТенсор | быть       | Введите среду выполненияТензор       |

**Возвращаемое значение**

Н/Д

**Пример кода**

```python
sim.set_input_tensor(0, nncase.RuntimeTensor.from_numpy(self.inputs[0]['data']))
```

#### get_output_tensor()

**Описание функции**

Получает тензор среды выполнения для вывода указанного индекса.

**Определение интерфейса**

```python
get_output_tensor(index)
```

**Входные параметры**

| Имя параметра | тип | Да или нет | описание                    |
| -------- | ---- | -------- | ----------------------- |
| индекс    | инт  | быть       | Выводит индекс среды выполненияТенсор |

**Возвращаемое значение**

Среда выполненияТенсор

**Пример кода**

```python
output_arr_0 = sim.get_output_tensor(0).to_numpy()
```

#### set_output_tensor()

**Описание функции**

Задает RuntimeTensor для вывода указанного индекса

**Определение интерфейса**

```python
set_output_tensor(index, tensor)
```

**Входные параметры**

| Имя параметра | тип          | Да или нет | описание                    |
| -------- | ------------- | -------- | ----------------------- |
| индекс    | инт           | быть       | Выводит индекс среды выполненияТенсор |
| тензор   | Среда выполненияТенсор | быть       | Выходной тензор времени выполнения       |

**Возвращаемое значение**

Н/Д

**Пример кода**

```python
sim.set_output_tensor(0, tensor)
```

#### run()

**Описание функции**

Вывод Run kmodel

**Определение интерфейса**

```python
run()
```

**Входные параметры**

Н/Д

**Возвращаемое значение**

Н/Д

**Пример кода**

```python
sim.run()
```

## 4.5 Пример модели вывода

**Обязательное условие:**mobilenetv2_onnx_fp32_image.py сценарий был скомпилирован с моделью mobiletv2-7.onnx

mobilenetv2_onnx_simu.py находится в подкаталоге /path/to/nncase_sdk/examples/scripts, который выглядит следующим образом:

```python
import os
import copy
import argparse
import numpy as np
import onnxruntime as ort
import nncase

def read_model_file(model_file):
    with open(model_file, 'rb') as f:
        model_content = f.read()
    return model_content

def cosine(gt, pred):
    return (gt @ pred) / (np.linalg.norm(gt, 2) * np.linalg.norm(pred, 2))

def main():
    parser = argparse.ArgumentParser(prog="nncase")
    parser.add_argument("--model_file", type=str, help='original model file')
    parser.add_argument("--kmodel_file", type=str, help='kmodel file')
    parser.add_argument("--input_file", type=str, help='input bin file for kmodel')
    args = parser.parse_args()

    # create simulator
    sim = nncase.Simulator()

    # read kmodel
    kmodel = read_model_file(args.kmodel_file)

    # load kmodel
    sim.load_model(kmodel)

    # read input.bin
    input_tensor=sim.get_input_tensor(0).to_numpy()
    input = np.fromfile(args.input_file, input_tensor.dtype).reshape(input_tensor.shape)

    # set input for simulator
    sim.set_input_tensor(0, nncase.RuntimeTensor.from_numpy(input))

    # simulator inference
    nncase_results = []
    sim.run()
    for i in range(sim.outputs_size):
        nncase_result = sim.get_output_tensor(i).to_numpy()
        nncase_results.append(copy.deepcopy(nncase_result))

    # cpu inference
    cpu_results = []
    ort_session = ort.InferenceSession(args.model_file)
    input_name = ort_session.get_inputs()[0].name
    output_name = ort_session.get_outputs()[0].name
    cpu_results = ort_session.run([output_name], { input_name : input })

    # compare
    for i in range(sim.outputs_size):
        cos = cosine(np.reshape(nncase_results[i], (-1)), np.reshape(cpu_results[i], (-1)))
        print('output {0} cosine similarity : {1}'.format(i, cos))

if __name__ == '__main__':
    main()
```

Выполнение скрипта вывода

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_onnx_simu.py --model_file models/mobilenetv2-7.onnx --kmodel_file tmp/mobilenetv2_onnx_fp32_image/test.kmodel --input_file mobilenetv2_onnx_fp32_image/data/input_0_0.bin
```

Сравнение результатов вывода симулятора nncase и ЦП выглядит следующим образом

```shell
... ...
output 0 cosine similarity : 0.9992437958717346
```

# Библиотека среды выполнения 5 nncase

## 5.1 Введение в среду выполнения nncase

nncase runtime используется для загрузки kmodel на устройства AI / установки входных данных / выполнения расчетов KPU / получения выходных данных и т. Д.

В настоящее время **в каталоге nncase sdk/riscv64 доступна только версия API на C++, связанные заголовочные файлы и статические библиотеки**

```bash
$ tree -L 3 riscv64/
riscv64/
├── include
│   ├── gsl
│   │   └── gsl-lite.hpp
│   ├── gsl-lite
│   │   └── gsl-lite.hpp
│   ├── mpark
│   │   ├── config.hpp
│   │   ├── in_place.hpp
│   │   ├── lib.hpp
│   │   └── variant.hpp
│   └── nncase
│       ├── functional
│       ├── kernels
│       ├── runtime
│       └── version.h
└── lib
    ├── cmake
    │   ├── nncasefunctional
    │   ├── nncase_rt_modules_k510
    │   └── nncaseruntime
    ├── libnncase.functional.a
    ├── libnncase.rt_modules.k510.a
    └── libnncase.runtime.a

13 directories, 10 files
```

## 5.2 API среды выполнения

### 5.2.1 runtime_tensor класса

Тензор, используемый для хранения входных/выходных данных модели

#### hrt::create()

**Описание функции**

Создание runtime_tensor

**Определение интерфейса**

```C++
(1) NNCASE_API result<runtime_tensor> create(datatype_t datatype, runtime_shape_t shape, memory_pool_t pool = pool_cpu_only, uintptr_t physical_address = 0) noexcept;

(2) NNCASE_API result<runtime_tensor> create(datatype_t datatype, runtime_shape_t shape, gsl::span<gsl::byte> data, bool copy, memory_pool_t pool = pool_cpu_only, uintptr_t physical_address = 0) noexcept;
```

**Входные параметры**

| Имя параметра         | тип                  | Да или нет | описание                              |
| ---------------- | --------------------- | -------- | --------------------------------- |
| тип данных         | datatype_t            | быть       | Тип данных, например dt_float32            |
| форма            | runtime_shape_t       | быть       | Форма тензора                      |
| данные             | gsl::span\<gsl::byte> | быть       | Буфер данных пользовательского состояния                  |
| копировать             | буль                  | быть       | Стоит ли копировать                          |
| бассейн             | memory_pool_t         | не       | Тип пула памяти, значение по умолчанию pool_cpu_only |
| physical_address | uintptr_t             | не       | Физический адрес, значение по умолчанию — 0               |

**Возвращаемое значение**

результат<runtime_tensor>

Пример кода

```c++
// create input
auto in_shape = interp.input_shape(0);
auto input_tensor = host_runtime_tensor::create(dt_float32, in_shape,
                                                {(gsl::byte *)mat.data, mat.cols * mat.rows * mat.elemSize()},
                                                true, hrt::pool_shared).expect("cannot create input tensor");
```

### 5.2.2 классный переводчик

Интерпретатор является запущенным экземпляром среды выполнения nncase, который предоставляет основные функциональные функции, такие как load_model()/run()/input_tensor()/output_tensor().

#### load_model()

**Описание функции**

Загрузка модели kmodel

**Определение интерфейса**

```C++
 NNCASE_NODISCARD result<void> load_model(gsl::span<const gsl::byte> buffer) noexcept;
```

**Входные параметры**

| Имя параметра | тип                            | Да или нет | описание          |
| -------- | ------------------------------- | -------- | ------------- |
| буфер   | gsl::span `<const gsl::byte>` | быть       | kmodel buffer |

**Возвращаемое значение**

результат `<void>`

**Пример кода**

```c++
template <class T>
std::vector<T>read_binary_file(const char *file_name)
{
  std::ifstream ifs(file_name, std::ios::binary);
  ifs.seekg(0, ifs.end);
  size_t len = ifs.tellg();
  std::vector<T> vec(len / sizeof(T), 0);
  ifs.seekg(0, ifs.beg);
  ifs.read(reinterpret_cast<char*>(vec.data()), len);
  ifs.close();
  return vec;
}

interpreter interp;
auto model = read_binary_file<unsigned char>(kmodel);
interp.load_model({(const gsl::byte *)model.data(), model.size()}).expect("cannot load model.");
```

#### inputs_size()

**Описание функции**

Получает количество входных данных модели.

**Определение интерфейса**

```C++
size_t inputs_size() const noexcept;
```

**Входные параметры**

Н/Д

**Возвращаемое значение**

size_t

**Пример кода**

```c++
auto inputs_size = interp.inputs_size();
```

#### outputs_size()

**Описание функции**

Получает количество выходных данных модели.

**Определение интерфейса**

```C++
size_t outputs_size() const noexcept;
```

**Входные параметры**

Н/Д

**Возвращаемое значение**

size_t

**Пример кода**

```c++
auto outputs_size = interp.outputs_size();
```

#### input_shape()

**Описание функции**

Получает форму заданного входного сигнала модели.

**Определение интерфейса**

```C++
const runtime_shape_t &input_shape(size_t index) const noexcept;
```

**Входные параметры**

| Имя параметра | тип   | Да или нет | описание       |
| -------- | ------ | -------- | ---------- |
| индекс    | size_t | быть       | Индекс входных данных |

**Возвращаемое значение**

runtime_shape_t

**Пример кода**

```c++
auto in_shape = interp.input_shape(0);
```

#### output_shape()

**Описание функции**

Получает форму заданного выходных данных модели.

**Определение интерфейса**

```C++
const runtime_shape_t &output_shape(size_t index) const noexcept;
```

**Входные параметры**

| Имя параметра | тип   | Да или нет | описание       |
| -------- | ------ | -------- | ---------- |
| индекс    | size_t | быть       | Индекс выходных данных |

**Возвращаемое значение**

runtime_shape_t

**Пример кода**

```c++
auto out_shape = interp.output_shape(0);
```

#### input_tensor()

**Описание функции**

Получает/задает входной тензор для указанного индекса

**Определение интерфейса**

```C++
(1) result<runtime_tensor> input_tensor(size_t index) noexcept;
(2) result<void> input_tensor(size_t index, runtime_tensor tensor) noexcept;
```

**Входные параметры**

| Имя параметра | тип           | Да или нет | описание                     |
| -------- | -------------- | -------- | ------------------------ |
| индекс    | size_t         | быть       | kmodel buffer            |
| тензор   | runtime_tensor | быть       | Введите соответствующий тензор среды выполнения |

**Возвращаемое значение**

(1) Возвращает результаты<runtime_tensor>

(2) Возвращает результаты `<void>`

**Пример кода**

```c++
// set input
interp.input_tensor(0, input_tensor).expect("cannot set input tensor");
```

#### output_tensor()

**Описание функции**

Получает/задает исходящий тензор для указанного индекса

**Определение интерфейса**

```C++
(1) result<runtime_tensor> output_tensor(size_t index) noexcept;
(2) result<void> output_tensor(size_t index, runtime_tensor tensor) noexcept;
```

**Входные параметры**

| Имя параметра | тип           | Да или нет | описание                     |
| -------- | -------------- | -------- | ------------------------ |
| индекс    | size_t         | быть       |                          |
| тензор   | runtime_tensor | быть       | Введите соответствующий тензор среды выполнения |

**Возвращаемое значение**

(1) Возвращает результаты<runtime_tensor>

(2) Возвращает результаты `<void>`

**Пример кода**

```c++
// get output
auto output_tensor = interp.output_tensor(0).expect("cannot get output tensor");
auto mapped_buf = std::move(hrt::map(output_tensor, hrt::map_read).unwrap_or_throw());
float *output_data = reinterpret_cast<float *>(mapped_buf.buffer().data());
auto out_shape = interp.output_shape(0);
auto it = std::max_element(output_data, output_data + compute_size(out_shape));
size_t idx = it - output_data;
std::cout << "image classification result: " << labels[idx] << "(" << *it << ")" << std::endl;
```

#### run()

**Описание функции**

Выполнение расчетов kPU

**Определение интерфейса**

```C++
result<void> run() noexcept;
```

**Входные параметры**

Н/Д

**Возвращаемое значение**

результат `<void>`

**Пример кода**

```c++
// run
interp.run().expect("error occurred in running model");
```

## 5.3 Пример среды выполнения

Пример кода находится по адресу /path/to/nncase_sdk/examples/mobilenetv2_onnx_fp32_image

**Условие префикса**

- mobilenetv2_onnx_fp32_image.py скрипт скомпилировал модель mobiletv2-7.onnx
- Поскольку пример основан на библиотеке OpenCV, необходимо указать путь к OpenCV в .txt CMakeLists образца.

**Приложения для перекрестной компиляции**

```shell
cd /path/to/nncase_sdk/examples
./build.sh
```

Наконец, создайте mobilenetv2_onnx_fp32_image в каталоге out/bin

**K510 EVB работает на плате**

Скопируйте следующие файлы на плату k510 EVB

| файл                        | замечание                                                         |
| --------------------------- | ------------------------------------------------------------ |
| mobilenetv2_onnx_fp32_image | Создаются примеры перекрестной компиляции                                         |
| test.kmodel                 | Использование mobilenetv2_onnx_fp32_image.py компиляции сборки mobiletv2-7.onnx |
| Кошачьи .png и labels_1000.txt    | Находится в подкаталоге /path/to/nncase_sdk/examples/mobilenetv2_onnx_fp32_image/data/ |

```bash
$ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mnt/zhangyang/nncase_check/lib/gomp:/mnt/zhangyang/nncase_check/lib/opencv
$ ./mobilenetv2_onnx_fp32_image test.kmodel cat.png labels_1000.txt
case ./mobilenetv2_onnx_fp32_image build at Mar  1 2022 16:31:29
interp.run() duration: 12.6642 ms
image classification result: tiger cat(9.25)
```

# 6 Библиотеки функционального программирования (поддержка среды выполнения)

## 6.1 Введение в функционал

nncase Functional используется для повышения простоты использования при использовании до- и постпроцессных моделей пользователей

В настоящее время доступна только версия API на C++, а связанные с ними заголовочные файлы и библиотеки находятся в каталоге riscv64 пакета SDK nncase.

## 6.2 APIS

### 6.2.1 квадрат

**Описание функции**

Рассчитайте квадрат, в настоящее время поддерживается вход uint8/int8, на выходе также uint8/int8, обратите внимание, что на входе находится фиксированная точка, а на выходе с плавающей запятой необходимо задать параметры квантования.

**Определение интерфейса**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`square`](#ops_8h_1adff2f60c7c045a9840519eab2c04d127)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Входные параметры**

| Имя параметра  | тип           | Да или нет | описание                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | быть       | ввод                |
| `dtype` | datatype_t     | быть       | Выходной тензорный тип данных |

**Возвращаемое значение**

`result<runtime_tensor>`

**Пример кода**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto squared = F::square(input, output_type).unwrap_or_throw();
```

### 6.2.2 м²

**Описание функции**

Вычислите корневое числовое значение, в настоящее время поддерживается вход uint8/int8, вывод также uint8/int8, обратите внимание, что вход является фиксированной точкой, а выход с плавающей запятой должен установить параметры квантования.

**Определение интерфейса**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`sqrt`](#ops_8h_1a53f8dde3dd4e27058b5dc743eb5dd076)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Входные параметры**

| Имя параметра  | тип           | Да или нет | описание                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | быть       | ввод                |
| `dtype` | datatype_t     | быть       | Выходной тензорный тип данных |

**Возвращаемое значение**

`result<runtime_tensor>`

**Пример кода**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::sqrt(input, output_type).unwrap_or_throw();
```

### 6.2.3 Лог

**Описание функции**

Вычислите значение журнала, отрицательное число входных данных будет преобразовано в Nan, в настоящее время поддерживается вход uint8/int8, выход также uint8/int8, обратите внимание, что вход является фиксированной точкой и выход с плавающей запятой необходимо задать параметр квантования.

**Определение интерфейса**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`log`](#ops_8h_1a91df53276c3f1511427d4ac1a0140b71)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Входные параметры**

| Имя параметра  | тип           | Да или нет | описание                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | быть       | ввод                |
| `dtype` | datatype_t     | быть       | Выходной тензорный тип данных |

**Возвращаемое значение**

`result<runtime_tensor>`

**Пример кода**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::log(input, output_type).unwrap_or_throw();
```

### 6.2.4 exp

**Описание функции**

Вычислите значение exp, в настоящее время поддерживается вход uint8/int8, выход также uint8/int8, обратите внимание, что вход является фиксированной точкой, а на выходе с плавающей запятой необходимо задать параметры квантования.

**Определение интерфейса**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`exp`](#ops_8h_1a2c6ce457805a5ba515fa7454fb4aede0)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Входные параметры**

| Имя параметра  | тип           | Да или нет | описание                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | быть       | ввод                |
| `dtype` | datatype_t     | быть       | Выходной тензорный тип данных |

**Возвращаемое значение**

`result<runtime_tensor>`

**Пример кода**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::exp(input, output_type).unwrap_or_throw();
```

### 6.2.5 без

**Описание функции**

Чтобы вычислить значение sin, входной uint8/int8 в настоящее время поддерживается, а выход также uint8/int8, обратите внимание, что параметры квантования должны быть установлены, когда вход является фиксированной точкой, а выход — с плавающей запятой.

**Определение интерфейса**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`sin`](#ops_8h_1a9605b2b0dc9a6892ce878bda14586890)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Входные параметры**

| Имя параметра  | тип           | Да или нет | описание                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | быть       | ввод                |
| `dtype` | datatype_t     | быть       | Выходной тензорный тип данных |

**Возвращаемое значение**

`result<runtime_tensor>`

**Примеры кода**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::sin(input, output_type).unwrap_or_throw();
```

### 6.2.6 кузов

**Описание функции**

Рассчитайте значение cos, в настоящее время поддерживается вход uint8/int8, выход также uint8/int8, обратите внимание, что вход является фиксированной точкой, а выход с плавающей запятой должен установить параметр квантования.

**Определение интерфейса**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`cos`](#ops_8h_1a71d36c13c82f4c411f24d030cf333249)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Входные параметры**

| Имя параметра  | тип           | Да или нет | описание                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | быть       | ввод                |
| `dtype` | datatype_t     | быть       | Выходной тензорный тип данных |

**Возвращаемое значение**

`result<runtime_tensor>`

**Примеры кода**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::cos(input, output_type).unwrap_or_throw();
```

### 6.2.7 раунд

**Описание функции**

Для вычисления круглого значения входной uint8/int8 в настоящее время поддерживается, а выход также uint8/int8, обратите внимание, что параметр квантования необходимо задать, когда вход имеет фиксированную точку, а выход имеет плавающую точку.

**Определение интерфейса**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`round`](#ops_8h_1a81db8ac4866004f75fb65db876262785)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Входные параметры**

| Имя параметра  | тип           | Да или нет | описание                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | быть       | ввод                |
| `dtype` | datatype_t     | быть       | Выходной тензорный тип данных |

**Возвращаемое значение**

`result<runtime_tensor>`

**Примеры кода**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::round(input, output_type).unwrap_or_throw();
```

### 6.2.8 этаж

**Описание функции**

Вычислите значение мороза, в настоящее время поддерживается вход uint8/int8, на выходе также uint8/int8, обратите внимание, что на входе находится фиксированная точка, а на выходе с плавающей запятой необходимо задать параметры квантования.

**Определение интерфейса**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`floor`](#ops_8h_1a1079af8fe9fb6edbb2906d91fac12635)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Входные параметры**

| Имя параметра  | тип           | Да или нет | описание                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | быть       | ввод                |
| `dtype` | datatype_t     | быть       | Выходной тензорный тип данных |

**Возвращаемое значение**

`result<runtime_tensor>`

**Примеры кода**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::floor(input, output_type).unwrap_or_throw();
```

### 6.2.9

**Описание функции**

Вычислите значение ceil, в настоящее время поддерживается вход uint8/int8, выход также uint8/int8, обратите внимание, что вход имеет фиксированную точку и на выходе с плавающей запятой необходимо задать параметры квантования.

**Определение интерфейса**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`ceil`](#ops_8h_1ad3b78c97f1e5348a26de7e5ba2396fb7)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Входные параметры**

| Имя параметра  | тип           | Да или нет | описание                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | быть       | ввод                |
| `dtype` | datatype_t     | быть       | Выходной тензорный тип данных |

**Возвращаемое значение**

`result<runtime_tensor>`

**Примеры кода**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::ceil(input, output_type).unwrap_or_throw();
```

### 6.2.10 абс

**Описание функции**

Вычислите значение abs, в настоящее время поддерживается вход uint8/int8, выход также uint8/int8, обратите внимание, что вход является фиксированной точкой, а выход с плавающей запятой должен задавать параметры квантования.

**Определение интерфейса**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`abs`](#ops_8h_1ad8290dc793bae0dc22b3baf9e0f80c14)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Входные параметры**

| Имя параметра  | тип           | Да или нет | описание                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | быть       | ввод                |
| `dtype` | datatype_t     | быть       | Выходной тензорный тип данных |

**Возвращаемое значение**

`result<runtime_tensor>`

**Примеры кода**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::abs(input, output_type).unwrap_or_throw();
```

### 6.2.11 нег

**Описание функции**

Вычислите значение neg, в настоящее время поддерживается вход uint8/int8, на выходе также uint8/int8, обратите внимание, что вход является фиксированной точкой и на выходе с плавающей запятой необходимо задать параметры квантования.

**Определение интерфейса**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`neg`](#ops_8h_1aa1b7858802e1afce78db72163c5210d8)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Входные параметры**

| Имя параметра  | тип           | Да или нет | описание                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | быть       | ввод                |
| `dtype` | datatype_t     | быть       | Выходной тензорный тип данных |

**Возвращаемое значение**

`result<runtime_tensor>`

**Примеры кода**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::neg(input, output_type).unwrap_or_throw();
```

### 6.2.12 квантование

**Описание функции**

Входные dt_bfloat16, dt_float32 данные, выходные dt_int8 или dt_uint8 выходные данные

**Определение интерфейса**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`quantize`](#ops_8h_1ad8ad779083b5c08da520d2f1c2469c3a)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Входные параметры**

| Имя параметра  | тип           | Да или нет | описание                                |
| --------- | -------------- | -------- | ----------------------------------- |
| `input` | runtime_tensor | быть       | Вход, тип должен быть float32 или bfloat16 |
| `dtype` | datatype_t     | быть       | Выходной тензорный тип данных                 |

**Возвращаемое значение**

`result<runtime_tensor>`

**Примеры кода**

```cpp
auto quantized = F::quantize(input, dt_int8).unwrap_or_throw();
```

### 6.2.13 деквантизация

**Описание функции**

Введите входные данные uint8 или int8, преобразуйте их в данные с плавающей точкой или bfloat. Обратите внимание, что пользователь должен заранее задать правильные параметры квантования для данных для деквантизации.

**Определение интерфейса**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`dequantize`](#ops_8h_1ab91a262349baf393c91abad6f393de24)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**Входные параметры**

| Имя параметра  | тип           | Да или нет | описание                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | быть       | ввод                |
| `dtype` | datatype_t     | быть       | Выходной тензорный тип данных |

**Возвращаемое значение**

`result<runtime_tensor>`

**Примеры кода**

```cpp
input.quant_param({ 0, 1 });
auto dequantized = F::dequantize(input, output_type).unwrap_or_throw();
```

### 6.2.14 Урожай

**Описание функции**

Заданные b box, обрезанные из исходного тензора и изменяющие размер выходных данных в новый тензор. Принимайте dt_bfloat16, dt_float32, dt_int8, dt_uint8 тип вывода, выходные данные того же типа.

**Определение интерфейса**

`NNCASE_API inline result<runtime::runtime_tensor> crop(runtime::runtime_tensor &input, runtime::runtime_tensor &bbox, size_t out_h, size_t out_w, image_resize_mode_t resize_mode, bool align_corners, bool half_pixel_centers) noexcept`

**Входные параметры**

| Имя параметра           | тип                | Да или нет | описание                                                                                     |
| ------------------ | ------------------- | -------- | ---------------------------------------------------------------------------------------- |
| ввод              | runtime_tensor      | быть       | Введите данные, нужно [н,с,в,з,ш] отформатировать макет, если данные uint8 или int8, пожалуйста, убедитесь в правильности параметров квантования данных       |
| bbox               | runtime_tensor      | быть       | Введите данные bbox, нужно [1,1,м,4] отформатировать макет, внутренние данные есть[y0,x0,y1,x1], тип[float32,bfloat16] |
| out_h              | size_t              | быть       | Высота выходных данных                                                                           |
| out_w              | size_t              | быть       | Введите ширину данных                                                                            |
| resize_mode        | image_resize_mode_t | быть       | Шаблон метода изменения размера                                                                           |
| align_corners      | буль                | быть       | Изменение размера align_corners                                                    |
| half_pixel_centers | буль                | быть       | Изменение размера, если пиксель выровнен по центру                                                                  |

**Возвращаемое значение**

`result<runtime_tensor>`

**Примеры кода**

```cpp
auto bbox = get_rand_bbox(input_shape, roi_amount);
auto &&[out_h, out_w] = get_rand_out_hw();
auto output_opt = F::crop(input, bbox, out_h, out_w, resize_mode).unwrap_or_throw();
```

### 6.2.15 Изменение размера

**Описание функции**

Учитывая ширину выходной высоты, измените размер входного тензора на новый размер. Принимайте dt_bfloat16, dt_float32, dt_int8, dt_uint8 тип вывода, выходные данные того же типа.

**Определение интерфейса**

`NNCASE_API inline result<runtime::runtime_tensor> resize(runtime::runtime_tensor &input, size_t out_h, size_t out_w, image_resize_mode_t resize_mode, bool align_corners, bool half_pixel_centers) noexcept`

**Входные параметры**

| Имя параметра           | тип                | Да или нет | описание                                                                               |
| ------------------ | ------------------- | -------- | ---------------------------------------------------------------------------------- |
| ввод              | runtime_tensor      | быть       | Введите данные, которые должны быть [н,с,в,з,ш] отформатированы, если данные uint8 или int8, пожалуйста, убедитесь в правильности параметров квантования данных |
| out_h              | size_t              | быть       | Высота выходных данных                                                                     |
| out_w              | size_t              | быть       | Введите ширину данных                                                                      |
| resize_mode        | image_resize_mode_t | быть       | Шаблон метода изменения размера                                                                     |
| align_corners      | буль                | быть       | Изменение размера align_corners                                              |
| half_pixel_centers | буль                | быть       | Изменение размера, если пиксель выровнен по центру                                                            |

**Возвращаемое значение**

`result<runtime_tensor>`

**Примеры кода**

```cpp
auto &&[out_h, out_w] = get_rand_out_hw();
auto output_opt = F::resize(input, out_h, out_w, resize_mode, false, false).unwrap_or_throw();
```

### 6.2.16 колодка

**Описание функции**

Заполнение данных для каждого измерения принимает dt_bfloat16, dt_float32, dt_int8, dt_uint8 тип вывода и вывода одного и того же типа.

**Определение интерфейса**

`NNCASE_API inline result<runtime::runtime_tensor> pad(runtime::runtime_tensor &input, runtime_paddings_t &paddings, pad_mode_t pad_mode, float fill_v)`

**Входные параметры**

| Имя параметра | тип               | Да или нет | описание                                                                                                                                       |
| -------- | ------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| ввод    | runtime_tensor     | быть       | Введите данные, если данные uint8 или int8 Убедитесь в правильности параметров квантования данных                                                                                  |
| набивочный материал  | runtime_paddings_t | быть       | Например, значение заполнения указывается `[ {2,3}, {1,3} ]`перед блокпостом 2 в последнем измерении, за которым следует блок 3. Предпоследнему размеру предшествует блок 1, за которым следует блок 2 |
| pad_mode | pad_mode_t         | быть       | В настоящее время поддерживается только режим const                                                                                                                   |
| fill_v   | плавать              | быть       | Заполнение значений                                                                                                                                     |

**Возвращаемое значение**

`result<runtime_tensor>`

**Примеры кода**

```cpp
runtime_paddings_t paddings{ { 0, 0 }, { 0, 0 }, { 0, 0 }, { 1, 2 } };
auto output = F::pad(input, paddings, pad_constant, pad_value).unwrap_or_throw();
```
<!-- markdownlint-enable no-emphasis-as-header -->
# 7 Количественная белая книга

## 7.1 Информационный документ по количественной оценке модели классификации

| Классификационная модель     | Точность процессора (Топ-1) | Точность с плавающей запятой (Топ-1) | Точность uint8 (Топ-1) | int8 Точность (Топ-1) |
| ------------ | -------------- | --------------- | ---------------- | --------------- |
| алекснет      | 0.531          | 0.53            | Н/Д              | 0.52            |
| плотная сеть 121 | 0.732          | 0.732           | 0.723            | Н/Д             |
| начало v3 | 0.766          | 0.765           | 0.773            | 0.77            |
| начало v4 | 0.789          | 0.789           | 0.793            | 0.792           |
| mobilenet v1 | 0.731          | 0.73            | 0.723            | 0.718           |
| mobilenet v2 | 0.713          | 0.715           | 0.713            | 0.719           |
| resnet50 v2  | 0.747          | 0.74            | 0.748            | 0.749           |
| VGG 16       | 0.689          | 0.687           | 0.690            | 0.689           |

> Эта таблица в основном предназначена для сравнения производительности квантования, точность ЦП представляет собой полные данные набора проверок ImageNet, а точность с плавающей запятой и квантованием является результатом теста подмножества данных для первого изображения 1000 классов в наборе проверки в соответствии с порядковым числом.
>
> Результаты тестов Alexnet и SenseNet являются старыми данными, оба из которых являются результатами тестирования первых 1000 изображений проверочного набора в качестве подмножества данных, а N/A заключается в том, что подмножество тестовых данных в это время отличается от cpu, поэтому оно не используется в качестве сравнения.
>
> Поскольку выбранная сеть не обязательно исходит от официальной или существуют различия в предварительной обработке и т. Д., Она может отличаться от официальной производительности.

## 7.2 Информационный документ по количественной оценке модели обнаружения

1. ЙОЛОВ3

    | КОКОАПИ                                                      | Официальные результаты | Точность процессора с плавающей запятой | Точность с плавающей запятой gnne | Точность uint8 | точность int8 |
    | ------------------------------------------------------------ | -------- | ----------- | ------------ | --------- | -------- |
    | Средняя точность (AP) @ [IoU = 0,50:0,95\| площадь = все \| maxDets = 100] | 0.314    | 0.307       | 0.306        | 0.295     | 0.288    |
    | Средняя точность (AP) @ [IoU = 0,50\| площадь = все \| maxDets = 100] | 0.559    | 0.555       | 0.554        | 0.555     | 0.554    |
    | Средняя точность (AP) @ [IoU = 0,75\| площадь = все \| maxDets = 100] | 0.318    | 0.308       | 0.307        | 0.287     | 0.275    |
    | Средняя точность (AP) @ [IoU = 0,50:0,95\| площадь = маленькая \| maxDets = 100] | 0.142    | 0.150       | 0.149        | 0.147     | 0.144    |
    | Средняя точность (AP) @ [IoU= 0.50:0.95\| площадь = средняя \| maxDets = 100] | 0.341    | 0.332       | 0.332        | 0.322     | 0.316    |
    | Средняя точность (AP) @ [IoU = 0,50:0,95\| площадь = большая \| maxDets = 100] | 0.464    | 0.437       | 0.437        | 0.414     | 0.404    |
    | Средний отзыв (AR) @ [IoU= 0.50:0.95\| площадь = все \| максСеты = 1] | 0.278    | 0.270       | 0.271        | 0.262     | 0.256    |
    | Средний отзыв (AR) @ [IoU= 0.50:0.95\| площадь = все \| maxDets = 10] | 0.419    | 0.412       | 0.412        | 0.399     | 0.392    |
    | Средний отзыв (AR) @ [IoU = 0,50:0,95\| площадь = все \| maxDets = 100] | 0.442    | 0.433       | 0.433        | 0.421     | 0.414    |
    | Средний отзыв (AR) @ [IoU = 0,50:0,95\| площадь = маленькая \| maxDets = 100] | 0.239    | 0.251       | 0.251        | 0.248     | 0.246    |
    | Средний отзыв (AR) @ [IoU= 0.50:0.95\| площадь = средняя \| maxDets = 100] | 0.482    | 0.462       | 0.463        | 0.451     | 0.443    |
    | Средний отзыв (AR) @ [IoU = 0,50:0,95\| площадь = большая \| maxDets = 100] | 0.611    | 0.586       | 0.585        | 0.559     | 0.550    |

2. ssd-mobilenetv1

    | КОКОАПИ                                                                    | Официальные результаты | Точность процессора с плавающей запятой | Точность с плавающей запятой gnne | Точность uint8 | точность int8 |
    | -------------------------------------------------------------------------- | -------- | ----------- | ------------ | --------- | -------- |
    | Средняя точность (AP) @ [IoU = 0,50:0,95\| площадь = все \| maxDets = 100]   | 0.184    | 0.184       | 0.184        | 0.183     | 0.183    |
    | Средняя точность (AP) @ [IoU = 0,50\| площадь = все \| maxDets = 100]        | 0.306    | 0.307       | 0.306        | 0.305     | 0.306    |
    | Средняя точность (AP) @ [IoU = 0,75\| площадь = все \| maxDets = 100]        | 0.191    | 0.192       | 0.190        | 0.189     | 0.190    |
    | Средняя точность (AP) @ [IoU = 0,50:0,95\| площадь = маленькая \| maxDets = 100] | 0.017    | 0.017       | 0.017        | 0.017     | 0.017    |
    | Средняя точность (AP) @ [IoU= 0.50:0.95\| площадь = средняя \| maxDets = 100] | 0.157    | 0.157       | 0.157        | 0.156     | 0.155    |
    | Средняя точность (AP) @ [IoU = 0,50:0,95\| площадь = большая \| maxDets = 100] | 0.371    | 0.372       | 0.371        | 0.370     | 0.369    |
    | Средний отзыв (AR) @ [IoU= 0.50:0.95\| площадь = все \| максСеты = 1]         | 0.180    | 0.180       | 0.180        | 0.181     | 0.181    |
    | Средний отзыв (AR) @ [IoU= 0.50:0.95\| площадь = все \| maxDets = 10]        | 0.242    | 0.242       | 0.242        | 0.243     | 0.243    |
    | Средний отзыв (AR) @ [IoU = 0,50:0,95\| площадь = все \| maxDets = 100]      | 0.242    | 0.242       | 0.242        | 0.243     | 0.243    |
    | Средний отзыв (AR) @ [IoU = 0,50:0,95\| площадь = маленькая \| maxDets = 100]    | 0.026    | 0.026       | 0.026        | 0.026     | 0.026    |
    | Средний отзыв (AR) @ [IoU= 0.50:0.95\| площадь = средняя \| maxDets = 100]    | 0.206    | 0.206       | 0.206        | 0.206     | 0.205    |
    | Средний отзыв (AR) @ [IoU = 0,50:0,95\| площадь = большая \| maxDets = 100]    | 0.489    | 0.491       | 0.490        | 0.490     | 0.491    |

3. ЙОЛОВ5С

    | КОКОАПИ                                                                    | Официальные результаты | Точность процессора с плавающей запятой | Точность с плавающей запятой gnne | Точность uint8 | точность int8 |
    | -------------------------------------------------------------------------- | -------- | ----------- | ------------ | --------- | -------- |
    | Средняя точность (AP) @ [IoU = 0,50:0,95\| площадь = все \| maxDets = 100]   | 0.367    | 0.365       | 0.335        | 0.334     | 0.335    |
    | Средняя точность (AP) @ [IoU = 0,50\| площадь = все \| maxDets = 100]        | 0.555    | 0.552       | 0.518        | 0.518     | 0.518    |
    | Средняя точность (AP) @ [IoU = 0,75\| площадь = все \| maxDets = 100]        | 0.398    | 0.395       | 0.364        | 0.363     | 0.362    |
    | Средняя точность (AP) @ [IoU = 0,50:0,95\| площадь = маленькая \| maxDets = 100] | 0.223    | 0.220       | 0.199        | 0.199     | 0.197    |
    | Средняя точность (AP) @ [IoU= 0.50:0.95\| площадь = средняя \| maxDets = 100] | 0.419    | 0.418       | 0.387        | 0.386     | 0.386    |
    | Средняя точность (AP) @ [IoU = 0,50:0,95\| площадь = большая \| maxDets = 100] | 0.463    | 0.459       | 0.423        | 0.422     | 0.423    |
    | Средний отзыв (AR) @ [IoU= 0.50:0.95\| площадь = все \| максСеты = 1]         | 0.306    | 0.306       | 0.288        | 0.287     | 0.287    |
    | Средний отзыв (AR) @ [IoU= 0.50:0.95\| площадь = все \| maxDets = 10]        | 0.518    | 0.518       | 0.487        | 0.486     | 0.487    |
    | Средний отзыв (AR) @ [IoU = 0,50:0,95\| площадь = все \| maxDets = 100]      | 0.576    | 0.576       | 0.540        | 0.539     | 0.540    |
    | Средний отзыв (AR) @ [IoU = 0,50:0,95\| площадь = маленькая \| maxDets = 100]    | 0.391    | 0.399       | 0.350        | 0.350     | 0.347    |
    | Средний отзыв (AR) @ [IoU= 0.50:0.95\| площадь = средняя \| maxDets = 100]    | 0.641    | 0.640       | 0.606        | 0.605     | 0.607    |
    | Средний отзыв (AR) @ [IoU = 0,50:0,95\| площадь = большая \| maxDets = 100]    | 0.716    | 0.710       | 0.680        | 0.683     | 0.685    |

# 8 Часто задаваемые вопросы

1. 安装wheel时报错: «xxx.whl не является поддерживаемым колесом на этой платформе». **

    Q: 安装nncase wheel包, 出现ERROR: nncase-1.0.0.20210830-cp37-cp37m-manylinux_2_24_x86_64.whl не является поддерживаемым колесом на этой платформе.

    A: > пункта обновления = 20.3

    ```shell
    sudo pip3 install --upgrade pip
    ```

2. **Когда CRB запускает программу App inference, он сообщает об ошибке "std::bad_alloc"**

    Вопрос: Запустите программу вывода приложений в CRB и создайте исключение "std::bad_alloc"

    ```shell
    $ ./cpp.sh
    case ./yolov3_bfloat16 build at Sep 16 2021 18:12:03
    terminate called after throwing an instance of 'std::bad_alloc'
    what():  std::bad_alloc
    ```

    A: исключения std::bad_alloc обычно вызваны сбоями выделения памяти, которые можно проверить следующим образом.

    - Проверьте, превышает ли сгенерированный kmodel текущую доступную систему памяти (например, yolov3 bfloat16 kmodel размер составляет 121 МБ, текущая доступная память Linux составляет всего 70 МБ, исключение будет выброшено).  Если он превышает, попробуйте использовать посттренировочное квантование, чтобы уменьшить размер кмоделя.
    - Проверьте приложение на наличие утечек памяти

3. **При запуске программы App inference[.. t_runtime_tensor.cpp:310 (создать)] data.size_bytes() == size = false (bool).**

    Вопрос: Симулятор запускает программу вывода приложений, выдавая исключение "[.. t_runtime_tensor.cpp:310 (создать)] data.size_bytes() == size = false (bool)"

    A: Проверьте входную тензорную информацию для настроек, сосредоточив внимание на входной форме и количестве байтов, занятых каждым элементом (fp32/uint8)

**Отказ от ответственности за**перевод  
Для удобства клиентов Canaan использует переводчик AI для перевода текста на несколько языков, которые могут содержать ошибки. Мы не гарантируем точность, надежность или своевременность предоставленных переводов. Компания Canaan не несет ответственности за любые убытки или ущерб, вызванные доверием к точности или надежности переведенной информации. При наличии разницы в содержании переводов на разные языки преимущественную силу имеет упрощенная версия на китайском языке.

Если вы хотите сообщить об ошибке или неточности перевода, пожалуйста, не стесняйтесь обращаться к нам по почте.
