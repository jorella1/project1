from selenium.webdriver.chrome.webdriver import WebDriver
#from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Project_login:
    def __init__(self, driver: WebDriver):
        """This class is injected with a driver on intialization"""
        self.driver = driver

    def username_bar(self):
        return self.driver.find_element(By.ID, "user_name")

    def password_bar(self):
        return self.driver.find_element(By.ID, "user_pass")

    def login_button(self):
        return self.driver.find_element(By.ID, "submit_button")

    def logout_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".nav > li:nth-child(3) > a:nth-child(1)")