from .services import create_account
from .validator import validate_password, validate_name, validate_balance

import questionary

def main():
    print("Welcome to Bank Account")
    first_request = questionary.select(
        "How can we help you?",
        choices=[
            questionary.Choice("Create Account", value=1),
            questionary.Choice("Exit", value=0),
        ]
    ).ask()

    match first_request:
        case 1:
            account = create_account()
        case 0:
            return "So long"

    account_transactions = {
        1 : account.get_balance,
        2 : account.deposit,
        3 : account.withdraw,
        4 : account.change_password,
        5 : account.account_detail,
    }

    while True:
        function = questionary.select(
            "What do you want to do?",
            choices=[
                questionary.Choice("get Balance", value=1),
                questionary.Choice("Deposit to your account", value=2),
                questionary.Choice("Withdraw from your account", value=3),
                questionary.Choice("Change your password", value=4),
                questionary.Choice("Show account detail", value=5),
                questionary.Choice("Exit", value=0),
            ]
        ).ask()

        match function:
            case 0:
                return "have a nice day"

            case 2 | 3:
                password = questionary.password(
                    "please enter your account password",
                    validate=validate_password,
                ).ask()

                amount = int(questionary.text(
                    "please enter your amount",
                    validate=validate_balance
                ).ask())
                message = account_transactions[function](password, amount)

            case 1 | 4 | 5:
                password = questionary.password("please enter your account password").ask()
                message = account_transactions[function](password)

            case _:
                message = "please select an option"

        print(message)

if __name__ == "__main__":
    print(main())