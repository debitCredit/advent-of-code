import re
import os
import sys
import functools
from collections import defaultdict
from collections import Counter


file = os.path.join(sys.path[0], "input.txt")
# file = os.path.join(sys.path[0], "test_input.txt")

ll = [[[int(i) for i in y.split("-")] for y in x.split(",")] for x in open(file).read().strip().split('\n')]

c = 0

for l in ll:
    first_elf = set(range(l[0][0], l[0][1]+1))
    second_elf = set(range(l[1][0], l[1][1]+1))
    if first_elf <=second_elf or second_elf <= first_elf:
        c += 1

print(c)