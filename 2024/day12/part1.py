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

    for point in grid.grid:  # iterate over points in the internal dictionary
        if point not in visited:
            region = flood_fill(point)
            visited |= region
            regions.append(region)
            
    return regions


def determine_perimeter(grid: Grid, point: Tuple[int, int]) -> int:
    return 4 - sum(1 for n in grid.neighbors(point, num_dirs=4) 
                  if n in grid and grid[n] == grid[point])


regions = find_regions(grid)

total = 0
for region in regions:
    perimeter = 0
    for point in region:
        perimeter += determine_perimeter(grid, point)
    total += perimeter * len(region)

print(total)