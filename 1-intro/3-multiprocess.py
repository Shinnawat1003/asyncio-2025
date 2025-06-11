import time
from multiprocessing import Process, current_process
from datetime import datetime

def make_burger(student_id):
    start_time = datetime.now()
    start_timestamp = time.time()

    print(f"[{start_time.strftime('%H:%M:%S')}] เริ่มทำเบอร์เกอร์ให้นักเรียนคนที่ {student_id} เวลา {start_time.strftime('%H:%M:%S')}")

    print(f"[{datetime.now().strftime('%H:%M:%S')}] 1. ทอดเบอร์เกอร์...")
    time.sleep(5)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] 2. ทอดไก่...")
    time.sleep(5)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] 3. ใส่ผักและชีส...")
    time.sleep(5)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] 4. ห่อเบอร์เกอร์...")
    time.sleep(5)

    end_time = datetime.now()
    end_timestamp = time.time()
    duration = end_timestamp - start_timestamp

    print(f"[{end_time.strftime('%H:%M:%S')}] ✅ เสร็จแล้ว! เบอร์เกอร์ของนักเรียนคนที่ {student_id} ได้รับเวลา {end_time.strftime('%H:%M:%S')}")
    print(f"⏳ นักเรียนคนที่ {student_id} ใช้เวลาไปทั้งหมด {duration:.2f} วินาที\n")

def main():
    start = time.time()
    print(f"[{datetime.now().strftime('%H:%M:%S')}] เริ่มกระบวนการทำเบอร์เกอร์ทั้งหมด\n")

    processes = []

    for i in range(1, 6):
        p = Process(target=make_burger, args=(i,))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    
    end = time.time()
    print(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ ทำเบอร์เกอร์ครบทุกคนแล้ว")
    print(f"🕒 รวมเวลาทั้งหมด: {end - start:.2f} วินาที")

if __name__ == "__main__":
    main()
