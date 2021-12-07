import numpy as np

file = "input.txt"
# file = "test_input.txt"

with open(file) as f:
    data = list(map(int, next(f).strip().split(",")))


def min_cost(d: list) -> int:
    data.sort()
    median_crab = int(np.median(data))
    cost = 0
    len_data = len(data)
    for i in range(len_data):
        cost += abs(data[i] - median_crab)
    return cost


print(f"Part 1: {min_cost(data)}")
