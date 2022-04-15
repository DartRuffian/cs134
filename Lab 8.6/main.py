def find_product(lst: list, product: str) -> int:
    try:
        item_index = lst.index(product)
        # Returns the first index that the given value is at. If the value is not present, a ValueError is raised
    except ValueError:
        item_index = -1

    return item_index


def display_product_info(lst_one: list, lst_two: list, index: int) -> None:
    print(f"""Item Name : {lst_one[index]}
Item Price: {lst_two[index]}""")


def main() -> None:
    products = ["eggs", "milk", "sausage", "bread", "apple"]
    prices = [2.99, 4.99, 5.99, 3.49, 1.22]
    choice = input("Enter a product: ").lower()

    price_index = find_product(products, choice)

    if price_index == -1:
        # -1 represents that the given value does not exist within the list
        print("Product not found")
    else:
        display_product_info(products, prices, price_index)


if __name__ == "__main__":
    main()
