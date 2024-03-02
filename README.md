# MeloTTS API Server
A quick easy way to access [MeloTTS](https://github.com/myshell-ai/MeloTTS) through REST API calls.

Currently only locked to english with american accent. Easy fix if requested, or you can just change the hardcode speaker_ids before build if needed.

## Usage 
Assuming you have docker installed and setup
### Build
    git clone git@github.com:timhagel/melotts-api-server.git
    cd melotts-api-server
    docker build -t melotts-api-server .
 ### Run
    docker run -p 8888:8080 melotts-api-server
### Call API
**localhost:8888/text_to_speech**

    {
        "text": "Put input here"
    }
Response : en-us.wav

## ## Acknowledgement
This just a API server for the awesome work of [MeloTTS](https://github.com/myshell-ai/MeloTTS) from [MyShell](https://github.com/myshell-ai)
