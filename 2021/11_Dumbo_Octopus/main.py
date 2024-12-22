from pyaoc import *
from itertools import count

file = "input.txt"
# file = "test_input.txt"

with open(file) as f:
    input_data = f.read()

entry = list(input_data.splitlines())

octopuses = Grid(rows=mapt(digits, entry), neighbors=neighbors8)


def check_flash(grid, octopus, flashed):
    """ Check if grid[octopus] flashes and spread the flashes recursively """
    if grid[octopus] > 9 and octopus not in flashed:
        flashed.add(octopus)
        for octo in grid.neighbors(octopus):
            grid[octo] += 1
            check_flash(grid, octo, flashed)


def sim_flashes(grid, steps=100) -> int:
    """ Simulate octopus flashes for n steps and return total number of flashes """
    grid = grid.copy()
    number_of_flashes = 0

    for step in range(steps):
        flashed = set()
        for octo in grid:
            grid[octo] += 1
        for octo in grid:
            check_flash(grid, octo, flashed)
        for octo in flashed:
            grid[octo] = 0
        number_of_flashes += len(flashed)
    return number_of_flashes


def sim_flashes2(grid) -> int:
    """ Simulate octopus flashes until all octopuses flash in the same step and return the step number """
    grid = grid.copy()
    for step in count(1):
        flashed = set()
        for octo in grid:
            grid[octo] += 1
        for octo in grid:
            check_flash(grid, octo, flashed)
        for octo in flashed:
            grid[octo] = 0
        if len(flashed) == len(grid):
            return step


print(sim_flashes(octopuses, 100))
print(sim_flashes2(octopuses))
