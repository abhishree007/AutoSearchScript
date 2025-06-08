from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def main():
    webdriver_path = "C:\\Users\\abhis\\Downloads\\edgedriver_win64\\msedgedriver.exe"

    # Optional: prevent "Automation Controlled" warning
    options = webdriver.EdgeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    service = EdgeService(executable_path=webdriver_path)
    driver = webdriver.Edge(service=service, options=options)

    try:
        driver.get("https://www.google.com")
        wait = WebDriverWait(driver, 5)

        # Handle Google cookies (if shown)
        try:
            consent_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'I agree')] | //button[contains(text(),'Accept all')]")))
            consent_button.click()
        except:
            pass

        # Wait for the search box
        search_box = wait.until(EC.visibility_of_element_located((By.NAME, "q")))

        # Type and search
        search_box.clear()
        search_box.send_keys("hello world")
        search_box.send_keys(Keys.RETURN)

        # Wait for result container or CAPTCHA
        try:
            wait.until(EC.presence_of_element_located((By.ID, "search")))
            print("Search results loaded.")
        except:
            # Check for CAPTCHA and wait
            print("Possible CAPTCHA detected. Please solve it manually.")
            input("Press Enter after solving CAPTCHA...")

        print("Done. Browser will remain open for inspection.")

    except Exception as e:
        print(f"Error occurred: {e}", file=sys.stderr)

    # Do NOT call driver.quit() – leave browser open
    # You can manually close the browser after inspection

if __name__ == "__main__":
    main()
