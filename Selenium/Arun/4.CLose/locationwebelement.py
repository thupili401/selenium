from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://tutorialsninja.com/demo/")
#Location_bodx=driver.find_element(By.XPATH,"//input[@class='form-control input-lg']").location
Location_bodx=driver.find_element(By.XPATH,"//input[@class='form-control input-lg']").rect
# by using .rect command we can find width height and cordiantions
print(Location_bodx)
