import pytest
from critter import Critter


def test_critter_name():
    critter = Critter(lambda: None)
    assert critter.name == "A"

    critter2 = Critter(lambda: None)
    assert critter2.name == "B"
