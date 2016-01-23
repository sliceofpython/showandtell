'''
PyPig
Chra94

Two player, proof of concept
'''


import random

score = {'PlayerOne': 0, 'PlayerTwo': 0}

def turn(player):
    global score
    player = 'PlayerOne'
    
    while True:
        turn = 0
        print(player + ' is up!')
        print('You have ' + str(score[player]) + ' points.')

        while True:    
            print('Press enter to roll (or enter "hold" to hold)')
            enter = input()
            if enter == '':
                dice = random.randint(1, 6)               
                if dice == 1:
                    print('Oh no, it\'s a one!')
                    print('Your score is ' + str(score[player]))
                    break
                else:
                    print('The dice shows ' + str(dice))  
                    print(str(dice) + ' points added to turn')
                    turn += dice
                    print('Your turn score is ' + str(turn))
                    
            elif enter.lower() == 'hold':
                score[player] += turn
                print('Points held. Your score is ' + str(score[player]))
                break

        if player == 'PlayerOne':
            player = 'PlayerTwo'
        else:
            player = 'PlayerOne'

turn('PlayerOne')
print(score)
