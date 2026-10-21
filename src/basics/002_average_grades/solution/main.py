def main():
    print("** Average Grades **")
    print("\n")
    print("we will calculate your average grades")
    grades = []
    get_grade = True
    print("\n")
    print("Enter a 'done' or 'd' after finishing the entry of grades.")

    while get_grade:
        grade = input("Enter your grade: ")
        match grade:
            case 'done' | 'd':
                get_grade = False
            case _:
                grades.append(float(grade))

    return sum(grades) / len(grades)

if __name__ == "__main__":
    print(main())