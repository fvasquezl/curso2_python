import random 
OPTIONS= {1:'piedra', 2:'papel', 3:'tijera'}
GAME ={ 'op':[0,0],'points':{'gamer':0,"computer":0}}
RULES = [(1,3),(2,1),(3,2)]

incGamer = lambda x: GAME['gamer'][0]+1
incComputer = lambda x: GAME['computer'][0]+1
increment_points:lambda func:func()

def choose_options():    
    GAME['op'][0] = int(input('>>> [1]:Piedra, [2]:papel o [3]tijera => '))
    if not GAME['op'][0] in OPTIONS.keys():
        print('Esa opción no es valida')
        choose_options()
    GAME['op'][1] = random.choice(tuple(OPTIONS))

    print('User option => ',  OPTIONS[GAME['op'][0]])
    print('Computer option => ',  OPTIONS[GAME['op'][1]])


def check_rules():
    if GAME['op'][0] == GAME['op'][1]:
        print('Empate!\n')
    elif (GAME['op'][0],GAME['op'][1]) in RULES:
        print("User Wins")
        increment_points(incGamer())
        # GAME['points'][0] +=1
    else:
        print("computer wins")
        increment_points(incComputer())
        # GAME['points'][1] +=1

def dashboard():
     print(f'''
            🙋 User wins: {GAME['points']['gamer']}
            🤖 Computer wins: {GAME['points']['computer']}
        ''')

def winner():
    if GAME['points']["gamer"]==3 or GAME['points']['computer']==3:
        w= 'USER'
        if GAME['points']['computer'] == 3:
            w ='COMPUTER' 
        print(f"El ganador es {w}")
        return True
    return False


if __name__ == "__main__":

    rounds = 1

    while not winner():
        print('***' * 10)
        print('Round ', rounds)
        print('***' * 10)

        rounds += 1
        choose_options()
        check_rules()
        dashboard()