#Classe bank account com balanco e nome do proprietario com dois metodos: depositar/retirar
class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account Owner: {self.owner}\nAccount Balance: ${self.balance}'

    def deposit(self, deposit_amt):
        self.balance += deposit_amt
        print('Deposit Accepted!')

    def withdraw(self, withdraw_amt):
        if self.balance >= withdraw_amt:
            self.balance -= withdraw_amt
            print('Withdrawal Accepted!')
        else:
            print('Not enough credit!')

account = BankAccount('Renan', 5000)
print(account)
print(account.deposit(500))
print(account.withdraw(5502))





