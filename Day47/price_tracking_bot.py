from bs4 import BeautifulSoup
import requests
import smtplib
import os

# the pass and email are there in day32 birthday_email
my_email = os.getenv("MY_Email") 
password = os.getenv('password')

PRODUCT_URL = "https://www.amazon.in/Sparring-Punching-Training-Kickboxing-Hanging/dp/B07JW1Y4SV/ref=sr_1_7?crid=F03D4B45ACC8&dib=eyJ2IjoiMSJ9.j39biX-9NOKEXgoU-5FXD2EtxSBZJwFROt2UGFBieOXMfxvw3dYF20Jy_Tl_wF7sgOyUNXGRnQh_u-TN60U6FMm7yZOoyk35RnFOiYYKUm--JA3j86aOwq2r7SXjn2NZ7vPArz4e50JTPvx6mqAZc_sS4GaVkvRdwzc3N-EOxst6CH-GgCmDW7Kv4_WW4LrcPTCM2uKVEaAX4Rm_6lJeKN2p5X4WuQZU80881tA0NBbXwARy8EV2gwZaAax4uyCnpAUkpv1rf61wJAllFDhZmLN989tEWNPD7Ezwsd2o3Xc.nSnhsmgYRo7wU1zHl-a-Ywm8hXkpuHKDtRT3c1KB2pk&dib_tag=se&keywords=boxing%2Bbag%2Bfilled&qid=1720380222&sprefix=boxing%2Bba%2Caps%2C266&sr=8-7&th=1"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
    "Accept-Language": "en-US,en;q=0.9,en-IN;q=0.8",
}

response = requests.get(url= PRODUCT_URL, headers= headers, verify= False)
contents = response.text

soup = BeautifulSoup(contents, 'lxml')
price = float(soup.find(name= 'span', class_= "a-price-whole").getText().replace(',',''))
title = soup.find(name= 'span', id= 'productTitle').getText()
# print(title)

target_price = 2100.0

if price < target_price:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user= my_email, password=password)
        connection.sendmail(
            from_addr= my_email,
            to_addrs= '123havish123@gmail.com',
            msg= f"Subject: Price Alert for Boxing Bag\n\n{title}\n{PRODUCT_URL}"
        )


