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

def getCurrentTemp():
    # print("temperature = %.*f" % (2, temp))
    return round(temp, 2);

def getCurrentHum():
    # print("humidity = %.*f" % (2, hum))
    return round(hum, 2);
