class BankAccount:
    """
    Represents a bank account with deposit, withdrawal, and balance display functionalities.
    """

    def __init__(self, initial_balance=0.0):
        """
        Initializes a BankAccount object with an optional starting balance.

        Args:
            initial_balance (float, optional): The initial balance of the account. Defaults to 0.0.
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposits a specified amount into the account balance.

        Args:
            amount (float): The amount to deposit.
        """
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Attempts to withdraw a specified amount from the account balance.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            bool: True if the withdrawal is successful, False otherwise (insufficient funds).
        """
        if amount > self.account_balance:
            return False
        self.account_balance -= amount
        return True

    def display_balance(self):
        """
        Prints the current balance of the account in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")  # Format to two decimal places
