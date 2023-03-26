from board import Board


chars = iter('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')


class Critter:
    '''A critter is an object that can move around on a board.'''

    def __init__(self, Brain):
        self.name = next(chars)
        self.brain = Brain()

    def __str__(self):
        return self.name

    def behave(self, board: Board):
        '''Have the critter behave on the board.'''

        behavior = self.brain(self, board)
        pos = board.locate(self)
        if behavior == self.brain.Behavior.MOVE_LEFT:
            print(f"{str(self)} is moving left")
            board.move(pos[0] - 1, pos[1], self)
        elif behavior == self.brain.Behavior.MOVE_RIGHT:
            print(f"{str(self)} is moving right")
            board.move(pos[0] + 1, pos[1], self)
        elif behavior == self.brain.Behavior.MOVE_UP:
            print(f"{str(self)} is moving up")
            board.move(pos[0], pos[1] - 1, self)
        elif behavior == self.brain.Behavior.MOVE_DOWN:
            print(f"{str(self)} is moving down")
            board.move(pos[0], pos[1] + 1, self)
