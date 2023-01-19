from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def extract(driver,log):
    try:
        driver.get("https://acme-test.uipath.com/vendors/inventory")
        select = Select(driver.find_element(By.ID,"vendorTaxId"))
        select.select_by_visible_text('DE325476')
        driver.find_element(By.ID,"buttonOrder").click()
        
        return driver

    except Exception as e:
        log.logger_add(e,True)