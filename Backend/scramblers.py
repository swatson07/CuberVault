import random

moves = ["U", "D", "L", "R", "F", "B",
         "U'", "D'", "L'", "R'", "F'", "B'",
         "U2", "D2", "L2", "R2", "F2", "B2"]

def is_redundant(move, prev):
    """Checks if the current move repeats the same face as the previous move."""
    if prev is None:
        return False
    return move[0] == prev[0]

def full_scramble():
    """Scrambles the Cube ready for solving."""
    scramble = []
    while len(scramble) < 21:
        move = random.choice(moves)
        prev = scramble[-1] if scramble else None
        if is_redundant(move, prev):
            continue
        scramble.append(move)

    return scramble