from whatsapp.manager import WhatsAppManager

wa = WhatsAppManager()

while True:

    msg = wa.latest_message()

    print(msg)

    command = input("Reply: ")

    wa.send(command)
