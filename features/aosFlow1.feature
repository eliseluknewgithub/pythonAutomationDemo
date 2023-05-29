Feature: AOS Flow 1 scroll then login to main page

  Scenario: Launch Test
    Given I click HK button


  Scenario: Scroll to start page
    Given I am on the scrollable page
    Then I scroll the view from right to left
    Then I click Start button


  Scenario: Login Test
    Given Open Side Menu
    When I click the Avatar to open Login page
    And I submit the following credentials to login
      |Username |Password|
      | John    | testerJohn |
      | Mary    | maryann |
      | 98475521| E123456 |




