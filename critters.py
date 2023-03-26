import asyncio

from textual.app import App, ComposeResult
from textual.widgets import Header, Static

from board import Board
from simulation import Simulation


class BoardView(Static):
    '''A view of the board.'''

    def on_mount(self) -> None:
        self.update_timer = self.set_interval(
            1/10, self.next_board, pause=True)

    def next_board(self) -> None:
        try:
            self.update(next(self.boards_iter))
        except StopIteration:
            self.update_timer.pause()

    def set_boards(self, boards):
        self.boards = boards
        self.boards_iter = iter(self.boards)
        self.update_timer.resume()


class SimApp(App):
    def compose(self) -> ComposeResult:
        yield Header("HI")
        yield BoardView("Running simulation...")

    async def on_mount(self) -> None:
        board = Board(100, 100)

        sim = Simulation(board, critter_count=100, steps=500, cull_every=110)
        await asyncio.to_thread(sim.run)
        self.query_one(BoardView).set_boards(sim.boards)


def run():
    '''Run the simulation.'''
    app = SimApp()
    app.run()


if __name__ == "__main__":
    run()
