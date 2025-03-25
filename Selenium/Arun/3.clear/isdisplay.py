from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
a=driver.find_element(By.ID,'ta1').is_displayed()
print(a)
#By using loop
if driver.find_element(By.ID,'ta1').is_displayed():
    print("displayed")
else:
    print("Not Displayed")