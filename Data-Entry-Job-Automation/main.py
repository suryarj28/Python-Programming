import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

place_url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.70222002536713%2C%22east%22%3A-122.1625166562265%2C%22south%22%3A37.64980171507572%2C%22north%22%3A37.96391183448605%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(url=place_url, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")
time.sleep(2)
# print(soup.prettify())

property_link = soup.find_all(class_="property-card-link")
# print(property_link)

all_links = []

for link in property_link:
    href = link["href"]
    # print(href)
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

print(all_links)



prices = soup.find_all(class_="StyledPropertyCardDataArea-c11n-8-69-2__sc-yipmu-0 kJFQQX")

costs = []

for price in prices:
    # print(price)
    costs.append(price.text.split("+")[0])
print(costs)


adress = soup.find_all(class_="StyledPropertyCardDataArea-c11n-8-69-2__sc-yipmu-0 dZxoFm property-card-link")

adresses = []

for location in adress:
    adresses.append(location.text.split("|")[-1])
print(adresses)

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

for n in range(len(all_links)):
    # Substitute your own Google Form URL here 👇
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfULFirdsSP3ZY3JWoDZX1WHi38tQH4pvY7xUH8FLUBJ9DyAQ/viewform?usp=sf_link")

    time.sleep(2)
    address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    time.sleep(2)
    price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    time.sleep(2)
    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    time.sleep(2)
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')

    address.send_keys(adresses[n])
    price.send_keys(costs[n])
    link.send_keys(all_links[n])
    submit_button.click()
