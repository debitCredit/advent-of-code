import numpy as np

file = "input.txt"
# file = "test_input.txt"

with open(file) as f:
    input_data = f.read()

entry = list(input_data.splitlines())

stack = []
opposites = {")": "(", "]": "[", ">": "<", "}": "{"}
score_list = {")": 3, "]": 57, "}": 1197, ">": 25137}
score_list2 = {"(": 1, "[": 2, "{": 3, "<": 4}
total = 0
scores = []
count = 0
# Part 1
# for line in entry:
#     for i in line:
#         if i in '([{<':
#             stack.append(i)
#         elif stack.pop() != opposites[i]:
#             total += score_list[i]

# Part 2

for line in entry:
    for i in line:
        if i in '([{<':
            stack.append(i)
        elif stack.pop() != opposites[i]:
            stack = []
            break
    else:
        score = 0
        while stack:
            score = score * 5 + score_list2[stack.pop()]
        scores.append(score)
        continue

print(int(np.median(scores)))

