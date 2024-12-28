import re

# file = "test_input.txt"
file = "input.txt"

with open(file) as f:
  text= f.read()

pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
number_pairs = re.findall(pattern, text)
number_pairs = [(int(x), int(y)) for x, y in number_pairs]

print(sum(pair[0] * pair[1] for pair in number_pairs))
