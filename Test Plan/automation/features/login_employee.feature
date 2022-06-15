Feature: I can login to the service with my username and password as an employee or manager

    Scenario Outline: Entering the correct login information will take you to the profile page
        Given I am on the project homepage
        When I click the login button
        When I enter <username> and <password>
        When I click the submit button I should be redirected to the profile screen with <title>
        Then I can click the logout button and am taken back to the login screen

        Examples:

        |   username    |   password    |   title                   |  
        |   jorell      |   password    |   Welcome Back, jorell    |
        |   joeor1      |   password1   |   Welcome Back, joeor1    |

    Scenario Outline: Entering your username and password incorrectly will prompt the user to try again

        Given I am on the project homepage
        When I click the login button
        When I enter <incorrect_username>, which is not valid
        When I enter <incorrect_password>, which is not valid
        Then I click the submit button where I should be given a message that my login details were incorrect and to loggin in again

        Examples:

        |   incorrect_username             |   incorrect_password         |
        |   incorrectuser1                 |   wrongpass1                 |
        |   incorrectuser2                 |   wrongpass2                 |
    



