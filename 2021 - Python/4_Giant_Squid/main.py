import numpy as np

boards = []
with open('input.txt') as f:
    draw = list(map(int, next(f).strip().split(",")))
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


def check_if_won(arr: np.ndarray) -> bool:
    for q in arr:
        if np.all(q):
            return True
    for e in range(5):
        if np.all(arr[:, e]):
            return True
    if np.all(arr.diagonal()) or np.all(np.fliplr(arr).diagonal()):
        return True
    return False


def process_boards(draw: list, boards: list) -> tuple:
    scores = {}
    scores_so_far = []
    for d in draw:
        scores_so_far.append(d)
        for i in range(len(boards)):
            scores[d] = np.asarray(np.in1d(boards[i], scores_so_far)).reshape((5, 5))
            if check_if_won(scores[d]):
                return d, scores[d], i


def process_board(draw: list, board: np.ndarray) -> tuple:
    scores = {}
    scores_so_far = []
    for d in draw:
        scores_so_far.append(d)
        scores[d] = np.asarray(np.in1d(board, scores_so_far)).reshape((5, 5))
        if check_if_won(scores[d]):
            return d, scores[d]


d, m, b = process_boards(draw, boards)
sum_of_false = 0

for j in range(5):
    for i in range(5):
        if not m[j][i]:
            sum_of_false += boards[b][j][i]

print(f"Part 1: {sum_of_false * d}")  # 21607


def process_boards_last(draw: list, boards: list) -> dict:
    scores = {}
    scores_so_far = []
    for b in range(len(boards)):
        for d in draw:
            scores_so_far.append(d)
            h = np.asarray(np.in1d(boards[b], scores_so_far)).reshape((5, 5))
            if check_if_won(h):
                scores[b] = len(scores_so_far)
                break
        scores_so_far.clear()
    return scores


dyt = dict(sorted(process_boards_last(draw, boards).items(), key=lambda item: item[1], reverse=True))

final_board = next(iter(dyt.items()))[0]
final_guess = draw[next(iter(dyt.items()))[1]-1]
pb = process_board(draw, boards[final_board])[1]

sum_of_false = 0
for j in range(5):
    for i in range(5):
        if not pb[j][i]:
            sum_of_false += boards[final_board][j][i]
print(f"Part 2: {sum_of_false * final_guess}")
