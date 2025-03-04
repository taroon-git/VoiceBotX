import asyncio
import websockets

async def send_audio():
    uri = "ws://127.0.0.1:8000/ws"
    async with websockets.connect(uri) as websocket:
        print("Connected to WebSocket server.")

        # Read and send audio file
        with open("received_audio.wav", "rb") as audio_file:
            data = audio_file.read()
            await websocket.send(data)
        
        print("Audio file sent.")

asyncio.run(send_audio())
