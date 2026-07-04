"""This is my second project with Python!!
If you have suggestions or comments tell me on discord!!"""

import random as r

while True:
    print("I thought of a number from 1 to 100, guess it! ")
    number_to_guess = r.randint(1, 100)
    attempts = 0
    try:
        attempt = int(input("Choose a number: "))
    except ValueError:
        print("Please enter a number!")
        continue

    while True:
        attempts += 1
        if attempt > number_to_guess:
            try:
                attempt = int(input("The number you chose is bigger than the one you guessed! Try again: \n"))
            except ValueError:
                print("Please enter a number!")
        elif attempt < number_to_guess:
            try:
                attempt = int(input("The number you chose is smaller than the one you guessed! Try again: \n"))
            except ValueError:
                print("Please enter a number!")
        elif attempt == number_to_guess:
            print(f"You guessed the number in {attempts} attemps!\n ")
            break

    again = input("Do you want to try again? (y/n): ").lower()
    if again == "y":
        continue
    elif again == "n":
        print("Goodbye!\n")
        break
    else:
        print("Invalid input")

"""This is a beta, I will add many more things soon in a new file"""