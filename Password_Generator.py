

from pathlib import Path
import secrets as se
import string as s

letters = s.ascii_letters
numbers = s.digits
symbols = s.punctuation
all_characters = letters + numbers + symbols
password_without_symbols = letters + numbers
password_without_numbers = letters + symbols

def generate_password(characters, length):
    password = ""

    for character in range(length):
        password += se.choice(characters)

    return password

while True:
    print("\nWelcome to the Password Generator!")
    while True:
        try:
            required_characters = int(input("Please enter a number of characters: "))
            if required_characters < 12 or required_characters > 40:
                print("Please enter a number between 12 and 40")
            else:
                break
        except ValueError:
            print("Please enter a number")

    want_numbers = (input("Do you want numbers?: ")).lower()
    want_symbols = (input("Do you want symbols?: ")).lower()
    while want_numbers not in ("yes", "no") or want_symbols not in ("yes", "no"):
        print("Please enter yes or no")
        want_numbers = (input("Do you want numbers?: ")).lower()
        want_symbols = (input("Do you want symbols?: ")).lower()

    match (want_numbers, want_symbols):
        case ("yes", "yes"):
            characters = all_characters
        case ("yes", "no"):
            characters = password_without_symbols
        case ("no", "yes"):
            characters = password_without_numbers
        case ("no", "no"):
            characters = letters
        case _:
            print("Error")

    password = generate_password(characters, required_characters)
    print(f"\nThe password I generate is: {password} ")
    while True:
        save_password = input("Do you want to save your password in a file?: ").lower()

        if save_password in ("yes", "no"):
            break

        print("Please enter yes or no")

    if save_password == "yes":
        file_path = Path.home() / "Desktop" / "Password_generated.txt"
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(password + "\n")
            print(f"Saved your password in {file_path}")
    elif save_password == "no":
        pass
    else:
        print("Error")

    wanna_another_password = input("Do you want another password?: ").lower()
    if wanna_another_password == "yes":
        continue
    else:
        print("\nThank you for using Password Generator!")
        break