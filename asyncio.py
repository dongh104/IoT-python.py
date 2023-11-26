import asyncio
import time
import loop

async def say(what, when):
    print("process...1")
    await asyncio.sleep(0.2)
    print("process...2")
    await asyncio.sleep(0.2)
    print("process...3")
    await asyncio.sleep(0.2)

    print("process...main")
    await asyncio.sleep(when)
    print(what)


def saySync(what):
    time.sleep(1)
    print(what)


#saySync("Good Sync")

loop = asyncio.get_event_loop()
loop.run_until_complete(say('hello world', 1) )
loop.close()