from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
import os

# Set up Edge options and WebDriver
edge_driver_path = 'path/to/msedgedriver'  # Update with the path to your msedgedriver executable
options = Options()
options.add_experimental_option("detach", True)
service = EdgeService(executable_path=edge_driver_path)

# LinkedIn credentials
gmail = ".17@gmail.com"
password = "@1234"
login_url = "https://www.linkedin.com/login"
dashboard_url = 'https://www.linkedin.com/feed/'

# Initialize WebDriver
bot = webdriver.Edge( options=options)
bot.get(login_url)

try:
    # Perform login
    WebDriverWait(bot, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="username"]')))
    login_gmail = bot.find_element(By.XPATH, '//*[@id="username"]')
    login_gmail.send_keys(gmail)
    
    login_pass = bot.find_element(By.XPATH, '//*[@id="password"]')
    login_pass.send_keys(password)
    
    signin = bot.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
    signin.send_keys(Keys.ENTER)
    
    bot.maximize_window()

    # Wait for successful login
    wait = WebDriverWait(bot, 60)
    wait.until(EC.url_contains('/feed'))
    print("Successfully logged in.")

except TimeoutException:
    print("Login failed or took too long. Check credentials or network connection.")
    bot.quit()

# Navigate to job search 
bot.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&=false&position=1&pageNum=0")

# Example of extracting job titles and companies
try:
    WebDriverWait(bot, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'job-card-list__content')]")))
    job_titles = bot.find_elements(By.XPATH, "//div[contains(@class, 'job-card-list__content')]//a[contains(@class, 'job-card-list__title--link')]")
    company_names = bot.find_elements(By.XPATH, "//div[contains(@class, 'job-card-list__content')]//div[contains(@class, 'job-card-list__company')]")
    
    for job_title in job_titles:
        print("Job Title:", job_title.text)
    
    for company_name in company_names:
        print("Company Name:", company_name.text)

except TimeoutException:
    print("Failed to load job listings or took too long.")

# Close the browser
bot.quit()
