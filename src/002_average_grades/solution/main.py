def main():
    print("** Average Grades **")
    print("we will calculate your average grades")

    grades = []

    while True:
        grade = input("Enter a grade or 'done' to finish: ")

        if grade.lower() in ("done", "d"):
            break

        grades.append(float(grade))

    return sum(grades) / len(grades)


if __name__ == "__main__":
    print(main())
