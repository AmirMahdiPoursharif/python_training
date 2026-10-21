import pytest

from average_grades.main import main

def test_main_calculates_average(monkeypatch, capsys):
    inputs = iter(["10", "20", "15", "done"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = main()

    assert result == 15.0

    output = capsys.readouterr().out
    assert "** Average Grades **" in output
    assert "we will calculate your average grades" in output


def test_main_accepts_d_as_exit_command(monkeypatch):
    inputs = iter(["12", "18", "d"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = main()

    assert result == 15.0


def test_main_with_one_grade(monkeypatch):
    inputs = iter(["17.5", "done"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = main()

    assert result == 17.5


def test_main_returns_float(monkeypatch):
    inputs = iter(["10", "20", "done"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = main()

    assert isinstance(result, float)


def test_main_with_no_grades_raises_error(monkeypatch):
    inputs = iter(["done"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with pytest.raises(ZeroDivisionError):
        main()


def test_main_with_invalid_grade_raises_error(monkeypatch):
    inputs = iter(["abc"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with pytest.raises(ValueError):
        main()
