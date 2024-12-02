import requests
from flight_data import FlightData


class DataManager:

    def data(self):
        self.sheety_flighDeals_Api_url = 'https://api.sheety.co//flightDeals/prices'
        self.received = requests.get(url=self.sheety_flighDeals_Api_url)
        self.data_json = self.received.json()
        self.data = self.data_json['prices']
        if len(self.data) == 0:
            raise Exception('No locations')
        return self.data

    def update_data(self):
        for data in self.data():
            url = f'{self.sheety_flighDeals_Api_url}/{data["id"]}'
            city = data['city']
            iata_code = FlightData.iata_code(city)
            new_data = {
                "price": {
                    "iataCode": iata_code
                }
            }
            sent = requests.put(url=url, json=new_data)
