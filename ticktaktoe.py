import time

class Game:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.current_state = [['.','.','.'],
                              ['.','.','.'],
                              ['.','.','.']]

        # Player X always plays first
        self.player_turn = 'X'

    def draw_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print('{}|'.format(self.current_state[i][j]), end=" ")
            print()
        print()

#determine if the move is legal move
def is_valid(self, px, py):
    if px < 0 or px > 2 or py < 0 or py > 2:
        return False
    elif self.current_state[px][py] != '.':
        return False
    else:
        return True
