import requests
import json


class Customer:
    def newcustomer(self):
        self.name = input('Enter your name .\n')
        name = self.name
        self.email = input('Enter your email .\n')
        verification = input('Re-enter your email .\n')
        if self.email == verification and len(verification) != 0:
            with open('customer.txt', 'a') as file:
                file.write(f'{self.name.title()},{self.email}\n')
            api = 'https://api.sheety.co//untitledSpreadsheet/sheet1'
            body = {
                'sheet1': {
                    'name': self.name,
                    'email': self.email
                }
            }

            result = requests.post(url=api, json=body)
        else:
            print('Your entered a wrong email.')
