from fastapi import FastAPI, File, UploadFile, Request
from fastapi.templating import Jinja2Templates
from faster_whisper import WhisperModel
from fastapi.responses import JSONResponse
import shutil
import os

app = FastAPI()

from app import stt, tts  

app.include_router(stt.router)
app.include_router(tts.router)

model = WhisperModel("medium")
print("✅ Whisper Model Loaded.")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

templates = Jinja2Templates(directory="app/templates") 

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    """
    Accepts an audio file from the user and transcribes it.
    """
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save the uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    print(f"🔍 Processing uploaded file: {file_path}")

    # Transcribe the audio
    segments, _ = model.transcribe(file_path)
    
    # Generate transcription
    transcribed_text = " ".join(segment.text for segment in segments)

    print(f"✅ Transcription Completed: {transcribed_text}")

    return JSONResponse(content={"transcription": transcribed_text})
