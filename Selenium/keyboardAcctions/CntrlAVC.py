import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
browser_actions=webdriver.ChromeOptions()
browser_actions.add_argument('--disable-notifications')
driver=webdriver.Chrome(options=browser_actions)
driver.implicitly_wait(10)
driver.get("https://gotranscript.com/text-compare")
driver.maximize_window()
tab1=driver.find_element(By.XPATH,"//textarea[@name='text1']")
tab2=driver.find_element(By.XPATH,"//textarea[@name='text2']")
tab1.send_keys("Welcome Sreekanth")
act=ActionChains(driver)
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
act.send_keys(Keys.TAB).perform()
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(5)