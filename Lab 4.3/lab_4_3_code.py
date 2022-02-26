def main():
    age = int(input("Enter your age: "))
    if 0 <= age <= 12:
        team = "No Play"
    elif 13 <= age <= 19:
        team = "Teen"
    elif 20 <= age <= 64:
        team = "Adult"
    else:
        team = "Senior"

    print(f"Team: {team}")


if __name__ == "__main__":
    main()
