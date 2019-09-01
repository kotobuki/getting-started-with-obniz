import asyncio
from obniz import Obniz


async def onconnect(obniz):
    led = obniz.wired("LED", {"anode": 0, "cathode": 1})

    def read_state(state):
        print(state)

        if state == "push":
            led.on()
        else:
            led.off()

    obniz.switch.onchange = read_state


obniz_id = input("obniz ID (e.g., 1234-5678): ")
obniz = Obniz(obniz_id)
obniz.onconnect = onconnect

asyncio.get_event_loop().run_forever()
