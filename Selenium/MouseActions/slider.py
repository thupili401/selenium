from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
Browser_Actions=webdriver.ChromeOptions()
Browser_Actions.add_argument('--disable-notifications')
driver=webdriver.Chrome(options=Browser_Actions)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.icicibank.com/personal-banking/loans/personal-loan/emi-calculator")
driver.find_element(By)