def _get_letter_unicode(letter : str, first_pos: str) -> int:
    # number in range of 0 to 25
    return ord(letter) - ord(first_pos)


def caesar_cipher(password : str, key : int, decryption: bool = False) -> str:
    key = -key if decryption else key

    generated = ""

    for char in password:


        if char.isupper():
            char_unicode: int = _get_letter_unicode(char, "A")
            generated += chr(((char_unicode + key) % 26) + ord("A"))


        elif char.islower():
            char_unicode: int = _get_letter_unicode(char, "a")
            generated += chr(((char_unicode + key) % 26) + ord("a"))

        else:
            generated += char

    return generated


def encrypt(password : str, key : int) -> str:
    return caesar_cipher(password, key, False)


def decrypt(password : str, key : int) -> str:
    return caesar_cipher(password, key, True)

