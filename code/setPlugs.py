import plugs
import getData
import asyncio

async def controlTH():
    print("Executing setPlugs.py")

    currentTemp = getData.getCurrentTemp()
    currentHum = getData.getCurrentHum()

    import websocketServer

    lowTemp = websocketServer.globalData.get('min_temperature', 24.00)
    highTemp = websocketServer.globalData.get('max_temperature', 27.00)
    lowHum = websocketServer.globalData.get('min_humidity', 45.00)
    highHum = websocketServer.globalData.get('max_humidity', 55.00)

    print("lowTemp: " + str(lowTemp) + ", highTemp: " + str(highTemp))
    print("lowHum: " + str(lowHum) + ", highHum: " + str(highHum))

    # three plugs
    fanPlug = "192.168.3.29"
    humidifierPlug = "192.168.3.30"
    heaterPlug = "192.168.3.31"

    # temperature control
    # if currentTemp >= highTemp:
    #     asyncio.run(plugs.turnOnPlug(fanPlug))
    #     print("turnOnPlug(fanPlug)")
    # elif currentTemp <= lowTemp:
    #     asyncio.run(plugs.turnOnPlug(heaterPlug))
    #     print("turnOnPlug(heaterPlug)")
    # else:
    #     asyncio.run(plugs.turnOffPlug(fanPlug))
    #     asyncio.run(plugs.turnOffPlug(heaterPlug))
    #     print("nice temperature")
    if currentTemp >= highTemp:
        await plugs.turnOnPlug(fanPlug)
        print("turnOnPlug(fanPlug)")
    elif currentTemp <= lowTemp:
        await plugs.turnOnPlug(heaterPlug)
        print("turnOnPlug(heaterPlug)")
    else:
        await plugs.turnOffPlug(fanPlug)
        await plugs.turnOffPlug(heaterPlug)
        print("nice temperature")

    # humidity control
    # if currentHum >= highHum:
    #     # asyncio.run(plugs.turnOnPlug(fanPlug))
    #     print("high hum")
    # elif currentHum <= lowHum:
    #     asyncio.run(plugs.turnOnPlug(humidifierPlug))
    #     print("turnOnPlug(humidifierPlug)")
    # else:
    #     # asyncio.run(plugs.turnOffPlug(fanPlug))
    #     asyncio.run(plugs.turnOffPlug(humidifierPlug))
    #     print("nice humidity")
    if currentHum >= highHum:
        # asyncio.run(plugs.turnOnPlug(fanPlug))
        print("high hum")
    elif currentHum <= lowHum:
        await plugs.turnOnPlug(humidifierPlug)
        print("turnOnPlug(humidifierPlug)")
    else:
        # asyncio.run(plugs.turnOffPlug(fanPlug))
        await plugs.turnOffPlug(humidifierPlug)
        print("nice humidity")

    # while True:
    #     currentTemp = getData.getCurrentTemp()
    #     currentHum = getData.getCurrentHum()
    #
    #     lowTemp = websocketServer.globalData.get('min_temperature', 24.00)
    #     highTemp = websocketServer.globalData.get('max_temperature', 27.00)
    #     lowHum = websocketServer.globalData.get('min_humidity', 45.00)
    #     highHum = websocketServer.globalData.get('max_humidity', 55.00)
    #
    #     print("lowTemp: " + str(lowTemp) + ", highTemp: " + str(highTemp))
    #     print("lowHum: " + str(lowHum) + ", highHum: " + str(highHum))
    #
    #     # three plugs
    #     fanPlug = "192.168.3.29"
    #     humidifierPlug = "192.168.3.30"
    #     heaterPlug = "192.168.3.31"
    #
    #     # temperature control
    #     # if currentTemp >= highTemp:
    #     #     asyncio.run(plugs.turnOnPlug(fanPlug))
    #     #     print("turnOnPlug(fanPlug)")
    #     # elif currentTemp <= lowTemp:
    #     #     asyncio.run(plugs.turnOnPlug(heaterPlug))
    #     #     print("turnOnPlug(heaterPlug)")
    #     # else:
    #     #     asyncio.run(plugs.turnOffPlug(fanPlug))
    #     #     asyncio.run(plugs.turnOffPlug(heaterPlug))
    #     #     print("nice temperature")
    #     if currentTemp >= highTemp:
    #         await plugs.turnOnPlug(fanPlug)
    #         print("turnOnPlug(fanPlug)")
    #     elif currentTemp <= lowTemp:
    #         await plugs.turnOnPlug(heaterPlug)
    #         print("turnOnPlug(heaterPlug)")
    #     else:
    #         await plugs.turnOffPlug(fanPlug)
    #         await plugs.turnOffPlug(heaterPlug)
    #         print("nice temperature")
    #
    #     # humidity control
    #     # if currentHum >= highHum:
    #     #     # asyncio.run(plugs.turnOnPlug(fanPlug))
    #     #     print("high hum")
    #     # elif currentHum <= lowHum:
    #     #     asyncio.run(plugs.turnOnPlug(humidifierPlug))
    #     #     print("turnOnPlug(humidifierPlug)")
    #     # else:
    #     #     # asyncio.run(plugs.turnOffPlug(fanPlug))
    #     #     asyncio.run(plugs.turnOffPlug(humidifierPlug))
    #     #     print("nice humidity")
    #     if currentHum >= highHum:
    #         # asyncio.run(plugs.turnOnPlug(fanPlug))
    #         print("high hum")
    #     elif currentHum <= lowHum:
    #         await plugs.turnOnPlug(humidifierPlug)
    #         print("turnOnPlug(humidifierPlug)")
    #     else:
    #         # asyncio.run(plugs.turnOffPlug(fanPlug))
    #         await plugs.turnOffPlug(humidifierPlug)
    #         print("nice humidity")
    #
    #     # await asyncio.sleep(30)  # 设置每30秒执行一次控制逻辑

# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.create_task(controlTH())

    # 主循环
    # loop.run_forever()


# import plugs
# import getData
# import asyncio
# import websocketServer
#
# def controlTH():
#     global data
#
#     currentTemp = getData.getCurrentTemp()
#     currentHum = getData.getCurrentHum()
#
#     lowTemp = websocketServer.globalData.get('min_temperature', 24.00)
#     highTemp = websocketServer.globalData.get('max_temperature', 27.00)
#     lowHum = websocketServer.globalData.get('min_humidity', 45.00)
#     highHum = websocketServer.globalData.get('max_humidity', 55.00)
#
#     print("lowTemp: " + str(lowTemp) + ", highTemp: " + str(highTemp))
#     print("lowHum: " + str(lowHum) + ", highHum: " + str(highHum))
#
#     # three plugs
#     fanPlug = "192.168.3.29"
#     humidifierPlug = "192.168.3.30"
#     heaterPlug = "192.168.3.31"
#
#     # temperature control
#     if currentTemp >= highTemp:
#         asyncio.run(plugs.turnOnPlug(fanPlug))
#         print("turnOnPlug(fanPlug)")
#     elif currentTemp <= lowTemp:
#         asyncio.run(plugs.turnOnPlug(heaterPlug))
#         print("turnOnPlug(heaterPlug)")
#     else:
#         asyncio.run(plugs.turnOffPlug(fanPlug))
#         asyncio.run(plugs.turnOffPlug(heaterPlug))
#         print("nice temperature")
#
#     # humidity control
#     if currentHum >= highHum:
#         # asyncio.run(plugs.turnOnPlug(fanPlug))
#         print("high hum")
#     elif currentHum <= lowHum:
#         asyncio.run(plugs.turnOnPlug(humidifierPlug))
#         print("turnOnPlug(humidifierPlug)")
#     else:
#         # asyncio.run(plugs.turnOffPlug(fanPlug))
#         asyncio.run(plugs.turnOffPlug(humidifierPlug))
#         print("nice humidity")
#
# controlTH()
#
#
# # controlTH()
#
# # currentTemp = getData.getCurrentTemp()
# # currentHum = getData.getCurrentHum()
# #
# # lowTemp = websocketServer.min_temperature
# # highTemp = websocketServer.max_temperature
# # lowHum = websocketServer.min_humidity
# # highHum = websocketServer.max_humidity
# #
# # print("lowTemp: " + websocketServer.min_temperature + ", highTemp: " + websocketServer.max_temperature)
# # print("lowHum: " + websocketServer.min_humidity + ", highHum: " + websocketServer.max_humidity)
# #
# # # three plugs
# # fanPlug = "192.168.3.29"
# # humidifierPlug = "192.168.3.30"
# # heaterPlug = "192.168.3.31"
# #
# # # temperature control
# # if currentTemp >= websocketServer.max_temperature:
# #     asyncio.run(plugs.turnOnPlug(fanPlug))
# #     print("turnOnPlug(fanPlug)")
# # elif currentTemp <= websocketServer.min_temperature:
# #     asyncio.run(plugs.turnOnPlug(heaterPlug))
# #     print("turnOnPlug(heaterPlug)")
# # else:
# #     asyncio.run(plugs.turnOffPlug(fanPlug))
# #     asyncio.run(plugs.turnOffPlug(heaterPlug))
# #     print("nice temperature")
# #
# # # humidity control
# # if currentHum >= websocketServer.max_humidity:
# #     # asyncio.run(plugs.turnOnPlug(fanPlug))
# #     print("high hum")
# # elif currentHum <= websocketServer.min_humidity:
# #     asyncio.run(plugs.turnOnPlug(humidifierPlug))
# #     print("turnOnPlug(humidifierPlug)")
# # else:
# #     # asyncio.run(plugs.turnOffPlug(fanPlug))
# #     asyncio.run(plugs.turnOffPlug(humidifierPlug))
# #     print("nice humidity")