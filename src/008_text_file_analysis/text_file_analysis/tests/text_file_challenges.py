import pytest

from ..counter import longest_word
from ..main import main


@pytest.mark.parametrize(
    ("words", "expected"),
    [
        (["hello", "beautiful", "world"], "beautiful"),
        (["cat,", "dogs"], "dogs"),
        (["planet!!", "universe"], "universe"),
        (["...wonderful!!!"], "wonderful"),
        (["python."], "python"),
        (["(quoted)"], "quoted"),
        (["dont", "isn't"], "isn't"),
        (["abcd", "wxyz"], "abcd"),
    ],
)
def test_longest_word_ignores_surrounding_punctuation(words, expected):
    assert longest_word(words) == expected


def test_longest_word_without_punctuation():
    assert longest_word(["cat", "elephant", "dog"]) == "elephant"


def test_longest_word_empty_list():
    assert longest_word([]) == ""


def test_longest_word_only_punctuation():
    assert longest_word(["...", "!!!"]) == ""


def test_main_uses_challenge_longest_word(monkeypatch, tmp_path):
    path = tmp_path / "sample.txt"
    path.write_text("cat, dogs\n", encoding="utf-8")
    monkeypatch.setattr("builtins.input", lambda _: str(path))

    result = main()

    assert result.startswith("the longest word: dogs\n")
