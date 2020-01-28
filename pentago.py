import numpy as np
from random import randint

#initialize new board
def reset_board(board):
    board = np.zeros((6,6), dtype=int)
    return board

#Extra & Supporting Function Initialization
def welcome():
    print("""
============================================================
  _____           _                     _____       
 |  __ \         | |                   |  __ \      
 | |__) |__ _ __ | |_ __ _  __ _  ___  | |__) |   _ 
 |  ___/ _ \ '_ \| __/ _` |/ _` |/ _ \ |  ___/ | | |
 | |  |  __/ | | | || (_| | (_| | (_) || |   | |_| |
 |_|   \___|_| |_|\__\__,_|\__, |\___(_)_|    \__, |
 By: Dyah Ayu Nurun Nafisah __/ |              __/ |
 Matric: U1940940L         |___/              |___/ 
============================================================
    """)

#Select Level and repeat if false input
def select_level():
    level = input('\n' +"1. Easy"+ '\n' +"2. Medium"+ '\n' +"3. Hard" +  '\n'+"4. Super Hard"+ '\n' +'\n' + "Select the level of the computer:")
    while not(level == "1" or level == "2" or level == "3" or level == "4"):
        level = input('Choose 1, 2 ,3 or 4!')
    
    print() 
    return level


#Select game/computer mode
def select_computer_mode():
    computer_option = input("Do you want to play with computer? 'Y' or 'N':")
    while not (computer_option == 'Y' or computer_option == 'N'):
        computer_option = input('"Y" or "N"?')
    return (True if computer_option == 'Y' else False)

#function to get cleaned input
def cleaned_input(input_question, error_massage, start, end):
    while True:
        value = input(input_question)
        try:
           value = int(value)
        except ValueError:
           print ("\n"+error_massage)
           continue
        
        #condition to end the game
        if value == 9: 
            return value
        
        #condition for valid input
        if start <= value <= end:
            return value
            break
        else:
           print ("\n"+error_massage)

#Player Move
def player_move(board,turn):
    valid_move = False
    
    print(board,"\n")
    
    print("Now is player ", turn, " turn")
    print("Press 9 to exit the game at any time")
    #Run until get valid move 
    while not valid_move:
        row = cleaned_input('type the row:','Enter valid number between 0 and 5, please',0,5)
        col = cleaned_input('type the column:','Enter valid number between 0 and 5, please',0,5)
        rot = cleaned_input('type the rotation:','Enter valid number between 1 and 8, please',1,8)
        
        #check user to exit the game
        if row==9 or col==9 or rot==9:
            #return True to end game and current rotation
            return 1, rot 
        
        
        #check valid move then break the while loop
        if check_move(board, row, col):
            valid_move = True
            print("Accepted move applied:", row, col, rot, "\n")
        
        #not valid move, ask user to enter valid move
        else:
            print("its not a valid move, please try another move")
            continue
    
    #apply move
    apply_move(board, turn, row, col, rot)
    #return False to continue game and current rotation
    return 0, rot
    #print(board, "debugging only, please delete")  #delete after finished debugging


#Main Function Initialization

#Function to display the board
def display_board(board):
    print(board)

#Check whether the move in valid or not
def check_move(board, row, col):
    if board[row,col] == 0:
        return True
    else:
        return False

#Apply move to the game board
def apply_move(board, turn, row, col, rot):
    board[row,col] = turn
    board = rotation(board, rot)
    return board 

#Apply computer move to the game board
def computer_move(board, turn, level):
    
    row = col = rot = 0

    # Easy level, just pick a random number for the row, column, and rotation
    if level == 1:
        return computer_easy(board, turn)
        
    # Medium Level
    if level == 2:
        return computer_medium(board, turn)
        
    # Hard Level
    if level == 3:
        row, col, rot, score = computer_hard(board, turn)
        return row, col, rot
    
    # Super Hard Level
    if level == 4:
        row, col, rot = computer_super_hard(board, turn)
        return row, col, rot


#################################################################################################
#Main function of the game
def menu(): 
    
    #initialize new board
    board = np.zeros((6,6), dtype=int)
    
    #check user input for alone or vs computer
    is_with_computer = select_computer_mode()
    end_game = 0
    win_game = 0
    row = col = rot = 0
    
    turn = randint(1, 2) #player 1 or player 2 playing
    
    #select level for multiplier game and continue flow for multiplayer game
    if is_with_computer:
        level = int(select_level())
        
        #start the game
        print("Okay, new game started at level", level)
        reset_board(board) #Reset the main board
        
        while not end_game:
            
            #player 1 turn
            if turn == 1:
                end_game, rot = player_move(board,turn)
                win_game = check_victory(board, rot)

                turn = 2  #change player to computer
            
                #end game if user choose to end or someone win
                end_game = end_game or win_game
                
                if end_game: break
        
        
            #player 2 (computer) turn
            if turn == 2:
                #get the move from computer move function
                print('Computer turn')
                row, col, rot = computer_move(board, turn, level)
                apply_move(board, turn, row, col, rot)
                win_game = check_victory(board, rot)
                
                turn = 1  #change player to player 1
            
                #end game if user choose to end or someone win
                end_game = end_game or win_game
                
                if end_game: break
            
    
    #select level for cpu bot and continue flow for multiplayer game
    else: 
        print("\n","Okay, let the game begin","\n")
        reset_board(board) #Reset the main board
        
        
        while not end_game:
            end_game, rot = player_move(board,turn)
            win_game = check_victory(board, rot)

            turn = 2 if turn == 1 else 1 #change player  
            
            #end game if user choose to end or someone win
            end_game = end_game or win_game
            
            
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
    
    
    
    #print / announce the winnner of the game
    if win_game == 1:
        display_board(board)
        print("Congratulation Player 1 Win!")
    elif win_game == 2:
        display_board(board) 
        print("Congratulation Player 2 Win!")
    else:
        display_board(board)
        print("Congratulation, it's a draw, at least no one lose!")
                
    
    
    print("\n","---o0o------You've finished the game, See you later!-----o0o---") 
            
##########################################################################################################3

# Rotation function
def rotation(board, rot):
    if rot == 1:
        board[0:3,3:] = np.rot90(board[0:3,3:], k=1, axes=(1,0))
    elif rot == 2:
        board[0:3,3:] = np.rot90(board[0:3,3:])
    elif rot == 3:
        board[3:,3:] = np.rot90(board[3:,3:], k=1, axes=(1,0))
    elif rot == 4:
        board[3:,3:] = np.rot90(board[3:,3:])
    elif rot == 5:
        board[3:,0:3] = np.rot90(board[3:,0:3], k=1, axes=(1,0))
    elif rot == 6:
        board[3:,0:3] = np.rot90(board[3:,0:3])
    elif rot == 7:
        board[0:3,0:3] = np.rot90(board[0:3,0:3], k=1, axes=(1,0))
    elif rot == 8:
        board[0:3,0:3] = np.rot90(board[0:3,0:3])
    return board

def initial_rotation(rot):
    if rot % 2 == 0:
        rot_in = 1 * rot - 1
    elif rot % 2 == 1:
        rot_in = 1 * rot + 1
    return rot_in

# Winning Checking Block

# Possible position to win the game, for both player 1 and player 2

def player1_win(board):
    if any([(board[0, 0:5] == 1).all(),
            (board[0, 1:] == 1).all(),
            (board[1, 0:5] == 1).all(),
            (board[1, 1:] == 1).all(),
            (board[2, 0:5] == 1).all(),
            (board[2, 1:] == 1).all(),
            (board[3, 0:5] == 1).all(),
            (board[3, 1:] == 1).all(),
            (board[4, 0:5] == 1).all(),
            (board[4, 1:] == 1).all(),
            (board[5, 0:5] == 1).all(),
            (board[5, 1:] == 1).all(),
            (board[0:5, 0] == 1).all(),
            (board[1:, 0] == 1).all(),
            (board[0:5, 1] == 1).all(),
            (board[1:, 1] == 1).all(),
            (board[0:5, 2] == 1).all(),
            (board[1:, 2] == 1).all(),
            (board[0:5, 3] == 1).all(),
            (board[1:, 3] == 1).all(),
            (board[0:5, 4] == 1).all(),
            (board[1:, 4] == 1).all(),
            (board[0:5, 5] == 1).all(),
            (board[1:5, 5] == 1).all(),
            (board[0,0]==1)&(board[1,1]==1)&(board[2,2]==1)&(board[3,3]==1)&(board[4,4]==1),
            (board[1,1]==1)&(board[2,2]==1)&(board[3,3]==1)&(board[4,4]==1)&(board[5,5]==1),
            (board[0,1]==1)&(board[1,2]==1)&(board[2,3]==1)&(board[3,4]==1)&(board[4,5]==1),
            (board[1,0]==1)&(board[2,1]==1)&(board[3,2]==1)&(board[4,3]==1)&(board[5,4]==1),
            (board[0,5]==1)&(board[1,4]==1)&(board[2,3]==1)&(board[3,2]==1)&(board[4,1]==1),
            (board[1,4]==1)&(board[2,3]==1)&(board[3,2]==1)&(board[4,1]==1)&(board[5,0]==1),
            (board[0,4]==1)&(board[1,3]==1)&(board[2,2]==1)&(board[3,1]==1)&(board[4,0]==1),
            (board[1,5]==1)&(board[2,4]==1)&(board[3,3]==1)&(board[4,2]==1)&(board[5,1]==1)]):
        return True
    else:
        return False

def player2_win(board):
    if any([(board[0, 0:5] == 2).all(),
            (board[0, 1:] == 2).all(),
            (board[1, 0:5] == 2).all(),
            (board[1, 1:] == 2).all(),
            (board[2, 0:5] == 2).all(),
            (board[2, 1:] == 2).all(),
            (board[3, 0:5] == 2).all(),
            (board[3, 1:] == 2).all(),
            (board[4, 0:5] == 2).all(),
            (board[4, 1:] == 2).all(),
            (board[5, 0:5] == 2).all(),
            (board[5, 1:] == 2).all(),
            (board[0:5, 0] == 2).all(),
            (board[1:, 0] == 2).all(),
            (board[0:5, 1] == 2).all(),
            (board[1:, 1] == 2).all(),
            (board[0:5, 2] == 2).all(),
            (board[1:, 2] == 2).all(),
            (board[0:5, 3] == 2).all(),
            (board[1:, 3] == 2).all(),
            (board[0:5, 4] == 2).all(),
            (board[1:, 4] == 2).all(),
            (board[0:5, 5] == 2).all(),
            (board[1:5, 5] == 2).all(),
            (board[0,0]==2)&(board[1,1]==2)&(board[2,2]==2)&(board[3,3]==2)&(board[4,4]==1),
            (board[1,1]==2)&(board[2,2]==2)&(board[3,3]==2)&(board[4,4]==2)&(board[5,5]==1),
            (board[0,1]==2)&(board[1,2]==2)&(board[2,3]==2)&(board[3,4]==2)&(board[4,5]==1),
            (board[1,0]==2)&(board[2,1]==2)&(board[3,2]==2)&(board[4,3]==2)&(board[5,4]==1),
            (board[0,5]==2)&(board[1,4]==2)&(board[2,3]==2)&(board[3,2]==2)&(board[4,1]==1),
            (board[1,4]==2)&(board[2,3]==2)&(board[3,2]==2)&(board[4,1]==2)&(board[5,0]==1),
            (board[0,4]==2)&(board[1,3]==2)&(board[2,2]==2)&(board[3,1]==2)&(board[4,0]==1),
            (board[1,5]==2)&(board[2,4]==2)&(board[3,3]==2)&(board[4,2]==2)&(board[5,1]==1)]):
        return True
    else:
        return False

# Check victory of the player, return 1 if player 1 wins, 2 if player 2 wins, 3 if draw, 0 if no one wins
def check_victory(board, rot):
    initial_board = rotation(1 * board, initial_rotation(rot))

    if (player1_win(initial_board)==True) and (player2_win(initial_board)==False):
        return 1
    elif (player1_win(initial_board)==False) and (player2_win(initial_board)==True):
        return 2
    elif (player1_win(initial_board)==True) and (player2_win(initial_board)==True):
        return 3
    else:
        return 0

    check_board = 1 * board
    if (player1_win(check_board)==True) and (player2_win(check_board)==False):
        return 1
    elif (player1_win(check_board)==False) and (player2_win(check_board)==True):
        return 2
    elif (player1_win(check_board)==True) and (player2_win(check_board)==True):
        return 3
    else:
        return 0

#scorring system for the current configuration, help for hard mode game

def scoring(array, turn):
    a = array


    #array of element in diagonal
    ac = np.array([[a[0,0],a[1,1],a[2,2],a[3,3],a[4,4],a[5,5]],
                   [a[5,0],a[4,1],a[3,2],a[2,3],a[1,4],a[0,5]]])

    #array of element surrounding the diagonal
    ab = np.array([[a[0,1],a[1,2],a[2,3],a[3,4],a[4,5]],
                   [a[1,0],a[2,1],a[3,2],a[4,3],a[5,4]],
                   [a[4,0],a[3,1],a[2,2],a[1,3],a[0,4]],
                   [a[5,1],a[4,2],a[3,3],a[2,4],a[1,5]]])

    score = 0
    total_score = 0

    #get score for each group in a same row
    for row_index in range(6):
        for subset in range(6):
            for col_index in range(6 - subset):
#                 print("Now with subset and index:",subset+1,row_index, all(a[row_index, col_index:col_index+subset+1] == turn))
#                 print("Current score and add score:", score, 10**subset)
                if all(a[row_index, col_index:col_index+subset+1] == turn): 
                    score += 10**subset
#         print(score)
        total_score += score
        score = 0

    #get score for each group in a same column
    for col_index in range(6):
        for subset in range(6):
            for row_index in range(6 - subset):
                if all(a[row_index:row_index+subset+1,col_index] == turn): 
                    score+=10**subset
        #print(score)
        total_score += score
        score = 0

    #get score for each group in a same diagonal, 4 5 crossing diagonal
    for row_index in range(4):
        for subset in range(5):
            for col_index in range(5 - subset):
                if all(ab[row_index, col_index:col_index+subset+1] == turn): 
                    score+=10**subset
        #print(score)
        total_score += score
        score = 0

    #get score for each group in a same diagonal, 2 6 crossing diagonal
    for row_index in range(2):
        for subset in range(6):
            for col_index in range(6 - subset):
                if all(ac[row_index, col_index:col_index+subset+1] == turn): 
                    score+=10**subset
        #print(score)
        total_score += score
        score = 0

    #print("total score is:",total_score)
    return total_score

#AI Part

#Computer Level Easy, Just put stuff randomly
def computer_easy(board, turn):
   
    check_board = 1 * board
    row = col = rot = 0
    
    # Check if certain position is impossible, repeat until valid move
    while True:
        row = np.random.randint(0,6)
        col = np.random.randint(0,6)
        rot = np.random.randint(1,9)
        
        if check_move(check_board, row, col):
            break
    
    return row, col, rot

def computer_medium(board, turn):
    
    # Specify the turn of the computer
    opp_turn = 2 if turn == 1 else 1
    for row in range(0,6):
        for col in range(0,6):
            for rot in range(1,9):
                check_board_one = 1 * board
                check_board_two = 1 * board 

                # Check for every position that's still 0 in the board
                if check_move(check_board_one, row, col) == True:
                    
                    check_board_one[row,col] = turn
                    check_board_one = rotation(check_board_one, rot)
                    
                    check_board_two[row,col] = opp_turn
                    check_board_two = rotation(check_board_two, rot)
                    
                    # Directly win position
                    if (check_victory(check_board_one, rot) == turn):
                        return row, col, rot

                    # Directly lose position
                    elif (check_victory(check_board_two, rot) == opp_turn):
                        return row, col, rot
                    
                    # Random computer
    else:
        return computer_easy(board, turn)

#Computer Level Hard, Do move based on scoring system of the future board
def computer_hard(board, turn):
    #initializing opponent turn
    opp_turn = 2 if turn == 1 else 1
    best_score = -999999999
    current_score = 0
    best_row = 0
    best_col = 0 
    best_rot = 0
    
    #iterate through all combination of movement        
    for row in range(0,6):
        for col in range(0,6):
            for rot in range(1,9):
                check_board_one = 1 * board
                check_board_two = 1 * board 

                # Check for every position that's still 0 in the board
                if check_move(check_board_one, row, col) == True:
                    
                    check_board_one[row,col] = turn
                    check_board_one = rotation(check_board_one, rot)
                    
                    check_board_two[row,col] = opp_turn
                    check_board_two = rotation(check_board_two, rot)
                    
                    # Directly win position
                    if (check_victory(check_board_one, rot) == turn):
                        score = 999999
                        return row, col, rot, score

                    # Directly lose position
                    elif (check_victory(check_board_two, rot) == opp_turn):
                        score = 999999
                        return row, col, rot, score
                    
                    # Scoring system for this current configuration                  
                    current_score = scoring(check_board_one, turn) - scoring(check_board_one, opp_turn)

                    if current_score >= best_score:
                        #save the current best score, and best location
                        best_row, best_col, best_rot, best_score = row, col, rot, current_score                             
                    
    # Random computer
    # Replace with beads placement in best current scoring configuration
    else:
        return best_row, best_col, best_rot, best_score                                         
           
        

#Computer Level Super Hard, Do move based on scoring system optimize by minimax function for the future x move
def computer_super_hard(board, turn):
    #minimax function
    
    
    
    pass

#Computer Level Super Hard, Do move based on scoring system optimize by minimax function for the future x move
#def computer_super_hard(board, turn):


#minimax function 
# working of Alpha-Beta Pruning  
  
#(Initially called for root and maximizer)  
def minimax(root, depth, alpha, beta, maximizingPlayer):  
   
    print(root, root.score, depth, alpha, beta, maximizingPlayer)
    # Terminating condition. i.e  
    # leaf node is reached  
    if depth == 0 : #or someone win/game over in this position, stop
        return root.score
      
    #minimax for maximizing player
    if maximizingPlayer:  
        maxEval = -9999999  
        
        # Recur for left children maximizing player
        left_val = minimax(root.left, depth - 1, alpha, beta, False)
        maxEval = max(maxEval, left_val)  
        alpha = max(alpha, left_val)  

        # Alpha Beta Pruning  
        if beta <= alpha:  
            return maxEval
            
        # Recur for Right children maximizing player
        right_val = minimax(root.right, depth - 1, alpha, beta, False)
        maxEval = max(maxEval, right_val)  
        alpha = max(alpha, right_val)  

        # Alpha Beta Pruning  
        if beta <= alpha:  
            return maxEval
        return maxEval
    
    #minimax for minimizing player
    else :  
        minEval = 9999999  
        
        # Recur for left children maximizing player
        left_val = minimax(root.left, depth - 1, alpha, beta, True)
        minEval = min(minEval, left_val)  
        beta = min(alpha, left_val)  

        # Alpha Beta Pruning  
        if beta <= alpha:  
            return minEval
            
        # Recur for Right children maximizing player
        right_val = minimax(root.right, depth - 1, alpha, beta, True)
        minEval = min(minEval, right_val)  
        alpha = min(alpha, right_val)  

        # Alpha Beta Pruning  
        if beta <= alpha:  
            return minEval
        return minEval

welcome()
menu()