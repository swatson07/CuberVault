from dataclasses import dataclass
from typing import List

# Immutable class for the moves
@dataclass(frozen=True)
class Move:
    cp_map: List[int]       # Corner permutation
    co_delta: List[int]     # Corner orientation delta
    ep_map: List[int]       # Edge permutation
    eo_delta: List[int]     # Edge orientation delta

# All basic moves
MOVES = {
    "U" : Move(
        cp_map = [3, 0, 1, 2, 4, 5, 6, 7],
        co_delta = [0, 0, 0, 0, 0, 0, 0, 0],
        ep_map = [3, 0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11],
        eo_delta = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ),

    "D" : Move(
        cp_map = [0, 1, 2, 3, 7, 4, 5, 6],
        co_delta = [0, 0, 0, 0, 0, 0, 0, 0],
        ep_map = [0, 1, 2, 3, 4, 5, 6, 7, 11, 8, 9, 10],
        eo_delta = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ),

    "R" : Move(
        cp_map = [4, 1, 2, 0, 7, 5, 6, 3],
        co_delta = [2, 0, 0, 1, 1, 0, 0, 2],
        ep_map = [4, 1, 2, 3, 8, 5, 6, 0, 7, 9, 10, 11],
        eo_delta = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ),

    "L" : Move(
        cp_map = [0, 2, 6, 3, 4, 1, 5, 7],
        co_delta = [0, 1, 2, 0, 0, 2, 1, 0],
        ep_map = [0, 1, 6, 3, 4, 2, 10, 7, 8, 9, 5, 11],
        eo_delta = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ),

    "F" : Move(
        cp_map = [1, 5, 2, 3, 0, 4, 6, 7],
        co_delta = [1, 2, 0, 0, 2, 1, 0, 0],
        ep_map = [0, 5, 2, 3, 1, 9, 6, 7, 8, 4, 10, 11],
        eo_delta = [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0]
    ),

    "B" : Move(
        cp_map = [0, 1, 3, 7, 4, 5, 2, 6],
        co_delta = [0, 0, 1, 2, 0, 0, 2, 1],
        ep_map = [0, 1, 2, 7, 4, 5, 3, 11, 8, 9, 10, 6],
        eo_delta = [0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1]
    )
}