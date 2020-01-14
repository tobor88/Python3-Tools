# This script is used to generate a password of random characters
import string
import random


def pwd_gen(n):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for i in range(n))


num = input("Enter a number to define the length of the password: ")

if (num.isdigit()):
    n = int(num)
    password = pwd_gen(n)
    print(password)
else:
    print("Value Error occured. Please enter a valid number next time. Example: 18")

