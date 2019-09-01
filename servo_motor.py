import asyncio
from obniz import Obniz


async def onconnect(obniz):
    servo = obniz.wired("ServoMotor", {"signal": 2, "vcc": 3, "gnd": 4})

    def read_state(state):
        print(state)

        if state == "right":
            servo.angle(180)
        elif state == "left":
            servo.angle(0)

    obniz.switch.onchange = read_state


obniz_id = input("obniz ID (e.g., 1234-5678): ")
obniz = Obniz(obniz_id)
obniz.onconnect = onconnect

asyncio.get_event_loop().run_forever()
