# file = "test_input.txt"
file = "input.txt"

with open(file) as f:
  grid = f.read().splitlines()

count = 0

for row in range(len(grid)):
  for col in range(len(grid[0])):
    if grid[row][col] != "A": continue
    # Check if out of bounds
    if row - 1 < 0 or row + 1 > len(grid) -1: continue
    if col - 1 < 0 or col + 1 > len(grid[0]) -1: continue

    if {grid[row - 1][col - 1], grid[row + 1][col + 1]} == {"M", "S"} and {grid[row + 1][col - 1], grid[row - 1][col + 1]} == {"M", "S"}:
      count += 1

print(count)
