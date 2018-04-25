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

def aiMove(Board):
    return Board

    
def reset(Board):
    global gamesFinished
    global draws
    
    gamesFinished += 1
    Board = [[-1 for x in range(columns)] for y in range(columns)]
    return Board
def checkWin(Board):

    global gamesFinished
    global player0wins
    global player1wins
    global draws
    fullBoard = True
    columns = len(Board)
  
    for column in Board:
        for x in column:
            if x == -1:
                fullBoard = False
   ##horizonalWin
    for i in range(len(Board)): 
        sequentialOnes = 0
        sequentialZeros = 0
       
        for x in range(len(Board)):
		 
            
            if Board[x][i] == 0:
             
                sequentialZeros += 1
                if sequentialOnes != 4:
                    sequentialOnes = 0
            if Board[x][i] == 1:
               
                sequentialOnes += 1
                if sequentialZeros != 4:
                    sequentialZeros = 0
            if Board[x][i] == -1:
                if(sequentialZeros != 4):
                    sequentialZeros = 0
                if(sequentialOnes != 4):
                    sequentialOnes = 0
              
                fullBoard = False
            
       
        if sequentialOnes >= 4:
            print("player 1 wins horizontally")
            horizonalWin = True
          
            temp = []
            print(i)
            for x in range(len(Board)):
             
                temp.append(Board[x][i])	
          
            printBoard(Board)
				
            player1wins += 1
           
            return reset(Board)
        if sequentialZeros >= 4:
            print("player 0 wins horizontally")
            horizonalWin = True
            temp = []
            print(i) 
            for x in range(len(Board)):
           
                temp.append(Board[x][i])
      
            printBoard(Board)
         
            player0wins += 1
           
            return reset(Board)
          
       
	##verticalWin
    
    for column in Board:
        sequentialZeros = 0
        sequentialOnes = 0
		  
		
        for x in column:
            if x == 0:
       	        sequentialZeros+=1
                if(sequentialOnes != 4):
                    sequentialOnes = 0
            if x == 1:
                sequentialOnes+=1
                
                if(sequentialZeros != 4):
                    sequentialZeros = 0

        if sequentialZeros >= 4:
            print("Player0 wins vertically")
            printBoard(Board)
            verticalWin = True
          
            player0wins += 1
    
            Board = reset(Board)
            return Board
    
        if sequentialOnes >=4:
            print("Player1 wins vertically")
            printBoard(Board)
            verticalWin = True
        
            player1wins += 1
    
            Board = reset(Board)
            return Board
		
##diagonalWin
    for x in range(0,7):
        sequentialOnes = 0
        sequentialZeros = 0
    
        for i in range(0,7):
            
            if (x + 3 <= 6 and i + 3 <= 6):
                if Board[x][i] == 1:
                    if Board[x+1][i+1] == 1:
                        if Board[x+2][i+2] == 1:
                            if Board[x+3][i+3] == 1:
                                sequentialOnes = 4
                               	player1wins += 1
                               
                                printBoard(Board)
                              
                                return reset(Board)
            if (x + 3 <= 6 and i +3 <= 6):
                if Board[x][i] == 0:
                    if Board[x+1][i+1] == 0:
                        if Board[x+2][i+2] == 0:
                            if Board[x+3][i+3] == 0:
                                sequentialZeros = 4
                               	player0wins += 1
                            
                                printBoard(Board)
                                  
                                return reset(Board)   
			
            if (x >= 3 and i <= 3):
        
                if Board[x][i] == 1:
                    if Board[x-1][i+1] == 1:
                        if Board[x-2][i+2] == 1:
                            if Board[x-3][i+3] == 1:
                                sequentialOnes = 4
                               	player1wins += 1
                                print("player 1 wins diagonally")
                                printBoard(Board)
                               
							  
                                return reset(Board)		
            if (x >= 3 and i <= 3):
                if Board[x][i] == 0:
                    if Board[x-1][i+1] == 0:
                        if Board[x-2][i+2] == 0:
                            if Board[x-3][i+3] == 0:
                                sequentialZeros = 4
                               	player0wins += 1
                                print("player 0 wins diagonally")
                                printBoard(Board)
                            
                                return reset(Board)										
    if fullBoard != False:

        draws += 1
        sequentialOnes = 0
        sequentialZeros = 0

        Board = reset(Board)
       
	
            			
    return Board
def Flip(Board):
    temp = []

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

    return temp
def AddPiece(Board,column,player):

    c = Board[column]
  
    for i in range(0,len(c)):
    
        if c[i] == -1:
            Board[column][i] = player
            return Board
			
    return Board
def player0turn(playerTurn):
    global Board
    move = randomPlay(Board)

    Board = AddPiece(Board,move[1],playerTurn)
    flip = random.random()
    if flip >= 0.67:
        Flip(Board)
    playerTurn = 1
    return Board
    
def player1turn(playerTurn):
    global Board
    move = randomPlay(Board)
   
    Board = AddPiece(Board,move[1],playerTurn)

    flip = random.random()
    if flip >= 0.67:
        Flip(Board)
    		
    playerTurn = 0
    return Board
def printBoard(Board):
    for i in range(len(Board)-1,-1,-1):
       
        b0 = Board[0][i]
        b1 = Board[1][i]
        b2 = Board[2][i]
        b3 = Board[3][i]
        b4 = Board[4][i]
        b5 = Board[5][i]
        b6 = Board[6][i]
        if b0 == 0 or b0 == 1:
            b0 = " "+str(b0)
        if b1 == 0 or b1 == 1:
            b1 = " "+str(b1)
        if b2 == 0 or b2 == 1:
            b2 = " "+str(b2)
        if b3 == 0 or b3 == 1:
            b3 = " "+str(b3)
        if b4 == 0 or b4 == 1:
            b4 = " "+str(b4)
        if b5 == 0 or b5 == 1:
            b5 = " "+str(b5)
        if b6 == 0 or b6 == 1:
            b6 = " "+str(b6)
			
        b0 = str(b0)
        b1 = str(b1)	
        b2 = str(b2)
        b3 = str(b3)
        b4 = str(b4)
        b5 = str(b5)
        b6 = str(b6)
        
        print(b0+" | "+b1 +" | "+b2 +" | "+b3 +" | "+b4 +" | "+b5+" | "+b6)
        print("--------------------------------")

playerArr = ['White','Green']

columns = 7
Board = [[-1 for x in range(columns)] for y in range(columns)]

playerTurn = 0
won = False
gamesFinished = 0
player0wins = 0
player1wins = 0
draws = 0

RandomVsRandom = False
playerVsAi = False
playerVsRandom = False
playerVsPlayer = False

ui = input("Enter which option you want to play: (1-4) \n1. Random Vs Random \n2. Player Vs Random \n3.Player Vs Ai \n4. Player Vs Player \n")

ui = int(ui)
if ui == 1:
    #print("True")
    RandomVsRandom = True


playerTurn = input("Which player will move first? ")
playerTurn = int(playerTurn)
while not won:
    horizonalWin = False
    verticalWin = False
    diagonalWin = False
    #print(playerTurn)
    if RandomVsRandom == True:
        #print("true")
        if playerTurn == 0:
            Board = player0turn(playerTurn)
            Board = checkWin(Board)
            playerTurn = 1
        if playerTurn == 1:
        #print('playerTurn1')
            Board = player1turn(playerTurn)
            playerTurn = 0
            Board = checkWin(Board)

        if gamesFinished >= 10000:
            print(gamesFinished)
            print(str(playerArr[0])+" won: "+str(player0wins))
            print(str(playerArr[1])+" won: "+str(player1wins))
        
            print("Draws: "+str(draws))

            sys.exit()
  