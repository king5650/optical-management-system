# import re
# from playwright.sync_api import Page, expect

# def test_has_title(page: Page):
#     page.goto("https://youtube.com/")

#     # Expect a title "to contain" a substring.
#     expect(page).to_have_title(re.compile("youtube"))

# def test_get_started_link(page: Page):
#     page.goto("https://youtube.com/")

#     # Click the get started link.
#     page.get_by_role("link", name="sign in").click()

#     # Expects page to have a heading with the name of Installation.
#     expect(page.get_by_role("heading", name="sign up")).to_be_visible()
    
    

# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     # Only use storage_state if the file exists
#     import os
#     if os.path.exists("playwright_state.json"):
#         context = browser.new_context(storage_state="playwright_state.json")
#     else:
#         context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://web.whatsapp.com")

#     page.wait_for_selector('input[title="Search input textbox"]', timeout=60000)
#     page.fill('input[title="Search input textbox"]', 'John Doe')
#     page.keyboard.press("Enter")
    
#     page.wait_for_selector('div[title="Type a message"]', timeout=60000)
#     page.fill('div[title="Type a message"]', 'Hello from Playwright!')
#     page.keyboard.press("Enter")
    
#     # Save session state for future runs
#     context.storage_state(path="playwright_state.json")
#     browser.close()



# from playwright.sync_api import sync_playwright, TimeoutError
# import os

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     context = None

#     # Use saved session if exists
#     if os.path.exists("playwright_state.json"):
#         context = browser.new_context(storage_state="playwright_state.json")
#     else:
#         context = browser.new_context()

#     page = context.new_page()
#     page.goto("https://web.whatsapp.com")

#     print("🚀 Loading WhatsApp Web...")

#     try:
#         # STEP 1: Detect QR code (if user needs to log in)
#         page.wait_for_selector("canvas[aria-label='Scan me!']", timeout=90000)
#         print("🔄 Waiting for QR code scan...")
        
#         # STEP 2: Wait until QR is scanned and home page is visible
#         page.wait_for_selector("div[role='textbox']", timeout=60000)  # Message input visible
#         print("✅ Login done")

#     except TimeoutError:
#         # If QR not found in 10s, assume already logged in
#         print("ℹ️ No QR code found, assuming session already active.")
    
#     try:
#         # STEP 3: Wait for WhatsApp home page/chat UI
#         page.wait_for_selector("div[role='textbox']", timeout=30000)
#         print("🏠 Home page loaded, ready to automate.")
#     except TimeoutError:
#         print("❌ Home page failed to load. Something went wrong.")

#     # Save session for future runs
#     context.storage_state(path="playwright_state.json")
#     browser.close()


    
    
# from playwright.sync_api import sync_playwright, TimeoutError

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://web.whatsapp.com")
#     page.locator("canvas[aria-label='Scan me!']").is_visible()  # Detect QR screen
#     # page.get_by_role('paragraph').fill("shafai")
#     # page.locator('div').filter(has_text="Search or start a new chat").first.click()
  
#     page.get_by_role('button', name='Shafai').click()
#     page.get_by_role('textbox', name='Type a message').locator('p').click()
#     page.get_by_role('textbox', name='Type a message').fill('hello bro')
#     # page.get_by_role('button', name='Send').click()
#     page.get_by_role('button', name='Send').filter(has_text="Send").click()
#     # page.get_by_role('textbox', name='Type a message').fill('cool?')
#     # page.get_by_role('button', name='Send').click()
   
# #     print("🚀 Opened WhatsApp Web...")

# #     try:
# #         # Try to detect the QR code canvas
# #         page.wait_for_selector("canvas[aria-label='Scan me!']", timeout=10000)
# #         print("🕐 Waiting for QR scan...")
# #     except TimeoutError:
# #         print("✅ Already logged in or QR scan completed.")

#     browser.close()

import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://web.whatsapp.com")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("WhatsApp"))

def test_get_started_link(page: Page):
    page.goto("https://web.whatsapp.com/")
    
    page.locator("canvas[aria-label='Scan me!']").is_visible()  # Detect QR screen
    page.get_by_role('paragraph').fill("kiven")
    page.locator('div').filter(has_text="Search or start a new chat").first.click()

    page.locator('.x10l6tqk > div').first.click()
    page.get_by_role('button', name='Shafai Yesterday yo Open the').click()
    page.get_by_role('textbox', name='Type a message').locator('p').click()
    page.get_by_role('textbox', name='Type a message').fill('hello bro')
    page.get_by_role('button', name='Send').click()
    page.get_by_role('textbox', name='Type a message').fill('cool?')
    page.get_by_role('button', name='Send').click()
   
    # # Click the get started link.
    # page.get_by_role("link", name="sign in").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="sign up")).to_be_visible()




# import { test, expect } from '@playwright/test';

# test('test', async ({ page }) => {
#   await page.goto('https://web.whatsapp.com/');
#   await page.locator('#app').click();
#   await page.locator('.x1c4vz4f.xs83m0k.xdl72j9.x1g77sc7.x78zum5.xozqiw3.x1oa3qoh.x12fk4p8.xeuugli.x2lwn1j.xl56j7k.x1q0g3np.x6s0dn4.x1ndca9r').click();
#   await page.getByRole('img', { name: 'Scan this QR code to link a' }).click({
#     position: {
#       x: 135,
#       y: 76
#     }
#   });
#   await page.getByRole('img', { name: 'Scan this QR code to link a' }).click({
#     position: {
#       x: 135,
#       y: 76
#     }
#   });
#   await page.goto('https://web.whatsapp.com/');
#   await page.getByRole('button', { name: 'Continue' }).click();
#   await page.getByRole('paragraph').click();
#   await page.locator('div').filter({ hasText: /^Search or start a new chat$/ }).first().click();
#   await page.getByRole('button', { name: '+237 6 80 84 36 67 6:14 PM 0:' }).click();
#   await page.getByRole('textbox', { name: 'Type a message' }).getByRole('paragraph').click();
#   await page.getByText('plus-roundedexpressionsType a').click();
# });
# import { test, expect } from '@playwright/test';

# test('test', async ({ page }) => {
#   await page.goto('https://web.whatsapp.com/');
#   await page.getByRole('img', { name: 'Scan this QR code to link a' }).click({
#     position: {
#       x: 94,
#       y: 38
#     }
#   });
#   await page.getByRole('img', { name: 'Scan this QR code to link a' }).click({
#     position: {
#       x: 94,
#       y: 38
#     }
#   });
#   await page.locator('.x1c4vz4f.xs83m0k.xdl72j9.x1g77sc7.x78zum5.xozqiw3.x1oa3qoh.x12fk4p8.xgpatz3').click();
#   await page.getByText('wa-logowa-wordmarkweb-login-').click();
#   await page.getByText('wa-logowa-wordmarkweb-login-').click();
#   await page.getByText('wa-logowa-wordmarkweb-login-').click();
#   await page.getByText('wa-logowa-wordmarkweb-login-').click();
#   await page.getByRole('img', { name: 'Scan this QR code to link a' }).click({
#     position: {
#       x: 195,
#       y: 52
#     }
#   });
# });