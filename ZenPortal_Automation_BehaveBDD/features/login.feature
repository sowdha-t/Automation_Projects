@login
Feature: Zen Portal Login Functionality

Background:
    Given user navigate to the Zen Portal login page

@minor
Scenario: verify login page elements
    Then verify that the username input box is visible
    And verify that the password box is visible
    And verify that submit button is visible


@smoke @regression @blocker
Scenario: successful login
    When user enter valid configured credentials
    And click on the submit button
    Then validate user logged into the dashboard page

@smoke @critical
Scenario Outline: unsuccessful login
    When user enter invalid "<username>" and "<password>"
    And click on the submit button
    Then appropriate "<error_message>" is displayed in "<error_field>"
    And  the user remains on the login page

Examples:
| username                    | password |error_message                |error_field|
| sowdha.perumal@gmail.com    | wrong123 | *Incorrect password!        |password   |
| invalid@gmail.com           | admin123 | *Invalid email!             |email      |
| test@gmail.com              |   ""     | Password required!          |password   |
|          ""                 |fdsgdgdga  | Email required!            |email      |
|          ""                 |   ""      |Email and password required!|password   |


@smoke @regression @logout @blocker
Scenario: successful logout
    Given user in the dashboard page
    When user click the profile menu and click log out
    Then user is redirected back to the login page

