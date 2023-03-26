import pytest

from board import Board


class Dummy:
    pass


def test_board():
    board = Board(10, 10)
    assert board.move(0, 0, "X")
    assert not board.move(0, 0, "Y")


def test_board_invalid():
    board = Board(10, 10)
    assert not board.move(-1, 0, "X")

    assert not board.move(0, -1, "X")

    assert not board.move(11, 0, "X")

    assert not board.move(0, 11, "X")


def test_board_moves():
    board = Board(10, 10)

    assert board.move(0, 0, "X")
    assert board.move(1, 1, "X")

    assert board.move(0, 0, "Y")
    assert not board.move(1, 1, "Y")
    assert board[0, 0] == "Y"
    assert board[1, 1] == "X"
