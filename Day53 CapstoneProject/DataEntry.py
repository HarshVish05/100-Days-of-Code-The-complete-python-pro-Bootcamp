from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


website_link = "https://appbrewery.github.io/Zillow-Clone/"
form_link = " https://docs.google.com/forms/d/e/1FAIpQLSeH3PL0gehSx9uLDTg4ebPDkC0ba-qwb-ybyfomSHICYPSddA/viewform?usp=sf_link"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
    "Accept-Language": "en-US,en;q=0.9,en-IN;q=0.8",
}

contents = requests.get(url= website_link,headers= headers, verify= False).text

soup = BeautifulSoup(contents, 'html.parser')

links = [link.getText().replace('\n', '').replace('|', '').strip() for link in soup.find_all(name= 'a', class_ = 'StyledPropertyCardDataArea-anchor')]
prices = [price.getText().replace('+/mo', '').replace('/mo', '').replace('+ 1 bd', '') for price in soup.find_all(name= 'span', class_ = 'PropertyCardWrapper__StyledPriceLine')]
address = [add.getText().replace('|', '').replace('\n','').strip() for add in soup.find_all(name= 'address')]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)


for i in range(len(links)):
    driver.get(url= form_link)
# address_tag = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
# address_tag.send_keys(address[0])

# Wait for the address input to be clickable
    address_tag = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'))
    )
    # Scroll into view and interact
    driver.execute_script("arguments[0].scrollIntoView(true);", address_tag)
    address_tag.send_keys(address[i])

    price_tag = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_tag.send_keys(prices[i])

    link_tag = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_tag.send_keys(links[i])

    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()
    
    time.sleep(5)