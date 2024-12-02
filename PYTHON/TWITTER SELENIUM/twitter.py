from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import sys
import credentials

class twitter():
    def __init__(self) -> None:
        self.user_name=''
        self.password='@1'
        settings = webdriver.EdgeOptions()
        settings.add_experimental_option("detach",True)
        self.bot=webdriver.Edge(options=settings)
        self.bot.maximize_window()
        self.wait=WebDriverWait(self.bot,60)
        self.bot.get("https://x.com/i/flow/login")
    
    def login(self):

        try:
            username_xpath="//input[@name='text']"
            username=self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,username_xpath)))
            username.send_keys(self.user_name)
        except:
            print("failed to enter the username")
            self.bot.close()
            sys.exit()

        try:
            button1_xpath="//button[.//span[text()='Next']]"
            button1=self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,button1_xpath)))
            button1.click()
        except:
            print("failed to click next")
            self.bot.close()
            sys.exit()
      
        try:
            password_xpath="//input[@name='password']"
            password=self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,password_xpath)))
            password.send_keys(self.password)
        except:
            print("failed to enter the password")
            self.bot.close()
            sys.exit()

        try:
            loginButton_xpath="//button[.//span[text()='Log in']]"
            loginButton=self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,loginButton_xpath)))
            loginButton.click()
        except:
            print("failed to login")
            self.bot.close()
            sys.exit()
      
obj=twitter()
obj.login()
        

            


