from view import terminal as view
from model import model

def clear_console():
    view.console_clear()

def print_picked_letters():
    letters_to_print = model.get_letters_for_game(4, 6)
    view.print_picked_letters(letters_to_print)