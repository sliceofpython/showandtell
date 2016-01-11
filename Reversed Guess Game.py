# Reversed Guess Game
# By VR29
# Idea on http://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html

print("Take a number between 1 and 100 in your mind.")
print("Answer the questions with 'higher', 'lower' or 'yes'")

number = 50
incr = 50

n = input("Is your number %s? " % number)
while True:
    if n.lower().startswith('y'):
        print("Yay!")
        break
    elif n.lower().startswith('h'):
        incr =  int((incr/2))
        number += incr
        n = input("Is your number %s? " % number)
    elif n.lower().startswith('l'):
        incr =  int((incr/2))
        number -= incr
        n = input("Is your number %s? " % number)