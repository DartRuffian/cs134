def print_grid(rows: int, cols: int):
    for i in range(rows):
        print("".join([f"{ii+1}  " for ii in range(cols)]))


def main() -> None:
    num_rows = int(input("Enter a number of rows:    "))
    num_cols = int(input("Enter a number of columns: "))
    print_grid(num_rows, num_cols)


if __name__ == "__main__":
    main()
