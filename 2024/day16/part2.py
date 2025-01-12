from collections import namedtuple
import heapq
from utils.utils import Grid

# file = "test_input.txt"
file = "input.txt"

with open(file) as f:
  maze = f.read()


def find_shortest_path(grid: Grid, 
                      start: tuple[int, int], 
                      end: tuple[int, int], 
                      straight_cost: int = 1, 
                      turn_cost: int = 1000) -> tuple[list[list[tuple[int, int]]], int]:
    """
    Find all shortest paths with turn penalties in a grid maze.
    Starting direction is East.
    """
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
    initial_state = State(start, 1)  # Start facing East
    priority_queue = [(0, initial_state, [start])]
    best_paths = []
    min_cost = float('inf')
    
    # Track minimum cost to reach each state (position + direction)
    state_costs = {initial_state: 0}
    
    while priority_queue:
        total_cost, current_state, path = heapq.heappop(priority_queue)
        
        # Skip paths that can't be optimal
        if total_cost > min_cost:
            continue
            
        # Skip if we found a better way to this state
        if total_cost > state_costs[current_state]:
            continue
        
        if current_state.position == end:
            if total_cost <= min_cost:
                if total_cost < min_cost:
                    best_paths = []
                    min_cost = total_cost
                best_paths.append(path)
            continue
        
        for new_dir, (drow, dcol) in enumerate(directions):
            new_pos = (current_state.position[0] + drow, current_state.position[1] + dcol)
            
            # Skip invalid moves
            if (not (0 <= new_pos[0] < grid.height and 0 <= new_pos[1] < grid.width) or
                new_pos not in grid or grid[new_pos] not in [".", "E"] or
                new_pos in path):  # Prevent loops
                continue
                
            # Calculate new cost
            move_cost = straight_cost if new_dir == current_state.direction else turn_cost + straight_cost
            new_cost = total_cost + move_cost
            new_state = State(new_pos, new_dir)
            
            # Only explore if this could lead to an optimal path
            if new_cost <= min_cost and (new_state not in state_costs or new_cost <= state_costs[new_state]):
                state_costs[new_state] = new_cost
                heapq.heappush(priority_queue, (new_cost, new_state, path + [new_pos]))
    
    return best_paths, min_cost if best_paths else (None, float('inf'))



State = namedtuple('State', ['position', 'direction'])
grid = Grid.from_strings(maze.splitlines())
start = grid.find_first("S")
end = grid.find_first("E")
paths, cost = find_shortest_path(grid, start, end)

unique_tiles = set()

for path in paths:
    for tile in path:
        unique_tiles.add(tile)

print(len(unique_tiles))

    