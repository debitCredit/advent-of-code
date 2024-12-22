import numpy as np

file = "input.txt"
# file = "test_input.txt"
result = []
sum = 0

data = np.genfromtxt(file, dtype=int, delimiter=1)
it = np.nditer(data, flags=['multi_index'])


def get_next_cell(pos: tuple, matrix=data):
    x = pos[1]
    y = pos[0]
    value = matrix[y][x]
    next_cell = pos
    # up
    if y >= 1 and value >= matrix[y-1][x]:
        value = matrix[y-1][x]
        next_cell = (y-1, x)
    # left
    if x >= 1 and value >= matrix[y][x-1]:
        value = matrix[y][x-1]
        next_cell = (y, x-1)
    # right
    if x < matrix.shape[1]-1 and value >= matrix[y][x+1]:
        value = matrix[y][x+1]
        next_cell = (y, x+1)
    # down
    if y < matrix.shape[0]-1 and value >= matrix[y+1][x]:
        # value = matrix[y+1][x]
        next_cell = (y+1, x)
    return next_cell


def find_local_min(pos):
    next_cell = get_next_cell(pos)
    if next_cell == pos:
        return pos
    else:
        return find_local_min(next_cell)


for e in it:
    result.append(find_local_min(it.multi_index))

result = set(result)

for t in result:
    sum += data[t[0]][t[1]] + 1

print(f"Part 1: {sum}")
