def get_grade_input(num: int) -> list:
    all_grades = []
    for _ in range(num):
        all_grades.append(float(input("Enter a grade: ")))

    return all_grades


def calc_average(lst: list) -> float:
    return sum(lst) / len(lst)


def main() -> None:
    num_grades = int(input("Enter number of grades: "))
    all_grades = get_grade_input(num_grades)
    average = round(calc_average(all_grades), 2)

    print(f"Grade average: {average}")


if __name__ == "__main__":
    main()
