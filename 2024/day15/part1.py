from utils.utils import Grid

# file = "test_input.txt"
file = "input.txt"

with open(file) as f:
    grid_txt, moves_txt = f.read().split('\n\n')

def push_boxes(grid: Grid, direction: str) -> Grid:
    """Push boxes in specified cardinal direction.
    
    Args:
        grid: Grid instance containing the game state
        direction: One of 'N', 'S', 'E', 'W'
    
    Returns:
        New Grid instance (either moved or unchanged if blocked.)
    """
    # Create a new grid with copied state
    new_grid = Grid(dict(grid.grid), width=grid.width, height=grid.height)
    
    # Get player position
    player_pos = new_grid.find_first("@")
    if not player_pos:
        return new_grid
        
    direction_map = {
        '^': (-1, 0),    # Up (decrease row)
        'v': (1, 0),     # Down (increase row)
        '<': (0, -1),    # Left (decrease col)
        '>': (0, 1),     # Right (increase col)
    }
    
    if direction not in direction_map:
        return new_grid
        
    drow, dcol = direction_map[direction]
    
    # Find chain of positions to move
    positions_to_move = []
    current_pos = player_pos
    
    while True:
        next_pos = (current_pos[0] + drow, current_pos[1] + dcol)
        next_value = new_grid.grid.get(next_pos, "#")
        
        if next_value == "#":
            return new_grid
            
        if next_value == "O":
            positions_to_move.append(next_pos)
            current_pos = next_pos
            continue
            
        if next_value == ".":
            break
            
        return new_grid

    # If no boxes to push, verify player can move to empty space
    if not positions_to_move:
        next_player_pos = (player_pos[0] + drow, player_pos[1] + dcol)
        if new_grid.grid.get(next_player_pos) != ".":
            return new_grid
            
    # Execute the move
    # 1. Move boxes starting from the last one
    for pos in reversed(positions_to_move):
        new_pos = (pos[0] + drow, pos[1] + dcol)
        new_grid[new_pos] = "O"
        new_grid[pos] = "."
        
    # 2. Move player
    new_player_pos = (player_pos[0] + drow, player_pos[1] + dcol)
    new_grid[new_player_pos] = "@"
    new_grid[player_pos] = "."
    
    return new_grid


grid = Grid.from_strings(grid_txt.splitlines())

moves = list(moves_txt)

for move in moves:
    grid = push_boxes(grid, move)


total = 0
for box in grid.find_all("O"):
    x, y = box
    total += 100 * x + y

print(total)