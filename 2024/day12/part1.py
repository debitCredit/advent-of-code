from utils.utils import neighbors, parse_grid, GridPoint, Grid

# file = "test_input.txt"
file = "input.txt"

with open(file) as f:
  grid = parse_grid(f.read().splitlines())


def find_regions(grid: Grid) -> list[set[GridPoint]]:
    regions = []
    visited = set()
    
    def flood_fill(start: GridPoint) -> set[GridPoint]:
        region = set()
        value = grid[start]
        stack = [start]
        
        while stack:
            curr = stack.pop()
            if curr not in region:
                region.add(curr)
                stack.extend(
                    n for n in neighbors(curr, num_dirs=4)
                    if grid.get(n) == value and n not in region
                )
        return region

    for point in grid:
        if point not in visited:
            region = flood_fill(point)
            visited |= region
            regions.append(region)
            
    return regions


def determine_perimiter(point: GridPoint) -> int:
  return 4 - sum(1 for n in neighbors(center=point, num_dirs=4) if grid.get(n) == grid.get(point))


regions = find_regions(grid)

total = 0
for region in regions:
  perimeter = 0
  for point in region:
    perimeter += determine_perimiter(point)
  total += perimeter * len(region)

print(total)
