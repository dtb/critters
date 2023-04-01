from collections import defaultdict


class Board:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.board = defaultdict(lambda: False)
        self.critters = {}

    def __str__(self):
        board = ""
        for y in range(self.width):
            for x in range(self.height):
                item = self.board[self.__pos(x, y)]

                board += "_" if not item else "."
            board += "\n"

        return board

    def __getitem__(self, pos):
        return self.board[self.__pos(*pos)]

    def __pos(self, x: int, y: int) -> int:
        assert y < self.height
        assert x < self.width
        assert x * y < self.width * self.height
        return y * self.width + x

    def locate(self, item) -> (int, int):
        '''Return the position of an item on the board, or None if not found.'''
        return self.critters.get(item, None)

    def remove(self, item):
        pos = self.locate(item)
        self.board[self.__pos(*pos)] = False
        del self.critters[item]

    def move(self, x: int, y: int, item) -> bool:
        '''Move an item to a position.
         Returns True if successful, False if the position is occupied.'''

        if (x < 0 or x >= self.width or y < 0 or y >= self.height):
            return False

        if self.board[self.__pos(x, y)]:
            return False

        if item in self.critters:
            old_pos = self.critters[item]
            self.board[self.__pos(*old_pos)] = False

        self.board[self.__pos(x, y)] = item
        self.critters[item] = (x, y)

        return True
