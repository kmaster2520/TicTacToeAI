import pickle
from training import didWin

# computer is x
# player is o

curr = '---------C'
with open("gametree.pkl", "rb") as f:
    states = pickle.load(f)

def printState():
    print(curr[0] + curr[1] + curr[2])
    print(curr[3] + curr[4] + curr[5])
    print(curr[6] + curr[7] + curr[8])
    print()


def computerTurn():
    global curr

    print('Computer move: ')
    curr = states[curr]

    if states[curr] == 'x win':
        print('Computer Wins')
        return 0
    
    if states[curr] == 'tie':
        print('Tie')
        return 0

    return 1

def playerTurn():
    global curr

    mov = 0
    while True:
        mov = int(input('Your Move (1-9): '))
        if mov > 9 or mov < 1:
            print('Invalid Number, Must be 1-9')
            continue
        if curr[mov-1] != '-':
            print('Already taken')
            continue
        break
    #
    mov -= 1
    curr = curr[:mov] + 'o' + curr[mov+1:]

    if states[curr] == 'o win':
        print('Player Wins')
        return 0

    if states[curr] == 'tie':
        print('Tie')
        return 0

    return 1

while True:
    order = str(input('Press 1 for player-first, 0 for computer-first: '))
    if order == '1' or order == '0':
        break

if order == '0':
    curr = '---------C'
    while True:
        # computer turn
        printState()
        if not computerTurn():
            printState()
            break
        # player turn
        printState()
        if not playerTurn():
            printState()
            break

if order == '1':
    curr = '---------P'
    while True:
        # player turn
        printState()
        if not playerTurn():
            printState()
            break
        # computer turn
        printState()
        if not computerTurn():
            printState()
            break
        
    



