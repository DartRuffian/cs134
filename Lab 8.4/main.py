def calc_average(lst: list) -> float:
    return sum(lst) / len(lst)


def main() -> None:
    product_prices = [10.99, 13.74, 3.29, 5.69, 100.0, 89.99, 19.35, 14.25]
    avg = calc_average(product_prices)
    print(f"Average: {avg}")


if __name__ == "__main__":
    main()
