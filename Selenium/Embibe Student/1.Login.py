import time

from selenium import webdriver
from selenium.webdriver.common.by import By
browser_actions=webdriver.ChromeOptions()
browser_actions.add_argument('--disable-notifications')
driver=webdriver.Chrome(options=browser_actions)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.embibe.com/")
driver.find_element(By.XPATH,"//button[@style='margin-right: 1rem;']").click()
driver.find_element(By.XPATH,"//input[@class='eds-text-field css-efet9v']").send_keys("9912866236")
driver.find_element(By.XPATH,"//button[@class='eds-btn eds-btn--secondary eds-btn--blunt-edge eds-btn--md sign_in_password_link']").click()
driver.find_element(By.XPATH,"//input[@class='eds-text-field--password-field css-efet9v']").send_keys("Embibe@123")
time.sleep(3)
driver.find_element(By.XPATH,"//button[@class='eds-btn eds-btn--primary eds-btn--capsular eds-btn--sm eds-btn--block proceed_btn']").click()
time.sleep(3)
# driver.find_element(By.XPATH,"//button[@id='react-burger-menu-btn']").click()#signout
# driver.find_element(By.XPATH,"//button[.='Sign Out']").click()
# time.sleep(3)
time.sleep(3)
driver.find_element(By.XPATH,"//button[.='Home']").click()
time.sleep(3)
driver.find_element(driver.find_elements(By.XPATH,"(//div[@class='sc-iMTnTL jQlcRy tile-wrapper big-book']")).click()
time.sleep(3)
driver.close()