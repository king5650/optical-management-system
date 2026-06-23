# import asyncio
# from playwright.async_api import async_playwright
# import csv
# from datetime import datetime
# import random

# # WhatsApp Web URL
# WHATSAPP_WEB = "https://web.whatsapp.com/"

# # Message components
# HELLO = "Hi "  # Greeting to start the message
# MEET_AND_GREET = ", hope I find you well\n\n"  # Contextual intro
# BODY = "(whatever message you want to send)"  # Main message body page

# # String to search in previous messages to avoid duplicates
# CHECK_STRING = "STRING TO SEARCH"

# # Input file containing leads (CSV format)
# FILE_TO_OPEN = "whatsapp_automation\leads.csv"

# # Dictionary to track statistics during execution
# stats = {
#     "sent": 0,  # Number of successfully sent messages
#     "failed": 0,  # Number of failed message attempts
#     "without_whatsapp": [],  # Leads without WhatsApp
#     "existent_chat": []  # Leads who already received the message
# }

# # Logs a message with a timestamp
# def log(message):
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Current time
#     print(f"[{timestamp}] {message}")  # Print the formatted log message

# # Formats a name by removing unnecessary characters and capitalizing it
# def name_formatter(name_and_surname):
#     try:
#         # Extract the first "word" from the name (ignores additional parts)
#         name = name_and_surname.split()[0]
#         # Replace underscores, convert to lowercase, and capitalize
#         return name.replace("_", " ").lower().title()
#     except IndexError:
#         # If the name is empty or malformed, return it as is
#         return name_and_surname

# # Sends a message to a specified phone number using WhatsApp Web
# # async def send_message(page, number, message, name, full_name):
# #     try:
# #         # Step 1: Search for the number in WhatsApp search box
# #         # await page.fill('div[data-testid="chat-list-search"]', number)
# #         # await page.wait_for_timeout(2000)  # Wait for results to load value
# #         await page.fill('div[aria-label="Search input textbox"]', number)
# #         # await page.wait_for_timeout( timeout=60000)
# #         # Step 2: Check if the contact exists and click to open chat
# #         contact = await page.locator('div[data-testid="cell-frame-container"]').first()
# #         await contact.click()

# #         # Step 3: Check if the message has already been sent
# #         elementi_messaggi = await page.locator(f'text="{CHECK_STRING}"').count()
# #         if elementi_messaggi > 0:
# #             log(f"{name} already received the message.")  # Log and return
# #             stats["existent_chat"].append((name, number))  # Add to stats
# #             return False

# #         # Step 4: Locate the message input field
# #         message_field = await page.locator('div[title="Write message"]').first()
# #         if not message_field:
# #             # Raise an error if the input field is not found (e.g., blocked contact)
# #             raise Exception("Message field not found, possibly blocked.")

# #         # Step 5: Type the message and press Enter to send
# #         await message_field.type(message)  # Enter the full message
# #         await message_field.press("Enter")  # Send the message
# #         log(f"Successfully sent message to {full_name}.")  # Log success
# #         stats["sent"] += 1  # Update success stats
# #         return True
# #     except Exception as e:
# #         # Handle any exceptions during message sending
# #         log(f"Error sending message to {full_name}: {e}")
# #         stats["failed"] += 1  # Update failure stats
# #         return False
# async def send_message(page, number, message, name, full_name):
#     try:
#         # Clear and search for the number
#         search_box = page.locator('div[aria-label="Search input textbox"]')
#         await search_box.click()
#         await search_box.fill('')  # Clear first
#         await search_box.fill(number)
#         await asyncio.sleep(2)  # Wait for search results

#         # Check if "No results found" appears
#         no_results = page.locator('text=No results found')
#         if await no_results.count() > 0:
#             log(f"No WhatsApp account found for {full_name} ({number})")
#             stats["without_whatsapp"].append((name, number))
#             return False

#         # Improved contact selection - wait for the specific contact element
#         try:
#             # Wait for the contact to appear in search results
#             # contact = page.locator(f'div[data-testid="Chat list"] >> text=+{number}')
#             # await contact.wait_for(timeout=10000)
#             # await contact.click()
#             # More reliable contact selection
#             contact = page.locator('div[data-testid="listitem"]').first
#             await contact.wait_for(timeout=10000)
#             await contact.click()

#             # Wait for message input instead of unstable selector
#             await page.wait_for_selector('div[title="Type a message"]', timeout=15000)
                        
                        
#             # Wait for chat pane to load completely
#             await page.wait_for_selector('div[data-testid="x12lumcd"]', timeout=15000)
#             await asyncio.sleep(2)  # Additional safety delay
#         except Exception as e:
#             log(f"Failed to open chat for {full_name}: {str(e)}")
#             stats["failed"] += 1
#             return False

#         # Check for existing message
#         if await page.get_by_text(CHECK_STRING).count() > 0:
#             log(f"{name} already received the message.")
#             stats["existent_chat"].append((name, number))
#             return False

#         # Focus and send message
#         message_box = page.locator('div[title="Type a message"]')
#         await message_box.click()
#         await message_box.fill(message)
#         await message_box.press("Enter")
#         await asyncio.sleep(1)  # Wait for message to send

#         # Verify message was sent
#         last_msg = page.locator('.message-out').last
#         if await last_msg.count() > 0:
#             last_msg_text = await last_msg.inner_text()
#             if message in last_msg_text:
#                 log(f"Successfully sent message to {full_name}.")
#                 stats["sent"] += 1
#                 return True
        
#         log(f"Message may not have sent to {full_name}")
#         stats["failed"] += 1
#         return False

#     except Exception as e:
#         log(f"Error sending to {full_name}: {str(e)}")
#         stats["failed"] += 1
#         return False
# # Main function to orchestrate message sending
# async def main():
#     # Initialize Playwright and launch the browser in persistent mode
#     async with async_playwright() as p:
#         browser = await p.chromium.launch_persistent_context(
#             user_data_dir="/home/dario/.config/google-chrome",  # Use existing login session
#             headless=False  # Run browser in visible mode for debugging
#         )
#         page = await browser.new_page()  # Create a new page (tab)
#         await page.goto(WHATSAPP_WEB)  # Open WhatsApp Web

#         # Wait for the user to scan the QR Code
#         log("Scan WhatsApp Web QR Code to continue...")
#         # await page.wait_for_selector('div[data-testid="chat-list-search"]')  # Ensure successful login
#         await page.wait_for_selector('div[aria-label="Search input textbox"]', timeout=60000)
#         log("QR Code successfully scanned!")  # Log success

#         # Open the leads CSV file
#         with open(FILE_TO_OPEN, newline='') as csvfile:
#             reader = csv.reader(csvfile)  # Read the CSV file
#             contacts = [row for row in reader]  # Convert rows to a list
        
#         # Iterate over the contacts and send messages
#         for lead in contacts:
#             try:
#                 # Extract name and number from the current lead
#                 name = name_formatter(lead[0])  # Format the name
#                 number = lead[1]  # Extract the phone number

#                 # Compose the full message
#                 message = HELLO + name + MEET_AND_GREET + BODY

#                 # Send the message and add a random delay
#                 await send_message(page, number, message, name, lead[0])
#                 await asyncio.sleep(random.uniform(1, 2))  # Delay to reduce bot detection risk
#             except IndexError:
#                 # Handle malformed rows (e.g., missing columns)
#                 log(f"Skipping malformed row: {lead}")
#                 continue

#         # Log final statistics
#         log(f"Successfully sent {stats['sent']} messages")
#         log(f"Failed to send {stats['failed']} messages")

#         # Close the browser session
#         await browser.close()

# # Entry point of the script
# if __name__ == "__main__":
#     # Run the main function in the asyncio event loop
#     asyncio.run(main())


# import asyncio
# from playwright.async_api import async_playwright
# import csv
# from datetime import datetime
# import random

# WHATSAPP_WEB = "https://web.whatsapp.com/"

# HELLO = "Hi "
# MEET_AND_GREET = ", hope I find you well\n\n"
# BODY = "(whatever message you want to send)"

# CHECK_STRING = "STRING TO SEARCH"
# FILE_TO_OPEN = "whatsapp_automation\leads.csv"

# stats = {
#     "sent": 0,
#     "failed": 0,
#     "without_whatsapp": [],
#     "existent_chat": []
# }

# def log(message):
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     print(f"[{timestamp}] {message}")

# def name_formatter(name_and_surname):
#     try:
#         name = name_and_surname.split()[0]
#         return name.replace("_", " ").lower().title()
#     except IndexError:
#         return name_and_surname

# async def send_message(page, number, message, name, full_name):
#     try:
#         # 1. Click and fill WhatsApp Web search box (using data-tab="3")
#         search_box = page.locator('//div[@contenteditable="true"][@data-tab="3"]')
#         await search_box.click()
#         await search_box.fill("")  # clear previous input
#         await search_box.fill(number)
#         await asyncio.sleep(2)  # wait for search results  

#         # 2. Check if no results found
#         no_results = page.locator('text=No results found')
#         if await no_results.count() > 0:
#             log(f"No WhatsApp account found for {full_name} ({number})")
#             stats["without_whatsapp"].append((name, number))
#             return False
        
#         # After filling search box
#         await search_box.fill(name)  # if searching by name instead of number

#         contact = page.locator(f'//span[@title="{name}"]')
#         await contact.wait_for(timeout=10000)
#         await contact.click()
                

#         # # 3. Click on the contact matching the number (using span[@title="{number}"])
#         # contact = page.locator(f'//span[@title="{number}"]')
#         try:
#             await contact.wait_for(timeout=10000)
#             await contact.click()
#             # wait for message input to appear (data-tab=10)
#             await page.wait_for_selector('//div[@contenteditable="true"][@data-tab="10"]', timeout=15000)
#             await asyncio.sleep(2)
#         except Exception as e:
#             log(f"Failed to open chat for {full_name}: {str(e)}")
#             stats["failed"] += 1
#             return False

#         # 4. Check for duplicate message
#         if await page.get_by_text(CHECK_STRING).count() > 0:
#             log(f"{name} already received the message.")
#             stats["existent_chat"].append((name, number))
#             return False

#         # 5. Focus message input box and send message
#         message_box = page.locator('//div[@contenteditable="true"][@data-tab="10"]')
#         await message_box.click()
#         await message_box.fill(message)
#         await message_box.press("Enter")
#         await asyncio.sleep(1)

#         # 6. Verify message was sent by checking last outgoing message
#         last_msg = page.locator('.message-out').last
#         if await last_msg.count() > 0:
#             last_msg_text = await last_msg.inner_text()
#             if message in last_msg_text:
#                 log(f"Successfully sent message to {full_name}.")
#                 stats["sent"] += 1
#                 return True

#         log(f"Message may not have sent to {full_name}")
#         stats["failed"] += 1
#         return False

#     except Exception as e:
#         log(f"Error sending to {full_name}: {str(e)}")
#         stats["failed"] += 1
#         return False

# async def main():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch_persistent_context(
#             user_data_dir="/home/dario/.config/google-chrome",
#             headless=False
#         )
#         page = await browser.new_page()
#         await page.goto(WHATSAPP_WEB)

#         log("Scan WhatsApp Web QR Code to continue...")
#         await page.wait_for_selector('//div[@contenteditable="true"][@data-tab="3"]', timeout=60000)
#         log("QR Code successfully scanned!")

#         with open(FILE_TO_OPEN, newline='') as csvfile:
#             reader = csv.reader(csvfile)
#             contacts = [row for row in reader]

#         for lead in contacts:
#             try:
#                 name = name_formatter(lead[0])
#                 number = lead[1]
#                 message = HELLO + name + MEET_AND_GREET + BODY

#                 await send_message(page, number, message, name, lead[0])
#                 await asyncio.sleep(random.uniform(1, 2))
#             except IndexError:
#                 log(f"Skipping malformed row: {lead}")
#                 continue

#         log(f"Successfully sent {stats['sent']} messages")
#         log(f"Failed to send {stats['failed']} messages")

#         await browser.close()

# if __name__ == "__main__":
#     asyncio.run(main())




import asyncio
import csv
import logging
import os
import random
from datetime import datetime
from dotenv import load_dotenv
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout

# Load environment variables
load_dotenv()

# Config
WHATSAPP_WEB = "https://web.whatsapp.com/"
CSV_FILE = os.getenv("CSV_FILE", "whatsapp_automation/leads.csv")
CHECK_STRING = os.getenv("CHECK_STRING", "whatever message you want to send")
USER_DATA_DIR = os.getenv("USER_DATA_DIR", "./chrome-data")
FAILED_OUTPUT = "failed.csv"

# Logging setup
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s')
log = logging.info

# Message template
HELLO = "Hi "
MEET_AND_GREET = ", hope I find you well done dude\n\n"
BODY = "(whatever message you want to send)"

# Stats
stats = {
    "sent": 0,
    "failed": 0,
    "without_whatsapp": [],
    "existent_chat": []
}

# Utils
def name_formatter(name_and_surname):
    try:
        name = name_and_surname.split()[0]
        return name.replace("_", " ").lower().title()
    except IndexError:
        return name_and_surname

async def human_delay(min_sec=1.5, max_sec=3.5):
    await asyncio.sleep(random.uniform(min_sec, max_sec))

def export_failed(data, filename=FAILED_OUTPUT):
    with open(filename, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Number"])
        writer.writerows(data)

# Message Sender
async def send_message(page, number, message, name, full_name, max_retries=2):
    for attempt in range(max_retries):
        try:
            log(f"Trying to message {full_name} ({number}) [Attempt {attempt+1}]")

            # 1. Click and fill search box
            search_box = page.locator('[contenteditable="true"][data-tab="3"]')
            await search_box.click()
            await search_box.fill("")
            await human_delay()
            await search_box.fill(number)
            await human_delay(2, 3)

            # 2. Check if no results found
            if await page.locator('text="No results found"').count() > 0:
                log(f"No WhatsApp account for {full_name} ({number})")
                stats["without_whatsapp"].append((name, number))
                return False

            # 3. Click the first visible search result
            try:
                search_result = page.locator(f'//span[@title="{name}"]')
                await search_result.first.wait_for(timeout=10000)
                await search_result.first.click()
                await human_delay(2, 3)
            except Exception as e:
                log(f"Could not click contact for {full_name}: {e}")
                stats["failed"] += 1
                return False

            # 4. Wait for message input box
            try:
                await page.wait_for_selector('[contenteditable="true"][data-tab="10"]', timeout=15000)
            except PlaywrightTimeout:
                log(f"Message box not found for {full_name}")
                stats["failed"] += 1
                return False

            # 5. Check for duplicate message
            if await page.locator(f'.message-out:has-text("{CHECK_STRING}")').count() > 0:
                log(f"{name} already received the message.")
                stats["existent_chat"].append((name, number))
                return False

            # 6. Send message
            message_box = page.locator('[contenteditable="true"][data-tab="10"]')
            await message_box.click()
            await human_delay()
            await message_box.fill(message)
            await human_delay()
            await message_box.press("Enter")
            await human_delay()

            # 7. Confirm sent
            last_msg = page.locator('.message-out').last
            if await last_msg.count() > 0:
                last_msg_text = await last_msg.inner_text()
                if BODY in last_msg_text:
                    log(f"✅ Message sent to {full_name}.")
                    stats["sent"] += 1
                    return True

            log(f"❓ Message may not have sent to {full_name}.")
            stats["failed"] += 1
            return False

        except PlaywrightTimeout:
            log(f"⏱️ Timeout while messaging {full_name}. Retrying...")
        except Exception as e:
            log(f"❌ Error sending to {full_name}: {e}")
            await human_delay(3, 5)

    stats["failed"] += 1
    return False

# Main Automation Logic
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False
        )
        page = await browser.new_page()
        await page.goto(WHATSAPP_WEB)

        log("Please scan the QR code (if not already logged in)...")
        try:
            await page.wait_for_selector('[contenteditable="true"][data-tab="3"]', timeout=60000)
            log("✅ WhatsApp Web is ready.")
        except PlaywrightTimeout:
            log("❌ QR scan timeout. Exiting.")
            return

        # Load contacts
        with open(CSV_FILE, newline='') as csvfile:
            reader = csv.reader(csvfile)
            contacts = [row for row in reader if len(row) >= 2]

        for lead in contacts:
            try:
                name = name_formatter(lead[0])
                number = lead[1]
                message = HELLO + name + MEET_AND_GREET + BODY
                await send_message(page, number, message, name, lead[0])
                await human_delay()
            except Exception as e:
                log(f"⚠️ Error processing contact {lead}: {e}")
                continue

        # Summary
        log(f"\n--- ✅ SUMMARY ---")
        log(f"Messages sent: {stats['sent']}")
        log(f"Failed messages: {stats['failed']}")
        log(f"No WhatsApp: {len(stats['without_whatsapp'])}")
        log(f"Already contacted: {len(stats['existent_chat'])}")

        # Export failures
        failed_data = stats["without_whatsapp"] + stats["existent_chat"]
        if failed_data:
            export_failed(failed_data)
            log(f"📁 Exported failed/duplicate contacts to: {FAILED_OUTPUT}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
