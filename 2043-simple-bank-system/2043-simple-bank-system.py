class Bank:
    def __init__(self, balance: List[int]):
        self.balance = balance
        self.n = len(balance)

    def _is_valid(self, account: int) -> bool:
        """Helper to check if an account number is within range."""
        return 1 <= account <= self.n

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # Step 1: Validate both accounts exist and account1 has enough funds
        if not self._is_valid(account1) or not self._is_valid(account2):
            return False
        if self.balance[account1 - 1] < money:
            return False
            
        # Step 2: Execute the transfer
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        # Validate account exists
        if not self._is_valid(account):
            return False
            
        # Execute deposit
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        # Validate account exists and has enough funds
        if not self._is_valid(account) or self.balance[account - 1] < money:
            return False
            
        # Execute withdrawal
        self.balance[account - 1] -= money
        return True