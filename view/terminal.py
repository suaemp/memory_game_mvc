import os

def console_clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def print_picked_letters(picked_letters):
    print(picked_letters)

def get_board_size_from_user():
    heigth = int(input("Please give the heigth of the board: "))
    width = int(input("Please give the width of the board: "))
    return heigth, width

def print_error_message(message):
    print(message)

def print_board(board):
    for row in board:
        print(row)