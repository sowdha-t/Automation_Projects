Feature: EduTech App GUVI Home Page
  As a visitor
  I want to verify the GUVI Home page
  So that i can validate the navigation and login and sign up buttons

  Background:
    Given the user opens the Guvi Home Page

    Scenario: TestCase_01: Application URL loads
      Then the application should load without errors

    Scenario Outline: TestCase_02: Check Page Title is correct
      Then the page title should be "<title>"

      Examples:
      |title|
      |HCL GUVI \| Learn to code in your native language|

    Scenario: TestCase_03: Login button is visible and clickable
      Then the login button should be visible
      When the user clicks the login button
      Then the user navigates to login page

    Scenario Outline: TestCase_04: Sign Up button is visible and clickable
      Then the sign up button should be visible
      When the user clicks the sign up button
      Then the current url should be "<url>"

      Examples:
      | url |
      |https://www.guvi.in/register/|

    Scenario Outline: TestCase_05: Sign Up button navigates to register page
      When the user clicks the sign up button
      Then the user navigates to "<register_url>" successfully
      And the register page should load properly

      Examples:
      |register_url|
      |https://www.guvi.in/register/|