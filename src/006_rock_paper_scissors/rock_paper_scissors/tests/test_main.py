import pytest

from ..main import main
from ..winner_logic import select_winner


@pytest.mark.parametrize(
    ("cpu_choice", "human_choice", "expected"),
    [
        (1, 1, None),
        (2, 2, None),
        (3, 3, None),
        (2, 1, 2),
        (1, 2, 2),
        (3, 2, 3),
        (2, 3, 3),
        (1, 3, 1),
        (3, 1, 1),
    ],
)
def test_select_winner(cpu_choice, human_choice, expected):
    assert select_winner(cpu_choice, human_choice) == expected


@pytest.mark.parametrize("choice", [1, 2, 3])
def test_select_winner_returns_none_for_equal_choices(choice):
    assert select_winner(choice, choice) is None


@pytest.mark.parametrize(
    ("cpu_choice", "human_choice", "expected_text"),
    [
        (1, 1, "Equal"),
        (2, 1, "cpu won the game"),
        (1, 2, "human won the game"),
        (3, 2, "cpu won the game"),
        (2, 3, "human won the game"),
        (1, 3, "cpu won the game"),
        (3, 1, "human won the game"),
    ],
)
def test_main_result(
    monkeypatch,
    capsys,
    cpu_choice,
    human_choice,
    expected_text,
):
    monkeypatch.setattr(
        "random.randint",
        lambda a, b: cpu_choice,
    )
    monkeypatch.setattr(
        "builtins.input",
        lambda _: str(human_choice),
    )

    result = main()

    assert expected_text in result
    assert f"cpu choice: " in result
    assert f"human choice: " in result

    captured = capsys.readouterr()
    assert "rock paper scissors" in captured.out


@pytest.mark.parametrize(
    ("cpu_choice", "human_choice", "cpu_symbol", "human_symbol"),
    [
        (1, 1, "🪨", "🪨"),
        (2, 3, "📃", "✂"),
        (3, 1, "✂", "🪨"),
    ],
)
def test_main_includes_correct_symbols(
    monkeypatch,
    cpu_choice,
    human_choice,
    cpu_symbol,
    human_symbol,
):
    monkeypatch.setattr(
        "random.randint",
        lambda a, b: cpu_choice,
    )
    monkeypatch.setattr(
        "builtins.input",
        lambda _: str(human_choice),
    )

    result = main()

    assert f"cpu choice: {cpu_symbol}" in result
    assert f"human choice: {human_symbol}" in result


def test_main_returns_string(monkeypatch):
    monkeypatch.setattr("random.randint", lambda a, b: 1)
    monkeypatch.setattr("builtins.input", lambda _: "1")

    result = main()

    assert isinstance(result, str)
