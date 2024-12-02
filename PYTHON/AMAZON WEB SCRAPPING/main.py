import requests,lxml
from bs4 import BeautifulSoup
URL="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_="
HEADERS = {
    "upgrade-insecure-requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,en-IN;q=0.8",
    "priority": "u=0, i",
    "x-forwarded-proto": "https",
    "x-https": "on",
    "X-Forwarded-For": "152.58.188.119"
}
resposne=requests.get(url=URL,headers=HEADERS)
soup=BeautifulSoup(resposne.text,"lxml")
price_whole = soup.select_one(".a-price-whole")
price_fraction = soup.select_one(".a-price-fraction")
price=float(price_whole.getText()+price_fraction.getText())
import smtplib

FROM_MY = ".17@yahoo.com"
TO = "@gmail.com"
SUBJ = "Price alert!!!!"
APP_PASSWORD = ""


MESSAGE = f"From: {FROM_MY}\nTo: {TO}\nSubject: {SUBJ}\n\nThe price is currently {price}"
if price<200:
    try:
        server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        server.starttls()
        server.login(user=FROM_MY, password=APP_PASSWORD)
        server.sendmail(from_addr=FROM_MY, to_addrs=TO, msg=MESSAGE)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()

