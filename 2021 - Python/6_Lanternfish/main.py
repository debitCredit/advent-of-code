import numpy as np

file = "input.txt"
days = 80
# file = "test_input.txt"
# days = 18

with open(file) as f:
    fish = np.array(list(map(int, next(f).strip().split(","))))


def process_day(fish: np.array, days=days) -> np.ndarray:
    for d in range(days):
        new_fish_count = np.sum(fish == 0)
        fish[fish == 0] = 10
        fish = np.where(fish == 0, fish, fish - 1)
        fish[fish == 9] = 6
        fish = np.append(fish, np.repeat(8, new_fish_count))
    return fish


answer1 = print(f"Part 1: {process_day(fish).size}")


