import time

from selenium import webdriver
from selenium.webdriver.common.by import By
Chrome_options=webdriver.ChromeOptions()
Chrome_options.add_argument('--headless')
driver=webdriver.Chrome(options=Chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.hdfc.com/")
total_width=driver.execute_script("return document.body.scrollWidth")
total_height = driver.execute_script("return document.body.scrollHeight")
driver.set_window_size(total_width,total_height)
page_body=driver.find_element(By.TAG_NAME,"body")
page_body.screenshot('bigpage.png')
time.sleep(3)
driver.close()