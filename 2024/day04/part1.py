# file = "test_input.txt"
file = "input.txt"

with open(file) as f:
  grid = f.read().splitlines()

count = 0

for row in range(len(grid)):
  for col in range(len(grid[0])):
    if grid[row][col] != "X": continue
    for dir_row in {-1, 0, 1}:
      for dir_col in {-1, 0, 1}:
        if dir_row == dir_col == 0: continue
        # Check if outside of the range
        if not (0 <= row + 3 * dir_row < len(grid) and 0 <= col + 3 * dir_col < len(grid[0])): continue
        if grid[row + dir_row][col + dir_col] == "M" and grid[row + 2 * dir_row][col + 2 * dir_col] == "A" and grid[row + 3 * dir_row][col + 3 * dir_col] == "S":
          count += 1




print(count)
