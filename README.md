# MeloTTS Docker API Server

A quick easy way to access [MeloTTS](https://github.com/myshell-ai/MeloTTS) through REST API calls.

## Usage

Assuming you have docker installed and setup

### Build
(This might take a bit because MeloTTS is a big dependency)
#### Local

    git clone git@github.com:timhagel/MeloTTS-Docker-API-Server.git
    cd MeloTTS-Docker-API-Server
    docker build -t timhagel/melotts-api-server .

#### Docker Hub

    docker pull timhagel/melotts-api-server
    
### Languages and Speakers

#### Language

- EN - English
- ES - Spanish
- FR - French
- ZH - Chinese
- JP - Japanese
- KR - Korean

#### Speaker IDs

- EN-US - American English accent
- EN-BR - British English accent
- EN_INDIA - Indian English accent
- EN-AU - Australian English accent
- EN-Default - Default English accent
- **Notice!** Currently only English accents are working, and other accents are returning an error. This does not mean that other languages do not work!

### Run (CPU) (English)

    docker run --name melotts-server -p 8888:8080 -e DEFAULT_SPEED=1 -e DEFAULT_LANGUAGE=EN -e DEFAULT_SPEAKER_ID=EN-Default timhagel/melotts-api-server

### Run (GPU) (English)
    
    docker run --name melotts-server -p 8888:8080 --gpus=all -e DEFAULT_SPEED=1 -e DEFAULT_LANGUAGE=EN -e DEFAULT_SPEAKER_ID=EN-Default timhagel/melotts-api-server

### Call API

**localhost:8888/convert/tts**

##### Use Environment Defaults

    {
        "text": "Put input here"
    }

Response: .wav

##### Customize (Everything except for "text" is optional)

    {
        "text": "input",
        "speed": "speed",
        "language": "language",
        "speaker_id": "speaker_id"
    }

Response: .wav

## Acknowledgement

This is just an API server for the awesome work of [MeloTTS](https://github.com/myshell-ai/MeloTTS) from [MyShell](https://github.com/myshell-ai)
