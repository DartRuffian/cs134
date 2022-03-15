def main() -> None:
    all_grades = []
    while curr_grade := float(input("Enter a grade: ")):
        if curr_grade < 0:
            print("Negative number entered, all grades recorded.")
            break

        all_grades.append(curr_grade)
    print(f"\nGrade average: {round(sum(all_grades)/len(all_grades), 2)}")


if __name__ == "__main__":
    main()
