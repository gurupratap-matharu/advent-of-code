import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""

    return [int(x) for x in puzzle_input.split("\n")]


def part1(numbers):
    """Solve part1"""

    return sum(((x // 3) - 2) for x in numbers)


def get_total_module_fuel(n):
    """
    Finds the total fuel needed for each module mass
    """

    total_fuel = 0
    while n > 6:
        n = (n // 3) - 2
        total_fuel += n

    return total_fuel


def part2(numbers):
    """Solve part2"""

    fuels = (get_total_module_fuel(n) for n in numbers)
    return sum(fuels)


def solve(puzzle_input):
    """Solve the puzzles for the given input"""

    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print(solutions)
