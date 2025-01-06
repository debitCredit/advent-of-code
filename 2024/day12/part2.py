from utils.utils import neighbors, parse_grid, GridPoint, Grid, DIAGONAL_DIRS

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


def determine_sides(point: GridPoint, grid: Grid) -> int:
    corners = 0
    current = grid[point]
    
    # Check each diagonal direction for possible corners
    for dx, dy in DIAGONAL_DIRS:
        diagonal_pos = (point[0] + dx, point[1] + dy)
        
        # Get the two edges adjacent to this diagonal
        edge1_pos = (point[0] + dx, point[1])  # horizontal neighbor
        edge2_pos = (point[0], point[1] + dy)  # vertical neighbor
        
        diagonal_val = grid.get(diagonal_pos)
        edge1_val = grid.get(edge1_pos)
        edge2_val = grid.get(edge2_pos)
        
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
