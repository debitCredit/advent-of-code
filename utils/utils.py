from __future__ import annotations
from typing import Optional, Iterator, Union, Dict

class Grid:
    """A 2D grid representation with coordinate-based access and neighbor utilities.
    
    The Grid class provides a flexible way to work with 2D grids using coordinate-based
    access. It supports both string and integer values, sparse or dense grids, and
    includes utilities for neighbor calculations and pretty printing.
    
    The coordinate system uses (row, col) tuples where:
        - Origin (0,0) is at the top-left
        - Positive row values go downward
        - Positive col values go rightward
    
    The grid can be initialized either from:
        - A list of strings (e.g., ['123', '456'])
        - A dictionary mapping (row, col) coordinates to values
    
    Attributes:
        width (int): Width of the grid (number of columns)
        height (int): Height of the grid (number of rows)
        grid (Dict[tuple[int, int], Union[str, int]]): Internal grid storage
        
    Example:
        >>> # Create from strings
        >>> grid = Grid.from_strings([
        ...     '123',
        ...     '456'
        ... ], int_vals=True)
        >>> grid[0, 0]  # Access top-left value
        1
        
        >>> # Create from dictionary
        >>> grid = Grid({
        ...     (0, 0): 'A', (0, 1): 'B',
        ...     (1, 0): 'C', (1, 1): 'D'
        ... }, width=2, height=2)
        >>> list(grid.neighbors((0, 0)))  # Get neighboring coordinates
        [(0, 1), (1, 0)]
        
        >>> # Pretty print
        >>> grid.print()
        AB
        CD
    
    Constants:
        CARDINAL_DIRS: List of (dx, dy) offsets for N, W, E, S directions
        DIAGONAL_DIRS: List of (dx, dy) offsets for NW, NE, SW, SE directions
        CENTER: List containing (0, 0) offset for self-reference
    """
    # Class constants for directions
    CARDINAL_DIRS = [
        (-1, 0),          # North (decrease row)
        (0, -1), (0, 1),  # West (decrease col), East (increase col)
        (1, 0),           # South (increase row)
    ]

    DIAGONAL_DIRS = [
        (-1, -1), (-1, 1),  # NW (up-left), NE (up-right)
        (1, -1),  (1, 1),   # SW (down-left), SE (down-right)
    ]

    CENTER = [(0, 0)]

    def __init__(self, 
                 data: Union[Dict[tuple[int, int], str], Dict[tuple[int, int], int], list[str]], 
                 width: Optional[int] = None,
                 height: Optional[int] = None,
                 int_vals: bool = False,
                 ignore_chars: str = ""):
        """Initialize Grid with either a dictionary of coordinates or raw grid strings."""
        if isinstance(data, list):
            self.grid = self._parse_grid(data, int_vals=int_vals, ignore_chars=ignore_chars)
        else:
            self.grid = data
            
        # Auto-detect dimensions if not specified
        if width is None or height is None:
            if not self.grid:
                self.width = 0
                self.height = 0
            else:
                max_row = max(pos[0] for pos in self.grid.keys())
                max_col = max(pos[1] for pos in self.grid.keys())
                self.width = width or (max_col + 1)
                self.height = height or (max_row + 1)
        else:
            self.width = width
            self.height = height

    def _parse_grid(self, 
                   raw_grid: list[str], 
                   *, 
                   int_vals: bool = False, 
                   ignore_chars: str = "") -> Dict[tuple[int, int], Union[str, int]]:
        """Convert a 2D text grid into a dictionary of coordinates and values."""
        grid = {}
        for row, line in enumerate(raw_grid):
            for col, char in enumerate(line):
                if char in ignore_chars:
                    continue
                grid[row, col] = int(char) if int_vals else char
                
        return grid
    
    def copy(self) -> Grid:
        return Grid(dict(self.grid), width=self.width, height=self.height)


    def neighbors(self,
                center: tuple[int, int],
                num_dirs: int = 8,
                ) -> Iterator[tuple[int, int]]:
        """Get neighboring coordinates within grid bounds.
        
        Args:
            center: (row, col) coordinate to find neighbors for
            num_dirs: Number of directions (4, 8, or 9)
            
        Yields:
            Valid neighboring coordinates
        """
        assert num_dirs in {4, 8, 9}

        offsets = self.CARDINAL_DIRS
        if num_dirs >= 8:
            offsets += self.DIAGONAL_DIRS
        if num_dirs == 9:
            offsets += self.CENTER

        row, col = center

        for drow, dcol in offsets:
            next_row, next_col = row + drow, col + dcol

            if next_row < 0 or next_row >= self.height:
                continue
            if next_col < 0 or next_col >= self.width:
                continue

            yield (next_row, next_col)


    def get_neighbor_value(self, 
                        pos: tuple[int, int], 
                        direction: str,
                        default: Union[str, int, None] = None) -> Union[str, int, None]:
        """Get the value of a neighbor in a specified direction.
        
        Args:
            pos: (row, col) coordinate to find neighbor for
            direction: String indicating direction ('N', 'S', 'E', 'W', 'NW', 'NE', 'SW', 'SE')
            default: Value to return if neighbor is out of bounds or not present
            
        Returns:
            Value of the neighbor in specified direction, or default if not found
        """
        direction_map = {
            'N': (-1, 0),    # Up (decrease row)
            'S': (1, 0),     # Down (increase row)
            'W': (0, -1),    # Left (decrease col)
            'E': (0, 1),     # Right (increase col)
            'NW': (-1, -1),  # Up-left
            'NE': (-1, 1),   # Up-right
            'SW': (1, -1),   # Down-left
            'SE': (1, 1)     # Down-right
        }
        
        if direction not in direction_map:
            raise ValueError(f"Invalid direction: {direction}")
            
        drow, dcol = direction_map[direction]
        new_pos = (pos[0] + drow, pos[1] + dcol)
        
        # Check if the position is within bounds
        if (new_pos[0] < 0 or new_pos[0] >= self.height or
            new_pos[1] < 0 or new_pos[1] >= self.width):
            return default
            
        return self.grid.get(new_pos, default)

    def values(self):
        """Get all values in the grid."""
        return self.grid.values()

    def __getitem__(self, pos: tuple[int, int]) -> Union[str, int]:
        return self.grid[pos]
    
    def __setitem__(self, pos: tuple[int, int], value: Union[str, int]):
        self.grid[pos] = value
    
    def __contains__(self, pos: tuple[int, int]) -> bool:
        return pos in self.grid
    
    def __iter__(self):
        return iter(self.grid.items())
    

    def find_first(self, target: Union[str, int]) -> tuple[int, int] | None:
        """Find the first occurrence of a value in the grid."""
        try:
            return next(pos for pos, val in self.grid.items() if val == target)
        except StopIteration:
            return None

    def find_all(self, target: Union[str, int]) -> list[tuple[int, int]]:
        """Find all occurrences of a value in the grid."""
        return [pos for pos, val in self.grid.items() if val == target]

    def print(self, empty_char: str = ".", cell_width: int = 1) -> None:
        """Pretty print the grid."""
        for row in range(self.height):
            row_chars = []
            for col in range(self.width):
                value = self.grid.get((row, col), empty_char)
                row_chars.append(str(value).rjust(cell_width))
            print("".join(row_chars))

    @classmethod
    def from_strings(cls, 
                    raw_grid: list[str], 
                    int_vals: bool = False,
                    ignore_chars: str = "") -> Grid:
        """Create Grid from list of strings."""
        return cls(raw_grid, int_vals=int_vals, ignore_chars=ignore_chars)