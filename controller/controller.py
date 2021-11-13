from math import pi
from view import terminal as view
from model import model

def clear_console():
    view.console_clear()


def get_board_parameters():
    heigth, width = view.get_board_size_from_user()
    if model.is_value_correct(heigth, width):
        board = model.generate_board(heigth, width)
        view.print_board(board)
    else:
        view.print_error_message("Invalid parameters")

