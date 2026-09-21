Feature: Inventory Management (Stock Tracking)
  As a store manager
  Want to manage products in stock and keep track of product quantities
  
  Scenario: Add a new product to stock
    Given an empty stock
    When add product "Laptop" with quantity 10
    Then "Laptop" should be in the stock
    And the quantity of "Laptop" should be 10
    
  Scenario: Reduce the product quantity
    Given a stock "Mobiles" with quantity 10
    When I reduce the quantity of "Mobiles" by 3
    Then the quantity of "Mobiles" should be 7