def main() -> None:
    names = []
    while (x := input("Enter a name: ")) != "STOP":  # Just wanted to get more familiar with the walrus operator
        names.append(x)

    print("\n".join(names))


if __name__ == "__main__":
    main()
