from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
c=driver.find_elements(By.XPATH,"//table[@id='table1']//tr")
for i in c:
    print(i.text)

