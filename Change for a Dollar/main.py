def main() -> None:
    coin_types = {
        # Coin Type : Cents worth
        "Penny": 1,
        "Nickel": 5,
        "Dime": 10,
        "Quarter": 25,
        "Dollar": 100
    }
    coin_counts = {coin: 0 for coin in list(coin_types)}

    for coin in coin_types:
        coin_counts[coin] = int(input(f"How many {coin + 's' if coin != 'Penny' else 'Pennies'} do you have?\n"))

    coin_counts = {coin: count * coin_types[coin] for coin, count in coin_counts.items()}

    total_value = sum(list(coin_counts.values()))
    print(f"You have {total_value} cent{'s' if total_value > 0 else ''}, which is", end=" ")
    if total_value > 100:
        print("more than a dollar.")
    elif total_value == 100:
        print("equal to a dollar.")
    else:
        print("less than a dollar.")


if __name__ == "__main__":
    main()
