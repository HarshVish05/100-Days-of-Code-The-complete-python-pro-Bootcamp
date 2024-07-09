from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= chrome_options)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# print(article_count)
# article_count.click()

# all_portals = driver.find_element(By.LINK_TEXT, value= 'Content portals')
# # all_portals.click()

# searc_icon = driver.find_element(By.CLASS_NAME, value= 'mw-ui-icon-search')
# # searc_icon.send_keys(Keys.ENTER)
# searc_icon.click()

# search = driver.find_element(By.NAME, value='search')
# # sending keyboard input to selenium
# search.send_keys("Python")

# button = driver.find_element(By.CSS_SELECTOR, value= ".cdx-search-input button")
# button.click()

# challenge - fill this form with selenium
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value= 'fName')
last_name = driver.find_element(By.NAME, value= 'lName')
email_input = driver.find_element(By.NAME, value= 'email')
button = driver.find_element(By.TAG_NAME, 'button')

first_name.send_keys("Harsh")
last_name.send_keys("Vishwakarma")
email_input.send_keys("codeharshit@gmail.com")
button.click()




# driver.quit()