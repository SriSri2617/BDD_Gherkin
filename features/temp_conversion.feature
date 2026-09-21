Feature: Temperature conversion
    
  Scenario Outline: Convert Fahrenheit into Celsius
    Given the temperature is <fahrenheit> degrees Fahrenheit
    When convert it to Celsius
    Then the result should be <celsius> degrees Celsius
    
    Examples:
    
      | fahrenheit |  celsius |
      |    32      |    0     |
      |   212      |    100   |
      |   -40      |    -40   |
    
    
  Scenario Outline: Convert Celsius to Fahrenheit
    Given the temperature is <celsius> degrees Celsius
    When convert it to Fahrenheit
    Then the result should be <fahrenheit> degrees Fahrenheit
    
    Examples: 
    
      | celsius | fahrenheit  |
      |   0     |     32      |
      |   100   |     212     |
      |   -40   |     -40     |