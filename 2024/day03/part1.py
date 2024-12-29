import re

file = "test_input.txt"
# file = "input.txt"

with open(file) as f:
    text = f.read()

total = sum(
    int(x) * int(y) 
    for x, y in re.findall(r'mul\((\d+),(\d+)\)', text)
)

print(total)