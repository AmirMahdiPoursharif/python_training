
from vowel_counter.main import main


def test_main_counts_vowels_correctly(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "hello world")

    assert main() == {
        "a": 0,
        "e": 1,
        "i": 0,
        "o": 2,
        "u": 0,
    }


def test_main_counts_repeated_vowels(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "aeiouaaee")

    assert main() == {
        "a": 3,
        "e": 3,
        "i": 1,
        "o": 1,
        "u": 1,
    }


def test_main_with_no_vowels(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "rhythm")

    assert main() == {
        "a": 0,
        "e": 0,
        "i": 0,
        "o": 0,
        "u": 0,
    }


def test_main_counts_only_lowercase_vowels(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "aeiou")

    assert main() == {
        "a": 1,
        "e": 1,
        "i": 1,
        "o": 1,
        "u": 1,
    }


def test_main_returns_dict(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "python")

    assert isinstance(main(), dict)


def test_main_displays_intro_message(monkeypatch, capsys):
    def mock_input(prompt):
        print(prompt, end="")
        return "hello"

    monkeypatch.setattr("builtins.input", mock_input)

    main()
    output = capsys.readouterr().out

    assert "This app will count vowel sounds" in output
    assert "Enter yor text:" in output
