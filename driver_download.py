import os
import zipfile
import requests
import subprocess
import sys
import platform
from packaging import version
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time




def get_chrome_version():
    system = platform.system()

    if system == "Windows":
        import winreg
        reg_path = r"SOFTWARE\Google\Chrome\BLBeacon"
        try:
            reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path)
            value, _ = winreg.QueryValueEx(reg_key, "version")
            return value
        except Exception:
            raise Exception("Could not find Chrome version in registry.")
    elif system == "Darwin":
        process = subprocess.Popen(
            ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "--version"],
            stdout=subprocess.PIPE)
        output, _ = process.communicate()
        return output.decode("utf-8").strip().split()[-1]
    elif system == "Linux":
        process = subprocess.Popen(["google-chrome", "--version"], stdout=subprocess.PIPE)
        output, _ = process.communicate()
        return output.decode("utf-8").strip().split()[-1]
    else:
        raise Exception("Unsupported OS")

def get_chromedriver_url(chrome_version):
    major_version = chrome_version.split('.')[0]
    metadata_url = f"https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json"
    response = requests.get(metadata_url)
    response.raise_for_status()
    versions_data = response.json()

    for entry in versions_data['channels'].values():
        if entry['version'].startswith(major_version):
            for item in entry['downloads']['chromedriver']:
                if platform.system() == "Windows" and item['platform'] == "win32":
                    return item['url']
                elif platform.system() == "Linux" and item['platform'] == "linux64":
                    return item['url']
                elif platform.system() == "Darwin" and item['platform'] == "mac-x64":
                    return item['url']
    raise Exception("Compatible ChromeDriver not found.")

def download_and_extract_chromedriver(url, extract_to="."):
    zip_path = os.path.join(extract_to, "chromedriver.zip")
    with open(zip_path, "wb") as f:
        f.write(requests.get(url).content)

    # with zipfile.ZipFile(zip_path, "r") as zip_ref:
    #     zip_ref.extractall(extract_to)
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        for member in zip_ref.namelist():
            filename = os.path.basename(member)
            if filename == "chromedriver.exe":
                source = zip_ref.open(member)
                target_path = os.path.join(extract_to, "chromedriver.exe")
                with open(target_path, "wb") as target:
                    with source as src:
                        target.write(src.read())
                break

    os.remove(zip_path)
    print("Chromedriver downloaded and extracted.")

def launch_browser_and_download(chromedriver_path):
    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": os.getcwd()}
    options.add_experimental_option("prefs", prefs)

    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)

    # Example: Download a test file (replace with your desired URL)
    driver.get("https://www.thinkbroadband.com/download")

    # Example download click (you may need to adjust this)
    link = driver.find_element(By.PARTIAL_LINK_TEXT, "100MB")
    link.click()

    print("Download initiated. Waiting for 10 seconds...")
    time.sleep(10)
    driver.quit()

def main():
    print("Detecting Chrome version...")
    chrome_version = get_chrome_version()
    print(f"Chrome version detected: {chrome_version}")

    print("Fetching compatible ChromeDriver...")
    url = get_chromedriver_url(chrome_version)

    print(f"Downloading ChromeDriver from: {url}")
    download_and_extract_chromedriver(url)

    chromedriver_path = os.path.join(".", "chromedriver")  # or chromedriver.exe on Windows
    if platform.system() == "Windows":
        chromedriver_path += ".exe"

    print("Launching browser...")
    # launch_browser_and_download(chromedriver_path)
    launch_browser_and_download(chromedriver_path)

    print(f"Using ChromeDriver at: {chromedriver_path}")
    # print(f"Using browser binary at: {browser_binary_path}")


if __name__ == "__main__":
    main()
