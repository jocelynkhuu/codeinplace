"""
File: liftoff.py
----------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""

def main():
    countdown = 11 #start at 11 to avoid fencepost bug to print starting from 10
    for i in range(10):
        countdown -= 1
        countdown = countdown # holds value of new countdown number after subtracting 1
        print(countdown)
    print("Liftoff!")



# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
