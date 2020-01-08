# This script is used to generate a password of random characters

import string
from random import *

characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(choice(characters) for x in range(randint(18, 24)))
print password
