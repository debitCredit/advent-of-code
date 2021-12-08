from functools import reduce
from operator import concat


file = "input.txt"
# file = "test_input.txt"

with open(file) as f:
    input_data = f.read()

entry = list(input_data.splitlines())

patterns_pre = [e.split("|")[0] for e in entry]
patterns_post = [l.strip().split() for l in patterns_pre]

digi_pre = [e.split("|")[1] for e in entry]
digi_post = [l.strip().split() for l in digi_pre]

lens = [[len(text) for text in group] for group in digi_post]
flat = reduce(concat, lens)

count = 0
for i in flat:
    if i in [2, 4, 3, 7]:
        count += 1

print(count)

# Unique values based on the length:
# 1 = 2
# 4 = 4
# 7 = 3
# 8 = 7
