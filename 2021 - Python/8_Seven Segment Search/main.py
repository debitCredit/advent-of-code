from functools import reduce
from operator import concat
import re


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


def count_shared(s1, s2):
    counter = 0
    if s1 is None:
        return 0
    for c in s1:
        if re.search(c, s2):
            counter += 1
    return counter


output_matching = []
for c in patterns_post:
    matching = dict.fromkeys(range(0, 10))
    for x in range(3):
        for i in c:
            if len(i) == 2:
                matching[1] = "".join(sorted(i))
            elif len(i) == 4:
                matching[4] = "".join(sorted(i))
            elif len(i) == 3:
                matching[7] = "".join(sorted(i))
            elif len(i) == 7:
                matching[8] = "".join(sorted(i))
            elif len(i) == 5 and count_shared(matching.get(7), i) == 3:
                matching[3] = "".join(sorted(i))
            elif len(i) == 6 and count_shared(matching.get(3), i) == 5:
                matching[9] = "".join(sorted(i))
            elif len(i) == 6 and count_shared(matching.get(7), i) == 3:
                matching[0] = "".join(sorted(i))
            elif len(i) == 6 and count_shared(matching.get(7), i) == 2:
                matching[6] = "".join(sorted(i))
            elif len(i) == 5 and count_shared(matching.get(4), i) == 3:
                matching[5] = "".join(sorted(i))
            elif len(i) == 5 and count_shared(matching.get(4), i) == 2:
                matching[2] = "".join(sorted(i))
    output_matching.append({value:key for key, value in matching.items()})

# TODO: To be fixed
count = []
for o, d in zip(output_matching, digi_post):
    for x in d:
        count.append(o.get("".join(sorted(x))))

pre_final_list = [count[i:i+4] for i in range(0, len(count), 4)]

almost = [["".join(str(i) for i in x)] for x in pre_final_list]
final_count = 0

for i in almost:
    final_count += int(*i)
print(final_count)
