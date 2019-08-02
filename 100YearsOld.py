# When will you be 100 years old
name = input("What is your name?: ")  # Get users name
agestr = input("How old are you? ")

while not agestr.isdigit():  # Loop until a number is entered
    print('Please enter a number. Example 30 ')'
    agestr = input("How old are you? ")

if agestr.isdigit():
    age = int(agestr)

years = 100 - age

print("In " + str(years) + " years, " + name + " will be 100 years old.")
