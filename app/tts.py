from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse  
from pydantic import BaseModel
from TTS.api import TTS 
import os

router = APIRouter()

model_name = "tts_models/en/ljspeech/tacotron2-DDC"
tts = TTS(model_name).to("cpu")

AUDIO_DIR = "generated_audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

class TTSRequest(BaseModel):
    text: str

def synthesize_text(text: str) -> str:
    """
    It'll synthesize the given text into an audio file.
    Returns: The path to the generated audio file.
    """
    if not text.strip():
        raise ValueError("Text cannot be empty.")

    audio_path = os.path.join(AUDIO_DIR, "output.wav")
    tts.tts_to_file(text=text, file_path=audio_path)
    return audio_path

@router.post("/tts/")
async def generate_speech(request: TTSRequest):
    """
    API endpoint to generate speech from text.
    """
    try:
        audio_path = synthesize_text(request.text)
        return {"audio_url": f"/audio/output.wav"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"TTS Error: {str(e)}")

@router.get("/audio/{filename}")
async def get_audio(filename: str):
    """
    Audio file endpoint.
    """
    file_path = os.path.join(AUDIO_DIR, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="audio/wav")
    raise HTTPException(status_code=404, detail="Audio file not found")
