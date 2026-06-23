# automation/whatsapp_selenium.py

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os



def send_whatsapp_message(phone_number: str, message: str, log_callback=print):
    """
    Sends a WhatsApp message using Selenium automation.
    """

    # Chrome options with user profile to keep login session 

    options = Options()

    user_data_dir = os.path.abspath("C:Users\falco\Desktop\system_optic\chrome_whatsapp_profile")
    options.add_argument(f"--user-data-dir={user_data_dir}")
    options.add_argument("--profile-directory=Default")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=9222")
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)


    try:
        log_callback("🌐 Launching browser...")
        driver = webdriver.Chrome(options=options)
        driver.get(f"https://wa.me/{phone_number}")

        time.sleep(5)

        # Click the "Continue to Chat" button
        try:
            continue_btn = driver.find_element(By.XPATH, "//a[contains(@href, 'web.whatsapp.com')]")
            continue_btn.click()
            log_callback("➡️ Clicked 'Continue to Chat'")
        except Exception:
            log_callback("⚠️ 'Continue to Chat' not found — already redirected?")

        # Wait for WhatsApp Web to load
        time.sleep(10)

        # Click "Use WhatsApp Web" (in case of mobile fallback page)
        try:
            use_web = driver.find_element(By.XPATH, "//a[text()='use WhatsApp Web']")
            use_web.click()
            time.sleep(5)
        except:
            pass

        # Wait and locate the message box
        message_box = None
        for _ in range(20):  # Retry for up to ~20 seconds
            try:
                message_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@data-tab='10']")
                break
            except:
                time.sleep(1)

        if not message_box:
            raise TimeoutException("Message box not found")

        # Type and send message
        message_box.send_keys(message)
        time.sleep(1)
        message_box.send_keys(u'\ue007')  # Press Enter
        log_callback(f"✅ Message sent to {phone_number}")

    except Exception as e:
        log_callback(f"❌ Error: {e}")

    # Don’t close browser — keep it open for reuse
    # driver.quit()  # Uncomment if you want it to auto-close
