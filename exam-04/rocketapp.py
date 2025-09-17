# file: rocketapp.py

from fastapi import FastAPI, HTTPException
import asyncio
import random

app = FastAPI(title="Asynchronous Rocket Launcher")

# เก็บ task ของจรวด (optional)
rockets = []

async def launch_rocket(student_id: str):
    """
    จำลองการบินของจรวด: random delay 1-2 วินาที
    """
    eta = round(random.uniform(1.0, 2.0), 2)
    print(f"Rocket {student_id} launched! ETA: {eta:.2f} seconds")
    await asyncio.sleep(eta)
    print(f"Rocket {student_id} reached destination after {eta:.2f} seconds")
    return eta

@app.get("/fire/{student_id}")
async def fire_rocket(student_id: str):
    # ตรวจสอบ student_id ต้องเป็นตัวเลข 10 หลัก
    if len(student_id) != 10 or not student_id.isdigit():
        raise HTTPException(status_code=400, detail="student_id must be 10 digits")

    # สร้าง background task
    task = asyncio.create_task(launch_rocket(student_id))
    rockets.append(task)

    # random เวลาที่ใช้ (ตรงกับเวลาที่จรวดจะถึง)
    time_to_target = round(random.uniform(1.0, 2.0), 2)

    # ส่ง response กลับทันที โดยไม่รอ task
    return {
        "message": f"Rocket {student_id} fired!",
        "time_to_target": time_to_target
    }

