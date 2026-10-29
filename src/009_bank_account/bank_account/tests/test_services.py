import pytest
import questionary

from ..account import BankAccount
from ..services import create_account

ACCOUNT_DATA = {"name": "Sara", "balance": "1500", "password": "secret1"}


class FakePrompt:
    def __init__(self, value):
        self.value = value

    def ask(self):
        return self.value


@pytest.fixture
def form_fields(monkeypatch):
    fields = {}

    def fake_form(**kwargs):
        fields.update(kwargs)
        return FakePrompt(ACCOUNT_DATA)

    monkeypatch.setattr(questionary, "text", lambda *args, **kwargs: FakePrompt(None))
    monkeypatch.setattr(
        questionary, "password", lambda *args, **kwargs: FakePrompt(None)
    )
    monkeypatch.setattr(questionary, "form", fake_form)

    return fields


def test_create_account_returns_bank_account(form_fields):
    account = create_account()

    assert isinstance(account, BankAccount)


def test_create_account_uses_form_values(form_fields):
    account = create_account()

    assert account.name == "Sara"
    assert account.get_balance("secret1") == "your balance is: 1500.0"


def test_create_account_converts_balance_to_float(form_fields):
    account = create_account()

    assert isinstance(account.balance, float)
    assert account.balance == 1500.0


def test_create_account_asks_for_three_fields(form_fields):
    create_account()

    assert set(form_fields) == {"name", "balance", "password"}
