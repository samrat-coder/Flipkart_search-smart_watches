import time

from pytest_bdd import when, parsers
from selenium.webdriver.common.by import By
from webdriver_manager import driver

@when(parsers.cfparse("User search item '{smart_watches}'"))
def search_item(driver, smart_watches):
   time.sleep(5)
   search = driver.find_element(By.XPATH, "//input[@name='q']")
 # search.click()
   search.send_keys(smart_watches)
   submit = driver.find_element(By.XPATH, "//button[@type='submit']")
   submit.click()
   time.sleep(10)


