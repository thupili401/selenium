import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# Set an implicit wait
driver.implicitly_wait(10)

# Navigate to the website
driver.get("https://omayo.blogspot.com/")

# Store the parent window handle
parent = driver.current_window_handle

# Click the link to open a new window
driver.find_element(By.XPATH, "//a[.='http://www.Selenium143.blogspot.com']").click()

# Get the new window handle
windows = driver.window_handles

# Switch directly to the newly opened window (second window)
driver.switch_to.window(windows[1])

# Click the link 'What is Selenium?'
driver.find_element(By.XPATH, "//a[.='What is Selenium?']").click()

# Wait for 3 seconds to observe the action
time.sleep(3)

# Close the newly opened window
driver.close()

# Switch back to the parent window
driver.switch_to.window(parent)

# Enter text in the text area
driver.find_element(By.ID, "ta1").send_keys("Sreekanth")

# Wait for 3 seconds
time.sleep(3)

# Quit the browser
driver.quit()
