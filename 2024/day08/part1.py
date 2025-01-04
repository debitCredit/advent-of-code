from collections import defaultdict
from itertools import combinations

# file = "test_input.txt"
file = "input.txt"

d = defaultdict(list)
result = defaultdict(list)

with open(file) as f:
  grid = f.read().splitlines()
  grid = [list(row) for row in grid]

for row in range(len(grid)):
  for col in range(len(grid[0])):
    if grid[row][col] != ".":
      d[grid[row][col]].append((row, col))

for key, coords in d.items():
  pairs = list(combinations(coords, 2))
  result[key] = pairs

def _calc_antinodes(pair: tuple) -> tuple:
    (ax, ay), (bx, by) = pair
    
    diff_x = bx - ax
    diff_y = by - ay
    
    x1 = ax - diff_x
    y1 = ay - diff_y
    x2 = bx + diff_x
    y2 = by + diff_y

    return ((x1, y1), (x2, y2))


def _validate_antinode(antinode: tuple) -> bool:
  x, y = antinode
  return 0 <= x < len(grid) and 0 <= y < len(grid[0])


antinodes = set()

for key in result.keys():
  for pair in result[key]:
    antinodes.update(_calc_antinodes(pair))

antinodes_validated = {antinode for antinode in antinodes if _validate_antinode(antinode)}
print(len(antinodes_validated))