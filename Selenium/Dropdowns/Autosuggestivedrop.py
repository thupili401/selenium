import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.makemytrip.com/?srsltid=AfmBOopq-tq_WM0LnL8Y7ZNx1dt5o2BXiZDmHUoXppMMGGZRtGWDV_1i")
time.sleep(5)
driver.find_element(By.ID,"fromCity").click()
driver.find_element(By.XPATH,"//*[@aria-autocomplete='list']").send_keys("g")
time.sleep(3)
actions=ActionChains(driver)
# actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
# time.sleep(3)
# driver.quit()
for i in range(10):
    actions.send_keys(Keys.ARROW_DOWN)
actions.send_keys(Keys.ENTER).perform()
time.sleep(3)
driver.quit()