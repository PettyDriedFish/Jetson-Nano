import asyncio

import schedule
import time
import datetime
import getData
import setPlugs

today_temperature = [0.0] * 24
today_humidity = [0.0] * 24
hourly_data_count = [0.0] * 24 # 平均值

data = {
    # 'today_temperature': [30.03, 29.84, 29.69, 29.66, 29.59, 29.5, 29.4, 29.28,
    #                       29.16, 28.88, 28.7, 28.65, 28.62, 28.5, 27.55, 27.08,
    #                       27.47, 28.88, 28.42, 28.49, 28.47, 28.34, 28.4, 29.34],
    # 'today_humidity': [39.52, 40.25, 43.28, 46.85, 48.94, 49.91, 50.38, 50.52,
    #                    49.61, 49.53, 49.61, 49.92, 48.09, 44.8, 34.84, 33.51,
    #                    30.72, 38.7, 35.96, 32.03, 31.65, 33.02, 36.22, 38.01]
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

    today_temperature[current_hour] += current_temperature
    today_humidity[current_hour] += current_humidity
    hourly_data_count[current_hour] += 1

    print("today_temperature: " + str(today_temperature))
    print("today_humidity: " + str(today_humidity))

    # 判断是否为整点，并计算平均值
    if hourly_data_count[current_hour] == 2:
        today_temperature[current_hour] = round(today_temperature[current_hour] / hourly_data_count[current_hour], 2)
        today_humidity[current_hour] = round(today_humidity[current_hour] / hourly_data_count[current_hour], 2)
        hourly_data_count[current_hour] = 1

    print("today_temperature: " + str(today_temperature))
    print("today_humidity: " + str(today_humidity))

    # # 通过将对main模块的导入放在函数内部，可以避免循环导入问题
    # from main import lock
    # # 释放锁
    # if lock.locked():
    #     lock.release()
    #     print("scheduleTH： Lock released")

# 定义定时任务，每分钟触发记录数据函数
# schedule.every().minute.do(record_data)
# schedule.every().hour.at(":00").do(record_data)

# 定义异步函数来运行定时任务
# async def run_schedule():
#     schedule.run_pending()
#     # record_data()
#     # 通过将对main模块的导入放在函数内部，可以避免循环导入问题
#     from main import lock
#     # 释放锁
#     if lock.locked():
#         lock.release()
#         print("scheduleTH： Lock released")
#     await asyncio.sleep(1)

# def run_set_plugs():
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     loop.run_until_complete(setPlugs.controlTH())

async def run_schedule():
    # 通过将对main模块的导入放在函数内部，可以避免循环导入问题
    # from main import lock
    while True:
        # 检查锁的状态
        # if lock.locked():
        record_data()  # 获取到锁后立即执行record_data()函数
        # loop = asyncio.new_event_loop()
        # asyncio.set_event_loop(loop)
        # loop.run_until_complete(setPlugs.controlTH())
            # lock.release()
            # print("scheduleTH： Lock released")

        await asyncio.sleep(600)

