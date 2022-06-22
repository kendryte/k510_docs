# K510-CRB-KIT AWS Quick Start Guide

## 1. Document information

### 1.1 Product name

K510-CRB-KIT

### 1.2 Version

|Version|Date|Description|Author|
| :- | :- | :- | :- |
|1.0.0|2022-06-13|First version|Wanghao Zhangtao Shiwentao|
|||||
|||||

## 2. Overview

Kendryte K510 is the second-generation AI edge-side inference chip launched by Canaan, providing high-performance image and voice processing capabilities. It integrates the latest generation image processor ISP, supports TOF depth signal access.

K510-CORE is the core module, with a K510 chip onboard, which CPU adopts dual-core 64bit RISC-V architecture. K510 is equipped with the second-generation neural network processor KPU 2.0, using independent computing data-flow technology. Compared with the previous generation, it has improved computing power significantly while reducing power consumption. The onboard memory is 512MB LPDDR3@1600MHz. It supports two MIPI serial image inputs and one DVP parallel image input, and supports one MIPI image output.

K510 CRB-KIT is a developer kit based on the K510 chip. It adopts a hierarchical design and is based on the K510 core module.

## 3. Hardware Description

### 3.1 DataSheet

<https://canaan.io/product/kendryte-k510-crb-kit-developer-kit>

## 4. Set up your Development Environment

1. Install Docker Desktop on Ubuntu
   Download the Installation package: [Download](https://desktop.docker.com/linux/main/amd64/docker-desktop-4.9.1-amd64.deb?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-linux-amd64)

   Install Docker Desktop:

   ```shell
   sudo apt-get install ./docker-desktop-4.9.1-amd64.deb
   ```

   Reference: <https://docs.docker.com/desktop/linux/install/ubuntu>

2. Download K510 SDK:

   ```shell
   git clone https://github.com/kendryte/k510_buildroot.git
   ```

3. Start Docker environment:

   ```shell
   sh k510_buildroot/tools/docker/run_k510_docker.sh
   ```

4. Generate firmware:

   ```shell
   make
   ```

   __(On the docker env)__
5. Burn the firmware to TF Card:

   ```shell
   sudo dd if=k510_buildroot/k510_crb_lp3_v1_2_defconfig/image/sysimage-sdcard.img of=/dev/sdx oflag=sync bs=1M
   ```

   __(Use your actual device path instead of '/dev/sdx')__

## 5. Set up your hardware

- Front view of the hardware

![](/zh/images/aws_quick_start/board_front.png)

- Back view of the hardware

![](/zh/images/aws_quick_start/board_back.png)

- 5A@2A power adaptor, USB to type-C cable(Attached parts)

- Boot mode settting table

![](/zh/images/aws_quick_start/boot_mode.png)

- Uart driver download page: [Download](https://www.wch.cn/downloads/CH341SER_EXE.html)

## 6. Setup your AWS account and Permissions

### 6.1 Sign up for an AWS account

1. Open <https://portal.aws.amazon.com/billing/signup>
2. Follow the online instructions.

__Note:Save your AWS account number, because you need it for the next task.__

### 6.2 Create a user and grant permissions

1. Sign in to the [IAM console](https://console.aws.amazon.com/iam/) as the account owner by choosing Root user and entering your AWS account email address. On the next page, enter your password.
2. In the navigation pane, choose Users and then choose Add users.
3. For User name, enter iot_test
4. Select the check box next to AWS Management Console access. Then select Custom password, and then enter your new password in the text box.
5. (Optional) By default, AWS requires the new user to create a new password when first signing in. You can clear the check box next to User must create a new password at next sign-in to allow the new user to reset their password after they sign in.
6. Choose Next: Permissions.
7. Under Set permissions, choose Add user to group.
8. Choose Create group.
9. In the Create group dialog box, for Group name enter  iot_test
10. Choose Filter policies, and then select AWS managed - job function to filter the table contents.
11. In the policy list, select the check box for AWSIoTDataAccess and AWSIoTConfigAccess. Then choose Create group.
12. Back in the list of groups, select the check box for your new group. Choose Refresh if necessary to see the group in the list.
13. Choose Next: Tags.
14. (Optional) Add metadata to the user by attaching tags as key-value pairs. For more information about using tags in IAM, see [Tagging IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *IAM User Guide*.
15. Choose Next: Review to see the list of group memberships to be added to the new user. When you are ready to proceed, choose Create user.

## 7. Create Resources in AWS IoT

### 7.1 Create an AWS IoT Policy

Create an AWS IoT Policy document for your device to interact with AWS IoT services

Navigate to IoT Core console > Manage > Security > Policy and click on “Create policy”

__Note: A new policy must have a name and policy document.__

![](/zh/images/aws_quick_start/create_policy.png)

Then chose Policy statements > Policy document > JSON and add policy.

Sample Policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iot:Publish",
        "iot:Receive",
        "iot:Subscribe"
      ],
      "Resource": [
        "*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "iot:Connect"
      ],
      "Resource": [
        "arn:aws:iot:region:AWS-account-ID:client/*"
      ]
    }
  ]
}
```

__Note: This policy should be used for testing only.__

### 7.2 Create a new Device

Navigate to IoT Core console > Manage > All Devices > Things and click on “Create  Things”

![](/zh/images/aws_quick_start/create_things.png)

Then click Create single thing

![](/zh/images/aws_quick_start/create_single_thing.png)

Then add the name of new device

![](/zh/images/aws_quick_start/thing_properties.png)

Then chose Auto-generate a new certificate (recommended)

![](/zh/images/aws_quick_start/device_certificate.png)

Then chose your policy

![](/zh/images/aws_quick_start/attach_policies.png)

Download the certificate, public key, and private key for the device. Next, download the root CA for AWS IoT. Finally, click Done.

![](/zh/images/aws_quick_start/download_crts_keys.png)

## 8. Provision the Device with credentials

Make sure you have downloaded the k510_buildroot file in step four，put the file generated in step 7 into the certs folder，as shown in the figure

![](/zh/images/aws_quick_start/certs_folder.png)

Change variable name in `k510_buildroot/package/aws_iot_test/subscribe_publish_sample/aws_iot_config.h` file

![](/zh/images/aws_quick_start/aws_iot_config.png)

After all changes are completed, run the compiler on the premise that the build_root has been compiled

```shell
cd k510_buildroot/k510_crb_lp3_v1_2_defconfig
make aws_iot_test-rebuild
```

After compilation, you can see the file in the `k510_buildroot/k510_crb_lp3_v1_2_defconfig/target/app/aws_iot_test` folder

## 9. Build the demo

Compile k510_buildreoot, aws_iot_test has been compiled in package, and the generated executable file is in `/app/aws_iot_test`

## 10. Run the demo

Test MQTT Connect

Please enter the command on the serial port debugging page

```shell
cd /app/aws_iot_test
./aws_iot_test
```

Display on the development k510 board

![](/zh/images/aws_quick_start/aws_iot_test.png)

AWS IoT certification display

![](/zh/images/aws_quick_start/certification_display.png)

Each time an individual item is verified, just run aws_iot_test directly, and the final result is displayed

![](/zh/images/aws_quick_start/activity_log.png)

## 11. Debugging

During debugging, all log logs will be printed on the serial port debugging interface, as shown in the figure

![](/zh/images/aws_quick_start/aws_iot_test_log.png)

## 12. Troubleshooting

In case of network fluctuation, the link fails. Just rerun the test program

![](/zh/images/aws_quick_start/troubleshooting.png)
