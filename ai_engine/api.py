from fastapi import FastAPI, UploadFile
import shutil
from ai_engine.audio.voice_detector import analyze_audio_call

app = FastAPI()

@app.get("/")
def home():
    return {"message": "SentinelCall AI Running"}

@app.post("/detect_audio_scam")

async def detect_audio(file: UploadFile):

    path = "temp_audio.wav"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = analyze_audio_call(path)

    return result