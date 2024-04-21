import tortoise

def clone_voice(input_audio_path, output_voice_path):
    # Load the model
    tts_model = tortoise.TTSModel()

    # Load the input audio
    input_audio = tortoise.load_audio(input_audio_path)

    # Generate the voice
    generated_voice = tts_model.generate_voice(input_audio)

    # Save the generated voice
    tortoise.save_audio(generated_voice, output_voice_path)

if __name__ == "__main__":
    input_path = "MYNEWVOICE/1.wav"
    output_path = "MYNEWVOICE/res.wav"
    
    clone_voice(input_path, output_path)

# from gtts import gTTS

# def text_to_speech(text, output_path):
#     # Initialize the gTTS object
#     tts = gTTS(text=text, lang='en')
    
#     # Save the audio
#     tts.save(output_path)

# if __name__ == "__main__":
#     # Define the text you want to convert to speech
#     text_to_convert = "Your custom text here."
    
#     # Define the output audio file path
#     output_path = "voice/MYNEWVOICE/res.wav"
    
#     # Convert and save the text to speech
#     text_to_speech(text_to_convert, output_path)
