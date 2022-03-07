def main() -> None:
    weight_start = float(input("Starting Weight: "))

    for i in range(6):
        i += 1
        print(f"Expected weight at the end of month {i}: {weight_start - (i * 4)}")


if __name__ == "__main__":
    main()
