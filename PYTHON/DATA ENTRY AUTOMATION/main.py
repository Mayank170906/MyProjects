import data
import time
datas=data.data_extractor.give_data()
print(datas)


google_docs_link="https://docs.google.com/forms/d/e/1FAIpQLSekKz5-Jcw_GFQBUmeYFMf7v2qako6tvm5vIuOUKLKmdwN9Gw/viewform?usp=sf_link"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

settings=webdriver.EdgeOptions()
settings.add_experimental_option('detach',True)

bot=webdriver.Edge(options=settings)
bot.maximize_window()

bot.get(google_docs_link)

time.sleep(5)
adress_xpath="/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input"
price_xpath="/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input"
link_xpath="/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input"


wait=WebDriverWait(bot,5)
for i in range(len(datas['price'])):
    adress=wait.until(EC.presence_of_element_located((By.XPATH,adress_xpath)))
    price=wait.until(EC.presence_of_element_located((By.XPATH,price_xpath)))
    link=wait.until(EC.presence_of_element_located((By.XPATH,link_xpath)))

    adress.send_keys(datas["price"][i])
    price.send_keys(datas['adress'][i])
    link.send_keys(datas['link'][i])

    submit_xpath="/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span"
    submit=wait.until(EC.presence_of_element_located((By.XPATH,submit_xpath)))
    submit.click()
    time.sleep(2)
    bot.get(google_docs_link)

