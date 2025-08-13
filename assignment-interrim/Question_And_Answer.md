# Question
1. ถ้าสร้าง asyncio.create_task(*tasks) ที่ไม่มี await ที่ main() เกิดอะไรบ้าง
   1. Task จะถูกสร้างและเริ่มรัน ทันทีใน background แต่โค้ดหลักจะไม่รอให้ task เสร็จ → main อาจจบก่อน task ทำงานเสร็จ
   2. ถ้า event loop ปิด (เช่น main() return แล้ว asyncio.run() ปิด loop) → task ที่ยังไม่เสร็จจะถูก cancel อัตโนมัติ
   3. ผลลัพธ์จาก task จะ ไม่ถูกเก็บ และ exception ภายใน task จะไม่ถูกจับ → อาจได้ warning "Task exception was never retrieved"
2. ความแตกต่างระหว่าง asyncio.gather(*tasks) กับ asyncio.wait(tasks) คืออะไร
   1. gather รันพร้อมกันและคืนค่าเป็น ลิสต์ผลลัพธ์ตามลำดับ args เมื่อ await กลุ่มนั้นเสร็จทุกตัว
   2. gather (ค่าเริ่มต้น) ถ้างานใดพัง จะยกเลิกที่เหลือและ raise ทันที; หรือกำหนด retur n_exceptions=True เพื่อรวบ error กลับมาในลิสต์ได้
   3. ต้อง “แสดงผลทันทีที่เสร็จทีละตัว”: ใช้ wait(..., return_when=FIRST_COMPLETED) เพื่อสตรีมค่าที่เสร็จก่อนแบบ real‑time ตามตัวอย่าง iot-wait.py
3. สร้าง create_task() และ coroutine ของ http ให้อะไรต่างกัน
   1. การส่ง coroutine เข้า asyncio.create_task() จะ เริ่มรัน coroutine นั้นทันที และคืน Task object → เราสามารถเก็บไปใช้ต่อ, รอหลายอันพร้อมกัน, หรือยกเลิกได้
   2. การสร้าง coroutine เฉย ๆ (เช่น fetch(url)) จะได้ coroutine object ที่ ยังไม่รัน จนกว่าจะถูก await หรือส่งเข้าไปใน create_task()/gather()/wait()
   3. create_task() เหมาะกับงานที่ต้องรันไปพร้อมกับโค้ดอื่นโดยไม่ต้องรอทันที coroutine เปล่าเหมาะเมื่อจะรอให้มันเสร็จเลย (await) หรือเก็บไว้รันตอนที่เราพร้อม
