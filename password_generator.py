# -*- coding: utf-8 -*-
"""password generator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q1odPU7yLqa8E-rxEXdOTLCl9I3zZTUz
"""

import random
import string

def generate_password(length, include_letters, include_numbers, include_symbols):
    characters = ""
    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter the desired password length: "))
include_letters = input("Include letters? (y/n): ").lower() == "y"
include_numbers = input("Include numbers? (y/n): ").lower() == "y"
include_symbols = input("Include symbols? (y/n): ").lower() == "y"

password = generate_password(length, include_letters, include_numbers, include_symbols)
print("Generated Password:", password)