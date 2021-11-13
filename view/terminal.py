import os

def console_clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def print_picked_letters(picked_letters):
    print(picked_letters)
