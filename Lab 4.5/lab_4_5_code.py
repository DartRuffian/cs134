def main() -> None:
    operand_one = float(input("Enter a number: "))
    valid_operators = ["*", "/", "+", "-"]

    # Error Handling for operator
    # while True:
    #     operator = input("Enter an operator: ")
    #     if operator in valid_operators:
    #         break
    #     else:
    #         print(f"Only the following operators are supported:\n{', '.join(valid_operators)}")

    operator = input("Enter an operator: ")
    if operator not in valid_operators:
        print("ERROR: Not a valid operator.")
        exit()

    operand_two = float(input("Enter a number: "))
    if operator == "/" and operand_two == 0:
        # raise ZeroDivisionError("Can not divide by zero.")
        print("ERROR: Cannot divide by zero.")
        exit()

    result = {
        "*": operand_one * operand_two,
        "/": operand_one / operand_two,
        "+": operand_one + operand_two,
        "-": operand_one - operand_two
    }[operator]
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
