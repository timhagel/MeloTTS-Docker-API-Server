from fastapi import FastAPI, Body
from pydantic import BaseModel
from fastapi.responses import FileResponse
from melo.api import TTS

speed = 1.0
device = 'auto' # Will automatically use GPU if available

class TextModel(BaseModel):
    text: str

app = FastAPI()

@app.post("/text_to_speech")
async def create_upload_file(body: TextModel = Body(...)):
    model = TTS(language='EN', device=device)
    speaker_ids = model.hps.data.spk2id

    output_path = 'en-us.wav'
    model.tts_to_file(body.text, speaker_ids['EN-US'], output_path, speed=speed)

    # Return the audio file
    return FileResponse("en-us.wav", media_type="audio/mpeg", filename="en-us.wav")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)