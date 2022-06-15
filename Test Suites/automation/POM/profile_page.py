#from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.select import Select


class Project_profile:
    def __init__(self, driver: WebDriver):
        """This class is injected with a driver on intialization"""
        self.driver = driver

    def requested_amount(self):
        return self.driver.find_element(By.ID, "amount")

    def request_description(self):
        return self.driver.find_element(By.ID, "description")

    def submit_request(self):
        return self.driver.find_element(By.ID, "submit_request")

    def cancel_request_id(self):
        return self.driver.find_element(By.ID, "cancel_id")
    
    def cancel_request_button(self):
        return self.driver.find_element(By.ID, "cancel_request_button")
