from utils.utils import Grid

file = "test_input.txt"
# file = "input.txt"

with open(file) as f:
    grid_txt, moves_txt = f.read().split('\n\n')

grid = Grid.from_strings(grid_txt.splitlines())

grid.print()
print(grid.find_first("@"))
robot = grid.find_first("@")
print(grid.get_neighbor_value(robot, "W"))