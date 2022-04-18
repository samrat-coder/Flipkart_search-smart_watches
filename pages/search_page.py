import csv

from pytest_bdd import when, then
from selenium.webdriver.common.by import By


@then('User gets name and prices of the items')
def search_item(driver):
   name_elems = driver.find_elements(By.XPATH, "//div[@class='_4rR01T']")
   price_elems = driver.find_elements(By.XPATH, "//div[@class='_30jeq3 _1_WHN1']")

   for i in range(len(name_elems)):
      print(name_elems[i].text)
      print(price_elems[i].text)

   with open('result.csv', 'w') as f:
      thewriter = csv.writer(f)
      thewriter.writerow(['Name', 'Price'])
      for i in range(len(name_elems)):
         thewriter.writerow([name_elems[i].text, price_elems[i].text])
