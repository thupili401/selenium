import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# Initialize the Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

# Open the URL
driver.get("https://tutorialsninja.com/demo/")

# Initialize ActionChains
actions = ActionChains(driver)

# Locate the "Components" element and hover over it
components = driver.find_element(By.XPATH, "//a[text()='Components']")
actions.move_to_element(components).perform()

# Wait for the dropdown to become visible
time.sleep(1)  # Add a brief sleep to ensure the dropdown is fully rendered

# Click on "Monitors (2)" from the dropdown
driver.find_element(By.XPATH, "//a[text()='Monitors (2)']").click()

# Wait for a few seconds before closing the browser
time.sleep(3)
driver.close()
