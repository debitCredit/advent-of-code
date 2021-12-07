import scipy

file = "input.txt"

with open(file) as f:
    data = list(map(int, next(f).strip().split(",")))
