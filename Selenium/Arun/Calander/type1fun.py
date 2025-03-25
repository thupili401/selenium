import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")
driver.find_element(By.ID, "datepicker").click()
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.ID, "ui-datepicker-div")))

def calender_select(month,year,day):
    current_month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    current_year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    while not(current_month==month and current_year==year):
        driver.find_element(By.XPATH, "//span[.='Next']").click()
        current_month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
        current_year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    xpath_text="//a[.='"+day+"']"
    driver.find_element(By.XPATH,xpath_text).click()

calender_select("December","2026","19")
time.sleep(3)
driver.close()
