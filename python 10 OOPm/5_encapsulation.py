class Account:
    def __init__(self, balance):
        self.__balance = balance  

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = Account(100)
acc.deposit(50)
print(acc.get_balance())