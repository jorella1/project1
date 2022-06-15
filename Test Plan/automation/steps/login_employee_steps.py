from behave import when, then, given
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

@given(u'I am on the project homepage')
def step_enter_homepage(context):
    context.driver.get("http://127.0.0.1:5000/")

@when(u'I click the login button')
def step_click_login_button(context):
    context.Project_landing.index_login_button().click()

@when(u'I enter {username} and {password}')
def step_enter_login_info(context, username, password):
    context.Project_login.username_bar().send_keys(username)
    context.Project_login.password_bar().send_keys(password)

@when(u'I click the submit button I should be redirected to the profile screen with {title}')
def step_redirect_to_profile(context,title):
    context.Project_login.login_button().click()
    assert context.driver.find_element(By.ID, "welcome_title").text == title

@then(u'I can click the logout button and am taken back to the login screen')
def step_impl(context):
    context.Project_login.logout_button().click()

@when(u'I enter an {incorrect_username}, which is not valid')
def step_incorrect_user(context,incorrect_username):
    context.Project_login.username_bar().send_keys(incorrect_username)

@when(u'I enter {incorrect_password}, which is not valid')
def step_incorrect_password(context,incorrect_password):
    context.Project_login.password_bar().send_keys(incorrect_password)

@then(u'I click the submit button where I should be given a message that my login details were incorrect and to loggin in again')
def step_submit_login_info(context):
    context.Project_login.login_button().click()
    assert context.driver.title == "Login"







    