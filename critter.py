from board import Board


def char_range():
    """Generates the characters from `c1` to `c2`, inclusive."""
    for char in range(ord('A'), ord('Z')+1):
        yield chr(char)


chars = char_range()


class Critter:
    '''A critter is an object that can move around on a board.'''

    def __init__(self):
        self.name = next(chars)

    def __str__(self):
        return self.name

    def behave(self, board: Board):
        '''Behave on the board.'''
        pos = board.locate(self)
        board.move(pos[0], pos[1] + 1, self)
