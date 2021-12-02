with open('input.txt', 'r') as f:
    input_data = f.read()
    a = input_data.splitlines()

horizontal, depth, aim = 0, 0, 0

for i in a:
    c, v = i.split()
    if c == "forward":
        horizontal += int(v)
        depth += (int(v) * aim)
    elif c == "down":
        aim += int(v)
    elif c == "up":
        aim -= int(v)

print(horizontal * aim, horizontal * depth)
