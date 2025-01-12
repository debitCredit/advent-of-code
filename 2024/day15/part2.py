from utils.utils import Grid
from collections import defaultdict

# file = "test_input.txt"
file = "input.txt"

with open(file) as f:
    grid_txt, moves_txt = f.read().split('\n\n')

# Transform for part 2 first
grid_txt = grid_txt.translate(str.maketrans({
    "#": "##", 
    ".": "..",
    "O": "[]",
    "@": "@."
}))
moves_txt = ''.join(moves_txt.split())
moves_txt = moves_txt.translate(str.maketrans({
    "^": "N", 
    "v": "S",
    "<": "W",
    ">": "E"
}))

grid = Grid.from_strings(grid_txt.splitlines())


def push_boxes(grid: Grid, direction: str) -> Grid:
    """Push boxes in specified cardinal direction.
    
    This function simulates movement of boxes and the player ('@') on a grid. 
    Boxes are represented by '[' and ']' on two adjacent positions. 
    If a box cannot be pushed further (due to walls or other boxes), 
    the movement stops, affecting all subsequent pushes in that direction.

    Args:
        grid: Grid instance containing the game state
        direction: One of 'N', 'S', 'W', 'E' for north, south, west, east movement

    Returns:
        New Grid instance (either moved or unchanged if blocked.)
    """
    new_grid = grid.copy()
    player_pos = grid.find_first('@')
    if not player_pos:
        return grid
    
    # Direction offsets
    direction_map = {
        'N': (-1, 0),
        'S': (1, 0),
        'E': (0, 1),
        'W': (0, -1)
    }
    dx, dy = direction_map[direction]
    
    def safe_get(pos):
        """Safely get grid value, returns None if position is invalid."""
        row, col = pos
        if 0 <= row < grid.height and 0 <= col < grid.width and pos in grid:
            return grid[pos]
        return None
    
    # Find all box positions (as left-right pairs)
    box_positions = []
    for row in range(grid.height):
        for col in range(grid.width-1):
            if safe_get((row, col)) == '[' and safe_get((row, col+1)) == ']':
                box_positions.append((row, col))
    
    # Find all coordinates that need to move
    coords_to_move = [player_pos]
    i = 0
    impossible = False
    
    # Build list of all coordinates that need to move
    while i < len(coords_to_move):
        x, y = coords_to_move[i]
        nx, ny = x + dx, y + dy
        
        # Check if move is blocked by wall
        if safe_get((nx, ny)) == '#':
            impossible = True
            break
        
        # If we hit a box, add both parts
        for box_row, box_col in box_positions:
            if (nx, ny) in [(box_row, box_col), (box_row, box_col+1)]:
                if (box_row + dx, box_col) not in [(p[0], p[1]) for p in coords_to_move]:
                    coords_to_move.append((box_row, box_col))
                    coords_to_move.append((box_row, box_col + 1))
        i += 1
    
    # If move is possible, execute it
    if not impossible:
        # First clear all moving pieces
        for x, y in coords_to_move:
            new_grid[x, y] = '.'
        
        # Then move all pieces to new positions
        for x, y in coords_to_move:
            val = grid[x, y]
            new_x, new_y = x + dx, y + dy
            new_grid[new_x, new_y] = val
    
    return new_grid

def safe_get(grid, pos):
    """Safely get grid value, returns None if position is invalid."""
    row, col = pos
    if 0 <= row < grid.height and 0 <= col < grid.width and pos in grid:
        return grid[pos]
    return None


moves = list(moves_txt)
for move in moves:
    grid = push_boxes(grid, move)

total = 0
for box in grid.find_all("["):
    x, y = box
    total += 100 * x + y

print(total)