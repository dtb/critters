from collections import defaultdict


class Board:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.state = defaultdict(lambda: False)

    def __pos(self, x: int, y: int) -> int:
        return x * self.width + y

    def move(self, x: int, y: int, item) -> bool:
        if (x < 0 or x >= self.width or y < 0 or y >= self.height):
            raise ValueError("Invalid position")

        if (self.state[self.__pos(x, y)] != False):
            return False

        self.state[self.__pos(x, y)] = item

        return True


class Simulation:
    def __init__(self, board: Board):
        self.board = board

    def run(self):
        pass


if __name__ == "__main__":
    board = Board(10, 10)
    sim = Simulation(board)

    sim.run()
