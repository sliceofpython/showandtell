'''
Blackjack
chra94
'''

import random

def standard():
    global cardList, playerCards, houseCards, decisions
    cardList = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
    #cardList = [11, 2, 3, 4, 5, 6,] * 4

    playerCards = []
    houseCards = []
    decision = ''

def dealCards():
    for i in range(2):
        r = random.randint(0, (len(cardList) - 1))
        playerCards.append(cardList[r])
        del cardList[r]
    for i in range(2):
        r = random.randint(0, (len(cardList) - 1))
        houseCards.append(cardList[r])
        del cardList[r]

def playerTurn():
    while True:
        while sum(playerCards) > 21 and 11 in playerCards:
            playerCards.sort()
            playerCards[len(playerCards) - 1] = 1
            if sum(playerCards) > 21 and 14 not in playerCards:
                break
        if sum(playerCards) > 21:
            break
        decision = input('Do you stand or hit?\n')
        if decision == 'stand':
            break
        elif decision == 'hit':
            r = random.randint(0, (len(cardList) - 1))
            playerCards.append(cardList[r])
            del cardList[r]
            print('Your cards are : ' + str(playerCards) + '.')
            print('The sum of your cards is :' + str(sum(playerCards)))

def houseTurn():
    while True:
        if sum(houseCards) < 17:
            while sum(houseCards) < 17:
                r = random.randint(0, (len(cardList)))
                houseCards.append(cardList[r])
                del cardList[r]
        elif sum(houseCards) > 21 and 11 in (houseCards):
            houseCards.sort()
            houseCards[len(houseCards) - 1] = 1
            if sum(playerCards) > 21 and 14 not in houseCards:
                break
        elif sum(houseCards) >= 17:
            break

def findWinner():
    if sum(playerCards) > 21:
        print('The house always wins!')
    elif sum(houseCards) > 21:
        print('The house busted, you win')
    elif sum(playerCards) == sum(houseCards):
        print("It's a draw")
    elif sum(playerCards) < sum(houseCards):
        print('The house always wins!')
    else:
        print('You win')

def printCards():
    print('Player cards: ' + str(playerCards), '\nHouse cards : ' + str(houseCards))
    print('Sum player: ' + str(sum(playerCards)) + ' ' + 'Sum house: ' + str(sum(houseCards)))

def playAgain():
    decide = input('Do you want to play again? yes/no\n')
    if decide == 'no':
        print('Bai')
    elif decide == 'yes':
        main()


def main():
    standard()
    dealCards()
    print('Player cards: ' + str(playerCards), '\nHouse cards : ' + str(houseCards[1]))
    playerTurn()
    houseTurn()
    printCards()
    findWinner()
    playAgain()


main()
