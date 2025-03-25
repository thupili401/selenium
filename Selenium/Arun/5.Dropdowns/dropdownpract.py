from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

Chrome_actions=webdriver.ChromeOptions()
Chrome_actions.add_argument("--disable-notifications")
driver=webdriver.Chrome(options=Chrome_actions)
driver.get("https://practice.expandtesting.com/dropdown")
drop_down=driver.find_element(By.XPATH,"//select[@id='country']")
select=Select(drop_down)
dropdown_options=select.options
for i in dropdown_options:
    print(i.text)