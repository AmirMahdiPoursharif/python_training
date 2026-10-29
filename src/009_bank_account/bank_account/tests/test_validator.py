import pytest

from ..validator import validate_balance, validate_name, validate_password


@pytest.mark.parametrize("balance", ["1", "100", "0.5", "1000.00", "0.01", " 250 "])
def test_validate_balance_accepts_positive_numbers(balance):
    assert validate_balance(balance) is True


@pytest.mark.parametrize("balance", ["0", "0.0", "-1", "-0.5", " 0 "])
def test_validate_balance_rejects_zero_and_negative(balance):
    assert validate_balance(balance) is False


@pytest.mark.parametrize("balance", ["", " ", "abc", "12abc", "1,000", "1 000"])
def test_validate_balance_rejects_non_numeric(balance):
    assert validate_balance(balance) is False


@pytest.mark.parametrize("name", ["Sara", "Johnny", "Ali Reza", "  Sara  "])
def test_validate_name_accepts_names_longer_than_three_characters(name):
    assert validate_name(name) is True


@pytest.mark.parametrize("name", ["", "Ali", "abc", "a", "   abc   ", "    "])
def test_validate_name_rejects_short_names(name):
    assert validate_name(name) is False


@pytest.mark.parametrize("password", ["1234567", "secret!", "  abcdefg  "])
def test_validate_password_accepts_passwords_longer_than_six_characters(password):
    assert validate_password(password) is True


@pytest.mark.parametrize("password", ["", "123456", "abcdef", "   abcdef   "])
def test_validate_password_rejects_short_passwords(password):
    assert validate_password(password) is False
