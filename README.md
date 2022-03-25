# stock-news-model

Steps to perform:

STEP 1: Use https://www.alphavantage.co/documentation/#daily
When stock price increase/decreases by 5% between yesterday and the day before yesterday 
then print("Get News"). 

1. Get yesterday's closing stock price. performed list comprehensions on Python dictionaries.
   e.g. [new_value for (key, value) in dictionary.items()]
2. Get the day before yesterday's closing stock price
3. Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
   used abs() from:https://www.w3schools.com/python/ref_func_abs.asp
4. Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
5. If TODO4 percentage is greater than 5 then print("Get News").
6. Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
   
STEP 2: https://newsapi.org/
Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

7. Use Python slice operator to create a list that contains the first 3 articles.

STEP 3: Use twilio.com/docs/sms/quickstart/python 
to send a separate message with each article's title and description to your phone number. 

8. Create a new list of the first 3 article's headline and description using list comprehension.
9. Send each article as a separate message via Twilio.


#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
