def main() -> None:
    start_num_bacteria = int(input("Starting number of bacteria: "))
    num_days = int(input("Number of days: "))
    i = 1

    while i <= num_days:
        curr_bacteria = start_num_bacteria * (2 ** i)
        print(f"Bacteria Day #{i}: {curr_bacteria}")
        i += 1


if __name__ == "__main__":
    main()
