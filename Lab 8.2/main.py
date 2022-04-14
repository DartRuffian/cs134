def main() -> None:
    lst = ["eggs", "milk", "sausage", "bread", "apple juice", "Snickers", "carrots", "sliced turkey", "ketchup",
           "cheese"]
    for i, val in enumerate(lst):
        print(f"{i+1}: {val}")


if __name__ == "__main__":
    main()
