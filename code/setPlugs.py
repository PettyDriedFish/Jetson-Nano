import plugs
# import getData
import asyncio

# currentTemp = getData.getCurrentTemp()
# currentHum = getData.getCurrentHum()

currentTemp = 26
currentHum = 40

# set temperature
highTemp = 27
lowTemp = 24
# set humidity
highHum = 50
lowHum = 40

# 三个插头
fanPlug = "192.168.3.29"
humidifierPlug = "192.168.3.30"
heaterPlug = "192.168.3.31"


# temperature control
if currentTemp > highTemp:
    asyncio.run(plugs.turnOnPlug(fanPlug))
    print("The temperature is higher than the set maximum temperature")
elif currentTemp < lowTemp:
    asyncio.run(plugs.turnOnPlug(heaterPlug))
    print("The temperature is lower than the set minimum temperature")
else:
    asyncio.run(plugs.turnOffPlug(fanPlug))
    asyncio.run(plugs.turnOffPlug(heaterPlug))
    print("nice temperature")

# humidity control
if currentHum > highHum:
    asyncio.run(plugs.turnOnPlug(fanPlug))
    print("The humidity is higher than the set maximum humidity")
elif currentHum < lowHum:
    asyncio.run(plugs.turnOnPlug(humidifierPlug))
    print("The humidity is lower than the set minimum humidity")
else:
    asyncio.run(plugs.turnOffPlug(fanPlug))
    asyncio.run(plugs.turnOffPlug(humidifierPlug))
    print("nice humidity")