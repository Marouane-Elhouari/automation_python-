import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config import filling_config as config

base_dir = os.path.dirname(os.path.abspath(__file__))
driver_path = os.path.join(base_dir, 'drivers', 'msedgedriver.exe')
service = EdgeService(executable_path=driver_path)
driver = webdriver.Edge(service=service)

driver.get(config.URL)
driver.maximize_window()
time.sleep(2)

try:
    wait = WebDriverWait(driver, 20)
    first_name_field = wait.until(EC.presence_of_element_located((By.NAME, 'f irstname')))
    first_name_field.send_keys(config.FORM_DATA['first_name'])
    last_name_field = driver.find_element(By.NAME, 'lastname')
    last_name_field.send_keys(config.FORM_DATA['last_name'])

    if config.FORM_DATA['gender'].lower() == 'male':
        driver.find_element(By.ID, 'sex-0').click()
    else:
        driver.find_element(By.ID, 'sex-1').click()

    driver.find_element(By.ID, f"exp-{int(config.FORM_DATA['experience']) - 1}").click()

    driver.find_element(By.ID, 'profession-0').click()

    driver.find_element(By.ID, 'tool-2').click()

    driver.find_element(By.ID, 'submit').click()

    time.sleep(10)
except Exception as e:
    print(e)
finally:
    driver.quit()