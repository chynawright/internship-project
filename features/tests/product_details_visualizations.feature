# Created by ChynaWright at 5/30/2024
Feature: Create Test Case

  Scenario: The user can open product detail and see three options for visualization
    Given Open the main page
    When Log in to the page
    And Click “off plan” on the left side of the menu
    And Click on the first product
    Then Verify the three options of visualization are “architecture”, “interior”, “lobby”
    And Verify the visualization options are clickable