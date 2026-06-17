import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()


def speak(text):

    print("Jarvis:", text)

    engine.say(text)

    engine.runAndWait()


def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        audio = recognizer.listen(source)

    try:

        text = recognizer.recognize_google(audio)

        print("You:", text)

        return text.lower()

    except Exception:

        return ""

