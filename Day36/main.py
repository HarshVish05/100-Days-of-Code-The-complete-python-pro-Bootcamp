import requests
import os
from twilio.rest import Client

# this also worked in replit because of certificate error
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY_ALPHA = os.getenv("ALPHAVANTAGE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token  = os.getenv("TWILIO_AUTH_TOKEN")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    # "interval": "60min",
    "apikey": API_KEY_ALPHA
}
price = requests.get(url= "https://www.alphavantage.co/query", params= parameter, verify= False) 
price.raise_for_status()
stock_data = price.json()['Time Series (Daily)']
stock_data_list = [value for key,value in stock_data.items()]

yesterday_stock_price = stock_data_list[0]['4. close']
daybeforeyesterday_stock_price = stock_data_list[1]['4. close']
# print(yesterday_stock_price)

difference = abs(float(yesterday_stock_price) - float(daybeforeyesterday_stock_price))
diff_percent = (difference / float(yesterday_stock_price)) * 100
# print(diff_percent)



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
parameter_for_news = {
    "q": COMPANY_NAME,
    "apikey": NEWS_API_KEY
} 
get_news = requests.get(url= "https://newsapi.org/v2/everything", params= parameter_for_news, verify= False)
if diff_percent > -1:
    # print("Good news")
    articles = get_news.json()['articles']
    three_articles = articles[:3]
    print(three_articles[0]['description'])
    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    # alert_message = three_articles[0]['description']

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
    
    
    client = Client(account_sid, auth_token)
    
    for article in formatted_articles:
        message = client.messages.create(
            body = article,
            from_ = "+12093077352",
            to = "+918777656566",
        )


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

