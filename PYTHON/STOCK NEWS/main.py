import requests
import smtplib

my_email = '.17@gmail.com'
passkey = ''

stocks_api = 'https://www.alphavantage.co/query?'
stocks_apikey = ' '

news_apikey = ''

parameters_stocks = {}
received_stocks = requests.get(url=stocks_api)


parameters_stocks = {'function': '',
                     'apikey': ''}
received_stocks = requests.get(url=stocks_api, params=parameters_stocks)
data_stocks = received_stocks.json()

# top_gainers = [i for i in data_stocks['top_gainers']]
# company_symbol_profit = [
#     symbol['ticker'] for symbol in top_gainers
# ]
# company_profit = [profit['change_percentage'] for profit in top_gainers]

# top_losers = [i for i in data_stocks['top_losers']]
# company_symbol_loss = [
#     symbol['ticker'] for symbol in top_losers
# ]
# company_loss = [profit['change_percentage'] for profit in top_losers]

# gain_dict = dict(zip(company_symbol_profit, company_profit))
# loss_dict = dict(zip(company_symbol_loss, company_loss))

received_news = requests.get(
    'https://newsapi.org/v2/everything?q=stocks&apiKey=')
news_data = received_news.json()
articles = [i for i in news_data['articles']]
content = [i['content'] for i in articles]
with smtplib.SMTP('smtp.gmail.com') as request:
    request.starttls()
    request.login(user=my_email, password=passkey)
    message = f'Subject:Stocks\n\nprofit=\n\n\n\n\nloss=\n\n\nnews={content}'
    encoded_message = message.encode('utf-8')
    request.sendmail(from_addr=my_email, to_addrs='@gmail.com',
                     msg=encoded_message)
