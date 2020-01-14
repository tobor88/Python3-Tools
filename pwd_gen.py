# This script is used to generate a password of random characters
import string
import random


def pwd_gen(n):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for i in range(n))

def validate_num(num):
    if (num.isdigit()):
        vn = int(num)
        return vn 
    else:
        print("Value error occured. Enter a valid number. Example: 18")

num = input("Enter a number to define the length of the password: ")
n = validate_num(num)
password = pwd_gen(n)
print(password)
