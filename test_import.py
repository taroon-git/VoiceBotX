# test_import.py
from faster_whisper import Whisper

print("Step 1: Import successful!")

# Load the model
model = Whisper("small")
print("Step 2: Model loaded successfully!")

# Dummy transcription test
segments, _ = model.transcribe("test.wav")
print("Step 3: Transcription process started!")

for segment in segments:
    print(f"Start: {segment.start}, End: {segment.end}, Text: {segment.text}")

print("Step 4: Transcription complete!")
