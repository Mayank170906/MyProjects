from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys,time

settings=webdriver.EdgeOptions()
settings.add_experimental_option("detach",True)

bot=webdriver.Edge(options=settings)
wait=WebDriverWait(bot,60)
bot.maximize_window()

bot.get("https://www.instagram.com/accounts/login/")
username=".17@gmail.com"
password="@1"

try:
    username_xpath="//input[@name='username']"
    user=wait.until(EC.visibility_of_element_located((By.XPATH,username_xpath)))
    user.send_keys(username)
except:
    print("unable to enter username")
    bot.close()
    sys.exit()

try:
    password_xpath="//input[@name='password']"
    pas=wait.until(EC.visibility_of_element_located((By.XPATH,password_xpath)))
    pas.send_keys(password)
except:
    print("unable to enter password")
    bot.close()
    sys.exit()

try:
    login_xpath="//button[div[text()='Log in']]"
    login=wait.until(EC.visibility_of_element_located((By.XPATH,login_xpath)))
    login.click()
except:
    print("unable to login")
    bot.close()
    sys.exit()

try:
    notification_xpath="//button[text()='Not Now']"
    notification=wait.until(EC.visibility_of_element_located((By.XPATH,notification_xpath)))
    notification.click()
except:
    pass

time.sleep(2)


try:
    user_link="https://www.instagram.com/?/"
    bot.get(user_link)
    following_button_css = "a[href='//following/']"
    foloowing=wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,following_button_css)))
    no_followers_xpath="/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[3]/div/a/span/span"
    no_folowers=int(wait.until(EC.visibility_of_element_located((By.XPATH, no_followers_xpath))).text)

    foloowing.click()
except:
    print("unable to get following")
    bot.close()
    sys.exit()
time.sleep(2)
try:
    follow_buttons_xpath = "//button[div/div[text()='Follow']]"
    follow_buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH, follow_buttons_xpath)))
    for button in follow_buttons[1:no_folowers]:
        try:
            button.click()
            time.sleep(2)
        except:
            print("unable to folow this user")
except:
    print("unanle to follow")
print(no_folowers)
try:
    user_name_xpath = "//span[@class='_ap3a _aaco _aacw _aacx _aad7 _aade']"
    user_name = wait.until(EC.presence_of_all_elements_located((By.XPATH, user_name_xpath)))
    for name in user_name[0:no_folowers]:
        try:
            print(name.text)
        except:
            print("unable to print namer of this user")
except:
    print("unanle to print name")

with open("following.txt","a") as file:
    for name in user_name[0:no_folowers]:
        file.write(f"hi:{name.text}\n")
