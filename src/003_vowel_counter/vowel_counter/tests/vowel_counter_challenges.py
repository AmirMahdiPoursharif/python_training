
from vowel_counter.main import main


def test_counts_uppercase_and_lowercase_vowels(monkeypatch):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "AaEeIiOoUu",
    )

    assert main() == {
        "a": 2,
        "e": 2,
        "i": 2,
        "o": 2,
        "u": 2,
    }


def test_empty_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "")

    assert main() == {
        "a": 0,
        "e": 0,
        "i": 0,
        "o": 0,
        "u": 0,
    }


def test_counts_total_vowels(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Hello World")

    result = main()

    assert sum(result.values()) == 3
