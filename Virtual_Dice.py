"""Virtual Dice
- Rolls a dice
- Saves your previous rolls"""


import random as r

rolls = 0
previous_rolls = []

def roll_dice():
    global rolls
    global previous_rolls

    dice = r.randint(1, 6)
    print(f"\nThe dice chosen is {dice}")
    rolls += 1
    previous_rolls.append(dice)
    print(f"\nYou rolled {rolls} times, your previous rolls were {previous_rolls}")

    print("\nWelcome to the Virtual Dice!")
    while True:
        roll_dice()

        wanna_continue = input("\nWould you like to continue? (yes/no) ").lower()

        while wanna_continue not in ("yes", "no"):
            print("Please enter yes or no.")
            wanna_continue = input("\nWould you like to continue? (yes/no) ").lower()

        if wanna_continue == "no":
            print("\nThanks for coming!")
            break