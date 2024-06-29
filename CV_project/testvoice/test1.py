import requests
import os
from dotenv import load_dotenv
load_dotenv()
CHUNK_SIZE=1024

url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"

payload = {
    "text": "Hello world",
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
        "similarity_boost": 0.5,
        "stability": 0.5,
        "style": 0.5,
        "use_speaker_boost": True
    }
}
headers = {
    "xi-api-key": os.getenv('xi-api-key'),
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)
with open('output.wav', 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)
