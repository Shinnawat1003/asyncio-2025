# example of waiting for the first task to complete
import asyncio
from random import random

# Coroutine to execute in a new task
async def task_coro(arg):
    value = random()
    await asyncio.sleep(value)
    print(f'task {arg} done with {value}')
    return value

# Main coroutine
async def main():
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    
    print('Done')
    
    
    first = done.pop()
    print(f'First completed task result: {first.result()}')


asyncio.run(main())