import smtplib
import requests


class NotificationManager:
    def __init__(self):
        url = 'https://api.sheety.co//untitledSpreadsheet/sheet1'
        data = requests.get(url=url)
        data_json = data.json()
        self.customer = [i['email'] for i in data_json['sheet1']]
        if len(self.customer) == 0:
            raise Exception('No customers')

    def send_mail(self, msg):
        my_email = '.17@gmail.com'
        passkey = ''
        with smtplib.SMTP('smtp.gmail.com') as server:
            message = f'Subject:Flight Price Alert\n\n{msg}'
            server.starttls()
            server.login(user=my_email, password=passkey)
            server.sendmail(from_addr=my_email, to_addrs=self.customer,
                            msg=message)
