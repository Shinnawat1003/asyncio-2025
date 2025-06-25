# Asynchronous breakfast
import asyncio
from time import sleep, time

async def make_coffee():
    print("Starting to make coffee...")
    await asyncio.sleep(5)  # 1+5 = 6 units of time?
    print("Coffee is ready!")

async def fry_eggs():
    print("Starting to fry eggs...")
    await asyncio.sleep(3)  # 1+3 = 4 units of time?
    print("Eggs are ready!")

async def main():
    start_time = time()
    
    # Run tasks concurrently
    await asyncio.gather(
        make_coffee(),
        fry_eggs()
    )
    
    total_time = time() - start_time
    print(f"Breakfast is ready in {total_time:.2f} seconds!")

asyncio.run(main())