#!/usr/bin/env python3
# Created By: Sam V
# Date: Oct 13th, 2026
# A program to determine if a given year is a leap year.


def main():
    try:
        year = int(input("Enter a year: "))

        # Check if the number is positive
        if year <= 0:
            print("Please enter a positive year greater than 0.")
            return

        # Check if year is a leap year using logical operators
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")

    except ValueError:
        print("That is not a valid year. Please enter a valid integer.")


if __name__ == "__main__":
    main()
