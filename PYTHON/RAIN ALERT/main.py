import requests
from twilio.rest import Client
import smtplib

my_email = '.17@gmail.com'
passkey = ''
account_sid = ''
auth_token = ''

api_key = ''
parameters = {
    'lat': 28.680553,
    'lon':  77.224005,
    'appid': api_key
}


received = requests.get(
    url='https://api.openweathermap.org/data/2.5/weather?', params=parameters)
data = received.json()
weather = data['weather'][0]
weather_description = weather['description']
weather_main = weather['main']
weather_id = weather['id']
cloud = data['clouds']['all']
if weather_id <= 700:
    # client = Client(account_sid, auth_token)

    # message = client.messages.create(
    #     body='Bring your umbrella it will rain.',
    #     from_='+',
    #     to='+'
    # )
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=passkey)
        connection.sendmail(from_addr=my_email, to_addrs='@gmail.com ',
                            msg='Subject:Weather\n\nIt will rain today morning.')

    # print(message.status)
else:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=passkey)
        connection.sendmail(from_addr=my_email, to_addrs='@gmail.com ',
                            msg='Subject:Weather\n\nIt will not rain today morning.')
