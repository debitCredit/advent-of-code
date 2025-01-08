import re
from math import prod

WIDTH = 101
HEIGHT = 103

# file = "test_input.txt"
file = "input.txt"


with open(file) as f:
  text = f.read()

def parse_robots(text):
  pattern = r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)'
  matches = list(re.finditer(pattern, text))

  return [tuple(map(int, match.groups())) for match in matches]


def sim_pos(x: int, 
                       y: int, 
                       dx: int, 
                       dy: int,
                       ticks: int, 
    ) -> tuple[int, int]:
  
  # Final position sim & wrap around
  return (x + dx * ticks) % WIDTH, (y + dy * ticks) % HEIGHT


def append_grid_to_file(positions, filename, iteration: int, width=101, height=103):
    grid_counts = {}
    for pos in positions:
        grid_counts[pos] = grid_counts.get(pos, 0) + 1
    
    with open(filename, 'a') as f:
        f.write(f"{iteration} \n")
        for y in range(height):
            row = []
            for x in range(width):
                count = grid_counts.get((x, y), 0)
                row.append(str(count) if count > 0 else '.')
            f.write(''.join(row) + '\n')
        f.write('\n')
  

robots = parse_robots(text)

for i in range(10000):
   final_pos = [sim_pos(*robot, ticks=i) for robot in robots]
   
   append_grid_to_file(final_pos, "grid_output.txt", iteration=i)
