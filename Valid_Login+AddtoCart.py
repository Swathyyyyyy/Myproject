from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep

username = input('Enter your username: ')
password = input('Enter your password: ')

driver = webdriver.Chrome("chromedriver")

driver.get(" https://www.saucedemo.com/")
def test_valid_crentials_login(driver):
    driver.get('http://www.saucedemo.com')

    driver.find_element(By.ID, 'user-name').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'login-button').click()

    if  "https://www.saucedemo.com/inventory.html" in  driver.current_url:
               print("Login successful")
    else:
                print("[!] Login failed")

#Add to cart
driver.maximize_window()
sleep(5)
driver.find_element("name","add-to-cart-sauce-labs-backpack").click()
driver.find_element("name","add-to-cart-sauce-labs-bike-light").click()
driver.find_element("name","add-to-cart-sauce-labs-bolt-t-shirt").click()
