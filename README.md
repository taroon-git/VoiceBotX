<<<<<<< HEAD
# VoiceBotX - Real-time Voice Chatbot

VoiceBotX is a **real-time voice chatbot** that utilizes **WebSockets** for bidirectional communication. It allows users to speak with the bot, convert speech to text using **Whisper STT** (Speech-to-Text), and get text responses converted back to speech using **Coqui TTS** (Text-to-Speech).

## Features
- **Real-time Voice Input/Output:** Users can interact with the bot using their voice in real-time.
- **Speech-to-Text:** Converts speech input into text using **Whisper**.
- **Text-to-Speech:** Converts the bot's text response back to speech using **Coqui TTS**.
- **WebSocket Communication:** Enables real-time interaction between the frontend and backend.

## Requirements
- Python 3.8+
- `whisper` (Speech-to-Text)
- `coqui-ai` (Text-to-Speech)
- `fastapi` (Backend framework)
- `uvicorn` (ASGI server for FastAPI)
- `websockets` (For real-time WebSocket communication)

## Installation

### Clone the Repository

```bash
git clone https://github.com/taroon-git/VoiceBotX.git
cd VoiceBotX
=======
# Voice Chatbot - FastAPI STT & TTS

## 📌 Project Overview
This project is a **Voice Chatbot** built using FastAPI that integrates:
- **Speech-to-Text (STT)** using OpenAI Whisper
- **Text-to-Speech (TTS)** using Coqui TTS
- **Real-time audio recording & transcription**
- **A simple frontend** to interact with STT & TTS functionalities

## 🚀 Features
- 🎤 **Speech-to-Text (STT)**: Converts spoken audio into text.
- 🔊 **Text-to-Speech (TTS)**: Converts text into speech.
- 🎙 **Real-time Speech Recognition**: Records and transcribes voice in real time.
- 🌐 **FastAPI Backend**: Handles API requests for STT & TTS.
- 🖥 **Interactive UI**: Allows users to record and listen to responses.

---

## 📁 Project Structure
```
📂 fastapi-stt
│── 📂 app
│   ├── 📜 main.py        # FastAPI entry point
│   ├── 📜 stt.py         # Speech-to-Text functionality
│   ├── 📜 tts.py         # Text-to-Speech functionality
│   ├── 📜 audio_utils.py # Audio processing utilities
│   ├── 📜 __init__.py    # Package initialization
│── 📂 static
│   ├── 🎨 index.html     # Frontend UI
│── 📂 generated_audio    # Stores TTS output files
│── 📂 recordings         # Stores recorded audio files
│── 📜 README.md          # Documentation
│── 📜 requirements.txt   # Dependencies
```

---

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone <repo-url>
cd fastapi-stt
```

### 2️⃣ Create a Virtual Environment & Install Dependencies
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Run the FastAPI Server
```sh
uvicorn app.main:app --reload
```
**Server running at:** `http://127.0.0.1:8000`

### 4️⃣ Access the UI
Open `http://127.0.0.1:8000` in your browser to use the Voice Chatbot.

---

## 🔄 Project Workflow
### **Step 1: Setup FastAPI & Project Structure**
- Created `main.py` as FastAPI entry point
- Added `stt.py` for speech-to-text processing
- Added `tts.py` for text-to-speech conversion

### **Step 2: Implement STT (Speech-to-Text)**
- Integrated OpenAI Whisper for transcription
- Handled file uploads & real-time recording

### **Step 3: Implement TTS (Text-to-Speech)**
- Integrated Coqui TTS for generating speech
- Saved generated audio for playback

### **Step 4: Build Frontend (HTML, JS)**
- Created `index.html` with UI for STT & TTS
- Used JavaScript to handle API calls

### **Step 5: Testing & Debugging**
- Fixed CORS issues
- Improved real-time response handling

### **Step 6: Final Deployment**
- Ensured the project runs smoothly
- Optimized for performance

---

## 🖥 UI Preview
(Add screenshot of the UI here)

---

## 🎯 API Endpoints
### 1️⃣ Speech-to-Text (STT)
**Endpoint:** `POST /transcribe/`
```sh
curl -X POST -F "file=@audio.wav" http://127.0.0.1:8000/transcribe/
```
_Response:_
```json
{
  "transcription": "Hello, how are you?"
}
```

### 2️⃣ Text-to-Speech (TTS)
**Endpoint:** `POST /tts/`
```sh
curl -X POST http://127.0.0.1:8000/tts/ -H "Content-Type: application/json" -d '{"text":"Hello!"}'
```
_Response:_
```json
{
  "audio_url": "/audio/output.wav"
}
```

### 3️⃣ Fetch Generated Audio
**Endpoint:** `GET /audio/output.wav`
```sh
curl -X GET http://127.0.0.1:8000/audio/output.wav
```

---

## 🤝 Contributing
Want to improve this project? Feel free to fork, modify, and submit a pull request! 🚀

---

## 📜 License
MIT License © 2025

>>>>>>> c5172fc (Initial commit)
