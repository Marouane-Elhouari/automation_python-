from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_config import URL, USERNAME, PASSWORD
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
driver_path = os.path.join(base_dir, 'drivers', 'msedgedriver.exe')

service = Service(driver_path)
driver = webdriver.Edge(service=service)

try:
    driver.get(URL)
    driver.maximize_window()

    wait = WebDriverWait(driver, 20)
    username_field = wait.until(EC.presence_of_element_located((By.ID, 'username')))
    password_field = driver.find_element(By.ID, 'password')

    username_field.send_keys(USERNAME)
    password_field.send_keys(PASSWORD)

    driver.find_element(By.XPATH, "//button[@id='submit']").click()
finally:
    driver.quit()