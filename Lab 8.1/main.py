def main() -> None:
    lst = ["eggs", "milk", "sausage", "bread", "apple juice", "Snickers", "carrots", "sliced turkey", "ketchup",
           "cheese"]
    display_indexes = [3, 6, 9, 2, 4, 6]
    for i in display_indexes:
        print(f"{i}: {lst[i]}")
    """
    3: bread
    6: carrots
    9: cheese
    2: sausage
    4: apple juice
    6: carrots
    """


if __name__ == "__main__":
    main()
