import numpy as np
import numpy.ma as ma

boards = []
with open('input.txt') as f:
    draw = list(next(f).strip().split(","))
    counter = 0
    for line in f:
        if not line == "\n" and counter == 0:
            a = np.array(list(map(int, line.split())))
            counter += 1
        elif not line == "\n" and counter < 4:
            a = np.vstack((a, np.array(list(map(int, line.split())))))
            counter += 1
        elif not line == "\n" and counter == 4:
            a = np.vstack((a, np.array(list(map(int, line.split())))))
            boards.append(a)
            counter += 1
        else:
            counter = 0

print(boards)
