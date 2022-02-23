def main() -> None:
    print("Enter a number:")
    number = int(input(""))

    if number > 0:
        print("Positive.")

    if number < 0:
        print("Negative")

    if number == 0:
        print("Zero.")


if __name__ == "__main__":
    main()
