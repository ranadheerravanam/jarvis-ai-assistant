import time

from whatsapp.manager import WhatsAppManager
from core.processor import process

wa = WhatsAppManager()

last_message = ""

print("=" * 60)
print("         JARVIS WHATSAPP STARTED")
print("=" * 60)

while True:

    try:

        message = wa.latest_message()

        if not message:
            time.sleep(1)
            continue

        message = message.strip()

        if message == last_message:
            time.sleep(1)
            continue

        last_message = message

        print("\nReceived:", message)

        # Only execute commands starting with "Jarvis"
        if not message.lower().startswith("jarvis"):
            continue

        command = message[6:].strip()

        print("Command:", command)

        reply = process(command)

        print("Reply:", reply)

        wa.send(str(reply))

        time.sleep(2)

    except KeyboardInterrupt:
        print("\nStopping Jarvis...")
        break

    except Exception as e:
        print("Error:", e)
        time.sleep(2)
