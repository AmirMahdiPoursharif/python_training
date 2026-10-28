import pytest

from ..main import main


def write_sample(tmp_path, text):
    path = tmp_path / "sample.txt"
    path.write_text(text, encoding="utf-8")
    return str(path)


def run_main(monkeypatch, path):
    monkeypatch.setattr("builtins.input", lambda _: path)
    return main()


def test_main_returns_summary(monkeypatch, tmp_path):
    path = write_sample(tmp_path, "Python is a language.\nIt is easy.\n")

    result = run_main(monkeypatch, path)

    assert result.startswith("the longest word: language")
    assert "\nwords count: 7\n" in result
    assert "\nnon empty lines count: 2\n" in result
    assert result.endswith("used characters count: 34")


def test_main_returns_string(monkeypatch, tmp_path):
    path = write_sample(tmp_path, "hello world\n")

    assert isinstance(run_main(monkeypatch, path), str)


def test_main_empty_file(monkeypatch, tmp_path):
    path = write_sample(tmp_path, "")

    result = run_main(monkeypatch, path)

    assert result == (
        "the longest word: \n"
        "words count: 0\n"
        "non empty lines count: 0\n"
        "used characters count: 0"
    )


def test_main_asks_again_when_file_does_not_exist(monkeypatch, capsys, tmp_path):
    missing = str(tmp_path / "missing.txt")
    existing = write_sample(tmp_path, "one two\n")

    answers = iter([missing, existing])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))

    result = main()

    captured = capsys.readouterr()

    assert "file not exist" in captured.out
    assert "\nwords count: 2\n" in result


@pytest.mark.parametrize(
    ("text", "expected_longest"),
    [
        ("a bb ccc\n", "ccc"),
        ("one\none\none\n", "one"),
        ("single\n", "single"),
    ],
)
def test_main_longest_word(monkeypatch, tmp_path, text, expected_longest):
    path = write_sample(tmp_path, text)

    result = run_main(monkeypatch, path)

    assert result.startswith(f"the longest word: {expected_longest}\n")
