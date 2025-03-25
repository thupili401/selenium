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
button=driver.find_element(By.XPATH,"//button[contains(text(),'Double-Click Me To See Alert')]")
act=ActionChains(driver)
act.double_click(button).perform()
time.sleep(3)
driver.close()