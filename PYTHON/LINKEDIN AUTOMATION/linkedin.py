from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

settings=webdriver.EdgeOptions()
settings.add_experimental_option("detach",True)

gmail="mayankeducation.17@gmail.com"
password="AKMA@1234"
link="https://www.linkedin.com/login"
dashboard_url='https://www.linkedin.com/feed/'

bot=webdriver.Edge(options=settings)
bot.get(link)

login_gmail=bot.find_element(By.XPATH,value='//*[@id="username"]')
login_gmail.send_keys(gmail)
login_pass=bot.find_element(By.XPATH,value='//*[@id="password"]')
login_pass.send_keys(password)
signin=bot.find_element(By.XPATH,value='//*[@id="organic-div"]/form/div[3]/button')
signin.send_keys(Keys.ENTER)
bot.maximize_window()

wait=WebDriverWait(bot,60)
try:
    wait.until(EC.url_to_be(dashboard_url))
    print("Succesfully Login")
except:
    bot.quit()
    print("Unsuccesfull signin")

# while True:
#     time.sleep(1)
#     if bot.current_url == dashboard_url:
#         print("Login successful")
#         break
#     else:
#         print("Login failed or incorrect redirection")

bot.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
apply_wait = WebDriverWait(bot, 60)
apply_selector="//button[contains(@class, 'jobs-apply-button') and .//span[text()='Easy Apply']]"

try:
    apply_element = apply_wait.until(EC.presence_of_element_located((By.XPATH, apply_selector)))
    clickable = apply_wait.until(EC.element_to_be_clickable((By.XPATH, apply_selector)))
    print("Appllying for job\nFilling the data.")
    clickable.click()
except:
    print("Error while finding job")
    bot.close()

phone_xpath='//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3989642624-4565986378-phoneNumber-nationalNumber"]'

phone_wait=WebDriverWait(bot,60)

try:
    phone_no=phone_wait.until(EC.element_to_be_clickable((By.XPATH, phone_xpath)))
    print("Appllying for job\nFilling the Number.")
    phone_no.send_keys("9876543210")
except:
    print("Error while finding job")
    bot.close()

next_button_wait=WebDriverWait(bot,60)
button_xpath="//button[@aria-label='Continue to next step']"
try:
    next_button_click=next_button_wait.until(EC.element_to_be_clickable((By.XPATH,button_xpath)))
    print("Sending the data")
    next_button_click.click()
except:
    print("Failed to send the data.")

next2_wait=WebDriverWait(bot,60)
next2_xpath="//button[@aria-label='Continue to next step']"

try:
    next2_click=next2_wait.until(EC.element_to_be_clickable((By.XPATH,next2_xpath)))
    next2_click.click()
    print("next")
except:
    print("fail at next2")

input_wait = WebDriverWait(bot, 60)
input_field_xpath = "//input[@id='single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3989642624-4565986362-numeric']"

try:
    input_field = input_wait.until(EC.element_to_be_clickable((By.XPATH, input_field_xpath)))    
    input_field.send_keys("5")
    print("Input is done")
except :
    print("Failed to interact with the input field")


label_wait = WebDriverWait(bot, 60)
label_xpath = "//label[@data-test-text-selectable-option__label='Yes']"

try:
    label = label_wait.until(EC.element_to_be_clickable((By.XPATH, label_xpath)))
    label.click()
    print("Label is clicked and option is selected")
except Exception as e:
    print(f"Failed to interact with the label: {e}")


review_wait=WebDriverWait(bot,60)
review_button_xpath = "//button[@aria-label='Review your application']"
try:
    review_click=review_wait.until(EC.element_to_be_clickable((By.XPATH,review_button_xpath)))
    review_click.click()
    print("review is done")
except:
    print("Fail to review")

submit_wait = WebDriverWait(bot, 60)
submit_button_xpath = "//button[@aria-label='Submit application']"

try:
    # Wait until the submit button is clickable
    submit_button = submit_wait.until(EC.element_to_be_clickable((By.XPATH, submit_button_xpath)))
    
    # Click the submit button to submit the application
    submit_button.click()
    print("Application submitted successfully")
except Exception as e:
    print(f"Failed to submit application: {e}")