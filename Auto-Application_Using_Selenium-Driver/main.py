from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


Chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(Chrome_driver_path)
driver.get("https://www.linkedin.com/home")

# for Sign in page

sign_in = driver.find_element(By.XPATH, "/html/body/nav/div/a[2]")
sign_in.click()

user_name = driver.find_element(By.ID, "username")
user_name.send_keys("surya@gmail.com")
time.sleep(2)
password = driver.find_element(By.ID, "password")
password.send_keys("xxxxx")

sign_inside = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign_inside.click()

job_click = driver.find_element(By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]/a')
job_click.click()


search = driver.find_element(By.CSS_SELECTOR, ".jobs-search-box__keywords-label + input")

search.send_keys("web development")
search.send_keys(Keys.ENTER)
time.sleep(2)