from itertools import cycle

file = "test_input.txt"
# file = "input.txt"

directions = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}
direction_values = cycle(directions.values())

with open(file) as f:
  grid = f.read().splitlines()
  print(grid)

# Determine starting pos:
for row in range(len(grid)):
  for col in range(len(grid[0])):
    if grid[row][col] not in directions.keys():
      continue
    else:
      current_pos = (row, col)

# Check the next pos based on the direction
while len(grid) >= current_pos[0] >= 0 and len(grid[0]) >= current_pos[1] >= 0:
  if current_pos + 