from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver for Safari
driver = webdriver.Safari()

# Open the website
url = "https://packetstats.com"
driver.get(url)

# Wait for the "Start" button to be clickable, increase the wait time
start_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="button_pause_resume"]'))  # Adjust XPath as needed
)
start_button.click()  # Click the "Start Test" button

# Wait for the test to start (adjust the time as needed)
time.sleep(5)

# Continuously get the ping value every second
try:
    while True:
        # Wait for the ping value element to appear and retrieve the text
        ping_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="contentArea"]/div[2]/div/span[2]'))  # Adjust XPath as needed
        )
        ping = ping_element.text  # Get the text (ping value)
        print(f"Current Ping: {ping}")
        time.sleep(0.5)  # Wait for 1 second before checking again
except KeyboardInterrupt:
    print("Test interrupted")

# Close the browser
driver.quit()