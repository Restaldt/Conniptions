import random
import numpy as np
from time import sleep
import sys
def checkHueristic(BoardSet):
    
    #((0,c,0),AddPiece(Board,c,1))
    temp  = []
    print("*******************************")
    for b in BoardSet:
        oneH = 0
        zeroH = 0
        sequentialZeros = 0
        sequentialOnes = 0
        col = -1
        # print(b[0])
        # print(b[1])
        #printBoard(b)
        ##verticalH
        for c in b[1]:
            sequentialZeros = 0
            sequentialOnes = 0
            for x in c:
                if x == 0:
                    sequentialZeros += 1
                    if sequentialOnes > oneH:
                        oneH = sequentialOnes
                    sequentialOnes = 0
                if x == 1:
                    sequentialOnes += 1
                    if sequentialZeros > zeroH:
                        zeroH = sequentialZeros
                    sequentialZeros = 0
                if x == -1:
                    if sequentialOnes > oneH:
                        oneH = sequentialOnes
                    if sequentialZeros > zeroH:
                        zeroH = sequentialZeros
                    sequentialOnes = 0
                    sequentialZeros = 0

        #horizonalH
        # tempHorizontalHs = []
        #'''
        for i in range(0,len(b[1])):
			#v = 0 #placeholder code this does nothing   
            sequentialOnes = 0
            sequentialZeros = 0
            for x in range(0,len(b[1])):
                if b[1][x][i] == 0:
                    sequentialZeros += 1
                    if sequentialOnes > oneH:
                        oneH = sequentialOnes
						
                    sequentialOnes = 0
                if b[1][x][i] == 1:
                    sequentialOnes += 1
                    if sequentialZeros > zeroH:
                        zeroH = sequentialZeros
                    sequentialZeros = 0
                if b[1][x][i] == -1:
                    if sequentialOnes > oneH:
                        oneH = sequentialOnes
                    if sequentialZeros > zeroH:
                        zeroH = sequentialZeros
                    sequentialOnes = 0
                    sequentialZeros = 0
        # print(tempHorizontalHs)
        #'''
        ##diagonalH
        for x in range(0,len(b[1])):
            sequentialOnes = 0
            sequentialZeros = 0
            for i in range(0,len(b[1])):
                #'''
                if (x + 3 <= 6 and i + 3 <= 6):
                    if b[1][x][i] == 1:
                        sequentialOnes += 1
                        if sequentialZeros > zeroH:
                            zeroH = sequentialZeros

                        sequentialZeros = 0
                        if b[1][x+1][i+1] == 1:
                            sequentialOnes += 1
                            if sequentialZeros > zeroH:
                                zeroH = sequentialZeros
                            sequentialZeros = 0
                            if b[1][x+2][i+2] == 1:
                                sequentialOnes += 1
                                if sequentialZeros > zeroH:
                                    zeroH = sequentialZeros
                                sequentialZeros = 0
                                if b[1][x+3][i+3] == 1:
                                    sequentialOnes += 1
                                    #player1wins += 1
                                    if sequentialZeros > zeroH:
                                        zeroH = sequentialZeros
                                    sequentialZeros = 0
                                    #print(b[1])
                                  
                                    #return reset(b[1])
                                if b[1][x+3][i+3]== -1 or b[1][x+3][i+3] == 0:
                                    if sequentialOnes > oneH:
                                        oneH = sequentialOnes
                                    sequentialOnes = 0
                            if b[1][x+2][i+2] == -1 or b[1][x+3][i+3] == 0:
                                if sequentialOnes > oneH:
                                    oneH = sequentialOnes
                                sequentialOnes = 0
                        if b[1][x+1][i+1] == -1 or b[1][x+3][i+3] == 0:
                            if sequentialOnes > oneH:
                                oneH = sequentialOnes
                            sequentialOnes = 0


                    if b[1][x][i] == 0:
                        sequentialZeros += 1
                        if sequentialOnes > oneH:
                            oneH = sequentialOnes
                        sequentialOnes = 0
                        if b[1][x+1][i+1] == 0:
                            sequentialZeros += 1
                            if sequentialOnes > oneH:
                                oneH = sequentialOnes
                            sequentialOnes = 0
                            if b[1][x+2][i+2] == 0:
                                sequentialZeros += 1
                                if sequentialOnes > oneH:
                                    oneH = sequentialOnes
                                sequentialOnes = 0
                                if b[1][x+3][i+3] == 0:
                                    sequentialZeros += 1
                                    #player0wins += 1
                                    if sequentialOnes > oneH:
                                        oneH = sequentialOnes
                                    sequentialOnes = 0
                                if b[1][x+3][i+3]== -1 or b[1][x+3][i+3] == 1:
                                    if sequentialZeros > zeroH:
                                        zeroH = sequentialZeros
                                    sequentialZeros = 0
                            if b[1][x+2][i+2] == -1 or b[1][x+3][i+3] == 1:
                                if sequentialZeros > zeroH:
                                    zeroH = sequentialZeros
                                sequentialZeros = 0
                        if b[1][x+1][i+1] == -1 or b[1][x+3][i+3] == 1:
                            if sequentialZeros > zeroH:
                                zeroH = sequentialZeros
                            sequentialZeros = 0
                    #'''
                if (x >= 3 and i <= 3):
                    if b[1][x][i] == 1:
                        sequentialOnes += 1
                        if sequentialZeros > zeroH:
                            zeroH = sequentialZeros
                        sequentialZeros = 0
                        if b[1][x-1][i+1] == 1:
                            sequentialOnes += 1
                            if sequentialZeros > zeroH:
                                zeroH = sequentialZeros
                            sequentialZeros = 0
                            if b[1][x-2][i+2] == 1:
                                sequentialOnes += 1
                                if sequentialZeros > zeroH:
                                    zeroH = sequentialZeros
                                sequentialZeros = 0
                                if b[1][x-3][i+3] == 1:
                                    sequentialOnes += 1
                                    if sequentialZeros > zeroH:
                                        zeroH = sequentialZeros
                                    sequentialZeros = 0
                                else:
                                    if sequentialOnes > oneH:
                                        oneH = sequentialOnes
                                    sequentialOnes = 0
                            else: 
                                if sequentialOnes > oneH:
                                    oneH = sequentialOnes
                                sequentialOnes = 0
                        else:
                            if sequentialOnes > oneH:
                                oneH = sequentialOnes
                            sequentialOnes = 0  
                if (x >= 3 and i <= 3):
                    if b[1][x][i] == 0:
                        sequentialZeros += 1
                        if sequentialOnes > oneH:
                            oneH = sequentialOnes
                        sequentialOnes = 0
                        if b[1][x-1][i+1] == 0:
                            sequentialZeros += 1
                            if sequentialOnes > oneH:
                                oneH = sequentialOnes
                            sequentialOnes = 0
                            if b[1][x-2][i+2] == 0:
                                sequentialZeros += 1
                                if sequentialOnes > oneH:
                                    oneH = sequentialOnes
                                sequentialOnes = 0
                                if b[1][x-3][i+3] == 0:
                                    sequentialZeros += 1
                                    if sequentialOnes > oneH:
                                        oneH = sequentialOnes
                                    sequentialOnes = 0
                                else:
                                    if sequentialZeros > zeroH:
                                        zeroH = sequentialZeros
                                    sequentialZeros = 0
                            else: 
                                if sequentialZeros > zeroH:
                                    zeroH = sequentialZeros
                                sequentialZeros = 0
                        else:
                            if sequentialZeros > zeroH:
                                zeroH = sequentialZeros
                            sequentialZeros = 0
                    #'''
        #print(str(oneH)+" "+str(zeroH))
        # for c in b:
            # print(c)
       
        #printBoard(b[1])
        temp.append((b,oneH,zeroH))
        
		#print(temp)
    print("*******************************")
    return temp
def randomPlay(Board):

    #print(Board)
    move1 = random.random()
    move2 = random.randint(0,6)
    move = (move1,move2)
    return move

def aiMove(Board):
    ##checkHueristic(Board)
    moveSet = []
    currentBoard = Flip(Board)
	
    # print("................................................")
    # printBoard(Board)
    # print("CB................................................")
    #printBoard(currentBoard)
    global flips

    for c in range(0,len(Board)):
        #for x in range(0,len(Board)):
            #if Board[x][i] == -1:
        moveSet.append(((0,c,0),AddPiece(Board,c,1)))
        Board = Flip(currentBoard)
        
        #tb = Flip(Board)
        moveSet.append(((1,c,0),AddPiece(Flip(Board),c,1)))
        Board = Flip(currentBoard)

        moveSet.append(((0,c,1),Flip(AddPiece(Board,c,1))))
        Board = Flip(currentBoard)

 
        #printBoard(currentBoard)
    
    # Hueristics = checkHueristic(moveSet)
    # print("................................................")
    # for b in moveSet:
        # printBoard(b)
    #Board = Flip(currentBoard)
    # print("NewBoard................................................")
    # printBoard(Board)
    # print("CB................................................")
    # printBoard(currentBoard)
    tuples = checkHueristic(moveSet)
    #tuples = sorted(tuples, key=lambda x: x[1])

    for i in tuples:
        tuplesOne = tuples.sort(key=lambda x: x[1])
        tuplesZero = tuples.sort(key=lambda x: x[2])

    print(tuplesOne)
    print(tuplesZero)


    print("Length of tuples: "+str(len(tuples)))
    maxH = -10
    bestMove = ()
    for tuple in tuples:
        #print(str(tuple[1])+" :oneH zeroH: "+str(tuple[2]))
        #print("Move: "+str(tuple[0][0]))
        #printBoard(tuple[0][1])
        #calculatedH = tuple[1] - tuple[2]
        calculatedH = tuple[1]

        if calculatedH > maxH:
            maxH = calculatedH
            bestMove = tuple

    print("Move: "+ str(bestMove[0][0]))
    if bestMove[0][0][0] == 1:
        flips += 1
    if bestMove[0][0][2] == 1:
        flips += 1
    print(flips)
    return bestMove[0][1]

    
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
        print(column)
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
flips = 0
player0wins = 0
player1wins = 0
draws = 0

RandomVsRandom = False
playerVsAi = False
RandomVsAi = False

ui = input("Enter which option you want to play: (1-3) \n1. Random Vs Random \n2. Ai Vs Random \n3.Player Vs Ai \n")

ui = int(ui)
if ui == 1:
    #print("True")
    RandomVsRandom = True
if ui == 2:
    RandomVsAi = True
if ui == 3:
    playerVsAi = True


playerTurn = input("Which player will move first? ")
playerTurn = int(playerTurn)
firstTurn = True
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

        if gamesFinished >= 5000:
            print(gamesFinished)
            print(str(playerArr[0])+" won: "+str(player0wins))
            print(str(playerArr[1])+" won: "+str(player1wins))
        
            print("Draws: "+str(draws))

            sys.exit()
    if RandomVsAi == True:
 
        #print("true")
        if playerTurn == 0:
            Board = player0turn(playerTurn)
         
            playerTurn = 1 
            Board = checkWin(Board)
        if playerTurn == 1:
           #print('playerTurn1')
            Board = aiMove(Board)
            playerTurn = 0
            Board = checkWin(Board)

        if gamesFinished >= 100:
            print(gamesFinished)
            print(str(playerArr[0])+" won: "+str(player0wins))
            print(str(playerArr[1])+" won: "+str(player1wins))
        
            print("Draws: "+str(draws))
            sys.exit()     
    if playerVsAi == True:

        if playerTurn == 0:
            flipBefore = input('Enter 1 or 0 for flipBefore:')
            chooseColumn = input('Enter the column where you would place your piece:')
            chooseColumn = int(chooseColumn)
            flipAfter= input('Enter 1 or 0 for FlipAfter):')
            #colPlayer = play
            #Board = 
            print(chooseColumn)
            if flipBefore == 1:
                Board = Flip(Board)
            Board = AddPiece(Board, chooseColumn, playerTurn)
            if flipAfter == 1:
                Board = Flip(Board)

            playerTurn = 1 
            Board = checkWin(Board)
            printBoard(Board)
            if gamesFinished >= 1:
                print("Player 0 Wins")
                sys.exit()
        if playerTurn == 1:
           #print('playerTurn1')
            if firstTurn == True:
                columnPlayed = randomPlay(Board)
                print("Move: "+"(0,"+str(columnPlayed[1])+",0)")
                Board = AddPiece(Board,columnPlayed[1],playerTurn)
                printBoard(Board)
                playerTurn = 0
                firstTurn = False
            else: 
                Board = aiMove(Board)
                playerTurn = 0
                Board = checkWin(Board)
                printBoard(Board)
                if gamesFinished >= 1:
                    print("AI wins")
                    sys.exit()























				