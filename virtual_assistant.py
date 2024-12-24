import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment, playback
import json
import constants as c

def readText(text_to_read):
    tts_output = gTTS(text=text_to_read, lang=c.TTS_LANGUAGE, slow=False)
    tts_output.save(c.AUDIO_OUTPUT_PATH)
    
    sound = AudioSegment.from_mp3(c.AUDIO_OUTPUT_PATH)
    spedup_sound = sound.speedup(playback_speed=c.PLAYBACK_SPEED)

    playback.play(spedup_sound)


def get_audio(first):
    recorder = sr.Recognizer()

    with sr.Microphone() as source:
        if first:
            print("Hey, I'm your virtual assistant. What can I do for you today?", end=" ")
            readText("Hey, I'm your virtual assistant. What can I do for you today?")
        else:
            readText("What else can i do for you today?")
        
        playback.play(AudioSegment.from_mp3("sounds/activate.mp3"))
        source_audio = recorder.listen(source)

    source_text = recorder.recognize_google(source_audio)
    print(source_text)

    return source_text

def import_jokes_from_json(filename):
    with open(filename, "r") as jokes_json:
        jokes_dict = json.load(jokes_json)
    
    return jokes_dict