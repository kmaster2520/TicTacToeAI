import pickle

# game tree, maps one state to the next state
states = {} 

# value of each outcome (for the computer)
# values can be adjusted
LOSS = -10
WIN = 1
TIE = -2

def didWin(curr, c):
    ''' checks if there is a win '''

    #row
    if (curr[0] == curr[1] and curr[1] == curr[2] and curr[2] == c):
        return True
    if (curr[3] == curr[4] and curr[4] == curr[5] and curr[5] == c):
        return True
    if (curr[6] == curr[7] and curr[7] == curr[8] and curr[8] == c):
        return True

    #col
    if (curr[0] == curr[3] and curr[3] == curr[6] and curr[6] == c):
        return True
    if (curr[1] == curr[4] and curr[4] == curr[7] and curr[7] == c):
        return True
    if (curr[2] == curr[5] and curr[5] == curr[8] and curr[8] == c):
        return True

    #diag
    if (curr[0] == curr[4] and curr[4] == curr[8] and curr[8] == c):
        return True
    if (curr[2] == curr[4] and curr[4] == curr[6] and curr[6] == c):
        return True

    return False

def getResults(curr, c):
    global states

    if (didWin(curr, 'x')): #computer win
        states[curr] = 'x win'
        return WIN
    elif (didWin(curr, 'o')): #player win
        states[curr] = 'o win'
        return LOSS

    nextstates = []

    gameover = True
    # generates next states
    for i in range(9):
        if curr[i] == '-':
            nextstates.append(curr[:i] + c + curr[i+1:])
            gameover = False
    
    # if game ends in a tie
    if gameover:
        states[curr] = 'tie'
        return TIE
    
    ans = 0
    bestRes = -999999999
    bestNex = None
    for nex in nextstates:
        if c == 'x':
            res = getResults(nex, 'o')
        else:
            res = getResults(nex, 'x')
        if res > bestRes:
            bestRes = res
            bestNex = nex

        ans += res
    
    states[curr] = bestNex # selects best next state
    
    return ans / len(nextstates)
git
getResults('---------C', 'x') #computer goes first
getResults('---------P', 'o') #player goes first

with open("gametree.pkl", "wb") as f:
    pickle.dump(states, f)

#print(states['---------'])



    
