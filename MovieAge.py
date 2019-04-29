# Movie age

print('Are you old enough to see a movie? \nLet\'s find out.')
agestr = input('How old are you? ')
rating = input('What is the movie rated? ')

while not agestr.isdigit():
    print('Enter a number please. Example: 18')
    agestr = input('How old are you? ')

age = int(agestr)
ratings = ['R', 'PG-13', 'PG', 'G']
print(ratings[0])
if ratings[0] == 'R' and age >= 17:
    print('Congratulations! You can see the R Rated movie. ')
elif ratings[0] == 'R' and age < 17 and age >= 13:
    print('You are not old enough to see an R rated movie. Nice try kid.')
   
elif ratings[1] == 'PG-13' and age >= 13:
    print('Congratulations! You can see the PG-13 movie. ')
elif ratings[1] == 'PG-13' and age < 13 and age >= 6:
    print('You are not old enough to see a PG-13 rated movie. Stick to your dinosaurs. ')
   
elif ratings[2] == 'PG' and age >= 6:
    print('You need to be 6 or older to view PG Rated movies. ')
elif ratings[2] == 'PG' and age < 6:
    print('You are not old enough to see a movie rated PG. ')
   
elif ratings[3] == 'G':
    print('Anyone can see a G rated movie you narc. ')

else:
    print('You are not old enough to see your movie. Sorry kid.')

