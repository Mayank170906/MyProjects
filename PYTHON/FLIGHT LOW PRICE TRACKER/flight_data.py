import requests


class FlightData:
    def iata_code(country):
        try:
            Tequila_api_url = 'https://api.tequila.kiwi.com/locations/query?'
            header = {
                'apikey': '-18M'}
            parameters = {
                'term': country
            }
            data = requests.get(url=Tequila_api_url,
                                params=parameters, headers=header)
            data_json = data.json()

            return data_json['locations'][0]['code']
        except:
            raise Exception('Inavalid location')
