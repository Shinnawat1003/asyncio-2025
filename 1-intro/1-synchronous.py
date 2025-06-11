import time
from datetime import datetime

def make_burger(student_id):
    start_time = datetime.now()
    print(f"[{start_time.strftime('%H:%M:%S')}] เริ่มทำเบอร์เกอร์ให้นักเรียนคนที่ {student_id} เวลา {start_time.strftime('%H:%M:%S')}")
    
    step_start = time.time()

    print(f"[{datetime.now().strftime('%H:%M:%S')}] 1. ทอดเบอร์เกอร์...")
    time.sleep(5)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] 2. ทอดไก่...")
    time.sleep(5)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] 3. ใส่ผักและชีส...")
    time.sleep(5)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] 4. ห่อเบอร์เกอร์...")
    time.sleep(5)

    step_end = time.time()
    end_time = datetime.now()

    elapsed = step_end - step_start
    print(f"[{end_time.strftime('%H:%M:%S')}] เสร็จแล้ว! เบอร์เกอร์ของนักเรียนคนที่ {student_id} ได้รับเวลา {end_time.strftime('%H:%M:%S')}")
    print(f"⏳ นักเรียนคนที่ {student_id} ใช้เวลาไปทั้งหมด {elapsed:.2f} วินาที\n")

def main():
    start = time.time()
    print(f"[{datetime.now().strftime('%H:%M:%S')}] เริ่มทำเบอร์เกอร์ให้นักเรียนทั้งหมด\n")

    for i in range(1, 6):
        make_burger(i)
    
    end = time.time()
    total_time = end - start
    print(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ ทำเบอร์เกอร์ครบทุกคนแล้ว")
    print(f" รวมเวลาทั้งหมด: {total_time:.2f} วินาที")

if __name__ == "__main__":
    main()
