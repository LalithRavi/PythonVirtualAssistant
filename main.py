# USE THIS FOR TEXTUAL ASSISTANT
# print("Hey, I'm your virtual assistant. What can I do for you today?", end=" ")
# readText("Hey, I'm your virtual assistant. What can I do for you today?")
# playback.play(AudioSegment.from_mp3("sounds/activate.mp3"))
# source = input()

import pywhatkit
import random

import speech_recognition
import virtual_assistant as va
from pydub import AudioSegment, playback

first = True

try:
    source_text = va.get_audio(first)

    while not "bye" in source_text.lower():
        if "youtube" in source_text.lower():
            pywhatkit.playonyt(source_text)
        elif "joke" in source_text.lower():
            jokes_data = va.import_jokes_from_json("jokes.json")
            joke_id = random.randint(1, len(jokes_data))
            va.readText("Here's a joke for you!" + jokes_data[joke_id]["body"])
        else:
            pywhatkit.search(source_text)
        
        first = False
        
        source_text = va.get_audio(first)
except speech_recognition.exceptions.UnknownValueError:
    print("\nOops couldn't hear you", end=". ")
finally:
    print("Goodbye! Love you")
    va.readText("Goodbye! Love you \N{heart}")
    playback.play(AudioSegment.from_mp3("sounds/deactivate.mp3"))