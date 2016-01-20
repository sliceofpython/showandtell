'''
Blackjack
chra94
'''

import random
import sys


# Globals
chips = 20
bet = 0

def standard():
    global cardList, playerCards, houseCards, decisions, blackjack, bet
    cardList = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
    playerCards = []
    houseCards = []
    decision = ''
    blackjack = False
    print('You have ' + str(chips) + ' chips.')
    while True:
        try:
            bet = int(input('How much do you bet?\n'))
            if bet < 1:
                raise AssertionError
            elif bet > chips:
                raise NameError
            break
        except ValueError:
            print('Incorrect input, try again.')
        except NameError:
            print("You don't have that many chips!")
        except AssertionError:
            print("I see what you're trying. LOOOL.")

def dealCards():
    global blackjack
    for i in range(2):
        r = random.randint(0, (len(cardList) - 1))
        playerCards.append(cardList[r])
        del cardList[r]
    for i in range(2):
        r = random.randint(0, (len(cardList) - 1))
        houseCards.append(cardList[r])
        del cardList[r]
    playerCards.sort()
    print('House cards : [' + str(houseCards[1]) + ']')
    if sum(playerCards) == 21:
        blackjack = True


def playerTurn():
    while True:
        while sum(playerCards) > 21 and 11 in playerCards:
            playerCards.sort()
            playerCards[len(playerCards) - 1] = 1
            if sum(playerCards) > 21 and 14 not in playerCards:
                break
        if sum(playerCards) > 21:
            break
        playerCards.sort()
        print('Your cards are: ' + str(playerCards) + '.')
        print('The sum of your cards is: [' + str(sum(playerCards)) + ']')
        try:
            decision = input('Do you stand or hit?\n')
            if decision == 'stand':
                break
            elif decision == 'hit':
                r = random.randint(0, (len(cardList) - 1))
                playerCards.append(cardList[r])
                del cardList[r]
        except ValueError:
                pass

        print('Incorrect input, try again')


def houseTurn():
    while True:
        if sum(houseCards) < 17:
            while sum(houseCards) < 17:
                r = random.randint(0, (len(cardList)- 1))
                houseCards.append(cardList[r])
                del cardList[r]
        elif sum(houseCards) > 21 and 11 in (houseCards):
            houseCards.sort()
            houseCards[(len(houseCards) - 1)] = 1
            if sum(playerCards) > 21 and 14 not in houseCards:
                break
        elif sum(houseCards) >= 17:
            break

def printCards():
    playerCards.sort(), houseCards.sort()
    print('Player cards: ' + str(playerCards), '\nHouse cards:' + str(houseCards))
    print('Sum player: [' + str(sum(playerCards)) + '] Sum house: [' + str(sum(houseCards)) + ']')

def findWinner():
    global chips
    if sum(playerCards) == sum(houseCards):
        print("It's a draw")
    elif blackjack:
        print('Blackjack!')
        print('You won ' + str(round(bet*3/2)) + ' chips.')
        chips += round(bet*3/2)
    elif sum(playerCards) > 21:
        print('The house ALWAYS wins!')
        chips -= bet
        print('You lost ' + str(bet) + ' chips.')
    elif sum(houseCards) > 21:
        print('The house busted, you win.')
        chips += bet
        print('You won ' + str(bet) + ' chips.')
    elif sum(playerCards) < sum(houseCards):
        print('The house ALWAYS wins!')
        chips -= bet
        print('You lost ' + str(bet) + ' chips.')
    else:
        print('You win.')
        chips += bet
        print('You won ' + str(bet) + ' chips.')

    if chips == 0:
        print('No chips? THE HOUSE ALWAYS WINS.')
        sys.exit()
    elif chips > 100:
        print('Congratulations, you defeated the house.')
        sys.exit()


def playAgain():
    while True:
        try:
            decide = input('Do you want to play again? yes/no\n')
            if decide == 'no':
                print("You'll be back.")
                sys.exit()
            elif decide == 'yes':
                main()
        except ValueError:
            pass

        print('Incorrect input, try again')


def main():
    standard()
    dealCards()
    playerTurn()
    houseTurn()
    printCards()
    findWinner()
    playAgain()

print('Welcome to The House.')
main()
