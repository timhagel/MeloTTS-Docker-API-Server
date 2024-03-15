# MeloTTS API Server

A quick easy way to access [MeloTTS](https://github.com/myshell-ai/MeloTTS) through REST API calls.

Assuming you have docker installed and setup

### Build

    git clone git@github.com:timhagel/melotts-api-server.git
    cd melotts-api-server
    docker build -t melotts-api-server .

### Run (English)

    docker run -p 8888:8080 -e DEFAULT_SPEED=1 -e DEFAULT_LANGUAGE=EN -e DEFAULT_SPEAKER_ID=EN-US  melotts-api-server

### Call API

**localhost:8888/convert/tts**

##### Use Environment Defaults

    {
        "text": "Put input here"
    }

Response : .wav

##### Customize (Everything except for "text" is optional)

    {
        "text": "input",
        "speed": "speed",
        "language": "language",
        "speaker_id": "speaker_id"
    }

## Acknowledgement

This just a API server for the awesome work of [MeloTTS](https://github.com/myshell-ai/MeloTTS) from [MyShell](https://github.com/myshell-ai)
