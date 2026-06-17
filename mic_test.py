import speech_recognition as sr

print(sr.Microphone.list_microphone_names())

recognizer = sr.Recognizer()

recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 1

with sr.Microphone(device_index=4) as source:

    print("Speak now...")

    recognizer.adjust_for_ambient_noise(
        source,
        duration=1
    )

    audio = recognizer.listen(
        source,
        timeout=5,
        phrase_time_limit=8
    )

try:

    text = recognizer.recognize_google(audio)

    print("You said:", text)

except Exception as e:

    print("Error:", e)
