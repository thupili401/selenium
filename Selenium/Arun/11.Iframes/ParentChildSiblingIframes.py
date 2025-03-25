from selenium import webdriver
from selenium.webdriver.common.by import By
Chrome_Actions=webdriver.ChromeOptions()
Chrome_Actions.add_argument("--disable-notifications")
driver=webdriver.Chrome(options=Chrome_Actions)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/nested_frames")
driver.switch_to.frame("frame-top")
driver.switch_to.frame("frame-left")
text1=driver.find_element(By.XPATH,"//*[contains(text(),'LEFT')]").text
print(text1)
driver.switch_to.parent_frame()
driver.switch_to.frame("frame-middle")
text2=driver.find_element(By.XPATH,"//*[contains(text(),'MIDDLE')]").text
print(text2)
driver.switch_to.parent_frame()
driver.switch_to.frame("frame-right")
text3=driver.find_element(By.XPATH,"//*[contains(text(),'RIGHT')]").text
print(text3)
driver.switch_to.default_content()
driver.switch_to.frame("frame-bottom")
text4=driver.find_element(By.XPATH,"//*[contains(text(),'BOTTOM')]").text
print(text4)