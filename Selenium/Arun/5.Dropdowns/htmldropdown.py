import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

Chrome_options=webdriver.ChromeOptions()
Chrome_options.add_argument("disable-notifications")
driver=webdriver.Chrome(options=Chrome_options)
driver.get("https://omayo.blogspot.com/")
drop_down=driver.find_element(By.XPATH,"//select[@class='combobox']")
select= Select(drop_down)
dropdown_options=select.options
for i in dropdown_options:
    print(i.text)
    
select.select_by_visible_text("doc 1")
# select.select_by_index(3)
# select.select_by_value("mno")

time.sleep(5)
driver.close()