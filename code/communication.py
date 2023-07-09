import time
import threading
from datetime import datetime
from kasa import SmartPlug
import requests
import getData
import setPlugs

# 配置Kasa智能插头的IP地址
fanPlug_ip = setPlugs.fanPlug
humidifierPlug_ip = setPlugs.humidifierPlug
heaterPlug_ip = setPlugs.heaterPlug

# 配置手机接收消息的URL
phone_url = 'ws://192.168.3.17:8000/websocket'

# 发送温湿度消息的函数
def send_temperature_humidity():
    while True:
        temp = getData.getCurrentTemp()
        hum = getData.getCurrentHum()

        # 构建要发送的消息
        message = f"Temperature: {temp}°C, Humidity: {hum}%"

        # 发送消息到手机
        requests.post(phone_url, json={'message': message})

        # 等待10分钟
        time.sleep(600)

# 监听Kasa智能插头状态的函数
def monitor_fanPlug_state():
    fanPlug = SmartPlug(fanPlug_ip)

    while True:
        fanPlug.update()

        # 获取插头的开关状态
        is_on = fanPlug.is_on

        # 构建要发送的消息
        message = f"fanPlug is {'on' if is_on else 'off'}"

        # 发送消息到手机
        requests.post(phone_url, json={'message': message})

        # 等待1秒
        time.sleep(1)

def monitor_humidifierPlug_state():
    humidifierPlug = SmartPlug(humidifierPlug_ip)

    while True:
        humidifierPlug.update()

        # 获取插头的开关状态
        is_on = humidifierPlug.is_on

        # 构建要发送的消息
        message = f"fanPlug is {'on' if is_on else 'off'}"

        # 发送消息到手机
        requests.post(phone_url, json={'message': message})

        # 等待1秒
        time.sleep(1)

def monitor_heaterPlug_state():
    heaterPlug = SmartPlug(heaterPlug_ip)

    while True:
        heaterPlug.update()

        # 获取插头的开关状态
        is_on = heaterPlug.is_on

        # 构建要发送的消息
        message = f"fanPlug is {'on' if is_on else 'off'}"

        # 发送消息到手机
        requests.post(phone_url, json={'message': message})

        # 等待1秒
        time.sleep(1)

# 创建并启动线程来发送温湿度消息和监听Kasa智能插头状态
thread1 = threading.Thread(target=send_temperature_humidity)
thread2 = threading.Thread(target=monitor_fanPlug_state)
thread3 = threading.Thread(target=monitor_humidifierPlug_state)
thread4 = threading.Thread(target=monitor_heaterPlug_state)

thread1.start()
thread2.start()
thread3.start()
thread4.start()

# 等待线程结束
thread1.join()
thread2.join()
thread3.join()
thread4.join()
