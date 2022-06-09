from selenium import webdriver
from behave.runner import Context
from POM.project_login import Project_login

def before_all(context: Context):

    context.driver = webdriver.Firefox("utils/Driver/")

    context.Project_login = Project_login(context.driver)

    context.driver.implicitly_wait(1)

def after_all(context: Context):
    context.driver.quit()