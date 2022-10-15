from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"

SIMILAR_ACCOUNT = "chefsteps"
USER_NAME = "im-surya"
PASSWORD = "yyyyyy"


class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        self.driver.maximize_window()
        time.sleep(2)
        username = self.driver.find_element(By.NAME, 'username')
        username.send_keys(USER_NAME)
        time.sleep(3)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(PASSWORD)
        time.sleep(2)
        inside = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        inside.click()
        time.sleep(3)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        time.sleep(5)
        followers = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mount_0_0_uS"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div/text()'))).click()

        followers.click()
        time.sleep(5)

    def follow(self):
        modal = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

            try:
                follow_button = self.driver.find_element(By.XPATH, "eqwr")
                follow_button.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, "wety")
                cancel_button.click()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
