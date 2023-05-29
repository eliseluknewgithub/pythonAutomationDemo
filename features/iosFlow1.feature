Feature: IOS Flow 1 scroll then login to main page

  Scenario: Launch Test
    Given I click allow button
    Then I click HK button


  Scenario: Scroll to start page
    Given I am on the scrollable page in IOS
    Then I scroll the view from right to left in IOS
    Then I click Start button in IOS


  Scenario: Login Test
    Given Open Side Menu in IOS
    When I click the Avatar to open Login page in IOS
    And I submit the following credentials to login in IOS
      |Username |Password|
      | John    | testerJohn |
      | Mary    | maryann |
      | 98475521| E123456 |