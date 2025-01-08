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


def get_quadrant(x: int, y: int) -> int:
    
    if x == WIDTH // 2 or y == HEIGHT // 2:
      return None
    
    left_half = x < WIDTH // 2
    top_half = y < HEIGHT // 2
    
    if top_half:
        return 1 if left_half else 2
    return 3 if left_half else 4

robots = parse_robots(text)
final_pos = [sim_pos(*robot, ticks=100) for robot in robots]
counts = [sum(1 for x, y in final_pos if get_quadrant(x, y) == q) for q in range(1, 5)]

print(prod(counts))