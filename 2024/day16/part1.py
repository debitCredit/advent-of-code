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
                      turn_cost: int = 1000) -> tuple[list[tuple[int, int]], int]:
    """
    Find shortest path with turn penalties in a grid maze.
    Starting direction is East.
    
    Args:
        grid: Grid instance representing the maze
        start: Starting (row, col) coordinate  
        end: Target (row, col) coordinate
        straight_cost: Cost of moving forward
        turn_cost: Cost of making a turn
    
    Returns:
        Tuple of (path, total_cost) where path is list of coordinates
    """
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
    initial_state = State(start, 1)  # Start facing East
    queue = [(0, initial_state, [start])]
    costs = {initial_state: 0}
    
    while queue:
        total_cost, current_state, path = heapq.heappop(queue)
        
        if current_state.position == end:
            return path, total_cost
        
        for new_dir, (drow, dcol) in enumerate(directions):
            new_pos = (current_state.position[0] + drow, current_state.position[1] + dcol)
            
            # Skip if out of bounds or not walkable
            if not (0 <= new_pos[0] < grid.height and 0 <= new_pos[1] < grid.width):
                continue
            if new_pos not in grid or grid[new_pos] not in [".", "E"]:
                continue
                
            move_cost = straight_cost
            if new_dir != current_state.direction:
                move_cost = turn_cost + straight_cost
            new_cost = total_cost + move_cost
            new_state = State(new_pos, new_dir)
            
            if new_state not in costs or new_cost < costs[new_state]:
                costs[new_state] = new_cost
                heapq.heappush(queue, (new_cost, new_state, path + [new_pos]))
    
    return None, float('inf')

State = namedtuple('State', ['position', 'direction'])
grid = Grid.from_strings(maze.splitlines())
start = grid.find_first("S")
end = grid.find_first("E")
path, cost = find_shortest_path(grid, start, end)

print(cost)