import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Initialize the driver
driver = webdriver.Chrome()
driver.maximize_window()

# Open the webpage
driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")

# Open the date picker
driver.find_element(By.ID, "datepicker").click()

# Wait for the calendar to appear
wait = WebDriverWait(driver, 10)
cal = wait.until(EC.visibility_of_element_located((By.ID, "ui-datepicker-div")))

# Get the current month and year as text
current_month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
current_year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

# Loop until December 2024
while not (current_month == "December" and current_year == "2024"):
    driver.find_element(By.XPATH, "//span[.='Next']").click()
    time.sleep(1)  # Small delay for the calendar to update
    current_month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    current_year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

# Select the 19th day
driver.find_element(By.XPATH, "//a[.='19']").click()

# Wait and close the browser
time.sleep(3)
driver.close()
