import pytest

from ..winner_logic import is_valid_choice, get_choice_name


@pytest.mark.parametrize(
    "choice",
    [1, 2, 3],
)
def test_is_valid_choice_accepts_valid_choices(choice):
    assert is_valid_choice(choice) is True


@pytest.mark.parametrize(
    "choice",
    [0, 4, -1, 10, "1", "", None, True, False],
)
def test_is_valid_choice_rejects_invalid_choices(choice):
    assert is_valid_choice(choice) is False


@pytest.mark.parametrize(
    ("choice", "expected"),
    [
        (1, "rock"),
        (2, "paper"),
        (3, "scissors"),
    ],
)
def test_get_choice_name_returns_correct_name(choice, expected):
    assert get_choice_name(choice) == expected


@pytest.mark.parametrize(
    "choice",
    [0, 4, -1, "1", None, True],
)
def test_get_choice_name_rejects_invalid_choices(choice):
    with pytest.raises(ValueError):
        get_choice_name(choice)
