import statistics

file = "input.txt"

with open(file) as f:
    data = list(map(int, next(f).strip().split(",")))

median, mean = int(statistics.median(data)), int(statistics.mean(data))

print(f"Part 1: {sum(abs(c - median) for c in data)}")

gauss = lambda v: v * (v + 1) // 2

print(f"Part 2: {sum(gauss(abs(c - mean)) for c in data)}")
