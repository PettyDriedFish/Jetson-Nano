from python-kasa import SmartPlug
from python-kasa.exceptions import SmartDeviceException

#连接到智能插座
ip_address = "192.168.3.29"
plug = SmartPlug(ip_address)
plug.get_sysinfo()

#根据收到的值控制智能插座
received_value = 1  # 假设收到的值为 1 或 0
try:
    if received_value == 1:
        plug.turn_on()
    else:
        plug.turn_off()
except SmartDeviceException as e:
    print("控制插座时发生错误:", str(e))