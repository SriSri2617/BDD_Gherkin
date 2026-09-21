from behave import *
from src.bank_account import Bank


def get_account(context):
    # 1. Safely try to get 'accounts' from 'context'.
    # If 'accounts' doesn't exist yet, return None instead of crashing with an error.
    account = getattr(context, 'account', None)

    # 2. If it returned None (meaning it was never created before):
    if account is None:
        context.account = {}           # Create an empty dictionary on the context object
        account = context.account     # and point our local variable 'accounts' to it.
    return account                    # Hand back the dictionary so the caller can use it immediately.

#GIVEN STEP
@given('an account for "{name}" with {amount:d} dollars')
#@when('create a new account for "{name}" with {amount:d} dollars')
def step_given_account(context, name, amount):
    account = get_account(context)
    account[name] = Bank(name, amount)
    
 
# WHEN STEPS    
@when('create a new account for "{name}" with {amount:d} dollars')
def step_create_account(context, name, amount):
    account = get_account(context)
    account[name] = Bank(name, amount)
 
    
@when('I deposit {amount:d} dollars into "{name}"\'s account')
def step_deposit_amount(context, name, amount):
    context.account[name].deposit(amount)
    
@when('I withdraw {amount:d} dollars from "{name}"\'s account')    
def step_withdraw_amount(context, name, amount):
    context.account[name].withdraw(amount)
    
@when('interest is applied to "{name}"\'s account')    
def step_apply_interest(context, name):
    context.account[name].interest()

@when('I transfer {amount:d} dollars from "{sender}" to "{receiver}"')    
def step_transfer_amount(context, sender, receiver, amount):
    withdraw = context.account[sender].withdraw(amount)
    if withdraw > 0:
        context.account[receiver].deposit(withdraw)       

# THEN STEPS
@then('the account balance for "{name}" should be {expected_balance:d} dollars')
def step_verify_balance(context, name, expected_balance):
    account = context.account.get(name)
    assert account is not None, f"Account for '{name}' was not found."
    actual_balance = account.get_balance()
    assert actual_balance == expected_balance, \
    (f"Expected {expected_balance} for {name}, but got {actual_balance}.")