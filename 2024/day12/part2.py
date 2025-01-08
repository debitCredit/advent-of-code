from typing import Set, List, Tuple

from utils.utils import Grid

# file = "test_input.txt"
file = "input.txt"

with open(file) as f:
    grid = Grid.from_strings(f.read().splitlines())


def find_regions(grid: Grid) -> List[Set[Tuple[int, int]]]:
    regions = []
    visited = set()
    
    def flood_fill(start: Tuple[int, int]) -> Set[Tuple[int, int]]:
        region = set()
        value = grid[start]
        stack = [start]
        
        while stack:
            curr = stack.pop()
            if curr not in region:
                region.add(curr)
                stack.extend(
                    n for n in grid.neighbors(curr, num_dirs=4)
                    if n in grid and grid[n] == value and n not in region
                )
        return region

    for point in grid.grid:
        if point not in visited:
            region = flood_fill(point)
            visited |= region
            regions.append(region)
            
    return regions


def determine_perimeter(grid: Grid, point: Tuple[int, int]) -> int:
    return 4 - sum(1 for n in grid.neighbors(point, num_dirs=4) 
                  if n in grid and grid[n] == grid[point])


def determine_sides(point: Tuple[int, int], grid: Grid) -> int:
    corners = 0
    current = grid[point]
    
    # Check each diagonal direction for possible corners
    for dx, dy in grid.DIAGONAL_DIRS:
        diagonal_pos = (point[0] + dx, point[1] + dy)
        
        # Get the two edges adjacent to this diagonal
        edge1_pos = (point[0] + dx, point[1])  # horizontal neighbor
        edge2_pos = (point[0], point[1] + dy)  # vertical neighbor
        
        # Use in grid check instead of get()
        diagonal_val = grid[diagonal_pos] if diagonal_pos in grid else None
        edge1_val = grid[edge1_pos] if edge1_pos in grid else None
        edge2_val = grid[edge2_pos] if edge2_pos in grid else None
        
        # Inner corner: two edges are different
        if edge1_val != current and edge2_val != current:
            corners += 1
        # Outer corner: edges same but diagonal different
        elif edge1_val == current and edge2_val == current and diagonal_val != current:
            corners += 1
            
    return corners


regions = find_regions(grid)

total = 0
for region in regions:
    sides = 0
    for point in region:
        sides += determine_sides(point, grid)
    total += sides * len(region)

print(total)