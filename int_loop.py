#!/usr/bin/env python3

# Created by Brian Musembi
# Created on May 2021
# This program shows every integer from 1000-2000
#      using 1 loop and an if statement


def main():
    # This function shows every integer from 1000-2000
    #      using 1 loop and an if statement

    print("This program shows every integer from "
          "1000 to 2000.")

    # variable declarations
    loop_counter = 0

    # process
    for counter in range(1000, 2000 + 1):
        if counter % 5 != 4:
            print(counter, " ", end="")
        else:
            print(counter)


if __name__ == "__main__":
    main()
