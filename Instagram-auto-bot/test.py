from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get("https://www.instagram.com/chefsteps/")
driver.maximize_window()
time.sleep(5)



