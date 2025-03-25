from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
c=driver.find_element(By.XPATH,"//table[@id='table1']//tr[2]").text
print(c)