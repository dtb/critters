import random
from board import Board
from critter import Critter


class Simulation:
    def __init__(self, board: Board, critters: list[Critter], steps=10):
        self.board = board
        self.critters = critters
        self.steps = steps

    def run(self):
        '''Run the simulation'''
        for step in range(0, self.steps):
            print(f'===={step}====')
            print(self.board)
            for critter in self.critters:
                critter.behave(self.board)


def init_critters(board: Board):
    '''Initialize critters on the board.'''
    critters = []

    for _ in range(10):
        critters.append(Critter())
        while True:
            x = random.randint(0, board.width)
            y = random.randint(0, board.height)
            if board.move(x, y, critters[-1]):
                break

    return critters


def run():
    board = Board(10, 10)
    critters = init_critters(board)

    sim = Simulation(board, critters)
    sim.run()


if __name__ == "__main__":
    run()
