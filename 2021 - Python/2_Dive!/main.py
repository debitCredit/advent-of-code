a = {}
with open('input.txt', 'r') as f:
    input_data = f.read()
    a = input_data.splitlines()

forward, depth = 0, 0

for i in a:
    c, v = i.split()
    if c == "forward":
        forward += int(v)
    elif c == "down":
        depth += int(v)
    elif c == "up":
        depth -= int(v)

print(forward * depth)  # 1938402
