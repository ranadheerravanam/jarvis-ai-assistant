import speech_recognition as sr
import whisper
import torch

print("CUDA Available:", torch.cuda.is_available())

# Load Whisper on CPU
model = whisper.load_model("small")
model = model.cpu()

recognizer = sr.Recognizer()

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

with open("voice.wav", "wb") as f:
    f.write(audio.get_wav_data())
result = model.transcribe(
    "voice.wav",
    language="en",
    fp16=False
)
print("\nYou said:")
print(result["text"])
