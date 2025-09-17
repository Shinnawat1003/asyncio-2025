# ให้เขียนโปรแกรมหาจำนวนเฉพาะที่ ≤ n แบบ อะซิงโครนัส
# โปรแกรมต้องรองรับการคำนวณ หลายค่า n พร้อมกัน
# นักศึกษาต้องเติมโค้ดที่ทำการ หาจำนวนเฉพาะ และ สร้าง task

# Hint:
# 1. ฟังก์ชัน is_prime(num) → return True ถ้า num เป็น prime, False ถ้าไม่ใช่
# 2. ใน primes_up_to(n) → ใช้ loop หรือ list comprehension เพื่อหา prime numbers 2..n
# 3. ใช้ asyncio.create_task() เพื่อสร้าง task สำหรับแต่ละค่า n
# 4. ใช้ await เพื่อรอผลลัพธ์ของแต่ละ task ก่อนพิมพ์ผลลัพธ์

# Result:
# Primes <= 10: [2, 3, 5, 7]
# Primes <= 20: [2, 3, 5, 7, 11, 13, 17, 19]
# Primes <= 30: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

import asyncio
from typing import List

# ---------- 1. ตรวจสอบจำนวนเฉพาะ ----------
def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# ---------- 2. หา prime ≤ n แบบ async ----------
async def primes_up_to(n: int) -> List[int]:
    # คืน control เล็กน้อยเพื่อไม่ block event loop
    await asyncio.sleep(0)
    return [x for x in range(2, n + 1) if is_prime(x)]

# ---------- 3. main ----------
async def main():
    ns = [10, 20, 30]        # ค่า n หลายชุด
    tasks = []               # เก็บ task แต่ละตัว

    # 3.1 สร้าง task
    for n in ns:
        tasks.append(asyncio.create_task(primes_up_to(n)))

    # 3.2 รอและพิมพ์ผลลัพธ์แต่ละ task
    for n, t in zip(ns, tasks):
        primes = await t
        print(f"Primes <= {n}: {primes}")

# ---------- 4. เรียก main ----------
if __name__ == "__main__":
    asyncio.run(main())
