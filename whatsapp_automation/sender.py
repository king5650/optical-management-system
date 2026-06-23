# sender.py
import asyncio
import logging
from playwright.async_api import async_playwright

WHATSAPP_WEB = "https://web.whatsapp.com/"
USER_DATA_DIR = "./chrome-data"

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s')
log = logging.info

async def send_whatsapp_message(number: str, message: str) -> bool:
    async with async_playwright() as p:
        browser = await p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False
        )
        page = await browser.new_page()
        await page.goto(WHATSAPP_WEB)

        try:
            await page.wait_for_selector('[contenteditable="true"][data-tab="3"]', timeout=60000)
        except:
            log("QR code not scanned or WhatsApp not ready.")
            return False

        try:
            # Search contact
            search_box = page.locator('[contenteditable="true"][data-tab="3"]')
            await search_box.click()
            await search_box.fill("")
            await asyncio.sleep(1.5)
            await search_box.fill(number)
            await asyncio.sleep(3)

            # Try to click contact using visible title
            contact = page.locator(f'//span[@title="{number}"]')
            await contact.wait_for(timeout=10000)
            await contact.click()
            await asyncio.sleep(2)

            # Message box
            message_box = page.locator('[contenteditable="true"][data-tab="10"]')
            await message_box.click()
            await message_box.fill(message)
            await message_box.press("Enter")
            await asyncio.sleep(1)

            log(f"✅ Message sent to {number}")
            return True

        except Exception as e:
            log(f"❌ Error sending message: {e}")
            return False

        finally:
            await browser.close()

def send_single_message(number, message) -> bool:
    return asyncio.run(send_whatsapp_message(number, message))
