import questionary

from .account import BankAccount
from .validator import validate_balance, validate_name, validate_password

def create_account():
    account_data = questionary.form(
        name = questionary.text(
            "whats your name? ",
            validate=validate_name,
        ),
        balance = questionary.text(
            "whats your balance? ",
            validate=validate_balance,
        ),
        password= questionary.password(
            "whats your password? ",
            validate=validate_password,
        ),
    ).ask()

    account_data["balance"] = float(account_data["balance"])
    return BankAccount(**account_data)