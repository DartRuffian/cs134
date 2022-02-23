def main() -> None:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    # ENTER YOUR CODE BELOW
    if num1 > num2:
        largest = num1
    else:
        largest = num2
    # THE FOLLOWING LINES WILL DISPLAY THE RESULT
    print("\nThe largest number is:", largest) 


if __name__ == "__main__":
    main()
