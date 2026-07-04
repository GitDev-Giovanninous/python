"""Hi guys, this is my first project I've published on GitHub.
This project is about a simple calculator. If you have any suggestions or comments, please let me know.
You're welcome to use my code, just don't pass it off as your own."""

menu = {
    1: "Addition",
    2: "Subtraction",
    3: "Multiplication",
    4: "Division",
    5: "Percentage",
    6: "Square",
    7: "Cube",
    8: "Power",
    9: "Exit"
}


# FUNCTIONS
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot divide by zero."
def percentage(a):
    return a/100
def square(a):
    return a**2
def cube(a):
    return a**3
def power(a,b):
    return a**b
def read_number():
    while True:
        try:
            return float(input("Choose a number: "))
        except ValueError:
            print("Please enter a valid number.")
def read_two_numbers():
    return read_number(), read_number()
def print_result(result):
    print(f"The result is: {result}\n")

# CALCULATOR
while True:
    print(f"""Welcome to the simple calculator!
In this calculator you can perform simple calculations such as addition, subtraction, multiplication and division.
Choose one of the following options:
""")
    for k,v in menu.items():
        print(f"{k}: {v}")
    try:
        user_input = int(input("Choose an option: "))
    except ValueError:
        print("Please enter a number between 1 and 9.")
        continue

    if user_input == 1:
        num1,num2 = read_two_numbers()
        print_result(add(num1, num2))
    elif user_input == 2:
        num1,num2 = read_two_numbers()
        print_result(subtract(num1, num2))
    elif user_input == 3:
        num1,num2 = read_two_numbers()
        print_result(multiply(num1, num2))
    elif user_input == 4:
        num1, num2 = read_two_numbers()
        print_result(divide(num1, num2))
    elif user_input == 5:
        num1 = read_number()
        print_result(percentage(num1))
    elif user_input == 6:
        num1 = read_number()
        print_result(square(num1))
    elif user_input == 7:
        num1 = read_number()
        print_result(cube(num1))
    elif user_input == 8:
        num1,num2 = read_two_numbers()
        print_result(power(num1, num2))
    elif user_input == 9:
        print("Thanks for using this calculator!\n")
        break
    else:
        print("Invalid input, please try again\n")

"""If you want some help you can contact me on discord. 
Add me on discord: giovanninous"""