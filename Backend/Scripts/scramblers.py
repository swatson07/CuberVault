import random
import json
from enum import Enum

# Possible cube moves
moves = ["U", "D", "L", "R", "F", "B",
         "U'", "D'", "L'", "R'", "F'", "B'",
         "U2", "D2", "L2", "R2", "F2", "B2"]

# OLL version
class OLLVersion(Enum):
    TWO_LOOK = "2-look"
    ADVANCED = "advanced"


# Full scramble
# Checks if the current move is redundant 
def is_redundant(move, prev):
    if prev is None:
        return False
    return move[0] == prev[0]

# Generates a manoeuvre to scramble the cube 
def full_scramble():
    scramble = []
    while len(scramble) < 21:
        move = random.choice(moves)
        prev = scramble[-1] if scramble else None
        if is_redundant(move, prev):
            continue
        scramble.append(move)

    return scramble


# OLL scramble
#Load OLL cases
with open("Backend/OLL_cases.json", "r") as f:
    OLL_CASES = json.load(f)

# Generates a manoeuvre to a random OLL case
def OLL_scramble(version: OLLVersion):
    if not isinstance(version, OLLVersion):
        raise TypeError("version is not type: OLLVersion")

    case = random.choice(list(OLL_CASES[str(version.value)].keys()))
    