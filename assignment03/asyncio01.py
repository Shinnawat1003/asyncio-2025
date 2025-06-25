# check the type of a corutine
import asyncio
#define a coroutine
async def custom_coro():
    #await another coroutine
    await asyncio.sleep(1)
#create the corutine
coro = custom_coro()
#check the type of the corutine
print(type(coro))