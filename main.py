import random
import string
import sys
import time
from getpass import getpass
import pyperclip

def generate_password(length, use_uppercase=True, use_numbers=True, use_special_char=True):
    if length < 8:
        print("The password length should be at least 8.")
        return None

    char_set = string.ascii_letters

    if use_uppercase:
        char_set += string.ascii_uppercase
    if use_numbers:
        char_set += string.digits
    if use_special_char:
        char_set += string.punctuation

    password = ''

    for i in range(length):
        password += random.choice(char_set)

    return password


length = int(input("Enter the desired password length (at least 8): "))
use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
use_special_char = input("Include special characters? (y/n): ").lower() == 'y'


password = generate_password(length, use_uppercase, use_numbers, use_special_char)
print(f"\nGenerated password: {password}\n")
print("Press Enter to copy password to clipboard and close this script")
sys.stdin.readline()


pyperclip.copy(password)


print("Password has been copied to clipboard. Keep this terminal open for 15 seconds...")
time.sleep(15)
sys.exit()