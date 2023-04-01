import tkinter as tk
import tkinter.ttk as ttk
import asyncio

from board import Board
from simulation import Simulation


def start():
    print("starting")


class App:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.columnconfigure(0, weight=1, minsize=600)
        self.window.rowconfigure(0, weight=0, minsize=600)

        self.window.columnconfigure(1, weight=0, minsize=100)
        self.window.rowconfigure(1, weight=1, minsize=300)

        board_frame = tk.Frame(
            master=self.window,
        )
        board_frame.grid(row=0, column=0)
        self.board_canvas = tk.Canvas(
            master=board_frame, bg="white", height=600, width=600)
        self.board_canvas.pack()

        buttons_frame = tk.Frame(
            master=self.window,
        )
        buttons_frame.grid(row=0, column=1)
        start_button = ttk.Button(master=buttons_frame,
                                  text="Start", command=self.start)
        start_button.pack()

        message_frame = tk.Frame(
            master=self.window,
        )

        message_frame.grid(row=1, column=0, columnspan=2)

    def start(self):
        print("starting")
        board = Board(100, 100)
        sim = Simulation(board, critter_count=100, steps=600, cull_every=110)
        sim.run()

        self.animateBoards(sim, sim.boards)

    def run(self):
        self.circs = []
        # self.window.after(12, self.animate)
        self.window.mainloop()

    def animateBoards(self, sim: Simulation, boards):
        if len(boards) == 0:
            print("no boards?!")

        self.animateBoard(sim, boards, 0)

    def animateBoard(self, sim: Simulation, boards, idx):
        CRITTER_RADIUS = 6
        for i in range(0, sim.critter_count):
            self.circs.append(self.board_canvas.create_oval(
                0, 0, CRITTER_RADIUS, CRITTER_RADIUS, fill="red"))

        board = boards[idx]
        circ_index = 0

        pos_y_max = 0
        pos_x_max = 0
        pos_x_min = 1000
        pos_y_min = 1000
        pos = 0
        for char in board:
            if char == '_':
                pos += 1
            elif char == '.':
                pos_x = pos % sim.board.width
                pos_y = pos // sim.board.width

                if pos_x > pos_x_max:
                    pos_x_max = pos_x

                if pos_y < pos_y_min:
                    pos_y_min = pos_y

                if pos_x < pos_x_min:
                    pos_x_min = pos_x

                if pos_y > pos_y_max:
                    pos_y_max = pos_y

                self.board_canvas.moveto(
                    self.circs[circ_index],
                    pos_x * CRITTER_RADIUS,
                    pos_y * CRITTER_RADIUS
                )
                circ_index += 1
                pos += 1
            elif char == '\n':
                pass
            else:
                print(f"wtf is this char: {char} at pos: {pos}")

        print(pos_x_max, pos_y_max, pos_x_min, pos_y_min)
        self.board_canvas.after(
            3, lambda idx=idx: self.animateBoard(sim, boards, idx + 1))


def run():
    '''Run the simulation.'''
    app = App()
    app.run()
    # sim = Simulation(board, critter_count=100, steps=600, cull_every=110)
    # sim.run


if __name__ == "__main__":
    run()
