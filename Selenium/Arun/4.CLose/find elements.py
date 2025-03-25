from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://omayo.blogspot.com/")
options=driver.find_elements(By.XPATH,"//select[@id='multiselect1']/option")
print("total_Options:",len(options))
for i in options:
    print((i.text))