from math import pi
import string
import random

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