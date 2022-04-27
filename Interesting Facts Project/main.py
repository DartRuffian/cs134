"""
"Note:  While you will customize menu wording, use the function names provided in the instructions.
This will make grading easier."

CamelCase is not the standard for function names in Python, snake_case should be used.
I'll use the given names for the functions defined in the project details, but for other functions I will
be using snake_case, as that is the standard and preferred way to name Python methods and functions.
"""

# Imports
from tabulate import tabulate  # Display information neatly
import json                    # Used to load the olympic data


def load_json(filename: str) -> list:
    if not filename.endswith(".json"):
        filename += ".json"

    with open(filename, "r") as f:
        return json.load(f)


class InterestingFacts:
    def __init__(self):
        self.countries, self.medals = InterestingFacts.__load_olympics_data()
        self.menu()

    @staticmethod
    def __load_olympics_data() -> tuple:    # tuple[list[str],[list[list[int]]]
        countries = load_json("countries")  # [country, country...]
        medals = load_json("medals")        # [[gld, slvr, brz], [gold, slvr, brz]...]

        for medal_count in medals:
            # Dynamically add the total amount of medals for each set
            medal_count.append(sum(medal_count))

        return countries, medals

    @staticmethod
    def __get_user_selection() -> int:
        while True:
            print(f"""Select an option from the list below:
1. Display Data for Single Country
2. Display All Olympic Data
3. Compare Two Countries
4. Exit""")
            try:
                selection = int(input("Enter your selection: "))
                break

            except ValueError as e:
                e = str(e).split("'")[1]  # Get user's input
                print(f"Sorry, we couldn't find an option under {e!r}, please try again.\n\n")

        if selection < 1:
            selection = 1

        elif selection > 4:
            selection = 4

        return selection

    @staticmethod
    def display_given_data(data) -> None:
        print("\n")
        print(tabulate(data, headers=["Country", "Gold Medals", "Silver Medals", "Bronze Medals", "Total"]))

    def get_country_user_input(self) -> tuple:  # tuple[str, int]
        """Queries ther user for a country from the countries data set, and returns the country name and index"""
        while True:
            country_name = input("Enter the name of the country that you would like to view the olympic data of:\n")
            country_name = " ".join([name.capitalize() for name in country_name.split(" ")])
            index = self.findIndex(country_name)

            if index == -1:
                print("Sorry, that country does not exist within our data set, please try again.\n")
            else:
                break

        return country_name, index

    def findIndex(self, country_name: str) -> int:
        # Should be find_index
        if country_name not in self.countries:
            return -1

        return self.countries.index(country_name)

    def menu(self):
        selection = self.__get_user_selection()
        # The Repl you provided uses Python 3.8.12
        # If it was updated to 3.10, then this whole if/else block could be a simple enum

        if selection == 1:
            # Display data for single country
            _, index = self.get_country_user_input()
            self.displayInformation(index)

        elif selection == 2:
            # Display data for all countries
            self.displayAllInformation()

        elif selection == 3:
            # Compare two countries
            print("First Country:")
            _, index_country_one = self.get_country_user_input()
            print("Second Country:")
            _, index_country_two = self.get_country_user_input()

            self.compareTwoItems(index_country_one, index_country_two)

        else:
            # Exit
            exit()

    def displayInformation(self, index: int) -> None:
        """Display data for a single country"""
        data = [[self.countries[index]] + self.medals[index]]
        self.display_given_data(data)

    def displayAllInformation(self):
        """Display information for all countries"""
        data = [[country]+self.medals[index] for index, country in enumerate(self.countries)]
        self.display_given_data(data)

    def compareTwoItems(self, index_country_one, index_country_two):
        """Compare Olympic Data between two countries"""
        data = [[self.countries[index_country_one]] + self.medals[index_country_one],
                [self.countries[index_country_two]] + self.medals[index_country_two]]
        self.display_given_data(data)


def main() -> None:
    InterestingFacts()


if __name__ == "__main__":
    main()
