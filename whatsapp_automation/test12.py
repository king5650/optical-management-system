import asyncio
from playwright.async_api import async_playwright
import csv
from datetime import datetime
import random
import re # Import regex module

# WhatsApp Web URL
WHATSAPP_WEB = "https://web.whatsapp.com/"

# Message components
HELLO = "Hi "  # Greeting to start the message
MEET_AND_GREET = ", hope I find you well\n\n"  # Contextual intro
BODY = "(whatever message you want to send)"  # Main message body page

# String to search in previous messages to avoid duplicates
CHECK_STRING = "STRING TO SEARCH"

# Input file containing leads (CSV format)
FILE_TO_OPEN = "whatsapp_automation\leads.csv"

# Dictionary to track statistics during execution
stats = {
    "sent": 0,  # Number of successfully sent messages
    "failed": 0,  # Number of failed message attempts
    "without_whatsapp": [],  # Leads without WhatsApp
    "existent_chat": []  # Leads who already received the message
}

# Logs a message with a timestamp
def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Current time
    print(f"[{timestamp}] {message}")  # Print the formatted log message

# Formats a name by removing unnecessary characters and capitalizing it
def name_formatter(name_and_surname):
    try:
        name = name_and_surname.split()[0]
        return name.replace("_", " ").lower().title()
    except IndexError:
        return name_and_surname

# NEW FUNCTION: Formats the phone number to match WhatsApp's display format (e.g., adding spaces, country code)
# This is crucial. You MUST verify these formats by manually searching a number on WhatsApp Web
# and inspecting the 'name' attribute of the chat result button.
def format_whatsapp_number_for_search(number_str):
    digits_only = ''.join(filter(str.isdigit, number_str))

    # Based on your previous examples (+237 6 80 78 56 77 and +237 99157781)
    # Let's try to generate common patterns WhatsApp might use.
    
    formatted_numbers = [number_str] # Always include the original
    if not number_str.startswith('+'):
        formatted_numbers.append(f'+{number_str}') # Add with a plus sign

    # Attempt to format for Cameroon specific pattern if it's a 9-digit number starting with 6 or 7
    if len(digits_only) == 9 and digits_only[0] in ['6', '7']: # Common starting digits for Cameroon mobiles
        # Example: 680785677 -> +237 6 80 78 56 77
        formatted = f"+237 {digits_only[0]} {digits_only[1:3]} {digits_only[3:5]} {digits_only[5:7]} {digits_only[7:]}"
        formatted_numbers.append(formatted)
        
        # Also try just the spaced local number without country code, if WhatsApp shows it that way
        formatted_local = f"{digits_only[0]} {digits_only[1:3]} {digits_only[3:5]} {digits_only[5:7]} {digits_only[7:]}"
        formatted_numbers.append(formatted_local)

    # If it's a full 12-digit number (e.g., 237680785677)
    elif len(digits_only) == 12 and digits_only.startswith('237'):
        # Example: 237680785677 -> +237 6 80 78 56 77 (assuming a 9-digit local after 237)
        local_part = digits_only[3:]
        if len(local_part) == 9 and local_part[0] in ['6', '7']:
            formatted = f"+{digits_only[0:3]} {local_part[0]} {local_part[1:3]} {local_part[3:5]} {local_part[5:7]} {local_part[7:]}"
            formatted_numbers.append(formatted)
            
    # Add any other specific formats you observe from your manual tests on WhatsApp Web.
    # For instance, if a contact name shows up as "John Doe +237680785677"
    # then you might need to add a regex like `r".*\b" + re.escape(digits_only) + r"\b.*"`
    # But for now, focusing on the number itself in various common formats.

    return list(set(formatted_numbers)) # Return unique formats

# Sends a message to a specified phone number using WhatsApp Web
async def send_message(page, number, message, name, full_name):
    try:
        log(f"Attempting to send message to {full_name} ({number})...")

        # Step 1: Clear and search for the number in WhatsApp search box
        search_input_locator = page.getByRole('textbox', { name: 'Search input textbox' })
        
        await search_input_locator.wait_for(state='visible', timeout=10000)
        await search_input_locator.click()
        await search_input_locator.fill('') # Clear any previous search text
        await search_input_locator.type(number, delay=random.uniform(50, 150)) # Type with a slight delay for realism
        log(f"Filled search box with {number}. Waiting for search results to appear...")
        
        # Step 2: Wait for the specific contact element to appear and click it
        # Generate potential number formats for the 'name' attribute of the button
        possible_number_formats = format_whatsapp_number_for_search(number)
        log(f"Trying to find contact with these number patterns in button name: {possible_number_formats}")

        contact_found = False
        for num_format in possible_number_formats:
            # Escape special regex characters in the formatted number to ensure exact match for literal numbers
            escaped_num_format = re.escape(num_format)
            
            # Use a regex to find the button name that contains our formatted number.
            # This is flexible as the button name might contain other text like "Yesterday", "Open the chat".
            contact_button_locator = page.getByRole('button', { name: re.compile(f".*{escaped_num_format}.*") })
            
            try:
                # Wait for the specific contact button to appear and be enabled (clickable)
                await contact_button_locator.wait_for(state='visible', timeout=5000) 
                await contact_button_locator.wait_for(state='enabled', timeout=5000)
                log(f"Found contact button using pattern: '{escaped_num_format}'. Clicking...")
                await contact_button_locator.click()
                contact_found = True
                break # Exit loop once found and clicked
            except TimeoutError:
                log(f"Contact button not found with pattern: '{escaped_num_format}'. Trying next format...")
                continue
            except Exception as e:
                log(f"Error during search with pattern '{escaped_num_format}': {e}")
                continue
        
        if not contact_found:
            log(f"No WhatsApp contact found for {full_name} ({number}) after trying all formats. Moving to next lead.")
            stats["without_whatsapp"].append((name, number))
            return False

        # Step 3: Wait for the chat input field to be visible, indicating the chat is open
        message_input_locator = page.getByRole('textbox', { name: 'Type a message' })
        try:
            await message_input_locator.wait_for(state='visible', timeout=15000)
            log(f"Chat with {full_name} opened.")
        except TimeoutError:
            log(f"Chat failed to load message input for {full_name} after clicking contact. Moving to next lead.")
            stats["failed"] += 1
            return False
        except Exception as e:
            log(f"Error waiting for message input for {full_name}: {e}. Moving to next lead.")
            stats["failed"] += 1
            return False

        # Step 4: Check if the message has already been sent
        # Using getByText is robust for checking if CHECK_STRING exists
        previous_message_count = await page.getByText(CHECK_STRING).count()
        if previous_message_count > 0:
            log(f"{name} already received the message (found '{CHECK_STRING}').")
            stats["existent_chat"].append((name, number))
            return False

        # Step 5: Locate the message input field and type the message
        # message_field = page.locator(message_input_selector).first # Old way
        message_field = message_input_locator # Use the locator we already defined
        
        # Verify the message field is actually editable before typing
        if not await message_field.is_editable():
            raise Exception(f"Message field for {full_name} not editable, possibly blocked or UI issue.")

        # Step 6: Type the message and press Enter to send
        await message_field.type(message, delay=random.uniform(20, 70)) # Simulate typing more naturally
        await message_field.press("Enter")
        log(f"Successfully sent message to {full_name}.")
        stats["sent"] += 1
        return True
    
    except Exception as e:
        log(f"General error during message sending process for {full_name}: {e}")
        stats["failed"] += 1
        return False
    finally:
        # After attempting to send (or failing), try to clear the search bar.
        try:
            # Use the 'Cancel search' button
            cancel_search_button = page.getByRole('button', { name: 'Cancel search' })
            if await cancel_search_button.is_visible():
                log("Attempting to click 'Cancel search' button.")
                await cancel_search_button.click()
                log("Cleared search bar using 'Cancel search' button.")
            else:
                log("Cancel search button not visible. Skipping clear.")
        except Exception as clear_error:
            log(f"Could not clear search bar using 'Cancel search' button: {clear_error}")

        # Add a small pause before processing the next contact, important for stability
        await asyncio.sleep(random.uniform(2, 5)) # Slightly longer random delay, essential for WhatsApp stability


# Main function to orchestrate message sending
async def main():
    # Initialize Playwright and launch the browser in persistent mode
    async with async_playwright() as p:
        browser = await p.chromium.launch_persistent_context(
            user_data_dir="C:\\Users\\falco\\AppData\\Local\\Google\\Chrome\\User Data",  # Adjusted for Windows
            headless=False  # Run browser in visible mode for debugging
        )
        page = await browser.new_page()  # Create a new page (tab)
        await page.goto(WHATSAPP_WEB)  # Open WhatsApp Web

        # Wait for the user to scan the QR Code
        log("Scan WhatsApp Web QR Code to continue...")
        # Use the more robust locator for the search input
        await page.getByRole('textbox', { name: 'Search input textbox' }).wait_for(state='visible', timeout=60000)
        log("QR Code successfully scanned!")  # Log success

        # Open the leads CSV file
        with open(FILE_TO_OPEN, newline='', encoding='utf-8') as csvfile: 
            reader = csv.reader(csvfile)  
            contacts = [row for row in reader] 
        
        # Iterate over the contacts and send messages
        for lead in contacts:
            try:
                name = name_formatter(lead[0])
                number = lead[1]

                message = HELLO + name + MEET_AND_GREET + BODY

                await send_message(page, number, message, name, lead[0])
            except IndexError:
                log(f"Skipping malformed row: {lead}")
                continue

        log(f"Successfully sent {stats['sent']} messages")
        log(f"Failed to send {stats['failed']} messages")
        if stats['without_whatsapp']:
            log(f"Contacts without WhatsApp: {stats['without_whatsapp']}")
        if stats['existent_chat']:
            log(f"Contacts with existent chat: {stats['existent_chat']}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())


# import { test, expect } from '@playwright/test';

# test('test', async ({ page }) => {
#   await page.goto('https://web.whatsapp.com/');
#   await page.locator('html').click();
#   await page.getByRole('button', { name: 'Click to reload QR code' }).click();
#   await page.goto('https://web.whatsapp.com/');
#   await page.locator('.x10l6tqk > div').first().click();
#   await page.getByRole('grid', { name: 'Chat list' }).click();
#   await page.getByRole('textbox', { name: 'Search input textbox' }).getByRole('paragraph').click();
#   await page.getByRole('textbox', { name: 'Search input textbox' }).fill('kevin');
#   await page.getByText('Chats').click();
#   await page.getByRole('grid', { name: 'Search results.' }).click();
#   await page.getByRole('button', { name: 'Cancel search' }).click();
#   await page.getByRole('grid', { name: 'Chat list' }).click();
#   await page.getByRole('textbox', { name: 'Type a message' }).click();
#   await page.getByRole('textbox', { name: 'Search input textbox' }).getByRole('paragraph').click();
#   await page.getByRole('textbox', { name: 'Search input textbox' }).fill('kevin');
#   await page.getByRole('grid', { name: 'Search results.' }).click();
#   await page.getByRole('grid', { name: 'Search results.' }).click();
#   await page.getByRole('button', { name: 'Cancel search' }).click();
#   await page.getByRole('button', { name: 'Profile picture, disappearing messages on Joël-Amihdaf Yesterday Photo Selected' }).click();
#   await page.getByText('7/24/2025tail-outdocument-PDF').click();
#   await page.getByText('7/24/2025tail-outdocument-PDF').click();
#   await page.getByRole('textbox', { name: 'Type a message' }).getByRole('paragraph').click();
#   await page.getByRole('textbox', { name: 'Type a message' }).getByRole('paragraph').click();
#   await page.getByRole('button', { name: 'Nadi 11:20 PE-20250731-100744' }).click();
#   await page.getByRole('button', { name: 'Kevin Yesterday Yo Open the' }).click();
#   await page.getByRole('button', { name: 'Profile picture, disappearing messages on Joël-Amihdaf Yesterday Photo Open the' }).click();
# });

# import { test, expect } from '@playwright/test';

# test('test', async ({ page }) => {
#   await page.goto('https://web.whatsapp.com/');
#   await page.locator('html').click();
#   await page.getByRole('button', { name: 'Click to reload QR code' }).click();
#   await page.goto('https://web.whatsapp.com/');
#   await page.locator('.x10l6tqk > div').first().click();
#   await page.getByRole('grid', { name: 'Chat list' }).click();
#   await page.getByRole('textbox', { name: 'Search input textbox' }).getByRole('paragraph').click();
#   await page.getByRole('textbox', { name: 'Search input textbox' }).fill('kevin');
#   await page.getByText('Chats').click();
#   await page.getByRole('grid', { name: 'Search results.' }).click();
#   await page.getByRole('button', { name: 'Cancel search' }).click();
#   await page.getByRole('grid', { name: 'Chat list' }).click();
#   await page.getByRole('textbox', { name: 'Type a message' }).click();
#   await page.getByRole('textbox', { name: 'Search input textbox' }).getByRole('paragraph').click();
#   await page.getByRole('textbox', { name: 'Search input textbox' }).fill('kevin');
#   await page.getByRole('grid', { name: 'Search results.' }).click();
#   await page.getByRole('grid', { name: 'Search results.' }).click();
#   await page.getByRole('button', { name: 'Cancel search' }).click();
#   await page.getByRole('button', { name: 'Profile picture, disappearing messages on Joël-Amihdaf Yesterday Photo Selected' }).click();
#   await page.getByText('7/24/2025tail-outdocument-PDF').click();
#   await page.getByText('7/24/2025tail-outdocument-PDF').click();
#   await page.getByRole('textbox', { name: 'Type a message' }).getByRole('paragraph').click();
#   await page.getByRole('textbox', { name: 'Type a message' }).getByRole('paragraph').click();
#   await page.getByRole('button', { name: 'Nadi 11:20 PE-20250731-100744' }).click();
#   await page.getByRole('button', { name: 'Kevin Yesterday Yo Open the' }).click();
#   await page.getByRole('button', { name: 'Profile picture, disappearing messages on Joël-Amihdaf Yesterday Photo Open the' }).click();
#   await page.getByRole('textbox', { name: 'Type a message' }).click();
#   const downloadPromise = page.waitForEvent('download');
#   await page.getByText('Fridaytail-out08:36msg-').click();
#   const download = await downloadPromise;
#   await page.getByRole('button', { name: 'Kevin Yesterday Yo' }).click();
#   await page.getByText('Fridaytail-outvideo-pipmedia-').click();
#   await page.getByTitle('Close').click();
#   await page.getByRole('button', { name: '+237 99157781 7/9/2025 Ok' }).click();
#   await page.getByText('7/8/2025tail-inGroup •').click();
#   await page.getByRole('button', { name: 'Profile picture, disappearing messages on +237 6 97 00 30 96 Open the chat' }).click();
#   await page.locator('.x12lumcd').first().click();
#   await page.locator('.x12lumcd').first().click();
#   await page.locator('.x12lumcd').first().click();
#   await page.locator('.x12lumcd').first().click();
#   await page.locator('.x12lumcd').first().click();
#     await page.getByText('status-dblcheckRead').click();
#   await page.getByText('status-dblcheckDelivered').click();
# });










# import { test, expect } from '@playwright/test';

# test('test', async ({ page }) => {
#   await page.goto('https://web.whatsapp.com/');
#   await page.locator('html').click();
#   await page.getByRole('button', { name: 'Click to reload QR code' }).click();
#   await page.goto('https://web.whatsapp.com/');
#   await page.locator('.x10l6tqk > div').first().click();
#   await page.getByRole('grid', { name: 'Chat list' }).click();
#   await page.getByRole('textbox', { name: 'Search input textbox' }).getByRole('paragraph').click();
#   await page.getByRole('textbox', { name: 'Search input textbox' }).fill('kevin');
#   await page.getByText('Chats').click();
#   await page.getByRole('grid', { name: 'Search results.' }).click();
#   await page.getByRole('button', { name: 'Cancel search' }).click();
#   await page.getByRole('grid', { name: 'Chat list' }).click();
#   await page.getByRole('textbox', { name: 'Type a message' }).click();
#   await page.getByRole('textbox', { name: 'Search input textbox' }).getByRole('paragraph').click();
#   await page.getByRole('textbox', { name: 'Search input textbox' }).fill('kevin');
#   await page.getByRole('grid', { name: 'Search results.' }).click();
#   await page.getByRole('grid', { name: 'Search results.' }).click();
#   await page.getByRole('button', { name: 'Cancel search' }).click();
#   await page.getByRole('button', { name: 'Profile picture, disappearing messages on Joël-Amihdaf Yesterday Photo Selected' }).click();
#   await page.getByText('7/24/2025tail-outdocument-PDF').click();
#   await page.getByText('7/24/2025tail-outdocument-PDF').click();
#   await page.getByRole('textbox', { name: 'Type a message' }).getByRole('paragraph').click();
#   await page.getByRole('textbox', { name: 'Type a message' }).getByRole('paragraph').click();
#   await page.getByRole('button', { name: 'Nadi 11:20 PE-20250731-100744' }).click();
#   await page.getByRole('button', { name: 'Kevin Yesterday Yo Open the' }).click();
#   await page.getByRole('button', { name: 'Profile picture, disappearing messages on Joël-Amihdaf Yesterday Photo Open the' }).click();
#   await page.getByRole('textbox', { name: 'Type a message' }).click();
#   const downloadPromise = page.waitForEvent('download');
#   await page.getByText('Fridaytail-out08:36msg-').click();
#   const download = await downloadPromise;
#   await page.getByRole('button', { name: 'Kevin Yesterday Yo' }).click();
#   await page.getByText('Fridaytail-outvideo-pipmedia-').click();
#   await page.getByTitle('Close').click();
#   await page.getByRole('button', { name: '+237 99157781 7/9/2025 Ok' }).click();
#   await page.getByText('7/8/2025tail-inGroup •').click();
#   await page.getByRole('button', { name: 'Profile picture, disappearing messages on +237 6 97 00 30 96 Open the chat' }).click();
#   await page.locator('.x12lumcd').first().click();
#   await page.locator('.x12lumcd').first().click();
#   await page.locator('.x12lumcd').first().click();
#   await page.locator('.x12lumcd').first().click();
#   await page.locator('.x12lumcd').first().click();
#   await page.getByRole('button', { name: 'Kevin Yesterday Yo Open the' }).click();
#   await page.getByRole('button', { name: ':04 Read' }).nth(1).click();
#   await page.getByText('status-dblcheckRead').click();
#   await page.getByText('status-dblcheckDelivered').click();
# });