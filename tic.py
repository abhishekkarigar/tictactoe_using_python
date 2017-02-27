import os,sys,random,time

drawn=0
series=0
board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
win=1
draw=-1
running=0
game=running
person=random.randint(1,2)
stop=1
mark='x'
score1=0
score2=0
total_series=series

def again():
    global board
    board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    global win
    win=1
    global draw
    draw=-1
    global running
    running=0
    global game
    game=running
    global person
    person=random.randint(1,2)
    global stop
    stop=1
    global mark
    mark='x'
    global series
    series=series-1
    return series


def drawboard():
    print(" %c | %c | %c "%(board[1],board[2],board[3]))
    print("___|___|___")
    print(" %c | %c | %c "%(board[4],board[5],board[6]))
    print("___|___|___")
    print(" %c | %c | %c "%(board[7],board[8],board[9]))
    print("   |   |   ")

def checkposition(x):
    if (board[x]==' '):
        return True
    else:
        return False
    
def scoreboard():
   print("      SCORE BOARD       ")
   print("  OUT OF %d MATCHES"%total_series)
   print("_________________________________ ")
   print(" AARUSH    |  ABHISHEK   |   draw ")
   print("           |             |")
   print("   %d       |     %d       |     %d     "%(score1,score2,drawn))
   print("__________________________________")
   print("\n")


def checkforwin():
    global game
    if((board[1]==board[2]==board[3]) and (board[1]!=' ')):
        game=win
    elif((board[4]==board[5]==board[6]) and (board[4]!=' ')):
        game=win
    elif((board[7]==board[8]==board[9]) and (board[7]!=' ')):
        game=win
    elif((board[1]==board[4]==board[7]) and (board[1]!=' ')):
        game=win
    elif((board[2]==board[5]==board[8]) and (board[2]!=' ')):
        game=win
    elif((board[3]==board[6]==board[9]) and (board[3]!=' ')):
        game=win
    elif((board[1]==board[5]==board[9]) and (board[1]!=' ')):
        game=win
    elif((board[3]==board[5]==board[7]) and (board[3]!=' ')):
        game=win
    elif((board[1]!=' ') and (board[2]!=' ') and (board[3]!=' ') and (board[4]!=' ') and (board[5]!=' ') and (board[6]!=' ') and (board[7]!=' ') and (board[8]!=' ') and (board[9]!=' ')):
        game=draw
    else:
        game=running


print("tic",end="")
time.sleep(2)
print(" tac",end="")
time.sleep(2)
print(" toe",end="")
print("\nbe ready folks")
series=int(input("enter the series \n>>>"))
total_series=series
while(series>0):

    while(game==running):
        drawboard()
        if(person%2!=0):
            print("AARUSH its your turn :  ")
            mark='x'
        elif(person%2==0):
            print("ABHISHEK  its your turn :  ")
            mark='o'
        choice=int(input("enter the value from  1 to 9 to put the value"))
        
        if(checkposition(choice)==True and (0<choice<10)):
            board[choice]=mark;
            person+=1
            checkforwin()
        else:
            print("      ERROR      \n")
            print("\n")
            print("please enter at the vacant place")
            choice=int(input("enter the value from  1 to 9 to put the value"))
            if(checkposition(choice)==True and (0<choice<10)):
                board[choice]=mark;
                person+=1
                checkforwin()
        
            
        checkforwin()

    drawboard()
    if(game==draw):
        print("game draw")
        drawn+=1
    elif(game==win):
        person-=1
        if(person%2!=0):
            print("AARUSH YOU won")
            print("\n")
            score1+=1
        else:
            print("ABHISHEK YOU won")
            print("\n")
            score2+=1

    scoreboard()
    again()


if score1>score2:
    print("*************************************************")
    print("\n")
    print(" AARUSH HAS WON THE SERIES  KUDOS ")
    print("\n")
    print("*************************************************")
elif score1==score2:
    print("*************************************************")
    print("\n")
    print(" DRAW MATCH ")
    print("\n")
    print("*************************************************")
    
else:
    print("*************************************************")
    print("\n")
    print(" ABHISHEK HAS WON THE SERIES  KUDOS ")
    print("\n")
    print("*************************************************")
    

'''
os.system('python tic.py')
'''
'''       
a=input("would you like to continue")
if (a=='y' or a=='Y'):
    os.execv(sys.executable,['python']+sys.argv)
    os.execv(__file__,sys.argv)
else:
    exit(0)
'''


