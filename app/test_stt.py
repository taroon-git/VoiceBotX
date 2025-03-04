from app.stt import transcribe_audio

# Test with the received audio file
audio_path = "received_audio.wav"
text = transcribe_audio(audio_path)

print(f"🎤 Transcription Result: {text}")
