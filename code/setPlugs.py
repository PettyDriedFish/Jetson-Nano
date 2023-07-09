import plugs
import getData
import asyncio

currentTemp = getData.getCurrentTemp()
currentHum = getData.getCurrentHum()

# currentTemp = 31.22
# currentHum = 35

# set temperature
highTemp = 27
lowTemp = 24
# set humidity
highHum = 50
lowHum = 40

# three plugs
fanPlug = "192.168.3.29"
humidifierPlug = "192.168.3.30"
heaterPlug = "192.168.3.31"


# temperature control
if currentTemp >= highTemp:
    asyncio.run(plugs.turnOnPlug(fanPlug))
    print("turnOnPlug(fanPlug)")
elif currentTemp <= lowTemp:
    asyncio.run(plugs.turnOnPlug(heaterPlug))
    print("turnOnPlug(heaterPlug)")
else:
    asyncio.run(plugs.turnOffPlug(fanPlug))
    asyncio.run(plugs.turnOffPlug(heaterPlug))
    print("nice temperature")

# humidity control
if currentHum >= highHum:
    # asyncio.run(plugs.turnOnPlug(fanPlug))
    print("high hum")
elif currentHum <= lowHum:
    asyncio.run(plugs.turnOnPlug(humidifierPlug))
    print("turnOnPlug(humidifierPlug)")
else:
    # asyncio.run(plugs.turnOffPlug(fanPlug))
    asyncio.run(plugs.turnOffPlug(humidifierPlug))
    print("nice humidity")
