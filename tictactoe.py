import os
from subprocess import call 

def clear(): 
    _ = call('clear' if os.name =='posix' else 'cls') 

board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

game_running = True
marking = 'X'
possible_moves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def display_board():
    print("----------")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("----------")

def attempt_move(marking):
    select_box = ''
    while select_box not in possible_moves:
        select_box = input("(" + marking + ") Select a box " + str(possible_moves) + ": ")

    board[int(select_box)-1] = marking
    possible_moves.remove(select_box)
    return True

def check_win(marking):
    if len(possible_moves) == 0:
        return True

    if board[0] + board[1] + board[2] == marking*3:
        return True
    
    if board[3] + board[4] + board[5] == marking*3:
        return True
    
    if board[6] + board[7] + board[8] == marking*3:
        return True
    
    if board[0] + board[3] + board[6] == marking*3:
        return True
    
    if board[1] + board[4] + board[7] == marking*3:
        return True
    
    if board[2] + board[5] + board[8] == marking*3:
        return True
    
    if board[0] + board[4] + board[8] == marking*3:
        return True
    
    if board[2] + board[4] + board[6] == marking*3:
        return True
    
    return False
    
while game_running:
    clear()
    display_board()
    if attempt_move(marking):
        if check_win(marking):
            game_running = False
            clear()
            display_board()
            if len(possible_moves) == 0:
                print("It's a draw!")
            else:
                print(marking + " has won the game!")
        else:
            if marking == 'X':
                marking = 'O'
            else:
                marking = 'X'