Feature: Guvi Login
  As a registered user
  I want to log in
  So that i can access my dashboard

  Background:
    Given the user is on the login page

    Scenario: TestCase_06: Login with valid credentials
      When the user enters valid credentials from configuration
      And the user clicks the submit button
      Then the user logged in and redirected to dashboard page

    Scenario Outline: TestCase_07: Login with invalid credentials
      When the user enters invalid "<email>" and "<password>"
      And the user clicks the submit button
      Then the "<error_msg>" should be displayed
      And the user remains on the login page

      Examples:
        |email                |password           |error_msg          |
        |invalid@gmail.com    |Test@123           |Invalid Email      |
        |validemail@gmail.com |invalid-password    |Invalid Password  |

