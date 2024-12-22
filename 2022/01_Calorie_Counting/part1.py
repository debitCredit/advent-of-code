import os
import sys
from collections import defaultdict


file = os.path.join(sys.path[0], "input.txt")
# file = os.path.join(sys.path[0], "test_input.txt")

ll = [[int(y) for y in x.split('\n')] for x in open(file).read().strip().split('\n\n')]

print(max(sum(x) for x in ll))