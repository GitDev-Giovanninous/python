import qrcode as qr
from pathlib import Path

def choice():
    while True:
        try:
            var = int(input("Enter your choice: "))
            return var
        except ValueError:
            print("Invalid input. Please enter a number.")

def qr_code_generator():

    while True:

        link = input("Enter the link to generate QR code (https://www. format): ")

        if link.startswith("https://www."):
            qr_code = qr.make(link)

            qr_path = Path.home() / "Downloads" / "qrcode.png"
        
            qr_code.save(qr_path)
        
            print(f"QR code generated and saved in {qr_path}")

            break

        else:
            print("Invalid link format. Please ensure it starts with 'https://www.'")


def main():
    while True:
        print("""\nQR CODE GENERATOR:
1. Generate QR Code
2. Exit""")

        user_choice = choice()

        if user_choice == 1:
            qr_code_generator()
        elif user_choice == 2:
            break

if __name__ == "__main__":
    main()


