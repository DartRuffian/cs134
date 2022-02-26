def is_triangle(x: float, y: float, z: float) -> bool:
    x, y, z = sorted([x, y, z])  # Sort by value, z will always be greatest value
    return x + y <= z 


def main() -> None:
    side1 = float(input("Enter the first segment: "))
    side2 = float(input("Enter the second segment: "))
    side3 = float(input("Enter the third segment: "))

    if is_triangle(side1, side2, side3):
        print("Is a triangle")
    else:
        print("Not a triangle")


if __name__ == "__main__":
    main()
