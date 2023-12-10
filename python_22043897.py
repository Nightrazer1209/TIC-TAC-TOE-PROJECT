#Student ID: 22043897
#Lim Fong Yew
#CSC1024
#2/12/2022
#tictactoe game

import random

#initial values of boxes in game_board
board =['-','-','-','-','-','-','-','-','-']

#function to design game_board interface using lines
def game_board(board):
    print(" ")
    print(" "+board[0]+ " | " +board[1] +" | " + board[2])
    print("-----------")
    print(" "+board[3]+ " | " +board[4] +" | " + board[5])
    print("-----------")
    print(" "+board[6]+ " | " +board[7] +" | " + board[8])
    return " "

#function to set the pattern to play 
def pattern():
    while True:
        pattern = input ("Select your pattern to be 'O' or 'X': ").upper()
        if pattern == "O":          #prevent lower caps being counted as mistype                  
            pattern_ai = "X"                #choose pattern of the computer after player decide
            break
        elif pattern == "X":
            pattern_ai = "O"
            break
        else:
            print("INVALID INPUT! Please type only 'O' or 'X'.\n")      #while loop to avoid input errors
    return pattern,pattern_ai
            
#design of computer movement after player input
def ai(pattern_ai):
                                       
    player_round = not True                 #when its not the player's round
    while player_round is not True:         
        num_ai=random.randint(1,9)      #randomise computer's input and select one among 9 boxes
        
        if board[num_ai-1] != "O" and board[num_ai-1] != "X":       #computer can only enter a input when the box is not filled with O or X 
            board[num_ai-1] = pattern_ai
            
            #if's to determine rows and cols of the input
            if num_ai in range(1,4):
                row = 1
            elif num_ai in range(4,7):
                row = 2
            elif num_ai in range(7,10):
                row = 3
                
            #since list values differs by 3 in each row, numbers to represent boxes of diff col are added in
            #sequence of 3
            if num_ai in range(1,10,3):
                col = 1
            elif num_ai in range(2,10,3):
                col = 2
            elif num_ai in range(3,10,3):
                col = 3
            player_round = True        #after calculated the row and col, return true value to break loop
            
        else:
            num_ai=random.randint(1,9)      #if randomised number box is filled, number is randomised again until an empty box is found
     
    print("\nComputer's turn: ")
    return game_board(board),str(row),str(col),pattern_ai       #return the game board after computer's move


#design of player function to react according to player's input
def player(pattern_player):
    player_round = True
    while player_round:
        print()
        num = ["1","2","3","4","5","6","7","8","9"]          #to be easier for player, number of 1 ~ 9 is used to represent the boxes instead of 0~8
        choice = input("Select a box between 1 ~ 9 that is not filled: ")
        if choice not in num:
            print("INVALID INPUT! Please select a number between 1 to 9.")     #to eliminate any invalid input, repeat input loop
        else:
            choice = int(choice)         #switch data type to integer only after input is valid, to avoid TypeError that stops the program to run

            #check if box is filled
            if board[choice-1] != "X" and board[choice-1] != "O":
                board[choice-1] = pattern_player
                
                #identify filled box's row and col
                if choice in range(1,4):
                    row = 1
                elif choice in range(4,7):
                    row = 2
                elif choice in range(7,10):
                    row = 3
                if choice in range(1,10,3):
                    col = 1
                elif choice in range(2,10,3):
                    col = 2
                elif choice in range(3,10,3):
                    col = 3
                player_round=False  #break loop
                
            else:
                print("INVALID INPUT! The box is already filled!")        #loop choice input if invalid
            
    print("\nPlayer's turn: ")       
    return game_board(board),str(row),str(col),pattern_player
    
#starting turn 
def game_start():
    print(game_board(board))
    file = open("logfile_22043897.txt","a")
    file.write("--Start of Round "+str(round_num)+"--\n\n")       #game number is written before game start
    while True:
        ask = input("To start the game, decide if you want to go first. Yes(Y)/No(N): ")  #ask player intention to go first or second
        if ask.lower() == "y":
            player_round = True
            break
        elif ask.lower() == "n":
            player_round = False
            break
        else:
            print("INVALID INPUT! Please type only 'y' or 'n'.\n")
            print()  
    return player_round     #return player_round variable which is then transferred to game_run function


#function to switch turns between player and computer
def game_run(turn):
    symbol = pattern()  #call pattern function after game_start() function
    run =  True         #variable to indicate that game is running
    move = 0            #variable to track number of movements in the game
    
    while run:  
        if turn == False:       #when turn is false, it's computer's turn. Thus, ai() function is called
            row_col = ai(symbol[1])
            #after computer input, turn is switched to player, and move number is increased by one
            turn = True
            move += 1
            file = open("logfile_22043897.txt","a")      #log file is appended after retrieving row and col values from ai(board) function
            file.write(str(move)+",C,"+row_col[1]+","+row_col[2]+","+symbol[1]+"\n")    #retrieve value from ai() function to the log file
            
        elif turn == True:      #when turn is true, it's player's turn. Thus, player(board) function is called
            row_col = player(symbol[0])
            turn = False
            #after player's input, turn is switched to computer(turn = False), and move number is increased by one
            move += 1
            file = open("logfile_22043897.txt","a")     #log file is appended after retrieving row and col values from player(board) function
            file.write(str(move)+",H,"+row_col[1]+","+row_col[2]+","+symbol[0]+"\n")      #retrieve value from ai() function to the log file


        #if 3 boxes are aligned with the same values horizontally, vertically or diagonally, and the value is not "-", there is a winner
        if\
        (board[0] == board[1] == board[2] != "-") or\
        (board[3] == board[4] == board[5] != "-") or\
        (board[6] == board[7] == board[8] != "-") or\
        (board[0] == board[3] == board[6] != "-") or\
        (board[1] == board[4] == board[7] != "-") or\
        (board[2] == board[5] == board[8] != "-") or\
        (board[0] == board[4] == board[8] != "-") or\
        (board[2] == board[4] == board[6] != "-"):
            run = False                     #break loop when found a winner
            print("\nThe game is over!")
            if turn == False:
                print("Player wins!")
                file = open("logfile_22043897.txt","a")
                file.write("Winner: Human\n")   #write winner in log file
            else:
                print("Computer wins!")
                file = open("logfile_22043897.txt","a")
                file.write("Winner: Computer\n")    #write winner in log file
                
        #tie happens when all boxes are filled and no winner conditions is fulfilled
        elif "-" not in board:
            print("\nGame over! It's a tie!")
            file = open("logfile_22043897.txt","a")
            file.write("Winner: Tie\n")
            break        #break indicates end of the game
    file.write("\n--End of Round "+str(round_num)+"--\n\n")
    file.close()

#instructions are given to player before starting the game
print('''
Welcome to the Amazing Tic Tac Toe Game!

Game Rule:
1.  To win this game, the player must obtain three identical inputs in the
    game board in the same row, column or diagonally.
2.  The game board is divided to 9 boxes, with numbers from 1~9 representing
    each one of them, as shown as below:
   
             1 | 2 | 3
           -------------
             4 | 5 | 6
           -------------
             7 | 8 | 9
             
3.  The player can select to start first or not.
4.  When it's the player's turn, he/she can select one of the 9 boxes which
    is not filled with "O" or "X", specifically only the boxes with "-".
5.  All can only be filled ONCE. 
6.  After a valid player input, it's the computer's turn and it will draw
    its pattern on the other box which is not filled.
7.  The switch between player and computer continues until a winner emerges or
    all boxes are filled, which results in a tie.
9.  After that the round ends, the player can choose if he/she wants to start
    a new round.
   
Note:
This game is case sensitive and an error message will pop up if the player's
input is invalid. In that case, he/she will have to reenter the value again.


That's all. Have fun. :D


Game Board:''')

file = open("logfile_22043897.txt","a")
file.write('''
New game
---------
''')
file.close()
round_num = 1
game_run(game_start())
game = True

#check player's intention to replay
while game:   
    replay = input("\nDo you want to play again? Yes(Y)/No(N): ")
    if replay.lower() == "n":   #program terminated if no replay intention
        print("Game terminated. Thank you for playing!")
        game = False
    elif replay.lower() == "y":
        print("\nNew round: ")
        board =['-','-','-','-','-','-','-','-','-']
        round_num += 1            #game number increases by one after each game for clearer records
        game_run(game_start())   #if player choose to replay, game is restarted by calling the game_run function again
    else:
        print("INVALID INPUT! Please type only 'y' or 'n'.")   #eliminate invalid inputs

while game is False:
    keep = input("\nKeep game records in log file? Yes(Y)/No(N): ")    #user intention to save game records after don't want to play anymore
    if keep.lower() == "n":
        file = open("logfile_22043897.txt","w")    #write to file to make the file blank
        file.close()
        print("Game records deleted.")
        break
    elif keep.lower() == "y":
        print("Game records saved.")    #no actions needed to save as data are saved beforehand using functions
        break
    else:
        print("INVALID INPUT! Please type only 'y' or 'n'.")    #elimate invalid inputs
    

    


   

