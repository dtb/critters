from board import Board
from simulation import Simulation


def run():
    '''Run the simulation.'''
    board = Board(10, 10)

    sim = Simulation(board, critter_count=10, steps=100)
    sim.run()

    for board in sim.boards:
        print(board)


if __name__ == "__main__":
    run()
