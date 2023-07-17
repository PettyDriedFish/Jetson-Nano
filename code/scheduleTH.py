import schedule
import time
import datetime
import getData

today_temperature = [0] * 24
today_humidity = [0] * 24

data = {
    'today_temperature': today_temperature,
    'today_humidity': today_humidity
}

record_count = 0  # 记录次数

# 定义记录数据的函数
def record_data():
    print("in the record_data")
    global record_count

    current_hour = datetime.datetime.now().hour

    # 记录当前温度和湿度数据
    current_temperature = getData.getCurrentTemp()
    current_humidity = getData.getCurrentHum()

    today_temperature[record_count] = current_temperature
    today_humidity[record_count] = current_humidity

    print("today_temperature: " + str(today_temperature))
    print("today_humidity: " + str(today_humidity))

    record_count += 1

    if record_count >= 24:
        record_count = 0

# 定义定时任务，每分钟触发记录数据函数
schedule.every().minute.do(record_data)

# 主循环
while True:
    schedule.run_pending()
    time.sleep(1)
