from itertools import count
import random

from board import Board


chars = count(0)


class Critter:
    '''A critter is an object that can move around on a board.'''

    def __init__(self, Brain):
        self.name = f"{next(chars):^3}"
        self.brain = Brain()
        self.age = 0

    def __str__(self):
        return self.name

    def behave(self, board: Board, simulation):
        '''Have the critter behave on the board.'''

        self.age += 1

        behavior = self.brain(self, board)
        pos = board.locate(self)
        if behavior == self.brain.Behavior.MOVE_LEFT:
            board.move(pos[0] - 1, pos[1], self)
        elif behavior == self.brain.Behavior.MOVE_RIGHT:
            board.move(pos[0] + 1, pos[1], self)
        elif behavior == self.brain.Behavior.MOVE_UP:
            board.move(pos[0], pos[1] - 1, self)
        elif behavior == self.brain.Behavior.MOVE_DOWN:
            board.move(pos[0], pos[1] + 1, self)
