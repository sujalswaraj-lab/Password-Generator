"""A random password generator for the terminal."""

import secrets  # like `random`, but safe to use for passwords
import string


def generate_password(length, use_numbers=True, use_symbols=True):
    characters = string.ascii_letters

    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += "!@#$%^&*()-_=+"

    password = ""
    for _ in range(length):
        password += secrets.choice(characters)

    return password


def ask_yes_no(question):
    answer = input(question + " (y/n): ").strip().lower()
    return answer == "y"


def main():
    print("=== Random Password Generator ===\n")

    while True:
        try:
            length = int(input("Password length (at least 6): "))
            if length >= 6:
                break
            print("Too short! Please choose 6 or more.\n")
        except ValueError:
            print("Please enter a whole number.\n")

    use_numbers = ask_yes_no("Include numbers?")
    use_symbols = ask_yes_no("Include symbols?")

    print("\nYour password:", generate_password(length, use_numbers, use_symbols))


if __name__ == "__main__":
    main()