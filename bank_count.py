# """
# Bank class:
#
#     Attributes: name (string), branches (list of Branch objects)
#     Methods:
#     add_branch(branch): Add a new branch to the bank.
#     get_total_balance(): Return the total balance of all accounts in the bank.
#     get_customer_with_highest_balance(): Return the customer object with the highest balance in the bank.
#
# Branch class:
#     Attributes: name (string), customers (list of Customer objects)
#     Methods:
#     add_customer(customer): Add a new customer to the branch.
#     get_total_balance(): Return the total balance of all accounts in the branch.
#     get_customer_with_highest_balance(): Return the customer object with the highest balance in the branch.
#
# Customer class:
#     Attributes: name (string), accounts (list of Account objects)
#     Methods:
#     add_account(account): Add a new account to the customer.
#     get_total_balance(): Return the total balance of all accounts of the customer.
#     get_account_with_highest_balance(): Return the account object with the highest balance of the customer.
# Account class:
#     Attributes: account_number (string), balance (float)
#     Methods: None
#     Your task is to implement these classes and write a program to
#    simulate the banking system. The program should create a bank with multiple branches and customers,
#    each having multiple accounts. It should then perform the following operations:
#
# Add branches, customers, and accounts to the bank.
# Deposit and withdraw money from the accounts.
# Retrieve and display the total balance of the bank, branch, and customer.
# Retrieve and display the customer and account with the highest balance in the bank.
# """


class Account:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance.")


class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_total_balance(self):
        total_balance = 0.0
        for account in self.accounts:
            total_balance += account.balance
        return total_balance

    def get_account_with_highest_balance(self):
        highest_balance = 0.0
        account_with_highest_balance = None
        for account in self.accounts:
            if account.balance > highest_balance:
                highest_balance = account.balance
                account_with_highest_balance = account
        return account_with_highest_balance


class Branch:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def get_total_balance(self):
        total_balance = 0.0
        for customer in self.customers:
            total_balance += customer.get_total_balance()
        return total_balance

    def get_customer_with_highest_balance(self):
        highest_balance = 0.0
        customer_with_highest_balance = None
        for customer in self.customers:
            if customer.get_total_balance() > highest_balance:
                highest_balance = customer.get_total_balance()
                customer_with_highest_balance = customer
        return customer_with_highest_balance


class Bank:
    def __init__(self, name):
        self.name = name
        self.branches = []

    def add_branch(self, branch):
        self.branches.append(branch)

    def get_total_balance(self):
        total_balance = 0.0
        for branch in self.branches:
            total_balance += branch.get_total_balance()
        return total_balance

    def get_customer_with_highest_balance(self):
        highest_balance = 0.0
        customer_with_highest_balance = None
        for branch in self.branches:
            customer = branch.get_customer_with_highest_balance()
            if customer and customer.get_total_balance() > highest_balance:
                highest_balance = customer.get_total_balance()
                customer_with_highest_balance = customer
        return customer_with_highest_balance


# Simulation
bank = Bank("My Bank")

# Create branches
branch1 = Branch("Branch 1")
branch2 = Branch("Branch 2")

bank.add_branch(branch1)
bank.add_branch(branch2)

# Create customers
customer1 = Customer("John Doe")
customer2 = Customer("Jane Smith")

# Add customers to branches
branch1.add_customer(customer1)
branch2.add_customer(customer2)

# Create accounts
account1 = Account("A1", 1000)
account2 = Account("A2", 2000)
account3 = Account("A3", 5000)

# Add accounts to customers
customer1.add_account(account1)
customer1.add_account(account2)
customer2.add_account(account3)

# Deposit and withdraw money from accounts
account1.deposit(500)
account2.withdraw(1000)

# Retrieve and display total balances
print("Bank's total balance:", bank.get_total_balance())
print("Branch 1's total balance:", branch1.get_total_balance())
print("Customer 1's total balance:", customer1.get_total_balance())

#

