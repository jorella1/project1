Feature: I can login to the service with my username and password as an employee

    Scenario Outline:
        Given I am on the project homepage
        When I enter <username> and <password>
        When I click the submit button
        Then I should be directed to the employee profile page with <title>
        Then I should be able to logout

        Examples:

        |   username    |   password    |   title                   |  
        |   jorell      |   password    |   Welcome Back, jorell    |
        |   jorell1     |   password1   |   Welcome Back, jorell1   |