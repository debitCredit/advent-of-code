from itertools import cycle

# file = "test_input.txt"
file = "input.txt"

direction_values = cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])

with open(file) as f:
  grid = f.read().splitlines()
  grid = [list(row) for row in grid]

for row in range(len(grid)):
  for col in range(len(grid[0])):
    if grid[row][col] == "^":
      current_pos = (row, col)
      break
      

rd, cd = next(direction_values)
while True:
  next_pos = (current_pos[0] + rd, current_pos[1] + cd)
  
  if not (0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0])):
      grid[current_pos[0]][current_pos[1]] = "X"
      break
  if grid[next_pos[0]][next_pos[1]] == "#":
      rd, cd = next(direction_values)
  else:
      grid[current_pos[0]][current_pos[1]] = "X"
      current_pos = next_pos


count = sum(row.count("X") for row in grid)
print(count)