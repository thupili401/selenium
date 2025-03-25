import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://omayo.blogspot.com/")
time.sleep(5)
driver.find_element(By.TAG_NAME,'textarea').send_keys("Sreekanth is good boy")
time.sleep(5)
links=driver.find_elements(By.TAG_NAME,'a')
print(len(links))
for i in links:
    print(i.get_attribute("href"))
driver.quit()