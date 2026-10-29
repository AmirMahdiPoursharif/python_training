import random

from .cryptographer import encrypt, decrypt


class BankAccount:
    def __init__(self, balance: float | int, name: str, password: str):
        self.balance = balance
        self.name = name
        self.password_key = random.randint(1, 9)
        self.password = encrypt(password, self.password_key)

    def get_balance(self, password):
        if self._check_password(password):
            return f"your balance is: {self.balance}"
        else:
            return f"password is not correct try again"

    def withdraw(self, password: str, amount: float | int):
        if self._check_password(password):
            if amount > self.balance:
                return f"your balance is not enough to withdraw"
            else:
                self.balance -= amount
                return f"your balance is: {self.balance}"
        else:
            return "password is not correct try again"

    def deposit(self, password: str, amount: float | int):
        if self._check_password(password):
            self.balance += amount
            return f"Done\nyour balance is: {self.balance}"
        else:
            return "password is not correct try again"

    def change_password(self, password: str):
        if self._check_password(password):
            entry_password = input("please enter your new password: ")
            self.password_key = random.randint(1, 9)
            self.password = encrypt(entry_password, self.password_key)
            return f"Your password has been changed"
        else:
            return "password is not correct try again"

    def account_detail(self, password: str):
        if self._check_password(password):
            return (f"Account owner: {self.name}\n"
                    f"Account Balance: {self.balance}")
        else:
            return "password is not correct try again"

    def _check_password(self, password: str) -> bool:
        return password == decrypt(self.password, self.password_key)
