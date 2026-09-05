from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Move:
    cp_map: List[int]
    co_delta: List[int]
    ep_map: List[int]
    eo_delta: List[int]

MOVES = {
    "U" : Move(
        cp_map = [3, 0, 1, 2, 4, 5, 6, 7],
        co_delta = [0, 0, 0, 0, 0, 0, 0, 0],
        ep_map = [3, 0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11],
        eo_delta = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ),

    "R" : Move(
        cp_map = [0, 5, 1, 3, 4, 6, 2, 7],
        co_delta = [0, 1, 2, 0, 0, 2, 1, 0],
        ep_map = [4, 1, 2, 3, 8, 5, 6, 0, 7, 9, 10, 11],
        eo_delta = [1,]
    )
}