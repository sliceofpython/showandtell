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
        average = (max(current) - min(current))/2
        if average == 1: # if the average is equal to 1 then the number must be the average of the string
            answer = min(current) + 1
            print("Your number is %s!" % answer)
            break
        else:
            number = int(average + min(current))
            n = input("Is your number %s? " % number)
        # Set the 'magic value' to the average of the min and max values of current

 #Next question

    elif n.lower().startswith('l'): # The answer is something like lower.
        current[current.index(max(current))] = number
        # Take the index of the maximum value of the 'current' list and change it to the "magic number"
        average = (max(current) - min(current))/2
        if average == 1: # if the average is equal to 1 then the number must be the average of the string
            answer = min(current) + 1
            print("Your number is %s!" % answer)
            break
        elif current[0] == 1 and current[1]==2:
            print("Your number is 1!")
            break

        else:
            number = int(average + min(current))
            # Set the 'magic value' to the average of the min and max values of current
            n = input("Is your number %s? " % number) #Next question

