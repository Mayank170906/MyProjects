import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

settings=webdriver.EdgeOptions()
settings.add_experimental_option("detach",True)

bot=webdriver.Edge(options=settings)
bot.get('http://orteil.dashnet.org/experiments/cookie/')
bot.maximize_window()


def cokkie_clicker():
    while True:
        button_cokkie=bot.find_element(By.ID,'cookie')
        button_cokkie.click()

def buy_Cursor():
    button_cursor=bot.find_element(By.ID,value='buyCursor')
    button_cursor.click()
    print("Bought Cursor")

def money():
    amount=bot.find_element(By.XPATH,value='//*[@id="money"]')
    return int(amount.text)
def purchase():
    while True:
        time.sleep(5)
        try: 
            button_time_machine=bot.find_element(By.ID,value='buyTime machine')
            if button_time_machine.get_attribute('class')!='grayed':
                button_time_machine.click()
                print("Bought TimeMachine")
                continue
            button_Portal=bot.find_element(By.ID,value='buyPortal')
            if button_Portal.get_attribute('class')!='grayed':
                button_Portal.click()
                print("Bought Portal")
                continue
            button_Alchemy=bot.find_element(By.ID,value='buyAlchemy lab')
            if button_Alchemy.get_attribute('class')!='grayed':
                button_Alchemy.click()
                print("Bought Alchemy")
                continue
            button_Shipment=bot.find_element(By.ID,value='buyShipment')
            if button_Shipment.get_attribute('class')!='grayed':
                button_Shipment.click()
                print("Bought Shipment")
                continue
            button_mine=bot.find_element(By.ID,value='buyMine')
            if button_mine.get_attribute('class')!='grayed':
                button_mine.click()
                print("Bought Mine")
                continue
            button_factory=bot.find_element(By.ID,value='buyFactory')
            if button_factory.get_attribute('class')!='grayed':
                button_factory.click()
                print("Bought factory")
            button_grandma=bot.find_element(By.XPATH,'//*[@id="buyGrandma"]')
            if button_grandma.get_attribute('class')!='grayed':
                button_grandma.click()
                print("grandma bought")
                continue
            button_cursor=bot.find_element(By.ID,value='buyCursor')
            if button_cursor.get_attribute('class')!='grayed':
                button_cursor.click()
                print("Bought Cursor")
                continue
        except:
            print("Error while purchasing")
    





  

thread1=threading.Thread(target=cokkie_clicker)
thread2=threading.Thread(target=purchase)

thread1.start()
thread2.start()
thread1.join()
thread2.join()
