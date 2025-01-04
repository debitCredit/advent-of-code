from collections import deque

# file = "test_input.txt"
file = "input.txt"

with open(file) as f:
    grid = [[int(num) for num in row] for row in f.read().splitlines()]
rows, cols = len(grid), len(grid[0])


def get_next_positions(pos, current_value):
    row, col = pos
    neighbors = []
    target = current_value + 1
    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        r, c = row + dr, col + dc
        if 0 <= r < rows and 0 <= c < cols and grid[r][c] == target:
            neighbors.append((r, c))
    return neighbors


def explore_paths(start_pos):
    queue = deque([(start_pos, 0, [start_pos])])
    paths_by_end = {}
    
    while queue:
        pos, value, path = queue.popleft()

        if value == 9:
            paths_by_end.setdefault(pos, set()).add(tuple(path))
            continue
            
        for next_pos in get_next_positions(pos, value):
            if next_pos not in path:
                queue.append((next_pos, value + 1, path + [next_pos]))
    
    return sum(len(paths) for paths in paths_by_end.values())


starting_pos = {(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 0}
print(sum(explore_paths(start) for start in starting_pos))