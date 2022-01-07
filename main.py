import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


CHROMEDRIVER_PATH = "C:\Development\chromedriver.exe"
SIMILAR_ACCOUNT = "Kendall Jenner"

#Enter you details 
INSTA_USERNAME = "YOUR USERNAME"
INSTA_PASSWORD = "YOUR PASSWORD"


service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service)

driver.get('https://www.instagram.com')
driver.maximize_window()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, 'input[name="username"]').send_keys(INSTA_USERNAME)
driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys(INSTA_PASSWORD)
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, 'div.cTBqC').click()
driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Search Input"]').send_keys(SIMILAR_ACCOUNT)
driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Search Input"]').send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, 'a[class="-qQT3"]').click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, 'a.-nal3').click()
time.sleep(2)
followers = driver.find_elements(By.CSS_SELECTOR, 'ul.jSC57 li button')
for follower in followers[:10]:
    follower.click()
driver.close()







