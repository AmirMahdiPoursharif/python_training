def main():
    print("This app will count vowel sounds in your entered text")
    string = input("Enter yor text: ")
    string = string.lower()
    result: dict = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0, }
    for char in string:
        if char in "aeiou":
            result[char] += 1
    return result

if __name__ == "__main__":
    print(main())