with open('input.txt', 'r') as f:
    input_data = f.read()
    a = input_data.splitlines()

horizontal, depth, aim = 0, 0, 0

# Part 1
for i in a:
    c, v = i.split()
    if c == "forward":
        horizontal += int(v)
    elif c == "down":
        depth += int(v)
    elif c == "up":
        depth -= int(v)

print(horizontal * depth)  # 1938402

# Part 2 (uncomment to run)

# for i in a:
#     c, v = i.split()
#     if c == "forward":
#         horizontal += int(v)
#         depth += (int(v) * aim)
#     elif c == "down":
#         aim += int(v)
#     elif c == "up":
#         aim -= int(v)
#
# print(horizontal * depth)  # 1947878632
