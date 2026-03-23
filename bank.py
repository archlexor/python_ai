class bank_account:
    
    def __init__(self,balance = 0):
        
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return 'Invalid Deposit'
        self.__balance = self.__balance + amount
        # self.__balance += amount
        return f'Rs.{amount} Deposited and final balance after deposit is Rs.{self.__balance}'

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance = self.__balance - amount
            # self.__balance -= amount
            return f'Rs.{self.__balance} left in bank account after Rs.{amount} is withdrawn.The total amount in the bank before withdraw was Rs.{self.__balance + amount}'
        else:
            return 'Invalid Withdrawl since the required amount is not in the account'

    def get_balance(self):
        return f'The total balance in your account is Rs.{self.__balance}'

diwas = bank_account()
diwas = bank_account(1000)
print(diwas.get_balance())
print(diwas.deposit(5000))
print(diwas.get_balance())
print(diwas.withdraw(7001))
print(diwas.get_balance())



rajesh = bank_account(5000)
print(rajesh.deposit(10000))
print(rajesh.get_balance())