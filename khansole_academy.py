"""
File: khansole_academy.py
-------------------------
Create a program that generates a simple addition problem and determine if the answer is correct or not.
Program should keep giving the user problems until the user has gotten 3 problems correct in a row.
"""

import random

MIN_NUM = 10
MAX_NUM = 99

def main():
    number = 0 # specified for number of problems solved
    while number != 3:

        # Constants defined in while loop so that it can re-call the method and update each loop
        NUM1 = random.randint(MIN_NUM, MAX_NUM)
        NUM2 = random.randint(MIN_NUM, MAX_NUM)
        TOTAL = NUM1 + NUM2

        # Print question
        print("What is " + str(NUM1) + " + " + str(NUM2) + "? ")
        answer = int(input("Your Answer: "))
        if answer == TOTAL:
            number += 1 # adds 1 to number if answer is correct
            print("Correct! You've gotten " + str(number) + " correct in a row.")
        else:
            print("Incorrect. The expected answer is " + str(TOTAL))
            number = 0 #reset number of problems solved in a row
    print("Congratulations! You mastered addition.")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
