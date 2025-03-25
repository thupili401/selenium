import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
Browser_Actions=webdriver.ChromeOptions()
Browser_Actions.add_argument('--disable-notifications')
driver=webdriver.Chrome(options=Browser_Actions)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://stqatools.com/demo/MouseHover.php")
a=driver.find_element(By.XPATH,"//button[@class='dropbtn']")
b=driver.find_element(By.XPATH,"//a[@type='button' and contains(text(),'Link 2')]")
act=ActionChains(driver)
act.move_to_element(a).move_to_element(b).click().perform()
time.sleep(5)
driver.close()