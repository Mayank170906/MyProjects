import requests
import datetime


class FlightSearch:
    def data(self, fly_from, fly_to, date_from, date_to):
        try:
            Tequila_api_url = 'https://api.tequila.kiwi.com/v2/search?'
            params = {
                "fly_from": fly_from,
                'fly_to': fly_to,
                'date_from': date_from,
                'date_to': date_to
            }
            header = {
                'apikey': ''
            }
            received = requests.get(url=Tequila_api_url,
                                    params=params, headers=header)
            return received.json()
        except:
            raise Exception('No flights')

    def price(self, fly_from, fly_to, date_from, date_to):
        try:
            new_data = FlightSearch.data(
                self, fly_from, fly_to, date_from, date_to)
            return new_data['data'][0]['price']
        except:
            raise Exception('No flight')
