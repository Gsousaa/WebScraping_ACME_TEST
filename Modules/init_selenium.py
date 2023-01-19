from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Modules import logger as log

def inicializa_selenium(log):
    try:
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(ChromeDriverManager().install())

        return driver 

    except Exception as e:
        log.logger_add(e,True)