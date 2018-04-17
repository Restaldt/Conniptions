import random
import numpy as np
from time import sleep
import sys
def checkHueristic(Board):
    oneH = 0
    zeroeH = 0
    	

def randomPlay(Board):

    #print(Board)
    move1 = random.random()
    move2 = random.randint(0,6)
    move = (move1,move2)
    return move
def reset(Board):
    global gamesFinished
    global draws
    
    gamesFinished += 1
    Board = [[-1 for x in range(columns)] for y in range(columns)]
    return Board
def checkWin(Board):
    horizonalWin = False
    verticalWin = False
    diagonalWin = False
    # print(horizonalWin)
    # print(verticalWin)
    # print(diagonalWin)
    global gamesFinished
    global player0wins
    global player1wins
    global draws
    fullBoard = True
    columns = len(Board)
    ##horizonalWin
    for column in Board:
        for x in column:
            if x == -1:
                fullBoard = False
 
    for i in range(len(Board)): 
        sequentialOnes = 0
        sequentialZeros = 0
        # print("Checking column" + str(i))
        for x in range(len(Board)):
		    #for x in range(len(Board)):
                #print(x)
            
            if Board[x][i] == 0:
                #print("Board["+str(x)+"] ["+str(i)+"]: " +str(Board[x][i]))
                sequentialZeros += 1
                if sequentialOnes != 4:
                    sequentialOnes = 0
            if Board[x][i] == 1:
                #print("Board["+str(x)+"] ["+str(i)+"]: " +str(Board[x][i]))
                sequentialOnes += 1
                if sequentialZeros != 4:
                    sequentialZeros = 0
            if Board[x][i] == -1:
                #print("Board["+str(x)+"] ["+str(i)+"]: " +str(Board[x][i]))
        #print('Ones: '+str(sequentialOnes) +'   zeroes:'+str(sequentialZeros))
        #for c in Board:
            #print(c)
                fullBoard = False
                if sequentialOnes != 4:
                    sequentialOnes = 0
                if sequentialZeros != 4:
                    sequentialZeros = 0 
        # print(str(sequentialZeros) +' '+str(sequentialOnes))
        if sequentialOnes >= 4:
            print("player 1 wins horizontally")
            horizonalWin = True
           ## print(Board[for x in range(len(Board))][i])
            temp = []
 
            for x in range(len(Board)):
                 #for x in c:
                temp.append(Board[x][i])	
            # print(temp)		
            # print("****************************")
            # for c in Board:
                # print(c)
            # print("****************************")
            				
            player1wins += 1
            #Board = reset(Board)
            #fullBoard = True
            #sys.exit()
            return reset(Board)
        if sequentialZeros >= 4:
            print("player 0 wins horizontally")
            horizonalWin = True
            temp = []
 
            for x in range(len(Board)):
                 #for x in c:
                temp.append(Board[x][i])
            print(temp)		
            # print("****************************")
            # for c in Board:
                # print(c)
            # print("****************************")
            	
            player0wins += 1
            #Board = reset(Board)
            #sys.exit()
            return reset(Board)
            #fullBoard = True
       
	##verticalWin
    
    for column in Board:
        sequentialZeros = 0
        sequentialOnes = 0
        for x in column:
            if x == -1:
                fullBoard = False
           
		  
		  
       
			#gamesFinished += 1
        for x in column:
            if x == 0:
       	        sequentialZeros+=1
                sequentialOnes = 0
            if x == 1:
                sequentialOnes+=1
                sequentialZeros = 0

        if sequentialZeros >= 4:
            print("Player0 wins vertically")
            verticalWin = True
            # print(column)
            # print("****************************")
            # for c in Board:
                  # print(c)  
            #sys.exit()
            player0wins += 1
            #gamesFinished += 1
            Board = reset(Board)
            return Board
            #fullBoard = True
        if sequentialOnes >=4:
            print("Player1 wins vertically")
            verticalWin = True
            # print(column)
            # print("****************************")
            # for c in Board:
                # print(c)  
            #sys.exit()
            player1wins += 1
            #gamesFinished += 1
            Board = reset(Board)
            return Board
			#fullBoard = True  
    for x in range(0,6):
        sequentialOnes = 0
        sequentialZeros = 0
        for i in range(0,6):
            
            if (x + 3 <= 6 and i + 3 <= 6):
                if Board[x][i] == 1:
                    if Board[x+1][i+1] == 1:
                        if Board[x+2][i+2] == 1:
                            if Board[x+3][i+3] == 1:
                                sequentialOnes = 4
                               	player1wins += 1
                                # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$player 1 wins diagonally")
                                # for c in Board:
                                    # print(c)
                                #sys.exit()
                                return reset(Board)
            if (x + 3 <= 6 and i +3 <= 6):
                if Board[x][i] == 0:
                    if Board[x+1][i+1] == 0:
                        if Board[x+2][i+2] == 0:
                            if Board[x+3][i+3] == 0:
                                sequentialZeros = 4
                               	player0wins += 1
                                # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$player 0 wins diagonally")
                                # for c in Board:
                                    # print(c)                              
                                #sys.exit()
                                return reset(Board)   
			
            if (x >= 3 and i <= 3):
                # print('here')
                if Board[x][i] == 1:
                    if Board[x-1][i+1] == 1:
                        if Board[x-2][i+2] == 1:
                            if Board[x-3][i+3] == 1:
                                sequentialOnes = 4
                               	player1wins += 1
                                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$player 1 wins diagonally")
                                for c in Board:
                                    print(c)
                               
							   # sys.exit()
                                return reset(Board)		
            if (x >= 3 and i <= 3):
                if Board[x][i] == 0:
                    if Board[x-1][i+1] == 0:
                        if Board[x-2][i+2] == 0:
                            if Board[x-3][i+3] == 0:
                                sequentialZeros = 4
                               	player0wins += 1
                                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$player 0 wins diagonally")
                                for c in Board:
                                    print(c)
                                # sys.exit()
                                return reset(Board)										
    if fullBoard != False:
        # print("Resetting board")
        draws += 1
        sequentialOnes = 0
        sequentialZeros = 0

        Board = reset(Board)
        ##Board = []
        #Board = [[-1 for x in range(columns)] for y in range(columns)]
        #fullBoard = False 
        # for c in Board:
             # print(c)
    # print(sequentialOnes)
    # print(sequentialZeros)
	##diagonalWin
            			
    return Board
def Flip(Board):
    temp = []
    # for c in Board:
        # print(c) 
    # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&FLIPPING&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    for column in Board:
        empties = 0
        tempC = []
        for x in reversed(column):
            if x == -1:
               empties += 1
            else:
               tempC.append(x)
        for x in range(0,empties):
            tempC.append(-1)
        temp.append(tempC)			   
    # for c in temp:
        # print(c)
    return temp
def AddPiece(Board,column,player):
    # print(column)
    c = Board[column]
    #print('adding'+str(c))
    # for x in c:
        # print(str(len(c))+str(x))
        #print(str(i)+' '+str(x))
        ##if x != -1:
    for i in range(0,len(c)):
        #print(str(i) + str(c[i]))
        if c[i] == -1:
            Board[column][i] = player
            #print(Board)
            #return Board
            return
def player0turn(playerTurn):
    #playerTurn = 1
    global Board
    move = randomPlay(Board)
    ##print(move[0])
    ##print(move[1])
    AddPiece(Board,move[1],playerTurn)
    flip = random.random()
    if flip >= 0.67:
        Flip(Board)
    #print(move)
    playerTurn = 1
    Board = checkWin(Board)  
def player1turn(playerTurn):
    global Board
    move = randomPlay(Board)
        #print(move)
    AddPiece(Board,move[1],playerTurn)
    #print('setting playerTurn to 0')
    flip = random.random()
    if flip >= 0.67:
        Flip(Board)
    		
    playerTurn = 0
    Board = checkWin(Board)	
playerArr = ['White','Green']

print(playerArr)
print(playerArr[0])
print(playerArr[1])
print(len(playerArr))

columns = 7
Board = [[-1 for x in range(columns)] for y in range(columns)]

print(Board)
print('\n\n\n\n')
move = randomPlay(Board)
	
print(move)
playerTurn = 0
won = False
gamesFinished = 0
player0wins = 0
player1wins = 0
draws = 0
while not won:
    horizonalWin = False
    verticalWin = False
    diagonalWin = False
    #print(playerTurn)
    if playerTurn == 0:
        player0turn(playerTurn)
        Board = checkWin(Board)
        playerTurn = 1
    if playerTurn == 1:
        #print('playerTurn1')
        player1turn(playerTurn)
        playerTurn = 0
        Board = checkWin(Board)

    # print("*************************************************************************")
    ##print(Board)
    # print('games finished: '+str(gamesFinished)+' '+' p0: '+str(player0wins)+'  p1: '+str(player1wins)+'  draws: '+str(draws)) 
    # for c in Board:
        # print(c)    
    # print("*************************************************************************")
    
    if gamesFinished >= 1000:
        print(gamesFinished)
        print(player0wins)
        print(player1wins)
        
        print(draws)

        sys.exit()
  