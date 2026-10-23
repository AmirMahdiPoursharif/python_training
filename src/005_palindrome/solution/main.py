from check_palindrome import check

def main():
    print("Welcome to the Palindrome Checker")
    string = input("Please enter any string you want to check: ")
    sample, result = check(string)
    if result:
        return "Yes, its a Palindrome"
    else:
        return f"No, it's not a Palindrome the reversed word is *{sample}*"

if __name__ == "__main__":
    print(main())