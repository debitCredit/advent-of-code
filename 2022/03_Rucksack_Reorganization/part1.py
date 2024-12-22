import re
import os
import sys
import functools
import string
from collections import defaultdict
from collections import Counter


file = os.path.join(sys.path[0], "input.txt")
# file = os.path.join(sys.path[0], "test_input.txt")

ll = [x for x in open(file).read().strip().split('\n')]

c = 0

def split_list(l: list):
    middle_index = len(l) // 2
    return [l[:middle_index], l[middle_index:]]

for l in ll:
    b = set(split_list(l)[0]) & set(split_list(l)[1])
    c += string.ascii_letters.index(*b) + 1

print(c)