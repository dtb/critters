from board import Board
import random

from critter import Critter
from brain import Brain


class Simulation:
    '''A simulation of critters on a board.'''

    def __init__(self, board: Board, critter_count, steps=10):
        self.board = board
        self.critter_count = critter_count
        self.steps = steps
        self.critters = []

        self.boards = []

    def __init(self):
        '''Initialize critters on the board.'''

        for _ in range(self.critter_count):
            self.critters.append(Critter(Brain))
            self.__place(self.critters[-1])

    def __place(self, critter):
        '''Place a critter on the board.'''
        while True:
            x = random.randint(0, self.board.width)
            y = random.randint(0, self.board.height)
            if self.board.move(x, y, critter):
                break

    def run(self):
        '''Run the simulation'''

        self.__init()

        self.boards.append(str(self.board))
        for step in range(0, self.steps):
            for critter in self.critters:
                critter.behave(self.board)

            self.boards.append(str(self.board))
            if step % 10 == 0:
                self._cull()

    def _cull(self):
        '''Remove critters that fail the selection criteria'''

        buffer = []
        buffer.append("===Culling===\n")
        buffer.append("List: \n")

        kill_list = []
        orig_len = len(self.critters)
        for critter in self.critters:
            pos = self.board.locate(critter)
            buffer.append(str(critter))
            buffer.append(str(pos))
            if pos[0] > 0:
                buffer.append("<-cull")
                kill_list.append(critter)
            buffer.append("\n")

        for critter in kill_list:
            self.critters.remove(critter)
            self.board.remove(critter)

        buffer.append("\n")
        buffer.append(
            f"Survival rate: {len(self.critters) / orig_len * 100:.2f}\n")
        buffer.append(str(self.board))
        buffer.append("\n")

        new_critters = []
        for _ in range(orig_len - len(self.critters)):
            lucky_critter = random.choice(self.critters)
            buffer.append(f"Cloning {lucky_critter.name}\n")
            new_critters.append(
                Critter(lambda parent_brain=lucky_critter.brain: Brain(parent=parent_brain)))

            self.__place(new_critters[-1])

        self.critters.extend(new_critters)

        self.boards.append("".join(buffer))
