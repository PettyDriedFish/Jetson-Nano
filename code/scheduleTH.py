import schedule
import time
import datetime
import getData

today_temperature = [0] * 24
today_humidity = [0] * 24

data = {
    'today_temperature': [25.36, 25.39, 25.42, 25.5, 25.48, 25.46, 25.4, 25.41,
                          25.44, 25.39, 25.35, 25.31, 25.36, 25.26, 25.29, 25.2,
                          25.25, 25.2, 25.2, 25.23, 25.22, 25.21, 25.18, 25.16],
    'today_humidity': [45.85, 45.8, 45.81, 45.41, 45.49, 45.54, 45.57, 45.57,
                       45.61, 45.61, 45.73, 45.8, 45.97, 45.85, 45.91, 46.08,
                       45.98, 46.06, 46.05, 45.88, 45.84, 45.89, 45.98, 46.03]
}

record_count = 0  # 记录次数

# 定义记录数据的函数
# def record_data():
#     print("in the record_data")
#     global record_count
#
#     current_hour = datetime.datetime.now().hour
#
#     # 记录当前温度和湿度数据
#     current_temperature = getData.getCurrentTemp()
#     current_humidity = getData.getCurrentHum()
#
#     today_temperature[record_count] = current_temperature
#     today_humidity[record_count] = current_humidity
#
#     print("today_temperature: " + str(today_temperature))
#     print("today_humidity: " + str(today_humidity))
#
#     record_count += 1
#
#     if record_count >= 24:
#         record_count = 0
#
# # 定义定时任务，每分钟触发记录数据函数
# schedule.every().minute.do(record_data)
#
# # 主循环
# while True:
#     schedule.run_pending()
#     time.sleep(1)
