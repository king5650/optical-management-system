import schedule
import time
from datetime import datetime
from whatsapp import send_whatsapp_message
from sms import send_sms  # Optional

def check_events():
    # Load events from JSON or database
    events = [
        {"name": "Christmas", "date": "2023-12-25", "message": "Merry Christmas! 🎄"},
        # Add more events
    ]

    today = datetime.now().strftime("%Y-%m-%d")
    for event in events:
        if event["date"] == today:
            send_whatsapp_message(event["message"])
            # send_sms(event["message"])  # Optional

# Schedule the event checker to run daily
schedule.every().day.at("12:11").do(check_events)

while True:
    schedule.run_pending()
    time.sleep(1)