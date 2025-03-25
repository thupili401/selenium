import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://ps.uci.edu/~franklin/doc/file_upload.html")
driver.maximize_window()
upload=driver.find_element(By.XPATH,"//input[@name='userfile']").send_keys("/Users/sreekantht/Desktop/AlekhyaMResume .pdf")
time.sleep(3)

