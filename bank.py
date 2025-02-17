# Simple Bank System
# You are to create a simple banking system that:

# Allows users to create an account with their name and initial deposit.
# Provides balance inquiry to check the available balance.
# Allows deposits to increase the account balance.
# Allows withdrawals, ensuring that the withdrawal does not exceed the available balance.
# (Bonus) Supports multiple accounts and allows switching between them.
# the complete code
class BankAccount:
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance
        # Define a function to create a new account
        def create_account(self, name, initial_balance):
            self.name = name
            self.balance = initial_balance
            return self
        # Define a function to inquire the balance
        def inquire_balance(self):
            return self.balance
        # Define a function to deposit money
        def deposit(self, amount):
            self.balance += amount
            return self.balance
        # Define a function to withdraw money
        def withdraw(self, amount):
            if self.balance >= amount:
                self.balance -= amount
                return self.balance
            else:
                return "Insufficient funds"
            # Define a function to switch between accounts
            def switch_account(self, name):
                self.name = name
                return self.name
            # Create an instance of BankAccount
            account = BankAccount("John", 1000)
            # Create a new account
            new_account = account.create_account("Jane", 500)
            # Inquire the balance of the new account
            print(new_account.inquire_balance())  # Output: 500
            # Deposit money into the new account
            print(new_account.deposit(200))  # Output: 700
            # Withdraw money from the new account
            print(new_account.withdraw(300))  # Output: 400
            # Switch to the original account
            print(account.switch_account("John"))  # Output: John
            # Inquire the balance of the original account
            print(account.inquire_balance())  # Output: 400
            # Bonus: Support multiple accounts and allow switching between them
            # Define a class to manage multiple accounts
        