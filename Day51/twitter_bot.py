from selenium import webdriver
from selenium.webdriver.common.by import By
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
Twitter_Email = "karmadevishere05@gmail.com"
Twitter_Pass = "Lucifer@0599"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = 0
        self.up = 0
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)

        self.driver = webdriver.Chrome(options= chrome_options)
        
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        policy_btn = self.driver.find_element(By.ID, 'onetrust-accept-btn-handler')
        policy_btn.click()
        
        time.sleep(3)
        go_button = self.driver.find_element(By.CLASS_NAME, 'start-text')
        go_button.click()
        
        time.sleep(60)
        self.down = self.driver.find_element(By.CLASS_NAME, "result-data-large")
        print(self.down.text) 
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed")
        print(self.up.text) 
        
    
    def tweet_at_provider(self):
        self.driver.get("https://x.com/i/flow/login")
        time.sleep(5)
        input_tag = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        input_tag.send_keys(Twitter_Email)

        next_btn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span')
        next_btn.click()

        time.sleep(5)
        password_tag = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_tag.send_keys(Twitter_Pass)

        login_btn = self.driver.find_element('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div/span/span')
        login_btn.click()
        
        
        
speed = InternetSpeedTwitterBot()

# speed.get_internet_speed()
speed.tweet_at_provider()
