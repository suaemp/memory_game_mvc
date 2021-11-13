from math import pi
import string
import random

MAX_BOARD_SIZE = 52

def get_letters_for_game(heigth, width):
    amount_of_unique_letters = (heigth * width) // 2
    picked_letters = []
    i = 0
    while i < amount_of_unique_letters:
        picked_letter = random.choice(string.ascii_uppercase)
        if picked_letter not in picked_letters:
            picked_letters.append(picked_letter)
            i += 1

    picked_letters *= 2
    random.shuffle(picked_letters)
    return picked_letters

def is_value_correct(heigth, width):
    if heigth * width <= MAX_BOARD_SIZE and (heigth * width) % 2 == 0:
        return True
    else:
        return False

def generate_board(heigth, width):
    board = [[""] * width for _ in range(heigth)]
    picked_letters = get_letters_for_game(heigth, width)

    letter_index = 0
    for row in range(heigth):
        for col in range(width):
            board[row][col] = picked_letters[letter_index]
            letter_index += 1

    return board