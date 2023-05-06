import requests
import smtplib
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
API="K9JBMRVREBOJWUCZ"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_api="744dc8784e464a7b8bdaddacf216f944"

my_email = "**************************"
my_password ="********************8"


response = requests.get(url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK_NAME}&apikey={API}")
response.raise_for_status()
data = response.json()
my_data=data["Time Series (Daily)"]
data_list = [value for key, value in my_data.items()]

yesterday_closing_stock = data_list[0]["4. close"]
daybeforeyesterday_closing_stock = data_list[1]["4. close"]

positive_difference = abs(float(yesterday_closing_stock)-float(daybeforeyesterday_closing_stock))
percentage_of_difference =float(positive_difference)/float(yesterday_closing_stock)*100

parameters={
    "qInTitle":COMPANY_NAME,
    "apiKEY":news_api,
}
if percentage_of_difference >5:
    news_response = requests.get(url=NEWS_ENDPOINT, params=parameters)
    news_data = news_response.json()
    trending_news=news_data["articles"]
    reports=trending_news[:2]

    list_title = str([report["title"] for report in reports])
    list_description =str([report["description"] for report in reports])
    list_url =str([report["url"] for report in reports])
    my_list =[list_title,list_url]
    print(my_list)


    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="********************",
                        msg=f"Subject:Drastic Change in stocks\n\nHeadline:{list_title.encode('utf-8')}, description:{list_description.encode('utf-8')},link:{list_url.encode('utf-8')}" )






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

