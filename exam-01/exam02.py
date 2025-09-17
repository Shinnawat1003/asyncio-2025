# Hint:
# แก้โค้ดให้สามารถรัน หลาย task พร้อมกัน ได้ถูกต้อง
# Result:
# Processing data
# Processing data
# Processing data
# Processing data
# Processing data

import asyncio

async def fetch_data():
    await asyncio.sleep(2)
    return "data"

async def process():
    data = await fetch_data()
    print("Processing", data)

async def main():
    await asyncio.gather(*(process() for _ in range(5)))

if __name__ == "__main__":
    asyncio.run(main())
