![](../zh/images/canaan-cover.png)

**<font face="黑体" size="6" style="float:right">K510 V4L2 Sensor Developer's Guide</font>**

<font face="黑体"  size=3>Document version: V1.0.0</font>

<font face="黑体"  size=3>Published: 2022-03-11</font>

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
This document is an explanatory document developed for the K510 sensor. 

**<font face="黑体"  size=5>Reader Objects</font>**

The main people to whom this document (this guide) applies:

- Software developers
- Technical support personnel

**<font face="黑体"  size=5>Revision history</font>**
 <font face="宋体"  size=2>The revision history accumulates a description of each document update. The latest version of the document contains updates for all previous versions. </font>

| The version number | Modified by | Date of revision   | Revision Notes     |
| :----- | ------ | ---------- | ------------ |
| V1.0.0 | Zhu Dalei | 2022-03-11 | SDK V1.5 released |
|        |        |            |              |
|        |        |            |              |
|        |        |            |              |
|        |        |            |              |
|        |        |            |              |
|        |        |            |              |
|        |        |            |              |
|        |        |            |              |

<div style="page-break-after:always"></div>

**<font face="黑体"  size=6>Contents</font>**

[TOC]

<div style="page-break-after:always"></div>

# 1. V4L2 sesor driver

Taking imx219 as an example, the code is in drivers/media/i2c/soc_camera/canaanchip/imx219_0.c  

## 1.1 Add sensor configuration

- Add the following set of configurations

    ```c
    /* MCLK:24MHz  1080x1920  30fps   MIPI LANE2 */
    static const struct imx219_reg imx219_init_tab_1080_1920_30fps[] = {
        //Access command sequence
        {0x30eb, 0x05},
        {0x30eb, 0x0c},
        {0x300a, 0xff},
        {0x300b, 0xff},
        {0x30eb, 0x05},
        {0x30eb, 0x09},

        {0x0114, 0x01}, //REG_CSI_LANE 01 -2lanes 03-4lanes
        {0x0128, 0x00}, //REG_DPHY_CTRL
        {0x012a, 0x18}, //REG_EXCK_FREQ_MSB
        {0x012b, 0x00}, //REG_EXCK_FREQ_LSB

        {0x0160, 0x08}, //FRM_LENGTH_A[15:8]
        {0x0161, 0x98}, //FRM_LENGTH_A[7:0]
        {0x0162, 0x0d}, //LINE_LENGTH_A[15:8]
        {0x0163, 0x94}, //LINE_LENGTH_A[7:0]

        {0x0164, 0x02}, //X_ADD_STA_A[11:8]
        {0x0165, 0xb4}, //X_ADD_STA_A[7:0]
        {0x0166, 0x06}, //X_ADD_END_A[11:8]
        {0x0167, 0xeb}, //X_ADD_END_A[7:0]

        {0x0168, 0x01}, //Y_ADD_STA_A[11:8]
        {0x0169, 0x00}, //Y_ADD_STA_A[7:0]
        {0x016a, 0x08}, //Y_ADD_END_A[11:8]
        {0x016b, 0x7f}, //Y_ADD_END_A[7:0]

        {0x016c, 0x04}, //x_output_size[11:8]
        {0x016d, 0x38}, //x_output_size[7:0]
        {0x016e, 0x07}, //y_output_size[11:8]
        {0x016f, 0x80}, // y_output_size[7:0]

        {0x0170, 0x01}, //X_ODD_INC_A
        {0x0171, 0x01}, //Y_ODD_INC_A

        {0x0172, 0x00}, //IMG_ORIENTATION_A
        //BINNING
        {0x0174, 0x00}, //BINNING_MODE_H_A
        {0x0175, 0x00}, //BINNING_MODE_V_A

        {0x0301, 0x05}, //VTPXCK_DIV
        {0x0303, 0x01}, //VTSYCK_DIV

        {0x0304, 0x03}, //PREPLLCK_VT_DIV
        {0x0305, 0x03}, //PREPLLCK_OP_DIV

        {0x0306, 0x00}, //PLL_VT_MPY[10:8]
        {0x0307, 0x48}, //PLL_VT_MPY[7:0]

        {0x030b, 0x01}, //OPSYCK_DIV

        {0x030c, 0x00}, //PLL_OP_MPY[10:8]
        {0x030d, 0x40}, //PLL_OP_MPY[7:0]

        {0x0624, 0x07},
        {0x0625, 0x80},
        {0x0626, 0x04},
        {0x0627, 0x38},
        {0x455e, 0x00},
        {0x471e, 0x4b},
        {0x4767, 0x0f},
        {0x4750, 0x14},
        {0x4540, 0x00},
        {0x47b4, 0x14},
        {0x4713, 0x30},
        {0x478b, 0x10},
        {0x478f, 0x10},
        {0x4793, 0x10},
        {0x4797, 0x0e},
        {0x479b, 0x0e},
        {0x0157, 0x40},
        {IMX219_TABLE_END, 0x00}
    };
    ```

- Add the configuration to the modes sequence as follows:

    ```c
    static const struct imx219_mode supported_modes[] = {
        {
            .width = 1920,
            .height = 1080,
            .max_fps = {
                .numerator = 10000,
                .denominator = 300000,
            },
            .hts_def = 0x0d94 - IMX219_EXP_LINES_MARGIN,
            .vts_def = 0x048e,
            .reg_list = imx219_init_tab_1920_1080_30fps,
        },
        {
            .width = 1080,
            .height = 1920,
            .max_fps = {
                .numerator = 10000,
                .denominator = 300000,
            },
            .hts_def = 0x0d78 - IMX219_EXP_LINES_MARGIN,
            .vts_def = 0x0898,
            .reg_list = imx219_init_tab_1080_1920_30fps,
        },
    };
    ```

    Illustrate:
    .width = 1080 is the sensor output level effective pixel.
    .height = 1920 is the number of highly valid rows for the sensor output.
    .hts_def = 0x0d78 - IMX219_EXP_LINES_MARGIN is the sensor output level total pixels minus the exposure line threshold. 0x0d78 is the sensor output level total pixels, which will be used in the vidieo.conf file. IMX219_EXP_LINES_MARGIN is to define the exposure row threshold, which is currently 4 and can be changed.
    .vts_def = 0x0898 is the total number of lines of sensor output height, which is used in the vidieo.conf file.
    .reg_list = imx219_init_tab_1080_1920_30fps is the configuration changed above.

- Add the model of stream on, which will be used imx219_s_stream

    ```c
    static const struct imx219_reg start[] = {
        {0x0100, 0x01},   /* mode select streaming on */
        {IMX219_TABLE_END, 0x00}
    };
    ```

- Add the stream off mode, which will be used imx219_s_stream

    ```c
    static const struct imx219_reg stop[] = {
        {0x0100, 0x00}, /* mode select streaming off */
        {IMX219_TABLE_END, 0x00}
    };
    ```

## 1.2 Increase the exposure gain and control of the exposure line

Add or modify
​case V4L2_CID_ANALOGUE_GAIN:
​case V4L2_CID_GAIN:
​case V4L2_CID_EXPOSURE:

```c
static int imx219_s_ctrl(struct v4l2_ctrl *ctrl)
{
    struct imx219 *priv =
        container_of(ctrl->handler, struct imx219, ctrl_handler);
    struct i2c_client *client = v4l2_get_subdevdata(&priv->subdev);
    u8 reg;
    int ret;
    u16 gain = 256;
    u16 a_gain = 256;
    u16 d_gain = 1;

    dev_dbg(&client->dev,"%s:ctrl->id(0x%x),ctrl->val(%d)\n",__func__,ctrl->id,ctrl->val);

    switch (ctrl->id) {
    case V4L2_CID_HFLIP:
        priv->hflip = ctrl->val;
        break;

    case V4L2_CID_VFLIP:
        priv->vflip = ctrl->val;
        break;

    case V4L2_CID_ANALOGUE_GAIN:
    case V4L2_CID_GAIN:
        /*
        * hal transfer (gain * 256)  to kernel
        * than divide into analog gain & digital gain in kernel
        */

        gain = ctrl->val;
        if (gain < 256)
            gain = 256;
        if (gain > 43663)
            gain = 43663;
        if (gain >= 256 && gain <= 2728) {
            a_gain = gain;
            d_gain = 1 * 256;
        } else {
            a_gain = 2728;
            d_gain = (gain * 256) / a_gain;
        }

        /*
        * Analog gain, reg range[0, 232], gain value[1, 10.66]
        * reg = 256 - 256 / again
        * a_gain here is 256 multify
        * so the reg = 256 - 256 * 256 / a_gain
        */
        priv->analogue_gain = (256 - (256 * 256) / a_gain);
        if (a_gain < 256)
            priv->analogue_gain = 0;
        if (priv->analogue_gain > 232)
            priv->analogue_gain = 232;

        /*
        * Digital gain, reg range[256, 4095], gain rage[1, 16]
        * reg = dgain * 256
        */
        priv->digital_gain = d_gain;
        if (priv->digital_gain < 256)
            priv->digital_gain = 256;
        if (priv->digital_gain > 4095)
            priv->digital_gain = 4095;

        /*
        * for bank A and bank B switch
        * exposure time , gain, vts must change at the same time
        * so the exposure & gain can reflect at the same frame
        */

        ret = reg_write(client, 0x0157, priv->analogue_gain);
        ret |= reg_write(client, 0x0158, priv->digital_gain >> 8);
        ret |= reg_write(client, 0x0159, priv->digital_gain & 0xff);

        return ret;

    case V4L2_CID_EXPOSURE:
        priv->exposure_time = ctrl->val;

        ret = reg_write(client, 0x015a, priv->exposure_time >> 8);
        ret |= reg_write(client, 0x015b, priv->exposure_time & 0xff);
        return ret;

    case V4L2_CID_TEST_PATTERN:
        return imx219_s_ctrl_test_pattern(ctrl);

    case V4L2_CID_VBLANK:
        if (ctrl->val < priv->cur_mode->vts_def)
            ctrl->val = priv->cur_mode->vts_def;
        if ((ctrl->val - IMX219_EXP_LINES_MARGIN) != priv->cur_vts)
            priv->cur_vts = ctrl->val - IMX219_EXP_LINES_MARGIN;
        ret = reg_write(client, 0x0160, ((priv->cur_vts >> 8) & 0xff));
        ret |= reg_write(client, 0x0161, (priv->cur_vts & 0xff));
        return ret;

    default:
        return -EINVAL;
    }
    /* If enabled, apply settings immediately */
    reg = reg_read(client, 0x0100);
    if ((reg & 0x1f) == 0x01)
        imx219_s_stream(&priv->subdev, 1);

    return 0;
}
```

## 1.3 Modify the initialization configuration in the probe function (to imx_probe)

### 1.3.1 Modify the version number

```c
dev_info(dev, "driver version: %02x.%02x.%02x",
    (uint8_t)(DRIVER_VERSION >> 16),
    (uint8_t)(DRIVER_VERSION >> 8),
    (uint8_t)(DRIVER_VERSION));
```

### 1.3.2 Add and modify canaan information parsing in DTS

```c
    ret = of_property_read_u32(node, CANAANMODULE_CAMERA_MODULE_INDEX,
            &priv->module_index);

    ret |= of_property_read_string(node, CANAANMODULE_CAMERA_MODULE_FACING,
            &priv->module_facing);

    ret |= of_property_read_string(node, CANAANMODULE_CAMERA_MODULE_NAME,
            &priv->module_name);

    ret |= of_property_read_string(node, CANAANMODULE_CAMERA_LENS_NAME,
            &priv->len_name);
```

### 1.3.3 Modify crop information for currently supported modes

This is consistent with the configuration information above.

```c
priv->crop_rect.left = 680; //0x2A8
priv->crop_rect.top = 692; //0x2b4;
priv->crop_rect.width = priv->cur_mode->width;
priv->crop_rect.height = priv->cur_mode->height;
```

### 1.3.4 Modify the sensor name and other information

This sensor name will be used in video_cfg.conf file, mediactl_lib library needs it to find the sensor.

```c
memset(facing, 0, sizeof(facing));
if (strcmp(priv->module_facing, "back") == 0)
    facing[0] = 'b';
else
    facing[0] = 'f';

snprintf(sd->name, sizeof(sd->name), "m%02d_%s_%s %s",
        priv->module_index, facing,
        IMX219_NAME, dev_name(sd->dev));
```

## 1.4 Add or modify the sensor version of the read function (imx219_video_probe)

```c
static int imx219_video_probe(struct i2c_client *client)
{
    struct v4l2_subdev *subdev = i2c_get_clientdata(client);
    u16 model_id;
    u32 lot_id;
    u16 chip_id;
    int ret;

    ret = imx219_s_power(subdev, 1);
    if (ret < 0)
        return ret;

    /* Check and show model, lot, and chip ID. */
    ret = reg_read(client, 0x0000);
    if (ret < 0) {
        dev_err(&client->dev, "Failure to read Model ID (high byte)\n");
        goto done;
    }
    model_id = ret << 8;

    ret = reg_read(client, 0x0001);
    if (ret < 0) {
        dev_err(&client->dev, "Failure to read Model ID (low byte)\n");
        goto done;
    }
    model_id |= ret;

    ret = reg_read(client, 0x0004);
    if (ret < 0) {
        dev_err(&client->dev, "Failure to read Lot ID (high byte)\n");
        goto done;
    }
    lot_id = ret << 16;

    ret = reg_read(client, 0x0005);
    if (ret < 0) {
        dev_err(&client->dev, "Failure to read Lot ID (mid byte)\n");
        goto done;
    }
    lot_id |= ret << 8;

    ret = reg_read(client, 0x0006);
    if (ret < 0) {
        dev_err(&client->dev, "Failure to read Lot ID (low byte)\n");
        goto done;
    }
    lot_id |= ret;

    ret = reg_read(client, 0x000D);
    if (ret < 0) {
        dev_err(&client->dev, "Failure to read Chip ID (high byte)\n");
        goto done;
    }
    chip_id = ret << 8;

    ret = reg_read(client, 0x000E);
    if (ret < 0) {
        dev_err(&client->dev, "Failure to read Chip ID (low byte)\n");
        goto done;
    }
    chip_id |= ret;

    if (model_id != 0x0219) {
        dev_err(&client->dev, "Model ID: %x not supported!\n",
            model_id);
        ret = -ENODEV;
        goto done;
    }
    dev_info(&client->dev,
        "Model ID 0x%04x, Lot ID 0x%06x, Chip ID 0x%04x\n",
        model_id, lot_id, chip_id);
done:
    imx219_s_power(subdev, 0);
    return ret;
}
```

## 1.5 Modify the sensor's control function

Mainly the default exposure value and the initial value of the exposure line are modified (IMX219_ANALOGUE_GAIN_MIN/IMX219_DIGITAL_GAIN_MAX/IMX219_ANALOGUE_GAIN_DEFAULT, IMX219_DIGITAL_EXPOSURE_MIN/IMX219_DIGITAL_EXPOSURE_MAX/IMX219_ DIGITAL_EXPOSURE_DEFAULT）

```c
static int imx219_ctrls_init(struct v4l2_subdev *sd)
{
    struct i2c_client *client = v4l2_get_subdevdata(sd);
    struct imx219 *priv = to_imx219(client);
    const struct imx219_mode *mode = priv->cur_mode;
    s64 pixel_rate, h_blank, v_blank;
    int ret;
    u32 fps = 0;

    v4l2_ctrl_handler_init(&priv->ctrl_handler, 10);
    v4l2_ctrl_new_std(&priv->ctrl_handler, &imx219_ctrl_ops,
                V4L2_CID_HFLIP, 0, 1, 1, 0);
    v4l2_ctrl_new_std(&priv->ctrl_handler, &imx219_ctrl_ops,
                V4L2_CID_VFLIP, 0, 1, 1, 0);

    /* exposure */
    v4l2_ctrl_new_std(&priv->ctrl_handler, &imx219_ctrl_ops,
                V4L2_CID_ANALOGUE_GAIN,
                IMX219_ANALOGUE_GAIN_MIN,
                IMX219_ANALOGUE_GAIN_MAX,
                1, IMX219_ANALOGUE_GAIN_DEFAULT);
    v4l2_ctrl_new_std(&priv->ctrl_handler, &imx219_ctrl_ops,
                V4L2_CID_GAIN,
                IMX219_DIGITAL_GAIN_MIN,
                IMX219_DIGITAL_GAIN_MAX, 1,
                IMX219_DIGITAL_GAIN_DEFAULT);
    v4l2_ctrl_new_std(&priv->ctrl_handler, &imx219_ctrl_ops,
                V4L2_CID_EXPOSURE,
                IMX219_DIGITAL_EXPOSURE_MIN,
                IMX219_DIGITAL_EXPOSURE_MAX, 1,
                IMX219_DIGITAL_EXPOSURE_DEFAULT);

    /* blank */
    h_blank = mode->hts_def - mode->width;
    priv->hblank = v4l2_ctrl_new_std(&priv->ctrl_handler, NULL, V4L2_CID_HBLANK,
                h_blank, h_blank, 1, h_blank);
    v_blank = mode->vts_def - mode->height;
    priv->vblank = v4l2_ctrl_new_std(&priv->ctrl_handler, NULL, V4L2_CID_VBLANK,
                v_blank, v_blank, 1, v_blank);

    /* freq */
    v4l2_ctrl_new_int_menu(&priv->ctrl_handler, NULL, V4L2_CID_LINK_FREQ,
                    0, 0, link_freq_menu_items);
    fps = DIV_ROUND_CLOSEST(mode->max_fps.denominator,
        mode->max_fps.numerator);
    pixel_rate = mode->vts_def * mode->hts_def * fps;
    priv->pixel_rate = v4l2_ctrl_new_std(&priv->ctrl_handler, NULL, V4L2_CID_PIXEL_RATE,
                0, pixel_rate, 1, pixel_rate);

    v4l2_ctrl_new_std_menu_items(&priv->ctrl_handler, &imx219_ctrl_ops,
                        V4L2_CID_TEST_PATTERN,
                        ARRAY_SIZE(tp_qmenu) - 1, 0, 0, tp_qmenu);

    priv->subdev.ctrl_handler = &priv->ctrl_handler;
    if (priv->ctrl_handler.error) {
        dev_err(&client->dev, "Error %d adding controls\n",
            priv->ctrl_handler.error);
        ret = priv->ctrl_handler.error;
        goto error;
    }

    ret = v4l2_ctrl_handler_setup(&priv->ctrl_handler);
    if (ret < 0) {
        dev_err(&client->dev, "Error %d setting default controls\n",
            ret);
        goto error;
    }

    return 0;
error:
    v4l2_ctrl_handler_free(&priv->ctrl_handler);
    return ret;
}
```

## 1.6 Power-up and power-up functions

Mainly to increase the control of the sensor power-up and power-up, the operation of the IO port.

```c
static int imx219_s_power(struct v4l2_subdev *sd, int on)
{
    struct i2c_client *client = v4l2_get_subdevdata(sd);
    struct imx219 *priv = to_imx219(client);

    // no used
    // if (on) {
    //      dev_dbg(&client->dev, "imx219 power on\n");
    //      clk_prepare_enable(priv->clk);
    // } else if (!on) {
    //      dev_dbg(&client->dev, "imx219 power off\n");
    //      clk_disable_unprepare(priv->clk);
    // }

    return 0;
}
```

## 1.7 set_fmt functions

Mainly a modification of the fmt->format.code = MEDIA_BUS_FMT_SRGGB10_1X10 sentence, the sensor is supported raw10/raw12.

```c
static int imx219_set_fmt(struct v4l2_subdev *sd,
        struct v4l2_subdev_pad_config *cfg,
        struct v4l2_subdev_format *fmt)
{
    struct i2c_client *client = v4l2_get_subdevdata(sd);
    struct imx219 *priv = to_imx219(client);
    const struct imx219_mode *mode;
    s64 h_blank, v_blank, pixel_rate;
    u32 fps = 0;

    dev_info(&client->dev,"%s:start\n",__func__);
    if (fmt->which == V4L2_SUBDEV_FORMAT_TRY)
        return 0;

    mode = imx219_find_best_fit(fmt);
    fmt->format.code = MEDIA_BUS_FMT_SRGGB10_1X10;
    fmt->format.width = mode->width;
    fmt->format.height = mode->height;
    fmt->format.field = V4L2_FIELD_NONE;
    priv->cur_mode = mode;
    h_blank = mode->hts_def - mode->width;
    __v4l2_ctrl_modify_range(priv->hblank, h_blank,
                    h_blank, 1, h_blank);
    v_blank = mode->vts_def - mode->height;
    __v4l2_ctrl_modify_range(priv->vblank, v_blank,
                    v_blank,
                    1, v_blank);
    fps = DIV_ROUND_CLOSEST(mode->max_fps.denominator,
        mode->max_fps.numerator);
    pixel_rate = mode->vts_def * mode->hts_def * fps;
    __v4l2_ctrl_modify_range(priv->pixel_rate, pixel_rate,
                    pixel_rate, 1, pixel_rate);

    /* reset crop window */
    priv->crop_rect.left = 1640 - (mode->width / 2);
    if (priv->crop_rect.left < 0)
        priv->crop_rect.left = 0;
    priv->crop_rect.top = 1232 - (mode->height / 2);
    if (priv->crop_rect.top < 0)
        priv->crop_rect.top = 0;
    priv->crop_rect.width = mode->width;
    priv->crop_rect.height = mode->height;

    return 0;
}
```

## 1.8 get_fmt functions

Mainly a modification of the fmt->format.code = MEDIA_BUS_FMT_SRGGB10_1X10 sentence, the sensor is supported raw10/raw12.

```c
static int imx219_get_fmt(struct v4l2_subdev *sd,
        struct v4l2_subdev_pad_config *cfg,
        struct v4l2_subdev_format *fmt)
{
    struct i2c_client *client = v4l2_get_subdevdata(sd);
    struct imx219 *priv = to_imx219(client);
    const struct imx219_mode *mode = priv->cur_mode;

    dev_info(&client->dev,"%s:start\n",__func__);

    if (fmt->which == V4L2_SUBDEV_FORMAT_TRY)
        return 0;

    fmt->format.width = mode->width;
    fmt->format.height = mode->height;
    fmt->format.code = MEDIA_BUS_FMT_SRGGB10_1X10;
    fmt->format.field = V4L2_FIELD_NONE;

    dev_info(&client->dev,"%s:mode->width(%d),mode->height(%d)end\n",__func__,mode->width,mode->height);
    return 0;
}
```

# 2. The configuration parameters of the ISP

The configuration file of isp is mediactl_init function to use, in json format, as follows: (The meaning of each parameter refer to the ISP's register document)

```json
{
    "isp_general": {
        "isp_out_sel": 0,
        "dvp_ch_mode": 1,
        "hist_3a_out_en": 0,
        "main_out": {
            "out_img_format": 1,
            "out_yuv_in_format": 0,
            "out_yuv422_pxl_order": 0,
            "out_pxl_width": 0,
            "out_frame_buf_size": 2048
        },
        "out0": {
            "ds0_out_img_format": 1,
            "ds0_out_yuv_in_format": 0,
            "ds0_out_yuv422_pxl_order": 0,
            "ds0_out_pxl_width": 0,
            "ds0_frame_buf_size": 2048
        },
        "out1": {
            "ds1_out_img_format": 1,
            "ds1_out_yuv_in_format": 0,
            "ds1_out_yuv422_pxl_order": 0,
            "ds1_out_pxl_width": 0,
            "ds1_frame_buf_size": 2048
        },
        "out2": {
            "ds2_out_img_format": 0,
            "ds2_out_yuv_in_format": 0,
            "ds2_out_yuv422_pxl_order": 0,
            "ds2_out_pxl_width": 0,
            "ds2_frame_buf_size": 2048
        },
        "wdr": {
            "wdr_mode": 0,
            "wdr_long_ch_mode": 0,
            "wdr_long_l2_buf_en": 0,
            "wdr_short_s1_buf_en": 0,
            "wdr_dynamic_switch_en": 0,
            "wdr_long_l2_buf_depth": 0,
            "wdr_long_img_format": 0,
            "wdr_long_yuv_in_format": 0,
            "wdr_long_img_out_format": 0,
            "wdr_long_yuv422_pxl_order": 0,
            "wdr_long_pixel_width": 2,
            "wdr_buf_base": 0,
            "wdr_line_stride": 0,
            "wdr_frame_buf_size": 0
        },
        "nr3d": {
            "nr3d_en": 0,
            "nr3d_fbcd_en": 0,
            "nr3d_mv_out_en": 0,
            "nr3d_y_img_format": 0,
            "nr3d_y_yuv_in_format": 0,
            "nr3d_y_img_out_format": 0,
            "nr3d_y_yuv422_pxl_order": 0,
            "nr3d_y_pixel_width": 2,
            "nr3d_uv_img_format": 0,
            "nr3d_uv_yuv_in_format": 0,
            "nr3d_uv_mig_out_format": 0,
            "nr3d_uv_yuv422_pxl_order": 0,
            "nr3d_uv_pixel_width": 2,
            "nr3d_frame_buf_size": 0
        },
        "ldc": {
            "ldc_line_stride": 2048,
            "ldc_frame_buf_size": 2048
        }
    },
    "isp_core": {
        "itc": {
            "hsync_pol": 0,
            "vsync_pol": 0,
            "hsync_input_timing": 2,
            "vsync_input_timing": 1,
            "flip_ctl": 0,
            "video_fmt_sl": 0,
            "itc_ttl_h": 3476,
            "itc_ttl_v": 1166,
            "itc_stt_hr": 0,
            "itc_stt_vr": 1
        },
        "tpg": {
            "tpg_en": 0,
            "bayer_mode_sel": 3,
            "motion_mode_sel": 0,
            "tpg_sel": 9,
            "wdr_l_mul_data": 0,
            "wdr_m_mul_data": 0,
            "wdr_s_mul_data": 0
        },
        "blc": {
            "blc_en": 1,
            "blc_offset": 261,
            "blc_ratio": 429
        },
        "lsc": {
            "lsc_en": 1,
            "lsc_h_center": 960,
            "lsc_v_center": 540,
            "lsc_r_ratio": 16,
            "lsc_g_ratio": 16,
            "lsc_b_ratio": 16,
            "lsc_ir_ratio": 16
        },
        "ae": {
            "ae_as_en": 1,
            "ae_ag_en": 1,
            "ae_airis_en": 0,
            "ae_enter_ls_sel": 0,
            "ae_exit_ls_sel": 0,
            "ae_win_mode_sel": 0,
            "ae_back_light_mode_sel": 0,
            "ae_day_change_en": 0,
            "ae_day_change_sel": 0,
            "ae_win_stth": 0,
            "ae_win_sttv": 0,
            "ae_win_endh": 1919,
            "ae_win_endv": 1079,
            "ae_yobj": 128,
            "ae_av_rg": 8,
            "ae_l_ex_time": 1000,
            "ae_m_ex_time": 32,
            "ae_s_ex_time": 32,
            "ae_agc": 0,
            "ae_ad_shuttle_freq": 1,
            "ae_ad_gain_freq": 1,
            "ae_adjust_step_max": 5,
            "ae_ex_value_max": 2112,
            "ae_ex_value_mid": 264,
            "ae_ex_value_min": 256,
            "ae_gain_value_max": 2304,
            "ae_gain_value_mid": 512,
            "ae_gain_value_min": 0,
            "ae_dn_switch_ad_step_max": 512,
            "ae_dn_switch_wait_time": 255,
            "ape_max_diff": 12,
            "ape_drv_signal_max": 3840,
            "ape_coeff_distance": 0,
            "ape_coeff_speed": 0,
            "ape_coeff_acceleration": 0,
            "ape_drv_manual_value": 4095,
            "ape_damp_manual_value": 2048
        },
        "awb": {
            "awb_d65_en": 1,
            "awb_ccm_en": 1,
            "awb_en": 1,
            "awb_mode_sel": 1,
            "awb_hist_mode_sel": 0,
            "awb_veri_en": 0,
            "awb_fb_en": 0,
            "awb_value_save_en": 0,
            "awb_ccm_adp_adjust_en": 1,
            "awb_stab_en": 1,
            "awb_d65_red_gain": 495,
            "awb_d65_blue_gain": 504,
            "ccm_rr": 264,
            "ccm_rg": 8,
            "ccm_rb": 8,
            "ccm_gr": 77,
            "ccm_gg": 345,
            "ccm_gb": 15,
            "ccm_br": 4,
            "ccm_bg": 64,
            "ccm_bb": 324,
            "ccm_correct_coff": 260,
            "awb_win_stth": 0,
            "awb_win_sttv": 0,
            "awb_win_endh": 1919,
            "awb_win_endv": 1079,
            "awb_correct_diff_th": 32,
            "awb_color_changeres_time": 8,
            "awb_historgram_th": 64,
            "awb_red_gain_adjust": 256,
            "awb_green_gain_adjust": 256,
            "awb_blue_gain_adjust": 256,
            "awb_red_max_value": 512,
            "awb_blue_max_value": 1023,
            "awb_red_min_value": 64,
            "awb_blue_min_value": 128,
            "awb_red_obj_value": 288,
            "awb_blue_obj_value": 288
        },
        "wdr": {
            "wdr_fusion_en": 0,
            "wdr_frame_sel": 0,
            "wdr_adp_adjust_en": 0,
            "wdr_stab_en": 0,
            "wdr_en": 0,
            "wdr_ghost_remove_en": 0,
            "wdr_3frame_out_mode": 0,
            "wdr_mode_sel": 0,
            "wdr_2frame_ex_ratio": 1,
            "wdr_3frame_ex_ratio": 1,
            "wdr_stat_img_sel": 0,
            "wdr_ltm_data_sel": 1,
            "wdr_tz_data_sel": 1,
            "wdr_remove_purple_en": 0,
            "wdr_over_ex_ratio_th1": 384,
            "wdr_over_ex_ratio_th2": 32,
            "wdr_fusion_ratio_th": 192,
            "wdr_fusion_value1": 64,
            "wdr_fusion_value2": 16
        },
        "csc": {
            "rgb2yuv_00": 153,
            "rgb2yuv_01": 315,
            "rgb2yuv_02": 75,
            "rgb2yuv_10": 301,
            "rgb2yuv_11": 264,
            "rgb2yuv_12": 148,
            "rgb2yuv_20": 58,
            "rgb2yuv_21": 51,
            "rgb2yuv_22": 223
        },
        "ada": {
            "gm_rgb_en": 1,
            "gm_yuv_en": 1,
            "ada_en": 1,
            "ada_sbz_en": 1,
            "ada_ccr_en": 1,
            "ada_adp_en": 1,
            "ada_adp_ccr_en": 1,
            "ada_stat_mode_sel": 0,
            "ada_enh_mode_sel": 2,
            "ada_hist_max": 128,
            "ada_ttl_max": 128,
            "ada_win_stth": 0,
            "ada_win_sttv": 0,
            "ada_win_endh": 1919,
            "ada_win_endv": 1079
        },
        "rgb-ir": {
            "raw_fmt": 0,
            "rgbir_rct_en": 0,
            "dfc_en": 0,
            "rgbir_fs_en": 0,
            "rgbir_ot_sl": 0,
            "rgbir_fs_max": 256,
            "dfc_krb": 0,
            "dfc_ky": 0,
            "dfc_th": 256,
            "dfc_th_1": 256
        },
        "2dnr": {
            "dpeak_en": 1,
            "nr2d_raw_en": 1,
            "nr2d_eg_en": 1,
            "nr2d_jl_en": 1,
            "nr2d_av_en": 1,
            "nr2d_c_en": 1,
            "dpeak_adp_en": 1,
            "nr2d_raw_adp_en": 1,
            "nr2d_y_adp_en": 1,
            "nr2d_c_adp_en": 1,
            "nr2d_raw_kl": 128,
            "nr2d_jl_th": 511,
            "nr2d_eg_k": 768,
            "nr2d_y_k": 128,
            "nr2d_c_k": 128
        },
        "3dnr": {
            "nr3d_en": 0,
            "nr3dp_y_en": 0,
            "nr3dp_c_en": 0,
            "nr3dm_y_en": 0,
            "nr3dm_c_en": 0,
            "nr3db_y_en": 0,
            "nr3db_c_en": 0,
            "nr3dm_nr2d_y_en": 0,
            "nr3dm_nr2d_c_en": 0,
            "core_3dnr_wb_en": 0,
            "core_3dnr_wb_sel": 0,
            "core_3dnr_adp_luma_en": 0,
            "core_3dnr_adp_chroma_en": 0,
            "nr3dp_thy": 64,
            "nr3dp_thyp": 64,
            "nr3dp_thcp": 32,
            "nr3dm_mid_th": 128,
            "nr3dm_mtp_th": 8,
            "nr3dm_mtc_th": 128,
            "nr3dm_ym_k": 128,
            "nr3dm_thy": 64,
            "nr3dm_min": 0,
            "nr3dm_thw0": 128,
            "core_3dnr_chroma_intensity": 128,
            "nr3db_nr2d_eg_th": 64,
            "nr3db_thyp": 64,
            "nr3db_thcp": 16
        },
        "enh": {
            "ltm": {
                "enh_ltm_en": 1,
                "enh_adp_ltm_en": 0,
                "ltm_gain": 192,
                "ltm_mm_th": 128
            },
            "sharp": {
                "enh_sharp_en": 1,
                "enh_adp_sharp_en": 1,
                "shp_core": 8,
                "shp_th1": 128,
                "shp_th2": 256,
                "shp_gain": 192
            },
            "cc": {
                "enh_cc_en": 0,
                "enh_adp_cc_en": 1
            }
        },
        "post_ctl": {
            "otc_ctl": {
                "otc_en": 0,
                "otc_yc_sl": 0,
                "otc_uv_sl": 1,
                "otc_hs_plt_sl": 0,
                "otc_vs_plt_sl": 0,
                "otc_stt_vr": 0,
                "otc_stt_hr": 0
            },
            "ctrst": {
                "ctrst_en": 1,
                "ctrst_gain": 128
            },
            "luma": {
                "luma_en": 1,
                "luma_gain": 192
            },
            "strt": {
                "strt_en": 1,
                "strt_gain": 192
            }
        },
        "ldc": {
            "ldc_en": 0,
            "ldc_rct_en": 0,
            "ldc_rq_frq": 128,
            "ldc_stt_ln": 540,
            "ldc_ch": 960,
            "ldc_cv": 540,
            "ldc_cr": 684,
            "ldc_cz": 684
        },
        "af": {
            "af_stat_en": 1,
            "af_stat_mode_sel": 0,
            "af_stat_win_h_start": 0,
            "af_stat_win_v_start": 0,
            "af_stat_win_h_end": 1919,
            "af_stat_win_v_end": 1079
        }
    },
    "isp_post": {
        "rgb2yuv": {
            "osd_rgb2yuv_coeff00": 306,
            "osd_rgb2yuv_coeff01": 601,
            "osd_rgb2yuv_coeff02": 117,
            "osd_rgb2yuv_coeff03": 0,
            "osd_rgb2yuv_coeff10": 3920,
            "osd_rgb2yuv_coeff11": 3749,
            "osd_rgb2yuv_coeff12": 523,
            "osd_rgb2yuv_coeff13": 128,
            "osd_rgb2yuv_coeff20": 523,
            "osd_rgb2yuv_coeff21": 3658,
            "osd_rgb2yuv_coeff22": 4011,
            "osd_rgb2yuv_coeff23": 128
        },
        "yuv2rgb": {
            "out_yuv2rgb_coeff00": 1024,
            "out_yuv2rgb_coeff01": 0,
            "out_yuv2rgb_coeff02": 1441,
            "out_yuv2rgb_coeff03": 3916,
            "out_yuv2rgb_coeff10": 1024,
            "out_yuv2rgb_coeff11": 3742,
            "out_yuv2rgb_coeff12": 3362,
            "out_yuv2rgb_coeff13": 136,
            "out_yuv2rgb_coeff20": 1024,
            "out_yuv2rgb_coeff21": 1822,
            "out_yuv2rgb_coeff22": 0,
            "out_yuv2rgb_coeff23": 3868
        },
        "ds0": {
            "ds0_out_rgb_mode": 0,
            "ds0_out_rgb_en": 0,
            "ds0_out_yuv_mode": 0,
            "ds0_out_uv_swap": 0,
            "ds0_osd0": {
                "ds0_osd0_enable": 0,
                "ds0_osd0_type": 0,
                "ds0_osd0_alpha_tpye": 0,
                "ds0_osd0_vst": 0,
                "ds0_osd0_hst": 0,
                "ds0_osd0_vend": 0,
                "ds0_osd0_hend": 0,
                "ds0_osd0_dma_request_length": 0,
                "ds0_osd0_dma_map": 0,
                "ds0_osd0_rgb_rev": 0,
                "ds0_osd0_global_alpha": 0,
                "ds0_osd0_swap_64": 0,
                "ds0_osd0_outstanding_num": 0,
                "ds0_osd0_bd_limit_en": 0
            },
            "ds0_osd1": {
                "ds0_osd1_enable": 0,
                "ds0_osd1_type": 0,
                "ds0_osd1_alpha_tpye": 0,
                "ds0_osd1_vst": 0,
                "ds0_osd1_hst": 0,
                "ds0_osd1_vend": 0,
                "ds0_osd1_hend": 0,
                "ds0_osd1_dma_request_length": 0,
                "ds0_osd1_dma_map": 0,
                "ds0_osd1_rgb_rev": 0,
                "ds0_osd1_global_alpha": 0,
                "ds0_osd1_swap_64": 0,
                "ds0_osd1_outstanding_num": 0,
                "ds0_osd1_bd_limit_en": 0
            },
            "ds0_osd2": {
                "ds0_osd2_enable": 0,
                "ds0_osd2_type": 0,
                "ds0_osd2_alpha_tpye": 0,
                "ds0_osd2_vst": 0,
                "ds0_osd2_hst": 0,
                "ds0_osd2_vend": 0,
                "ds0_osd2_hend": 0,
                "ds0_osd2_dma_request_length": 0,
                "ds0_osd2_dma_map": 0,
                "ds0_osd2_rgb_rev": 0,
                "ds0_osd2_global_alpha": 0,
                "ds0_osd2_swap_64": 0,
                "ds0_osd2_outstanding_num": 0,
                "ds0_osd2_bd_limit_en": 0
            }
        },
        "ds1": {
            "ds1_out_rgb_mode": 0,
            "ds1_out_rgb_en": 0,
            "ds1_out_yuv_mode": 0,
            "ds1_out_uv_swap": 0,
            "ds1_osd0": {
                "ds1_osd0_enable": 0,
                "ds1_osd0_type": 0,
                "ds1_osd0_alpha_tpye": 0,
                "ds1_osd0_vst": 0,
                "ds1_osd0_hst": 0,
                "ds1_osd0_vend": 0,
                "ds1_osd0_hend": 0,
                "ds1_osd0_dma_request_length": 0,
                "ds1_osd0_dma_map": 0,
                "ds1_osd0_rgb_rev": 0,
                "ds1_osd0_global_alpha": 0,
                "ds1_osd0_swap_64": 0,
                "ds1_osd0_outstanding_num": 0,
                "ds1_osd0_bd_limit_en": 0
            },
            "ds1_osd1": {
                "ds1_osd1_enable": 0,
                "ds1_osd1_type": 0,
                "ds1_osd1_alpha_tpye": 0,
                "ds1_osd1_vst": 0,
                "ds1_osd1_hst": 0,
                "ds1_osd1_vend": 0,
                "ds1_osd1_hend": 0,
                "ds1_osd1_dma_request_length": 0,
                "ds1_osd1_dma_map": 0,
                "ds1_osd1_rgb_rev": 0,
                "ds1_osd1_global_alpha": 0,
                "ds1_osd1_swap_64": 0,
                "ds1_osd1_outstanding_num": 0,
                "ds1_osd1_bd_limit_en": 0
            },
            "ds1_osd2": {
                "ds1_osd2_enable": 0,
                "ds1_osd2_type": 0,
                "ds1_osd2_alpha_tpye": 0,
                "ds1_osd2_vst": 0,
                "ds1_osd2_hst": 0,
                "ds1_osd2_vend": 0,
                "ds1_osd2_hend": 0,
                "ds1_osd2_dma_request_length": 0,
                "ds1_osd2_dma_map": 0,
                "ds1_osd2_rgb_rev": 0,
                "ds1_osd2_global_alpha": 0,
                "ds1_osd2_swap_64": 0,
                "ds1_osd2_outstanding_num": 0,
                "ds1_osd2_bd_limit_en": 0
            }
        },
        "ds2": {
            "ds2_out_rgb_mode": 0,
            "ds2_out_rgb_en": 1,
            "ds2_out_yuv_mode": 0,
            "ds2_out_uv_swap": 0,
            "ds2_osd0": {
                "ds2_osd0_enable": 0,
                "ds2_osd0_type": 0,
                "ds2_osd0_alpha_tpye": 0,
                "ds2_osd0_vst": 0,
                "ds2_osd0_hst": 0,
                "ds2_osd0_vend": 0,
                "ds2_osd0_hend": 0,
                "ds2_osd0_dma_request_length": 0,
                "ds2_osd0_dma_map": 0,
                "ds2_osd0_rgb_rev": 0,
                "ds2_osd0_global_alpha": 0,
                "ds2_osd0_swap_64": 0,
                "ds2_osd0_outstanding_num": 0,
                "ds2_osd0_bd_limit_en": 0
            },
            "ds2_osd1": {
                "ds2_osd1_enable": 0,
                "ds2_osd1_type": 0,
                "ds2_osd1_alpha_tpye": 0,
                "ds2_osd1_vst": 0,
                "ds2_osd1_hst": 0,
                "ds2_osd1_vend": 0,
                "ds2_osd1_hend": 0,
                "ds2_osd1_dma_request_length": 0,
                "ds2_osd1_dma_map": 0,
                "ds2_osd1_rgb_rev": 0,
                "ds2_osd1_global_alpha": 0,
                "ds2_osd1_swap_64": 0,
                "ds2_osd1_outstanding_num": 0,
                "ds2_osd1_bd_limit_en": 0
            }
        }
    }
}
```

# 3. video_cfg profile

This file is mediactl_init function to use, is in json format, the specific format and related explanations are as follows:

```json
{
    "sensor0": {
        "sensor0_name": "m00_f_imx219_0 0-0010",
        "sensor0_cfg_file": "imx219_0.conf",
        "sensor0_total_size": {
            "sensor0_total_width": 3476,
            "sensor0_total_height": 1166
        },
        "sensor0_active_size": {
            "sensor0_active_width": 1920,
            "sensor0_active_height": 1080
        },
        "/dev/video2": {
            "video2_used": 0,
            "video2_width": 1920,
            "video2_height": 1080,
            "video2_out_format": 1
        },
        "/dev/video3": {
            "video3_used": 1,
            "video3_width": 1920,
            "video3_height": 1080,
            "video3_out_format": 1
        },
        "/dev/video4": {
            "video4_used": 0,
            "video4_width": 640,
            "video4_height": 480,
            "video4_out_format": 1
        },
        "/dev/video5": {
            "video5_used": 0,
            "video5_width": 320,
            "video5_height": 320,
            "video5_height_r": 240,
            "video5_out_format": 1
        }
    },
    "sensor1": {
        "sensor1_name": "m01_f_imx219_1 3-0010",
        "sensor1_cfg_file": "imx219_1.conf",
        "sensor1_total_size": {
            "sensor1_total_width": 3476,
            "sensor1_total_height": 1166
        },
        "sensor1_active_size": {
            "sensor1_active_width": 1920,
            "sensor1_active_height": 1080
        },
        "/dev/video6": {
            "video6_used": 0,
            "video6_width": 1920,
            "video6_height": 1080,
            "video6_out_format": 1
        },
        "/dev/video7": {
            "video7_used": 0,
            "video7_width": 1080,
            "video7_height": 720,
            "video7_out_format": 1
        },
        "/dev/video8": {
            "video8_used": 0,
            "video8_width": 640,
            "video8_height": 480,
            "video8_out_format": 1
        },
        "/dev/video9": {
            "video9_used": 0,
            "video9_width": 320,
            "video9_height": 240,
            "video9_height_r": 240,
            "video9_out_format": 1
        }
    }
}
```

The information that needs to be modified is explained as follows:

```text
sensor0_name:只在V4L2驱动中设置的sensor驱动名字。
sensor0_cfg_file:sensor对应的isp参数配置文件名字，如imx219_0.conf。
sensor0_total_width:sensor输出的水平方向的总像素，用来产生VSYNC信号，如3476
sensor0_total_height:sensor输出的总行数，用来产生HSYNC信号，如1166
sensor0_active_width:sensor输出的水平方向的有效像素，如1920,
sensor0_active_height:sensor输出的有效行数，如1080
video2_used:1 -- 使能，0 -- 没有使用。
video2_width:video输出的宽度，如1920。
video2_height:video输出的高度，如1080。
video2_out_format:1--指YUV420,NV21。
video3_used:1 -- 使能，0 -- 没有使用。
video3_width:video输出的宽度，如1080。
video3_height:video输出的高度，如720。
video3_out_format:1--指YUV420,NV21。
video4_used:1 -- 使能，0 -- 没有使用。
video4_width:video输出的宽度，如640。
video4_height:video输出的高度，如480。
video4_out_format:1--指YUV420,NV21。
video5_used:1 -- 使能，0 -- 没有使用。
video5_width:video输出的宽度，如320。
video5_height":video存储的高度，如320。
video5_height_r:video输出的高度，如240。
video5_out_format:0--指分离RGB，1--指ARGB。
sensor1_name:只在V4L2驱动中设置的sensor驱动名字。
sensor1_cfg_file:sensor对应的isp参数配置文件名字，如imx219_0.conf。
sensor1_total_width:sensor输出的水平方向的总像素，用来产生VSYNC信号，如3476
sensor1_total_height:sensor输出的总行数，用来产生HSYNC信号，如1166
sensor1_active_width:sensor输出的水平方向的有效像素，如1920,
sensor1_active_height:sensor输出的有效行数，如1080
video6_used:1 -- 使能，0 -- 没有使用。
video6_width:video输出的宽度，如1920。
video6_height:video输出的高度，如1080。
video6_out_format:1--指YUV420,NV21。
video7_used:1 -- 使能，0 -- 没有使用。
video7_width:video输出的宽度，如1080。
video7_height:video输出的高度，如720.
video7_out_format:1--指YUV420,NV21。
video8_used:1 -- 使能，0 -- 没有使用。
video8_width:video输出的宽度，如640。
video8_height:video输出的高度，如480。
video8_out_format:1--指YUV420,NV21。
video9_used:1 -- 使能，0 -- 没有使用。
video9_width:video输出的宽度，如320。
video9_height:video存储的宽度，如320。
video9_height_r:video输出的高度，如240。
video9_out_format:0--指分离RGB，1--指ARGB。
[out]   dev_info:   mediactl_lib返回从video的配置文件得到的video信息，具体的解释如下。
video_used:这里是指ISP的pipeline，如果使用就会返回1，否则0。K510支持ISP_F2K/ISP_R2K这两个pipeline，每个pipeline最多支持4个video输出。
video_name[4]:返回的video的名字。f2k的四个video是video2/video3/video4/video5;r2k的四个video是 video6/video7/video8/video9
enable[4]:返回的每个video是否使能，1 -- 使能，0 -- 没有使用。
video_width[4]:返回的每个video的宽度。
video_height[4]:返回的每个video的高度。
video_out_format[4]:返回的每个video的输出图像格式，具体见《video的配置文件》的解释。
```

**Translation Disclaimer**  
For the convenience of customers, Canaan uses an AI translator to translate text into multiple languages, which may contain errors. We do not guarantee the accuracy, reliability or timeliness of the translations provided. Canaan shall not be liable for any loss or damage caused by reliance on the accuracy or reliability of the translated information. If there is a content difference between the translations in different languages, the Chinese Simplified version shall prevail. 

If you would like to report a translation error or inaccuracy, please feel free to contact us by mail.