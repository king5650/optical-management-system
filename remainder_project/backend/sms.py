from twilio.rest import Client
import json

def load_contacts():
    try:
        with open("data/contacts.json", "r") as file:
            data = json.load(file)
            return data["contacts"]
    except Exception as e:
        print(f"Error loading contacts: {e}")
        return []

def send_sms(message):
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return

    # Twilio credentials
    account_sid = "your_account_sid"
    auth_token = "your_auth_token"
    client = Client(account_sid, auth_token)

    for contact in contacts:
        try:
            phone_number = contact["phone"]
            message = client.messages.create(
                body=message,
                from_="+1234567890",  # Your Twilio number
                to=phone_number
            )
            print(f"SMS sent to {contact['name']} at {phone_number}: {message.sid}")
        except Exception as e:
            print(f"Error sending SMS to {contact['name']}: {e}")