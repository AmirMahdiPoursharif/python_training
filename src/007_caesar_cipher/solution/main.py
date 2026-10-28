from .cryptographer import encrypt, decrypt

def main():
    print("****   welcome to Caesar Cipher   ***\n\n")
    print("for encrypting your text enter 1 and for decrypting your text enter 2")
    user_wish = input("[1/2]: ")

    if user_wish == "1":
        print("OK, we will encrypt your text")
        txt = input("Enter your text: ")
        key = int(input("Enter your key (the key must be an integer and remember it): "))
        encoded_txt = encrypt(txt, key)
        return f"you encoded text is: \n{encoded_txt}"

    elif user_wish == "2":
        print("OK, we will decrypt your text")
        txt = input("Enter your text: ")
        key = int(input("Enter your decryption key (the key is an integer): "))
        decoded_txt = decrypt(txt, key)
        return f"you decoded text is: \n{decoded_txt}"

    else:
        return "Please enter a valid option"

if __name__ == '__main__':
    print(main())