Feature: Library Book Management
  As a library user, 
  I want to search, borrow, return and check books based on title and author
  
  Scenario: Search for a book by title and author
    Given the library contains the book "Atomic Habits" by "James Clear"
    When I search a book "Atomic Habits" by "James Clear"
    Then I should see the book "Atomic Habits" by "James Clear" in search results
    
  Scenario: Borrow a book
    Given the library contains the book "Atomic Habits" by "James Clear"
    When I borrow the book "Atomic Habits"
    Then The book "Atomic Habits" should be listed in my borrowed list
    
  Scenario: Return a book
    Given I have borrowed the book "Atomic Habits"
    When I return the book "Atomic Habits"
    Then The book "Atomic Habits" should be in the availalbe list
  
  Scenario: Check a particular book that is borrowed
    Given Book "Mahabaratham" should be on borrowed list
    When I search for the book "Mahabaratham"
    Then It should indicate the books is not avaialbe and borrowed.
    