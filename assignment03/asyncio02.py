# example of running a coroutine
import asyncio
#define a coroutine
async def custom_coro():
    #await another
    await asyncio.sleep(1)
#main coroutine
async def main():
    #execute my custom coroutine
    await custom_coro()
#stat the coroutine program
asyncio.run(main())
