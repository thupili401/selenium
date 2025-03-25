from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

actions = ActionChains(driver)
driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")

driver.find_element(By.ID, "input-firstname").send_keys("Sreekanth")
actions.send_keys(Keys.TAB).send_keys("T").send_keys(Keys.TAB)\
    .send_keys("abc@gmail.com").send_keys(Keys.TAB)\
    .send_keys("9912866234").send_keys(Keys.TAB)\
    .send_keys("12345").send_keys(Keys.TAB)\
    .send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB)\
    .send_keys(Keys.SPACE).send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()

driver.quit()
