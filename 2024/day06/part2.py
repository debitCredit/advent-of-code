from itertools import cycle

# file = "test_input.txt"
file = "input.txt"

direction_values = cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])

with open(file) as f:
  grid = [list(row) for row in f.read().splitlines()]

for row in range(len(grid)):
  for col in range(len(grid[0])):
    if grid[row][col] == "^":
      current_pos = (row, col)
      starting_pos = current_pos
      break
      
paths = []
rd, cd = next(direction_values)
while True:
  next_pos = (current_pos[0] + rd, current_pos[1] + cd)
  if not (0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0])):
      grid[current_pos[0]][current_pos[1]] = "X"
      paths.append(((current_pos[0], current_pos[1]), (rd, cd)))
      break
  if grid[next_pos[0]][next_pos[1]] == "#":
      rd, cd = next(direction_values)
  else:
      grid[current_pos[0]][current_pos[1]] = "X"
      paths.append(((current_pos[0], current_pos[1]), (rd, cd)))
      current_pos = next_pos


def _test_path(curr_pos: tuple, obstacle: tuple) -> bool:
  with open(file) as f:
    grid = [list(row) for row in f.read().splitlines()]

  direction_values = cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])
  rd, cd = next(direction_values)
  visited2 = set()
  grid[obstacle[0]][obstacle[1]] = "#"

  while True:
    next_pos = (curr_pos[0] + rd, curr_pos[1] + cd)
    if not (0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0])):
        return
    if grid[next_pos[0]][next_pos[1]] == "#":
        visited2.add(((curr_pos[0], curr_pos[1]), (rd, cd)))
        rd, cd = next(direction_values)
        continue
    if not (next_pos, (rd, cd)) in visited2:
        visited2.add(((curr_pos[0], curr_pos[1]), (rd, cd)))
        curr_pos = next_pos
    if (next_pos, (rd, cd)) in visited2:
        return obstacle


obstacles = set()
for path in paths[1:]:
  obstacles.add(_test_path(curr_pos=starting_pos,
                obstacle=path[0]))            
obstacles.remove(None)

print(len(obstacles))