import re
import os
import sys
import functools
from collections import defaultdict
from collections import Counter


file = os.path.join(sys.path[0], "input.txt")
# file = os.path.join(sys.path[0], "test_input.txt")

ll = [x for x in open(file).read().strip().split('\n')]

print(ll)

c = 0

# for i in range(len(ll)):

# for i in range(len(ll)-1):

# for l in ll:

print(c)