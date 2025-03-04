from fastapi import APIRouter, File, UploadFile
from faster_whisper import WhisperModel
from app.tts import synthesize_text  # Import TTS function

import os
import shutil

router = APIRouter()

# Load Whisper STT Model
model = WhisperModel("medium")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/transcribe_and_synthesize/")
async def transcribe_and_synthesize(file: UploadFile = File(...)):
    """
    Convert speech to text and then synthesize it back to speech.
    """
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    print(f"🔍 Processing uploaded file: {file_path}")

    # Transcribe audio
    segments, _ = model.transcribe(file_path)
    transcribed_text = " ".join(segment.text for segment in segments)

    print(f"✅ Transcription Completed: {transcribed_text}")

    # Convert Transcription to Speech
    audio_response = await synthesize_text(transcribed_text)

    return {
        "transcription": transcribed_text,
        "audio_file": audio_response["audio_file"]
    }
