# Reversed Guess Game
# By VR29
# Idea on http://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html

print("Take a number between 1 and 100 in your mind.")
print("Answer the questions with 'higher', 'lower' or 'yes'")

current = [1,100]
number = 50

n = input("Is your number %s? " % number)
while True:
    if n.lower().startswith('y'): # The answer is something like yes.
        print("Yay!")
        break

    elif n.lower().startswith('h'): # The answer is something like higher.
        current[current.index(min(current))] = number
        # Take the index of the minimum value of the current list and change it to the "magic number"
        number = int((max(current) - min(current))/2 + min(current))
        # Set the 'magic value' to the average of the min and max values of current

        n = input("Is your number %s? " % number) #Next question

    elif n.lower().startswith('l'): # The answer is something like lower.
        current[current.index(max(current))] = number
        # Take the index of the maximum value of the 'current' list and change it to the "magic number"

        number = int((max(current) - min(current))/2 + min(current))
        # Set the 'magic value' to the average of the min and max values of current

        n = input("Is your number %s? " % number) #Next question