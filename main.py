import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
TWILIO_SID = "AC1498874af0097554fa2a0e957aaa1e76"
TWILIO_AUTH_TKN = "0ca0810d7ac2c40e23d1fe5d2fbcf1ab"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "interval": "5min",
    "apikey": "P0HM4GKCWWF3ECIG"
}

news_response = requests.get(STOCK_ENDPOINT, params=parameters)
data = news_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]


yesterday_data = data_list[0]
yesterday_closingprice = float(yesterday_data["4. close"])

dayb_yesterday = data_list[1]
dayb_yesterday_closingprice = float(dayb_yesterday["4. close"])


difference = abs(yesterday_closingprice - dayb_yesterday_closingprice)

percent = (difference / float(yesterday_closingprice)) * 100

print(percent)

if percent > 1:
    para = {
        "apikey": "cc94947cd3504922825f93714cf76843",
        "qInTitle": COMPANY_NAME
    }

    news_response = requests.get(url=NEWS_ENDPOINT, params=para)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    #print(three_articles)

    formatted_articles = [f"Headline: {item['title']}\n Brief: {item['description']}"
                          for item in three_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TKN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+15734051285",
            to="VerifiedNumber"
        )
        print(message.status)




