from behave import given, when, then
from src.inventory_management import  StockItem, Stock
from behave.api.pending_step import StepNotImplementedError

# --- Scenario 1: Add a product ---

@given('an empty stock')
def step_empty_stock(context):
    context.stock = Stock()

@when('add product "{name}" with quantity {quantity:d}')
def step_add_product(context, name, quantity):
    product = StockItem(name, quantity)
    context.stock.add_product(product)

@then('"{name}" should be in the stock')
def step_product_exists(context, name):
    item = context.stock.get_products(name)
    assert item is not None, f"Product '{name}' was not found in stock."
    assert item.name == name



# --- Scenario 2: Reduce product quantity ---

@given('a stock "{name}" with quantity {quantity:d}')
def step_preset_stock(context, name, quantity):
    context.stock = Stock()
    product = StockItem(name, quantity)
    context.stock.add_product(product)

@when('I reduce the quantity of "{name}" by {quantity:d}')
def step_reduce_quantity(context, name, quantity):
    context.stock.reduce_quantity(name, quantity)
    
@then('the quantity of "{name}" should be {quantity:d}')
def step_verify_quantity(context, name, quantity):
    item = context.stock.get_products(name)
    assert item is not None, f"Product '{name}' was not found to check quantity."
    assert item.quantity == quantity, f"Expected quantity 10 for Mobiles, but got 7."
