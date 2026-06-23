# import asyncio
# import os
# import json
# import time
# from urllib.parse import quote
# from playwright.async_api import async_playwright

# SESSION_FILE = "whatsapp_session.json"

# async def save_session(context):
#     storage = await context.storage_state()
#     with open(SESSION_FILE, "w", encoding="utf-8") as f:
#         json.dump(storage, f)
#     print("✅ Session saved.")

# async def load_session(playwright):
#     if os.path.exists(SESSION_FILE):
#         print("🔐 Loading existing WhatsApp session...")
#         browser = await playwright.chromium.launch(headless=False)
#         context = await browser.new_context(storage_state=SESSION_FILE)
#     else:
#         print("📷 No saved session found. Login will be required.")
#         browser = await playwright.chromium.launch(headless=False)
#         context = await browser.new_context()
#     return browser, context

# async def send_whatsapp_message(phone_number, message, media_path=None):
#     async with async_playwright() as p:
#         browser, context = await load_session(p)
#         page = await context.new_page()

#         # Open WhatsApp Web
#         print(f"🌐 Navigating to WhatsApp Web for {phone_number}...")
#         await page.goto(f"https://web.whatsapp.com/send?phone={phone_number}&text={quote(message)}")

#         # Wait for chat or QR
#         try:
#             await page.wait_for_selector("canvas", timeout=5000)
#             print("📷 Waiting for login via QR code...")
#             await page.wait_for_selector("._3ndVb", timeout=60000)  # Chat container
#             await save_session(context)
#         except:
#             print("✅ Already logged in or QR skipped.")

#         # Send text message
#         try:
#             await page.wait_for_selector("div[title='Type a message']", timeout=60000)
#             await page.keyboard.press("Enter")
#             print(f"✅ Message sent to {phone_number}")
#         except Exception as e:
#             print(f"❌ Failed to send message: {e}")

#         # Send media if provided
#         if media_path and os.path.exists(media_path):
#             try:
#                 print("📎 Sending media...")
#                 await page.click("span[data-icon='clip']")
#                 file_input = await page.query_selector("input[type='file']")
#                 await file_input.set_input_files(media_path)
#                 await asyncio.sleep(2)
#                 await page.click("span[data-icon='send']")
#                 print(f"✅ Media sent to {phone_number}")
#             except Exception as e:
#                 print(f"❌ Failed to send media: {e}")

#         await save_session(context)
#         await browser.close()

# if __name__ == "__main__":
#     phone = "+237680785677"
#     message = "Hello from Playwright automation 🚀"
#     media = None  # Example: "image.jpg"
#     asyncio.run(send_whatsapp_message(phone, message, media))



import asyncio
import os
import json
import time
from urllib.parse import quote
from playwright.async_api import async_playwright

# SESSION_FILE = "whatsapp_session.json"

# async def save_session(context):
#     storage = await context.storage_state()
#     with open(SESSION_FILE, "w", encoding="utf-8") as f:
#         json.dump(storage, f)
#     print("✅ Session saved.")

# async def load_session(playwright):
#     if os.path.exists(SESSION_FILE):
#         print("🔐 Loading existing WhatsApp session...")
#         browser = await playwright.chromium.launch(headless=False)
#         context = await browser.new_context(storage_state=SESSION_FILE)
#     else:
#         print("📷 No saved session found. Login will be required.")
#         browser = await playwright.chromium.launch(headless=False)
#         context = await browser.new_context()
#     return browser, context

# async def send_whatsapp_message(phone_number, message, media_path=None):
#     async with async_playwright() as p:
#         browser, context = await load_session(p)
#         page = await context.new_page()

#         # Open WhatsApp Web
#         print(f"🌐 Navigating to WhatsApp Web for {phone_number}...")
#         await page.goto(f"https://web.whatsapp.com/send?phone={phone_number}&text={quote(message)}")

#         # Wait for chat or QR
#         try:
#             await page.wait_for_selector("canvas", timeout=5000)
#             print("📷 Waiting for login via QR code...")
#             await page.wait_for_selector("._3ndVb", timeout=60000)  # Chat container
#             await save_session(context)
#         except:
#             print("✅ Already logged in or QR skipped.")

#         # Send text message
#         try:
#             await page.wait_for_selector("div[title='Type a message']", timeout=60000)
#             await page.keyboard.press("Enter")
#             print(f"✅ Message sent to {phone_number}")
#         except Exception as e:
#             print(f"❌ Failed to send message: {e}")

#         # Send media if provided
#         if media_path and os.path.exists(media_path):
#             try:
#                 print("📎 Sending media...")
#                 await page.click("span[data-icon='clip']")
#                 file_input = await page.query_selector("input[type='file']")
#                 await file_input.set_input_files(media_path)
#                 await asyncio.sleep(2)
#                 await page.click("span[data-icon='send']")
#                 print(f"✅ Media sent to {phone_number}")
#             except Exception as e:
#                 print(f"❌ Failed to send media: {e}")

#         await save_session(context)
#         await browser.close()

# if __name__ == "__main__":
#     phone = "+237680785677"
#     message = "Hello from Playwright automation 🚀"
#     media = None  # Example: "image.jpg"
#     asyncio.run(send_whatsapp_message(phone, message, media))


# import asyncio
# import os
# import json
# from urllib.parse import quote
# from datetime import datetime
# from playwright.async_api import async_playwright

# SESSION_FILE = "whatsapp_session.json"
# CHECK_STRING = "STRING TO SEARCH"  # For duplicate message detection
# WHATSAPP_WEB = "https://web.whatsapp.com/"

# class WhatsAppAutomation:
#     def __init__(self, headless=False):
#         self.headless = headless
#         self.browser = None
#         self.context = None
#         self.page = None

#     async def save_session(self):
#         storage = await self.context.storage_state()
#         with open(SESSION_FILE, "w", encoding="utf-8") as f:
#             json.dump(storage, f)
#         print(f"[{datetime.now()}] ✅ Session saved")

#     async def load_session(self, playwright):
#         if os.path.exists(SESSION_FILE):
#             print(f"[{datetime.now()}] 🔐 Loading existing session")
#             self.browser = await playwright.chromium.launch(headless=self.headless)
#             self.context = await self.browser.new_context(storage_state=SESSION_FILE)
#         else:
#             print(f"[{datetime.now()}] 📷 No session found - QR login required")
#             self.browser = await playwright.chromium.launch(headless=self.headless)
#             self.context = await self.browser.new_context()
#         self.page = await self.context.new_page()

#     async def ensure_logged_in(self):
#         try:
#             await self.page.wait_for_selector("canvas", timeout=5000)
#             print(f"[{datetime.now()}] 🔍 QR code detected - waiting for scan")
#             await self.page.wait_for_selector('//div[@contenteditable="true"][@data-tab="3"]', timeout=60000)
#             await self.save_session()
#         except:
#             print(f"[{datetime.now()}] ✅ Already logged in")

#     async def find_contact(self, phone=None, name=None):
#         search_box = self.page.locator('//div[@contenteditable="true"][@data-tab="3"]')
#         await search_box.click()
#         await search_box.fill("")
        
#         # Try phone first, fall back to name
#         search_term = phone if phone else name
#         await search_box.fill(search_term)
#         await asyncio.sleep(3)

#         # Check for no results
#         if await self.page.locator('text="No results found"').count() > 0:
#             raise Exception(f"No contact found for {phone or name}")

#         # Try locating contact
#         contact_locator = None
#         if phone:
#             contact_locator = self.page.locator(f'//span[@title="{phone}"]')
#         if name and (not contact_locator or await contact_locator.count() == 0):
#             contact_locator = self.page.locator(f'//span[@title="{name}"]')

#         if not contact_locator or await contact_locator.count() == 0:
#             raise Exception(f"Could not find contact {phone or name}")

#         await contact_locator.first.click()
#         await self.page.wait_for_selector('//div[@contenteditable="true"][@data-tab="10"]', timeout=60000)
#         await asyncio.sleep(2)

#     async def check_duplicate_message(self):
#         if await self.page.get_by_text(CHECK_STRING).count() > 0:
#             print(f"[{datetime.now()}] ⚠️ Message already sent")
#             return True
#         return False

#     async def send_text_message(self, message):
#         message_box = self.page.locator('//div[@contenteditable="true"][@data-tab="10"]')
#         await message_box.click()
#         await message_box.fill(message)
#         await message_box.press("Enter")
#         await asyncio.sleep(4)

#         # Verify delivery
#         last_msg = self.page.locator('.message-out').last
#         if await last_msg.count() > 0:
#             last_msg_text = await last_msg.inner_text()
#             if message in last_msg_text:
#                 print(f"[{datetime.now()}] ✅ Message verified")
#                 return True
        
#         print(f"[{datetime.now()}] ⚠️ Message may not have sent")
#         return False

#     async def send_media(self, media_path):
#         if not os.path.exists(media_path):
#             raise FileNotFoundError(f"Media file not found: {media_path}")

#         print(f"[{datetime.now()}] 📎 Attaching media")
#         await self.page.click("span[data-icon='clip']")
#         file_input = await self.page.query_selector("input[type='file']")
#         await file_input.set_input_files(media_path)
#         await asyncio.sleep(2)
#         await self.page.click("span[data-icon='send']")
#         print(f"[{datetime.now()}] ✅ Media sent")

#     async def send_message(self, phone=None, name=None, message=None, media_path=None):
#         try:
#             async with async_playwright() as playwright:
#                 await self.load_session(playwright)
                
#                 # Option 1: Direct message URL (faster when it works)
#                 if phone and message:
#                     url = f"{WHATSAPP_WEB}send?phone={phone}&text={quote(message)}"
#                     print(f"[{datetime.now()}] 🌐 Opening direct message URL")
#                     await self.page.goto(url)
#                     await self.ensure_logged_in()
                
#                 # Option 2: Manual contact search (more reliable for names)
#                 else:
#                     await self.page.goto(WHATSAPP_WEB)
#                     await self.ensure_logged_in()
#                     await self.find_contact(phone, name)

#                 # Check for duplicates
#                 if await self.check_duplicate_message():
#                     return False

#                 # Send text message (if not already pre-filled in URL)
#                 if message and (not phone or not url):
#                     if not await self.send_text_message(message):
#                         return False

#                 # Send media if provided
#                 if media_path:
#                     await self.send_media(media_path)

#                 await self.save_session()
#                 return True

#         except Exception as e:
#             print(f"[{datetime.now()}] ❌ Error: {str(e)}")
#             return False
#         finally:
#             if self.browser:
#                 await self.browser.close()

# # Example usage
# async def main():
#     wa = WhatsAppAutomation(headless=False)
    
#     # Send by phone number with media
#     await wa.send_message(
#         phone="+1234567890",
#         message="Hello from the automated sender!",
#         # media_path="example.jpg"
#     )
    
#     # Send by contact name only
#     await wa.send_message(
#         name="Shafai",
#         message="Another test message"
#     )

# if __name__ == "__main__":
#     asyncio.run(main())



import asyncio
import os
from urllib.parse import quote
from datetime import datetime
from playwright.async_api import async_playwright

PROFILE_DIR = os.path.join(os.getcwd(), "profiles", "default")  # persistent profile storage
CHECK_STRING = "STRING TO SEARCH"  # For duplicate message detection
WHATSAPP_WEB = "https://web.whatsapp.com/"

class WhatsAppAutomation:
    def __init__(self, headless=False, profile_dir=PROFILE_DIR):
        self.headless = headless
        self.profile_dir = profile_dir
        self.browser = None
        self.context = None
        self.page = None

    async def load_session(self, playwright):
        """Load or create a persistent browser profile"""
        print(f"[{datetime.now()}] 🌐 Launching browser with profile: {self.profile_dir}")
        self.context = await playwright.chromium.launch_persistent_context(
            user_data_dir=self.profile_dir,
            headless=self.headless,
            args=["--start-maximized"]
        )
        self.page = await self.context.new_page()

    async def ensure_logged_in(self):
        """Ensure that user is logged in, else wait for QR scan"""
        try:
            await self.page.wait_for_selector("canvas", timeout=5000)
            print(f"[{datetime.now()}] 🔍 QR code detected - waiting for scan")
            await self.page.wait_for_selector('//div[@contenteditable="true"][@data-tab="3"]', timeout=60000)
            print(f"[{datetime.now()}] ✅ Login successful, session stored in profile")
        except:
            print(f"[{datetime.now()}] ✅ Already logged in")

    async def find_contact(self, phone=None, name=None):
        search_box = self.page.locator('//div[@contenteditable="true"][@data-tab="3"]')
        await search_box.click()
        await search_box.fill("")

        # Try phone first, fallback to name
        search_term = phone if phone else name
        await search_box.fill(search_term)
        await asyncio.sleep(3)

        if await self.page.locator('text="No results found"').count() > 0:
            raise Exception(f"No contact found for {phone or name}")

        contact_locator = None
        if phone:
            contact_locator = self.page.locator(f'//span[@title="{phone}"]')
        if name and (not contact_locator or await contact_locator.count() == 0):
            contact_locator = self.page.locator(f'//span[@title="{name}"]')

        if not contact_locator or await contact_locator.count() == 0:
            raise Exception(f"Could not find contact {phone or name}")

        await contact_locator.first.click()
        await self.page.wait_for_selector('//div[@contenteditable="true"][@data-tab="10"]', timeout=60000)
        await asyncio.sleep(2)

    async def check_duplicate_message(self):
        if await self.page.get_by_text(CHECK_STRING).count() > 0:
            print(f"[{datetime.now()}] ⚠️ Message already sent")
            return True
        return False

    async def send_text_message(self, message):
        message_box = self.page.locator('//div[@contenteditable="true"][@data-tab="10"]')
        await message_box.click()
        await message_box.fill(message)
        await message_box.press("Enter")
        await asyncio.sleep(4)

        last_msg = self.page.locator('.message-out').last
        if await last_msg.count() > 0:
            last_msg_text = await last_msg.inner_text()
            if message in last_msg_text:
                print(f"[{datetime.now()}] ✅ Message verified")
                return True

        print(f"[{datetime.now()}] ⚠️ Message may not have sent")
        return False

    async def send_media(self, media_path):
        if not os.path.exists(media_path):
            raise FileNotFoundError(f"Media file not found: {media_path}")

        print(f"[{datetime.now()}] 📎 Attaching media")
        await self.page.click("span[data-icon='clip']") 
        file_input = await self.page.query_selector("input[type='file']")
        await file_input.set_input_files(media_path)
        await asyncio.sleep(2)
        await self.page.click("span[data-icon='send']")
        print(f"[{datetime.now()}] ✅ Media sent")

    async def send_message(self, phone=None, name=None, message=None, media_path=None):
        try:
            async with async_playwright() as playwright:
                await self.load_session(playwright)

                # Option 1: Direct message URL
                if phone and message:
                    url = f"{WHATSAPP_WEB}send?phone={phone}&text={quote(message)}"
                    print(f"[{datetime.now()}] 🌐 Opening direct message URL")
                    await self.page.goto(url)
                    await self.ensure_logged_in()

                # Option 2: Manual contact search
                else:
                    await self.page.goto(WHATSAPP_WEB)
                    await self.ensure_logged_in()
                    await self.find_contact(phone, name)

                if await self.check_duplicate_message():
                    return False

                if message and (not phone):
                    if not await self.send_text_message(message):
                        return False

                if media_path:
                    await self.send_media(media_path)

                return True

        except Exception as e:
            print(f"[{datetime.now()}] ❌ Error: {str(e)}")
            return False
        finally:
            # ✅ Persistent context: don’t close it fully
            if self.page and not self.page.is_closed():
                await self.page.close()
            # ⚠️ Don't close self.context here (keeps session alive)


# Example usage
async def main():
    wa = WhatsAppAutomation(headless=False)

    await wa.send_message(
        phone="+1234567890",
        message="Hello from persistent profile!"
    )

    await wa.send_message(
        name="Shafai",
        message="This should also work without scanning QR again"
    )

if __name__ == "__main__":
    asyncio.run(main())
