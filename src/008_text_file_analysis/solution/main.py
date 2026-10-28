from .counter import character_counter, line_counter, words_counter


def main():
    path = input("please input the path of text file: ")
    while True:
        try:
            words_list, words_count = words_counter(path)
            line_count = line_counter(path)
            character_count = character_counter(path)
            longest_word = max(words_list, key=len, default="")
            break
        except FileNotFoundError:
            print("file not exist")
            path = input("Please input the path again: ")

    return (
        f"the longest word: {longest_word}\n"
        f"words count: {words_count}\n"
        f"non empty lines count: {line_count}\n"
        f"used characters count: {character_count}"
    )


if __name__ == "__main__":
    print(main())
