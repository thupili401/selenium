from datetime import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://omayo.blogspot.com/")
drop_down=driver.find_element(By.XPATH,"//select[@class='combobox']")
select=Select(drop_down)
select.select_by_visible_text('doc 1')
options=driver.find_elements(By.XPATH,"//div[@class='widget HTML' and @id='HTML1']//div//select//option")
for i in options:
    print(i.text)

driver.close()