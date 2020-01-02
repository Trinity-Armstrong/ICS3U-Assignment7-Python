#!/usr/bin/env python3

# Created by: Trinity Armstrong
# Created on: December 2019
# This program identifies the largest number in a list


def identify(array_of_numbers):
    # This function identifies the largest number in a list
    largest_number = 0

    # Process
    for counter in range(0, len(array_of_numbers)):
        if largest_number < array_of_numbers[counter]:
            largest_number = array_of_numbers[counter]

    return largest_number


def main():
    # This function gets a list of 5 numbers from user and prints the largest

    # Instructions
    print("I will help you identify the largest number in a list of 5 numbers.\
    ")
    print("")

    # Array declaration
    number_list = []

    # Process
    try:
        for loop_counter in range(5):
            number = int(input("Enter an integer: "))
            number_list.append(number)

        # Call function
        largest = identify(number_list)

        # Output
        print("")
        print("The largest number in this list is", largest)

    except Exception:
        print("")
        print("This is not an integer, try again.")


if __name__ == "__main__":
    main()
