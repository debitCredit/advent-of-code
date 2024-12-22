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

# Generator to yield 3 items from a list at a time.
def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

chunked = list(chunks(ll, 3))

for l in chunked:
    c += string.ascii_letters.index(*set.intersection(*map(set, l))) + 1 

print(c)