import asyncio
import time
import aiohttp

student_id = "6610301003"   # ใช้รหัสนักศึกษา

async def fire_rocket(name: str, t0: float):
    url = f"http://172.16.2.117:8088/fire/{student_id}"
    start_time = time.perf_counter() - t0      # เวลาเริ่มสัมพัทธ์

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            # response ควรมี key: "time_to_target"
            time_to_target = float(data["time_to_target"])

    end_time = time.perf_counter() - t0        # เวลาเมื่อจบ
    return {
        "name": name,
        "start_time": start_time,
        "time_to_target": time_to_target,
        "end_time": end_time
    }

async def main():
    t0 = time.perf_counter()
    print("Rocket prepare to launch ...")

    # สร้าง task ยิง rocket 3 ลูกพร้อมกัน
    tasks = [
        asyncio.create_task(fire_rocket("Rocket-1", t0)),
        asyncio.create_task(fire_rocket("Rocket-2", t0)),
        asyncio.create_task(fire_rocket("Rocket-3", t0)),
    ]

    # รอทุก task เสร็จ
    results = await asyncio.gather(*tasks)

    # เรียงตามเวลาที่ถึงจุดหมาย (end_time)
    results.sort(key=lambda r: r["end_time"])

    print("Rockets fired:")
    for r in results:
        print(
            f"{r['name']} | start_time: {r['start_time']:.2f} sec "
            f"| time_to_target: {r['time_to_target']:.2f} sec "
            f"| end_time: {r['end_time']:.2f} sec"
        )

    # เวลารวม = end_time ที่มากที่สุด
    total_time = max(r["end_time"] for r in results)
    print(f"\nTotal time for all rockets: {total_time:.2f} sec")

if __name__ == "__main__":
    asyncio.run(main())

