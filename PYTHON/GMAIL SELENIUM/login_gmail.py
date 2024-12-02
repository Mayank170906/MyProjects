from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
profile_path = 'C:/Users/gadha/AppData/Local/Microsoft/Edge/User Data/Profile 4'
settings = webdriver.EdgeOptions()
settings.add_experimental_option("detach",True)
settings.add_argument(f'user-data-dir={profile_path}')
settings.add_argument('profile-directory=Profile 4')

gmail="@gmail.com"
passwqord="@"
link="https://tinder.com/"

bot = webdriver.Edge(options=settings)
bot.get(link)
bot.maximize_window()


wait = WebDriverWait(bot,10)

try:
    sign_in_XPATH = '//*[contains(text(),"Log in")]'
    sign_in_BUTTON=wait.until(EC.element_to_be_clickable((By.XPATH,sign_in_XPATH)))
    sign_in_BUTTON.click()
    print("Signing you in")

except:
    print("sign in fail")
    bot.quit()
    sys.exit()



try:
    continue_button_xpath = '//span[contains(text(), "Continue with Google")]'
    continue_button=wait.until(EC.element_to_be_clickable((By.XPATH,continue_button_xpath)))
    continue_button.click()
    print("signining you with google")
except:
    print("unable to continue with google account")
    bot.quit()
    sys.exit()

try:
    original_window=bot.current_window_handle
    wait.until(EC.number_of_windows_to_be(2))
    bot.switch_to.window(bot.window_handles[1])
    print("SWITCHED the tab to google login page")
    try:
        email_xpath = '//input[@id="identifierId"]'
        email_input=wait.until(EC.element_to_be_clickable((By.XPATH,email_xpath)))
        email_input.send_keys(gmail)
        print("Email entered")
    except:
            print("Failed to enter email")
    try:
         next_button_xpath = "//span[text()='Next']"
         next_button=wait.until(EC.element_to_be_clickable((By.XPATH,next_button_xpath)))
         next_button.click()
         print("going to next")
    except:
         print("Unabloe to click on next")


except:
     print("Failed to find login window")


