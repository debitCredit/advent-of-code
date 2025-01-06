from utils.utils import neighbors, parse_grid, GridPoint, Grid

# file = "test_input.txt"
file = "input.txt"

with open(file) as f:
  grid = parse_grid(f.read().splitlines())


def find_regions(grid: Grid) -> list[set[GridPoint]]:
  regions: list[set[GridPoint]] = []
  visited: set[GridPoint] = set()

  for point in grid:
    if point in visited:
      continue
    
    # Identified new region
    region = set()
    stack = [point]

    while stack:
      curr = stack.pop()
      if curr in region:
        continue

      region.add(curr)
      curr_value = grid[curr]

      stack.extend(
          n for n in neighbors(center=curr, num_dirs=4)
          if grid.get(n) == curr_value and n not in region
      )

    visited |= region
    regions.append(region)

  return regions


def determine_perimiter(point: GridPoint) -> int:
  return 4 - len([n for n in neighbors(center=point, num_dirs=4) if grid.get(n) == grid.get(point)])


regions = find_regions(grid)

total = 0
for region in regions:
  perimeter = 0
  for point in region:
    perimeter += determine_perimiter(point)
  total += perimeter * len(region)

print(total)
