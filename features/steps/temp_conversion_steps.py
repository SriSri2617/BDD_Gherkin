from behave import given, when, then, step_matcher, use_step_matcher
from behave.api.pending_step import StepNotImplementedError
from src.temp_conversion import fahernheit_to_celsius, celsius_to_fahrenheit

use_step_matcher("cfparse")

# Fahrenheit to Celsius
@given('the temperature is {temp:d} degrees Fahrenheit')
def step_given_fahrenheit(context, temp):
    context.input_temp = float(temp)
 
@when('convert it to Celsius')
def step_when_convert_celsius(context):
   context.result = fahernheit_to_celsius(context.input_temp)


@then('the result should be {expected_temp} degrees Celsius')
def step_then_verify_result(context, expected_temp):
    expected = float(expected_temp)
    assert round(context.result, 2) == round(expected, 2)
    
    
# Celsius to Fahrenheit
@given('the temperature is {temp:d} degrees Celsius')
def step_given_fahrenheit(context, temp):
    context.input_temp = float(temp)
    
@when('convert it to Fahrenheit')
def step_when_convert_celsius(context):
   context.result = celsius_to_fahrenheit(context.input_temp)

@then('the result should be {expected_temp:d} degrees Fahrenheit')
def step_then_verify_result(context, expected_temp):
    expected = float(expected_temp)
    assert round(context.result, 2) == round(expected, 2)