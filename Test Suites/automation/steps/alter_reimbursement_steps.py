from behave import when, then, given
from requests import request
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

@given(u'A manager is on the profile page')
def manager_login(context):
    context.driver.get("http://127.0.0.1:5000/login")
    context.Project_login.username_bar().send_keys("joeor23")
    context.Project_login.password_bar().send_keys("password123")
    context.Project_login.login_button().click()



@then(u'They enter a valid pending request ID - {requestid} and choose to accept or deny it - {choice} and will be returned to their profile page with an updated list of reimbursement requests')
def manager_alter_request_status(context,requestid,choice):
    context.Project_profile.alter_request_id().send_keys(requestid)
    context.Project_profile.request_status().send_keys(choice)
    context.Project_profile.update_status().click()
    assert requestid, choice in context.driver.find_element(By.XPATH,"//*[@id='all_table']/tbody").text
    context.Project_profile.logout_button().click()

