# Is the number odd or even?
number = input('Pick a number any number. ')

while not number.isdigit():
    print('Please pick a number. Example: 5 ')
    number = input('Pick a number any number. ')
    
oddoreven = int(number) # Turn string to an integer

result = oddoreven % 2

if result:
    print(number + " is an odd number.")
else:
    print(number + " is an even number.")
