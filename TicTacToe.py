                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          # -*- coding: utf-8 -*-
"""
Created on Wed May 13 19:18:50 2020

@author: Yash
"""
#------Global variables----
#If game is running
game_still_going = True

winner = None

current_player="X"

#Game board
board=['-','-','-',
       '-','-','-',
       '-','-','-']


def show_board():
    print(board[0]+'|'+board[1]+'|'+board[2])    
    print(board[3]+'|'+board[4]+'|'+board[5])
    print(board[6]+'|'+board[7]+'|'+board[8])
    
    
    
def play():
    #Shows board every time
    show_board()
    
    while game_still_going:
        #Handles the turn of player
        handel_turn(current_player)
        
        #check if the game is over
        check_if_game_over()
        
        #Changes player every turn
        change_player()
    
    # Game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    else:
        print("Tie.")


def handel_turn(player):
    print(player+ "'s turn")
    position = input("Choose a position from 1 to 9 :\n ")
    
    valid =False
    while not valid:
        
        while position not in ['1','2','3','4','5','6','7','8','9']:
            position =  input("Choose a position from 1 to 9 :\n ")
   
        position=int(position) - 1
    
        if board[position] == '-':
             valid = True
        else:
             print("Cant place there,Go again")

    board[position]= player
    
    show_board()

def check_if_game_over():
    check_if_win()
    
    check_if_tie()
    
def check_if_win():
    
    
    global winner
    
    
    # check_rows()
    row_winner= check_rows()
    
    # check_columns()
    column_winner = check_columns()
    
    # check_diagonals()
    diagonal_winner = check_diagonals()
    
    if row_winner: 
        winner = row_winner
    
    elif column_winner:
        winner= column_winner
   
    elif diagonal_winner:
        winner= diagonal_winner
        
    return winner


def check_rows():
    
    global game_still_going
    
    # check every row for winner
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'
    if row_1 or row_2 or row_3:
        game_still_going= False
    if row_1:
       return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]

def check_columns():
    
    global game_still_going
    
    # check every row for winner
    column_1 = board[0] == board[3] == board[6] != '-'
    column_2 = board[1] == board[4] == board[7] != '-'
    column_3 = board[2] == board[5] == board[8] != '-'
    
    if column_1 or column_2 or column_3:
        game_still_going= False
    if column_1:
       return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]
    return

def check_diagonals():
    
    global game_still_going
    
    # check every row for winner
    diagonal_1 = board[0] == board[4] == board[8] != '-'
    diagonal_2 = board[2] == board[4] == board[6] != '-'
  
    
    if diagonal_1 or diagonal_2 :
        game_still_going= False
    if diagonal_1:
       return board[0]
    if diagonal_2:
        return board[6]

    return

def check_if_tie():
    
    global game_still_going
    
    if '-' not in board:
        game_still_going = False
    
    
def change_player():
    
    global current_player
    
    if current_player=="X":
        current_player="O"
    elif current_player=="O":
        current_player="X"
        
repeat_game = True
while repeat_game:
    board=['-','-','-',
           '-','-','-',
           '-','-','-']
    game_still_going = True

    winner = None

    current_player="X"
    play()
    option =input("Wanna play again?\n Press Q to Quit or any key to continue: ")
    if option == 'q':
        repeat_game = False
        