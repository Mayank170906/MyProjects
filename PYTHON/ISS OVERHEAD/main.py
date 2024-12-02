import requests
import datetime
import smtplib

my_email = '.17@gmail.com'
password = ''


def send_mail():
    with smtplib.SMTP('smtp.gmail.com') as connect:
        connect.starttls()
        connect.login(user=my_email, password=password)
        connect.sendmail(from_addr=my_email,
                         to_addrs='@gmail.com', msg="HI")


parameters = {
    'lat': 32.883854,
    'lng': -96.965538,
    'formatted': 0
}
received = requests.get(
    url='https://api.sunrise-sunset.org/json', params=parameters)
data = received.json()
sunrise = (data['results']['sunrise'])
sunset = (data['results']['sunset'])
sunrise_time = sunrise.split('T')[1].split(':')[0]
sunset_time = sunset.split('T')[1].split(':')[0]
current_time = datetime.datetime.now().hour
del data

response = requests.get(url='http://api.open-notify.org/iss-now.json')
data = response.json()
lat = float(data['iss_position']['latitude'])
lng = float(data['iss_position']['longitude'])

if int(lat) <= int(32.883854)+5 and int(lat) >= int(32.883854)-5:
    if int(lng) <= int(-96.965538)+5 and int(lng) >= int(-96.965538)-5:
        if int(current_time) > int(sunrise_time) and int(current_time) < int(sunset_time):
            send_mail()

else:
    send_mail()
