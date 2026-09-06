from moves import Move, MOVES

# Class to track the Cube state using permutation and orientation
# The UFR corner is 0 and counts clockwise so the UFL corner is 1, the UBL corner is 2 etc.
# The UR edge is 0 and counts clockwise so the UF edge is 1, the UL edge is 2 etc.
class CubeState:
    def __init__(self):
        self.corner_perm = list(range(8))       
        self.edge_perm = list(range(12))              

        self.corner_orient = [0] * 8
        self.edge_orient = [0] * 8

    # Method to update the cube state when a move is made
    def apply_move(self, move_name):
        move: Move = MOVES[move_name]

        # Update corner and edge permutations
        self.corner_perm = [self.corner_perm[i] for i in move.cp_map]
        self.edge_perm = [self.edge_perm[i] for i in move.ep_map]

        # Update corner and edge orientations
        self.corner_orient = [(self.corner_orient[move.cp_map[i]] + move.co_delta[i]) % 3 for i in range(8)]
        self.edge_orient = [(self.edge_orient[move.ep_map[i]] + move.eo_delta[i]) % 2 for i in range(12)]

    # Method to update the cube state with a full scramble
    def apply_scramble(self, scramble: list):
        for move_name in scramble:
            # If a prime move repeat 3 times to simulate a reverse turn
            if move_name[-1] == "'":
                self.apply_move(move_name)
                self.apply_move(move_name)
                self.apply_move(move_name)
            # Rotate twice if a double move
            elif move_name[-1] == "2":
                self.apply_move(move_name)
                self.apply_move(move_name)
            else:
                self.apply_move(move_name)