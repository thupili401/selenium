from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Initialize the Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()

# Open the target webpage
driver.get("https://omayo.blogspot.com/")

# Wait for the hidden button to be present
wait = WebDriverWait(driver, 30)
hidden_button = wait.until(EC.presence_of_element_located((By.ID, "hbutton")))

# Get the value attribute of the hidden button
label = hidden_button.get_attribute("value")

# Print the value
print(label)

# Close the driver
driver.quit()
