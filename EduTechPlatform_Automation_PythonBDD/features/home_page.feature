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