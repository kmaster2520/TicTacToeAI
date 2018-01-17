import pickle

# computer is x
# player is o
# computer always goes first

with open("gametree.pkl", "rb") as f:
    states = pickle.load(f)

    curr = '---------'
    while True:
        curr = states[curr]
        #
        print(curr[0] + curr[1] + curr[2])
        print(curr[3] + curr[4] + curr[5])
        print(curr[6] + curr[7] + curr[8])
        #
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



