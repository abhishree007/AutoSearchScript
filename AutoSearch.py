from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def main():
    # Set the path to your Edge WebDriver executable (e.g., msedgedriver)
    # Update this path as needed for your setup
    webdriver_path = "C:\\Users\\abhis\\Downloads\\edgedriver_win64\\msedgedriver.exe"  # Assumes msedgedriver is in your PATH

    # Initialize Edge driver
    service = EdgeService(executable_path=webdriver_path)
    driver = webdriver.Edge(service=service)

    try:
        # Open Google
        driver.get("https://www.google.com")

        wait = WebDriverWait(driver,5)

        # Accept cookies if the consent form appears (Google may show it sometimes)
        try:
            consent_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'I agree')] | //button[contains(text(),'Accept all')]")))
            consent_button.click()
        except:
            # Consent form not present, continue
            pass

        # Wait for the search bar to be visible
        search_box = wait.until(EC.visibility_of_element_located((By.NAME, "q")))

        # Enter "hello world" and submit the search form
        search_box.clear()
        search_box.send_keys("hello world")
        search_box.send_keys(Keys.RETURN)

        # Wait for the search results page to load by waiting for results div
        wait.until(EC.presence_of_element_located((By.ID, "search")))

        print("Search complete for 'hello world'.")

        # Optional: wait a few seconds so user can see result before browser closes
        time.sleep(5)

    except Exception as e:
        print(f"Error occurred: {e}", file=sys.stderr)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()

