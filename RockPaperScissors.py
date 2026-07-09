"""Rock Paper Scissors game
Hi guys, I hope you enjoy this project of mine.
If you have any suggestions or comments, please let me know on Discord!
Discord name: giovanninous"""

import random as r

# ITEMS
items = ["rock", "paper", "scissors"]

# FUNCTIONS
def bot_choice():
    return r.choice(items)

def player_choice():
    while True:
        player = input("Choose between rock, paper, or scissors: ").lower()
        if player in items:
            return player
        else:
            print("\nYou have to choose between rock, paper, or scissors")

def play_again():
    while True:
        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again == "yes":
            return True
        elif again == "no":
            return False
        else:
            print("Invalid input!")


# SCORES
bot_score = 0
player_score = 0

# GAME
while True:
    print("\nWelcome to Rock Paper Scissors!")
    bot = bot_choice()
    player = player_choice()
    match(bot, player):
        case (x, y) if x == y:
            print(f"It's a tie! Bot chose {bot}, player chose {player}")
            print(f"Bot: {bot_score}, Player: {player_score}")
        case ("rock", "paper") | ("paper", "scissors") | ("scissors", "rock"):
            print(f"Player wins! Bot chose {bot}, player chose {player}")
            player_score += 1
            print(f"Bot: {bot_score}, Player: {player_score}")
        case ("rock", "scissors") | ("paper", "rock") | ("scissors", "paper"):
            print(f"Bot wins! Bot chose {bot}, player chose {player}")
            bot_score += 1
            print(f"Bot: {bot_score}, Player: {player_score}")
        case _:
            print("Invalid input!")

    if not play_again():
        print("Thanks for playing!")
        break