#automated_number_guesser
#by chra94

#This program will find the number you select.



import random
print('Enter an integer, any integer. I will find it.')
n = int(input())
guess = random.randint(0, n*2) # Set initial guess range. n*2 makes the upper limit twice of the input number.
guess_high = n*2    #This makes it remember its highest guess \ # n*2 is to set max guess range for the first guess.
guess_low = 0       #This makes it remember its lowest guess
n_guess = 0
while guess != n:
    print("I will guess your number. My guess is " + str(guess) + '.')
    if guess < n:
        print('Damn, too low. I try again.')
        n_guess += 1
        guess_low = guess + 1                           # +1 increases its min guess value by one 
        guess = random.randint(guess_low, guess_high)   #this prevents a guess lower than a failed guess
    elif guess > n:
        print('Ach nein! Too high. I must try again.')
        n_guess += 1
        guess_high = guess - 1                          # -1 decreasess its max guess value by one
        guess = random.randint(guess_low, guess_high)   #this prevents a guess higher than a failed guess
print('Aha! Your number is ' + str(guess) + '. Your challenge is no match for me!  It only took me ' + str(n_guess) + ' attempts.')
