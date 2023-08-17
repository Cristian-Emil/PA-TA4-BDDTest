Feature: tests for login page
    Scenario: negative scenario
        Given I am on the login page
        When I click the cookie button
        When I insert the email "cristian-test@putlook.com"
        When I insert the password "Cristian21-test"
        When I click the loggin button
        Then I see no account error displayed
