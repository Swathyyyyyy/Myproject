from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
import sys

username = input('Enter your username: ')
password = input('Enter your password: ')
driver = webdriver.Chrome("chromedriver")
def test_valid_crentials_login(driver):
    driver.get('http://www.saucedemo.com/')

    driver.find_element(By.ID, 'user-name').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'login-button').click()

    if  "https://www.saucedemo.com/inventory.html" in  driver.current_url:
               print("Login successful")
    else:
                print("[!] Login failed")
            
def test_invalid_crentials_login(driver):
    driver.get('http://www.saucedemo.com')

    driver.find_element(By.ID, 'user-name').send_keys('locked_out_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    if driver.find_element(By.CSS_SELECTOR,'.error-button').is_displayed():
             print("Login failed")
test_invalid_crentials_login(driver)            
            

