import time

from pytest_bdd import when, parsers
from selenium.webdriver.common.by import By
from webdriver_manager import driver

@when("User close login window")
def login_window(driver):
  close = driver.find_element(By.XPATH,  "//button[@class='_2KpZ6l _2doB4z']")
  close.click()
  time.sleep(5)