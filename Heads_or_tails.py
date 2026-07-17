"""Head or tails:
- Flip an immaginary coin
- wait 3 seconds before the flip
- chooses between heads and tails"""


import random as r
import time as t

choices = ["Heads", "Tails"]

def do_again():
    while True:
        user_input = input("\nDo you want to continue? (yes/no): \n").lower().strip()
        if user_input == "yes":
            return True
        elif user_input == "no":
            return False



def main():
    while True:
        print("\n===== HEAD OR TAILS =====")

        bot_choice = r.choice(choices)

        print("\nI'm flipping the coin...")
        t.sleep(3)
        print(f"\n{bot_choice}!")

        if not do_again():
            print("Thanks!")
            break


if __name__ == "__main__":
    main()
