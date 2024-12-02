from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import sys

def speed_test():
    settings=webdriver.EdgeOptions()
    settings.add_experimental_option("detach",True)

    bot=webdriver.Edge(options=settings)
    bot.maximize_window()

    bot.get('https://www.speedtest.net/')
    
    wait=WebDriverWait(bot,120)

    try:
        button_xpath="//span[text()='Go']"
        button=wait.until(expected_conditions.visibility_of_element_located((By.XPATH,button_xpath)))
        button.click()
    except:
        print("Button not found")
        bot.close()
        sys.exit()


    try:
        wait.until(expected_conditions.url_contains("/result/"))
    except:
        print("Website taking longer time to provide data")
        bot.close()
        sys.exit()
    
    download_xpath="//span[@data-download-status-value='0.01']"
    upload_xpath="//span[@data-upload-status-value='0.01']"
    try:
        download=wait.until(expected_conditions.visibility_of_element_located((By.XPATH,download_xpath)))
        upload=wait.until(expected_conditions.visibility_of_element_located((By.XPATH,upload_xpath)))
    except:
        print("data missing")
        bot.close()
        sys.exit()
    bot.close()
    return (download.text,upload.text)
    


