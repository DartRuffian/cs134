def get_min_max_age() -> tuple:
    min_age = int(input("Enter minimum age: "))
    max_age = int(input("Enter maximum age: "))
    return min_age, max_age


def main() -> None:
    min_age, max_age = get_min_max_age()

    while True:
        curr_guess = int(input("Enter your age: "))
        if min_age < curr_guess < max_age:
            print("Valid age entered.")
            break
        else:
            print("Invalid age entered.")


if __name__ == "__main__":
    main()
