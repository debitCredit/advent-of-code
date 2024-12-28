# file = "test_input.txt"
file = "input.txt"

reports = []
with open(file) as f:
  for line in f:
    reports.append(list(map(int, line.split())))

def is_safe(row):
  inc = {row[i + 1] - row[i] for i in range(len(row) - 1)}
  return inc.issubset({1, 2, 3}) or inc.issubset({-1, -2, -3})
    
part2_count = sum([any([is_safe(row[:i] + row[i + 1:]) for i in range(len(row))]) for row in reports])
print(part2_count)