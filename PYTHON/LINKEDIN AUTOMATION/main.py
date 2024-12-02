from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Configuration
settings = webdriver.ChromeOptions()
settings.add_experimental_option("detach", True)

gmail = "mayankeducation.17@gmail.com"
password = "AKMA@1234"
link = "https://www.linkedin.com/login"
dashboard_url = 'https://www.linkedin.com/feed/'

# Initialize the browser
bot = webdriver.Chrome(options=settings)
bot.get(link)

# Log in
login_gmail = bot.find_element(By.XPATH, '//*[@id="username"]')
login_gmail.send_keys(gmail)
login_pass = bot.find_element(By.XPATH, '//*[@id="password"]')
login_pass.send_keys(password)
signin = bot.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
signin.send_keys(Keys.ENTER)
bot.maximize_window()

# Wait for dashboard to load
wait = WebDriverWait(bot, 60)
try:
    wait.until(EC.url_to_be(dashboard_url))
    print("Successfully Logged In")
except TimeoutException:
    bot.quit()
    print("Unsuccessful Sign-In")
    exit()

# Go to job search page
bot.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

# Wait for job links to be available
jobs_XPATH = ".//a[contains(@class, 'job-card-container__link')]"
wait.until(EC.presence_of_all_elements_located((By.XPATH, jobs_XPATH)))
print("All jobs link are available")

# Find and click "Easy Apply" button for each job
jobs = bot.find_elements(By.XPATH, jobs_XPATH)
print("All jobs found")

for link in [job.get_attribute("href") for job in jobs]:
    bot.get(link)
    print("Link visited")

    try:
        # Wait and click the "Easy Apply" button using id selector
        button_id = "ember39"
        button_apply = WebDriverWait(bot, 20).until(
            EC.presence_of_element_located((By.ID, button_id))
        )
        
        # Ensure the button is clickable
        bot.execute_script("arguments[0].scrollIntoView(true);", button_apply)
        WebDriverWait(bot, 10).until(
            EC.element_to_be_clickable((By.ID, button_id))
        )
        bot.execute_script("arguments[0].click();", button_apply)
        print("Button clicked")
    except TimeoutException:
        print("Easy Apply button not found or not clickable")
        continue

    phone_xpath='//*    [@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3989642624-456598    6378-phoneNumber-nationalNumber"]'

    # phone_wait=WebDriverWait(bot,60)

    # try:
    #     phone_no=phone_wait.until(EC.element_to_be_clickable((By.XPATH, phone_xpath)))
    #     print("Appllying for job\nFilling the Number.")
    #     phone_no.send_keys("9876543210")
    # except:
    #     print("Error while finding job")
    #     bot.close()

    next_button_wait=WebDriverWait(bot,60)
    button_xpath="//button[@aria-label='Continue to next step']"
    try:
        next_button_click=next_button_wait.until(EC.element_to_be_clickable((By.XPATH,button_xpath)))
        print("Sending the data")
        next_button_click.click()
    except:
        print("Failed to send the data.")
        continue

    next2_wait=WebDriverWait(bot,60)
    next2_xpath="//button[@aria-label='Continue to next step']"

    try:
        next2_click=next2_wait.until(EC.element_to_be_clickable((By.XPATH,next2_xpath)))
        next2_click.click()
        print("next")
    except:
        print("fail at next2")
        continue
    input_wait = WebDriverWait(bot, 60)
    input_field_xpath = "//input    [@id='single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3989642624-456598    6362-numeric']"

    try:
        input_field = input_wait.until(EC.element_to_be_clickable((By.XPATH, input_field_xpath)))    
        input_field.send_keys("5")
        print("Input is done")
    except :
        print("Failed to interact with the input field")
        continue


    label_wait = WebDriverWait(bot, 60)
    label_xpath = "//label[@data-test-text-selectable-option__label='Yes']"

    try:
        label = label_wait.until(EC.element_to_be_clickable((By.XPATH, label_xpath)))
        label.click()
        print("Label is clicked and option is selected")
    except Exception as e:
        print(f"Failed to interact with the label: {e}")
        continue

    review_wait=WebDriverWait(bot,60)
    review_button_xpath = "//button[@aria-label='Review your application']"
    try:
        review_click=review_wait.until(EC.element_to_be_clickable((By.XPATH,review_button_xpath)))
        review_click.click()
        print("review is done")
    except:
        print("Fail to review")
        continue
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
        continue

    time.sleep(5)

# Close the browser
bot.quit()
