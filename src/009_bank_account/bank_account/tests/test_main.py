import pytest
import questionary

from .. import main as main_module
from ..account import BankAccount

PASSWORD = "secret1"


class FakePrompt:
    def __init__(self, value):
        self.value = value

    def ask(self):
        return self.value


@pytest.fixture
def account(monkeypatch):
    account = BankAccount(balance=1000, name="Sara", password=PASSWORD)
    monkeypatch.setattr(main_module, "create_account", lambda: account)
    return account


@pytest.fixture
def run_main(monkeypatch, account):
    def runner(selections, passwords=(), amounts=()):
        selections_iter = iter(selections)
        passwords_iter = iter(passwords)
        amounts_iter = iter(amounts)

        def fake_select(*args, **kwargs):
            return FakePrompt(next(selections_iter))

        def fake_password(*args, **kwargs):
            return FakePrompt(next(passwords_iter))

        def fake_text(*args, **kwargs):
            return FakePrompt(next(amounts_iter))

        monkeypatch.setattr(questionary, "select", fake_select)
        monkeypatch.setattr(questionary, "password", fake_password)
        monkeypatch.setattr(questionary, "text", fake_text)

        return main_module.main()

    return runner


def test_main_prints_welcome_message(run_main, capsys):
    run_main([0])

    assert "Welcome to Bank Account" in capsys.readouterr().out


def test_main_returns_so_long_when_exiting_from_welcome_menu(run_main):
    assert run_main([0]) == "So long"


def test_main_returns_nice_day_when_exiting(run_main):
    assert run_main([1, 0]) == "have a nice day"


def test_main_get_balance(run_main, capsys):
    run_main([1, 1, 0], passwords=[PASSWORD])

    assert "your balance is: 1000" in capsys.readouterr().out


def test_main_deposit(run_main, capsys, account):
    run_main([1, 2, 0], passwords=[PASSWORD], amounts=["250"])

    captured = capsys.readouterr()

    assert "Done" in captured.out
    assert "your balance is: 1250" in captured.out
    assert account.balance == 1250


def test_main_withdraw(run_main, capsys, account):
    run_main([1, 3, 0], passwords=[PASSWORD], amounts=["400"])

    assert "your balance is: 600" in capsys.readouterr().out
    assert account.balance == 600


def test_main_withdraw_more_than_balance(run_main, capsys, account):
    run_main([1, 3, 0], passwords=[PASSWORD], amounts=["5000"])

    assert "your balance is not enough to withdraw" in capsys.readouterr().out
    assert account.balance == 1000


def test_main_change_password(run_main, capsys, monkeypatch, account):
    monkeypatch.setattr("builtins.input", lambda _: "new-secret")

    run_main([1, 4, 0], passwords=[PASSWORD])

    assert "Your password has been changed" in capsys.readouterr().out
    assert account.get_balance("new-secret") == "your balance is: 1000"


def test_main_account_detail(run_main, capsys):
    run_main([1, 5, 0], passwords=[PASSWORD])

    captured = capsys.readouterr()

    assert "Account owner: Sara" in captured.out
    assert "Account Balance: 1000" in captured.out


def test_main_shows_password_error(run_main, capsys):
    run_main([1, 1, 0], passwords=["wrong-password"])

    assert "password is not correct try again" in capsys.readouterr().out


def test_main_rejects_unknown_option(run_main, capsys):
    run_main([1, 9, 0])

    assert "please select an option" in capsys.readouterr().out


def test_main_applies_multiple_transactions(run_main, capsys, account):
    run_main(
        [1, 2, 3, 0],
        passwords=[PASSWORD, PASSWORD],
        amounts=["250", "100"],
    )

    captured = capsys.readouterr()

    assert "your balance is: 1250" in captured.out
    assert "your balance is: 1150" in captured.out
    assert account.balance == 1150
