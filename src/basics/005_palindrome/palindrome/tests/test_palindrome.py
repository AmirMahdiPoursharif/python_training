from palindrome.check_palindrome import check


def test_palindrome_with_even_length():
    assert check("abba") == ("abba", True)


def test_palindrome_with_odd_length():
    assert check("radar") == ("radar", True)


def test_non_palindrome():
    assert check("hello") == ("olleh", False)


def test_single_character():
    assert check("a") == ("a", True)


def test_empty_string():
    assert check("") == ("", True)


def test_palindrome_is_case_sensitive():
    assert check("Racecar") == ("racecaR", False)
