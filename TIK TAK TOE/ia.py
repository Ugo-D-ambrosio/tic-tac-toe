import random

def ia(board, signe):

    empty_spots = [i for i in range(9) if board[i] == 0]
    if empty_spots:
        return random.choice(empty_spots)
    else:
        return False
