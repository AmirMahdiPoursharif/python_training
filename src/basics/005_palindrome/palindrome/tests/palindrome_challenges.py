from palindrome.check_palindrome import check


def test_palindrome_with_spaces():
    _, result = check("nurses run")
    assert result is True


def test_non_palindrome_with_spaces():
    _, result = check("hello world")
    assert result is False
