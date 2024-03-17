# MeloTTS API Server

A quick easy way to access [MeloTTS](https://github.com/myshell-ai/MeloTTS) through REST API calls.

## Usage

Assuming you have docker installed and setup

### Build

    git clone git@github.com:timhagel/melotts-api-server.git
    cd melotts-api-server
    docker build -t melotts-api-server .

### Languages and Speakers

#### Language

- EN - English
- ES - Spainish
- FR - French
- ZH - Chinese
- JP - Japanese
- KR - Korean

#### Speaker IDs

- EN-US - American english accent
- EN-BR - British english accent
- EN_INDIA - Indian english accent
- EN-AU - Australian english accent
- EN-Default - Default english accent
- **Notice!** Currently only english accents are working, and other accents are returning an error. This dose not mean that other language do not work!

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

Response : .wav

## Acknowledgement

This just a API server for the awesome work of [MeloTTS](https://github.com/myshell-ai/MeloTTS) from [MyShell](https://github.com/myshell-ai)
