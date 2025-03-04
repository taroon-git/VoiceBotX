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
