import pathlib

import pytest

import aoc_1_1 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "test1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_part1_example1(example1):
    """Test part1 on example1 input"""
    assert aoc.part1(example1) == 34241


def test_part2_example1(example1):
    """Test part2 on example1 input"""

    assert aoc.part2(example1) == 51316


def test_get_total_module_fuel():
    """
    Test that individual module fuels are calculated correctly for
    different inputs.
    """

    assert aoc.get_total_module_fuel(-5) == 0
    assert aoc.get_total_module_fuel(2) == 0
    assert aoc.get_total_module_fuel(9) == 1
    assert aoc.get_total_module_fuel(1969) == 966
    assert aoc.get_total_module_fuel(100756) == 50346
