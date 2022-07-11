import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

list=[]
list2=[]
driver = webdriver.Chrome(executable_path = 'E:\\Workspace\\Selenium webdriver\\chromedriver.exe')

driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')

driver.find_element(By.XPATH,'//*[@class="search-keyword"]').send_keys('ber')
time.sleep(5)

buttons = driver.find_elements(By.XPATH,'//*[@class="product-action"]/button')

for button in buttons:
    list.append(button.find_element(By.XPATH,'parent::div/parent::div/h4').text)
    button.click()
print(list)

driver.find_element(By.XPATH,'//*[@alt="Cart"]').click()

driver.find_element(By.XPATH,'//*[contains(text(),"PROCEED TO CHECKOUT")]').click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@class="promoCode"]')))

veggies = driver.find_elements(By.CSS_SELECTOR,'p.product-name')
for veggie in veggies:
    list2.append(veggie.text)
print(list2)

assert list == list2


driver.find_element(By.XPATH, '//*[@class="promoCode"]').send_keys('rahulshettyacademy')
TotalAmt = driver.find_element(By.CSS_SELECTOR,'span.totAmt').text
print(TotalAmt)
driver.find_element(By.XPATH, '//*[@class="promoBtn"]').click()

wait.until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@class="promoInfo"]')))
print(driver.find_element(By.XPATH,'//*[@class="promoInfo"]').text)

DiscountAmt= driver.find_element(By.CSS_SELECTOR,'span.discountAmt').text
print(DiscountAmt)

assert float(DiscountAmt) < float(TotalAmt)

amounts = driver.find_elements(By.XPATH,'//tr//td[5]/p')

sum = 0
for amount in amounts:
    sum = sum + int(amount.text)
print(sum)

Totamts = int(driver.find_element(By.CSS_SELECTOR, 'span.totAmt').text)

assert sum == Totamts







