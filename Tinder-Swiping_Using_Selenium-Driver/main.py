import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep


chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)
driver.maximize_window()

driver.get("https://tinder.com/")
time.sleep(3)

# Accept
agree = driver.find_element(By.XPATH, '//*[@id="o-98920890"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
agree.click()
time.sleep(5)

login = driver.find_element(By.XPATH, '//*[@id="o-98920890"]/div/div[1]/div/div/main/div/div[2]/div/div[3]/div/div/button[2]/div[2]/div[2]')
login.click()
time.sleep(5)

more_option = driver.find_element(By.XPATH, '//*[@id="s1659711021"]/div/div/div[1]/div/div/div[3]/span/button')
more_option.click()
time.sleep(5)


fb_account_login = driver.find_element(By.XPATH, '//*[@id="s1659711021"]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]')
fb_account_login.click()


base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)


email_input = driver.find_element(By.XPATH, '//*[@id="email"]')
email_input.send_keys("9629824650")
time.sleep(2)

password_input = driver.find_element(By.XPATH, '//*[@id="pass"]')
password_input.send_keys("suryalovekuttima")
time.sleep(3)

password_input.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

time.sleep(10)
allow_location_button = driver.find_element(By.XPATH, '//*[@id="s1659711021"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
notifications_button = driver.find_element(By.XPATH, '//*[@id="s1659711021"]/div/div/div/div/div[3]/button[2]/span')
notifications_button.click()
# cookies = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
# cookies.click()

