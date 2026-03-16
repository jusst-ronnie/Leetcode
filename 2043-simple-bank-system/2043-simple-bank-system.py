from typing import List

class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.n = len(balance)

    def valid(self, account):
        return 1 <= account <= self.n

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.valid(account1) or not self.valid(account2):
            return False
        
        if self.balance[account1-1] < money:
            return False
        
        self.balance[account1-1] -= money
        self.balance[account2-1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self.valid(account):
            return False
        
        self.balance[account-1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.valid(account):
            return False
        
        if self.balance[account-1] < money:
            return False
        
        self.balance[account-1] -= money
        return True