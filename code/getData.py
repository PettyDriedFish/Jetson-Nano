# Get the temperature and humidity of bme280
import time
import BME280

# set BME280
bme280 = BME280.BME280()
bme280.get_calib_param()
time.sleep(1)
print("bme280 T&H I2C address:0X76")
data = []
data = bme280.readData()
print(data)

# get temperature
temp = data[1]
print("temperature = %.*f"%(2, temp))
# get humidity
hum = data[2]
print("humidity = %.*f"%(2, hum))

# set temperature
highTemp = 27
lowTemp = 24
# set humidity
highHum = 50
lowHum = 40

# temperature control
if temp > highTemp:
    print("The temperature is higher than the set maximum temperature")
elif temp < lowTemp:
    print("The temperature is lower than the set minimum temperature")
else:
    print("nice temperature")
# humidity control
if hum > highHum:
    print("The humidity is higher than the set maximum humidity")
elif hum < lowHum:
    print("The humidity is lower than the set minimum humidity")
else:
    print("nice humidity")