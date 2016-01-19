'''
Blackjack
chra94
'''

import random


def standard():
    global cardList, playerCards, houseCards, decisions
    cardList = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4

    playerCards = []
    houseCards = []
    decision = ''
    print('You have ' + str(chips) + ' chips.')
    global bet
    bet = int(input('How much do you bet?\n'))


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
    global chips
    if sum(playerCards) > 21:
        print('The house always wins!')
        chips -= bet
        print('You lost ' + str(bet) + ' chips.')
    elif sum(houseCards) > 21:
        print('The house busted, you win')s
        chips += bet
        print('You won ' + str(bet) + ' chips.')
    elif sum(playerCards) == sum(houseCards):
        print("It's a draw")
    elif sum(playerCards) < sum(houseCards):
        print('The house always wins!')
        chips -= bet
        print('You lost ' + str(bet) + ' chips.')
    else:
        print('You win')
        chips += bet
        print('You won ' + str(bet) + ' chips.')

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

chips = 20
bet = 0
main()
