file = "input.txt"
# file = "test_input.txt"

with open(file) as f:
    input_data = f.read()

entry = list(input_data.splitlines())

stack = []
opposites = {")": "(", "]": "[", ">": "<", "}": "{"}
score_list = {")": 3, "]": 57, "}": 1197, ">": 25137}
total = 0

# Part 1
for line in entry:
    for i in line:

        if i in '([{<':
            stack.append(i)
        elif stack.pop() != opposites[i]:
            total += score_list[i]

print(total)
