import asyncio
from obniz import Obniz


async def onconnect(obniz):
    obniz.display.clear()
    obniz.display.print("Hello, world!")


obniz_id = input("obniz ID (e.g., 1234-5678): ")
obniz = Obniz(obniz_id)
obniz.onconnect = onconnect

asyncio.get_event_loop().run_forever()
