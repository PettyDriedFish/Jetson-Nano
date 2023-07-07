# A-Smart-Home-System-Based-on-Jetson-Nano
Record various situations of the project!

I have been learning Jeston Nano for a few days and have encountered some issues. Suddenly, I want to record the entire project!

## 0609

I tried to burn the SD card and the entire process went very smoothly! I haven't even seen a system pop-up. But after telling me that the burn was successful, I found that countless disks appeared. I was very shocked. At present, I suspect that this issue may occur due to not being an official package. 
Possible solution: https://zhuanlan.zhihu.com/p/580758960

## 0610

need buy: 
https://www.amazon.co.uk/GeeekPi-Acrylic-Cooling-Network-Included/dp/B08MTLQCLJ/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=RhPIq&content-id=amzn1.sym.ee350e28-7617-480b-b9a4-e60d65a44a25&pf_rd_p=ee350e28-7617-480b-b9a4-e60d65a44a25&pf_rd_r=16VE41HMJP22Q8VE2JMW&pd_rd_wg=Ds4q8&pd_rd_r=421a5564-7597-4c01-922f-8084a2234558&pd_rd_i=B08MTLQCLJ 
and 
https://www.amazon.co.uk/Waveshare-AC8265-Wireless-Applicable-Bluetooth/dp/B07SGDRG34/ref=pd_bxgy_sccl_1/260-4820670-3112746?pd_rd_w=SMMd6&content-id=amzn1.sym.40f919ed-e530-4b1a-8d7e-39de6587208d&pf_rd_p=40f919ed-e530-4b1a-8d7e-39de6587208d&pf_rd_r=D6049ZC709JD5J8TBSHD&pd_rd_wg=k4LhI&pd_rd_r=7a3a9c57-fb0c-4e53-a428-189083162432&pd_rd_i=B07SGDRG34&psc=1

Another domestically produced burning process information: https://blog.csdn.net/weixin_67660471/article/details/127693072

The domestic nano and NVIDIA nano have an additional step of firmware flushing, and the image file is different. Other operations are basically the same.

## 0613

https://www.waveshare.com/wiki/JETSON-NANO-DEV-KIT

https://www.waveshare.net/wiki/JETSON-NANO-DEV-KIT

## 0701

something to remind for restart:

sudo sh -c 'echo 70 > /sys/devices/pwm-fan/target_pwm'

wifi：

ifconfig
sudo nmcli device wifi hotspot con-name USB-HS ifname wlan0 ssid zaozi-desktop password 12345678
sudo nmcli connection up USB-HS

and some links: 

https://www.waveshare.net/wiki/JETSON-NANO-DEV-KIT#GPIO

https://www.waveshare.net/wiki/Environment_Sensor_for_Jetson_Nano

https://www.waveshare.net/wiki/Fan-4020-PWM-5V

https://outlook.office365.com/mail/

https://airportal.cn/

https://chat.openai.com/

i am sooo sad

https://blog.csdn.net/qq1195365047/article/details/88974647

https://github.com/python-kasa/python-kasa

https://stackoverflow.com/questions/52231825/python-3-7-import-smbus-modulenotfounderror-no-module-named-smbus

## 0707

配置java环境变量：

https://juejin.cn/s/linux%E4%B8%8B%E9%85%8D%E7%BD%AEjava%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F

### .tar.gz 和 .tgz
tar -zxvf FileName.tar.gz               # 解压

tar -zcvf FileName.tar.gz DirName       # 将DirName和其下所有文件（夹）压缩

tar -C DesDirName -zxvf FileName.tar.gz # 解压到目标路径

###国产版jetson nano安装pycharm
https://zhuanlan.zhihu.com/p/583062190
