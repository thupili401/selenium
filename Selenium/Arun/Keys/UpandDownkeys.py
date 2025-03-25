import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://omayo.blogspot.com/")
links = driver.find_elements(By.XPATH, "//div[@id='LinkList1']//a")
time.sleep(3)
actions=ActionChains(driver)
time.sleep(3)
for i in links:
    actions.key_down(Keys.CONTROL).click(i).key_up(Keys.CONTROL).perform()
    time.sleep(3)
time.sleep(3)
driver.quit()