from playsound import playsound

# playsound("sounds/tts_output_spedup.mp3")
print(" ".join(["ffmpeg", "-i", "sounds/tts_output.mp3", "-filter:a", "atempo=1.5", "sounds/tts_output_spedup.mp3"]))