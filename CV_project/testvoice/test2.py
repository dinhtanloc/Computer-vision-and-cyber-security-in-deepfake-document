from elevenlabs.client import ElevenLabs
from elevenlabs import play

client = ElevenLabs(
  api_key="a8ece59d870df78353d9e9d554d2c766", # Defaults to ELEVEN_API_KEY
)

voice = client.clone(
    name="Alex",
    description="An old American male voice with a slight hoarseness in his throat. Perfect for news", # Optional
    files=["voice/MYNEWVOICE/a.m4a", "voice/MYNEWVOICE/b.m4a"],
)

audio = client.generate(text="Hi! I'm a cloned voice!", voice=voice)

play(audio)