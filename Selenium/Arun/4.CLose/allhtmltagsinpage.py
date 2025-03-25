from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://tutorialsninja.com/demo/index.php?route=product/manufacturer/info&manufacturer_id=7")
url=driver.find_elements(By.XPATH,'//a')
for i in url:
    print(i.get_attribute('href'))

driver.quit()