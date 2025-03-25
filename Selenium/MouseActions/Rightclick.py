import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
Browser_Actions=webdriver.ChromeOptions()
Browser_Actions.add_argument('--disable-notifications')
driver=webdriver.Chrome(options=Browser_Actions)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
button=driver.find_element(By.XPATH,"//span[contains(text(),'right click me')]")
act=ActionChains(driver)
act.context_click(button).perform()
time.sleep(3)