from typing import Optional, Iterator


type GridPoint = tuple[int, int]
type Grid = dict[tuple[int, int], str]
type IntGrid = dict[tuple[int, int], int]

CARDINAL_DIRS = [
    (0, -1),          # North
    (-1, 0), (1, 0),  # West, East
    (0, 1),           # South
]

DIAGONAL_DIRS = [
    (-1, -1), (1, -1),  # NW, NE
    (-1, 1),  (1, 1),   # SW, SE
]

CENTER = [(0, 0)]


def neighbors(
        center: GridPoint,
        num_dirs=8,
        *,
        max_x_size: Optional[int] = None,
        max_y_size: Optional[int] = None,
) -> Iterator[GridPoint]:
    assert num_dirs in {4, 8, 9}

    offsets = CARDINAL_DIRS
    if num_dirs >= 8:
        offsets += DIAGONAL_DIRS
    if num_dirs == 9:
        offsets += CENTER

    x, y = center

    for dx, dy in offsets:
        next_x, next_y = x + dx, y + dy

        if max_x_size is not None and (next_x < 0 or next_x > max_x_size):
            continue
        if max_y_size is not None and (next_y < 0 or next_y > max_y_size):
            continue

        yield (next_x, next_y)


def parse_grid(
    raw_grid: list[str], 
    *, 
    int_vals: bool = False, 
    ignore_chars: str = ""
) -> Grid | IntGrid:
    """Convert a 2D text grid into a dictionary of coordinates and values.
    
    Args:
        raw_grid: List of strings representing grid rows
        int_vals: If True, converts values to integers
        ignore_chars: Characters to skip (e.g., walls or empty spaces)
    
    Returns:
        Dictionary mapping (row, col) coordinates to their values.
        Origin (0,0) is top-left, increasing down and right.
        
    Example:
        >>> grid = ['123', '456']
        >>> parse_grid(grid, int_vals=True)
        {(0,0): 1, (0,1): 2, (0,2): 3, (1,0): 4, (1,1): 5, (1,2): 6}
        >>> grid[0, 0]  # Access top-left value
        1
    """
    grid = {}
    for row, line in enumerate(raw_grid):
        for col, char in enumerate(line):
            if char in ignore_chars:
                continue
            grid[row, col] = int(char) if int_vals else char
            
    return grid