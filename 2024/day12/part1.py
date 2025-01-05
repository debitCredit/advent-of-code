from utils.utils import neighbors, parse_grid, GridPoint, Grid

file = "test_input.txt"
# file = "input.txt"

with open(file) as f:
  grid = parse_grid(f.read())

print(grid[0, 0])