import pytest
from critter import Critter


def test_critter_name():
    critter = Critter()
    assert critter.name == "A"

    critter2 = Critter()
    assert critter2.name == "B"
