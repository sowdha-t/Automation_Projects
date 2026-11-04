Feature: Guvi Dashboard page
  As a registered user
  I want to verify the dashboard features
  So that i can validate the menu bar, Guvi dobby assistant and log out features
  Background:
    Given the user is logged in with the valid credentials from configuration

    Scenario:TestCase_08: Main menu items are displyed
      Then the following menu items should be visible
      | menu_item   |
      | Courses     |
      | LIVE Classes|
      | Practice    |

    @skip
    Scenario: TestCase_09: Dobby Guvi Assistant is present
      Then the Dobby Guvi Assistant should be displayed

    @skip
    Scenario:  TestCase_10 - Logout redirects the user out of the dashboard
      When the user clicks the Logout Option
      Then the user should be logged out
      And the user should be on the login page