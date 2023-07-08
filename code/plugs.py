from kasa import SmartPlug
import asyncio

# ip_address = "192.168.3.29"
# plug = SmartPlug(ip_address)

# plug = SmartPlug("192.168.3.30")
# asyncio.run(plug.update())
# plug.alias
#
# asyncio.run(plug.set_led(True))
# plug.led

async def turnOnPlug(Str):
    plug = SmartPlug(Str)
    await plug.update()
    print("Alias:", plug.alias)

    await plug.set_led(True)
    print("LED:", plug.led)

    await plug.turn_on()
    print("turn on")

async def turnOffPlug(Str):
    plug = SmartPlug(Str)
    await plug.update()
    print("Alias:", plug.alias)

    await plug.set_led(True)
    print("LED:", plug.led)

    await plug.turn_off()
    print("turn off")

# asyncio.run(turnOnPlug("192.168.3.30"))
# asyncio.run(turnOffPlug("192.168.3.30"))