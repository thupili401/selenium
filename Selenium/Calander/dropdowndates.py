import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

Browser_Action=webdriver.ChromeOptions()
Browser_Action.add_argument('--disable-notification')
driver=webdriver.Chrome(options=Browser_Action)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://www.dummyticket.com/dummy-ticket-for-visa-application/')
driver.find_element(By.XPATH,"//input[@name='dob']").click()
date_month=Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']"))
date_month.select_by_visible_text("Dec")

date_year=Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']"))
date_year.select_by_visible_text("1988")

dt=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tr/td/a")
for i in dt:
    if i.text=='19':
        i.click()
        break

time.sleep(5)
driver.close()