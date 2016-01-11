# Reversed Guess Game
# By VR29
# Idea on http://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html

print("Take a number between 1 and 100 in your mind.")
print("Answer the questions with 'higher', 'lower' or 'yes'")

current = [1,100]
number = 50

n = input("Is your number %s? " % number)
while True:
    if n.lower().startswith('y'):
        print("Yay!")
        break
    elif n.lower().startswith('h'):
        current[current.index(min(current))] = number
        number = int((max(current) - min(current))/2 + min(current))
        print (current)
        n = input("Is your number %s? " % number)
    elif n.lower().startswith('l'):
        current[current.index(max(current))] = number
        print (current)
        number = int((max(current) - min(current))/2 + min(current))
        n = input("Is your number %s? " % number)