# Write a program ton deposit or withdraw money in a bank account

class Account:
    def __init__(self):
        self.balance = 0
        print('New Account Created.')
        
    def deposit(self):
        amount = float(input('Enter amount to deposit : '))
        self.balance += amount
        print('New Balance : %f' %self.balance)
        
    def withdraw(self):
        amount = float(input('Enter the amount to withdraw : '))
        if amount > self.balance:
            print('Insufficient balance')
        else:
            self.balance -=amount
            print('New Balance : %f' %self.balance)
            
    def enquiry(self):
        print('Balance : %f' %self.balance)
        
account = Account()
account.deposit()
account.withdraw()
account.enquiry()
            