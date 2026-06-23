import pywhatkit as kit
import json

def load_contacts():
    try:
        with open("data/contacts.json", "r") as file:
            data = json.load(file)
            return data["contacts"]
    except Exception as e:
        print(f"Error loading contacts: {e}")
        return []

def send_whatsapp_message(message):
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return

    for contact in contacts:
        try:
            phone_number = contact["phone"]
            kit.sendwhatmsg_instantly(phone_number, message)
            print(f"Message sent to {contact['name']} at {phone_number}: {message}")
        except Exception as e:
            print(f"Error sending message to {contact['name']}: {e}")