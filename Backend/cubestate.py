from moves import Move, MOVES

# Class to track the Cube state using permutation and orientation
class CubeState:
    def __init__(self):
        self.corner_perm = list(range(8))
        self.edge_perm = list(range(12))              

        self.corner_orient = [0] * 8
        self.edge_orient = [0] * 8

    def apply_move(self, move_name):
        move = MOVES[move_name]

        self.corner_perm = [self.corner_perm[i] for i in move.cp_map]
        self.edge_perm = [self.edge_perm[i] for i in move.ep_map]

        self.corner_orient = [(self.corner_orient[move.cp_map[i]] + move.co_delta[i]) % 3 for i in range(8)]
        self.edge_orient = [(self.edge_orient[move.ep_map[i]] + move.eo_delta[i]) % 2 for i in range(12)]
