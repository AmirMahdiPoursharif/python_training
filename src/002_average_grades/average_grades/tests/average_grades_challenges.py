
import pytest

from .main import main


def test_no_grades_returns_none_and_prints_message(monkeypatch, capsys):
    inputs = iter(["done"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = main()
    captured = capsys.readouterr()

    assert result is None
    assert "No grades were entered" in captured.out


def test_d_command_with_no_grades_returns_none(monkeypatch, capsys):
    inputs = iter(["d"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = main()
    captured = capsys.readouterr()

    assert result is None
    assert "No grades were entered" in captured.out


def test_invalid_grade_prints_message_and_continues(
    monkeypatch,
    capsys,
):
    inputs = iter(["hello", "10", "20", "done"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = main()
    captured = capsys.readouterr()

    assert result == 15.0
    assert "Please enter a valid numeric grade" in captured.out


def test_invalid_grade_does_not_affect_average(monkeypatch, capsys):
    inputs = iter(["abc", "12", "18", "done"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = main()

    assert result == 15.0
