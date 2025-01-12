from utils.utils import Grid

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


grid = Grid.from_strings(grid_txt.splitlines())


def push_boxes(grid: Grid, direction: str) -> Grid:
    """Push boxes in specified cardinal direction.
    
    This function simulates movement of boxes and the player ('@') on a grid. 
    Boxes are represented by '[' and ']' on two adjacent positions.
    Movement stops if blocked by a wall or another box.
    
    Args:
        grid: Grid instance containing the game state
        direction: One of 'N', 'S', 'W', 'E' for cardinal directions
        
    Returns:
        New Grid instance with updated positions or unchanged if move is blocked
    """
    new_grid = grid.copy()
    player_pos = grid.find_first('@')
    if not player_pos:
        return grid

    offsets = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}
    dx, dy = offsets[direction]

    # Find all boxes (only need to track left bracket positions)
    boxes = []
    for row in range(grid.height):
        for col in range(grid.width - 1):
            pos = (row, col)
            if pos in grid and (row, col + 1) in grid:
                if grid[pos] == '[' and grid[(row, col + 1)] == ']':
                    boxes.append(pos)
    
    # Calculate which positions need to move
    to_move = [player_pos]
    i = 0
    while i < len(to_move):
        curr_row, curr_col = to_move[i]
        next_row, next_col = curr_row + dx, curr_col + dy
        next_pos = (next_row, next_col)
        
        # Stop if we hit a wall
        if (next_pos in grid and grid[next_pos] == '#' or 
            not (0 <= next_row < grid.height and 0 <= next_col < grid.width)):
            return grid
            
        # Check if we hit a box
        for box_row, box_col in boxes:
            if next_pos in [(box_row, box_col), (box_row, box_col + 1)]:
                box_next = (box_row + dx, box_col)
                if box_next not in [(p[0], p[1]) for p in to_move]:
                    to_move.extend([(box_row, box_col), (box_row, box_col + 1)])
        i += 1
    
    for pos in to_move:
        new_grid[pos] = '.'
    for pos in to_move:
        new_pos = (pos[0] + dx, pos[1] + dy)
        new_grid[new_pos] = grid[pos]
        
    return new_grid


moves = list(moves_txt)
for move in moves:
    grid = push_boxes(grid, move)

total = 0
for box in grid.find_all("["):
    x, y = box
    total += 100 * x + y

print(total)