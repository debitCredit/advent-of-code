import numpy as np

with open('input.txt') as f:
    draw = list(f.readline().strip().split(","))


a = np.zeros((5, 5), dtype=int)

# Processing the file to create a list of boards in np arrays