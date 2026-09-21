class Bank:
    def __init__(self, name, money):
        self.__name = name
        self.__money = money

    #Name
    def get_name(self):
        return self.__name

    # Balance
    def get_balance(self):
        return self.__money

   # Deposit
    def deposit(self, amount):
        if amount > 0:
            self.__money += amount
            return amount
        else:
            return 0


    # Interset calculation
    def interest(self):
        # Check enough amt is available or not
        if self.__money < 1000:
            return 0
        else:
            # Interest calculation
            interest = self.__money * (5 / 100)
            # Add interest
            self.__money += interest
            return interest


    # Withdraw
    def withdraw(self, amount):
        #check the balance
        if amount > 0 and amount <= self.__money:
            self.__money -= amount
            return amount
        else:
            return 0
        