import pytest

from ..main import main


@pytest.mark.parametrize(
    ("temperature", "unit", "expected"),
    [
        ("25", "1", 77),
        ("77", "2", 25),
        ("-40", "1", -40),
        ("0", "2", -17.77777777777778),
    ],
)
def test_main(monkeypatch, temperature, unit, expected):
    inputs = iter([temperature, unit])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs),
    )

    result = main()

    assert result == pytest.approx(expected)