file = "input.txt"

with open(file) as f:
    data = list(map(int, next(f).strip().split(",")))


def process_fish(data: list, days: int) -> int:
    fish = [data.count(i) for i in range(9)]
    for i in range(days):
        n = fish.pop(0)
        fish[6] += n
        fish.append(n)
    return sum(fish)


print(f"Part 1: {process_fish(data, 80)}")
print(f"Part 1: {process_fish(data, 256)}")
