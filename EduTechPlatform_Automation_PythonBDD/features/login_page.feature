Feature: Guvi Login
  As a registered user
  I want to log in
  So that i can access my dashboard

  Background:
    Given the user is on the login page

    @skip
    Scenario: TestCase_06: Login with valid credentials
      When the user enters valid credentials from configuration
      And the user clicks the submit button
      Then the user logged in and redirected to dashboard page

    Scenario Outline: TestCase_07: Login with invalid credentials
      When the user enters the invalid credentials for test case "<case_id>"
      And the user clicks the submit button
      Then the expected error message should be displayed
      And the user remains on the login page

    Examples:
      | case_id        |
      | wrong_email    |
      | wrong_password |
      | invalid_email   |
      | empty_password  |

