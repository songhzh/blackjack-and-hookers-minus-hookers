import os

def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')