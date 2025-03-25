import time

from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
driver=webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
checkbox=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkbox))
for i in checkbox:
    i.click()
time.sleep(3)
driver.close()