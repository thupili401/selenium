from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://omayo.blogspot.com/")
a=driver.find_element(By.ID,'ta1').get_attribute('cols')
print(a)
driver.close()