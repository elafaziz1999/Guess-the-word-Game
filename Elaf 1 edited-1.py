import  turtle
from turtle import*
MAX_CHANCES = 8

turtle.title("Elaf's Guess The Word Game")
turtle.bgcolor("yellow")
t1 = turtle.Turtle()
p1=Pen()
p2=Pen()

#check if p2Guess char is in p1Word
#if found return True,
#otherwise return false
def isCorrectP2guess(p1Word,p2Guess):
    #for each character in p1Word check if p2Guess or there or not...
    #if found return True
    for i in range(len(p1Word)):
        if p1Word[i]==p2Guess:
            return True
    return False 




def addUpText(hiddenGauss):
    #unchanged
    p1.clear()
    p1.color('blue','blue')

    p1.up()
    p1.goto(-350,290)
    p1.down()
    p1.write("Guess the word:", False, font=("Comic Sans MS italic", 18, 'bold'))
    p1.hideturtle()

    
    p1.color('blue','blue')
    p1.up()
    p1.goto(-300,250)
    p1.down()
    p1.write(hiddenGauss, False, font=("Comic Sans MS italic", 24, 'bold'))

    

    


def addDownText(allMissedInput,missCount):
    #will be changed by addMissGuessUpToNow
    p2.clear()
    
    p2.up()
    p2.goto(-350,-210)
    p2.down()
    p2.color('blue','blue')
    p2.write("Wrong Guesses:", False, font=("Comic Sans MS italic", 18, 'bold'))
    p2.hideturtle()

    p2.up()
    p2.goto(-300,-240)
    p2.down()
    p2.color('red','red')
    p2.write('  '.join(allMissedInput), False, font=("Comic Sans MS italic", 20, 'bold'))


    
    
    p2.up()
    p2.goto(-100,-300)
    p2.down()
    attemptInfo = 'Attempts Left: '+str(MAX_CHANCES-missCount)
    p2.write(attemptInfo, False, font=("Helvetica 17 italic", 12, 'bold'))



    
def addWinInfo():
    p2.up()
    p2.penup()
    p2.goto(-100,-150)
    p2.pencolor("green")
    p2.write("YOU WIN!","left",font=("Comic Sans MS",30,"bold","italic"))


def addLoseInfo():
    p2.penup()
    p2.goto(-100,-150)
    p2.pencolor("red")
    p2.write("YOU LOSE!","left",font=("Comic Sans MS",30,"bold"))

#find all index where p2Guess char is in p1Word
#then replace the * in p2Word with p2Guess for the index found
def alterP2Word(p1Word,p2Word,p2Guess):
    #for each character in p1Word check if p2Guess or there or not at index i, where i run from 0 to len(p1Word)
    #if found, replace the p2Word char at the index i with p2Guess
    #**dont use break, because there is chance p1Word has two or more repeated char
    for i in range(len(p1Word)):
            if p2Guess[0] == p1Word[i]:
                p2Word=p2Word[:i]+p2Guess[0]+p2Word[i+1:]
                #p2Word[i]=p2Guess[0]
    return p2Word
'''
def addMissInfo(missWordList):
    t1.goto(-200,-100)
    t1.pencolor("blue")
    t1.write("Missing Words:","left",font=("comic sans",20,"bold","italic"))
    t1.goto(-150,-120)
    t1.write(', '.join(missWordList),"left",font=("comic sans",20,"bold","italic"))
'''
def buildCarByParts(missCount):
    #carete object here

    
    
   

    
    if missCount ==1:
        #replace this print code with drawing the front of the ambulance
        #print("Draw first part[front of the ambulance]")
        t1.penup()
        t1.goto(0,0)
        t1.pendown()
        t1.fillcolor("white")
        t1.begin_fill()
        for i in range(4):
            t1.pencolor("blue")
            t1.forward(90)
            t1.right(270)
        t1.end_fill()
        t1.penup()
    if missCount ==2:
        ##replace this print code with drawing the back of the ambulance
        #print("Draw second part[back of the ambulance]")
        t1.penup()
        t1.goto(0,0)
        t1.pendown()
        t1.fillcolor("white")
        t1.begin_fill()
        for i in range(4):
            t1.pencolor("blue")
            t1.backward(180)
            t1.right(90)
        t1.end_fill()
        t1.penup()
    if missCount ==3:
        #replace this print code with drawing first wheel
        #print("Draw third part[wheel 1]")
        t1.penup()
        t1.goto(-90,-30)
        t1.pendown()
        t1.fillcolor("blue")
        t1.begin_fill()
        t1.pencolor("blue")
        for i in range(1):
            t1.circle(30)
            t1.penup()
            t1.backward(90)
        t1.end_fill()
    if missCount ==4:
        #replace this print code with drawing second wheel
        #print("Draw fourth part[wheel 2]")
        t1.penup()
        t1.goto(35,-30)
        t1.pendown()
        t1.fillcolor("blue")
        t1.begin_fill()
        t1.pencolor("blue")
        for i in range(1):
            t1.circle(30)
            t1.penup()
            t1.backward(90)
        t1.end_fill()
    if missCount ==5:
        #replace this print code with drawing window
        #print("Draw window")
        t1.penup()
        t1.goto(20,80)
        t1.pendown()
        t1.fillcolor("white")
        t1.begin_fill()
        for i in range(4):
            t1.pencolor("blue")
            t1.forward(45)
            t1.right(90)
            t1.forward(22.5)
            t1.right(90)
        t1.end_fill()
        t1.penup()
    if missCount ==6:
        #replace this print code with drawing plus sign part 1
        #print("Draw plus sign part 1")
        t1.penup()
        t1.goto(-110,160)
        t1.pendown()
        t1.fillcolor("red")
        t1.begin_fill()
        for i in range(4):
            t1.pencolor("red")
            t1.forward(45)
            t1.right(90)
            t1.forward(90)
            t1.right(90)
        t1.end_fill()
        t1.penup()
    if missCount ==7:
        #replace this print code with drawing plus sign part 2
        #print("Draw plus sign part 2")
        t1.penup()
        t1.goto(-140,140)
        t1.pendown()
        t1.fillcolor("red")
        t1.begin_fill()
        for i in range(4):
            t1.pencolor("red")
            t1.forward(105)
            t1.right(90)
            t1.forward(45)
            t1.right(90)
        t1.end_fill()
        t1.penup()
    if missCount ==8:
        #replace this print code with drawing siren
        #print("Draw siren")
        t1.penup()
        t1.goto(-110,202)
        t1.pendown()
        t1.fillcolor("red")
        t1.begin_fill()
        for i in range(4):
            t1.pencolor("blue")
            t1.forward(45)
            t1.right(90)
            t1.forward(22.5)
            t1.right(90)
        t1.end_fill()
        t1.penup()
        
def mainGame():
    missCount=0
    flagMatched = False
    missWordList=[]
    print("----------PLAYER 1----------")
    print("                                    ")
    print("(Make sure PLAYER 2 is not peaking!)")
    print("                                    ")
    print("Enter your word (if it has a space, use '-', e.g. ice-cream):", end=" ")
    p1Word = input()
    p2Word = "*"*len(p1Word)
    #scroll the screen such that player 2 cannot see
    
    print("\n"*50)
    print("----------PLAYER 2----------")
    print("                                    ")
    addUpText(p2Word)
    addDownText(missWordList,missCount)
    while missCount<MAX_CHANCES:
        
        print(p2Word)
        print("Guess a word [only first character considered]::")
        p2Guess = input()
        #incase player2 enter more than one character, only take first one
        p2Guess = p2Guess[0]
        #check if p2guess is in p1Words
        flagP2Guess = isCorrectP2guess(p1Word,p2Guess)
        #if guess is correct alter p2Word, otherwise increase missCount
        if flagP2Guess == True:
            p2Word=alterP2Word(p1Word,p2Word,p2Guess)
            addUpText(p2Word)
        else:
            missWordList.append(p2Guess)
            missCount = missCount+1
            buildCarByParts(missCount)
            addDownText(missWordList,missCount)
            #addMissInfo(missWordList)
        #check if p2 has got all world  correct
        if p2Word == p1Word:
            flagMatched=True
            break
        print('Missed Word List ',missWordList)
        
            
    if flagMatched == True:
        print("Well Done.....")
        addWinInfo()
    else:
        print("You Lose....")
        addLoseInfo()

while True:
    t1.clear()
    mainGame()
    print("\nDo you want to continue")
    print("\nPress x for exit")
    print("\nPress any key (excpet x ) for continue:\n")
    ans=input()
    if ans=='x' or ans =='X':
        break
    

        



    
