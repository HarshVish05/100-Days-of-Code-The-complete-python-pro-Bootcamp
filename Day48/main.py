from selenium import webdriver
from selenium.webdriver.common.by import By

PRODUCT_URL = "https://www.amazon.in/Sparring-Punching-Training-Kickboxing-Hanging/dp/B07JW1Y4SV/ref=sr_1_7?crid=F03D4B45ACC8&dib=eyJ2IjoiMSJ9.j39biX-9NOKEXgoU-5FXD2EtxSBZJwFROt2UGFBieOXMfxvw3dYF20Jy_Tl_wF7sgOyUNXGRnQh_u-TN60U6FMm7yZOoyk35RnFOiYYKUm--JA3j86aOwq2r7SXjn2NZ7vPArz4e50JTPvx6mqAZc_sS4GaVkvRdwzc3N-EOxst6CH-GgCmDW7Kv4_WW4LrcPTCM2uKVEaAX4Rm_6lJeKN2p5X4WuQZU80881tA0NBbXwARy8EV2gwZaAax4uyCnpAUkpv1rf61wJAllFDhZmLN989tEWNPD7Ezwsd2o3Xc.nSnhsmgYRo7wU1zHl-a-Ywm8hXkpuHKDtRT3c1KB2pk&dib_tag=se&keywords=boxing%2Bbag%2Bfilled&qid=1720380222&sprefix=boxing%2Bba%2Caps%2C266&sr=8-7&th=1"
# Chrome browser will close as soon as the program ends
# To keep the browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver  = webdriver.Chrome(options= chrome_options)
# driver.get(url= PRODUCT_URL)

# price = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# search_bar = driver.find_element(By.ID, "twotabsearchtextbox")
# print(search_bar.get_attribute("placeholder"))
# # print(price.tag_name)
# print(price.text)

#challenge get hold of all upcoming events from python website and store it in a dict

driver.get("https://www.python.org/events/")

event_list = driver.find_elements(By.CSS_SELECTOR, value=".event-title a")
# events = [event.text for event in event_list]
# print(events)

time_list = driver.find_elements(By.CSS_SELECTOR, value= "li p time")
# times = [time.text for time in time_list]
# print(times)

data = {}

for i in range(len(event_list)):
    data[i] = {'time': time_list[i].text, 'name': event_list[i].text}
    
print(data)



# driver.close()  # it only closes the active tab
driver.quit()   # it closes the whole browser