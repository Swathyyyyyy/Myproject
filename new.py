from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
import sys

username = input('Enter your username: ')
password = input('Enter your password: ')

driver = webdriver.Chrome("chromedriver")

driver.get(" https://www.saucedemo.com/")
uname = driver.find_element("id", "user-name") 
uname.send_keys(username)
pword = driver.find_element("id", "password") 
pword.send_keys(password)
driver.find_element("name", "login-button").click()
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)

actualUrl="https://www.saucedemo.com/inventory.html" 
expectedUrl= driver.current_url
if expectedUrl == actualUrl:
        print("Login successful")
else:
        print("[!] Login failed")
        driver.close()
        sys.exit()
        
driver.maximize_window()
sleep(5)
driver.find_element("name","add-to-cart-sauce-labs-backpack").click()
driver.find_element("name","add-to-cart-sauce-labs-bike-light").click()
driver.find_element("name","add-to-cart-sauce-labs-bolt-t-shirt").click()



    



    

