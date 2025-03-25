import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.fixture()
def setup_teardown():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://www.embibe.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//button[@class='eds-btn eds-btn--primary eds-btn--capsular eds-btn--md']").click()
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys('9912866236')
    driver.find_element(By.XPATH, "(//div[@class='eds-col-xs-12 eds-col-md-12 eds-col-lg-12'])[2]").click()
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Embibe@123")
    driver.find_element(By.XPATH,"//button[@class='eds-btn eds-btn--primary eds-btn--capsular eds-btn--sm eds-btn--block proceed_btn']").click()
    yield
    time.sleep(3)
    driver.quit()


def test_title(setup_teardown):
    expected_tile='Embibe Social Login Page'
    assert driver.title==expected_tile



def test_login(setup_teardown):
    driver.find_element(By.XPATH,"(//button[@class='eds-btn eds-btn--md eds-btn--link embibe-main-header__menu-item'])[4]").click()
    driver.find_element(By.XPATH,"(//div[@class='sc-gmgFlS lhsEjR'])[1]").click()