import pandas as pd
import smtplib
user_file=input("location of your excel file\n")
df=pd.read_excel(user_file)
user_coln=input("enter the column containing gmail\n")
users=df[user_coln].to_list()
print(users)
FROM_MY = input("Enter your email id\n")
MY_PASSWORD = input("enter your app password\n")
SEND_TO=users
SUBJ = input("Enter the subject\n")
BODY=input("Enter the body\n")
MESSAGE = f"From:{FROM_MY}\nTo:{SEND_TO}\nSubject:{SUBJ}\n\n{BODY}"
connection = smtplib.SMTP("smtp.mail.yahoo.com", 587)
connection.starttls()
connection.login(FROM_MY, MY_PASSWORD)
connection.sendmail(from_addr=FROM_MY, to_addrs=SEND_TO, msg=MESSAGE)
