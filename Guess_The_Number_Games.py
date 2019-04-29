play = 'yes'
while play is 'yes':

    answer = input('========================================\n|   What game would you like to play?  |\n========================================\n\ta:\t\'100 Guesses\'\n\tb:\t\'Guess the Number\'\n\n\tAnswer is case sensitive: a or b? \n')

    if (answer is 'a'):

############################
#    GAME: 100 Guesses!    #
############################

	    print('INSTRUCTIONS: A number will be selected at random. Guess the number until you get it right. \n\tYou will be given hints if you get the answer wrong.\n\n\tGOOD LUCK!')

	    import random

	    n = random.randint(1,99)
	    user_guess = input('Pick a number between 0 and 100. Let\'s see how close you get! ')

	    if user_guess.isdigit():
	        guess = int(user_guess)

	    while n != guess:
	        print
	        if guess < n:
	            print('\tYou guessed a little low. Try Again!\n\t')
	            user_guess = input('Enter a number between 0 and 100: ')
	            if user_guess.isdigit():
	                guess = int(user_guess)
	            else:
	                print('Enter a number. Example: 98')
	        elif guess > n:
	            print('\tYou guessed a little high. Try Again!\n\t')
	            user_guess = input('Enter a number between 0 and 100: ')
	            if user_guess.isdigit():
	                guess = int(user_guess)
	            else:
	                print('Enter a number. Example: 89')
	        else:
	            break

	    print('\nCONGRATULATIONS YOU WON!!! \n\nThe number was', n)

	    import turtle
	    STAR_SIZE = 100

	    EXPANSION = 1.2
	    TRANSLATION = STAR_SIZE * EXPANSION / 4

	    turtle.hideturtle()
	    turtle.color("green")
	    turtle.shape("triangle")
	    turtle.turtlesize(STAR_SIZE * EXPANSION / 20)

	    for _ in range(5):
	        turtle.right(72)
	        turtle.forward(TRANSLATION)
	        turtle.stamp()
	        turtle.backward(TRANSLATION)

    elif answer is 'b':

#############################
#  GAME: Guess the Number!  #
#############################

        print('INSTRUCTIONS: A number will be picked at random. Try to guess what it is!!!\n\nGOOD LUCK! :) ')
        import random
    
        random_number = random.randint(1,11)
        player_guess = input('Pick a number between 1 and 10: \n')
    
        if player_guess.isdigit():
            guess = int(player_guess)
    
        while random_number != guess:
            random_number = random.randint(1,11)

            if random_number == 11:
                print('The number was', random_number, 'Bet you didn\'t seee that coming. Ha! Ha!\n')
                player_guess = input('Pick a number between 1 and 10: \n')
                if player_guess.isdigit():
                    guess = int(player_guess)

            elif random_number != 11:
                print('BOOO!!! you lost :( \nBetter luck next time loser. The number was ', random_number, '\n')
                player_guess = input('Pick a number between 1 and 10: \n')
                if player_guess.isdigit():
                    guess = int(player_guess)

        else:
            print('HOORAY!!! YOU WON A SHITTY GAME, I BET YOUR MOTHER\'S PROUD. \n', guess, 'was the correct answer,')

    else:
        print(answer, 'Was not a choice. Your answer is case sensitive. ')

else:
    print('Thanks for playing! Go jerk off or something.')
