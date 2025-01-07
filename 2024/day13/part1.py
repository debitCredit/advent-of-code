import re

# file = "test_input.txt"
file = "input.txt"

with open(file) as f:
  text = f.read()


def parse_coordinates(text):
    pattern = r'Button A: X\+(\d+), Y\+(\d+)[\r\n]+Button B: X\+(\d+), Y\+(\d+)[\r\n]+Prize: X=(\d+), Y=(\d+)'
    matches = list(re.finditer(pattern, text))
  
    return [tuple(map(int, match.groups())) for match in matches]


def find_intersection(
      a_x: int, 
      a_y: int, 
      b_x: int, 
      b_y: int, 
      x_prize: int, 
      y_prize: int
    ) -> tuple[float, float]:
    """Solves the system of linear equations:
    a_x * a + b_x * b = x_prize
    a_y * a + b_y * b = y_prize
    """
    # Solve for 'a' using substitution method
    a = (x_prize * b_y - y_prize * b_x) / (a_x * b_y - a_y * b_x)
    
    # Solve for 'b' using the second equation
    b = (y_prize - a_y * a) / b_y
    
    return a, b



total = 0
machines = parse_coordinates(text)

for machine in machines:
   a, b = find_intersection(*machine)
   if not (a.is_integer() and b.is_integer()):
      continue
   total += 3 * a + b

print(int(total))