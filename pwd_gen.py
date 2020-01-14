# This script is used to generate a password of random characters
import sys
import string
import secrets 


def pwd_gen(n):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for i in range(n))

def validate_num(num):
    if (num.isdigit()):
        vn = int(num)
        return vn 
    else:
        print("Value error occured. Enter a valid number. Example: 18")
        sys.exit(1)

num = input("Enter a number to define the length of the password: ")
n = validate_num(num)
password = pwd_gen(n)
print(password)
