import pytest

from ..counter import character_counter, line_counter, words_counter


@pytest.fixture
def sample_file(tmp_path):
    path = tmp_path / "sample.txt"
    path.write_text("one two three\nfour five\n", encoding="utf-8")
    return str(path)


def test_words_counter_returns_words_and_count(sample_file):
    words, count = words_counter(sample_file)

    assert words == ["one", "two", "three", "four", "five"]
    assert count == 5


def test_words_counter_empty_file(tmp_path):
    path = tmp_path / "empty.txt"
    path.write_text("", encoding="utf-8")

    words, count = words_counter(str(path))

    assert words == []
    assert count == 0


def test_words_counter_ignores_extra_whitespace(tmp_path):
    path = tmp_path / "spaces.txt"
    path.write_text("  one   two\tthree  \n\n four \n", encoding="utf-8")

    words, count = words_counter(str(path))

    assert words == ["one", "two", "three", "four"]
    assert count == 4


def test_line_counter_counts_only_non_empty_lines(tmp_path):
    path = tmp_path / "lines.txt"
    path.write_text("first\n\n   \nsecond\n", encoding="utf-8")

    assert line_counter(str(path)) == 2


def test_line_counter_empty_file(tmp_path):
    path = tmp_path / "empty.txt"
    path.write_text("", encoding="utf-8")

    assert line_counter(str(path)) == 0


def test_character_counter_counts_all_characters(sample_file):
    assert character_counter(sample_file) == 24


def test_character_counter_includes_newline_characters(tmp_path):
    path = tmp_path / "chars.txt"
    path.write_text("abc\ndef\n", encoding="utf-8")

    assert character_counter(str(path)) == 8
