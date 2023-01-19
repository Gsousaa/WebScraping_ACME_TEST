import os
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
    

def login(driver,log):
    try:
        load_dotenv(r"Piloto\Config\.env")
        driver.get(os.getenv("URL_LOGIN"))

        email = driver.find_element(By.XPATH, '//*[@id="email"]')
        email.send_keys(os.getenv("USER_LOGIN"))
        password = driver.find_element(By.XPATH,'//*[@id="password"]')
        password.send_keys(os.getenv("PASSWORD_LOGIN"))
        driver.find_element(By.CSS_SELECTOR,'button.btn.btn-primary').click()
        
    except Exception as e:
        log.logger_add(e,True)