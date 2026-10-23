import pytest

from ..main import main


def test_calculates_average_of_multiple_grades(monkeypatch):
    inputs = iter(["10", "20", "30", "done"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    assert main() == 20.0


def test_accepts_d_as_end_command(monkeypatch):
    inputs = iter(["10", "20", "d"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    assert main() == 15.0


def test_calculates_average_of_one_grade(monkeypatch):
    inputs = iter(["18", "done"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    assert main() == 18.0


def test_returns_float(monkeypatch):
    inputs = iter(["10", "20", "done"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = main()

    assert isinstance(result, float)


def test_raises_zero_division_error_when_no_grades_are_entered(
    monkeypatch,
):
    inputs = iter(["done"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with pytest.raises(ZeroDivisionError):
        main()


def test_raises_value_error_for_non_numeric_grade(monkeypatch):
    inputs = iter(["hello"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with pytest.raises(ValueError):
        main()
