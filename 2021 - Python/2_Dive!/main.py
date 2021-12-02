a = {}
with open('input.txt', 'r') as f:
    input_data = f.read()
    a = input_data.splitlines()

horizontal, depth, aim = 0, 0, 0

# for i in a:
#     c, v = i.split()
#     if c == "forward":
#         forward += int(v)
#     elif c == "down":
#         depth += int(v)
#     elif c == "up":
#         depth -= int(v)

# print(forward * depth)  # 1938402

# TODO: Submission fails - to be debugged.
for i in a:
    c, v = i.split()
    if c == "forward":
        horizontal += int(v)
        depth += (depth * aim)
        print(f"{aim=}, {depth=}, {horizontal=}")
    elif c == "down":
        aim += int(v)
    elif c == "up":
        aim -= int(v)

print(horizontal * depth)