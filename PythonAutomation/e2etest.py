from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path = "E:\\Workspace\\Selenium webdriver\\chromedriver.exe")
driver.get('https://www.rahulshettyacademy.com/angularpractice/')

driver.find_element(By.CSS_SELECTOR,'a[href*="shop"]').click()
products = driver.find_elements(By.XPATH,'//*[@class="card h-100"]')

for product in products:
    productName = product.find_element(By.XPATH,'div/h4/a').text
    if productName == "Blackberry":
        product.find_element(By.XPATH,'div/button').click()

driver.find_element(By.XPATH,'//*[@class="nav-link btn btn-primary"]').click()
driver.find_element(By.XPATH,'//*[@class="btn btn-success"]').click()
driver.find_element(By.XPATH,'//*[@id="country"]').send_keys('ind')

wait = WebDriverWait(driver,7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,'India')))
driver.find_element(By.LINK_TEXT,'India').click()

driver.find_element(By.XPATH,'//div[@class="checkbox checkbox-primary"]').click()
driver.find_element(By.CSS_SELECTOR,'[type="submit"]').click()
tex = driver.find_element(By.CLASS_NAME, 'alert-success').text
print(tex)
assert str("Success! Thank you! Your order will be delivered in next few weeks :-).") == tex
