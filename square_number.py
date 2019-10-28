#!/usr/bin/env python3

# Created by Marwan Mashaly
# Created on October 2019
# This program lets user to know the square of numbers until input


def main():
    # This Function lets user to know the square of numbers until input
    # input
    positive_integer = input("Enter number for loop: ")
    print("")
    # process & output
    try:
        number = int(positive_integer)
        for square_number in range(number + 1):
            total = square_number**2
            print("the square number for ", square_number, ("="), total)

    except ValueError:
        print("Invalid input.")
    finally:
        print("")
        print("Thanks for trying")


if __name__ == '__main__':
    main()
