import random
from board import Board
from critter import Critter


class Simulation:
    def __init__(self, board: Board, critters: list[Critter]):
        self.board = board
        print(self.board)

    def run(self):
        '''Run one simulation step.'''
        for critter in critters:
            critter.behave(self.board)

        print(self.board)


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


if __name__ == "__main__":
    board = Board(10, 10)
    critters = init_critters(board)

    sim = Simulation(board, critters)

    for step in range(10):
        print(f'===={step}====')
        sim.run()
