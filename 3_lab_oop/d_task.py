class BankAccount:
    """Simple bank account class"""

    def __init__(self, initial_balance=0):
        """Initializes bank account

        Args:
            initial_balance (int, optional): account balance. Defaults to 0.
        """
        self._balance = initial_balance
        self._transactions = []

    @property
    def balance(self) -> float:
        """Returns balance

        Returns:
            float: balance
        """
        return self._balance

    def deposit(self, amount: float):
        """Deposits sum to an account

        Args:
            amount (float): amount of mony to deposit
        """
        self._balance += amount
        self._transactions.append(f"Dep: {amount}")

    def withdraw(self, amount: float):
        """Implements a withdrawl operation

        Args:
            amount (float): amoun of money to withdraw
        """
        if amount <= self._balance:
            self._balance -= amount
            self._transactions.append(f"Withdrawl: {amount}")

    def get_transactions(self) -> list:
        """Returns a list of transactions

        Returns:
            list: all handled transactions
        """
        return self._transactions
