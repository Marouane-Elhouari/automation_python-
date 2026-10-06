from selenium import webdriver
from selenium.webdriver.edge.options import Options


def get_driver():
    edge_options = Options()
    edge_options.add_argument('--start-maximized')
    # Selenium 4.6+ ships with Selenium Manager, which downloads the matching
    # Edge driver automatically, so webdriver-manager is no longer needed.
    return webdriver.Edge(options=edge_options)
