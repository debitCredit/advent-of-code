import re
import numpy as np

with open('input.txt') as f:
    input_data = f.read()

raw_lines = list(input_data.splitlines())


def process_input(lst: list) -> list:
    lines = []
    for l in lst:
        x0, y0, x1, y1 = re.findall(r"[0-9]+", l)
        lines.append([(int(x0), int(y0)), (int(x1), int(y1))])
    return lines


def calc_lines(p1: tuple, p2: tuple) -> list:
    # rearrange p1, p2 to allow simplified calc
    if not (p2[0] > p1[0] or p2[1] > p1[1]):
        p1, p2 = p2, p1

    px = p2[0] - p1[0]
    py = p2[1] - p1[1]
    points = []
    if px != 0:
        for i in range(p1[0], p2[0]+1):
            points.append((i, p2[1]))
    if py != 0:
        for i in range(p1[1], p2[1]+1):
            points.append((p1[0], i))
    return points


def filter_the_list(lst: list) -> list:
    filtered_list = []
    for i in lst:
        x0, y0, x1, y1 = *i[0], *i[1]
        if x0 == x1 or y0 == y1:
            filtered_list.append(i)
    return filtered_list


def populate_array(p: tuple, arr: np.ndarray) -> np.ndarray:
    arr[p[1], p[0]] += 1
    return arr


diag = np.zeros((1000, 1000), dtype=int)

data_pre_processing = process_input(raw_lines)
data_post_processing = filter_the_list(data_pre_processing)

print(f"{data_post_processing=}")

for i in data_post_processing:
    l = calc_lines(i[0], i[1])
    for z in l:
        diag = populate_array(z, diag)

print(diag)
print(np.sum(diag >= 2))
