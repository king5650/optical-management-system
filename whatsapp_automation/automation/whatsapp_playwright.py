# # # automation/whatsapp_playwright.py

# # import asyncio
# # from playwright.sync_api import sync_playwright
# # import os

# # def send_whatsapp_message(phone_number: str, message: str, log_callback=print):
# #     try:
# #         log_callback("🌐 Launching browser (Playwright)...")

# #         with sync_playwright() as p:
# #             browser = p.chromium.launch(headless=False)

# #             # Create or reuse session
# #             storage_path = "automation/session_storage.json"
# #             context = (
# #                 browser.new_context(storage_state=storage_path)
# #                 if os.path.exists(storage_path)
# #                 else browser.new_context()
# #             )
# #             page = context.new_page()

# #             # Go to wa.me link
# #             # page.goto(f"https://web.whatsapp.com")
# #             page.goto(f"https://wa.me/{phone_number}")
# #             log_callback("➡️ Navigated to wa.me")

# #             # Click "Continue to Chat"
# #             page.wait_for_selector("a[href*='web.whatsapp.com']")
# #             page.click("a[href*='web.whatsapp.com']")

# #             # Wait for WhatsApp Web
# #             page.wait_for_url("**/web.whatsapp.com/**", timeout=30000)

# #             log_callback("🔓 Waiting for WhatsApp Web to load...")

# #             # Wait for the message box to appear
# #             page.wait_for_selector("div[contenteditable='true'][data-tab='10']", timeout=60000)
# #             input_box = page.query_selector("div[contenteditable='true'][data-tab='10']")

# #             # Send message
# #             input_box.fill(message)
# #             input_box.press("Enter")

# #             log_callback(f"✅ Message sent to {phone_number}")

# #             # Save login session
# #             context.storage_state(path=storage_path)

# #     except Exception as e:
# #         log_callback(f"❌ Error (Playwright): {e}")
# # automation/whatsapp_playwright.py

# import os
# import time
# from playwright.sync_api import sync_playwright

# def send_whatsapp_message(phone_number: str, message: str, log_callback=print):
#     try:
#         log_callback("🌐 Launching browser (Playwright)...")

#         with sync_playwright() as p:
#             browser = p.chromium.launch(headless=False)

#             # Session path
#             storage_path = "automation/session_storage.json"

#             # Reuse login session if available
#             if os.path.exists(storage_path):
#                 context = browser.new_context(storage_state=storage_path)
#                 # log_callback("🔐 Loaded existing session.")
#                 # Save login session for reuse
#                 os.makedirs(os.path.dirname(storage_path), exist_ok=True)
#                 context.storage_state(path=storage_path)
#                 log_callback("💾 Session state saved.")

#             else:
#                 context = browser.new_context()
#                 log_callback("🆕 Creating new session.")

#             page = context.new_page()

#             # Use direct WhatsApp Web link to avoid redirect issues
#             whatsapp_url = f"https://web.whatsapp.com/send?phone={phone_number}"
#             log_callback(f"➡️ Navigating to {whatsapp_url}...")
#             page.goto(whatsapp_url, timeout=60000)

#             log_callback("⏳ Waiting for WhatsApp Web to load...")

#             # Wait for chat box to be ready
#             input_box = page.wait_for_selector("div[contenteditable='true']", timeout=60000)
#             log_callback("💬 Chat input box detected.")

#             time.sleep(2)  # Allow DOM to stabilize

#             # Type and send the message
#             input_box.click()
#             input_box.fill(message)
#             input_box.press("Enter")
#             log_callback(f"✅ Message sent to {phone_number}")

#             # Save login session for reuse
#             context.storage_state(path=storage_path)
#             log_callback("💾 Session state saved.")

#             # Optional: Screenshot for debugging
#             # page.screenshot(path="automation/debug_last_send.png")

#     except Exception as e:
#         log_callback(f"❌ Error (Playwright): {e}")

# automation/whatsapp_playwright.py

import os
import time
from playwright.sync_api import sync_playwright

def send_whatsapp_message(phone_number: str, message: str, log_callback=print):
    try:
        log_callback("🌐 Launching browser (Playwright)...")

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)

            # Session path
            storage_path = "automation/session_storage.json"

            # Reuse login session if available
            if os.path.exists(storage_path):
                context = browser.new_context(storage_state=storage_path)
                log_callback("🔐 Loaded existing session.")
            else:
                context = browser.new_context()
                log_callback("🆕 Creating new session.")

            page = context.new_page()

            # Open WhatsApp chat directly using the web version
            whatsapp_url = f"https://web.whatsapp.com/send?phone={phone_number}"
            log_callback(f"➡️ Navigating to {whatsapp_url}...")
            page.goto(whatsapp_url, timeout=60000)

            log_callback("⏳ Waiting for WhatsApp Web to load...")

            # Wait for the message box to appear
            input_box = page.wait_for_selector("div[contenteditable='true']", timeout=60000)
            log_callback("💬 Chat input box detected.")

            time.sleep(2)  # Optional wait for stability

            input_box.click()
            input_box.fill(message)
            input_box.press("Enter")
            log_callback(f"✅ Message sent to {phone_number}")

            # ✅ Ensure folder exists before saving session 
            os.makedirs(os.path.dirname(storage_path), exist_ok=True)
            context.storage_state(path=storage_path)
            log_callback("💾 Session state saved.")

    except Exception as e:
        log_callback(f"❌ Error (Playwright): {e}")
