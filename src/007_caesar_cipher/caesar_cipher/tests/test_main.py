import pytest

from ..main import main


def run_main(monkeypatch, inputs):
    answers = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    return main()


def test_main_encrypts_text(monkeypatch):
    result = run_main(monkeypatch, ["1", "hello", "3"])

    assert result == "you encoded text is: \nkhoor"


def test_main_decrypts_text(monkeypatch):
    result = run_main(monkeypatch, ["2", "khoor", "3"])

    assert result == "you decoded text is: \nhello"


def test_main_returns_string(monkeypatch):
    result = run_main(monkeypatch, ["1", "abc", "1"])

    assert isinstance(result, str)


def test_main_returns_message_for_invalid_option(monkeypatch):
    result = run_main(monkeypatch, ["3"])

    assert result == "Please enter a valid option"


@pytest.mark.parametrize("option", ["0", "", "encrypt", "12"])
def test_main_rejects_unknown_options(monkeypatch, option):
    result = run_main(monkeypatch, [option])

    assert result == "Please enter a valid option"


def test_main_displays_intro_message(monkeypatch, capsys):
    run_main(monkeypatch, ["3"])

    captured = capsys.readouterr()

    assert "welcome to Caesar Cipher" in captured.out
    assert "enter 1" in captured.out
    assert "enter 2" in captured.out


def test_main_encrypt_then_decrypt_round_trip(monkeypatch):
    encrypted = run_main(monkeypatch, ["1", "Secret Message 42", "7"])
    encrypted_text = encrypted.split("\n", 1)[1]

    decrypted = run_main(monkeypatch, ["2", encrypted_text, "7"])

    assert decrypted == "you decoded text is: \nSecret Message 42"
