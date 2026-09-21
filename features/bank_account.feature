Feature: Bank Account Operations
  As a bank customer
  I want to perform various banking operations
  So that I can manage my account balance accurately

  Scenario: Create a new account with zero balance
    When create a new account for "Julie" with 0 dollars
    Then the account balance for "Julie" should be 0 dollars

  Scenario: Deposit money into an account
    Given an account for "Julie" with 100 dollars
    When I deposit 50 dollars into "Julie"'s account
    Then the account balance for "Julie" should be 150 dollars

  Scenario: Withdraw money from an account
    Given an account for "Julie" with 200 dollars
    When I withdraw 50 dollars from "Julie"'s account
    Then the account balance for "Julie" should be 150 dollars

  Scenario: Apply 5% interest when balance is at least 1000
    Given an account for "Julie" with 1000 dollars
    When interest is applied to "Julie"'s account
    Then the account balance for "Julie" should be 1050 dollars

  Scenario: Do not apply interest when balance is under 1000
    Given an account for "Julie" with 500 dollars
    When interest is applied to "Julie"'s account
    Then the account balance for "Julie" should be 500 dollars

  Scenario: Transfer money between two accounts
    Given an account for "Julie" with 200 dollars
    And an account for "Bobby" with 50 dollars
    When I transfer 100 dollars from "Julie" to "Bobby"
    Then the account balance for "Julie" should be 100 dollars
    And the account balance for "Bobby" should be 150 dollars