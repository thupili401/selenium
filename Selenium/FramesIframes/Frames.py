import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html')
# driver.switch_to.frame("0") #here we need keep either name of the frame or ID of the frame or webelement or 0
driver.find_element(By.LINK_TEXT,'org.openqa.selenium').click()
# driver.switch_to.default_content() #go to back main page

# driver.switch_to.frame("0")
driver.find_element(By.LINK_TEXT,'AcceptedW3CCapabilityKeys').click()
# driver.switch_to.default_content() #go to back main page

# driver.switch_to.frame("0")
driver.find_element(By.XPATH, "//a[text()='Help']").click()