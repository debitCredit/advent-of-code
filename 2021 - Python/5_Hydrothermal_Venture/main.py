import numpy as np

diag = np.zeros((1000, 1000), dtype=int)
test_diag = np.zeros((10, 10), dtype=int)


def calc_lines(p1: tuple, p2: tuple) -> list:
    # rearrange p1, p2 to allow simplified calc
    if not (p2[0] > p1[0] or p2[1] > p1[1]):
        p1, p2 = p2, p1

    px = p2[0] - p1[0]
    py = p2[1] - p1[1]
    points = []
    # print(f"{px=}")
    # print(f"{py=}")
    # print(f"{p2[0]=}")
    # print(f"{p2[1]=}")
    # print(f"{p1[0]=}")
    # print(f"{p1[1]=}")
    if px != 0:
        for i in range(p1[0], p2[0]+1):
            points.append((i, p2[1]))
    if py != 0:
        for i in range(p1[1], p2[1]+1):
            points.append((p1[0], i))
    return points




def populate_array(p1: tuple, p2: tuple, arr: np.ndarray) -> np.ndarray:
    pass



