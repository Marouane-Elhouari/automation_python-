from config.settings import GOOGLE_URL, SEARCH_TERM
from utils.driver_setup import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def run_automation():
    driver = get_driver()
    try:
        driver.get(GOOGLE_URL)
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'q'))
        )
        search_box.send_keys(SEARCH_TERM)
        search_box.send_keys(Keys.RETURN)
        time.sleep(30)
    finally:
        driver.quit()


if __name__ == '__main__':
    run_automation()
