import re

file = "test_input.txt"
# file = "input.txt"

with open(file) as f:
    text = f"do(){f.read()}don't()"

total = sum(
    int(x) * int(y) 
    for section in re.findall(r"do\(\)(.*?)don't\(\)", text, re.DOTALL)
    for x, y in re.findall(r'mul\((\d+),(\d+)\)', section)
)

print(total)