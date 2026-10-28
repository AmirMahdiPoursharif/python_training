import pytest

from ..cryptographer import caesar_cipher, decrypt, encrypt


@pytest.mark.parametrize(
    ("text", "key", "expected"),
    [
        ("abc", 3, "def"),
        ("hello", 3, "khoor"),
        ("Hello, World!", 3, "Khoor, Zruog!"),
        ("xyz", 3, "abc"),
        ("XYZ", 3, "ABC"),
        ("abc", 0, "abc"),
        ("abc", 26, "abc"),
        ("abc", 29, "def"),
    ],
)
def test_encrypt(text, key, expected):
    assert encrypt(text, key) == expected


@pytest.mark.parametrize(
    ("text", "key", "expected"),
    [
        ("def", 3, "abc"),
        ("khoor", 3, "hello"),
        ("Khoor, Zruog!", 3, "Hello, World!"),
        ("abc", 3, "xyz"),
        ("def", 0, "def"),
        ("abc", 26, "abc"),
    ],
)
def test_decrypt(text, key, expected):
    assert decrypt(text, key) == expected


@pytest.mark.parametrize("key", [-5, 0, 1, 3, 13, 25, 26, 100])
def test_decrypt_reverses_encrypt(key):
    text = "The Quick Brown Fox Jumps Over 13 Lazy Dogs!"

    assert decrypt(encrypt(text, key), key) == text


def test_non_letter_characters_are_preserved():
    assert encrypt("Hello, World! 123 - _ @", 5) == "Mjqqt, Btwqi! 123 - _ @"


def test_case_is_preserved():
    assert encrypt("aBcD", 1) == "bCdE"


def test_negative_key_shifts_backwards():
    assert encrypt("abc", -1) == "zab"


def test_empty_text():
    assert encrypt("", 5) == ""
    assert decrypt("", 5) == ""


def test_caesar_cipher_decryption_flag():
    assert caesar_cipher("abc", 3, decryption=False) == "def"
    assert caesar_cipher("def", 3, decryption=True) == "abc"


def test_key_multiple_of_alphabet_returns_same_text():
    assert encrypt("Hello, World!", 26) == "Hello, World!"
