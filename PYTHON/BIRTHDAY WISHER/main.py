import pandas
import datetime
import smtplib
import random
my_email = '.17@gmail.com'
password = ''

data = pandas.read_csv('birthdays.csv')
data_dict = data.to_dict()

date = datetime.datetime.now()
day = date.day
month = date.month

with open('./letter_templates/letter_1.txt') as File:
    letter_1 = File.read()
with open('./letter_templates/letter_2.txt') as File:
    letter_2 = File.read()
with open('./letter_templates/letter_3.txt') as File:
    letter_3 = File.read()
letter = [letter_1, letter_2, letter_3]

i = 0
while i < len(data_dict['day']):
    if day == data_dict['day'][i]:
        if month == data_dict['month'][i]:
            message = random.choice(letter)
            new_message = message.replace('[NAME]', data_dict['name'][i])
            connection = smtplib.SMTP('smtp.gmail.com')
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=data_dict['email'][i], msg=f'Subject:Happy Birthday\n\n{new_message}')
            connection.close()
    i += 1
