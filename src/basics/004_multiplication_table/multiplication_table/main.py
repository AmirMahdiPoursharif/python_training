from table_generator import multiplication_table


def main():
    print("Welcome to the multiplication table generator")
    print("This app will generate any multiplication table for you with any size")
    table_size: int = int(input("Please enter the table size you want: "))
    return multiplication_table(table_size)


if __name__ == "__main__":
    table = main()
    for row in table:
        print(row)

