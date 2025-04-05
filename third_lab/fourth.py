class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance
        self._transactions = []

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount
        self._transactions.append(f"Dep: {amount}")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            self._transactions.append(f"Withdrawl: {amount}")

    def get_transactions(self):
        return self._transactions
