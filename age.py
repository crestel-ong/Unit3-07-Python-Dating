#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: Sept 2021
# This is the Dating program in python


def main():
    # this function tells you if you with in the age range to date

    # input
    integer_as_string = input("Please enter your age: ")

    try:
        # convert string to integer
        user_age = int(integer_as_string)

        # process and output
        if user_age >= 25 and user_age <= 40:
            print("You are accepted to date my grandchild.")
        elif user_age < 25:
            print("You are too young!")
        elif user_age > 40:
            print("You are too old!")
    except Exception:
        print("{0} is not an integer.".format(integer_as_string))
    print("\nDone.")


if __name__ == "__main__":
    main()
