from board import Board


class Simulation:
    def __init__(self, board: Board):
        self.board = board

    def run(self):
        pass


if __name__ == "__main__":
    board = Board(10, 10)
    sim = Simulation(board)

    sim.run()
