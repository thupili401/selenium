import time

from selenium import webdriver
from selenium.webdriver.common.by import By
Browser_actions=webdriver.ChromeOptions()
Browser_actions.add_argument('--disable-notifications')
driver=webdriver.Chrome(options=Browser_actions)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://jqueryui.com/datepicker/")
driver.switch_to.frame(0)
#driver.find_element(By.XPATH,"//input[@class='hasDatepicker']").send_keys('06/30/2024')#
year="2024"
Month="August"
date="15"

#//div[@class='DayPicker-wrapper']/div[2]/div[1]/div[3]/div/div/div/p[text()='26']
driver.find_element(By.XPATH,"//input[@class='hasDatepicker']").click()

while True:
    mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yer=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if year==yer and Month==mon:
        break
    else:
        driver.find_element(By.XPATH,"//a[@class='ui-datepicker-next ui-corner-all']").click()

dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tr/td/a")

for i in dates:
    if i.text==date:
        i.click()
        break



time.sleep(3)
driver.close()