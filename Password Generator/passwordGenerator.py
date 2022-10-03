# A small script to generate a strong password
from random import randint


def generate_length():
    # generate a password between 12-16 characters long
    length_of_password = randint(12, 16)
    return length_of_password


def generate_lowercase_letters():
    letter = chr(randint(97, 122))
    return letter


def generate_symbol():
    symbols = ["!", "@", "#", "$", "%", "&", "*", "?"]
    symbol = symbols[randint(0, len(symbols) - 1)]
    return symbol


def generate_number():
    number = chr(randint(48, 57))
    return number


def generate_password():
    length = generate_length()
    password = ""
    for i in range(length):
        flip = randint(0, 3)
        if flip == 0:
            password += str(generate_lowercase_letters())
        elif flip == 1:
            password += str(generate_lowercase_letters()).upper()
        elif flip == 2:
            password += str(generate_symbol())
        else:
            password += str(generate_number())

    return password


if __name__ == "__main__":
    print(generate_password())
