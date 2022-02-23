def main() -> None:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    # ENTER YOUR CODE BELOW
    if num1 > num2:
        largest = num1
    if num2 > num1:
        largest = num2
    # THE FOLLOWING LINES WILL DISPLAY THE RESULT
    print("\nThe largest number is:", largest)  # local unbound error if num1 and num2 are equal


if __name__ == "__main__":
    main()
