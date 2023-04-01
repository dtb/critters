from board import Board
import random

from critter import Critter
from brain import Brain


class Simulation:
    '''A simulation of critters on a board.'''

    def __init__(self, board: Board, critter_count, steps, cull_every):
        self.board = board
        self.critter_count = critter_count
        self.steps = steps
        self.cull_every = cull_every
        self.critters = []

        self.boards = []
        self.kill_queue = []

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

    def __kill(self, critter):
        '''Kill a critter.'''
        self.critters.remove(critter)
        self.board.remove(critter)

    def kill(self, critter):
        '''Queue a critter to be killed'''
        self.kill_queue.append(critter)

    def kill_queued(self):
        '''kill queued critters'''
        for critter in self.kill_queue:
            self.__kill(critter)
        self.kill_queue = []

    def run(self):
        '''Run the simulation'''

        self.__init()

        self.boards.append(str(self.board))
        for step in range(1, self.steps + 1):
            for critter in self.critters:
                critter.behave(self.board, self)

            self.kill_queued()

            self.boards.append(str(self.board))
            if step % self.cull_every == 0:
                self._cull()
                if len(self.critters) == 0:
                    break

    def _cull(self):
        orig_len = len(self.critters)

        reproducers = []

        output_buffer = ["===CULLING===\n"]

        for critter in self.critters:
            pos = self.board.locate(critter)
            if pos[0] == 0:
                output_buffer.append(f"{critter} will reproduce\n")
                reproducers.append(critter)

            self.kill(critter)

        self.kill_queued()
        output_buffer.append(
            f"Reproduction rate: {len(reproducers) / orig_len * 100:.2f}\n")

        offspring = []
        for reproducer in reproducers:
            offspring.append(Critter(
                lambda parent_brain=reproducer.brain: Brain(parent=parent_brain)))

        for critter in offspring:
            self.__place(critter)
            self.critters.append(critter)

        while len(self.critters) < self.critter_count:
            self.critters.append(Critter(Brain))
            self.__place(self.critters[-1])

        output_buffer.append(str(self.board))
        # self.boards.append("".join(output_buffer))
