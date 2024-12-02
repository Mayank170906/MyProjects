# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import datetime
from customer import Customer
is_true = True
while is_true:
    user = input('Do you want to add customer ?\ny for yes\nn for no\n')
    if user == 'y':
        Customer().newcustomer()
    elif user == 'n':
        is_true = False
    else:
        print('Invalid input !\nTry again')
dataManager = DataManager()
data = dataManager.data()
# dataManager.update_data()

city_prices = [(i['iataCode'], i['lowestPrice']) for i in data]
today = datetime.datetime.now().strftime('%d/%m/%Y')
today = datetime.datetime.now()
date_from = f'{today.day}/{today.month}/{today.year}'
date_to = (today + datetime.timedelta(days=7)).strftime('%d/%m/%Y')
fly_from = 'BOM'
for i in city_prices:
    city = i[0]
    lowest_price = i[1]
    flight = FlightSearch()
    price = flight.price(fly_from=fly_from, fly_to=city,
                         date_from=date_from, date_to=date_to)
    if price < lowest_price:
        message = f'You can visit {city}\nTicket price:{price}\nLowest_price={lowest_price}'
        NotificationManager().send_mail(message)
