# whatsapp_sender.py
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Setup
API_BASE = "http://localhost:8000/api"
driver = webdriver.Chrome()  # Or webdriver.Firefox()

def fetch_pending_messages():
    res = requests.get(f"{API_BASE}/messages/?status=pending")
    return res.json()

def update_recipient_status(recipient_id, status, error=None):
    data = {
        "status": status,
        "error_message": error
    }
    return requests.post(f"{API_BASE}/recipients/{recipient_id}/update/", json=data)

def send_message(contact, message):
    try:
        search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        search_box.clear()
        search_box.send_keys(contact)
        time.sleep(2)
        search_box.send_keys(Keys.ENTER)
        time.sleep(2)

        message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        return True, None
    except Exception as e:
        return False, str(e)

def run():
    driver.get("https://web.whatsapp.com")
    input("Scan QR code and press Enter to continue...")

    while True:
        messages = fetch_pending_messages()
        for msg in messages:
            for recipient in msg['recipients']:
                contact = recipient['patient']['contact']
                success, error = send_message(contact, msg['message'])
                status = 'sent' if success else 'failed'
                update_recipient_status(recipient['id'], status, error)
        time.sleep(60)  # Run every 60s

if __name__ == "__main__":
    run()
