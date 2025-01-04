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

def _calc_antinodes(pair: tuple) -> set:
    (ax, ay), (bx, by) = pair
    
    diff_x = bx - ax
    diff_y = by - ay

    antinodes = {(ax, ay), (bx, by)}

    for direction in [-1, 1]:  # Handle both directions in one loop
        point = (bx, by) if direction == 1 else (ax, ay)
        multiplier = 1
        
        while True:
            x = point[0] + (diff_x * multiplier * direction)
            y = point[1] + (diff_y * multiplier * direction)
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                antinodes.add((x, y))
                multiplier += 1
            else:
                break
    
    return antinodes

antinodes = set()

for key in result.keys():
  for pair in result[key]:
    antinodes.update(_calc_antinodes(pair))

print(len(antinodes))