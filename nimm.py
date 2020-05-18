"""
File: nimm.py
-------------------------
1. The game starts with a pile of 20 stones between the players
2. The 2 players alternate turns
3. On a given turn, a player may take 1 or 2 stones from the center pile
4. The 2 players continue until the pile has run out of stones
5. Last play to take a stone loses.
"""

P1 = "Player 1"
P2 = "Player 2"


def main():
    STONES_AVAILABLE = 20
    while int(STONES_AVAILABLE) > 0:
        # Player 1
        print("There are " + str(STONES_AVAILABLE) + " stones left")
        take = int(input(P1 + " would you like to remove 1 or 2 stones? "))
        if take == 1 or take == 2 and int(STONES_AVAILABLE) > 0:
            STONES_AVAILABLE -= take
            if int(STONES_AVAILABLE) <= 0:
                print("")
                print("Player 2 wins!")
                break
        else:
            while take != 1 and take != 2:
                take = int(input("Please enter 1 or 2: "))
                if take == 1 or take == 2:
                    STONES_AVAILABLE -= take
                    if int(STONES_AVAILABLE) <= 0:
                        print("")
                        print("Player 2 wins!")
                        break

        # Player 2
        print("")
        print("There are " + str(STONES_AVAILABLE) + " stones left")
        take = int(input(P2 + " would you like to remove 1 or 2 stones? "))
        if take == 1 or take == 2:
            STONES_AVAILABLE -= take
            print("")
            if int(STONES_AVAILABLE) <= 0:
                print("")
                print("Player 1 wins!")
                break
        else:
            while take != 1 and take != 2:
                take = int(input("Please enter 1 or 2: "))
                if take == 1 or take == 2:
                    STONES_AVAILABLE -= take
                    print("")
                    if int(STONES_AVAILABLE) <= 0:
                        print("")
                        print("Player 1 wins!")
                        break


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
