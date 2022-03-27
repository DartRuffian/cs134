def main() -> None:
    start_num = int(input("Enter a starting value: "))
    if start_num % 2 != 0:
        start_num -= 1

    for _ in range(int(start_num / 2)):
        print(start_num)
        start_num -= 2


if __name__ == "__main__":
    main()
