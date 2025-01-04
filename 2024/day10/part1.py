from collections import deque

# file = "test_input.txt"
file = "input.txt"

with open(file) as f:
  grid = f.read().splitlines()
  grid = [[int(num) for num in row]for row in grid]

rows, cols = len(grid), len(grid[0])

starting_pos = set()

for row in range(rows):
  for col in range(cols):
    if grid[row][col] == 0:
      starting_pos.add((row, col))

def get_next_positions(pos, current_value):
    row, col = pos
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    next_positions = []
    
    target_value = current_value + 1
    if current_value == 9:
        return next_positions
        
    for dx, dy in directions:
        new_row, new_col = row + dx, col + dy
        
        if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
            continue
            
        if grid[new_row][new_col] == target_value:
            next_positions.append((new_row, new_col))
    
    return next_positions

def explore_paths(start_pos):
    queue = deque([(start_pos, 0, [start_pos])])
    unique_paths = set()
    seen = set()

    while queue:
        pos, value, path = queue.popleft()
        
        if (pos, value) in seen:
            continue
        seen.add((pos, value))

        if value == 9:
            unique_paths.add(tuple(path))
            continue

        for next_pos in get_next_positions(pos, value):
            if next_pos not in path:
                queue.append((next_pos, value + 1, path + [next_pos]))

    return [list(p) for p in unique_paths]


starting_pos = {(row, col) for row in range(rows) for col in range(cols) if grid[row][col] == 0}

total = sum(len(explore_paths(start)) for start in starting_pos)

print(total)