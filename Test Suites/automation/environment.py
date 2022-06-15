from behave.runner import Context
from selenium import webdriver

from POM.landing_page import Project_landing
from POM.profile_page import Project_profile
from POM.project_login import Project_login


def before_all(context: Context):

    #context.driver = webdriver.Chrome("utils/Driver/chromedriver.exe")
    context.driver = webdriver.Firefox("utils/Driver/")
    context.Project_landing = Project_landing(context.driver)
    context.Project_login = Project_login(context.driver)
    context.Project_profile = Project_profile(context.driver)

    context.driver.implicitly_wait(1)

def after_all(context: Context):
    context.driver.quit()
