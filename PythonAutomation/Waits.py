import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path='E:\\Workspace\\Selenium webdriver\\chromedriver.exe')
#driver.implicitly_wait(10)
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.maximize_window()

driver.find_element(By.XPATH,'//*[contains(@type,"search")]').click()
driver.find_element(By.XPATH,'//*[contains(@type,"search")]').send_keys('ber')
time.sleep(4)

counts = len(driver.find_elements(By.XPATH,'//div[@class="products"]/div'))
assert counts == 3

buttons = driver.find_elements(By.XPATH,"//div[@class='product-action']/button")

for button in buttons:
    button.click()

driver.find_element(By.XPATH,'//*[contains(@class,"cart-icon")]').click()
driver.find_element(By.XPATH,'//button[contains(text(),"PROCEED TO CHECKOUT")]').click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//*[contains(@class,'promoCode')]")))

driver.find_element(By.XPATH, "//*[contains(@class,'promoCode')]").send_keys('rahulshettyacademy')
driver.find_element(By.XPATH,'//*[contains(@class,"promoBtn")]').click()

wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//*[contains(@class,'promoInfo')]")))
print(driver.find_element(By.XPATH,'//*[contains(@class,"promoInfo")]').text)





