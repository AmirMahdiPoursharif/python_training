import pytest

from ..account import BankAccount
from ..cryptographer import decrypt, encrypt

PASSWORD = "secret1"
WRONG_PASSWORD_MESSAGE = "password is not correct try again"


@pytest.fixture
def account():
    return BankAccount(balance=1000, name="Sara", password=PASSWORD)


def _input_must_not_be_called(*args, **kwargs):
    pytest.fail("input() should not be called when the password is wrong")


def test_account_stores_balance_and_name(account):
    assert account.balance == 1000
    assert account.name == "Sara"


def test_account_generates_a_key_between_one_and_nine(account):
    assert 1 <= account.password_key <= 9


def test_account_stores_password_encrypted(account):
    assert account.password != PASSWORD
    assert account.password == encrypt(PASSWORD, account.password_key)
    assert decrypt(account.password, account.password_key) == PASSWORD


def test_get_balance_returns_balance_with_correct_password(account):
    assert account.get_balance(PASSWORD) == "your balance is: 1000"


def test_get_balance_works_for_float_balance():
    account = BankAccount(balance=100.5, name="Reza", password=PASSWORD)

    assert account.get_balance(PASSWORD) == "your balance is: 100.5"


def test_password_is_case_sensitive(account):
    assert account.get_balance("SECRET1") == WRONG_PASSWORD_MESSAGE


@pytest.mark.parametrize(
    ("method", "args"),
    [
        ("get_balance", ()),
        ("deposit", (100,)),
        ("withdraw", (100,)),
        ("change_password", ()),
        ("account_detail", ()),
    ],
)
def test_wrong_password_is_rejected(account, monkeypatch, method, args):
    monkeypatch.setattr("builtins.input", _input_must_not_be_called)
    balance_before = account.balance

    result = getattr(account, method)("wrong-password", *args)

    assert result == WRONG_PASSWORD_MESSAGE
    assert account.balance == balance_before


def test_withdraw_decreases_balance(account):
    message = account.withdraw(PASSWORD, 250)

    assert message == "your balance is: 750"
    assert account.balance == 750


def test_withdraw_all_balance(account):
    message = account.withdraw(PASSWORD, 1000)

    assert message == "your balance is: 0"
    assert account.balance == 0


def test_withdraw_more_than_balance_is_rejected(account):
    message = account.withdraw(PASSWORD, 1500)

    assert message == "your balance is not enough to withdraw"
    assert account.balance == 1000


def test_deposit_increases_balance(account):
    message = account.deposit(PASSWORD, 500)

    assert message == "Done\nyour balance is: 1500"
    assert account.balance == 1500


def test_deposit_accepts_float_amount(account):
    message = account.deposit(PASSWORD, 12.5)

    assert message == "Done\nyour balance is: 1012.5"
    assert account.balance == 1012.5


def test_account_detail_shows_owner_and_balance(account):
    message = account.account_detail(PASSWORD)

    assert message == "Account owner: Sara\nAccount Balance: 1000"


def test_change_password_updates_password(account, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "new-secret")

    message = account.change_password(PASSWORD)

    assert message == "Your password has been changed"
    assert account.get_balance("new-secret") == "your balance is: 1000"
    assert account.get_balance(PASSWORD) == WRONG_PASSWORD_MESSAGE


def test_change_password_re_encrypts_new_password(account, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "new-secret")

    account.change_password(PASSWORD)

    assert account.password != "new-secret"
    assert decrypt(account.password, account.password_key) == "new-secret"
