import random
from board import Board
from critter import Critter
from brain import Brain


class Simulation:
    '''A simulation of critters on a board.'''

    def __init__(self, board: Board, critters: list[Critter], steps=10):
        self.board = board
        self.critters = critters
        self.steps = steps

    def run(self):
        '''Run the simulation'''

        for step in range(0, self.steps):
            # print(f'===={step}====')
            # print(self.board)
            for critter in self.critters:
                critter.behave(self.board)

            if step % 10 == 0:
                self._cull()

    def _cull(self):
        '''Remove critters that fail the selection criteria'''

        print("===Culling===")
        print(self.board)
        print("List: ", end="")
        kill_list = []
        orig_len = len(self.critters)
        for critter in self.critters:
            pos = self.board.locate(critter)
            print(critter, end="")
            print(pos, end="")
            if pos[0] > 0:
                print("<-cull", end="")
                kill_list.append(critter)
            print()
        for critter in kill_list:
            self.critters.remove(critter)
            self.board.remove(critter)

        print()
        print(f"Survival rate: {len(self.critters) / orig_len * 100:.2f}")
        print(self.board)

        new_critters = []
        for _ in range(orig_len - len(self.critters)):
            lucky_critter = random.choice(self.critters)
            print(f"Cloning {lucky_critter.name}")
            new_critters.append(
                Critter(lambda parent_brain=lucky_critter.brain: Brain(parent=parent_brain)))

            while True:
                x = random.randint(0, self.board.width)
                y = random.randint(0, self.board.height)
                if self.board.move(x, y, new_critters[-1]):
                    break
        self.critters.extend(new_critters)


def init_critters(board: Board):
    '''Initialize critters on the board.'''
    critters = []

    for _ in range(10):
        critters.append(Critter(Brain))
        while True:
            x = random.randint(0, board.width)
            y = random.randint(0, board.height)
            if board.move(x, y, critters[-1]):
                break

    return critters


def run():
    '''Run the simulation.'''
    board = Board(10, 10)
    critters = init_critters(board)

    sim = Simulation(board, critters, steps=100)
    sim.run()


if __name__ == "__main__":
    run()
