import sys

class customer:
    bank = 'SBI BANK'

    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount%100!=0:
            print("Sorry, only 100's, 500's, and 2000's rupees are available for deposit.")
            sys.exit()
        self.balance += amount
        print('After depositing amount in your bank: ', self.balance)

    def withdraw(self, amount):
        if amount%100!=0:
            print("Sorry, only 100's, 500's, and 2000's rupees are available for withdrawal.")
            sys.exit()
        if amount > self.balance:
            print('Insufficient balance')
            sys.exit()
        self.balance -= amount
        print('After withdrawing amount from your bank: ', self.balance)

print('Welcome to', customer.bank)
name = input('Enter your name: ')
c = customer(name)

while True:
    print('1 - Deposit \n2 - Withdraw \n3 - Exit')
    option = int(input("Choose your option: "))

    if option == 1:
        amount = int(input('Please enter amount to deposit: '))
        c.deposit(amount)
    elif option == 2:
        amount = int(input('Please enter amount to withdraw: '))
        c.withdraw(amount)
    elif option == 3:
        print('Thank you for banking with us!')
        sys.exit()
    else:
        print('Invalid option entered. Please choose a valid option for banking.')
