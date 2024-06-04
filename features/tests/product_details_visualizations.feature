# Created by ChynaWright at 5/30/2024
Feature: Create Test Case

  Scenario: The user can open product detail and see three options for visualization
    Given Open the main page
    When Enter email
    And Enter Password
    And Click login button
    And Click “off plan” on the left side of the menu
    And Click on the first product
    Then Verify the three options of visualization are “architecture”, “interior”, “lobby”
    And Verify the visualization options are clickable