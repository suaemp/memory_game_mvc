import os
import string

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
    size = len(board)

    for i in range(size):
        print(f"   {i + 1}", end="")
    print()

    for i in range(size):
        print(f"\n{string.ascii_uppercase[i]} ", end="")

        for j in range(len(board[i])):
            print(" #  ", end="")
        print()

def get_input(message):
    data = input(f"{message}")
    return data