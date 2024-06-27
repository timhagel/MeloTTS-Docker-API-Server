import os
import uvicorn
from fastapi import FastAPI, Body, Depends
from pydantic import BaseModel
from fastapi.responses import FileResponse
from melo.api import TTS
from dotenv import load_dotenv
import tempfile

load_dotenv()
DEFAULT_SPEED = float(os.getenv("DEFAULT_SPEED"))
DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE")
DEFAULT_SPEAKER_ID = os.getenv("DEFAULT_SPEAKER_ID")
device = "auto"  # Will automatically use GPU if available


class TextModel(BaseModel):
    text: str
    speed: float = DEFAULT_SPEED
    language: str = DEFAULT_LANGUAGE
    speaker_id: str = DEFAULT_SPEAKER_ID


app = FastAPI()


def get_tts_model(body: TextModel):
    return TTS(language=body.language, device=device)


@app.post("/convert/tts")
async def create_upload_file(
    body: TextModel = Body(...), model: TTS = Depends(get_tts_model)
):
    speaker_ids = model.hps.data.spk2id

    print(os.path.basename(body.text))

    # Use a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        output_path = tmp.name
        model.tts_to_file(
            body.text, speaker_ids[body.speaker_id], output_path, speed=body.speed
        )

        # Return the audio file, ensure the file is not deleted until after the response is sent
        response = FileResponse(
            output_path, media_type="audio/mpeg", filename=os.path.basename(output_path)
        )

    return response


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
