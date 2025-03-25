import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up Chrome options
Chrome_options = webdriver.ChromeOptions()
Chrome_options.add_argument("--headless")  # Run in headless mode

# Initialize the WebDriver
driver = webdriver.Chrome(options=Chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)

# Navigate to the target URL
driver.get("https://embibe.com/")
time.sleep(3)

# Calculate the total width and height of the page
total_width = driver.execute_script("return document.body.scrollWidth")
total_height = driver.execute_script("return document.body.scrollHeight")
time.sleep(3)
# Resize the window to the calculated dimensions
driver.set_window_size(total_width, total_height)
time.sleep(3)
# Capture the full-page screenshot
page_body = driver.find_element(By.TAG_NAME, "body")
page_body.screenshot("fullpage1.png")
time.sleep(3)
# Quit the WebDriver
driver.quit()
