def return_all_squares(num: int) -> list:  # list[int]
    # Why not just use a for loop, I get trying to teach while loops,
    # but this just isn't a very good way to teach it
    list_of_squares = []
    i = 1
    while i <= num:
        list_of_squares.append(i**2)
        i += 1
    return list_of_squares
    # Can literally be simplified to:
    # return [(i+1)**2 for i in range(num)]


def main() -> None:
    print(return_all_squares(int(input("Enter an integer: "))))


if __name__ == "__main__":
    main()
